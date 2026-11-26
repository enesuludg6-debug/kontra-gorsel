#!/usr/bin/env python3
"""kagit_bot.py — sanal (kağıt) işlem botu = ileriye dönük gerçek test (Enes 26.11 08:21: "bot eksiği").
GERÇEK EMİR GÖNDERMEZ. Kurallar backtest.py ile aynı; böylece backtest sonucu canlıda tutuyor mu ölçülür.
Strateji varsayılanı: kanıtı ÜSTÜN çıkan taramalar (tarama_kanit.json) -> dip_avcisi, derin_dip; evren 'hepsi' (122 hisse).
Kurallar: sinyal günün kapanışında -> giriş ERTESİ işlem günü açılışında; stop 2 ATR, hedef 4 ATR, en çok 15 işlem günü;
en çok 5 açık pozisyon, her biri sermayenin %20'si; başlangıç 100.000 sanal dolar; maliyet %0,1 gidiş-dönüş.
Kullanım:
  python3 invest/kagit_bot.py calis      (her sabah 09:00 görevi; borsa kapalı gün/hafta sonu da güvenli: yeni mum yoksa işlem yapmaz)
  python3 invest/kagit_bot.py durum      açık pozisyonlar, kapananlar, sermaye eğrisi, backtest beklentisiyle kıyas
  python3 invest/kagit_bot.py sifirla
"""
import sys, os, json, datetime as dt
import numpy as np, pandas as pd
from gosterge import veri, hesapla, degerlendir

YOL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "kagit_bot.json")
KYOL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tarama_kanit.json")
BAS = 100000.0; MAKS = 5; PAY = 0.20; STOP, HEDEF, SURE, MAL = 2.0, 4.0, 15, 0.1

def yukle():
    if os.path.exists(YOL): return json.load(open(YOL))
    return {"nakit": BAS, "acik": [], "bekleyen": [], "kapanan": [], "son_mum": None, "egri": []}

def stratejiler():
    from tarama import HAZIR
    K = json.load(open(KYOL)) if os.path.exists(KYOL) else {}
    sec = [k for k, v in K.items() if v.get("hukum") == "ÜSTÜN" and k in HAZIR] or ["dip_avcisi", "derin_dip"]
    return {k: HAZIR[k][1] for k in sec}

def calis():
    from tarama import evren
    S = yukle(); ref = veri("QQQ", "5y"); X = {}
    def x_(t):
        if t not in X: X[t] = hesapla(veri(t, "5y", ttl=3 * 3600), ref)
        return X[t]
    son_mum = str(x_("AVGO").index[-1].date())
    if S["son_mum"] == son_mum: print(f"yeni mum yok ({son_mum}); işlem yapılmadı"); return durum(S)
    gunluk = []
    # 1) bekleyen emirleri bugünün açılışından doldur
    for b in S["bekleyen"]:
        x = x_(b["t"]); gun = x[x.index > pd.Timestamp(b["sinyal_tarih"])]
        if gun.empty: continue
        r = gun.iloc[0]; adet = int(S["nakit"] * 0 + b["tutar"] // r.acilis)
        if adet <= 0 or len(S["acik"]) >= MAKS: continue
        S["nakit"] -= adet * r.acilis * (1 + MAL / 200)
        S["acik"].append({"t": b["t"], "strateji": b["strateji"], "giris_tarih": str(gun.index[0].date()), "giris": r.acilis, "adet": adet,
                          "stop": r.acilis - STOP * b["atr"], "hedef": r.acilis + HEDEF * b["atr"]})
        gunluk.append(f"ALIŞ (sanal) {b['t']} {adet} adet @ {r.acilis:,.2f} [{b['strateji']}]")
    S["bekleyen"] = []
    # 2) açık pozisyonları ilerlet: stop/hedef/süre (giriş gününden sonraki her mumda)
    kalan = []
    for p in S["acik"]:
        x = x_(p["t"]); gun = x[x.index >= pd.Timestamp(p["giris_tarih"])]; cik = None
        for i, (ts, r) in enumerate(gun.iterrows()):
            if r.dusuk <= p["stop"]: cik, neden = min(r.acilis, p["stop"]), "stop"
            elif r.yuksek >= p["hedef"]: cik, neden = max(r.acilis, p["hedef"]), "hedef"
            elif i + 1 >= SURE: cik, neden = r.kapanis, "süre"
            if cik is not None: cik_t = str(ts.date()); break
        if cik is None: kalan.append(p); continue
        S["nakit"] += p["adet"] * cik * (1 - MAL / 200); g = (cik / p["giris"] - 1) * 100 - MAL
        S["kapanan"].append({**p, "cikis": cik, "cikis_tarih": cik_t, "neden": neden, "getiri": g})
        gunluk.append(f"SATIŞ (sanal) {p['t']} @ {cik:,.2f} {neden}, {g:+.1f}%")
    S["acik"] = kalan
    # 3) yeni sinyaller (bugünün kapanışı) -> yarın açılışta giriş
    bos = MAKS - len(S["acik"]); sinyal = []
    if bos > 0:
        for ad, ifade in stratejiler().items():
            for t in evren("hepsi"):
                if any(p["t"] == t for p in S["acik"]): continue
                try:
                    x = x_(t)
                    if len(x) > 220 and degerlendir(x, ifade).iloc[-1]: sinyal.append((x.rsi.iloc[-1], t, ad, x.atr.iloc[-1]))
                except Exception: pass
        sinyal.sort()
        ozsermaye = S["nakit"] + sum(p["adet"] * x_(p["t"]).kapanis.iloc[-1] for p in S["acik"])
        for _, t, ad, atr in sinyal[:bos]:
            S["bekleyen"].append({"t": t, "strateji": ad, "sinyal_tarih": son_mum, "atr": atr, "tutar": ozsermaye * PAY})
            gunluk.append(f"SİNYAL {t} [{ad}] -> sonraki açılışta sanal alış")
    oz = S["nakit"] + sum(p["adet"] * x_(p["t"]).kapanis.iloc[-1] for p in S["acik"])
    S["egri"].append({"tarih": son_mum, "ozsermaye": round(oz, 2)}); S["son_mum"] = son_mum
    json.dump(S, open(YOL, "w"), ensure_ascii=False, indent=1, default=float)
    print("\n".join(gunluk) if gunluk else "işlem yok"); durum(S)

def durum(S=None):
    S = S or yukle(); oz = S["egri"][-1]["ozsermaye"] if S["egri"] else BAS
    print(f"\nKAĞIT BOT: öz sermaye {oz:,.0f} sanal $ ({(oz / BAS - 1) * 100:+.2f}%), nakit {S['nakit']:,.0f}, açık {len(S['acik'])}/{MAKS}, bekleyen {len(S['bekleyen'])}")
    for p in S["acik"]: print(f"   AÇIK {p['t']:<6} {p['giris_tarih']} @ {p['giris']:,.2f}  stop {p['stop']:,.2f}  hedef {p['hedef']:,.2f}  [{p['strateji']}]")
    for b in S["bekleyen"]: print(f"   BEKLEYEN {b['t']} [{b['strateji']}] sinyal {b['sinyal_tarih']}")
    if S["kapanan"]:
        g = np.array([k["getiri"] for k in S["kapanan"]])
        print(f"   kapanan {len(g)} işlem: kazanma %{(g > 0).mean() * 100:.0f}, ortalama {g.mean():+.2f}%")
        K = json.load(open(KYOL)) if os.path.exists(KYOL) else {}
        for ad in set(k["strateji"] for k in S["kapanan"]):
            gg = [k["getiri"] for k in S["kapanan"] if k["strateji"] == ad]
            if ad in K: print(f"   {ad}: canlı ort {np.mean(gg):+.2f}% ({len(gg)} işlem) vs backtest {K[ad]['ort']:+.2f}% / rastgele {K[ad]['taban_ort']:+.2f}%")
        if len(g) < 30: print("   (30 işlemden az: henüz hüküm verilmez)")

if __name__ == "__main__":
    a = sys.argv[1:] or ["durum"]
    if a[0] == "calis": calis()
    elif a[0] == "sifirla": os.path.exists(YOL) and os.remove(YOL); print("sıfırlandı")
    else: durum()

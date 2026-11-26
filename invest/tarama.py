#!/usr/bin/env python3
"""tarama.py — gelişmiş tarayıcı + dinamik izleme listesi (Enes 26.11 07:55 "İsviçre çakısı").
Kullanım:
  python3 invest/tarama.py hazir                         hazır taramaları listele
  python3 invest/tarama.py <hazır_ad> [--evren portfoy|ndx|hepsi|A,B,C] [--n 15]
  python3 invest/tarama.py "rsi<35 ve uz200>-1 ve hacim_oran>1.5" [--evren ...] [--sirala rs20]
  python3 invest/tarama.py izle                          tüm hazır taramaları çalıştırıp dinamik listeyi günceller
  python3 invest/tarama.py liste                         dinamik liste + girişten beri getiri (ileriye dönük karne)
Her eşleşmede: hangi şartlar sağlandı, kalite puanı (0-100: trend, göreli güç, hacim, oynaklık, yapı), 1 hafta beklenen bant.
Adlar: python3 invest/gosterge.py
"""
import sys, json, os, datetime as dt, warnings
import numpy as np, pandas as pd
warnings.filterwarnings("ignore")
from gosterge import veri, hesapla, degerlendir
from teknik_ust import NDX100
from teknik_ek import PORTFOY

EKSTRA = "RKLB SITM AXON CBRS VRT NBIS DOCN CRWV IREN SMR ASTS COIN HIMS ANET COHR CRDO ALAB HOOD SOFI ONDS LUNR OKLO".split()
HAZIR = {
    "dip_avcisi":   ("Aşırı satım + yükselen trend içinde", "rsi<35 ve kapanis>ema200 ve uz50<-1.5"),
    "derin_dip":    ("Sert düşüş, teslimiyet izi", "zirve52<-25 ve rsi<32 ve hacim_oran>1.3"),
    "supurme_donus":("Dip süpürmesi + güçlü kapanış", "sup_boga=1 ve kapanis>acilis ve rsi<50"),
    "kirilim":      ("20 gün tepesini hacimle kırdı, trend yukarı", "kirilim20=1 ve hacim_oran>1.5 ve kapanis>ema50 ve ema50>ema200"),
    "zirve_kirilim":("52 hafta zirvesinde", "kirilim52=1 ve rs20>0"),
    "sikisma":      ("Bollinger sıkışması, hareket hazırlığı", "sikisma=1 ve adx<20"),
    "lider":        ("Göreli güç çizgisi tepede, trend sağlam", "rs_tepe=1 ve kapanis>ema20 ve ema20>ema50 ve ema50>ema200"),
    "trend_donus":  ("Supertrend yukarı döndü, MACD onaylı", "st_yukari=1 ve macd_hist>0"),
    "altin_kesisim":("50/200 altın kesişim", "ema50_200_yukari=1"),
    "geri_cekilme": ("Güçlü trendde EMA20'ye çekilme", "ema20>ema50 ve ema50>ema200 ve dusuk<=ema20 ve kapanis>ema20 ve adx>20"),
    "birikim":      ("Fiyat dipte, para akışı yukarı (sessiz birikim)", "getiri20<-8 ve obv_egim>0 ve cmf>0"),
    "asiri_alim":   ("Tepe riski: aşırı uzama", "rsi>75 ve uz50>3"),
    "kirilim_asagi":("Destek kırılımı, trend aşağı", "kapanis<dusuk20 ve kapanis<ema200 ve hacim_oran>1.3"),
}
YOL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "izleme_listesi.json")

def evren(ad):
    if ad == "portfoy": return PORTFOY
    if ad == "ndx": return list(NDX100)
    if ad == "hepsi": return sorted(set(NDX100) | set(EKSTRA) | set(PORTFOY))
    return [s.strip().upper() for s in ad.split(",") if s.strip()]

_ref = None
def cerceve(t):
    global _ref
    if _ref is None: _ref = veri("QQQ", "5y")
    return hesapla(veri(t, "5y"), _ref)

def kalite(r):
    p = 0
    p += 20 * ((r.kapanis > r.ema50) + (r.ema50 > r.ema200)) / 2
    p += 20 * min(1, max(0, (r.rs20 + 10) / 20))
    p += 15 * min(1, r.hacim_oran / 2)
    p += 15 * (1 if 1.5 < r.atr_yuzde < 6 else 0.4)
    p += 15 * (1 if r.supertrend_yon == 1 else 0)
    p += 15 * min(1, max(0, r.adx / 30))
    return int(round(p))

def tara(ifade, uni, n=15, sirala="kalite"):
    out, hata = [], 0
    for t in uni:
        try:
            x = cerceve(t)
            if len(x) < 220: continue
            m = degerlendir(x, ifade)
            if m.iloc[-1]:
                r = x.iloc[-1]; s = r.atr_yuzde / 100 * np.sqrt(5)
                out.append({"t": t, "fiyat": r.kapanis, "rsi": r.rsi, "uz200": r.uz200, "rs20": r.rs20, "hacim": r.hacim_oran,
                            "zirve52": r.zirve52, "kalite": kalite(r), "bant": (r.kapanis * (1 - s), r.kapanis * (1 + s)),
                            "kac_gundur": int(m.iloc[-20:][::-1].cumprod().sum())})
        except Exception:
            hata += 1
    out.sort(key=lambda z: -z[sirala] if sirala in z else -z["kalite"])
    return out[:n], hata

def yaz(baslik, sonuc, hata, n_uni):
    print(f"== {baslik} | evren {n_uni} hisse | eşleşen {len(sonuc)}" + (f" | veri alınamadı {hata}" if hata else ""))
    if not sonuc: print("   eşleşme yok"); return
    print(f"   {'hisse':<6}{'fiyat':>9} {'RSI':>4} {'200G':>6} {'RS20':>6} {'hacim':>5} {'zirve':>6} {'kalite':>6}  1 hafta bandı   kaç gündür")
    for z in sonuc:
        print(f"   {z['t']:<6}{z['fiyat']:>9,.2f} {z['rsi']:>4.0f} {z['uz200']:>+5.1f}A {z['rs20']:>+6.1f} {z['hacim']:>4.1f}x {z['zirve52']:>+5.0f}% {z['kalite']:>6}  "
              f"{z['bant'][0]:,.0f}–{z['bant'][1]:,.0f}   {z['kac_gundur']}")

def izle():
    uni = evren("hepsi"); bugun = dt.date.today().isoformat()
    L = json.load(open(YOL)) if os.path.exists(YOL) else {"aktif": [], "kapanan": []}
    yeni = 0; eslesme = {}
    for ad, (_, ifade) in HAZIR.items():
        s, _ = tara(ifade, uni, n=50)
        for z in s: eslesme.setdefault((z["t"], ad), z)
    akt = {(a["t"], a["tarama"]): a for a in L["aktif"]}
    for (t, ad), z in eslesme.items():
        if (t, ad) not in akt:
            L["aktif"].append({"t": t, "tarama": ad, "giris_tarih": bugun, "giris": round(z["fiyat"], 2), "kalite": z["kalite"], "son_eslesme": bugun}); yeni += 1
        else: akt[(t, ad)]["son_eslesme"] = bugun
    kal = []
    for a in L["aktif"]:
        gun = (dt.date.fromisoformat(bugun) - dt.date.fromisoformat(a["giris_tarih"])).days
        if gun >= 30:
            try: a["cikis"] = round(cerceve(a["t"]).kapanis.iloc[-1], 2)
            except Exception: a["cikis"] = None
            a["cikis_tarih"] = bugun; L["kapanan"].append(a)
        else: kal.append(a)
    L["aktif"] = kal; json.dump(L, open(YOL, "w"), ensure_ascii=False, indent=1)
    print(f"İZLEME LİSTESİ güncellendi: {yeni} yeni, {len(kal)} aktif, {len(L['kapanan'])} kapanan (30 gün dolan otomatik kapanır)")
    liste()

def liste():
    L = json.load(open(YOL)) if os.path.exists(YOL) else {"aktif": [], "kapanan": []}
    print(f"\nAKTİF İZLEME ({len(L['aktif'])}):")
    for a in sorted(L["aktif"], key=lambda z: (z["tarama"], -z["kalite"])):
        try: f = cerceve(a["t"]).kapanis.iloc[-1]; g = (f / a["giris"] - 1) * 100
        except Exception: g = float("nan")
        print(f"   {a['tarama']:<14} {a['t']:<6} giriş {a['giris_tarih']} {a['giris']:>9,.2f}  şimdi {g:+6.1f}%  kalite {a['kalite']}")
    if L["kapanan"]:
        print("\nTARAMA KARNESİ (kapananlar, 30 gün sonra):")
        df = pd.DataFrame(L["kapanan"]).dropna(subset=["cikis"]); df["g"] = (df.cikis / df.giris - 1) * 100
        for ad, g in df.groupby("tarama").g:
            print(f"   {ad:<14} {len(g):3d} kayıt  ortalama {g.mean():+5.1f}%  yukarıda biten %{(g > 0).mean() * 100:.0f}")

AYOL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "alarmlar_kosul.json")
def alarm(a):
    """Çok faktörlü alarm: tarama.py alarm ekle <T|evren> "<ifade>" "<not>" | liste | sil <id> | kontrol
    Koşul YANLIŞTAN DOĞRUYA geçtiği gün bir kez tetiklenir (her gün aynı alarm tekrar çalmaz)."""
    L = json.load(open(AYOL)) if os.path.exists(AYOL) else []
    if a[0] == "ekle":
        L.append({"id": max([z["id"] for z in L] + [0]) + 1, "hedef": a[1], "ifade": a[2], "not": a[3] if len(a) > 3 else "", "son": {}})
        json.dump(L, open(AYOL, "w"), ensure_ascii=False, indent=1); print(f"alarm {L[-1]['id']} eklendi: {a[1]} [{a[2]}]"); return
    if a[0] == "sil":
        L = [z for z in L if z["id"] != int(a[1])]; json.dump(L, open(AYOL, "w"), ensure_ascii=False, indent=1); print("silindi"); return
    if a[0] == "liste":
        for z in L: print(f"  {z['id']}: {z['hedef']} [{z['ifade']}] {z['not']}")
        if not L: print("  koşullu alarm yok")
        return
    bugun = dt.date.today().isoformat(); cik = []
    for z in L:
        uni = evren(z["hedef"]) if z["hedef"] in ("portfoy", "ndx", "hepsi") or "," in z["hedef"] else [z["hedef"]]
        for t in uni:
            try:
                m = degerlendir(cerceve(t), z["ifade"])
                if m.iloc[-1] and not m.iloc[-2] and z["son"].get(t) != bugun:
                    z["son"][t] = bugun; cik.append(f"ALARM (koşul {z['id']}): {t} [{z['ifade']}] {z['not']} — kapanış {cerceve(t).kapanis.iloc[-1]:,.2f}")
            except Exception: pass
    json.dump(L, open(AYOL, "w"), ensure_ascii=False, indent=1)
    print("\n".join(cik) if cik else "koşullu alarm: tetiklenen yok")

def isi(a):
    """Isı haritası PNG: tarama.py isi [--evren hepsi] [--olcu getiri1|getiri5|getiri20|rs20|rsi] [--out g/isi.png]"""
    import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
    ev = a[a.index("--evren") + 1] if "--evren" in a else "hepsi"; ol = a[a.index("--olcu") + 1] if "--olcu" in a else "getiri1"
    out = a[a.index("--out") + 1] if "--out" in a else "/tmp/isi.png"; R = []
    for t in evren(ev):
        try: r = cerceve(t).iloc[-1]; R.append((t, r[ol], r.rsi))
        except Exception: pass
    R.sort(key=lambda z: -z[1]); n = len(R); k = int(np.ceil(np.sqrt(n * 1.6))); sat = int(np.ceil(n / k))
    fig, ax = plt.subplots(figsize=(10.8, 10.8 * sat / k + 1), dpi=100); fig.patch.set_facecolor("#0b0f14"); ax.set_facecolor("#0b0f14")
    lim = max(1e-9, np.percentile([abs(z[1]) for z in R], 90)) if ol != "rsi" else 30
    for i, (t, v, rs) in enumerate(R):
        x_, y_ = i % k, sat - 1 - i // k; u = ((v - 50) if ol == "rsi" else v) / lim; u = max(-1, min(1, u))
        col = (0.12 + 0.75 * max(0, -u), 0.12 + 0.6 * max(0, u), 0.16)
        ax.add_patch(plt.Rectangle((x_, y_), .96, .92, color=col))
        ax.text(x_ + .48, y_ + .58, t, ha="center", va="center", color="white", fontsize=10, weight="bold")
        ax.text(x_ + .48, y_ + .28, f"{v:+.1f}" + ("" if ol == "rsi" else "%"), ha="center", va="center", color="#dde", fontsize=8)
    ax.set_xlim(0, k); ax.set_ylim(0, sat); ax.axis("off")
    ax.set_title(f"Isı haritası • {ol} • {n} hisse", color="white", loc="left", fontsize=14)
    fig.text(.99, .005, "ENES ULUDAĞ", color="#667", ha="right", fontsize=9, weight="bold")
    fig.tight_layout(); fig.savefig(out, facecolor=fig.get_facecolor()); print(f"ısı haritası: {out}")

KYOL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tarama_kanit.json")
def kanit_olc(ev="hepsi"):
    """Her hazır taramayı evrende 10 yıl backtest eder (sonraki gün açılış girişi, 2 ATR stop, 4 ATR hedef, en çok 15 gün);
    rastgele girişe göre üstünlüğü tarama_kanit.json'a yazar. Taramalar ekranda bu kanıtla gösterilir."""
    from backtest import calistir, ozet, taban
    from veri_kalite import kanit as kn
    uni = evren(ev); K = {}
    for ad, (_, ifade) in HAZIR.items():
        yon = "kisa" if ad in ("asiri_alim", "kirilim_asagi") else "uzun"
        T, XX, p = calistir(uni, ["x", "--giris", ifade, "--stop", "2", "--hedef", "4", "--sure", "15", "--yon", yon])
        if T.empty: continue
        o = ozet(T, XX, 10); tb = [taban(x, 0, 15, yon, 0.1, stop=2, hedef=4) for x in XX if len(x) > 250]
        tk, to = np.mean([z[0] for z in tb]), np.mean([z[1] for z in tb]); k = kn(T.getiri.tolist(), tk)
        ust = k["fark"] >= 5 or o["ort"] - to >= 0.5
        K[ad] = {"n": o["n"], "kazanma": round(o["kazanma"]), "taban": round(tk), "ort": round(o["ort"], 2), "taban_ort": round(to, 2),
                 "pf": round(o["pf"], 2), "hukum": "ÜSTÜN" if ust and o["pf"] >= 1.2 else "FARKSIZ" if o["ort"] - to > -0.5 else "TERS", "tarih": dt.date.today().isoformat()}
        print(f"  {ad:<14} {o['n']:5d} işlem  kazanma %{o['kazanma']:.0f} (taban %{tk:.0f})  ort {o['ort']:+.2f}% (taban {to:+.2f}%)  PF {o['pf']:.2f} -> {K[ad]['hukum']}")
    json.dump(K, open(KYOL, "w"), ensure_ascii=False, indent=1)

def main():
    a = sys.argv[1:]
    if a and a[0] == "kanit": return kanit_olc(a[1] if len(a) > 1 else "hepsi")
    if a and a[0] == "alarm": return alarm(a[1:] or ["liste"])
    if a and a[0] == "isi": return isi(a[1:])
    if not a or a[0] == "hazir":
        K = json.load(open(KYOL)) if os.path.exists(KYOL) else {}
        for k, (ac, ifd) in HAZIR.items(): print(f"  {k:<14} {ac:<45} {K.get(k, {}).get('hukum', '?'):<8} {ifd}")
        return
    if a[0] == "izle": return izle()
    if a[0] == "liste": return liste()
    ev = a[a.index("--evren") + 1] if "--evren" in a else "hepsi"
    n = int(a[a.index("--n") + 1]) if "--n" in a else 15
    sir = a[a.index("--sirala") + 1] if "--sirala" in a else "kalite"
    ad = a[0]; baslik, ifade = (f"{ad}: {HAZIR[ad][0]}", HAZIR[ad][1]) if ad in HAZIR else (ad, ad)
    uni = evren(ev); s, h = tara(ifade, uni, n, sir); yaz(baslik + f"  [{ifade}]", s, h, len(uni))
    K = json.load(open(KYOL)) if os.path.exists(KYOL) else {}
    if ad in K:
        k = K[ad]; print(f"   GEÇMİŞ KANIT ({k['tarih']}, 10 yıl, {k['n']} işlem): kazanma %{k['kazanma']} vs rastgele %{k['taban']}, ort {k['ort']:+.2f}% vs {k['taban_ort']:+.2f}% -> {k['hukum']}")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""TEKNİK EK — telefondan tek mesajla tam analiz (Enes 25.11.2026 22:16 "çok daha geliştir, sadece telefondan yapabileyim").

Alt komutlar:
  kart <TICKER> [--seviyeler a,b] [--out g/x.jpg]   Tek görselde mobil analiz kartı (1080x1350) + metin özet
  derin <TICKER> [--seviyeler a,b]                   Ek modüller: çakışma (confluence) haritası, uyumsuzluk (RSI/MACD),
                                                     pivotlar (klasik + Camarilla), Ichimoku, Bollinger sıkışması,
                                                     ATR yüzdeliği (oynaklık rejimi), VIX'ten beklenen hareket,
                                                     göreli güç (vs Nasdaq 100), mevsimsellik, benzer koşul istatistiği
  tara [TICKER,...]                                   Liste taraması (varsayılan Enes portföyü): MTF puanı, RSI, ATR%,
                                                     zirveden uzaklık, en yakın güçlü seviye -> sıralı tablo
  istatistik <TICKER> "<koşul>"                       Basit geçmiş test: koşul = rsi<30 | zirveden<-20 | ema200_alti |
                                                     gun_dustu>3  -> sonraki 5/10/20 gün getiri dağılımı (ortalama, medyan, kazanma oranı)
  alarm ekle <TICKER> <seviye> <yukari|asagi> "<not>" | alarm liste | alarm sil <id> | alarm kontrol
                                                     Fiyat alarmı: her tur başında `alarm kontrol` çalışır, tetiklenince
                                                     Enes'e SendUserMessage ile bildirilir (tur_basi.sh).
Onay: Enes 25.11.2026 22:11 (pip smartmoneyconcepts, pandas_ta). Veri Yahoo (ham).
"""
import sys, json, os, datetime as dt, warnings
import numpy as np, pandas as pd
warnings.filterwarnings("ignore")
D0 = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, D0)
from smc_analiz import veri
PORTFOY = ["DOCN", "RKLB", "SITM", "AXON", "CBRS", "VRT", "AVGO", "NBIS"]

def kaynak(k):
    return ', '.join(sorted(set(x.replace('ENES', 'yatay seviye') for x in k['k'])))

def _ta():
    import pandas_ta as ta; return ta

def mtf(t):
    from teknik_pro import yon_ozet
    R = {}
    for k, sw in {"1wk": 5, "1d": 10, "4h": 6, "1h": 6}.items():
        try: R[k] = yon_ozet(veri(t, k), sw)
        except Exception: pass
    return R, sum(r["puan"] for r in R.values())

def seviye_havuzu(t, d1, h1, enes):
    """Tüm araçlardan seviye topla -> yakın olanları kümelendir -> çakışma puanı."""
    from smartmoneyconcepts import smc
    ta = _ta(); L = []
    shl = smc.swing_highs_lows(d1, swing_length=10)
    for k, v in zip(shl.HighLow, shl.Level):
        if pd.notna(k): L.append((v, "swing"))
    f = smc.fvg(d1, join_consecutive=True).dropna(subset=["FVG"]); f = f[f.MitigatedIndex.fillna(0) == 0]
    for r in f.itertuples(): L += [(r.Top, "FVG"), (r.Bottom, "FVG")]
    ob = smc.ob(d1, shl).dropna(subset=["OB"]); ob = ob[ob.MitigatedIndex.fillna(0) == 0]
    for r in ob.itertuples(): L += [(r.Top, "OB"), (r.Bottom, "OB")]
    c = d1.close
    for n in (20, 50, 200):
        if len(c) > n: L.append((_ta().ema(c, n).iloc[-1], f"EMA{n}"))
    p = piv(d1)
    for k, v in p.items(): L.append((v, "pivot"))
    from teknik_pro import hacim_profili, avwap
    if h1 is not None and h1.volume.sum() > 0:
        poc, vah, val = hacim_profili(h1.tail(140)); L += [(poc, "POC"), (vah, "VAH"), (val, "VAL")]
    hi_i = d1.high.tail(120).idxmax(); lo_i = d1.low.tail(120).idxmin()
    L += [(avwap(d1, d1.index.get_loc(hi_i)), "AVWAP-tepe"), (avwap(d1, d1.index.get_loc(lo_i)), "AVWAP-dip")]
    hi, lo = d1.high.tail(120).max(), d1.low.tail(120).min()
    for fr in (0.382, 0.5, 0.618, 0.786): L.append((lo + (hi - lo) * fr, f"Fib{fr}"))
    son = c.iloc[-1]; adim = 10 ** int(np.log10(son)) / (2 if son > 1000 else 4)
    for k in range(-3, 4): L.append((round(son / adim) * adim + k * adim, "yuvarlak"))
    for e in enes: L.append((e, "ENES"))
    L = [x for x in L if abs(x[0] / son - 1) < 0.12]
    atr = ta.atr(d1.high, d1.low, c, 14).iloc[-1]; tol = atr * 0.25
    L.sort(); K = []
    for v, kay in L:
        if K and abs(v - K[-1]["ort"]) <= tol: K[-1]["v"].append(v); K[-1]["k"].append(kay); K[-1]["ort"] = float(np.mean(K[-1]["v"]))
        else: K.append({"v": [v], "k": [kay], "ort": v})
    for k_ in K: k_["puan"] = len(set(k_["k"])) + (1 if "ENES" in k_["k"] else 0)
    return sorted(K, key=lambda x: -x["puan"]), son

def piv(d1):
    h, l, c = d1.high.iloc[-2], d1.low.iloc[-2], d1.close.iloc[-2]; P = (h + l + c) / 3
    return {"P": P, "R1": 2 * P - l, "S1": 2 * P - h, "R2": P + (h - l), "S2": P - (h - l),
            "H3": c + (h - l) * 1.1 / 4, "L3": c - (h - l) * 1.1 / 4}

def uyumsuzluk(df, n=40):
    ta = _ta(); r = ta.rsi(df.close, 14); d = df.tail(n); rr = r.tail(n); out = []
    lows = d.low.nsmallest(2).index.sort_values(); highs = d.high.nlargest(2).index.sort_values()
    if len(lows) == 2 and d.low[lows[1]] < d.low[lows[0]] and rr[lows[1]] > rr[lows[0]] and (lows[1] - lows[0]).days >= 2:
        out.append(f"BOĞA uyumsuzluğu: fiyat yeni dip ({d.low[lows[1]]:,.0f} < {d.low[lows[0]]:,.0f}) ama RSI yükseliyor ({rr[lows[0]]:.0f} -> {rr[lows[1]]:.0f})")
    if len(highs) == 2 and d.high[highs[1]] > d.high[highs[0]] and rr[highs[1]] < rr[highs[0]] and (highs[1] - highs[0]).days >= 2:
        out.append(f"AYI uyumsuzluğu: fiyat yeni tepe ama RSI düşüyor ({rr[highs[0]]:.0f} -> {rr[highs[1]]:.0f})")
    return out or ["Belirgin RSI uyumsuzluğu yok"]

def derin(t, enes):
    ta = _ta(); d1 = veri(t, "1d"); h4 = veri(t, "4h")
    try: h1 = veri(t, "1h")
    except Exception: h1 = None
    c = d1.close; son = c.iloc[-1]; o = []
    K, _ = seviye_havuzu(t, d1, h1, enes)
    o.append("ÇAKIŞMA HARİTASI (puan = farklı araç sayısı, Enes seviyesi +1):")
    ust = sorted([k for k in K if k["ort"] > son], key=lambda k: k["ort"])[:4]
    alt = sorted([k for k in K if k["ort"] <= son], key=lambda k: -k["ort"])[:4]
    for et, grp in (("  Direnç", ust), ("  Destek", alt)):
        for k in grp: o.append(f"{et} {k['ort']:,.0f} ({(k['ort']/son-1)*100:+.1f}%) puan {k['puan']} [{', '.join(sorted(set(k['k'])))}]{' GÜÇLÜ' if k['puan'] >= 3 else ''}")
    o.append("UYUMSUZLUK 1d: " + " | ".join(uyumsuzluk(d1))); o.append("UYUMSUZLUK 4h: " + " | ".join(uyumsuzluk(h4)))
    p = piv(d1); o.append("PİVOT (dünkü mum): " + " | ".join(f"{k} {v:,.0f}" for k, v in p.items()))
    ich = ta.ichimoku(d1.high, d1.low, c)[0]
    if ich is not None:
        sa, sb = ich.iloc[-1, 0], ich.iloc[-1, 1]; ust_b, alt_b = max(sa, sb), min(sa, sb)
        o.append(f"ICHIMOKU 1d: bulut {alt_b:,.0f}–{ust_b:,.0f}; fiyat {'bulutun ÜSTÜNDE' if son > ust_b else 'bulutun ALTINDA' if son < alt_b else 'bulutun İÇİNDE'}; Tenkan {ich.iloc[-1,2]:,.0f} Kijun {ich.iloc[-1,3]:,.0f}")
    bb = ta.bbands(c, 20, 2); gen = (bb.iloc[:, 2] - bb.iloc[:, 0]) / bb.iloc[:, 1]
    yuz = (gen.tail(250) < gen.iloc[-1]).mean() * 100
    o.append(f"BOLLINGER GENİŞLİĞİ yüzdelik {yuz:.0f} (20 altı = SIKIŞMA, patlama yakın; 80 üstü = aşırı oynak)")
    atr = ta.atr(d1.high, d1.low, c, 14); ap = (atr / c * 100); apy = (ap.tail(250) < ap.iloc[-1]).mean() * 100
    o.append(f"OYNAKLIK REJİMİ: ATR %{ap.iloc[-1]:.2f}, son 1 yılın yüzdelik {apy:.0f}")
    try:
        vx = veri("^VXN" if t in ("^NDX", "NQ=F", "QQQ") else "^VIX", "1d").close.iloc[-1]
        em = son * vx / 100 / np.sqrt(252); emw = son * vx / 100 / np.sqrt(52)
        o.append(f"BEKLENEN HAREKET (oynaklık endeksi {vx:.1f}): 1 gün ±{em:,.0f} ({son-em:,.0f}–{son+em:,.0f}) | 1 hafta ±{emw:,.0f} ({son-emw:,.0f}–{son+emw:,.0f})")
    except Exception: pass
    if t != "^NDX":
        b = veri("^NDX", "1d").close; j = c.index.intersection(b.index)
        rs = (c[j] / c[j].iloc[-60] - 1) - (b[j] / b[j].iloc[-60] - 1)
        o.append(f"GÖRELİ GÜÇ (60 gün, Nasdaq 100'e göre): {rs.iloc[-1]*100:+.1f} puan")
    w = veri(t, "1wk"); wc = w.close; ay, gun = son and dt.date.today().month, dt.date.today().day
    gec = []
    for y in sorted(set(wc.index.year))[:-1]:
        a0 = wc[(wc.index.year == y) & (wc.index.month == ay)]
        if len(a0) >= 2: gec.append(a0.iloc[-1] / a0.iloc[0] - 1)
    if gec: o.append(f"MEVSİMSELLİK ({len(gec)} yıl, bu ayın içi): ortalama {np.mean(gec)*100:+.1f}%, pozitif yıl {sum(g>0 for g in gec)}/{len(gec)}")
    return "\n".join(o)

def istatistik(t, kosul, df=None):
    ta = _ta(); d = df if df is not None else veri(t, "1wk") if False else None
    u = f"https://query1.finance.yahoo.com/v8/finance/chart/{t}?interval=1d&range=20y"
    import urllib.request
    j = json.load(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=20))["chart"]["result"][0]
    q = j["indicators"]["quote"][0]
    d = pd.DataFrame({"close": q["close"], "high": q["high"], "low": q["low"]}, index=pd.to_datetime(j["timestamp"], unit="s")).dropna()
    c = d.close
    if kosul.startswith("rsi<"): m = ta.rsi(c, 14) < float(kosul[4:])
    elif kosul.startswith("zirveden<"): m = (c / c.cummax() - 1) * 100 < float(kosul[9:])
    elif kosul == "ema200_alti": m = c < ta.ema(c, 200)
    elif kosul.startswith("gun_dustu>"): m = c.pct_change() * 100 < -float(kosul[10:])
    else: return "Bilinmeyen koşul. Seçenekler: rsi<30, zirveden<-20, ema200_alti, gun_dustu>3"
    mv = m.fillna(False).values; sec = []
    for i in range(1, len(mv)):
        if mv[i] and not mv[i - 1] and (not sec or i - sec[-1] >= 60): sec.append(i)  # yalnız koşula İLK giriş, olaylar arası en az 60 gün
    o = [f"{t} 20 yıl, koşul '{kosul}': {len(sec)} bağımsız olay (koşula ilk giriş, en az 60 gün arayla)"]
    for n in (5, 10, 20, 60):
        g = [c.iloc[i + n] / c.iloc[i] - 1 for i in sec if i + n < len(c)]
        if g: o.append(f"  {n:2} gün sonra: ortalama {np.mean(g)*100:+.1f}% | medyan {np.median(g)*100:+.1f}% | pozitif {np.mean([x>0 for x in g])*100:.0f}% | en kötü {min(g)*100:+.1f}%")
    son_olay = [c.index[i].date() for i in sec[-5:]]
    o.append("  Son olaylar: " + ", ".join(str(x) for x in son_olay))
    o.append("  Not: geçmiş dağılım, tahmin değil; az olay (<15) varsa güvenilmez.")
    return "\n".join(o)

def tara(lst):
    ta = _ta(); S = []
    for t in lst:
        try:
            d1 = veri(t, "1d"); c = d1.close; R, top = mtf(t)
            S.append((top, t, c.iloc[-1], ta.rsi(c, 14).iloc[-1], (ta.atr(d1.high, d1.low, c, 14).iloc[-1] / c.iloc[-1]) * 100, (c.iloc[-1] / c.max() - 1) * 100))
        except Exception as e: S.append((-99, t, 0, 0, 0, 0))
    o = ["TARAMA (MTF puanı büyükten küçüğe; −20 en zayıf, +20 en güçlü)", f"{'Hisse':7}{'MTF':>5}{'Fiyat':>10}{'RSI':>6}{'ATR%':>6}{'Zirve%':>8}"]
    for top, t, p, r, a, z in sorted(S, reverse=True):
        o.append(f"{t:7}{top:>+5d}{p:>10,.2f}{r:>6.0f}{a:>6.1f}{z:>8.1f}")
    return "\n".join(o)

AF = os.path.join(D0, "alarmlar.json")
def alarm(a):
    A = json.load(open(AF)) if os.path.exists(AF) else []
    k = a[0] if a else "liste"
    if k == "ekle":
        t, sv, yon = a[1], float(a[2]), a[3]; nt = a[4] if len(a) > 4 else ""
        i = (max([x["id"] for x in A]) + 1) if A else 1
        A.append({"id": i, "t": t, "seviye": sv, "yon": yon, "not": nt, "kuruldu": dt.datetime.now().strftime("%d.%m %H:%M"), "tetik": ""})
        json.dump(A, open(AF, "w"), ensure_ascii=False, indent=1); print(f"alarm {i}: {t} {yon} {sv}"); return
    if k == "sil":
        A = [x for x in A if x["id"] != int(a[1])]; json.dump(A, open(AF, "w"), ensure_ascii=False, indent=1); print("silindi"); return
    if k == "kontrol":
        import urllib.request; cikti = []
        for x in A:
            if x["tetik"]: continue
            try:
                u = f"https://query1.finance.yahoo.com/v8/finance/chart/{x['t']}?interval=5m&range=1d"
                j = json.load(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=10))["chart"]["result"][0]
                q = j["indicators"]["quote"][0]; hi = max(v for v in q["high"] if v); lo = min(v for v in q["low"] if v); p = j["meta"]["regularMarketPrice"]
            except Exception: continue
            if (x["yon"] == "yukari" and hi >= x["seviye"]) or (x["yon"] == "asagi" and lo <= x["seviye"]):
                x["tetik"] = dt.datetime.now().strftime("%d.%m %H:%M"); cikti.append(f"ALARM {x['id']}: {x['t']} {x['seviye']:,.1f} {'üstüne çıktı' if x['yon']=='yukari' else 'altına indi'} (şu an {p:,.1f}) — {x['not']}")
        json.dump(A, open(AF, "w"), ensure_ascii=False, indent=1)
        if cikti: print("\n".join(cikti) + "\n-> SendUserMessage ile Enes'e bildir.")
        return
    for x in A: print(f"{x['id']:3} {x['t']:7} {x['yon']:6} {x['seviye']:>12,.1f}  {('TETİKLENDİ '+x['tetik']) if x['tetik'] else 'bekliyor'}  {x['not']}")

def kart(t, enes, out):
    import kart3 as K
    R, top = mtf(t); d1 = veri(t, "1d")
    try: h1 = veri(t, "1h")
    except Exception: h1 = None
    Kl, son = seviye_havuzu(t, d1, h1, enes)
    ust = sorted([k for k in Kl if k["ort"] > son], key=lambda k: k["ort"])[:2]
    alt = sorted([k for k in Kl if k["ort"] <= son], key=lambda k: -k["ort"])[:1]
    yon = "GÜÇLÜ AŞAĞI" if top <= -8 else "AŞAĞI" if top <= -3 else "GÜÇLÜ YUKARI" if top >= 8 else "YUKARI" if top >= 3 else "KARARSIZ"
    madde = [(f"{top:+d}", f"çoklu zaman dilimi yönü: {yon}")]
    for k in ust[:1]: madde.append((f"{k['ort']:,.0f}".replace(",", "."), f"direnç • {kaynak(k)[:38]}"))
    for k in alt: madde.append((f"{k['ort']:,.0f}".replace(",", "."), f"destek • {kaynak(k)[:38]}"))
    h4 = veri(t, "4h")
    s1 = [(str(i.date()), v) for i, v in d1.close.tail(120).items()]
    s4 = [(str(i.date()), v) for i, v in h4.close.tail(60).items()]
    K.haber_dosya("", f"Teknik • {t}", f"{t}: yön {yon.lower()}", "SMC + ICT + MTF çakışma özeti.", madde,
                  [("Günlük (120)", s1), ("4 saatlik (60)", s4)], f"Yön {yon.lower()}; en güçlü seviyeler kartta",
                  "Yahoo; smartmoneyconcepts; pandas_ta", out, yontem="MTF puanı 1wk/1d/4h/1h • çakışma: FVG, OB, EMA, pivot, POC, AVWAP, Fib",
                  tarih=dt.date.today().strftime("%d.%m.%Y"), etk_et="FİYAT")
    print(f"kart: {out}")

GF = os.path.join(D0, "analiz_gunlugu.json")
def gunluk(a):
    """Enes'in analiz günlüğü: senaryo kaydı -> N gün sonra otomatik puanlama (isabet oranı)."""
    G = json.load(open(GF)) if os.path.exists(GF) else []
    k = a[0] if a else "liste"
    if k == "ekle":  # gunluk ekle <T> <yon yukari|asagi> <giris> <stop> <hedef> <gun> "<gerekçe>"
        t, yon, g, s_, h, n = a[1], a[2], float(a[3]), float(a[4]), float(a[5]), int(a[6])
        G.append({"id": len(G) + 1, "t": t, "yon": yon, "giris": g, "stop": s_, "hedef": h, "gun": n, "gerekce": a[7] if len(a) > 7 else "",
                  "tarih": dt.date.today().isoformat(), "sonuc": ""})
        json.dump(G, open(GF, "w"), ensure_ascii=False, indent=1); print("kaydedildi", len(G)); return
    if k == "kontrol":
        for x in G:
            if x["sonuc"]: continue
            d = veri(x["t"], "1d"); d = d[d.index.date >= dt.date.fromisoformat(x["tarih"])]
            if d.empty: continue
            sonuc = ""
            girdi = (d.low <= x["giris"]).any() if x["yon"] == "asagi" and False else ((d.high >= x["giris"]) & (d.low <= x["giris"])).any() or True
            for r in d.itertuples():
                if x["yon"] == "asagi":
                    if r.high >= x["stop"]: sonuc = "STOP"; break
                    if r.low <= x["hedef"]: sonuc = "HEDEF"; break
                else:
                    if r.low <= x["stop"]: sonuc = "STOP"; break
                    if r.high >= x["hedef"]: sonuc = "HEDEF"; break
            if not sonuc and (dt.date.today() - dt.date.fromisoformat(x["tarih"])).days >= x["gun"]: sonuc = "SÜRE DOLDU"
            if sonuc: x["sonuc"] = sonuc; x["kapanis"] = dt.date.today().isoformat(); print(f"{x['id']} {x['t']} {x['yon']} -> {sonuc}")
        json.dump(G, open(GF, "w"), ensure_ascii=False, indent=1)
    kap = [x for x in G if x["sonuc"]]
    if kap:
        h = sum(x["sonuc"] == "HEDEF" for x in kap); s_ = sum(x["sonuc"] == "STOP" for x in kap)
        print(f"KARNE: {len(kap)} kapanan senaryo | hedef {h} | stop {s_} | süre doldu {len(kap)-h-s_} | isabet {h/max(1,h+s_)*100:.0f}%")
    for x in G[-10:]: print(f"{x['id']:3} {x['tarih']} {x['t']:6} {x['yon']:6} giriş {x['giris']:,.0f} stop {x['stop']:,.0f} hedef {x['hedef']:,.0f} -> {x['sonuc'] or 'açık'} | {x['gerekce'][:60]}")

def seviye_test(t, seviyeler, tol_atr=0.25, ileri=5):
    """Seviyenin geçmişte işe yarayıp yaramadığı: fiyat seviyeye (±0,25 ATR) değdiği günlerden sonra
    5 günde en az 1 ATR tepki verdi mi (destekte yukarı / dirençte aşağı) yoksa kırıldı mı."""
    ta = _ta(); d = veri(t, "1d"); atr = ta.atr(d.high, d.low, d.close, 14); o = []
    for s_ in seviyeler:
        dok = tepki = kir = 0; i = 15
        while i < len(d) - ileri:
            r = d.iloc[i]; a_ = atr.iloc[i]
            if r.low - tol_atr * a_ <= s_ <= r.high + tol_atr * a_:
                dok += 1; ust = d.close.iloc[i - 1] > s_  # seviyeye yukarıdan mı geldi (destek)
                fut = d.iloc[i + 1:i + 1 + ileri]
                if ust:
                    if (fut.high.max() - s_) >= a_ and fut.close.min() > s_ - a_: tepki += 1
                    elif fut.close.min() < s_ - a_: kir += 1
                else:
                    if (s_ - fut.low.min()) >= a_ and fut.close.max() < s_ + a_: tepki += 1
                    elif fut.close.max() > s_ + a_: kir += 1
                i += ileri
            else: i += 1
        o.append(f"  {s_:,.1f}: {dok} temas (2 yıl) | tepki {tepki} | kırılım {kir} | tepki oranı {tepki/max(1,dok)*100:.0f}%{'  <- işe yarayan seviye' if dok >= 3 and tepki/dok >= 0.5 else ''}")
    return f"SEVİYE TESTİ {t} (temas = ±0,25 ATR; tepki = 5 günde ≥1 ATR geri dönüş):\n" + "\n".join(o)

if __name__ == "__main__":
    a = sys.argv[1:]; k = a[0]
    sev = [float(x) for x in a[a.index("--seviyeler") + 1].split(",")] if "--seviyeler" in a else []
    if k == "derin": print(derin(a[1], sev))
    elif k == "tara": print(tara(a[1].split(",") if len(a) > 1 and not a[1].startswith("--") else PORTFOY))
    elif k == "istatistik": print(istatistik(a[1], a[2]))
    elif k == "alarm": alarm(a[1:])
    elif k == "gunluk": gunluk(a[1:])
    elif k == "seviye_test": print(seviye_test(a[1], sev))
    elif k == "kart": kart(a[1], sev, a[a.index("--out") + 1] if "--out" in a else f"g/teknik_{a[1].strip('^')}.jpg")
    else: print(__doc__)

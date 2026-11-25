#!/usr/bin/env python3
"""smc_ek.py — Enes 26.11 00:08 "SMC ve ICT analizini daha iyi yapmak için yardımcı indikatör ve araçlar".
Kullanım: python3 invest/smc_ek.py <T> [--tf 4h|1h|1d] [--ortak ^GSPC]
1) LİKİDİTE SÜPÜRMESİ (stop avı): fitil eski dibin/tepenin ötesine geçip kapanış geri içeride. + ardından MSS (yapı kırılımı).
2) FVG KALİTESİ: her açık FVG için itki gücü (gövde/ATR), itki hacmi, indirim/prim bölgesi, test edildi mi, üst zaman dilimi uyumu -> 0-5 puan.
3) SMT UYUMSUZLUĞU: ortak enstrümanla (NDX<->S&P 500, hisse<->sektör ETF) biri yeni dip yaparken diğeri yapmıyor mu.
4) GEÇMİŞ TESTİ (bu enstrümanın kendi verisi, kanıt kuralı): süpürme, süpürme+MSS, FVG'ye ilk dönüş (itkili/itkisiz, hacimli/hacimsiz, indirim bölgesinde/değil)
   sonrası 10 mum getirisi; TABAN ORAN ve Wilson aralığıyla. 1d = 20 yıl, 1h = 2 yıl.
5) A+ KURULUM KONTROL LİSTESİ (7 madde) ve tek cümle hüküm.
Otomatik tweet yok.
"""
import sys, json, urllib.request, warnings
import numpy as np, pandas as pd
warnings.filterwarnings("ignore")
from veri_kalite import temiz, kanit

ORTAK = {"^NDX": "^GSPC", "QQQ": "SPY", "NQ=F": "ES=F", "^GSPC": "^NDX", "ES=F": "NQ=F", "AVGO": "SOXX", "NVDA": "SOXX", "AMD": "SOXX",
         "SITM": "SOXX", "MU": "SOXX", "RKLB": "ITA", "AXON": "ITA", "VRT": "XLI", "DOCN": "IGV", "NBIS": "IGV", "CBRS": "IGV", "TSLA": "QQQ"}

def gun_ici(t, tf):
    i, r = {"1h": ("60m", "730d"), "4h": ("60m", "730d")}[tf]
    u = f"https://query1.finance.yahoo.com/v8/finance/chart/{t}?interval={i}&range={r}"
    d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=25))["chart"]["result"][0]
    q = d["indicators"]["quote"][0]
    df = pd.DataFrame({k: q[k] for k in ("open", "high", "low", "close", "volume")},
                      index=pd.to_datetime(d["timestamp"], unit="s", utc=True).tz_convert("Europe/Istanbul")).dropna(subset=["close"])
    if tf == "4h":
        df = df.resample("4h", offset="30min").agg({"open": "first", "high": "max", "low": "min", "close": "last", "volume": "sum"}).dropna()
    return df

def yukle(t, tf):
    return temiz(t, "1d", "20y")[0] if tf == "1d" else gun_ici(t, tf)

def atr(d, n=14):
    tr = pd.concat([d.high - d.low, (d.high - d.close.shift()).abs(), (d.low - d.close.shift()).abs()], axis=1).max(axis=1)
    return tr.rolling(n).mean()

def salinimlar(d, n=3):
    """Onaylı salınım tepe/dipleri (n mum sonra bilinir -> ileriye bakma yok)."""
    h, l = d.high.values, d.low.values; T, D = [], []
    for i in range(n, len(d) - n):
        if h[i] == max(h[i - n:i + n + 1]): T.append((i, h[i]))
        if l[i] == min(l[i - n:i + n + 1]): D.append((i, l[i]))
    return T, D

def supurmeler(d, n=3):
    """Her mum için: o ana kadar onaylanmış ve henüz alınmamış son salınım dibi/tepesi süpürüldü mü."""
    T, D = salinimlar(d, n); h, l, c = d.high.values, d.low.values, d.close.values
    ev = []; aktifD, aktifT = [], []; ti = di = 0
    for i in range(len(d)):
        while di < len(D) and D[di][0] + n <= i: aktifD.append(D[di]); di += 1
        while ti < len(T) and T[ti][0] + n <= i: aktifT.append(T[ti]); ti += 1
        aktifD = aktifD[-6:]; aktifT = aktifT[-6:]
        for j, (k, v) in enumerate(aktifD):
            if l[i] < v:
                if c[i] > v: ev.append((i, "boga", v, aktifT[-1][1] if aktifT else None))
                aktifD.pop(j); break
        for j, (k, v) in enumerate(aktifT):
            if h[i] > v:
                if c[i] < v: ev.append((i, "ayi", v, aktifD[-1][1] if aktifD else None))
                aktifT.pop(j); break
    return ev

def mss_sonra(d, ev, k=10):
    """Süpürmeden sonra k mum içinde karşı salınımın kapanışla kırılması (MSS)."""
    c = d.close.values; out = []
    for i, yon, v, karsi in ev:
        if karsi is None: continue
        for j in range(i + 1, min(i + 1 + k, len(c))):
            if (yon == "boga" and c[j] > karsi) or (yon == "ayi" and c[j] < karsi): out.append((j, yon, i)); break
    return out

def fvgler(d):
    a = atr(d); h, l, o, c, v = d.high.values, d.low.values, d.open.values, d.close.values, d.volume.fillna(0).values
    vort = pd.Series(v).rolling(20).mean().values
    rng_h = d.high.rolling(60).max().values; rng_l = d.low.rolling(60).min().values
    out = []
    for i in range(2, len(d)):
        if np.isnan(a.iloc[i - 1]): continue
        for yon, alt, ust in (("boga", h[i - 2], l[i]), ("ayi", h[i], l[i - 2])):
            if ust <= alt: continue
            itki = abs(c[i - 1] - o[i - 1]) / a.iloc[i - 1]
            hac = v[i - 1] / vort[i - 1] if vort[i - 1] else np.nan
            orta = (rng_h[i] + rng_l[i]) / 2 if not np.isnan(rng_h[i]) else np.nan
            bolge = (alt < orta) if yon == "boga" else (ust > orta)
            out.append({"i": i, "yon": yon, "alt": alt, "ust": ust, "itki": itki, "hac": hac, "uygun_bolge": bool(bolge)})
    return out

def fvg_test(d, F, ufuk=10, max_bekle=40):
    """FVG'ye ilk dönüş (fiyat boşluğa girer) -> o mumun kapanışından ufuk mum sonra yön lehine mi?"""
    h, l, c = d.high.values, d.low.values, d.close.values; sonuc = []
    for f in F:
        for j in range(f["i"] + 1, min(f["i"] + max_bekle, len(c) - ufuk)):
            if (f["yon"] == "boga" and l[j] <= f["ust"]) or (f["yon"] == "ayi" and h[j] >= f["alt"]):
                g = c[j + ufuk] / c[j] - 1; sonuc.append({**f, "g": g if f["yon"] == "boga" else -g, "j": j}); break
    return pd.DataFrame(sonuc)

def taban(c, ufuk, yon="boga"):
    f = (c.shift(-ufuk) / c - 1).dropna(); return ((f > 0) if yon == "boga" else (f < 0)).mean() * 100

def smt(d1, d2, n=20):
    x = pd.concat([d1.low.rename("l1"), d2.low.rename("l2"), d1.high.rename("h1"), d2.high.rename("h2")], axis=1).dropna()
    if len(x) < n + 5: return "veri yok"
    son, once = x.iloc[-5:], x.iloc[-n - 5:-5]
    yd1, yd2 = son.l1.min() < once.l1.min(), son.l2.min() < once.l2.min()
    yt1, yt2 = son.h1.max() > once.h1.max(), son.h2.max() > once.h2.max()
    if yd1 != yd2: return f"BOĞA SMT: {'bu enstrüman' if yd1 else 'ortak'} yeni dip yaptı, {'ortak' if yd1 else 'bu enstrüman'} yapmadı (satış baskısı yayılmıyor)"
    if yt1 != yt2: return f"AYI SMT: {'bu enstrüman' if yt1 else 'ortak'} yeni tepe yaptı, diğeri yapmadı (alım gücü yayılmıyor)"
    return "SMT yok (ikisi aynı yönde)"

def main():
    a = sys.argv[1:]; t = a[0] if a else "^NDX"
    tf = a[a.index("--tf") + 1] if "--tf" in a else "4h"
    ortak = a[a.index("--ortak") + 1] if "--ortak" in a else ORTAK.get(t, "QQQ")
    d = yukle(t, tf); A = atr(d); fiy = d.close.iloc[-1]; ufuk = 10
    print(f"== {t} {tf} {fiy:,.2f} | {len(d)} mum ({d.index[0]:%d.%m.%Y} – {d.index[-1]:%d.%m.%Y %H:%M})")
    # 1) süpürmeler
    ev = supurmeler(d); ms = mss_sonra(d, ev); son_ev = [e for e in ev if e[0] >= len(d) - 15]
    print("\n1) LİKİDİTE SÜPÜRMESİ (son 15 mum):")
    if not son_ev: print("   yok")
    T1, D1 = salinimlar(d, 1)
    for i, yon, v, karsi in son_ev:
        ic_ = [x for x in (T1 if yon == "boga" else D1) if x[0] < len(d) - 1]
        ic_s = ic_[-1][1] if ic_ else None
        if ic_s is None or ic_s == karsi: ic_s = d.high.iloc[-3:-1].max() if yon == "boga" else d.low.iloc[-3:-1].min()
        m = [x for x in ms if x[2] == i]
        print(f"   {d.index[i]:%d.%m %H:%M} {'DİP süpürüldü (boğa)' if yon == 'boga' else 'TEPE süpürüldü (ayı)'} seviye {v:,.2f}"
              + (f" -> MSS onaylı {d.index[m[0][0]]:%d.%m %H:%M}" if m else (f" -> MSS henüz yok; onay için {karsi:,.2f} {'üstünde' if yon == 'boga' else 'altında'} kapanış (fiyata {(karsi / fiy - 1) * 100:+.1f}%)" + (f"; erken iç yapı onayı {ic_s:,.2f} (fiyata {(ic_s / fiy - 1) * 100:+.1f}%)" if ic_s else "") if karsi else " -> MSS henüz yok")))
    # 2) açık FVG kalitesi
    F = fvgler(d); h, l = d.high.values, d.low.values; acik = []
    for f in F[-300:]:
        if f["i"] == len(d) - 1: acik.append({**f, "test": False}); continue
        kalan_l, kalan_h = l[f["i"] + 1:].min(), h[f["i"] + 1:].max()
        dolu = kalan_l <= f["alt"] if f["yon"] == "boga" else kalan_h >= f["ust"]
        if not dolu: acik.append({**f, "test": bool(kalan_l <= f["ust"] if f["yon"] == "boga" else kalan_h >= f["alt"])})
    try:
        from teknik_pro import yon_ozet
        from smc_analiz import veri
        ust_tf = {"1h": "4h", "4h": "1d", "1d": "1wk"}[tf]; ub = yon_ozet(veri(t, ust_tf), 6 if ust_tf == "4h" else 10)["puan"]
    except Exception: ust_tf, ub = "?", 0
    print(f"\n2) AÇIK FVG'LER (kalite 0-5: itki ≥1,5 ATR, itki hacmi ≥1,5x, doğru bölge, ilk test bekliyor, {ust_tf} yönüyle uyumlu [{ub:+d}]):")
    sira = []
    for f in acik:
        p = int(f["itki"] >= 1.5) + ((f["hac"] or 0) >= 1.5) + f["uygun_bolge"] + (not f["test"]) + ((ub > 0) == (f["yon"] == "boga") and ub != 0)
        sira.append((int(p), f))
    ust_l = sorted([x for x in sira if x[1]["alt"] > fiy], key=lambda x: x[1]["alt"])[:3]
    alt_l = sorted([x for x in sira if x[1]["ust"] < fiy], key=lambda x: -x[1]["ust"])[:3]
    ic = [x for x in sira if x[1]["alt"] <= fiy <= x[1]["ust"]]
    print("   (fiyatın üstündeki en yakın 3, içinde olan, altındaki en yakın 3)")
    for p, f in ust_l[::-1] + ic + alt_l:
        print(f"   {p}/5 {'BOĞA' if f['yon'] == 'boga' else 'AYI '} {f['alt']:,.2f} – {f['ust']:,.2f} (orta {(f['alt'] + f['ust']) / 2:,.2f}, fiyata {((f['alt'] + f['ust']) / 2 / fiy - 1) * 100:+.1f}%)"
              f" itki {f['itki']:.1f} ATR, hacim {f['hac']:.1f}x, {'test edildi' if f['test'] else 'test edilmedi'}, {d.index[f['i']]:%d.%m %H:%M}")
    if not sira: print("   açık FVG yok")
    # 3) SMT
    try: s = smt(d, yukle(ortak, tf))
    except Exception as e: s = f"ortak veri alınamadı ({e})"
    print(f"\n3) SMT ({ortak} ile): {s}")
    # 4) geçmiş testi
    tb_b, tb_a = taban(d.close, ufuk, "boga"), taban(d.close, ufuk, "ayi")
    print(f"\n4) GEÇMİŞ TESTİ — {t} {tf}, {ufuk} mum sonra lehte biten oran (taban: rastgele mumda yukarı %{tb_b:.0f} / aşağı %{tb_a:.0f}):")
    c = d.close.values
    def satir(ad, g, tb):
        r = kanit(g, tb); print(f"   %{r['oran']:3.0f} ({r['alt']:.0f}-{r['ust']:.0f}, {r['n']:3d} olay, fark {r['fark']:+3.0f}) {ad} -> {r['hukum'].split(' (')[0]}")
        return r
    sonuc = {}
    for yon, tb in (("boga", tb_b), ("ayi", tb_a)):
        sg = [(c[i + ufuk] / c[i] - 1) * (1 if yon == "boga" else -1) for i, y, _, _ in ev if y == yon and i + ufuk < len(c)]
        mg = [(c[j + ufuk] / c[j] - 1) * (1 if yon == "boga" else -1) for j, y, _ in ms if y == yon and j + ufuk < len(c)]
        sonuc[f"sup_{yon}"] = satir(f"{'dip' if yon == 'boga' else 'tepe'} süpürmesi", sg, tb)
        sonuc[f"mss_{yon}"] = satir(f"{'dip' if yon == 'boga' else 'tepe'} süpürmesi + MSS", mg, tb)
    ft = fvg_test(d, F, ufuk)
    if len(ft):
        for yon, tb in (("boga", tb_b), ("ayi", tb_a)):
            x = ft[ft.yon == yon]; ad = "boğa FVG'ye ilk dönüş" if yon == "boga" else "ayı FVG'ye ilk dönüş"
            satir(ad + " (hepsi)", x.g.tolist(), tb)
            sonuc[f"fvg_{yon}_kalite"] = satir(ad + " — itki ≥1,5 ATR + doğru bölge", x[(x.itki >= 1.5) & x.uygun_bolge].g.tolist(), tb)
            satir(ad + " — itki hacmi ≥1,5x", x[x.hac >= 1.5].g.tolist(), tb)
    # 5) A+ kontrol listesi
    yon = "boga" if (son_ev and son_ev[-1][1] == "boga") or (not son_ev and ub >= 0) else "ayi"
    lehte = "boga" == yon; ip = []
    ip.append((f"{ust_tf} yönü kurulumla uyumlu", (ub > 0) == lehte and ub != 0))
    ip.append(("son 15 mumda lehte likidite süpürmesi", any(e[1] == yon for e in son_ev)))
    ip.append(("süpürme sonrası MSS onayı", any(x[1] == yon and x[2] >= len(d) - 15 for x in ms)))
    ip.append(("lehte, kalite ≥3 açık FVG fiyata %8 yakın", any(p >= 3 and f["yon"] == yon and abs((f["alt"] + f["ust"]) / 2 / fiy - 1) < 0.08 for p, f in sira)))
    hi, lo = d.high.iloc[-40:].max(), d.low.iloc[-40:].min(); konum = (fiy - lo) / (hi - lo + 1e-9)
    ip.append(("fiyat doğru bölgede (boğa için indirim <%50, ayı için prim >%50)", konum < .5 if lehte else konum > .5))
    ip.append(("SMT lehte", ("BOĞA" in s) if lehte else ("AYI" in s)))
    k = sonuc.get(f"mss_{yon}"); ip.append(("bu enstrümanda süpürme+MSS geçmişte tabanı geçiyor", bool(k and k["fark"] >= 8 and k["n"] >= 10)))
    puan = sum(ok for _, ok in ip)
    try:
        import os; yol = os.path.join(os.path.dirname(os.path.abspath(__file__)), "smc_karne.json")
        kj = json.load(open(yol)) if os.path.exists(yol) else {}
        kj[f"{t}|{tf}"] = {"tarih": f"{d.index[-1]:%d.%m.%Y}", **{k_: {"oran": round(v["oran"]), "n": v["n"], "fark": round(v["fark"]), "hukum": v["hukum"].split(" (")[0]} for k_, v in sonuc.items()}}
        json.dump(kj, open(yol, "w"), ensure_ascii=False, indent=1)
    except Exception: pass
    print(f"\n5) A+ KURULUM KONTROL LİSTESİ ({'BOĞA' if lehte else 'AYI'} tarafı): {puan}/7")
    for ad, ok in ip: print(f"   [{'x' if ok else ' '}] {ad}")
    print(f"\nBASİT HÜKÜM: {'A+ kurulum' if puan >= 6 else 'B kurulum, küçük pozisyon / onay bekle' if puan >= 4 else 'kurulum yok, bekle'} "
          f"({puan}/7). Fiyat son 40 mumun aralığının %{konum * 100:.0f}'inde.")

if __name__ == "__main__":
    main()

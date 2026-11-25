#!/usr/bin/env python3
"""teknik_plus.py — Enes 26.11 00:00 "daha da geliştir".
Kullanım: python3 invest/teknik_plus.py <T>      (ör. AVGO, ^NDX)
1) BENZER GÜNLER: bugünün teknik parmak izine en çok benzeyen geçmiş günler (en yakın komşu) ve sonrasında ne oldu.
2) BEKLENEN HAREKET: son 20 günün oynaklığından 1 hafta / 1 ay olası aralık (±1σ ~ %68) ve oynaklık rejimi.
3) MEVSİMSELLİK: içinde bulunulan ayın ve önümüzdeki 20 işlem gününün bu hissede tarihsel ortalaması.
4) GÖRELİ GÜÇ: QQQ ve sektör ETF'ine göre 20/60 gün fark, göreli güç çizgisi 3 ay dibinde mi tepesinde mi.
5) TEPE RİSKİ SKORU 0-100 (dip tarafının aynası) ve tek cümle BASİT HÜKÜM.
Otomatik tweet YOK; Enes'in analiz kalitesi için.
"""
import sys, warnings
import numpy as np, pandas as pd
warnings.filterwarnings("ignore")
from dip_tepe import yahoo, isaretler

SEKTOR = {"AVGO": "SOXX", "NVDA": "SOXX", "AMD": "SOXX", "SITM": "SOXX", "MU": "SOXX", "KLAC": "SOXX", "CRDO": "SOXX",
          "RKLB": "ITA", "AXON": "ITA", "VRT": "XLI", "DOCN": "IGV", "NBIS": "IGV", "CBRS": "IGV", "CRWV": "IGV",
          "TSLA": "XLY", "ANET": "IGV", "COHR": "SOXX"}

def ozellik(d):
    import pandas_ta as ta
    c = d.close; atr = ta.atr(d.high, d.low, c, 14); e200 = ta.ema(c, 200 if len(c) > 260 else 50)
    vol = c.pct_change().rolling(20).std()
    return pd.DataFrame({
        "g20": c.pct_change(20), "g5": c.pct_change(5), "rsi": ta.rsi(c, 14),
        "uz200": (c - e200) / atr, "dd": c / c.rolling(252, min_periods=60).max() - 1,
        "volp": vol.rolling(252, min_periods=60).rank(pct=True)}).dropna()

def benzer(d, k=12):
    f = ozellik(d); z = (f - f.mean()) / f.std(); bug = z.iloc[-1]
    gecmis = z.iloc[:-60]; mes = ((gecmis - bug) ** 2).sum(axis=1).sort_values()
    secilen = []
    for t in mes.index:
        if all(abs((t - s).days) > 30 for s in secilen): secilen.append(t)
        if len(secilen) == k: break
    c = d.close; sonuc = []
    for t in secilen:
        i = c.index.get_loc(t)
        sonuc.append({"tarih": t, **{f"f{h}": (c.iloc[i + h] / c.iloc[i] - 1) * 100 for h in (5, 20, 60) if i + h < len(c)}})
    return pd.DataFrame(sonuc)

def beklenen(d):
    r = np.log(d.close).diff(); s20 = r.iloc[-20:].std(); fiy = d.close.iloc[-1]
    yuz = r.rolling(20).std().rank(pct=True).iloc[-1] * 100
    return {h: (fiy * np.exp(-s20 * np.sqrt(n)), fiy * np.exp(s20 * np.sqrt(n))) for h, n in (("1 hafta", 5), ("1 ay", 21))}, s20 * np.sqrt(252) * 100, yuz

def mevsim(d):
    c = d.close; ay = c.index[-1].month
    aylik = c.resample("ME").last().pct_change().dropna() * 100
    a = aylik[aylik.index.month == ay]
    ileri = []
    for y in sorted(set(c.index.year))[:-1]:
        g = c[(c.index.year == y) & (c.index.month == ay) & (c.index.day >= c.index[-1].day)]
        if len(g):
            i = c.index.get_loc(g.index[0])
            if i + 20 < len(c): ileri.append((c.iloc[i + 20] / c.iloc[i] - 1) * 100)
    return ay, a, np.array(ileri)

def goreli(t, d):
    out = []
    for b in (["^GSPC", "RSP"] if t in ("^NDX", "QQQ", "NQ=F") else ["QQQ"]) + ([SEKTOR[t]] if t in SEKTOR else []):
        if b == t: continue
        try:
            bc = yahoo(b, rng="2y").close; c = d.close.reindex(bc.index).dropna(); bc = bc.reindex(c.index)
            rs = c / bc; f20 = (c.pct_change(20) - bc.pct_change(20)).iloc[-1] * 100; f60 = (c.pct_change(60) - bc.pct_change(60)).iloc[-1] * 100
            son63 = rs.iloc[-63:]; konum = (rs.iloc[-1] - son63.min()) / (son63.max() - son63.min() + 1e-12)
            out.append((b, f20, f60, konum))
        except Exception: pass
    return out

def main(t):
    d = yahoo(t); fiy = d.close.iloc[-1]; tarih = d.index[-1].strftime("%d.%m.%Y")
    print(f"== {t} {fiy:,.2f} ({tarih})")
    b = benzer(d)
    print(f"\n1) BENZER GÜNLER — bugünün parmak izine (20g/5g getiri, RSI, 200G uzaklığı, zirveden düşüş, oynaklık) en çok benzeyen {len(b)} geçmiş gün:")
    for _, r in b.iterrows():
        print(f"   {r.tarih:%d.%m.%Y}  5g {r.get('f5', np.nan):+6.1f}%  20g {r.get('f20', np.nan):+6.1f}%  60g {r.get('f60', np.nan):+6.1f}%")
    ozet = {}
    for h in (5, 20, 60):
        s = b[f"f{h}"].dropna()
        if len(s): ozet[h] = (s.median(), (s > 0).mean() * 100, s.min(), s.max())
    for h, (m, p, mn, mx) in ozet.items():
        print(f"   -> {h:2d} gün sonra: medyan {m:+.1f}%, yukarıda biten %{p:.0f}, en kötü {mn:+.1f}%, en iyi {mx:+.1f}%")
    bh, yil, yuz = beklenen(d)
    print(f"\n2) BEKLENEN HAREKET (20 günlük oynaklık yıllık %{yil:.0f}, son 1 yılın %{yuz:.0f}. yüzdeliği -> {'YÜKSEK oynaklık' if yuz > 80 else 'DÜŞÜK oynaklık' if yuz < 20 else 'normal'}):")
    for h, (a, u) in bh.items(): print(f"   {h}: {a:,.2f} – {u:,.2f}  (~%68 olasılık bandı, ±%{(u / fiy - 1) * 100:.1f})")
    ay, a, ileri = mevsim(d)
    AY = "Ocak Şubat Mart Nisan Mayıs Haziran Temmuz Ağustos Eylül Ekim Kasım Aralık".split()
    print(f"\n3) MEVSİMSELLİK: {AY[ay - 1]} ayı {len(a)} yılda ort {a.mean():+.1f}%, yükselen yıl %{(a > 0).mean() * 100:.0f}")
    if len(ileri): print(f"   bugünkü takvim gününden sonraki 20 işlem günü: {len(ileri)} yılda medyan {np.median(ileri):+.1f}%, yükselen %{(ileri > 0).mean() * 100:.0f}")
    g = goreli(t, d)
    if g:
        print("\n4) GÖRELİ GÜÇ:")
        for bn, f20, f60, k in g:
            print(f"   {bn}'ya göre 20g {f20:+.1f} puan, 60g {f60:+.1f} puan; göreli güç çizgisi 3 aylık aralığın %{k * 100:.0f}'inde"
                  + (" (3 ay DİBİNDE: liderlik kaybı)" if k < .1 else " (3 ay TEPESİNDE: lider)" if k > .9 else ""))
    vix = yahoo("^VXN" if t in ("^NDX", "QQQ", "NQ=F") else "^VIX").close
    DIP, TEPE, tr, atr = isaretler(d, vix)
    tp = int(TEPE.astype(int).rolling(5).max().sum(axis=1).iloc[-1]); dp = int(DIP.astype(int).rolling(5).max().sum(axis=1).iloc[-1])
    rsi = tr.rsi.iloc[-1]; uz = (fiy - tr.e200.iloc[-1]) / atr.iloc[-1]
    tepe = tp * 6 + max(0, rsi - 60) * 1.2 + max(0, uz - 3) * 5 + (10 if yuz > 80 and tr.c.iloc[-1] > tr.e20.iloc[-1] else 0)
    if g: tepe += 10 if g[0][3] < .2 and tr.c.iloc[-1] > tr.e50.iloc[-1] else 0
    tepe = int(min(100, max(0, tepe)))
    print(f"\n5) TEPE RİSKİ SKORU: {tepe}/100 ({'YÜKSEK' if tepe >= 60 else 'ORTA' if tepe >= 35 else 'DÜŞÜK'}) — tepe işaretleri {tp}/10, RSI {rsi:.0f}, 200G'den {uz:+.1f} ATR")
    m20 = ozet.get(20, (0, 50, 0, 0))
    print("\nBASİT HÜKÜM:")
    print(f"   Geçmişte bugüne en çok benzeyen {len(b)} günün %{m20[1]:.0f}'inde {'endeks' if t.startswith('^') or t=='QQQ' else 'hisse'} 1 ay sonra yukarıdaydı (medyan {m20[0]:+.1f}%).")
    print(f"   Önümüzdeki hafta için normal aralık {bh['1 hafta'][0]:,.0f} – {bh['1 hafta'][1]:,.0f}; bunun dışına çıkış haber/kırılım demek.")
    print(f"   Dip işaretleri {dp}/10, tepe riski {tepe}/100: " + ("düşüş tarafı yorgun, tepe riski yok." if dp >= 5 and tepe < 35 else
          "yükseliş uzamış, kâr satışı riski arttı." if tepe >= 60 else "net bir uç yok, seviyelere göre hareket."))

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "^NDX")

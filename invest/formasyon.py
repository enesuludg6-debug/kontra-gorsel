#!/usr/bin/env python3
"""formasyon.py — otomatik trend çizgileri, formasyon tanıma, boşluk (gap) tespiti, otomatik Fibonacci; çoklu zaman dilimi.
Kullanım: python3 invest/formasyon.py <T> [--tf 1d|1wk|4h] [--mtf] [--png g/x.png]
- TREND ÇİZGİLERİ: salınım diplerinden/tepelerinden geçen tüm çizgi adayları; dokunma sayısı (0,3 ATR tolerans), ihlal yok,
  yakınlık ve süreye göre puanlanır; en iyi destek ve direnç çizgisinin BUGÜNKÜ değeri. --mtf: haftalık çizgiler de (kesikli).
- FORMASYONLAR: ikili dip/tepe, omuz-baş-omuz (ve ters), yükselen/alçalan/simetrik üçgen, yükselen/düşen kama, bayrak.
  Her biri için boyun çizgisi / kırılım seviyesi, ölçülen hedef, ONAY durumu ve BU HİSSEDE geçmiş başarısı (kanıt kuralı, taban oran).
- BOŞLUKLAR: doldurulmamış açılış boşlukları (gap) ve büyüklükleri.
- OTOMATİK FİBONACCI: son büyük dalga (120 mum) 0,382/0,5/0,618/0,786 ve uzantı 1,272/1,618.
"""
import sys, warnings
import numpy as np, pandas as pd
warnings.filterwarnings("ignore")
from veri_kalite import kanit

def yukle(t, tf):
    if tf == "1d":
        from gosterge import veri; return veri(t, "10y")
    if tf == "1wk":
        from gosterge import veri; d = veri(t, "20y")
        return d.resample("W-FRI").agg({"open": "first", "high": "max", "low": "min", "close": "last", "volume": "sum"}).dropna()
    from smc_ek import gun_ici; return gun_ici(t, tf)

def atr(d, n=14):
    tr = pd.concat([d.high - d.low, (d.high - d.close.shift()).abs(), (d.low - d.close.shift()).abs()], axis=1).max(axis=1)
    return tr.rolling(n).mean().bfill()

def pivotlar(d, n=5):
    h, l = d.high.values, d.low.values; P = []
    for i in range(n, len(d) - n):
        if h[i] == h[i - n:i + n + 1].max(): P.append((i, h[i], "T"))
        if l[i] == l[i - n:i + n + 1].min(): P.append((i, l[i], "D"))
    P.sort(); Z = []
    for p in P:   # zigzag: art arda aynı tür -> uç olanı tut
        if Z and Z[-1][2] == p[2]:
            if (p[2] == "T" and p[1] > Z[-1][1]) or (p[2] == "D" and p[1] < Z[-1][1]): Z[-1] = p
        else: Z.append(p)
    return Z

def trend_cizgileri(d, A, tur="D", bak=250, n=3):
    x = d.iloc[-bak:]; ofs = len(d) - len(x); P = [p for p in pivotlar(x, n) if p[2] == tur]
    seri = x.low.values if tur == "D" else x.high.values; kap = x.close.values; a = A.iloc[-bak:].values; m = len(x)
    en = []
    for i in range(len(P)):
        for j in range(i + 1, len(P)):
            (i1, p1, _), (i2, p2, _) = P[i], P[j]
            if i2 - i1 < 5: continue
            eg = (p2 - p1) / (i2 - i1); hat = p1 + eg * (np.arange(m) - i1); tol = 0.3 * a
            ihlal = (kap[i1:] < hat[i1:] - tol[i1:]).sum() if tur == "D" else (kap[i1:] > hat[i1:] + tol[i1:]).sum()
            if ihlal > 1: continue
            dok = sum(1 for (pi, pv, _) in P if pi >= i1 and abs(pv - hat[pi]) <= tol[pi])
            if dok < 3: continue
            uz = (kap[-1] - hat[-1]) / a[-1]
            if (tur == "D" and not (-0.5 <= uz <= 6)) or (tur == "T" and not (-6 <= uz <= 0.5)): continue
            puan = dok * 3 + (i2 / m) * 4 + min(3, (m - i1) / 60) - abs(uz) * 0.5
            en.append({"puan": puan, "dokunma": dok, "egim": eg, "bugun": hat[-1], "i1": i1 + ofs, "p1": p1, "i2": i2 + ofs, "p2": p2,
                       "uzaklik_atr": (kap[-1] - hat[-1]) / a[-1]})
    sec = []
    for z in sorted(en, key=lambda z: -z["puan"]):
        if all(abs(z["bugun"] / y["bugun"] - 1) > 0.015 for y in sec): sec.append(z)
        if len(sec) == 2: break
    return sec

def formasyonlar(d, A, n=5):
    Z = pivotlar(d, n); c = d.close.values; F = []
    for k in range(4, len(Z)):
        p = Z[k - 4:k + 1]; tipler = "".join(z[2] for z in p); a = A.iloc[p[-1][0]]
        # ikili dip/tepe: son üç pivot D T D veya T D T
        q = Z[k - 2:k + 1]; t3 = "".join(z[2] for z in q)
        if t3 in ("DTD", "TDT") and 8 <= q[2][0] - q[0][0] <= 80:
            yak = abs(q[2][1] - q[0][1]) <= 0.6 * a; boy = abs(q[1][1] - q[0][1])
            if yak and boy >= 2 * a:
                ad = "ikili dip" if t3 == "DTD" else "ikili tepe"; yon = 1 if t3 == "DTD" else -1
                F.append({"ad": ad, "yon": yon, "bas": q[0][0], "son": q[2][0], "kirilim": q[1][1], "hedef": q[1][1] + yon * boy, "geçersiz": min(q[0][1], q[2][1]) if yon > 0 else max(q[0][1], q[2][1])})
        if tipler in ("TDTDT", "DTDTD"):
            s1, b, s2 = p[0][1], p[2][1], p[4][1]; n1, n2 = p[1][1], p[3][1]
            if tipler == "TDTDT" and b > max(s1, s2) + a and abs(s1 - s2) <= 1.5 * a:
                boyun = (n1 + n2) / 2; F.append({"ad": "omuz-baş-omuz", "yon": -1, "bas": p[0][0], "son": p[4][0], "kirilim": boyun, "hedef": boyun - (b - boyun), "geçersiz": s2})
            if tipler == "DTDTD" and b < min(s1, s2) - a and abs(s1 - s2) <= 1.5 * a:
                boyun = (n1 + n2) / 2; F.append({"ad": "ters omuz-baş-omuz", "yon": 1, "bas": p[0][0], "son": p[4][0], "kirilim": boyun, "hedef": boyun + (boyun - b), "geçersiz": s2})
            # üçgen / kama: tepeler ve dipler üzerinden eğim
            T_ = [z for z in p if z[2] == "T"]; D_ = [z for z in p if z[2] == "D"]
            if len(T_) >= 2 and len(D_) >= 2:
                et = (T_[-1][1] - T_[0][1]) / (T_[-1][0] - T_[0][0]); ed = (D_[-1][1] - D_[0][1]) / (D_[-1][0] - D_[0][0])
                duz = 0.05 * a; gen0 = T_[0][1] - D_[0][1]; gen1 = T_[-1][1] - D_[-1][1]
                if gen1 < gen0 * 0.8:
                    if abs(et) < duz and ed > duz: ad, yon = "yükselen üçgen", 1
                    elif abs(ed) < duz and et < -duz: ad, yon = "alçalan üçgen", -1
                    elif et < -duz and ed > duz: ad, yon = "simetrik üçgen", 0
                    elif et > duz and ed > duz: ad, yon = "yükselen kama", -1
                    elif et < -duz and ed < -duz: ad, yon = "düşen kama", 1
                    else: ad = None
                    if ad:
                        son = p[-1][0]; ust = T_[-1][1] + et * (len(d) - 1 - T_[-1][0]); alt = D_[-1][1] + ed * (len(d) - 1 - D_[-1][0])
                        F.append({"ad": ad, "yon": yon, "bas": p[0][0], "son": son, "kirilim": ust if yon >= 0 else alt, "alt_cizgi": alt,
                                  "hedef": (ust + gen0) if yon >= 0 else (alt - gen0), "geçersiz": alt if yon >= 0 else ust})
    # bayrak: son 30 mumda direk (≥3 ATR, ≤10 mum) + sığ konsolidasyon
    for i in range(len(d) - 30, len(d) - 5):
        if i < 15: continue
        for yon in (1, -1):
            dir_ = (c[i] - c[i - 10]) * yon
            if dir_ >= 3 * A.iloc[i]:
                sonra = c[i:]; geri = (c[i] - (sonra.min() if yon > 0 else sonra.max())) * yon
                if 5 <= len(sonra) <= 25 and geri < 0.5 * dir_:
                    F.append({"ad": "boğa bayrağı" if yon > 0 else "ayı bayrağı", "yon": yon, "bas": i - 10, "son": len(d) - 1,
                              "kirilim": d.high.values[i:].max() if yon > 0 else d.low.values[i:].min(), "hedef": (d.high.values[i:].max() + dir_) if yon > 0 else (d.low.values[i:].min() - dir_),
                              "geçersiz": sonra.min() if yon > 0 else sonra.max()})
                    break
    # onay durumu
    for f in F:
        sonra = c[f["son"] + 1:]
        if f["yon"] > 0: onay = np.argmax(sonra > f["kirilim"]) if (sonra > f["kirilim"]).any() else -1
        elif f["yon"] < 0: onay = np.argmax(sonra < f["kirilim"]) if (sonra < f["kirilim"]).any() else -1
        else: onay = -1
        f["onay_i"] = f["son"] + 1 + onay if onay >= 0 else None
    return F

def gecmis_basari(d, F, ufuk=20):
    c = d.close.values; t = (pd.Series(c).shift(-ufuk) / pd.Series(c) - 1).dropna()
    sonuc = {}
    for ad in sorted(set(f["ad"] for f in F)):
        g = []; yon = [f["yon"] for f in F if f["ad"] == ad][0] or 1
        for f in F:
            if f["ad"] == ad and f["onay_i"] is not None and f["onay_i"] + ufuk < len(c):
                g.append(yon * (c[f["onay_i"] + ufuk] / c[f["onay_i"]] - 1))
        tb = ((t > 0) if yon > 0 else (t < 0)).mean() * 100
        if g: sonuc[ad] = kanit(g, tb)
    return sonuc

def bosluklar(d, A, bak=250):
    x = d.iloc[-bak:]; o, h, l = x.open.values, x.high.values, x.low.values; out = []
    for i in range(1, len(x)):
        if l[i] > h[i - 1] and (l[i] - h[i - 1]) > 0.3 * A.iloc[-bak + i]:
            if l[i + 1:].min(initial=np.inf) > h[i - 1]: out.append(("yukarı", h[i - 1], l[i], x.index[i]))
        if h[i] < l[i - 1] and (l[i - 1] - h[i]) > 0.3 * A.iloc[-bak + i]:
            if h[i + 1:].max(initial=-np.inf) < l[i - 1]: out.append(("aşağı", h[i], l[i - 1], x.index[i]))
    return out[-6:]

def oto_fib(d, bak=120):
    x = d.iloc[-bak:]; ih, il = x.high.values.argmax(), x.low.values.argmin(); H, L = x.high.max(), x.low.min()
    if ih > il: yon, sev = "yukarı dalga (dipten tepeye)", {r: H - (H - L) * r for r in (0.382, 0.5, 0.618, 0.786)} | {1.272: L + (H - L) * 1.272, 1.618: L + (H - L) * 1.618}
    else: yon, sev = "aşağı dalga (tepeden dibe)", {r: L + (H - L) * r for r in (0.382, 0.5, 0.618, 0.786)} | {1.272: H - (H - L) * 1.272, 1.618: H - (H - L) * 1.618}
    return yon, H, L, sev

def rapor(t, tf, d):
    A = atr(d); fiy = d.close.iloc[-1]; fmt = "%d.%m.%Y" if tf != "4h" else "%d.%m %H:%M"
    print(f"\n== {t} {tf} {fiy:,.2f} ({d.index[-1]:{fmt}})")
    print("TREND ÇİZGİLERİ (en güçlü 2 destek / 2 direnç, bugünkü değer):")
    for tur, ad in (("D", "destek"), ("T", "direnç")):
        L_ = trend_cizgileri(d, A, tur)
        if not L_: print(f"   {ad}: geçerli çizgi yok")
        for z in L_:
            print(f"   {ad:<7} bugün {z['bugun']:,.2f} (fiyata {(z['bugun'] / fiy - 1) * 100:+.1f}%, {z['uzaklik_atr']:+.1f} ATR) | {z['dokunma']} dokunma | "
                  f"{d.index[z['i1']]:{fmt}} {z['p1']:,.2f} -> {d.index[z['i2']]:{fmt}} {z['p2']:,.2f} | eğim {'yukarı' if z['egim'] > 0 else 'aşağı'}")
    F = formasyonlar(d, A); B = gecmis_basari(d, F)
    son = [f for f in F if f["son"] >= len(d) - 40]
    print("FORMASYONLAR (son 40 mum; geçmiş başarısı bu hissenin kendi geçmişinden, onay sonrası 20 mum):")
    if not son: print("   yok")
    gor = set()
    for f in sorted(son, key=lambda z: -z["son"]):
        if f["ad"] in gor: continue
        gor.add(f["ad"]); b = B.get(f["ad"])
        dur = f"ONAYLI ({d.index[f['onay_i']]:{fmt}})" if f["onay_i"] is not None else f"onay bekliyor: {f['kirilim']:,.2f} {'üstü' if f['yon'] >= 0 else 'altı'} kapanış"
        print(f"   {f['ad']:<20} {dur} | ölçülen hedef {f['hedef']:,.2f} | geçersiz {f['geçersiz']:,.2f}"
              + (f" | geçmiş: {b['n']} olay %{b['oran']:.0f} (taban %{b['taban']:.0f}) {b['hukum'].split(' (')[0]}" if b else " | geçmiş: olay yok"))
    G = bosluklar(d, A)
    print("DOLDURULMAMIŞ BOŞLUKLAR:" + ("" if G else " yok"))
    for y, a_, b_, tt in G: print(f"   {y:<6} {a_:,.2f} – {b_:,.2f} ({tt:{fmt}}, fiyata {((a_ + b_) / 2 / fiy - 1) * 100:+.1f}%)")
    yon, H, L, sev = oto_fib(d)
    print(f"OTOMATİK FİBONACCI ({yon}, {L:,.2f} – {H:,.2f}): " + ", ".join(f"{k}: {v:,.2f}" for k, v in sev.items()))
    return F

def main():
    a = sys.argv[1:]; t = a[0] if a else "^NDX"; tf = a[a.index("--tf") + 1] if "--tf" in a else "1d"
    d = yukle(t, tf); rapor(t, tf, d)
    if "--mtf" in a:
        ust = {"4h": "1d", "1d": "1wk"}.get(tf)
        if ust: rapor(t, ust, yukle(t, ust))

if __name__ == "__main__":
    main()

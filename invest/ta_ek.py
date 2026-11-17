#!/usr/bin/env python3
"""TEKNIK ANALIZ EKLERI (kesin kural 33, Enes 17.11 21:37: "teknik analizle ilgili her seyi arastir, gelistir, bir sey cikarma, sadece ekle").
ta2.py'ye DOKUNMAZ; onun 21 gostergesine ek olarak calisir. Kullanim:
  python3 invest/ta_ek.py DOCN RKLB ... > /tmp/ek.txt          # her sembol icin ek bolumler
  python3 invest/ta_ek.py --karne                                # seviye_takip.csv: verilen kademeler tuttu mu
Bolumler: MTF hizalama | goreli guc (QQQ + sektor ETF) | hacim (RVOL, kuruma) | sikisma (BB-Keltner, bant genisligi yuzdeligi)
| haftalik pivot + onceki gun/hafta tepe-dip | RSI/MACD uyumsuzlugu (swing tabanli) | son mum formasyonu | acik fiyat bosluklari
| kanal/ucgen ipucu (regresyon) | 52 hafta uzaklik | anchored VWAP (52h dip ve son ana tepe) | olcumlu hareket hedefi
"""
import json, sys, urllib.request, datetime as dt, math, csv, os
UA = {"User-Agent": "Mozilla/5.0"}
SEKTOR = {"NVDA": "SMH", "AMD": "SMH", "AVGO": "SMH", "TSM": "SMH", "MU": "SMH", "SITM": "SMH", "MRVL": "SMH", "ALAB": "SMH", "CRDO": "SMH",
          "ON": "SMH", "AAOI": "SMH", "COHR": "SMH", "LITE": "SMH", "ANET": "SMH", "DOCN": "IGV", "CRWD": "IGV", "NET": "IGV", "DDOG": "IGV",
          "SNOW": "IGV", "PLTR": "IGV", "APP": "IGV", "RBRK": "IGV", "ORCL": "IGV", "MSFT": "IGV", "RKLB": "UFO", "ASTS": "UFO", "PL": "UFO",
          "LUNR": "UFO", "AXON": "XLI", "VRT": "XLI", "ETN": "XLI", "GEV": "XLI", "CBRS": "SMH", "HOOD": "XLF", "ISRG": "XLV", "TEM": "XLV",
          "ECL": "XLB", "CRWV": "IGV", "NBIS": "IGV", "GOOGL": "XLC", "META": "XLC", "AMZN": "XLY"}

def fetch(s, iv, rng):
    u = f"https://query1.finance.yahoo.com/v8/finance/chart/{s}?range={rng}&interval={iv}"
    d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=20))["chart"]["result"][0]
    q = d["indicators"]["quote"][0]; t = d["timestamp"]
    return [(t[i], q["open"][i], q["high"][i], q["low"][i], q["close"][i], q["volume"][i] or 0) for i in range(len(t))
            if q["close"][i] is not None and q["high"][i] is not None and q["open"][i] is not None]

def resample4(r):
    gun = {}; o = []
    for x in r: gun.setdefault(dt.datetime.utcfromtimestamp(x[0] - 5 * 3600).date(), []).append(x)
    for d in sorted(gun):
        b = gun[d]
        for i in range(0, len(b), 4):
            g = b[i:i + 4]; o.append((g[0][0], g[0][1], max(x[2] for x in g), min(x[3] for x in g), g[-1][4], sum(x[5] for x in g)))
    return o

def ema(a, n):
    k = 2 / (n + 1); e = a[0]; o = []
    for x in a: e = x * k + e * (1 - k); o.append(e)
    return o
def sma(a, n): return [None] * (n - 1) + [sum(a[i - n + 1:i + 1]) / n for i in range(n - 1, len(a))]
def sd(a, n): return [None] * (n - 1) + [(sum((x - sum(a[i - n + 1:i + 1]) / n) ** 2 for x in a[i - n + 1:i + 1]) / n) ** .5 for i in range(n - 1, len(a))]
def atr(r, n=20):
    tr = [r[0][2] - r[0][3]] + [max(r[i][2] - r[i][3], abs(r[i][2] - r[i - 1][4]), abs(r[i][3] - r[i - 1][4])) for i in range(1, len(r))]
    return ema(tr, n)
def rsi(c, n=14):
    g = [0] + [max(c[i] - c[i - 1], 0) for i in range(1, len(c))]; l = [0] + [max(c[i - 1] - c[i], 0) for i in range(1, len(c))]
    ag, al = ema(g, 2 * n - 1), ema(l, 2 * n - 1)
    return [100 if al[i] == 0 else 100 - 100 / (1 + ag[i] / al[i]) for i in range(len(c))]
def swings(h, l, k=5):
    SH = [(i, h[i]) for i in range(k, len(h) - k) if h[i] == max(h[i - k:i + k + 1])]
    SL = [(i, l[i]) for i in range(k, len(l) - k) if l[i] == min(l[i - k:i + k + 1])]
    return SH, SL
def trend(r):
    c = [x[4] for x in r]; e20, e50 = ema(c, 20)[-1], ema(c, 50)[-1]; e200 = ema(c, 200)[-1] if len(c) >= 200 else None
    sc = (1 if e20 > e50 else -1) + (1 if (e200 and c[-1] > e200) else -1 if e200 else 0)
    return "+" if sc >= 2 else "-" if sc <= -2 else "0"
def linreg(y):
    n = len(y); xs = range(n); mx = (n - 1) / 2; my = sum(y) / n
    b = sum((x - mx) * (v - my) for x, v in zip(xs, y)) / sum((x - mx) ** 2 for x in xs); a = my - b * mx
    ss = sum((v - my) ** 2 for v in y) or 1; r2 = 1 - sum((v - (a + b * x)) ** 2 for x, v in zip(xs, y)) / ss
    return a, b, r2

def analiz(s, qqq, etf_cache):
    out = [f"\n######## {s} (EK)"]
    d = fetch(s, "1d", "2y")
    # haftalik mumlar gunlukten (Yahoo 1wk son satirlari kismi hafta karistirabiliyor)
    hf = {}
    for x in d: hf.setdefault(dt.datetime.utcfromtimestamp(x[0]).isocalendar()[:2], []).append(x)
    w = [(g[0][0], g[0][1], max(y[2] for y in g), min(y[3] for y in g), g[-1][4], sum(y[5] for y in g)) for _, g in sorted(hf.items())]; h1 = fetch(s, "60m", "60d"); h4 = resample4(fetch(s, "60m", "180d"))
    c = [x[4] for x in d]; hi = [x[2] for x in d]; lo = [x[3] for x in d]; v = [x[5] for x in d]; L = c[-1]
    # 1 MTF hizalama
    out.append(f"   MTF hizalama    haftalik {trend(w)} | gunluk {trend(d)} | 4s {trend(h4)} | 1s {trend(h1)}  (+ yukari, - asagi; EMA20>50 ve fiyat>EMA200)")
    # 2 goreli guc
    def ret(a, n): return (a[-1] / a[-1 - n] - 1) * 100 if len(a) > n else float('nan')
    qc = [x[4] for x in qqq]; e = SEKTOR.get(s.replace("^", ""), None)
    rs = f"1a {ret(c,21)-ret(qc,21):+.1f} puan, 3a {ret(c,63)-ret(qc,63):+.1f} puan (QQQ'ya gore)"
    if e:
        if e not in etf_cache: etf_cache[e] = [x[4] for x in fetch(e, "1d", "2y")]
        ec = etf_cache[e]; rs += f" | {e}'ye gore 1a {ret(c,21)-ret(ec,21):+.1f}, 3a {ret(c,63)-ret(ec,63):+.1f}"
    m = min(len(c), len(qc)); rsl = [c[-m + i] / qc[-m + i] for i in range(m)]; e20 = ema(rsl, 20)
    rs += f" | RS cizgisi {'20 gunluk ortalamasinin USTUNDE' if rsl[-1] > e20[-1] else 'altinda'}" + (" ve 3 ayin zirvesinde" if rsl[-1] >= max(rsl[-63:]) else "")
    out.append("   Goreli guc      " + rs)
    # 3 hacim
    a20 = sum(v[-21:-1]) / 20 or 1; a50 = sum(v[-51:-1]) / 50 or 1; kur = (sum(v[-5:]) / 5) / a50
    out.append(f"   Hacim           son gun RVOL {v[-1]/a20:.2f}x (20g ort.) | 5g/50g {kur:.2f}x" + (" KURUMA (hacim cekiliyor)" if kur < 0.7 else " YUKSEK ILGI" if kur > 1.5 else "")
               + f" | son 25 gunde dagitim gunu {sum(1 for i in range(-25,0) if c[i] < c[i-1]*0.998 and v[i] > v[i-1])}")
    # 4 sikisma
    def sq(r):
        cc = [x[4] for x in r]; m20 = sma(cc, 20); s20 = sd(cc, 20); at = atr(r, 20); e20 = ema(cc, 20)
        bw = [(4 * s20[i] / m20[i]) if m20[i] else None for i in range(len(cc))]
        on = [s20[i] is not None and (m20[i] + 2 * s20[i] < e20[i] + 1.5 * at[i]) and (m20[i] - 2 * s20[i] > e20[i] - 1.5 * at[i]) for i in range(len(cc))]
        sure = 0
        for x in reversed(on):
            if x: sure += 1
            else: break
        son = [b for b in bw[-126:] if b]; yz = sum(1 for b in son if b <= bw[-1]) / len(son) * 100
        mom = cc[-1] - (max(x[2] for x in r[-20:]) + min(x[3] for x in r[-20:])) / 4 - m20[-1] / 2
        ates = (not on[-1]) and on[-2]
        return f"{'SIKISMA VAR (' + str(sure) + ' mum)' if on[-1] else ('SIKISMA BITTI, yon ' + ('yukari' if mom > 0 else 'asagi')) if ates else 'yok'}; bant genisligi 6 ay yuzdeligi %{yz:.0f}" + (" (cok dar)" if yz < 15 else "")
    out.append(f"   Sikisma         gunluk {sq(d)} | 4s {sq(h4)}")
    # 5 pivot + onceki gun/hafta
    pw = w[-2]; P = (pw[2] + pw[3] + pw[4]) / 3
    out.append(f"   Haftalik pivot  P {P:.2f} | R1 {2*P-pw[3]:.2f} R2 {P+pw[2]-pw[3]:.2f} | S1 {2*P-pw[2]:.2f} S2 {P-pw[2]+pw[3]:.2f} | onceki gun T/D {d[-2][2]:.2f}/{d[-2][3]:.2f} | onceki hafta T/D {pw[2]:.2f}/{pw[3]:.2f}")
    # 6 uyumsuzluk
    def uyum(r, ad):
        hh = [x[2] for x in r]; ll = [x[3] for x in r]; cc = [x[4] for x in r]; rr = rsi(cc); SH, SL = swings(hh, ll, 3)
        m12 = [a - b for a, b in zip(ema(cc, 12), ema(cc, 26))]; o = []
        if len(SL) >= 2:
            (i1, p1), (i2, p2) = SL[-2], SL[-1]
            if p2 < p1 and rr[i2] > rr[i1]: o.append(f"{ad} POZITIF RSI uyumsuzlugu (dip {p1:.2f}->{p2:.2f}, RSI {rr[i1]:.0f}->{rr[i2]:.0f})")
            if p2 < p1 and m12[i2] > m12[i1]: o.append(f"{ad} pozitif MACD uyumsuzlugu")
            if p2 > p1 and rr[i2] < rr[i1]: o.append(f"{ad} gizli pozitif uyumsuzluk (yukselen dip, dusen RSI)")
        if len(SH) >= 2:
            (i1, p1), (i2, p2) = SH[-2], SH[-1]
            if p2 > p1 and rr[i2] < rr[i1]: o.append(f"{ad} NEGATIF RSI uyumsuzlugu (tepe {p1:.2f}->{p2:.2f}, RSI {rr[i1]:.0f}->{rr[i2]:.0f})")
        return o
    u = uyum(d, "gunluk") + uyum(h4, "4s")
    out.append("   Uyumsuzluk      " + ("; ".join(u) if u else "belirgin uyumsuzluk yok"))
    # 7 mum
    def mum(r):
        o, h, l, c_ = r[-1][1:5]; po, ph, pl, pc = r[-2][1:5]; gov = abs(c_ - o); men = h - l or 1e-9
        if gov / men < 0.1: return "doji (kararsizlik)"
        if min(o, c_) - l > 2 * gov and h - max(o, c_) < gov: return "cekic (alttan alici tepkisi)" if c_ >= o or True else ""
        if h - max(o, c_) > 2 * gov and min(o, c_) - l < gov: return "kayan yildiz (ustten satis)"
        if c_ > o and pc < po and c_ >= po and o <= pc: return "yukari yutan mum"
        if c_ < o and pc > po and o >= pc and c_ <= po: return "asagi yutan mum"
        return "belirgin mum formasyonu yok"
    out.append(f"   Son mum         gunluk {mum(d)} | 4s {mum(h4)} | haftalik {mum(w)}")
    # 8 acik bosluklar (son 60 gun)
    gaps = []
    for i in range(len(d) - 60, len(d)):
        if d[i][3] > d[i - 1][2] and min(x[3] for x in d[i:]) > d[i - 1][2]: gaps.append(f"yukari bosluk {d[i-1][2]:.2f}-{d[i][3]:.2f}")
        if d[i][2] < d[i - 1][3] and max(x[2] for x in d[i:]) < d[i - 1][3]: gaps.append(f"asagi bosluk {d[i][2]:.2f}-{d[i-1][3]:.2f}")
    out.append("   Acik bosluk     " + (", ".join(gaps[-3:]) if gaps else "yok (son 60 gun)"))
    # 9 kanal / ucgen ipucu
    def kanal(r, n, ad):
        hh = [x[2] for x in r[-n:]]; ll = [x[3] for x in r[-n:]]
        ah, bh, r2h = linreg(hh); al_, bl, r2l = linreg(ll); son = n - 1; ust = ah + bh * son; alt = al_ + bl * son
        ort = sum(x[4] for x in r[-n:]) / n; ph, pl = bh / ort * 100, bl / ort * 100
        if ph > 0.05 and pl > 0.05: t = "YUKSELEN KANAL"
        elif ph < -0.05 and pl < -0.05: t = "DUSEN KANAL"
        elif ph < -0.05 and pl > 0.05: t = "SIKISAN UCGEN (daralan)"
        elif ph > 0.05 and pl < -0.05: t = "GENISLEYEN formasyon"
        elif abs(ph) <= 0.05 and pl > 0.05: t = "YUKSELEN UCGEN (yatay tepe, yukselen dip)"
        elif ph < -0.05 and abs(pl) <= 0.05: t = "ALCALAN UCGEN (dusen tepe, yatay dip)"
        else: t = "YATAY BANT"
        guven = "guclu" if min(r2h, r2l) > 0.6 else "orta" if min(r2h, r2l) > 0.35 else "zayif"
        return f"{ad} son {n} mum: {t} ({guven}, R2 {r2h:.2f}/{r2l:.2f}); bugunku ust cizgi {ust:.2f}, alt cizgi {alt:.2f}"
    out.append("   Yapi ipucu      " + kanal(d, 40, "gunluk") + " | " + kanal(h4, 40, "4s"))
    # 10 52 hafta
    h52 = max(hi[-252:]); l52 = min(lo[-252:])
    out.append(f"   52 hafta        zirveden %{(L/h52-1)*100:.1f} ({h52:.2f}) | dipten %{(L/l52-1)*100:+.1f} ({l52:.2f})")
    # 11 anchored VWAP
    def avwap(r, i0):
        pv = sum((x[2] + x[3] + x[4]) / 3 * x[5] for x in r[i0:]); vv = sum(x[5] for x in r[i0:]) or 1; return pv / vv
    i_l = max(range(len(d) - 252, len(d)), key=lambda i: -d[i][3]); i_h = max(range(len(d) - 126, len(d)), key=lambda i: d[i][2])
    out.append(f"   Anchored VWAP   52 hafta dibinden {avwap(d, i_l):.2f} | son 6 ay tepesinden {avwap(d, i_h):.2f} (fiyat {'ustunde' if L > avwap(d, i_h) else 'altinda'})")
    # 12 olcumlu hareket (son swing araligi)
    SH, SL = swings(hi, lo, 5)
    if SH and SL:
        rng = SH[-1][1] - SL[-1][1]
        out.append(f"   Olcumlu hareket son salinim {SL[-1][1]:.2f}-{SH[-1][1]:.2f}: yukari kirilimda hedef ~{SH[-1][1]+abs(rng):.2f}, asagi kirilimda ~{SL[-1][1]-abs(rng):.2f}")
    return out

def karne():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "seviye_takip.csv")
    if not os.path.exists(p): print("seviye_takip.csv yok"); return
    R = list(csv.DictReader(open(p, encoding="utf-8"))); ozet = {"dokundu_tuttu": 0, "dokundu_kirildi": 0, "dokunmadi": 0}
    for r in R:
        d = fetch(r["ticker"], "1d", "6mo"); t0 = dt.date.fromisoformat(r["tarih"]); sonra = [x for x in d if dt.datetime.utcfromtimestamp(x[0]).date() > t0]
        if not sonra: continue
        k1a, k1u, tez = float(r["k1_alt"]), float(r["k1_ust"]), float(r["tez"])
        dok = any(x[3] <= k1u for x in sonra); kir = any(x[4] < tez for x in sonra)
        dur = "dokundu_kirildi" if dok and kir else "dokundu_tuttu" if dok else "dokunmadi"; ozet[dur] += 1
        print(f"{r['tarih']} {r['ticker']} k1 {k1a}-{k1u} tez {tez} -> {dur} (son {sonra[-1][4]:.2f})")
    print("OZET", ozet)

if __name__ == "__main__":
    a = sys.argv[1:]
    if "--karne" in a: karne(); sys.exit()
    qqq = fetch("QQQ", "1d", "2y"); cache = {}
    for s in a:
        try: print("\n".join(analiz(s, qqq, cache)))
        except Exception as e: print(f"\n######## {s} (EK) HATA {e}")

#!/usr/bin/env python3
"""TEKNİK PRO (Enes 25.11.2026 22:14 'teknik analiz yeteneklerini daha da geliştir').
smc_analiz.py'nin üstüne: çoklu zaman dilimi yön tablosu, ICT OTE (Fibonacci 0,62-0,79), premium/discount,
hacim profili (POC/VAH/VAL), anchored VWAP (son büyük dip/tepeden), ICT killzone saatleri (TSİ),
haftalık/günlük açılış boşlukları (NWOG/NDOG), ATR tabanlı otomatik senaryo planı (giriş/stop/hedef/R:R)
ve tarih eksenli, etiketli grafik.

Kullanım:
  python3 invest/teknik_pro.py ^NDX                 # tam rapor (1wk/1d/4h/1h)
  python3 invest/teknik_pro.py ^NDX --png g/x.png    # + işaretli 4h grafik
  python3 invest/teknik_pro.py NVDA --seviyeler 140,150.5,163   # Enes'in çizdiği seviyeleri de rapora kat
Onay: Enes 25.11.2026 22:11 pip (smartmoneyconcepts, pandas_ta) — skill enes-teknik-smc.
"""
import sys, warnings
import numpy as np, pandas as pd
warnings.filterwarnings("ignore")
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from smc_analiz import veri

def yon_ozet(df, sw):
    from smartmoneyconcepts import smc
    import pandas_ta as ta
    c = df.close
    shl = smc.swing_highs_lows(df, swing_length=sw)
    bc = smc.bos_choch(df, shl, close_break=True)
    son_k = bc.dropna(subset=["BOS", "CHOCH"], how="all").tail(1)
    yap = 0
    if len(son_k):
        r = son_k.iloc[0]; yap = int(r.BOS if pd.notna(r.BOS) else r.CHOCH)
    e20 = ta.ema(c, 20).iloc[-1]; e50 = ta.ema(c, 50).iloc[-1]
    st = ta.supertrend(df.high, df.low, c, 10, 3); stv = int(st.iloc[-1, 1]) if st is not None else 0
    rsi = ta.rsi(c, 14).iloc[-1]
    puan = (1 if c.iloc[-1] > e20 else -1) + (1 if e20 > e50 else -1) + stv + yap + (1 if rsi > 55 else -1 if rsi < 45 else 0)
    return {"yap": yap, "ema": "üstünde" if c.iloc[-1] > e20 else "altında", "st": stv, "rsi": rsi, "puan": puan, "shl": shl}

def hacim_profili(df, kova=40):
    lo, hi = df.low.min(), df.high.max(); b = np.linspace(lo, hi, kova + 1); v = np.zeros(kova)
    for r in df.itertuples():
        i0, i1 = np.searchsorted(b, r.low) - 1, np.searchsorted(b, r.high) - 1
        i0, i1 = max(i0, 0), min(max(i1, i0), kova - 1); v[i0:i1 + 1] += (r.volume or 0) / (i1 - i0 + 1)
    poc = v.argmax(); tot = v.sum(); sec = {poc}; s = v[poc]; lo_i = hi_i = poc
    while s < 0.7 * tot and (lo_i > 0 or hi_i < kova - 1):
        a = v[lo_i - 1] if lo_i > 0 else -1; c = v[hi_i + 1] if hi_i < kova - 1 else -1
        if c >= a: hi_i += 1; s += v[hi_i]
        else: lo_i -= 1; s += v[lo_i]
    m = lambda i: (b[i] + b[i + 1]) / 2
    return m(poc), b[hi_i + 1], b[lo_i]

def avwap(df, i0):
    d = df.iloc[i0:]; tp = (d.high + d.low + d.close) / 3; vol = d.volume.replace(0, np.nan).fillna(1)
    return float((tp * vol).sum() / vol.sum())

def main(a):
    t = a[0]
    seviyeler = [float(x) for x in a[a.index("--seviyeler") + 1].split(",")] if "--seviyeler" in a else []
    tf = {"1wk": 5, "1d": 10, "4h": 6, "1h": 6}; R = {}; D = {}
    for k, sw in tf.items():
        try: D[k] = veri(t, k); R[k] = yon_ozet(D[k], sw)
        except Exception as e: print("veri yok", k, e)
    son = D["1h"].close.iloc[-1] if "1h" in D else D["1d"].close.iloc[-1]
    print(f"== {t}  son {son:,.1f}")
    print("ÇOKLU ZAMAN DİLİMİ (puan -5..+5; yapı = son BOS/CHoCH yönü)")
    for k, r in R.items():
        print(f"  {k:4} yapı {'YUKARI' if r['yap'] > 0 else 'AŞAĞI' if r['yap'] < 0 else '-':6} | EMA20 {r['ema']:8} | Supertrend {'+' if r['st'] > 0 else '-'} | RSI {r['rsi']:.0f} | puan {r['puan']:+d}")
    top = sum(r["puan"] for r in R.values())
    print(f"  TOPLAM {top:+d} -> {'GÜÇLÜ YUKARI' if top >= 8 else 'YUKARI' if top >= 3 else 'GÜÇLÜ AŞAĞI' if top <= -8 else 'AŞAĞI' if top <= -3 else 'KARARSIZ'}")
    # dealing range + OTE (günlük son büyük swing)
    d1 = D["1d"]; shl = R["1d"]["shl"].dropna(subset=["HighLow"])
    sh = shl[shl.HighLow == 1].Level.iloc[-1]; sl = shl[shl.HighLow == -1].Level.iloc[-1]
    ih = d1.index[R["1d"]["shl"].HighLow == 1][-1]; il = d1.index[R["1d"]["shl"].HighLow == -1][-1]
    asagi = ih < il  # son hareket tepeden dibe
    rng = sh - sl; eq = sl + rng / 2
    print(f"DEALING RANGE (günlük swing) dip {sl:,.0f} ({il:%d.%m}) – tepe {sh:,.0f} ({ih:%d.%m}); denge {eq:,.0f}; fiyat {'PREMIUM' if son > eq else 'DISCOUNT'}")
    if asagi:
        o1, o2, o3 = sl + rng * 0.62, sl + rng * 0.705, sl + rng * 0.79
        print(f"  OTE (düşüş dalgasına geri çekilme, satış bölgesi) 0,62 {o1:,.0f} | 0,705 {o2:,.0f} | 0,79 {o3:,.0f}")
    else:
        o1, o2, o3 = sh - rng * 0.62, sh - rng * 0.705, sh - rng * 0.79
        print(f"  OTE (yükseliş dalgasına geri çekilme, alış bölgesi) 0,62 {o1:,.0f} | 0,705 {o2:,.0f} | 0,79 {o3:,.0f}")
    # 4h içi kısa dalga OTE
    h4 = D["4h"]; s4 = R["4h"]["shl"].dropna(subset=["HighLow"]).tail(2)
    if len(s4) == 2:
        a_, b_ = s4.Level.iloc[0], s4.Level.iloc[1]; lo_, hi_ = min(a_, b_), max(a_, b_); r4 = hi_ - lo_
        if s4.HighLow.iloc[-1] == 1: print(f"  4h son dalga yukarı {lo_:,.0f}->{hi_:,.0f}: geri çekilme OTE {hi_ - r4*0.62:,.0f}–{hi_ - r4*0.79:,.0f}")
        else: print(f"  4h son dalga aşağı {hi_:,.0f}->{lo_:,.0f}: tepki OTE {lo_ + r4*0.62:,.0f}–{lo_ + r4*0.79:,.0f}")
    # hacim profili + AVWAP
    if "1h" in D and D["1h"].volume.sum() > 0:
        poc, vah, val = hacim_profili(D["1h"].tail(140))
        print(f"HACİM PROFİLİ (son ~20 seans, 1h) POC {poc:,.0f} | değer alanı {val:,.0f}–{vah:,.0f}")
    print(f"ANCHORED VWAP: son büyük tepeden ({ih:%d.%m}) {avwap(d1, d1.index.get_loc(ih)):,.0f} | son büyük dipten ({il:%d.%m}) {avwap(d1, d1.index.get_loc(il)):,.0f}")
    # açılış boşlukları
    w = D["1d"].copy(); w["hafta"] = w.index.to_period("W")
    gw = w.groupby("hafta"); ac = gw.open.first(); kp = gw.close.last()
    if len(ac) >= 2: print(f"NWOG (son haftalık açılış boşluğu) {min(kp.iloc[-2], ac.iloc[-1]):,.0f}–{max(kp.iloc[-2], ac.iloc[-1]):,.0f}")
    print(f"NDOG (son günlük açılış boşluğu) {min(d1.close.iloc[-2], d1.open.iloc[-1]):,.0f}–{max(d1.close.iloc[-2], d1.open.iloc[-1]):,.0f}")
    print("ICT KILLZONE (TSİ, kış): Londra 09:00-12:00 | New York açılış 15:30-18:00 | NY öğleden sonra 20:30-23:00 | Asya 03:00-06:00")
    # ATR plan
    import pandas_ta as ta
    atr = ta.atr(d1.high, d1.low, d1.close, 14).iloc[-1]; atr4 = ta.atr(h4.high, h4.low, h4.close, 14).iloc[-1]
    print(f"OYNAKLIK: günlük ATR {atr:,.0f} | 4h ATR {atr4:,.0f}  (stop en az 0,5-1 x 4h ATR)")
    if seviyeler:
        print("ENES SEVİYELERİ (fiyata uzaklık): " + " | ".join(f"{s:,.1f} ({(s/son-1)*100:+.1f}%)" for s in sorted(seviyeler)))
    yon = "AŞAĞI" if top < 0 else "YUKARI"
    if yon == "AŞAĞI":
        giris = min(o1, son + atr4) if asagi else son + atr4 * 0.5; stop = giris + atr4
        hedef = [son - atr4, sl, sl - atr * 0.5]
    else:
        giris = max(o1, son - atr4) if not asagi else son - atr4 * 0.5; stop = giris - atr4
        hedef = [son + atr4, sh, sh + atr * 0.5]
    rr = abs(hedef[1] - giris) / abs(giris - stop)
    print(f"OTOMATİK PLAN (trend yönü {yon}; senaryo, tavsiye değil): giriş ~{giris:,.0f} | stop {stop:,.0f} | hedefler {', '.join(f'{h:,.0f}' for h in hedef)} | R:R (2. hedef) {rr:.1f}")
    if "--png" in a:
        import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt, matplotlib.dates as mdates
        d = h4.tail(90); fig, ax = plt.subplots(figsize=(10.8, 7), dpi=100, facecolor="#0B0E14"); ax.set_facecolor("#0B0E14")
        x = np.arange(len(d))
        for k, r in enumerate(d.itertuples()):
            col = "#2BD47D" if r.close >= r.open else "#FF5A5F"
            ax.plot([k, k], [r.low, r.high], color=col, lw=0.8); ax.add_patch(plt.Rectangle((k - 0.32, min(r.open, r.close)), 0.64, max(abs(r.close - r.open), 1), color=col))
        def cizgi(y, et, renk, ls="-"):
            ax.axhline(y, color=renk, lw=1, ls=ls, alpha=0.9); ax.text(len(d) + 0.5, y, f"{et} {y:,.0f}", color=renk, va="center", fontsize=8)
        cizgi(eq, "Denge", "#8A94A6", "--")
        ax.axhspan(min(o1, o3), max(o1, o3), color="#E8B44C" if asagi else "#3D8BFF", alpha=0.15); ax.text(1, max(o1, o3), "OTE", color="#E8B44C", fontsize=9)
        if "1h" in D and D["1h"].volume.sum() > 0: cizgi(poc, "POC", "#3D8BFF", ":")
        cizgi(giris, "Giriş", "#F2F4F8", "-."); cizgi(stop, "Stop", "#FF5A5F", "-."); cizgi(hedef[1], "Hedef", "#2BD47D", "-.")
        for s in seviyeler: cizgi(s, "Enes", "#5BC0DE", "-")
        ax.set_xticks(x[::12]); ax.set_xticklabels([i.strftime("%d.%m") for i in d.index[::12]], color="#8A94A6")
        ax.tick_params(colors="#8A94A6"); [s_.set_color("#222A36") for s_ in ax.spines.values()]; ax.set_xlim(-1, len(d) + 9)
        ax.set_title(f"{t} 4 saatlik • yön {yon} (MTF {top:+d}) • OTE, POC, plan", color="#F2F4F8", loc="left")
        fig.savefig(a[a.index("--png") + 1], facecolor=fig.get_facecolor(), bbox_inches="tight")

if __name__ == "__main__":
    main(sys.argv[1:])

#!/usr/bin/env python3
"""STİL ÇİZİM (kural 108, Enes 28.11 11:20): beğenilen teknik analiz tweetinin çizim TARZINA benzer
(birebir aynı değil) kendi grafiğimizi çizer. Veri gerçek (Yahoo), çizgiler kendi pivotlarımızdan hesaplanır.

Öğeler (hepsi isteğe bağlı, beğenilen tweette ne varsa onu seç):
  --trend asagi|yukari|yok   ana trend çizgisi (son büyük tepe/dipten, en az 3 dokunuşa en uygun)
  --ma 50,200                hareketli ortalama(lar) (haftalıkta 40 = ~200G)
  --bolge 275-295            yatay destek/direnç bölgesi (mor kutu)
  --osc cci|rsi|macd|yok     alt panel osilatör + osilatördeki trend çizgisi
  --halka                    son kırılım bölgesine halka (dikkat noktası)
  --seviye 427,367           yatay seviye çizgileri (etiketli)
  --baslik "..."             sol üst kısa başlık (Türkçe, 6 kelimeyi geçme)
Kullanım: python3 invest/stil_cizim.py TSLA --tf 1wk --trend asagi --ma 40 --bolge 275-295 --osc cci --halka --out g/stil_tsla.png
"""
import sys, warnings, numpy as np, pandas as pd
warnings.filterwarnings("ignore")
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from smc_analiz import veri
import kart4 as K4

BG, INK, MUT, HAIR = K4.BG, K4.INK, K4.MUTED, K4.HAIR
UP, DOWN, ACC, GOLD = K4.UP, K4.DOWN, K4.ACC, K4.GOLD
TREND, MOR, HALKA = "#FF5C6C", "#A35BFF", "#F2A93B"

def arg(a, k, d=None): return a[a.index(k) + 1] if k in a else d

def temiz(t, tf):
    """Yahoo haftalık seride son günü ayrı bir 'hafta' olarak tekrar döndürür -> mum kayması. Aynı ISO haftası tek mum."""
    d = veri(t, tf)
    if tf == "1wk":
        iso = [(x.isocalendar()[0], x.isocalendar()[1]) for x in d.index]
        d = d[[i == 0 or iso[i] != iso[i - 1] for i in range(len(d))]]
    return d

def tarih_i(d, s):
    """'2026-11-02' -> o tarihi içeren mumun sırası."""
    ts = pd.Timestamp(s).tz_localize(d.index.tz)
    return int(np.argmin(np.abs((d.index - ts).total_seconds())))

def pivotlar(h, l, w):
    n = len(h)
    tp = [i for i in range(w, n - 1) if h[i] == max(h[max(0, i - w):i + w + 1])]
    dp = [i for i in range(w, n - 1) if l[i] == min(l[max(0, i - w):i + w + 1])]
    return tp, dp

def trend_cizgi(y, piv, asagi, n):
    """Ana uç noktadan (en yüksek tepe / en düşük dip) başlayıp sonraki pivotlara en çok değen, hiçbir mumu
    kesmeyen çizgi. Döndürür (i1, y1, egim, dokunus)."""
    if not piv: return None
    i1 = max(piv, key=lambda i: y[i]) if asagi else min(piv, key=lambda i: y[i])
    en = None
    for i2 in [p for p in piv if p > i1 + 3]:
        m = (y[i2] - y[i1]) / (i2 - i1)
        hat = y[i1] + m * (np.arange(n) - i1)
        ihlal = np.sum((y[i1:] - hat[i1:]) > abs(hat[i1:]) * 0.004) if asagi else np.sum((hat[i1:] - y[i1:]) > abs(hat[i1:]) * 0.004)
        if ihlal > 2: continue
        dok = sum(1 for p in piv if p > i1 and abs(y[p] - hat[p]) <= abs(hat[p]) * 0.02)
        if en is None or dok > en[3]: en = (i1, y[i1], m, dok)
    return en

def cci(d, p=20):
    tp = (d.high + d.low + d.close) / 3; sma = tp.rolling(p).mean()
    md = tp.rolling(p).apply(lambda x: np.mean(np.abs(x - x.mean())), raw=True)
    return (tp - sma) / (0.015 * md)

def rsi(c, p=14):
    dd = c.diff(); u = dd.clip(lower=0).ewm(alpha=1 / p).mean(); g = (-dd.clip(upper=0)).ewm(alpha=1 / p).mean()
    return 100 - 100 / (1 + u / g)

def main(a):
    t = a[0]; tf = arg(a, "--tf", "1wk"); osc = arg(a, "--osc", "yok"); tr = arg(a, "--trend", "asagi")
    D = temiz(t, tf); d = D.tail({"1wk": 80, "1d": 160, "4h": 120}.get(tf, 120))
    n = len(d); x = np.arange(n); h, l, c = d.high.values, d.low.values, d.close.values
    paneller = 2 if osc != "yok" else 1
    fig = plt.figure(figsize=(11.25, 10.5 if paneller == 2 else 8.2), dpi=100, facecolor=BG)
    gs = fig.add_gridspec(paneller + 1, 1, height_ratios=([3.2, 0.55, 1.5] if paneller == 2 else [3.2, 0.55]), hspace=0.02)
    ax = fig.add_subplot(gs[0]); axv = fig.add_subplot(gs[1], sharex=ax)
    for q in (ax, axv): q.set_facecolor(BG)
    rng = h.max() - l.min(); pad = rng * 0.02
    for k, r in enumerate(d.itertuples()):
        col = UP if r.close >= r.open else DOWN
        ax.plot([k, k], [r.low, r.high], color=col, lw=1.0, alpha=0.9)
        ax.add_patch(plt.Rectangle((k - 0.33, min(r.open, r.close)), 0.66, max(abs(r.close - r.open), rng * 0.002), color=col, alpha=0.92))
        axv.bar(k, r.volume, color=col, alpha=0.45, width=0.7)
    w = 3 if tf == "1wk" else 4
    tp, dp = pivotlar(h, l, w)
    kirilim = None
    if tr != "yok":
        asagi = tr == "asagi"
        tc = trend_cizgi(h if asagi else l, tp if asagi else dp, asagi, n)
        if arg(a, "--noktalar"):
            i1, i2 = [tarih_i(d, z) for z in arg(a, "--noktalar").split(",")]
            y = h if asagi else l; tc = (i1, y[i1], (y[i2] - y[i1]) / (i2 - i1), 2)
        if tc:
            i1, y1, m, dok = tc; xs = np.array([i1, n + 3]); ax.plot(xs, y1 + m * (xs - i1), color=TREND, lw=3.2, solid_capstyle="round", zorder=5)
            hat = y1 + m * (x - i1)
            ust = np.where((c > hat) if asagi else (c < hat))[0]; ust = ust[ust > i1 + 3]
            if len(ust): kirilim = int(ust[0])
            ax.text(n + 1.2, hat[-1] + rng * 0.035, f"{hat[-1]:,.0f}".replace(",", "."), color=TREND, fontsize=12, fontweight="bold", va="center", zorder=9)
            print("trend çizgisi şimdi:", round(hat[-1], 2), "| son kapanış:", round(c[-1], 2), "| gövde ihlali:", int(sum(1 for i in range(i1 + 1, n) if max(d.open.iloc[i], c[i]) > hat[i] * 1.002)))
    for p in [int(v) for v in (arg(a, "--ma", "") or "").split(",") if v]:
        ma = D.close.rolling(p).mean().reindex(d.index)
        ax.plot(x, ma.values, color=ACC if p == max([int(v) for v in arg(a, "--ma").split(",")]) else "#C9D3E3", lw=2.6 if p < 100 else 1.6, zorder=4)
    if arg(a, "--bolge"):
        lo, hi = map(float, arg(a, "--bolge").split("-"))
        ax.axhspan(lo, hi, color=MOR, alpha=0.16, zorder=1); ax.axhline(lo, color=MOR, lw=2.2); ax.axhline(hi, color=MOR, lw=2.2)
        if arg(a, "--bolge-ad"): ax.text(n * 0.30, (lo + hi) / 2, arg(a, "--bolge-ad"), color="#D9C2FF", fontsize=11.5, va="center", zorder=9)
    for s in [float(v) for v in (arg(a, "--seviye", "") or "").split(",") if v]:
        ax.axhline(s, color=MUT, lw=0.9, ls=(0, (4, 4))); ax.text(n + 4.5, s, f"{s:,.0f}".replace(",", "."), color=INK, fontsize=11, va="center", family=K4.MONO if hasattr(K4, "MONO") else None)
    son = c[-1]
    ax.axhline(son, color=ACC, lw=0.7, ls=":", alpha=0.7)
    ax.text(n + 1.2, son, f" {son:,.2f} ".replace(",", "X").replace(".", ",").replace("X", "."), color="#0A0C10", fontsize=11.5, va="center",
            bbox=dict(boxstyle="round,pad=0.25", fc=UP if c[-1] >= c[-2] else DOWN, ec="none"), zorder=9)
    if "--halka" in a:
        i0 = kirilim if kirilim is not None and kirilim > n - 15 else n - 4
        cx = (i0 + n - 1) / 2; sl = d.iloc[max(0, i0 - 1):]; cy = (sl.high.max() + sl.low.min()) / 2
        ax.add_patch(Ellipse((cx, cy), max(8, n - i0 + 5), (sl.high.max() - sl.low.min()) * 1.12, fc=HALKA, alpha=0.22, ec=HALKA, lw=2.6, zorder=6))
    if osc != "yok":
        ao = fig.add_subplot(gs[2], sharex=ax); ao.set_facecolor(BG)
        dd = D; o = {"cci": cci(dd), "rsi": rsi(dd.close)}.get(osc, cci(dd)).reindex(d.index).values
        ao.plot(x, o, color="#6FCF7F", lw=1.4)
        for g_ in ([100, 0, -100] if osc == "cci" else [70, 50, 30]): ao.axhline(g_, color=HAIR, lw=0.8)
        ot, od = pivotlar(np.nan_to_num(o, nan=-1e9), np.nan_to_num(o, nan=1e9), w)
        oc = trend_cizgi(np.nan_to_num(o, nan=-1e9), [p for p in ot if not np.isnan(o[p])], True, n)
        if arg(a, "--osc-noktalar"):
            j1, j2 = [tarih_i(d, z) for z in arg(a, "--osc-noktalar").split(",")]; oc = (j1, o[j1], (o[j2] - o[j1]) / (j2 - j1), 2)
        if oc:
            i1, y1, m, _ = oc; xs = np.array([i1, n]); ao.plot(xs, y1 + m * (xs - i1), color=TREND, lw=2.8, solid_capstyle="round")
        if "--halka" in a:
            ao.add_patch(Ellipse((n - 3, np.nanmean(o[-6:])), 9, (np.nanmax(o[-8:]) - np.nanmin(o[-8:])) * 1.6 + 20, fc=HALKA, alpha=0.22, ec=HALKA, lw=2.6))
        ao.text(0.005, 0.92, osc.upper(), transform=ao.transAxes, color=MUT, fontsize=10)
        alts = ao
    else: alts = axv
    for q in fig.axes:
        q.tick_params(colors=MUT, labelsize=10.5, length=0); q.yaxis.tick_right()
        for s_ in q.spines.values(): s_.set_visible(False)
        q.grid(color=HAIR, lw=0.6, alpha=0.7)
    for q in fig.axes[:-1]: plt.setp(q.get_xticklabels(), visible=False)
    axv.set_yticks([])
    ax.set_xlim(-1, n + 9); ax.set_ylim(min(l.min(), float(arg(a, "--bolge", "1e9-1e9").split("-")[0]) if arg(a, "--bolge") else l.min()) - 3 * pad, h.max() + 3 * pad)
    tk = [i for i in range(n) if i == 0 or d.index[i].month != d.index[i - 1].month]
    tk = [i for i in tk if d.index[i].month in (1, 7)] if tf == "1wk" else tk[::2]
    alts.set_xticks(tk); alts.set_xticklabels([str(d.index[i].year) if d.index[i].month == 1 else ["Oca","Şub","Mar","Nis","May","Haz","Tem","Ağu","Eyl","Eki","Kas","Ara"][d.index[i].month - 1] for i in tk])
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, q: f"{v:,.0f}".replace(",", ".")))
    tfad = {"1wk": "Haftalık", "1d": "Günlük", "4h": "4 saatlik"}.get(tf, tf)
    fig.text(0.02, 0.975, f"${t.strip('^')}", color=INK, fontsize=22, fontweight="bold", va="top")
    fig.text(0.02, 0.938, tfad + ("  ·  " + arg(a, "--baslik") if arg(a, "--baslik") else ""), color=MUT, fontsize=13.5, va="top")
    fig.text(0.985, 0.012, "ENES ULUDAĞ", color=INK, fontsize=11.5, fontweight="bold", ha="right", alpha=0.85)
    fig.subplots_adjust(left=0.02, right=0.93, top=0.9, bottom=0.05)
    out = arg(a, "--out", f"/tmp/stil_{t.strip('^')}.png"); fig.savefig(out, facecolor=BG, dpi=100)
    print("stil çizim:", out, "| kırılım mumu:", d.index[kirilim].date() if kirilim is not None else "yok")

if __name__ == "__main__":
    main(sys.argv[1:])

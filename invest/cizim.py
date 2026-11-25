#!/usr/bin/env python3
"""ÇİZİMLİ ANALİZ GRAFİĞİ (Enes 25.11.2026 23:01: "artık gerektiğinde analizleri çizimle beraber yap").

Otomatik çizer: mumlar, düşen/yükselen trend çizgisi (son tepeler ya da dipler), en güçlü direnç ve destek
bölgeleri (teknik_ek çakışma haritasından), belirgin dipler/tepeler, Fibonacci (son dalga), Enes seviyeleri,
iki senaryo oku (A yukarı onay, B aşağı bozulma) ve kısa notlar. Yazılar üst üste binmez (dikey itme).

Kullanım:
  python3 invest/cizim.py <TICKER> [--tf 4h|1d] [--seviyeler a,b] [--fib] [--onay 83] [--bozulma 65] [--out g/x.png]
  --onay / --bozulma verilmezse en yakın güçlü direnç / destek kullanılır.
"""
import sys, warnings, numpy as np
warnings.filterwarnings("ignore")
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
import kart3 as K
from smc_analiz import veri

def arg(a, k, d=None, t=str): return t(a[a.index(k) + 1]) if k in a else d

def yerlestir(ys, min_ara):
    """Etiket y konumlarını çakışmayacak şekilde dağıt."""
    s = sorted(range(len(ys)), key=lambda i: ys[i]); out = list(ys)
    for j in range(1, len(s)):
        if out[s[j]] - out[s[j - 1]] < min_ara: out[s[j]] = out[s[j - 1]] + min_ara
    return out

def main(a):
    t = a[0]; tf = arg(a, "--tf", "4h"); enes = [float(x) for x in arg(a, "--seviyeler", "").split(",") if x]
    d1 = veri(t, "1d"); d = veri(t, tf).tail(90 if tf == "4h" else 130)
    try: h1 = veri(t, "1h")
    except Exception: h1 = None
    from teknik_ek import seviye_havuzu
    Kl, son = seviye_havuzu(t, d1, h1, enes)
    ust = sorted([k for k in Kl if k["ort"] > son and k["puan"] >= 3], key=lambda k: k["ort"])[:2]
    alt = sorted([k for k in Kl if k["ort"] <= son and k["puan"] >= 3], key=lambda k: -k["ort"])[:2]
    onay = arg(a, "--onay", ust[0]["ort"] if ust else son * 1.05, float)
    boz = arg(a, "--bozulma", alt[0]["ort"] if alt else son * 0.95, float)
    BG, INK, MUT, GR = K.BG, K.INK, K.MUTED, K.GRID
    fig, ax = plt.subplots(figsize=(10.8, 7.6), dpi=100, facecolor=BG); ax.set_facecolor(BG)
    n = len(d); x = np.arange(n); rng = d.high.max() - d.low.min(); pad = rng * 0.02
    for k, r in enumerate(d.itertuples()):
        col = K.UP if r.close >= r.open else K.DOWN
        ax.plot([k, k], [r.low, r.high], color=col, lw=0.9)
        ax.add_patch(plt.Rectangle((k - 0.32, min(r.open, r.close)), 0.64, max(abs(r.close - r.open), rng * 0.002), color=col))
    h, l = d.high.values, d.low.values
    tepeler = [i for i in range(3, n - 2) if h[i] == max(h[i - 3:i + 3])]
    dipler = [i for i in range(3, n - 2) if l[i] == min(l[i - 3:i + 3])]
    trend_asagi = d.close.iloc[-1] < d.close.iloc[0]
    if trend_asagi and len(tepeler) >= 2:
        i1 = max(tepeler[-4:], key=lambda i: h[i]); i2 = tepeler[-1] if tepeler[-1] != i1 else tepeler[-2]
        i1, i2 = sorted([i1, i2]); m = (h[i2] - h[i1]) / max(1, i2 - i1); xs = np.array([i1, n + 12])
        ax.plot(xs, h[i1] + m * (xs - i1), color=K.GOLD, lw=2); ax.text(i1, h[i1] + pad, "Düşen trend çizgisi", color=K.GOLD, fontsize=10.5)
    elif len(dipler) >= 2:
        i1 = min(dipler[-4:], key=lambda i: l[i]); i2 = dipler[-1] if dipler[-1] != i1 else dipler[-2]
        i1, i2 = sorted([i1, i2]); m = (l[i2] - l[i1]) / max(1, i2 - i1); xs = np.array([i1, n + 12])
        ax.plot(xs, l[i1] + m * (xs - i1), color=K.GOLD, lw=2); ax.text(i1, l[i1] - 3 * pad, "Yükselen trend çizgisi", color=K.GOLD, fontsize=10.5)
    etiketler = []
    for k_ in ust: lo_, hi_ = min(k_["v"]), max(k_["v"]); ax.add_patch(plt.Rectangle((n - 35, lo_ - pad / 2), 47, (hi_ - lo_) + pad, color=K.DOWN, alpha=0.16)); etiketler.append((k_["ort"], f"Direnç {k_['ort']:,.0f} • {', '.join(sorted(set(k_['k'])))[:34]}".replace(",", "."), K.DOWN))
    for k_ in alt: lo_, hi_ = min(k_["v"]), max(k_["v"]); ax.add_patch(plt.Rectangle((n - 35, lo_ - pad / 2), 47, (hi_ - lo_) + pad, color=K.UP, alpha=0.16)); etiketler.append((k_["ort"], f"Destek {k_['ort']:,.0f} • {', '.join(sorted(set(k_['k'])))[:34]}".replace(",", "."), K.UP))
    for e in enes: ax.axhline(e, color="#5BC0DE", lw=1, alpha=0.8); etiketler.append((e, f"Enes {e:,.1f}".replace(",", "X").replace(".", ",").replace("X", "."), "#5BC0DE"))
    if "--fib" in a:
        hi_i, lo_i = int(np.argmax(h)), int(np.argmin(l)); hi, lo = h[hi_i], l[lo_i]
        for f in (0.382, 0.5, 0.618, 0.786):
            y = lo + (hi - lo) * f if hi_i < lo_i else hi - (hi - lo) * f
            ax.axhline(y, color=MUT, lw=0.8, ls=":"); etiketler.append((y, f"Fib {f}", MUT))
    ys = yerlestir([e[0] for e in etiketler], rng * 0.035)
    for (y0, tx, c), y in zip(etiketler, ys): ax.text(n + 13, y, tx, color=c, fontsize=9.5, va="center")
    for i in sorted(dipler, key=lambda i: l[i])[:2]: ax.annotate("dip", (i, l[i]), (i, l[i] - 4 * pad), color=INK, ha="center", fontsize=9.5, arrowprops=dict(arrowstyle="->", color=INK))
    for i in sorted(tepeler, key=lambda i: -h[i])[:1]: ax.annotate("tepe", (i, h[i]), (i, h[i] + 3 * pad), color=INK, ha="center", fontsize=9.5, arrowprops=dict(arrowstyle="->", color=INK))
    s = n - 1; p = d.close.iloc[-1]
    ax.annotate("", (s + 10, onay + pad), (s + 1, p), arrowprops=dict(arrowstyle="-|>", color=K.UP, lw=2.2, ls="--"))
    ax.annotate("", (s + 10, boz - pad), (s + 1, p), arrowprops=dict(arrowstyle="-|>", color=K.DOWN, lw=2.2, ls="--"))
    ax.text(2, min(d.low.min(), boz) - 1.5 * pad, f"A: {onay:,.0f} üstü kapanış → dönüş/devam onayı".replace(",", "."), color=K.UP, fontsize=10.5)
    ax.text(2, min(d.low.min(), boz) - 4.5 * pad, f"B: {boz:,.0f} altı kapanış → senaryo bozulur".replace(",", "."), color=K.DOWN, fontsize=10.5)
    ax.set_xlim(-1, n + 40); ax.set_ylim(min(d.low.min(), boz) - 7 * pad, max(d.high.max(), onay) + 5 * pad)
    ax.tick_params(colors=MUT); [q.set_color(GR) for q in ax.spines.values()]; ax.grid(color=GR, lw=0.5, alpha=0.5)
    tk = list(range(0, n, max(1, n // 7))); ax.set_xticks(tk); ax.set_xticklabels([d.index[i].strftime("%d.%m") for i in tk], color=MUT)
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, q: f"{v:,.0f}".replace(",", ".")))
    ax.set_title(f"{t} {'4 saatlik' if tf == '4h' else 'günlük'} • çizimli analiz", color=INK, loc="left", fontsize=13)
    fig.text(0.99, 0.01, "ENES ULUDAĞ", color=INK, fontsize=12, fontweight="bold", ha="right")
    out = arg(a, "--out", f"/tmp/cizim_{t.strip('^')}.png"); fig.savefig(out, facecolor=BG, bbox_inches="tight"); print("çizim:", out)

if __name__ == "__main__":
    main(sys.argv[1:])

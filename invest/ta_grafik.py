"""Teknik analiz grafiği (koyu tema, gerekçeli seviye etiketleri, RSI/MACD/OBV panelleri).

Kullanım:
    import ta_grafik
    ta_grafik.ciz(
        "DOCN", "Dibe yakın, ama dönüş teyidi henüz yok",
        bolgeler=[(79.16, 84.34, "al"), (69.8, 73.3, "al"), (93.83, 97.31, "direnc")],
        cizgiler=[(102.2, "sat", "--"), (69.78, "sat", "-")],
        etiketler=[(81.7, "al", "1. kademe 79-84: G bull FVG + 1s Supertrend 83,5"), ...],
        panel_notlari=["RSI 14: 42, dipten dönüyor", "MACD: ...", "OBV: ..."],
        son_fiyat=84.0, out="g/ta/20261116_1800_docn_teknik.jpg", ylim=(62, 160))
Renk anahtarları: al (yeşil), sat (kırmızı), direnc (kırmızı), fiyat (altın), ema (mavi), vwap (mor), beyaz.
"""
import datetime as dt

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle

import ta2

BG, FG, MU = "#0d0f14", "#e6e6ea", "#8a8f9c"
RENK = {"al": "#2ecc71", "sat": "#e5484d", "direnc": "#e5484d", "fiyat": "#d4af69",
        "ema": "#4c8dff", "vwap": "#c792ea", "beyaz": "#ffffff"}

try:
    fm.fontManager.addfont("font/InterDisplay-Medium.otf")
    _FONT = "Inter Display"
except Exception:
    _FONT = "DejaVu Sans"


def _rsi(a, n=14):
    g = [0] + [max(a[i] - a[i - 1], 0) for i in range(1, len(a))]
    d = [0] + [max(a[i - 1] - a[i], 0) for i in range(1, len(a))]
    ag, ad = sum(g[1:n + 1]) / n, sum(d[1:n + 1]) / n
    out = [None] * (n + 1)
    for i in range(n + 1, len(a)):
        ag = (ag * (n - 1) + g[i]) / n
        ad = (ad * (n - 1) + d[i]) / n
        out.append(100 - 100 / (1 + ag / ad) if ad else 100)
    return out


def ciz(ticker, baslik, bolgeler, cizgiler, etiketler, panel_notlari, son_fiyat, out,
        ylim=None, N=90, dilim="GÜNLÜK", tarih=None, kaynak_notu=None):
    r = ta2.fetch(ticker, "1d", "2y")
    t = [dt.datetime.fromtimestamp(x[0], dt.timezone.utc) for x in r]
    o, h, l, c, v = [[x[i] for x in r] for i in range(1, 6)]
    e200 = ta2.ema(c, 200)
    vw = [None] * 19 + [sum(((h[j] + l[j] + c[j]) / 3) * v[j] for j in range(i - 19, i + 1)) /
                        sum(v[j] for j in range(i - 19, i + 1)) for i in range(19, len(c))]
    R = _rsi(c)
    mac = [a - b for a, b in zip(ta2.ema(c, 12), ta2.ema(c, 26))]
    sig = ta2.ema(mac, 9)
    hist = [a - b for a, b in zip(mac, sig)]
    obv = [0]
    for i in range(1, len(c)):
        obv.append(obv[-1] + (v[i] if c[i] > c[i - 1] else -v[i] if c[i] < c[i - 1] else 0))
    s = len(c) - N
    idx = list(range(N))
    X = N + 1
    plt.rcParams.update({"font.family": _FONT, "text.color": FG, "xtick.color": MU, "ytick.color": MU})
    fig = plt.figure(figsize=(10.8, 13.5), dpi=100, facecolor=BG)
    gs = fig.add_gridspec(4, 1, height_ratios=[5.2, 1.1, 1.1, 1.1], hspace=0.07,
                          left=0.06, right=0.68, top=0.87, bottom=0.07)
    ax = fig.add_subplot(gs[0])
    axes = [ax] + [fig.add_subplot(gs[i], sharex=ax) for i in (1, 2, 3)]
    for a in axes:
        a.set_facecolor(BG)
        for sp in a.spines.values():
            sp.set_color("#262a33")
        a.grid(color="#1c1f27", lw=0.6)
    for lo, hi, k in bolgeler:
        ax.axhspan(lo, hi, color=RENK[k], alpha=0.2 if k == "al" else 0.15, lw=0)
    for i in idx:
        k = s + i
        col = RENK["al"] if c[k] >= o[k] else RENK["sat"]
        ax.vlines(i, l[k], h[k], color=col, lw=1.1)
        ax.add_patch(Rectangle((i - 0.35, min(o[k], c[k])), 0.7, max(abs(c[k] - o[k]), 0.001 * c[k]), color=col))
    ax.plot(idx, [e200[s + i] for i in idx], color=RENK["ema"], lw=2.2)
    ax.plot(idx, [vw[s + i] for i in idx], color=RENK["vwap"], lw=1.8)
    for y, k, ls in cizgiler:
        ax.axhline(y, color=RENK[k], lw=1.1, ls=ls, alpha=0.85)
    if son_fiyat:
        ax.plot([X], [son_fiyat], marker="o", color=RENK["fiyat"], ms=9)
    ax.set_xlim(-1, X + 1)
    if ylim:
        ax.set_ylim(*ylim)
    ax.yaxis.tick_right()
    fig.canvas.draw()
    pos = sorted([(ax.transData.transform((0, y))[1] / fig.dpi / 13.5, k, txt) for y, k, txt in etiketler], reverse=True)
    son = None
    for fy, k, txt in pos:
        if son is not None and son - fy < 0.022:
            fy = son - 0.022
        son = fy
        fig.text(0.695, fy, txt, color=RENK[k], fontsize=10.5, va="center", wrap=True)
    axes[1].plot(idx, [R[s + i] for i in idx], color=RENK["fiyat"], lw=1.5)
    axes[1].axhline(70, color=RENK["sat"], lw=0.7, ls="--")
    axes[1].axhline(30, color=RENK["al"], lw=0.7, ls="--")
    axes[1].set_ylim(15, 85)
    axes[2].bar(idx, [hist[s + i] for i in idx], color=[RENK["al"] if hist[s + i] >= 0 else RENK["sat"] for i in idx])
    axes[2].plot(idx, [mac[s + i] for i in idx], color=RENK["ema"], lw=1)
    axes[2].plot(idx, [sig[s + i] for i in idx], color="#ff9f43", lw=1)
    axes[3].plot(idx, [obv[s + i] / 1e6 for i in idx], color="#4dd0e1", lw=1.5)
    for a, txt in zip(axes[1:], panel_notlari):
        a.yaxis.tick_right()
        p = a.get_position()
        fig.text(0.695, (p.y0 + p.y1) / 2, txt, color=FG, fontsize=11, va="center")
    step = max(N // 5, 1)
    ticks = [i for i in idx if i % step == 0]
    axes[3].set_xticks(ticks)
    axes[3].set_xticklabels([t[s + i].strftime("%d.%m") for i in ticks])
    for a in axes[:3]:
        plt.setp(a.get_xticklabels(), visible=False)
    tarih = tarih or dt.date.today().strftime("%d.%m.%Y")
    fig.text(0.06, 0.952, f"${ticker}  •  {dilim}  •  {tarih}", color=RENK["fiyat"], fontsize=14, fontweight="bold")
    fig.text(0.06, 0.912, baslik, color=FG, fontsize=25, fontweight="bold")
    fig.text(0.06, 0.025, kaynak_notu or "Veri: Yahoo Finance • Göstergeler kendi hesabım", color=MU, fontsize=10)
    fig.text(0.94, 0.025, "ENES ULUDAĞ", color=FG, fontsize=12, fontweight="bold", ha="right")
    fig.savefig(out, facecolor=BG)
    plt.close(fig)
    return out

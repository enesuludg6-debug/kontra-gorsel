#!/usr/bin/env python3
"""kart4 — ESTETİK (editoryal) kart ailesi (Enes 27.11 23:43 'görünüş olarak daha estetik istiyorum').
Tercih: koyu, minimal, Instrument Serif + JetBrains Mono (fontlar invest/fonts/, OFL). Tek vurgu rengi, bol boşluk,
ince çizgiler, ızgarasız grafik, parlayan çizgi + yumuşak geçişli alan, serif başlık ve serif kahraman rakam.
Kullanım: import kart4 as K4; K4.cizgi(...)  (denetim + kaydet kart3'ten)."""
import os, datetime as dt
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt, matplotlib.dates as mdates
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, Polygon
D = os.path.dirname(os.path.abspath(__file__))
for f in os.listdir(os.path.join(D, "fonts")):
    if f.endswith(".ttf"): fm.fontManager.addfont(os.path.join(D, "fonts", f))
import kart3 as K3
SERIF, MONO = "Instrument Serif", "JetBrains Mono"
BG = "#0A0C10"; INK = "#EDEFF3"; MUTED = "#7C8596"; HAIR = "#1E2430"; ACC = "#5B9BFF"; UP = "#3DDC97"; DOWN = "#FF6B6B"; GOLD = "#D9B26A"
AY = ["", "OCA", "ŞUB", "MAR", "NİS", "MAY", "HAZ", "TEM", "AĞU", "EYL", "EKİ", "KAS", "ARA"]
def _s(v): return f"{v:,.0f}".replace(",", ".") if abs(v) >= 1000 else f"{v:.2f}".replace(".", ",")
def _up(t): return t.replace("i", "İ").upper()

def _zemin(fig, renk):
    """v2: iki yumuşak ışık (sol üst vurgu, sağ alt soluk), ince film greni ve kenar vinyeti."""
    n = 540; g = np.linspace(0, 1, n); X, Y = np.meshgrid(g, g)
    rgb = np.array(matplotlib.colors.to_rgb(renk)); bg = np.array(matplotlib.colors.to_rgb(BG))
    a1 = np.clip(1 - np.sqrt((X - 0.08) ** 2 + (Y - 0.95) ** 2) / 0.8, 0, 1) ** 2.2 * 0.26
    a2 = np.clip(1 - np.sqrt((X - 0.95) ** 2 + (Y - 0.18) ** 2) / 0.7, 0, 1) ** 2.5 * 0.08
    img = bg + (rgb - bg) * (a1 + a2)[..., None]
    vin = 1 - 0.28 * np.clip(np.sqrt((X - 0.5) ** 2 + (Y - 0.5) ** 2) / 0.72, 0, 1) ** 2.4
    img = img * vin[..., None]
    rng = np.random.default_rng(7); img = np.clip(img + rng.normal(0, 0.012, (n, n, 1)), 0, 1)
    ax = fig.add_axes([0, 0, 1, 1], zorder=-5); ax.imshow(img, extent=[0, 1, 0, 1], origin="lower", aspect="auto", interpolation="bicubic"); ax.axis("off")

def _aralik(t): return "\u2009".join(t)  # mono etiketlerde hafif harf aralığı

def cizgi(kicker, baslik, vurgu, seri, kahraman, kahraman_alt, olaylar, ref, alinti, kaynak, out, renk=ACC, birim="", ticker=None, kiyas=None, kiyas_ad=""):
    """baslik: düz kısım; vurgu: başlığın italik ve renkli ikinci satırı. kahraman: '+6,8%' gibi. olaylar: [(tarih, 'METİN')]. ref: [(değer, 'METİN')]."""
    fig = plt.figure(figsize=(10.8, 13.5), dpi=100, facecolor=BG); _zemin(fig, renk)
    L, R = 0.074, 0.926
    son = dt.date.fromisoformat(seri[-1][0])
    fig.text(L, 0.945, _aralik(_up(kicker)), fontsize=13, family=MONO, color=MUTED, va="center")
    fig.text(R, 0.945, _aralik(f"{son.day:02d} {AY[son.month]} {son.year}"), fontsize=13, family=MONO, color=MUTED, va="center", ha="right")
    fig.add_artist(Rectangle((L, 0.925), R - L, 0.0008, transform=fig.transFigure, color=HAIR))
    fig.text(L, 0.905, baslik, fontsize=66, family=SERIF, color=INK, va="top")
    fig.text(L, 0.838, vurgu, fontsize=66, family=SERIF, style="italic", color=renk, va="top")
    lg = K3._logo_png(ticker) if ticker else None
    if lg:  # Enes: logo çok belirgin
        h = 170; lg = lg.resize((int(lg.width * h / lg.height), h)); fig.figimage(lg, xo=int(1080 * R) - lg.width, yo=int(1350 * 0.905) - h, zorder=10)
    # kahraman
    hr = UP if kahraman.strip().startswith("+") else (DOWN if kahraman.strip().startswith(("−", "-")) else INK)
    import re as _re
    m = _re.match(r"^([+\-−]?%?)(.*)$", kahraman.strip()); on, govde = m.group(1), m.group(2)
    t1 = fig.text(L - 0.004, 0.752, on, fontsize=70, family=SERIF, color=hr, alpha=0.55, va="top")
    fig.canvas.draw(); bx = t1.get_window_extent(fig.canvas.get_renderer()).x1 / 1080 if on else L - 0.004
    fig.text(bx + 0.004, 0.772, govde, fontsize=128, family=SERIF, color=hr, va="top")
    fig.text(L, 0.6, _aralik(_up(kahraman_alt)), fontsize=12, family=MONO, color=MUTED, va="top")
    # grafik
    ax = fig.add_axes([L, 0.25, R - L - 0.09, 0.33]); ax.set_facecolor("none")
    for s_ in ax.spines.values(): s_.set_visible(False)
    x = [dt.date.fromisoformat(a) for a, _ in seri]; y = np.array([b for _, b in seri], float); xn = mdates.date2num(x)
    lo, hi = y.min(), y.max(); pad = (hi - lo) * 0.08; ymin = lo - pad
    ax.set_ylim(ymin, hi + pad); ax.set_xlim(xn[0], xn[-1] + (xn[-1] - xn[0]) * 0.02)
    # yumuşak geçişli alan
    grad = np.zeros((256, 1, 4)); grad[..., :3] = matplotlib.colors.to_rgb(renk); grad[:, 0, 3] = np.linspace(0, 0.28, 256)
    im = ax.imshow(grad, extent=[xn[0], xn[-1], ymin, hi + pad], origin="lower", aspect="auto", zorder=1)
    poly = Polygon(np.column_stack([np.r_[xn[0], xn, xn[-1]], np.r_[ymin, y, ymin]]), closed=True, transform=ax.transData)
    im.set_clip_path(poly)
    if kiyas:  # kıyas serisi: aynı başlangıca ölçekli, ince gri
        kd = dict(kiyas); xk = [mdates.date2num(dt.date.fromisoformat(a)) for a, _ in seri if a in kd]
        yk = [kd[a] * y[0] / kd[seri[0][0]] for a, _ in seri if a in kd]
        ax.plot(xk, yk, color=MUTED, lw=1.4, alpha=0.8, zorder=2)
        ax.set_ylim(min(ymin, min(yk) - pad), max(hi + pad, max(yk) + pad))
        fig.text(L, 0.612 - 0.0, "", fontsize=1)
        fig.text(R - 0.09, ax.transData.transform((xk[-1], yk[-1]))[1] / 1350, _up(kiyas_ad), fontsize=12.5, family=MONO, color=MUTED, ha="right", va="bottom")
    for lw, a in [(14, 0.05), (8, 0.10), (2.6, 1.0)]:  # parlama
        ax.plot(xn, y, color=renk, lw=lw, alpha=a, solid_capstyle="round", solid_joinstyle="round", zorder=3)
    for v, et in ref or []:
        ax.axhline(v, color=GOLD, lw=1, ls=(0, (1, 4)), zorder=2)
        ax.text(xn[0], v + pad * 0.25, _up(et), fontsize=12.5, family=MONO, color=GOLD, va="bottom")
    for td, et in olaylar or []:
        d0 = mdates.date2num(dt.date.fromisoformat(td)); i = int(np.argmin(abs(xn - d0)))
        ax.plot([xn[i], xn[i]], [y[i], ymin], color=MUTED, lw=0.8, alpha=0.6, zorder=2)
        ax.scatter([xn[i]], [y[i]], s=40, color=INK, zorder=5)
        ax.text(xn[i] - (xn[-1] - xn[0]) * 0.015, ymin + pad * 0.3, _up(et), fontsize=12.5, family=MONO, color=INK, ha="right", va="bottom")
    ax.scatter([xn[-1]], [y[-1]], s=900, color=renk, alpha=0.15, zorder=4); ax.scatter([xn[-1]], [y[-1]], s=90, color=renk, zorder=6, edgecolor=BG, lw=2)
    fig.text(R - 0.012, ax.transData.transform((xn[-1], y[-1]))[1] / 1350, _s(y[-1]) + birim, fontsize=17, family=MONO, color=INK, ha="right", va="center",
             bbox=dict(boxstyle="round,pad=0.5,rounding_size=0.9", fc=BG, ec=renk, lw=1.2))
    # sade eksen: 3 seviye, ızgara yok
    ax.set_yticks([]); ax.set_xticks([])
    for v in np.linspace(lo, hi, 3):
        yy = ax.transData.transform((xn[0], v))[1] / 1350
        if abs(v - y[-1]) > (hi - lo) * 0.12: fig.text(R, yy, _s(v), fontsize=12.5, family=MONO, color=MUTED, ha="right", va="center")
    aylar = sorted({(d.year, d.month) for d in x})[1:]
    for yl, ay in aylar:
        xx = ax.transData.transform((mdates.date2num(dt.date(yl, ay, 1)), 0))[0] / 1080
        fig.add_artist(Rectangle((xx - 0.0004, 0.243), 0.0008, 0.006, transform=fig.transFigure, color=MUTED, alpha=0.6))
        fig.text(xx, 0.232, _aralik(AY[ay]), fontsize=11.5, family=MONO, color=MUTED, ha="center", va="top")
    # alıntı
    fig.add_artist(Rectangle((L, 0.185), 0.04, 0.0012, transform=fig.transFigure, color=renk))
    fig.text(L, 0.168, alinti, fontsize=34, family=SERIF, style="italic", color=INK, va="top")
    fig.add_artist(Rectangle((L, 0.075), R - L, 0.0008, transform=fig.transFigure, color=HAIR))
    fig.text(L, 0.05, _aralik("KAYNAK") + "   " + _aralik(_up(kaynak)), fontsize=11, family=MONO, color=MUTED, va="center")
    fig.text(R, 0.05, "Enes Uludağ", fontsize=24, family=SERIF, color=INK, va="center", ha="right")
    return K3.kaydet(fig, out)

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
    g = np.linspace(0, 1, 400)
    X, Y = np.meshgrid(g, g); R = np.sqrt((X - 0.12) ** 2 + (Y - 0.92) ** 2)
    a = np.clip(1 - R / 0.75, 0, 1) ** 2 * 0.22
    rgb = matplotlib.colors.to_rgb(renk); img = np.zeros((400, 400, 4)); img[..., :3] = rgb; img[..., 3] = a
    ax = fig.add_axes([0, 0, 1, 1], zorder=-5); ax.imshow(img, extent=[0, 1, 0, 1], origin="lower", aspect="auto"); ax.axis("off")

def cizgi(kicker, baslik, vurgu, seri, kahraman, kahraman_alt, olaylar, ref, alinti, kaynak, out, renk=ACC, birim="", ticker=None, kiyas=None, kiyas_ad=""):
    """baslik: düz kısım; vurgu: başlığın italik ve renkli ikinci satırı. kahraman: '+6,8%' gibi. olaylar: [(tarih, 'METİN')]. ref: [(değer, 'METİN')]."""
    fig = plt.figure(figsize=(10.8, 13.5), dpi=100, facecolor=BG); _zemin(fig, renk)
    L, R = 0.074, 0.926
    son = dt.date.fromisoformat(seri[-1][0])
    fig.text(L, 0.945, _up(kicker), fontsize=15, family=MONO, color=MUTED, va="center")
    fig.text(R, 0.945, f"{son.day:02d} {AY[son.month]} {son.year}", fontsize=15, family=MONO, color=MUTED, va="center", ha="right")
    fig.add_artist(Rectangle((L, 0.925), R - L, 0.0008, transform=fig.transFigure, color=HAIR))
    fig.text(L, 0.905, baslik, fontsize=66, family=SERIF, color=INK, va="top")
    fig.text(L, 0.838, vurgu, fontsize=66, family=SERIF, style="italic", color=renk, va="top")
    lg = K3._logo_png(ticker) if ticker else None
    if lg:  # Enes: logo çok belirgin
        h = 170; lg = lg.resize((int(lg.width * h / lg.height), h)); fig.figimage(lg, xo=int(1080 * R) - lg.width, yo=int(1350 * 0.905) - h, zorder=10)
    # kahraman
    hr = UP if kahraman.strip().startswith("+") else (DOWN if kahraman.strip().startswith(("−", "-")) else INK)
    fig.text(L - 0.004, 0.765, kahraman, fontsize=118, family=SERIF, color=hr, va="top")
    fig.text(L, 0.6, _up(kahraman_alt), fontsize=14, family=MONO, color=MUTED, va="top")
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
    fig.text(R, ax.transData.transform((xn[-1], y[-1]))[1] / 1350, _s(y[-1]) + birim, fontsize=20, family=MONO, color=renk, ha="right", va="center", fontweight="bold")
    # sade eksen: 3 seviye, ızgara yok
    ax.set_yticks([]); ax.set_xticks([])
    for v in np.linspace(lo, hi, 3):
        yy = ax.transData.transform((xn[0], v))[1] / 1350
        if abs(v - y[-1]) > (hi - lo) * 0.12: fig.text(R, yy, _s(v), fontsize=12.5, family=MONO, color=MUTED, ha="right", va="center")
    aylar = sorted({(d.year, d.month) for d in x})[1:]
    for yl, ay in aylar:
        xx = ax.transData.transform((mdates.date2num(dt.date(yl, ay, 1)), 0))[0] / 1080
        fig.text(xx, 0.232, AY[ay], fontsize=12.5, family=MONO, color=MUTED, ha="center", va="top")
    # alıntı
    fig.add_artist(Rectangle((L, 0.185), 0.04, 0.0012, transform=fig.transFigure, color=renk))
    fig.text(L, 0.168, alinti, fontsize=34, family=SERIF, style="italic", color=INK, va="top")
    fig.add_artist(Rectangle((L, 0.075), R - L, 0.0008, transform=fig.transFigure, color=HAIR))
    fig.text(L, 0.05, "KAYNAK  " + _up(kaynak), fontsize=12.5, family=MONO, color=MUTED, va="center")
    fig.text(R, 0.05, "Enes Uludağ", fontsize=24, family=SERIF, color=INK, va="center", ha="right")
    return K3.kaydet(fig, out)

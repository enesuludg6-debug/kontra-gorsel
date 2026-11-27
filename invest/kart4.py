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

def cizgi(kicker, baslik, vurgu, seri, kahraman, kahraman_alt, olaylar, ref, alinti, kaynak, out, renk=ACC, birim="", ticker=None, kiyas=None, kiyas_ad="", yan=None):
    """v3 — TASARIMCI DÜZENİ (Enes 27.11 23:47 'daha estetik, bir tasarımcı gibi düşün').
    İlkeler: tek kahraman (rakam), tek vurgu rengi (yalnız çizgi + italik satır + küçük yön oku), 90 px ızgara kenarı,
    modüler tip ölçeği 12/17/34/58/180, kenardan kenara (full-bleed) grafik, eksensiz grafik: yalnız zirve/dip/son değer
    çizgi üstünde etiketli, bol negatif alan. yan: [(etiket, değer)] kahramanın sağında en çok 2 küçük veri."""
    fig = plt.figure(figsize=(10.8, 13.5), dpi=100, facecolor=BG); _zemin(fig, renk)
    L, R = 90 / 1080, 1 - 90 / 1080
    son = dt.date.fromisoformat(seri[-1][0])
    # üst şerit
    fig.text(L, 0.948, _aralik(_up(kicker)), fontsize=12, family=MONO, color=MUTED, va="center")
    fig.text(R, 0.948, _aralik(f"{son.day:02d} {AY[son.month]} {son.year}"), fontsize=12, family=MONO, color=MUTED, va="center", ha="right")
    # başlık (58 pt, iki satır, ikincisi italik vurgu)
    fig.text(L, 0.912, baslik, fontsize=58, family=SERIF, color=INK, va="top")
    fig.text(L, 0.858, vurgu, fontsize=58, family=SERIF, style="italic", color=renk, va="top")
    lg = K3._logo_png(ticker) if ticker else None
    if lg:
        h = 150; lg = lg.resize((int(lg.width * h / lg.height), h)); fig.figimage(lg, xo=int(1080 * R) - lg.width, yo=int(1350 * 0.912) - h, zorder=10)
    # ince ayraç
    fig.add_artist(Rectangle((L, 0.775), R - L, 0.0007, transform=fig.transFigure, color=HAIR))
    # kahraman satırı: rakam beyaz, işaret küçük ve soluk; yön yalnız küçük okla renkli
    import re as _re
    m = _re.match(r"^([+\-−]?%?)(.*)$", kahraman.strip()); on, govde = m.group(1), m.group(2)
    yon = UP if on.startswith("+") else (DOWN if on.startswith(("-", "−")) else MUTED)
    r_ = fig.canvas.get_renderer()
    t1 = fig.text(L - 0.003, 0.742, on, fontsize=64, family=SERIF, color=MUTED, va="top"); fig.canvas.draw()
    x2 = (t1.get_window_extent(fig.canvas.get_renderer()).x1 / 1080 + 0.004) if on else L - 0.005
    fig.text(x2, 0.762, govde, fontsize=180, family=SERIF, color=INK, va="top")
    fig.text(L, 0.522, ("▲ " if yon == UP else "▼ " if yon == DOWN else "") , fontsize=11, family=MONO, color=yon, va="top")
    fig.text(L + 0.022, 0.522, _aralik(_up(kahraman_alt)), fontsize=11.5, family=MONO, color=MUTED, va="top")
    for k, (et, dg) in enumerate((yan or [])[:2]):  # sağ sütun: küçük veri, rakamın taban çizgisine hizalı
        yy = 0.70 - k * 0.085
        fig.text(R, yy, _aralik(_up(et)), fontsize=11, family=MONO, color=MUTED, ha="right", va="top")
        fig.text(R, yy - 0.018, dg, fontsize=34, family=SERIF, color=INK, ha="right", va="top")
    # kenardan kenara grafik
    ax = fig.add_axes([0, 0.255, 1, 0.24]); ax.set_facecolor("none"); ax.axis("off")
    x = [dt.date.fromisoformat(a) for a, _ in seri]; y = np.array([b for _, b in seri], float); xn = mdates.date2num(x)
    lo, hi = y.min(), y.max(); pad = (hi - lo) * 0.10; ymin = lo - pad * 2.2
    span = xn[-1] - xn[0]; ax.set_xlim(xn[0] - span * 0.0, xn[-1] + span * 0.16); ax.set_ylim(ymin, hi + pad * 1.6)
    grad = np.zeros((256, 1, 4)); grad[..., :3] = matplotlib.colors.to_rgb(renk); grad[:, 0, 3] = np.linspace(0, 0.22, 256) ** 1.4
    im = ax.imshow(grad, extent=[xn[0], xn[-1], ymin, hi + pad], origin="lower", aspect="auto", zorder=1)
    im.set_clip_path(Polygon(np.column_stack([np.r_[xn[0], xn, xn[-1]], np.r_[ymin, y, ymin]]), closed=True, transform=ax.transData))
    if kiyas:
        kd = dict(kiyas); xk = [mdates.date2num(dt.date.fromisoformat(a)) for a, _ in seri if a in kd]
        yk = np.array([kd[a] * y[0] / kd[seri[0][0]] for a, _ in seri if a in kd])
        ax.plot(xk, yk, color=MUTED, lw=1.1, alpha=0.7, zorder=2)
        ky = yk[-1]
        if abs(ky - y[-1]) < (hi - lo) * 0.12: ky = y[-1] + np.sign(ky - y[-1] or 1) * (hi - lo) * 0.14
        ax.text(xk[-1] + span * 0.025, ky, _aralik(_up(kiyas_ad)), fontsize=10.5, family=MONO, color=MUTED, va="center")
        ax.set_ylim(min(ymin, yk.min() - pad), max(hi + pad * 1.6, yk.max() + pad))
    for lw, a in [(16, 0.04), (9, 0.08), (2.4, 1.0)]:
        ax.plot(xn, y, color=renk, lw=lw, alpha=a, solid_capstyle="round", solid_joinstyle="round", zorder=3)
    for v, et in ref or []:
        ax.axhline(v, xmin=0, xmax=(xn[-1] - xn[0]) / (span * 1.16), color=GOLD, lw=0.9, ls=(0, (1, 4)), zorder=2)
        ax.text(xn[0] + span * 0.083, v + pad * 0.3, _aralik(_up(et)), fontsize=10.5, family=MONO, color=GOLD, va="bottom")
    ih, il = int(np.argmax(y)), int(np.argmin(y))
    ax.scatter([xn[ih]], [y[ih]], s=22, color=INK, zorder=5)
    ax.text(xn[ih], y[ih] + pad * 0.45, _aralik(_s(y[ih])), fontsize=10.5, family=MONO, color=MUTED, ha="center", va="bottom")
    for td, et in olaylar or []:
        d0 = mdates.date2num(dt.date.fromisoformat(td)); i = int(np.argmin(abs(xn - d0)))
        ax.scatter([xn[i]], [y[i]], s=22, color=INK, zorder=5)
        tepe = y[i] >= y[max(i - 1, 0)] and y[i] >= y[min(i + 1, len(y) - 1)]
        ax.text(xn[i], y[i] + (pad * 0.5 if tepe else -pad * 0.55), _aralik(_up(et)), fontsize=10.5, family=MONO, color=INK, ha="center", va="bottom" if tepe else "top")
    ax.scatter([xn[-1]], [y[-1]], s=700, color=renk, alpha=0.14, zorder=4); ax.scatter([xn[-1]], [y[-1]], s=60, color=renk, zorder=6, edgecolor=BG, lw=2)
    ax.text(xn[-1] + span * 0.025, y[-1], _s(y[-1]) + birim, fontsize=17, family=SERIF, color=INK, va="center", zorder=7)
    # ay çentikleri (grafiğin altında, ızgara kenarına hizalı)
    for yl, ay in sorted({(d.year, d.month) for d in x})[1:]:
        xx = ax.transData.transform((mdates.date2num(dt.date(yl, ay, 1)), 0))[0] / 1080
        if L <= xx <= R: fig.text(xx, 0.24, _aralik(AY[ay]), fontsize=10.5, family=MONO, color=MUTED, ha="center", va="top", alpha=0.8)
    # alıntı
    fig.text(L, 0.175, alinti, fontsize=32, family=SERIF, style="italic", color=INK, va="top")
    fig.add_artist(Rectangle((L, 0.075), R - L, 0.0007, transform=fig.transFigure, color=HAIR))
    fig.text(L, 0.048, _aralik("KAYNAK") + "   " + _aralik(_up(kaynak)), fontsize=10.5, family=MONO, color=MUTED, va="center")
    fig.text(R, 0.048, "Enes Uludağ", fontsize=22, family=SERIF, color=INK, va="center", ha="right")
    return K3.kaydet(fig, out)

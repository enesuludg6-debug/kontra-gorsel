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

# ════════════════════════════════════════════════════════════════════════════════
# KART4 AİLESİ (Enes 27.11 23:49 'en az 10-15 görsel türü, hepsi bu kadar estetik')
# Ortak iskelet: üst şerit + iki satırlı serif başlık (2. satır italik vurgu) + ince ayraç + İÇERİK + alıntı + alt bilgi.
# ════════════════════════════════════════════════════════════════════════════════
L4, R4 = 90 / 1080, 1 - 90 / 1080

def _iskelet(kicker, baslik, vurgu, renk=ACC, ticker=None, tarih=None, alinti="", kaynak=""):
    """Döner: fig, içerik_üst_y (figür kesri), içerik_alt_y."""
    fig = plt.figure(figsize=(10.8, 13.5), dpi=100, facecolor=BG); _zemin(fig, renk)
    t = tarih or dt.date.today()
    fig.text(L4, 0.948, _aralik(_up(kicker)), fontsize=12, family=MONO, color=MUTED, va="center")
    fig.text(R4, 0.948, _aralik(f"{t.day:02d} {AY[t.month]} {t.year}"), fontsize=12, family=MONO, color=MUTED, va="center", ha="right")
    fig.text(L4, 0.912, baslik, fontsize=58, family=SERIF, color=INK, va="top")
    if vurgu: fig.text(L4, 0.858, vurgu, fontsize=58, family=SERIF, style="italic", color=renk, va="top")
    lg = K3._logo_png(ticker) if ticker else None
    if lg:
        h = 150; lg = lg.resize((int(lg.width * h / lg.height), h)); fig.figimage(lg, xo=int(1080 * R4) - lg.width, yo=int(1350 * 0.912) - h, zorder=10)
    fig.add_artist(Rectangle((L4, 0.775), R4 - L4, 0.0007, transform=fig.transFigure, color=HAIR))
    alt_y = 0.10
    if alinti:
        fig.text(L4, 0.175, alinti, fontsize=32 if len(alinti) < 48 else 27, family=SERIF, style="italic", color=INK, va="top"); alt_y = 0.215
    fig.add_artist(Rectangle((L4, 0.075), R4 - L4, 0.0007, transform=fig.transFigure, color=HAIR))
    fig.text(L4, 0.048, _aralik("KAYNAK") + "   " + _aralik(_up(kaynak)), fontsize=10.5, family=MONO, color=MUTED, va="center")
    fig.text(R4, 0.048, "Enes Uludağ", fontsize=22, family=SERIF, color=INK, va="center", ha="right")
    return fig, 0.745, alt_y

def _y(v, birim="%"):
    if birim == "%": return ("+" if v > 0 else "−" if v < 0 else "") + "%" + f"{abs(v):.1f}".replace(".", ",")
    return _s(v) + birim

# 2) SIRALAMA — yatay çubuklar, vurgulanan satır renkli, diğerleri gri
def siralama(kicker, baslik, vurgu, satirlar, alinti, kaynak, out, renk=ACC, vurgula=(), birim="%", tarih=None):
    fig, ust, alt = _iskelet(kicker, baslik, vurgu, renk, tarih=tarih, alinti=alinti, kaynak=kaynak)
    satirlar = sorted(satirlar, key=lambda r: -r[1]); n = len(satirlar); mx = max(abs(v) for _, v in satirlar) or 1
    h = (ust - alt - 0.03) / n; x0 = L4 + 0.20; w = R4 - x0 - 0.12
    for i, (et, v) in enumerate(satirlar):
        yy = ust - 0.02 - i * h; vr = et in vurgula
        c = renk if vr else ("#3A4250" if v >= 0 else "#4A2E33")
        fig.text(L4, yy - h * 0.35, et, fontsize=26, family=SERIF, color=INK if vr else MUTED, va="center")
        fig.add_artist(Rectangle((x0, yy - h * 0.5), w * abs(v) / mx, h * 0.30, transform=fig.transFigure, color=c))
        fig.text(R4, yy - h * 0.35, _y(v, birim), fontsize=20, family=MONO, color=(UP if v > 0 else DOWN) if vr else MUTED, va="center", ha="right")
        fig.add_artist(Rectangle((L4, yy - h * 0.82), R4 - L4, 0.0005, transform=fig.transFigure, color=HAIR))
    return K3.kaydet(fig, out)

# 3) BEKLENTİ — bilanço öncesi konsensüs tablosu
def beklenti(kicker, baslik, vurgu, ticker, satirlar, alinti, kaynak, out, renk=ACC, tarih=None, not_=""):
    """satirlar: [(metrik, konsensüs, alt not)]"""
    fig, ust, alt = _iskelet(kicker, baslik, vurgu, renk, ticker=ticker, tarih=tarih, alinti=alinti, kaynak=kaynak)
    fig.text(L4, ust, _aralik("METRİK"), fontsize=11, family=MONO, color=MUTED, va="top")
    fig.text(R4, ust, _aralik("KONSENSÜS"), fontsize=11, family=MONO, color=MUTED, va="top", ha="right")
    h = (ust - alt - 0.06) / max(len(satirlar), 3)
    for i, (m, v, a) in enumerate(satirlar):
        yy = ust - 0.04 - i * h
        fig.text(L4, yy, m, fontsize=34, family=SERIF, color=INK, va="top")
        fig.text(L4, yy - 0.045, _aralik(_up(a)), fontsize=10.5, family=MONO, color=MUTED, va="top")
        fig.text(R4, yy + 0.004, v, fontsize=58, family=SERIF, color=INK, va="top", ha="right")
        fig.add_artist(Rectangle((L4, yy - h + 0.02), R4 - L4, 0.0006, transform=fig.transFigure, color=HAIR))
    if not_: fig.text(L4, alt + 0.01, _aralik(_up(not_)), fontsize=11, family=MONO, color=renk, va="bottom")
    return K3.kaydet(fig, out)

# 4) SÜTUN — çeyreklik dikey çubuklar, son çubuk tahminse çizgili/boş
def sutun(kicker, baslik, vurgu, satirlar, alinti, kaynak, out, renk=ACC, ticker=None, birim="", tarih=None, tahmin_son=False):
    fig, ust, alt = _iskelet(kicker, baslik, vurgu, renk, ticker=ticker, tarih=tarih, alinti=alinti, kaynak=kaynak)
    n = len(satirlar); mx = max(v for _, v in satirlar); taban = alt + 0.06; yuks = ust - taban - 0.08
    gw = (R4 - L4) / n; bw = gw * 0.56
    for i, (et, v) in enumerate(satirlar):
        x = L4 + i * gw + (gw - bw) / 2; hh = yuks * v / mx; son = i == n - 1
        if son and tahmin_son:
            fig.add_artist(Rectangle((x, taban), bw, hh, transform=fig.transFigure, fc="none", ec=renk, lw=1.6, ls=(0, (3, 3))))
        else:
            fig.add_artist(Rectangle((x, taban), bw, hh, transform=fig.transFigure, color=renk if son else "#2E3644"))
        fig.text(x + bw / 2, taban + hh + 0.012, _s(v) + birim if v >= 100 else f"{v:.2f}".replace(".", ",") + birim, fontsize=26 if son else 20,
                 family=SERIF, color=INK if son else MUTED, ha="center", va="bottom")
        fig.text(x + bw / 2, taban - 0.015, _aralik(_up(et)), fontsize=10.5, family=MONO, color=MUTED, ha="center", va="top")
    fig.add_artist(Rectangle((L4, taban), R4 - L4, 0.0008, transform=fig.transFigure, color=MUTED, alpha=0.5))
    if tahmin_son: fig.text(R4, ust, _aralik("KESİKLİ = BEKLENTİ"), fontsize=10.5, family=MONO, color=renk, ha="right", va="top")
    return K3.kaydet(fig, out)

# 5) KIYAS — iki büyük rakam yan yana (A vs B)
def kiyas(kicker, baslik, vurgu, sol, sag, alinti, kaynak, out, renk=ACC, tarih=None, alt_not=""):
    """sol/sag: (etiket, değer_metni, açıklama, renk)"""
    fig, ust, alt = _iskelet(kicker, baslik, vurgu, renk, tarih=tarih, alinti=alinti, kaynak=kaynak)
    orta = (L4 + R4) / 2; yy = (ust + alt) / 2 + 0.14
    fig.add_artist(Rectangle((orta, alt + 0.04), 0.0007, ust - alt - 0.06, transform=fig.transFigure, color=HAIR))
    for x0, ha, (et, v, a, c) in [(L4, "left", sol), (R4, "right", sag)]:
        fig.text(x0, yy, _aralik(_up(et)), fontsize=12, family=MONO, color=MUTED, ha=ha, va="top")
        fig.text(x0, yy - 0.03, v, fontsize=128, family=SERIF, color=c, ha=ha, va="top")
        fig.text(x0, yy - 0.21, a, fontsize=24, family=SERIF, style="italic", color=MUTED, ha=ha, va="top")
    fig.text(orta, alt + 0.06, "vs", fontsize=30, family=SERIF, style="italic", color=MUTED, ha="center", va="center",
             bbox=dict(boxstyle="circle,pad=0.5", fc=BG, ec=HAIR))
    if alt_not: fig.text(L4, alt + 0.012, _aralik(_up(alt_not)), fontsize=10.5, family=MONO, color=MUTED, va="bottom")
    return K3.kaydet(fig, out)

# 6) ÖLÇER — 0-100 yarım daire gösterge (korku/kalabalık)
def olcer(kicker, baslik, vurgu, deger, bolgeler, etiket, alinti, kaynak, out, renk=ACC, tarih=None, onceki=()):
    """bolgeler: [(bas, son, ad)]; onceki: [(değer, 'etiket')] küçük işaretler"""
    fig, ust, alt = _iskelet(kicker, baslik, vurgu, renk, tarih=tarih, alinti=alinti, kaynak=kaynak)
    ax = fig.add_axes([0.08, alt + 0.06, 0.84, ust - alt - 0.07]); ax.set_aspect("equal"); ax.axis("off"); ax.set_xlim(-1.15, 1.15); ax.set_ylim(-0.25, 1.15)
    th = np.linspace(np.pi, 0, 300)
    ax.plot(np.cos(th), np.sin(th), color=HAIR, lw=18, solid_capstyle="round")
    t2 = np.linspace(np.pi, np.pi * (1 - deger / 100), 300)
    for lw, a in [(30, 0.06), (18, 1.0)]: ax.plot(np.cos(t2), np.sin(t2), color=renk, lw=lw, alpha=a, solid_capstyle="round")
    for b, s_, ad in bolgeler:
        m = np.pi * (1 - (b + s_) / 200); ax.text(1.17 * np.cos(m), 1.17 * np.sin(m), _aralik(_up(ad)), fontsize=11, family=MONO, color=MUTED, ha="center", va="center", rotation=np.degrees(m) - 90)
    for j, (v, et) in enumerate(onceki):
        m = np.pi * (1 - v / 100); rr = 0.66 - 0.12 * j; ax.plot([0.86 * np.cos(m), 0.78 * np.cos(m)], [0.86 * np.sin(m), 0.78 * np.sin(m)], color=MUTED, lw=1.5)

    ax.text(0, 0.30, f"{deger:.0f}".replace(".", ","), fontsize=150, family=SERIF, color=INK, ha="center", va="center")
    ax.text(0, -0.16, _aralik(_up(etiket)), fontsize=13, family=MONO, color=renk, ha="center", va="center")
    if onceki: ax.text(0, -0.25, "   ·   ".join(_aralik(_up(et)) for _, et in onceki), fontsize=10.5, family=MONO, color=MUTED, ha="center", va="center")
    return K3.kaydet(fig, out)

# 7) ISI — kare ızgara (getiri ısı haritası)
def isi(kicker, baslik, vurgu, hucreler, sutun_sayisi, alinti, kaynak, out, renk=ACC, tarih=None):
    """hucreler: [(etiket, değer%)]"""
    fig, ust, alt = _iskelet(kicker, baslik, vurgu, renk, tarih=tarih, alinti=alinti, kaynak=kaynak)
    n = len(hucreler); k = sutun_sayisi; sat = int(np.ceil(n / k)); gap = 0.008
    cw = (R4 - L4 - gap * (k - 1)) / k; ch = min((ust - alt - 0.03 - gap * (sat - 1)) / sat, cw * 1080 / 1350 * 1.0)
    mx = max(abs(v) for _, v in hucreler) or 1
    for i, (et, v) in enumerate(hucreler):
        r, c = divmod(i, k); x = L4 + c * (cw + gap); y = ust - 0.01 - (r + 1) * ch - r * gap
        base = np.array(matplotlib.colors.to_rgb(UP if v >= 0 else DOWN)); bg = np.array(matplotlib.colors.to_rgb(BG))
        col = bg + (base - bg) * (0.18 + 0.62 * abs(v) / mx)
        fig.add_artist(Rectangle((x, y), cw, ch, transform=fig.transFigure, color=col))
        fig.text(x + 0.018, y + ch - 0.018, et, fontsize=24, family=SERIF, color=INK, va="top")
        fig.text(x + cw - 0.018, y + 0.016, _y(v), fontsize=17, family=MONO, color=INK, ha="right", va="bottom")
    return K3.kaydet(fig, out)

# 8) TAKVİM — tarih sütunu + olaylar
def takvim(kicker, baslik, vurgu, gunler, alinti, kaynak, out, renk=ACC, tarih=None):
    """gunler: [('PZT 1 ARA', ['MRVL · Marvell', ...], 'kapanış sonrası')]"""
    fig, ust, alt = _iskelet(kicker, baslik, vurgu, renk, tarih=tarih, alinti=alinti, kaynak=kaynak)
    yy = ust - 0.01
    for g, ogeler, not_ in gunler:
        fig.text(L4, yy, _aralik(_up(g)), fontsize=12, family=MONO, color=renk, va="top")
        if not_: fig.text(R4, yy, _aralik(_up(not_)), fontsize=10.5, family=MONO, color=MUTED, va="top", ha="right")
        yy -= 0.035
        for o in ogeler:
            fig.text(L4 + 0.03, yy, o, fontsize=28, family=SERIF, color=INK, va="top"); yy -= 0.042
        yy -= 0.012; fig.add_artist(Rectangle((L4, yy + 0.008), R4 - L4, 0.0006, transform=fig.transFigure, color=HAIR)); yy -= 0.012
    return K3.kaydet(fig, out)

# 9) TARİHSEL — dev yüzde + taban oranla kıyas çubukları + maddeler
def tarihsel(kicker, baslik, vurgu, kosul, satirlar, olay_say, alinti, kaynak, out, renk=ACC, tarih=None):
    """satirlar: [(ufuk, oran%, taban%)]"""
    fig, ust, alt = _iskelet(kicker, baslik, vurgu, renk, tarih=tarih, alinti=alinti, kaynak=kaynak)
    fig.text(L4, ust, kosul, fontsize=26, family=SERIF, style="italic", color=MUTED, va="top", wrap=True)
    if len(satirlar) == 1:
        uf, o, tb = satirlar[0]
        fig.text(L4 - 0.005, ust - 0.05, f"%{o:.0f}", fontsize=200, family=SERIF, color=INK, va="top")
        fig.text(R4, ust - 0.10, _aralik("SIRADAN GÜN"), fontsize=12, family=MONO, color=GOLD, ha="right", va="top")
        fig.text(R4, ust - 0.125, f"%{tb:.0f}", fontsize=90, family=SERIF, style="italic", color=GOLD, ha="right", va="top")
        fig.text(L4, ust - 0.32, _aralik(_up(uf)), fontsize=12, family=MONO, color=MUTED, va="top")
        w = R4 - L4; by = ust - 0.36
        fig.add_artist(Rectangle((L4, by), w, 0.008, transform=fig.transFigure, color=HAIR))
        fig.add_artist(Rectangle((L4, by), w * o / 100, 0.008, transform=fig.transFigure, color=renk))
        fig.add_artist(Rectangle((L4 + w * tb / 100 - 0.001, by - 0.008), 0.002, 0.024, transform=fig.transFigure, color=GOLD))
        fig.text(L4, alt + 0.012, _aralik(f"{olay_say} OLAY · FARK {o - tb:+.0f} PUAN · TABAN ORANLA KIYAS"), fontsize=10.5, family=MONO, color=MUTED, va="bottom")
        return K3.kaydet(fig, out)
    yy = ust - 0.09; w = R4 - L4 - 0.22
    for uf, o, tb in satirlar:
        fig.text(L4, yy, _aralik(_up(uf)), fontsize=12, family=MONO, color=MUTED, va="top")
        fig.text(R4, yy + 0.006, f"%{o:.0f}", fontsize=44, family=SERIF, color=INK, ha="right", va="top")
        x0 = L4; fig.add_artist(Rectangle((x0, yy - 0.04), w, 0.008, transform=fig.transFigure, color=HAIR))
        fig.add_artist(Rectangle((x0, yy - 0.04), w * o / 100, 0.008, transform=fig.transFigure, color=renk))
        fig.add_artist(Rectangle((x0 + w * tb / 100 - 0.001, yy - 0.047), 0.002, 0.022, transform=fig.transFigure, color=GOLD))
        fig.text(x0 + w * tb / 100, yy - 0.052, _aralik(f"SIRADAN GÜN %{tb:.0f}"), fontsize=9.5, family=MONO, color=GOLD, ha="center", va="top")
        yy -= 0.115
    fig.text(L4, alt + 0.012, _aralik(f"{olay_say} OLAY · TABAN ORANLA KIYAS"), fontsize=10.5, family=MONO, color=MUTED, va="bottom")
    return K3.kaydet(fig, out)

# 10) SÖZ — yalnız tipografi (görüş/tartışma kartı)
def soz(kicker, metin, vurgu_kelime, alt_satir, kaynak, out, renk=ACC, tarih=None):
    fig = plt.figure(figsize=(10.8, 13.5), dpi=100, facecolor=BG); _zemin(fig, renk)
    t = tarih or dt.date.today()
    fig.text(L4, 0.948, _aralik(_up(kicker)), fontsize=12, family=MONO, color=MUTED, va="center")
    fig.text(R4, 0.948, _aralik(f"{t.day:02d} {AY[t.month]} {t.year}"), fontsize=12, family=MONO, color=MUTED, va="center", ha="right")
    fig.text(L4 - 0.01, 0.86, "“", fontsize=220, family=SERIF, color=renk, va="top", alpha=0.9)
    import textwrap
    yy = 0.60
    for sat in textwrap.wrap(metin, 20):
        stil = "italic" if vurgu_kelime and vurgu_kelime in sat else "normal"
        fig.text(L4, yy, sat, fontsize=72, family=SERIF, style=stil, color=renk if stil == "italic" else INK, va="top"); yy -= 0.075
    fig.add_artist(Rectangle((L4, yy - 0.02), 0.05, 0.0012, transform=fig.transFigure, color=renk))
    fig.text(L4, yy - 0.04, _aralik(_up(alt_satir)), fontsize=12, family=MONO, color=MUTED, va="top")
    fig.add_artist(Rectangle((L4, 0.075), R4 - L4, 0.0007, transform=fig.transFigure, color=HAIR))
    fig.text(L4, 0.048, _aralik("KAYNAK") + "   " + _aralik(_up(kaynak)), fontsize=10.5, family=MONO, color=MUTED, va="center")
    fig.text(R4, 0.048, "Enes Uludağ", fontsize=22, family=SERIF, color=INK, va="center", ha="right")
    return K3.kaydet(fig, out)

# 11) HABER — logo + manşet + 3 numaralı olgu
def haber(kicker, baslik, vurgu, ticker, olgular, alinti, kaynak, out, renk=ACC, tarih=None):
    """olgular: [(rakam/kısa, açıklama)] en çok 3"""
    fig, ust, alt = _iskelet(kicker, baslik, vurgu, renk, ticker=ticker, tarih=tarih, alinti=alinti, kaynak=kaynak)
    h = (ust - alt) / max(len(olgular), 3)
    for i, (r, a) in enumerate(olgular):
        yy = ust - i * h
        fig.text(L4, yy, f"0{i+1}", fontsize=12, family=MONO, color=renk, va="top")
        fig.text(L4 + 0.06, yy + 0.008, r, fontsize=52, family=SERIF, color=INK, va="top")
        fig.text(L4 + 0.06, yy - 0.06, a, fontsize=22, family=SERIF, style="italic", color=MUTED, va="top")
        if i < len(olgular) - 1: fig.add_artist(Rectangle((L4 + 0.06, yy - h + 0.03), R4 - L4 - 0.06, 0.0006, transform=fig.transFigure, color=HAIR))
    return K3.kaydet(fig, out)

# 12) ARALIK — 52 haftalık aralıkta konum (yatay cetvel)
def aralik(kicker, baslik, vurgu, satirlar, alinti, kaynak, out, renk=ACC, tarih=None):
    """satirlar: [(ad, dip, tepe, son)]"""
    fig, ust, alt = _iskelet(kicker, baslik, vurgu, renk, tarih=tarih, alinti=alinti, kaynak=kaynak)
    h = (ust - alt - 0.02) / len(satirlar); x0 = L4; w = R4 - L4
    for i, (ad, d, t, s_) in enumerate(satirlar):
        yy = ust - 0.01 - i * h; p = (s_ - d) / (t - d)
        fig.text(x0, yy, ad, fontsize=30, family=SERIF, color=INK, va="top")
        fig.text(R4, yy, _aralik(f"%{p*100:.0f} KONUMDA"), fontsize=11, family=MONO, color=renk, va="top", ha="right")
        by = yy - 0.065
        fig.add_artist(Rectangle((x0, by), w, 0.004, transform=fig.transFigure, color=HAIR))
        fig.add_artist(Rectangle((x0, by), w * p, 0.004, transform=fig.transFigure, color=renk, alpha=0.5))
        fig.add_artist(matplotlib.patches.Circle((x0 + w * p, by + 0.002), 0.008, transform=fig.transFigure, color=renk, ec=BG, lw=2, zorder=5))
        fig.text(x0 + w * p, by + 0.016, _s(s_), fontsize=15, family=MONO, color=INK, ha="center", va="bottom")
        fig.text(x0, by - 0.012, _aralik("DİP " + _s(d)), fontsize=10, family=MONO, color=MUTED, va="top")
        fig.text(R4, by - 0.012, _aralik("TEPE " + _s(t)), fontsize=10, family=MONO, color=MUTED, va="top", ha="right")
    return K3.kaydet(fig, out)

# 13) KÜÇÜK ÇOKLU — 2x2 mini grafik
def kucuk_coklu(kicker, baslik, vurgu, seriler, alinti, kaynak, out, renk=ACC, tarih=None):
    """seriler: [(ad, [(tarih, değer)])] 4 adet"""
    fig, ust, alt = _iskelet(kicker, baslik, vurgu, renk, tarih=tarih, alinti=alinti, kaynak=kaynak)
    gw = (R4 - L4 - 0.04) / 2; gh = (ust - alt - 0.04) / 2
    for i, (ad, sr) in enumerate(seriler[:4]):
        r, c = divmod(i, 2); x = L4 + c * (gw + 0.04); y = ust - (r + 1) * gh - r * 0.03
        y_ = np.array([v for _, v in sr]); ch = (y_[-1] / y_[0] - 1) * 100; col = UP if ch >= 0 else DOWN
        fig.text(x, y + gh, ad, fontsize=30, family=SERIF, color=INK, va="top")
        fig.text(x + gw, y + gh - 0.004, _y(ch), fontsize=17, family=MONO, color=col, va="top", ha="right")
        ax = fig.add_axes([x, y + 0.01, gw, gh - 0.075]); ax.axis("off")
        ax.plot(range(len(y_)), y_, color=col, lw=2.2); ax.fill_between(range(len(y_)), y_, y_.min(), color=col, alpha=0.08, lw=0)
        ax.scatter([len(y_) - 1], [y_[-1]], s=30, color=col, zorder=5)
    return K3.kaydet(fig, out)

# 14) İÇERİDEN ALIM — kişi, tutar, işlem detayları
def iceriden(kicker, baslik, vurgu, ticker, tutar, kisi, satirlar, alinti, kaynak, out, renk=ACC, tarih=None):
    """satirlar: [(etiket, değer)]"""
    fig, ust, alt = _iskelet(kicker, baslik, vurgu, renk, ticker=ticker, tarih=tarih, alinti=alinti, kaynak=kaynak)
    fig.text(L4, ust, _aralik("AÇIK PİYASA ALIMI"), fontsize=12, family=MONO, color=renk, va="top")
    fig.text(L4 - 0.004, ust - 0.02, tutar, fontsize=150, family=SERIF, color=INK, va="top")
    fig.text(L4, ust - 0.215, kisi, fontsize=28, family=SERIF, style="italic", color=MUTED, va="top")
    yy = ust - 0.29; cw = (R4 - L4) / len(satirlar)
    for i, (et, v) in enumerate(satirlar):
        x = L4 + i * cw
        if i: fig.add_artist(Rectangle((x - 0.015, yy - 0.075), 0.0007, 0.08, transform=fig.transFigure, color=HAIR))
        fig.text(x, yy, _aralik(_up(et)), fontsize=10.5, family=MONO, color=MUTED, va="top")
        fig.text(x, yy - 0.025, v, fontsize=34, family=SERIF, color=INK, va="top")
    return K3.kaydet(fig, out)

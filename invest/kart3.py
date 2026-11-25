#!/usr/bin/env python3
"""KART3 — tek görsel kimlik + gerçek grafik motoru (25.11.2026, Enes 'görselleri geliştirelim').
Tasarım sistemi:
  - Tek koyu tema, tek vurgu rengi (ACC), yükseliş/düşüş için yeşil/kırmızı.
  - Sabit yazı ölçeği (1080 px genişlikte): kicker 26, başlık 64-72, alt 30, grafik etiketi >= 24, sonuç 34, kaynak 22.
    Telefonda (~360 px) en küçük yazı ~8 pt kalır; 20 px altı yazı YOK.
  - Sabit iskelet: üstte kicker + başlık + alt; ortada grafik; altta SONUÇ bandı (tweetin hükmü tek cümle); en altta kaynak + imza.
Kullanım örnekleri: python3 kart3.py ornek  (g/ornek_*.jpg üretir)
"""
import os, json, datetime as dt
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import FancyBboxPatch, Rectangle
import matplotlib.dates as mdates

D = os.path.dirname(os.path.abspath(__file__))
F = os.path.join(D, "font")
for f in os.listdir(F):
    if f.endswith((".otf", ".ttf")): fm.fontManager.addfont(os.path.join(F, f))
FAM = "Inter Display"
MONO = "JetBrains Mono"

BG = "#0B0E14"; PANEL = "#141A24"; GRID = "#222A36"; INK = "#F2F4F8"; MUTED = "#8A94A6"
ACC = "#3D8BFF"; UP = "#2BD47D"; DOWN = "#FF5A5F"; GOLD = "#E8B44C"; GREY = "#5A6475"
HANDLE = "ENES ULUDAĞ"
W, H = 10.8, 13.5  # inç, dpi 100 -> 1080x1350

def _t(fig, x, y, s, size, w="bold", c=INK, **k):
    return fig.text(x, y, s, fontsize=size * 0.72, fontweight=w, color=c, family=FAM, **k)

def cerceve(kicker, baslik, alt="", sonuc="", kaynak=""):
    """Boş kart + iskelet. Döner: fig, grafik alanı [x0,y0,w,h] (figür kesri)."""
    fig = plt.figure(figsize=(W, H), dpi=100, facecolor=BG)
    # vurgu şeridi
    fig.add_artist(Rectangle((0.0555, 0.935), 0.05, 0.006, transform=fig.transFigure, color=ACC))
    _t(fig, 0.0555, 0.905, kicker.upper(), 26, "bold", ACC)
    # başlık (en çok 2 satır, otomatik küçülme)
    size = 72 if len(baslik) <= 28 else (64 if len(baslik) <= 44 else 56)
    import textwrap
    satir = textwrap.wrap(baslik, width=int(26 * 72 / size))
    y = 0.865
    for s in satir[:2]:
        _t(fig, 0.0555, y, s, size, "black", INK, va="top"); y -= size * 1.08 / 1350
    if alt:
        _t(fig, 0.0555, y - 0.012, alt, 30, "medium", MUTED, va="top"); y -= 0.045
    ust = y - 0.03
    alt_y = 0.20 if sonuc else 0.10
    if sonuc:
        fig.add_artist(FancyBboxPatch((0.0555, 0.085), 0.889, 0.085, boxstyle="round,pad=0,rounding_size=0.012",
                                      transform=fig.transFigure, facecolor=PANEL, edgecolor="none"))
        fig.add_artist(Rectangle((0.0555, 0.085), 0.008, 0.085, transform=fig.transFigure, color=ACC))
        _t(fig, 0.085, 0.1275, sonuc, 34 if len(sonuc) <= 46 else 30, "bold", INK, va="center")
    fig.text(0.0555, 0.035, ("KAYNAK  " + kaynak).upper(), fontsize=22 * 0.72, color=MUTED, family=MONO, va="center")
    _t(fig, 0.944, 0.035, HANDLE, 26, "black", INK, ha="right", va="center")
    fig.add_artist(Rectangle((0.0555, 0.062), 0.889, 0.0015, transform=fig.transFigure, color=GRID))
    return fig, [0.0555, alt_y, 0.889, ust - alt_y]

def _ax(fig, rect, pad=(0.06, 0.04, 0.02, 0.02)):
    l, b, r, t = pad
    ax = fig.add_axes([rect[0] + l, rect[1] + b, rect[2] - l - r, rect[3] - b - t], facecolor=BG)
    for s in ax.spines.values(): s.set_visible(False)
    ax.tick_params(colors=MUTED, labelsize=24 * 0.72, length=0)
    for lab in ax.get_xticklabels() + ax.get_yticklabels(): lab.set_family(FAM)
    ax.grid(axis="y", color=GRID, lw=1.2); ax.set_axisbelow(True)
    return ax

def kaydet(fig, out):
    fig.savefig(os.path.join(D, out), dpi=100, facecolor=BG, pil_kwargs={"quality": 92})
    plt.close(fig); return out

# ---------- 1. Fiyat çizgisi + olay işaretleri ----------
def cizgi_olay(kicker, baslik, alt, seri, olaylar, sonuc, kaynak, out, birim="$", vurgu=ACC):
    """seri: [(tarih_str, değer)], olaylar: [(tarih_str, etiket)]"""
    fig, r = cerceve(kicker, baslik, alt, sonuc, kaynak)
    ax = _ax(fig, r, (0.0, 0.05, 0.10, 0.02))
    x = [dt.date.fromisoformat(a) for a, _ in seri]; y = [b for _, b in seri]
    ax.plot(x, y, color=vurgu, lw=4, solid_capstyle="round")
    ax.fill_between(x, y, min(y) * 0.97, color=vurgu, alpha=0.10)
    ax.set_ylim(min(y) * 0.97, max(y) * 1.06)
    ax.yaxis.tick_right()
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%d.%m")); ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.set_xlim(x[0], x[-1] + (x[-1] - x[0]) * 0.16)
    for j, (td, et) in enumerate(olaylar):
        d0 = dt.date.fromisoformat(td); i = min(range(len(x)), key=lambda k: abs((x[k] - d0).days))
        ax.scatter([x[i]], [y[i]], s=180, color=INK, zorder=5, edgecolor=BG, lw=3)
        ax.annotate(et, (x[i], y[i]), xytext=(-150, 70 + 70 * j), textcoords="offset points", ha="center",
                    fontsize=24 * 0.72, color=INK, family=FAM, fontweight="bold",
                    bbox=dict(boxstyle="round,pad=0.45", fc=PANEL, ec=GRID), arrowprops=dict(arrowstyle="-", color=MUTED, lw=1.5))
    son = y[-1]; deg = 100 * (son / y[0] - 1)
    ax.annotate(f"{son:,.0f}{birim}".replace(",", ".") if son > 1000 else f"{son:.2f}".replace(".", ",") + birim,
                (x[-1], son), xytext=(12, 0), textcoords="offset points", va="center",
                fontsize=30 * 0.72, color=vurgu, family=FAM, fontweight="black")
    return kaydet(fig, out)

# ---------- 2. Dönem karşılaştırma (zirveden yol) ----------
def esleme(kicker, baslik, alt, yollar, sonuc, kaynak, out):
    """yollar: [(ad, [yüzde_zirveden...], renk, kalın_mı)]"""
    fig, r = cerceve(kicker, baslik, alt, sonuc, kaynak)
    ax = _ax(fig, r, (0.07, 0.06, 0.12, 0.02))
    for ad, ys, c, kalin in yollar:
        ax.plot(range(len(ys)), ys, color=c, lw=5 if kalin else 3, alpha=1 if kalin else 0.85)
        ax.annotate(ad, (len(ys) - 1, ys[-1]), xytext=(10, 0), textcoords="offset points", va="center",
                    fontsize=28 * 0.72, color=c, family=FAM, fontweight="black")
    ax.axhline(0, color=GREY, lw=1.5)
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"%{v:.0f}".replace("%-", "−%")))
    ax.set_xlabel("zirveden sonra işlem günü", color=MUTED, fontsize=22 * 0.72, family=FAM)
    return kaydet(fig, out)

# ---------- 3. Sıralı yatay çubuk ----------
def siralama(kicker, baslik, alt, satirlar, sonuc, kaynak, out, vurgu=(), birim="%"):
    """satirlar: [(etiket, değer)] -> büyükten küçüğe çizilir; vurgu: vurgulanacak etiketler"""
    fig, r = cerceve(kicker, baslik, alt, sonuc, kaynak)
    ax = _ax(fig, r, (0.14, 0.02, 0.10, 0.02)); ax.grid(False); ax.set_xticks([])
    s = sorted(satirlar, key=lambda x: x[1])
    for i, (et, v) in enumerate(s):
        c = (UP if v >= 0 else DOWN) if et in vurgu or not vurgu else GREY
        ax.barh(i, v, color=c, height=0.62)
        ax.text(v + (0.6 if v >= 0 else -0.6), i, (f"+%{v:.1f}" if v >= 0 else f"−%{abs(v):.1f}").replace(".", ","),
                va="center", ha="left" if v >= 0 else "right", fontsize=26 * 0.72, color=INK, family=FAM, fontweight="bold")
    ax.set_yticks(range(len(s))); ax.set_yticklabels([e for e, _ in s], fontsize=28 * 0.72, color=INK, fontweight="bold")
    ax.axvline(0, color=GREY, lw=1.5)
    lo = min(0, min(v for _, v in s)); hi = max(0, max(v for _, v in s)); pad = (hi - lo) * 0.22
    ax.set_xlim(lo - (pad if lo < 0 else 0), hi + (pad if hi > 0 else 0))
    return kaydet(fig, out)

# ---------- 4. Isı haritası ----------
def isi(kicker, baslik, alt, kutular, sonuc, kaynak, out, kolon=4):
    """kutular: [(etiket, yüzde)]"""
    fig, r = cerceve(kicker, baslik, alt, sonuc, kaynak)
    ax = fig.add_axes(r); ax.axis("off"); ax.set_xlim(0, kolon); n = len(kutular); sat = -(-n // kolon); ax.set_ylim(sat, 0)
    mx = max(abs(v) for _, v in kutular) or 1
    for i, (et, v) in enumerate(kutular):
        cx, cy = i % kolon, i // kolon; a = 0.25 + 0.75 * min(1, abs(v) / mx)
        ax.add_patch(FancyBboxPatch((cx + 0.04, cy + 0.05), 0.92, 0.9, boxstyle="round,pad=0,rounding_size=0.06",
                                    fc=UP if v >= 0 else DOWN, alpha=a, ec="none"))
        ax.text(cx + 0.5, cy + 0.40, et, ha="center", va="center", fontsize=34 * 0.72, color=INK, family=FAM, fontweight="black")
        ax.text(cx + 0.5, cy + 0.66, (f"+%{v:.1f}" if v >= 0 else f"−%{abs(v):.1f}").replace(".", ","), ha="center", va="center",
                fontsize=28 * 0.72, color=INK, family=FAM, fontweight="bold")
    return kaydet(fig, out)

# ---------- 5. Bilanço rakam kartı (kutular kalır, sadeleşir) ----------
def bilanco(kicker, baslik, alt, kalemler, sonuc, kaynak, out):
    """kalemler: [(ad, gelen, beklenti_metni, iyi_mi)] en çok 4"""
    fig, r = cerceve(kicker, baslik, alt, sonuc, kaynak)
    n = len(kalemler); h = r[3] / n
    for i, (ad, gel, bek, iyi) in enumerate(kalemler):
        y0 = r[1] + r[3] - (i + 1) * h
        fig.add_artist(FancyBboxPatch((r[0], y0 + 0.008), r[2], h - 0.016, boxstyle="round,pad=0,rounding_size=0.012",
                                      transform=fig.transFigure, fc=PANEL, ec="none"))
        _t(fig, r[0] + 0.03, y0 + h * 0.62, ad.upper(), 24, "bold", MUTED, va="center")
        _t(fig, r[0] + 0.03, y0 + h * 0.32, gel, 64, "black", INK, va="center")
        renk = UP if iyi else (DOWN if iyi is False else MUTED)
        _t(fig, r[0] + r[2] - 0.03, y0 + h * 0.45, bek, 28, "bold", renk, ha="right", va="center")
    return kaydet(fig, out)

# ---------- 6. Göreli performans (iki çizgi, 100'e endeks) ----------
def goreli(kicker, baslik, alt, seriler, sonuc, kaynak, out):
    """seriler: [(ad, [(tarih,değer)], renk)] -> ilk gün = 100"""
    fig, r = cerceve(kicker, baslik, alt, sonuc, kaynak)
    ax = _ax(fig, r, (0.0, 0.05, 0.08, 0.02)); ax.yaxis.tick_right()
    x0 = dt.date.fromisoformat(seriler[0][1][0][0]); x1 = dt.date.fromisoformat(seriler[0][1][-1][0])
    ax.set_xlim(x0, x1 + (x1 - x0) * 0.30)
    for ad, s, c in seriler:
        x = [dt.date.fromisoformat(a) for a, _ in s]; y = [100 * b / s[0][1] for _, b in s]
        ax.plot(x, y, color=c, lw=4)
        dv = y[-1] - 100
        ax.annotate(f"{ad}\n" + (f"+%{dv:.0f}" if dv >= 0 else f"−%{abs(dv):.0f}"),
                    (x[-1], y[-1]), xytext=(10, 0), textcoords="offset points", va="center",
                    fontsize=26 * 0.72, color=c, family=FAM, fontweight="black")
    ax.axhline(100, color=GREY, lw=1.5)
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%d.%m")); ax.xaxis.set_major_locator(mdates.MonthLocator())
    return kaydet(fig, out)

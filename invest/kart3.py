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

def _damga(alt, son_tarih):
    """KURAL 84: grafikli kartta verinin son günü alt başlıkta görünür (okur neyi gördüğünü bilir)."""
    g = dt.date.fromisoformat(son_tarih)
    return (alt + " • " if alt else "") + f"son veri {g.day:02d}.{g.month:02d}.{g.year}"

def dogrula(seri, kaynak_seri):
    """KURAL 84: çizilecek seri kaynaktan değiştirilmeden mi geldi? Her nokta aynı tarih/değer olmalı."""
    k = dict(kaynak_seri)
    hata = [(a, b, k.get(a)) for a, b in seri if a not in k or abs(k[a] - b) > 1e-9]
    if hata: raise ValueError(f"GRAFIK VERISI KAYNAKLA UYUSMUYOR: {hata[:3]}")
    return True

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
    alt = _damga(alt, seri[-1][0])
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
    alt = _damga(alt, seriler[0][1][-1][0])
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

# ================= v2 (25.11 11:40, Enes 'piyasanın en iyisi olmalıyız') =================
def _yuzde(v, ondalik=1):
    t = f"{abs(v):.{ondalik}f}".replace(".", ",")
    return ("+%" if v >= 0 else "−%") + t

def _kahraman(fig, rect, deger, etiket, renk):
    """Grafiğin sol üstüne büyük 'kahraman rakam' (okur ilk bunu görür)."""
    _t(fig, rect[0] + 0.005, rect[1] + rect[3] - 0.005, deger, 96, "black", renk, va="top")
    _t(fig, rect[0] + 0.008, rect[1] + rect[3] - 0.085, etiket, 26, "bold", MUTED, va="top")

def cizgi_pro(kicker, baslik, alt, seri, olaylar, sonuc, kaynak, out, kahraman=None, zirve=True, golge=None, ref=None, renk=ACC):
    """Açıklamalı çizgi: zirve çizgisi + zirveden düşüş gölgesi + kahraman rakam + olay notları.
    golge: (baş_tarih, son_tarih, etiket) gri dönem bandı; ref: [(değer, etiket)] yatay referans çizgileri."""
    alt = _damga(alt, seri[-1][0])
    fig, r = cerceve(kicker, baslik, alt, sonuc, kaynak)
    ax = _ax(fig, [r[0], r[1], r[2], r[3] - 0.10], (0.0, 0.05, 0.12, 0.0))
    x = [dt.date.fromisoformat(a) for a, _ in seri]; y = [b for _, b in seri]
    lo, hi = min(y), max(y); pad = (hi - lo) * 0.06
    ax.set_ylim(lo - pad, hi + pad * 2.5); ax.yaxis.tick_right()
    ax.set_xlim(x[0], x[-1] + (x[-1] - x[0]) * 0.13)
    if golge:
        a, b, et = golge; a, b = dt.date.fromisoformat(a), dt.date.fromisoformat(b)
        ax.axvspan(a, b, color=INK, alpha=0.06, lw=0)
        ax.text(a + (b - a) / 2, hi + pad * 1.6, et, ha="center", fontsize=22 * 0.72, color=MUTED, family=FAM, fontweight="bold")
    ax.plot(x, y, color=renk, lw=4.5, solid_joinstyle="round", zorder=3)
    if zirve:
        zi = y.index(hi)
        ax.axhline(hi, color=MUTED, lw=1.4, ls=(0, (4, 4)))
        ax.text(x[0], hi + pad * 0.5, f"zirve {x[zi].day:02d}.{x[zi].month:02d}  {_sayi(hi)}", fontsize=22 * 0.72, color=MUTED, family=FAM, fontweight="bold")
        ax.fill_between(x[zi:], y[zi:], hi, color=DOWN, alpha=0.12, lw=0)
    for v, et in (ref or []):
        ax.axhline(v, color=GOLD, lw=1.6, ls=(0, (2, 3)))
        ax.text(x[-1] + (x[-1] - x[0]) * 0.13, v, " " + et, va="center", ha="right", fontsize=22 * 0.72, color=GOLD, family=FAM, fontweight="bold")
    for j, (td, et) in enumerate(olaylar):
        d0 = dt.date.fromisoformat(td); i = min(range(len(x)), key=lambda k: abs((x[k] - d0).days))
        ax.scatter([x[i]], [y[i]], s=150, color=INK, zorder=5, edgecolor=BG, lw=3)
        ax.annotate(et, (x[i], y[i]), xytext=(-190, 40 + 62 * j), textcoords="offset points", ha="center",
                    fontsize=22 * 0.72, color=INK, family=FAM, fontweight="bold",
                    bbox=dict(boxstyle="round,pad=0.45", fc=PANEL, ec=GRID), arrowprops=dict(arrowstyle="-", color=MUTED, lw=1.4))
    ax.scatter([x[-1]], [y[-1]], s=120, color=renk, zorder=6)
    ax.annotate(_sayi(y[-1]), (x[-1], y[-1]), xytext=(14, 0), textcoords="offset points", va="center",
                fontsize=28 * 0.72, color=renk, family=FAM, fontweight="black")
    ax.xaxis.set_major_locator(mdates.MonthLocator()); _tr_eksen(ax)
    if kahraman: _kahraman(fig, r, kahraman[0], kahraman[1], kahraman[2] if len(kahraman) > 2 else (DOWN if kahraman[0].startswith("−") else UP))
    return kaydet(fig, out)

AYLAR = ["", "Oca", "Şub", "Mar", "Nis", "May", "Haz", "Tem", "Ağu", "Eyl", "Eki", "Kas", "Ara"]
def _tr_eksen(ax):
    ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: AYLAR[mdates.num2date(v).month]))
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: _sayi(v) if abs(v) >= 1000 else (f"{v:.0f}" if v == int(v) else f"{v:.1f}".replace(".", ","))))

def _ayir(ys, aralik):
    """Etiket y konumlarını çakışmasın diye en az 'aralik' kadar ayırır (sıra korunur)."""
    idx = sorted(range(len(ys)), key=lambda i: ys[i]); out = list(ys)
    for k in range(1, len(idx)):
        if out[idx[k]] - out[idx[k - 1]] < aralik: out[idx[k]] = out[idx[k - 1]] + aralik
    return out

def _sayi(v):
    if v >= 1000: return f"{v:,.0f}".replace(",", ".")
    return f"{v:.2f}".replace(".", ",")

def kucuk_coklu(kicker, baslik, alt, seriler, sonuc, kaynak, out, kolon=2):
    """Küçük çoklu: her hisse için kendi mini grafiği + dönem değişimi. seriler: [(ad, [(tarih,değer)])]"""
    alt = _damga(alt, seriler[0][1][-1][0])
    fig, r = cerceve(kicker, baslik, alt, sonuc, kaynak)
    n = len(seriler); sat = -(-n // kolon); cw = r[2] / kolon; ch = r[3] / sat
    for i, (ad, s) in enumerate(seriler):
        cx = r[0] + (i % kolon) * cw; cy = r[1] + r[3] - (i // kolon + 1) * ch
        fig.add_artist(FancyBboxPatch((cx + 0.006, cy + 0.006), cw - 0.012, ch - 0.012, boxstyle="round,pad=0,rounding_size=0.01",
                                      transform=fig.transFigure, fc=PANEL, ec="none", zorder=-5))
        y = [b for _, b in s]; dv = 100 * (y[-1] / y[0] - 1); c = UP if dv >= 0 else DOWN
        _t(fig, cx + 0.022, cy + ch - 0.03, ad, 30, "black", INK, va="top")
        _t(fig, cx + cw - 0.022, cy + ch - 0.03, _yuzde(dv), 30, "black", c, va="top", ha="right")
        ax = fig.add_axes([cx + 0.02, cy + 0.02, cw - 0.04, ch - 0.085]); ax.axis("off"); ax.set_zorder(5); ax.patch.set_alpha(0)
        ax.plot(range(len(y)), y, color=c, lw=2.8); ax.fill_between(range(len(y)), y, min(y), color=c, alpha=0.12, lw=0)
        ax.set_xlim(0, len(y) - 1)
    return kaydet(fig, out)

def egim(kicker, baslik, alt, satirlar, sol_et, sag_et, sonuc, kaynak, out):
    """Eğim grafiği: iki tarih arasında her hissenin değişimi. satirlar: [(ad, sol_yüzde, sağ_yüzde)] (aynı baz)"""
    fig, r = cerceve(kicker, baslik, alt, sonuc, kaynak)
    ax = _ax(fig, r, (0.16, 0.04, 0.16, 0.04)); ax.grid(False); ax.set_yticks([])
    ax.set_xticks([0, 1]); ax.set_xticklabels([sol_et, sag_et], fontsize=26 * 0.72, color=INK, fontweight="bold")
    allv = [v for _, a, b in satirlar for v in (a, b)]; gap = (max(allv) - min(allv)) * 0.045
    ya = _ayir([a for _, a, _ in satirlar], gap); yb = _ayir([b for _, _, b in satirlar], gap)
    for k, (ad, a, b) in enumerate(satirlar):
        c = UP if b >= a else DOWN
        ax.plot([0, 1], [a, b], color=c, lw=3.5, marker="o", ms=10, alpha=0.9)
        ax.text(-0.04, ya[k], f"{ad} {_yuzde(a,0)}", ha="right", va="center", fontsize=22 * 0.72, color=INK, family=FAM, fontweight="bold")
        ax.text(1.04, yb[k], f"{_yuzde(b,0)} {ad}", ha="left", va="center", fontsize=22 * 0.72, color=c, family=FAM, fontweight="bold")
    ax.axhline(0, color=GREY, lw=1.2); ax.set_xlim(-0.02, 1.02)
    return kaydet(fig, out)

def aralik(kicker, baslik, alt, satirlar, sonuc, kaynak, out):
    """52 haftalık aralık: her hisse için en düşük-en yüksek çubuğu ve bugünkü yeri. satirlar: [(ad, dusuk, yuksek, son)]"""
    fig, r = cerceve(kicker, baslik, alt, sonuc, kaynak)
    ax = _ax(fig, r, (0.13, 0.05, 0.22, 0.02)); ax.grid(False); ax.set_xlim(-2, 102)
    ax.set_xticks([0, 50, 100]); ax.set_xticklabels(["yıllık dip", "orta", "yıllık zirve"], fontsize=22 * 0.72, color=MUTED)
    s = sorted(satirlar, key=lambda z: (z[3] - z[1]) / (z[2] - z[1]))
    for i, (ad, lo, hi, son) in enumerate(s):
        p = 100 * (son - lo) / (hi - lo)
        ax.plot([0, 100], [i, i], color=GRID, lw=12, solid_capstyle="round")
        ax.plot([0, p], [i, i], color=ACC, lw=12, solid_capstyle="round", alpha=0.55)
        ax.scatter([p], [i], s=260, color=INK, zorder=5, edgecolor=ACC, lw=3)
        ax.text(104, i, f"zirveden {_yuzde(100*(son/hi-1),0)}", ha="left", va="center", fontsize=22 * 0.72, color=MUTED, family=FAM, fontweight="bold")
    ax.set_yticks(range(len(s))); ax.set_yticklabels([z[0] for z in s], fontsize=28 * 0.72, color=INK, fontweight="bold")
    ax.set_ylim(-0.6, len(s) - 0.2)
    return kaydet(fig, out)

def sutun(kicker, baslik, alt, donemler, seriler, sonuc, kaynak, out, birim=" Mr $"):
    """Bilanço çeyrek sütunu (gruplu). donemler: ['1Ç','2Ç','3Ç']; seriler: [(ad, [değerler], renk)]
    Veri şirket bülteni/görüşme dökümünden; her değer 2 kaynak (kural 84 + 3)."""
    fig, r = cerceve(kicker, baslik, alt, sonuc, kaynak)
    ax = _ax(fig, [r[0], r[1], r[2], r[3] - 0.05], (0.02, 0.05, 0.02, 0.0)); ax.set_yticks([]); ax.grid(False)
    n = len(seriler); w = 0.8 / n
    mx = max(v for _, vs, _ in seriler for v in vs)
    for j, (ad, vs, c) in enumerate(seriler):
        xs = [i - 0.4 + w * (j + 0.5) for i in range(len(donemler))]
        ax.bar(xs, vs, width=w * 0.88, color=c)
        for x_, v in zip(xs, vs):
            ax.text(x_, v + mx * 0.015, f"{v:.1f}".replace(".", ",").replace(",0", ""), ha="center", va="bottom",
                    fontsize=26 * 0.72, color=INK, family=FAM, fontweight="black")
    ax.set_xticks(range(len(donemler))); ax.set_xticklabels(donemler, fontsize=28 * 0.72, color=INK, fontweight="bold")
    ax.set_ylim(0, mx * 1.12)
    x0 = r[0] + 0.01
    for j, (ad, _, c) in enumerate(seriler):
        fig.add_artist(Rectangle((x0, r[1] + r[3] - 0.03), 0.022, 0.016, transform=fig.transFigure, color=c))
        t = _t(fig, x0 + 0.03, r[1] + r[3] - 0.022, ad, 24, "bold", INK, va="center")
        x0 += 0.05 + len(ad) * 0.0125
    _t(fig, r[0] + r[2], r[1] + r[3] - 0.022, birim.strip(), 22, "bold", MUTED, ha="right", va="center")
    return kaydet(fig, out)

# ================= v3 (25.11 11:45, 'daha da iyisini yapabiliriz') =================
from PIL import Image as _Img
def _logo_png(t):
    p = os.path.join(D, "logo", f"{t}.png"); ok = os.path.join(D, "logo", "DOGRULANDI.txt")
    if not os.path.exists(p) or t not in open(ok, encoding="utf-8").read().split(): return None
    return _Img.open(p).convert("RGBA")

def hikaye(kicker, baslik, alt, ticker, seri, kiyas, notlar, kutular, sonuc, kaynak, out, kiyas_ad="Nasdaq 100"):
    """Hikâye grafiği: hisse (kalın, vurgu) + kıyas endeksi (soluk gri) ilk gün=100; tarihli cümle notları; sağ üstte doğrulanmış logo;
    üstte 3 kilit rakam şeridi. notlar: [(tarih, 'kısa cümle', 'ust'|'alt')]; kutular: [(rakam, etiket, renk)] x3"""
    alt = _damga(alt, seri[-1][0])
    fig, r = cerceve(kicker, baslik, alt, sonuc, kaynak)
    lg = _logo_png(ticker)
    if lg:
        h = 120; lg = lg.resize((int(lg.width * h / lg.height), h))
        fig.figimage(lg, xo=int(1080 * 0.944) - lg.width, yo=int(1350 * 0.865) - h + 10, zorder=10)
    # kilit rakam şeridi
    kw = r[2] / 3; ky = r[1] + r[3] - 0.10
    for i, (rk, et, c) in enumerate(kutular[:3]):
        x0 = r[0] + i * kw
        fig.add_artist(FancyBboxPatch((x0 + 0.004, ky), kw - 0.008, 0.095, boxstyle="round,pad=0,rounding_size=0.01",
                                      transform=fig.transFigure, fc=PANEL, ec="none", zorder=-5))
        _t(fig, x0 + 0.022, ky + 0.062, rk, 44, "black", c, va="center")
        _t(fig, x0 + 0.022, ky + 0.022, et, 22, "bold", MUTED, va="center")
    ax = _ax(fig, [r[0], r[1], r[2], r[3] - 0.12], (0.0, 0.05, 0.06, 0.0)); ax.yaxis.tick_right()
    x = [dt.date.fromisoformat(a) for a, _ in seri]; y = [100 * b / seri[0][1] for _, b in seri]
    kd = dict(kiyas); xk = [dt.date.fromisoformat(a) for a, _ in seri if a in kd]; yk = [100 * kd[a] / kd[seri[0][0]] for a, _ in seri if a in kd]
    ax.plot(xk, yk, color=GREY, lw=2.5, alpha=0.9)
    ax.plot(x, y, color=ACC, lw=4.5, solid_joinstyle="round")
    ax.axhline(100, color=GRID, lw=1.5)
    ax.set_xlim(x[0], x[-1] + (x[-1] - x[0]) * 0.24)
    lo = min(min(y), min(yk)); hi = max(max(y), max(yk)); ax.set_ylim(lo - (hi - lo) * 0.08, hi + (hi - lo) * 0.10)
    for xx, yy, c, ad in ((x[-1], y[-1], ACC, ticker), (xk[-1], yk[-1], GREY, kiyas_ad)):
        ax.scatter([xx], [yy], s=110, color=c, zorder=6)
        ax.annotate(f"{ad}\n{_yuzde(yy-100,0)}", (xx, yy), xytext=(12, 0), textcoords="offset points", va="center",
                    fontsize=24 * 0.72, color=c if c != GREY else MUTED, family=FAM, fontweight="black", linespacing=0.95)
    for td, cumle, yon in notlar:
        d0 = dt.date.fromisoformat(td); i = min(range(len(x)), key=lambda k: abs((x[k] - d0).days))
        ax.scatter([x[i]], [y[i]], s=140, color=INK, zorder=7, edgecolor=BG, lw=3)
        dx, dy = (-150, 80) if yon == "ust" else (-230, 10)
        ax.annotate(cumle, (x[i], y[i]), xytext=(dx, dy), textcoords="offset points", ha="center", va="center",
                    fontsize=21 * 0.72, color=INK, family=FAM, fontweight="bold", linespacing=1.1,
                    bbox=dict(boxstyle="round,pad=0.55", fc=PANEL, ec=ACC, lw=1.5), arrowprops=dict(arrowstyle="-", color=ACC, lw=1.6))
    ax.xaxis.set_major_locator(mdates.MonthLocator()); _tr_eksen(ax)
    return kaydet(fig, out)

def esleme_video(kicker, baslik, alt, yollar, sonuc, kaynak, out_mp4, sure=7, fps=30):
    """Animasyonlu karşılaştırma: çizgiler soldan sağa çizilir, son 2 sn sonuç bandıyla durur. X akışında video kendiliğinden oynar."""
    import subprocess, tempfile, shutil
    tmp = tempfile.mkdtemp(); n = max(len(ys) for _, ys, _, _ in yollar)
    kare = sure * fps; ciz = int(kare * 0.7)
    for f in range(kare):
        k = max(2, int(n * min(1, (f + 1) / ciz)))
        kes = [(ad, ys[:k], c, kal) for ad, ys, c, kal in yollar]
        fig, r = cerceve(kicker, baslik, alt, sonuc if f >= ciz else " ", kaynak)
        ax = _ax(fig, r, (0.07, 0.06, 0.12, 0.02)); ax.set_xlim(0, n + 2)
        lo = min(min(ys) for _, ys, _, _ in yollar); ax.set_ylim(lo * 1.12, 2)
        for ad, ys, c, kal in kes:
            ax.plot(range(len(ys)), ys, color=c, lw=5 if kal else 3)
            ax.scatter([len(ys) - 1], [ys[-1]], s=90 if kal else 50, color=c, zorder=5)
            ax.annotate(ad, (len(ys) - 1, ys[-1]), xytext=(10, 0), textcoords="offset points", va="center",
                        fontsize=28 * 0.72, color=c, family=FAM, fontweight="black")
        ax.axhline(0, color=GREY, lw=1.5)
        ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"%{v:.0f}".replace("%-", "−%")))
        ax.set_xlabel("zirveden sonra işlem günü", color=MUTED, fontsize=22 * 0.72, family=FAM)
        fig.savefig(os.path.join(tmp, f"{f:04d}.png"), dpi=100, facecolor=BG); plt.close(fig)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(fps), "-i", os.path.join(tmp, "%04d.png"),
                    "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p", "-movflags", "+faststart",
                    os.path.join(D, out_mp4)], check=True)
    shutil.rmtree(tmp); return out_mp4

# ================= v4 'dosya' (25.11 11:50: veri katmanı + sinematik + video + 'çok emek verilmiş' hissi) =================
import numpy as _np
MARKA = {"NVDA": "#76B900", "AMD": "#ED1C24", "AVGO": "#CC092F", "DELL": "#0076CE", "MU": "#2E8BC0", "TSM": "#E60012",
         "RKLB": "#E03C31", "NBIS": "#D9F95E", "VRT": "#E8A33D", "DOCN": "#0080FF", "AXON": "#FFD100", "SITM": "#E31B23",
         "CBRS": "#F15A29", "ORCL": "#C74634", "MSFT": "#00A4EF", "GOOGL": "#4285F4", "META": "#0866FF", "AMZN": "#FF9900", "PLTR": "#D8D8D8"}

def _zemin(fig, renk):
    """Sinematik zemin: koyu taban + sağ üstte marka renginde yumuşak ışık + ince doku."""
    ax = fig.add_axes([0, 0, 1, 1], zorder=-20); ax.axis("off")
    yy, xx = _np.mgrid[0:1350, 0:1080]
    d = _np.sqrt(((xx - 900) / 900) ** 2 + ((yy - 120) / 800) ** 2)
    g = _np.clip(1 - d, 0, 1) ** 2.2 * 0.32
    base = _np.array(matplotlib.colors.to_rgb(BG)); c = _np.array(matplotlib.colors.to_rgb(renk))
    img = base[None, None, :] * (1 - g[..., None]) + c[None, None, :] * g[..., None]
    img += (_np.random.default_rng(7).random((1350, 1080, 1)) - 0.5) * 0.018
    ax.imshow(_np.clip(img, 0, 1), aspect="auto", extent=[0, 1, 0, 1])

def _parlak(ax, x, y, renk, lw=4.5):
    for k, a in ((5.0, 0.05), (3.2, 0.08), (2.0, 0.12)):
        ax.plot(x, y, color=renk, lw=lw * k, alpha=a, solid_capstyle="round", zorder=3)
    ax.plot(x, y, color=renk, lw=lw, solid_capstyle="round", zorder=4)

def dosya(ticker, kicker, baslik, spot, seri, kiyas, olaylar, sonuc, kaynak, out, kiyas_ad="Nasdaq 100"):
    """Hisse dosyası: marka ışıklı zemin, parlayan fiyat çizgisi + kıyas, olay şeritleri, alt panelde 'zirveden uzaklık',
    altta 4 istatistik ve yöntem notu. olaylar: [(tarih, kısa etiket)]. Yerleşim yukarıdan aşağı sırayla hesaplanır."""
    import textwrap
    renk = MARKA.get(ticker, ACC)
    fig = plt.figure(figsize=(W, H), dpi=100, facecolor=BG); _zemin(fig, renk)
    son = dt.date.fromisoformat(seri[-1][0]); L = 0.0555; R = 0.944
    fig.text(L, 0.94, kicker.upper(), fontsize=24 * 0.72, color=renk, family=FAM, fontweight="black", va="center")
    fig.text(R, 0.94, f"DOSYA • {son.day:02d}.{son.month:02d}.{son.year}", fontsize=22 * 0.72, color=MUTED, family=MONO, ha="right", va="center")
    fig.add_artist(Rectangle((L, 0.922), R - L, 0.0012, transform=fig.transFigure, color=GRID))
    lg = _logo_png(ticker); lw_ = 0
    if lg:
        h = 100; lg = lg.resize((int(lg.width * h / lg.height), h)); lw_ = lg.width
        fig.figimage(lg, xo=int(1080 * R) - lg.width, yo=int(1350 * 0.905) - h, zorder=10)
    size = 64; y = 0.905
    for s_ in textwrap.wrap(baslik, 26 if lg else 30)[:3]:
        _t(fig, L, y, s_, size, "black", INK, va="top"); y -= 0.056
    y -= 0.006
    fig.text(L, y, spot, fontsize=32 * 0.72, color="#C9CED8", family="Instrument Serif", style="italic", va="top"); y -= 0.045
    # lejant
    fig.add_artist(Rectangle((L, y - 0.012), 0.03, 0.005, transform=fig.transFigure, color=renk))
    fig.text(L + 0.038, y - 0.0095, ticker, fontsize=22 * 0.72, color=renk, family=FAM, fontweight="black", va="center")
    fig.add_artist(Rectangle((L + 0.13, y - 0.012), 0.03, 0.005, transform=fig.transFigure, color="#6B7385"))
    fig.text(L + 0.168, y - 0.0095, f"{kiyas_ad} (aynı başlangıca ölçekli)", fontsize=22 * 0.72, color="#8A94A6", family=FAM, fontweight="bold", va="center")
    ust = y - 0.03
    x = [dt.date.fromisoformat(a) for a, _ in seri]; yv = [b for _, b in seri]
    kd = dict(kiyas); yk = [kd[a] * yv[0] / kd[seri[0][0]] for a, _ in seri if a in kd]; xk = [dt.date.fromisoformat(a) for a, _ in seri if a in kd]
    ana_alt = 0.43
    ax = fig.add_axes([L, ana_alt, 0.78, ust - ana_alt]); ax.set_facecolor("none")
    for s_ in ax.spines.values(): s_.set_visible(False)
    ax.tick_params(colors=MUTED, labelsize=22 * 0.72, length=0); ax.grid(axis="y", color=GRID, lw=1)
    ax.plot(xk, yk, color="#6B7385", lw=2.2, alpha=0.85, zorder=2)
    ax.fill_between(x, yv, min(yv + yk) * 0.95, color=renk, alpha=0.07, lw=0, zorder=1)
    _parlak(ax, x, yv, renk)
    lo = min(yv + yk); hi = max(yv + yk); ax.set_ylim(lo - (hi - lo) * 0.05, hi + (hi - lo) * 0.30)
    ax.set_xlim(x[0], x[-1]); ax.set_xticks([])
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:.0f}"))
    for j, (td, et) in enumerate(olaylar):
        d0 = dt.date.fromisoformat(td); i = min(range(len(x)), key=lambda k: abs((x[k] - d0).days))
        ax.axvline(x[i], color=INK, lw=1, alpha=0.35, ls=(0, (2, 3)), zorder=2)
        ty = hi + (hi - lo) * (0.26 - 0.15 * j)
        ax.text(x[i], ty, et, ha="right", va="center", fontsize=19 * 0.72, color=BG, family=FAM, fontweight="black",
                bbox=dict(boxstyle="round,pad=0.35", fc=INK, ec="none"), zorder=6)
        ax.scatter([x[i]], [yv[i]], s=90, color=INK, edgecolor=BG, lw=2, zorder=7)
    yl = ax.get_ylim(); fy = ana_alt + (ust - ana_alt) * (yv[-1] - yl[0]) / (yl[1] - yl[0])
    fig.text(L + 0.79, fy, _sayi(yv[-1]), fontsize=30 * 0.72, color=renk, family=FAM, fontweight="black", va="center")
    # zirveden uzaklık paneli
    tepe = []; m = -1
    for v in yv: m = max(m, v); tepe.append(100 * (v / m - 1))
    fig.text(L, 0.405, "ZİRVEDEN UZAKLIK", fontsize=19 * 0.72, color=MUTED, family=MONO, va="center")
    a2 = fig.add_axes([L, 0.31, 0.78, 0.085]); a2.set_facecolor("none")
    for s_ in a2.spines.values(): s_.set_visible(False)
    a2.fill_between(x, tepe, 0, color=DOWN, alpha=0.35, lw=0); a2.plot(x, tepe, color=DOWN, lw=1.6)
    a2.set_xlim(x[0], x[-1]); a2.tick_params(colors=MUTED, labelsize=20 * 0.72, length=0)
    a2.yaxis.tick_right(); a2.set_yticks([0, round(min(tepe) / 10) * 10]); a2.grid(axis="y", color=GRID, lw=1)
    a2.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"%{v:.0f}".replace("%-", "−%")))
    a2.xaxis.set_major_locator(mdates.MonthLocator(interval=2)); a2.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: AYLAR[mdates.num2date(v).month]))
    # 4 istatistik
    yil = 100 * (yv[-1] / yv[0] - 1); kyil = 100 * (yk[-1] / yk[0] - 1)
    st4 = [(_yuzde(yil, 0), f"{ticker}, dönem"), (_yuzde(kyil, 0), f"{kiyas_ad}, dönem"), (_yuzde(min(tepe), 0), "en derin düşüş"), (_yuzde(tepe[-1], 0), "bugün zirveden")]
    for i, (rk, et) in enumerate(st4):
        x0 = L + i * (R - L) / 4
        fig.add_artist(FancyBboxPatch((x0 + 0.003, 0.17), (R - L) / 4 - 0.006, 0.08, boxstyle="round,pad=0,rounding_size=0.01",
                                      transform=fig.transFigure, fc=(1, 1, 1, 0.04), ec=(1, 1, 1, 0.08), lw=1))
        _t(fig, x0 + 0.02, 0.225, rk, 40, "black", UP if rk.startswith("+") else DOWN, va="center")
        _t(fig, x0 + 0.02, 0.188, et, 20, "bold", MUTED, va="center")
    fig.add_artist(Rectangle((L, 0.112), 0.008, 0.042, transform=fig.transFigure, color=renk))
    _t(fig, L + 0.02, 0.133, sonuc, 34 if len(sonuc) < 42 else 30, "black", INK, va="center")
    fig.text(L, 0.083, "YÖNTEM  günlük kapanış • zirveden uzaklık: o güne kadarki en yüksek kapanışa göre", fontsize=17 * 0.72, color="#6B7385", family=MONO, va="center")
    fig.add_artist(Rectangle((L, 0.062), R - L, 0.0012, transform=fig.transFigure, color=GRID))
    fig.text(L, 0.035, ("KAYNAK  " + kaynak).upper(), fontsize=20 * 0.72, color=MUTED, family=MONO, va="center")
    _t(fig, R, 0.035, HANDLE, 26, "black", INK, ha="right", va="center")
    return kaydet(fig, out)

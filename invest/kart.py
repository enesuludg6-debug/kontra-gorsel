"""EnesInvestUS kart üretici. Koyu, minimal; Instrument Serif + JetBrains Mono. 1080x1350 JPG.

Kullanım:
    import sys; sys.path.insert(0, "/home/claude/kontra-gorsel/invest")
    from kart import haber, rakamlar, liste

    haber("$NVDA", "BİLANÇO SONRASI", "Veri merkezi geliri beklentiyi geçti",
          ["Gelir 57,0 milyar $ (+%62)", "Rehberlik piyasanın üstünde"], "KAYNAK: ŞİRKET AÇIKLAMASI", "g/nvda.jpg")
    rakamlar("$CRDO", "Q2 FY27 sonuçları", [("GELİR", "479M $", "+%115 YoY"), ("EPS", "0,52 $", "bekl. 0,47")],
             "Yorum cümlesi tek satır.", "KAYNAK: ŞİRKET", "g/crdo.jpg")
    liste("PİYASA KAPANIŞI", "14 Kasım 2026", [("S&P 500", "+0,4%"), ("Nasdaq", "-0,2%")], "KAYNAK: ...", "g/kapanis.jpg")
Renk: yükseliş yeşil, düşüş kırmızı otomatik (değer '+' / '-' ile başlıyorsa).
"""
import os
from PIL import Image, ImageDraw, ImageFont

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "font")
W, H = 1080, 1350
BG = (12, 12, 14)
INK = (238, 236, 230)
MUTED = (128, 128, 136)
LINE = (44, 44, 50)
ACC = (212, 175, 105)      # soluk altın vurgu
UP = (88, 200, 140)
DOWN = (232, 92, 92)
HANDLE = "ENES ULUDAĞ"


def serif(s, italic=False):
    return ImageFont.truetype(os.path.join(D, "InstrumentSerif-Italic.ttf" if italic else "InstrumentSerif-Regular.ttf"), s)


def mono(s, w=400):
    f = ImageFont.truetype(os.path.join(D, "JetBrainsMono.ttf"), s)
    try:
        f.set_variation_by_axes([w])
    except Exception:
        pass
    return f


def _wrap(d, txt, font, maxw):
    out, cur = [], ""
    for w in txt.split():
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= maxw:
            cur = t
        else:
            if cur:
                out.append(cur)
            cur = w
    if cur:
        out.append(cur)
    return out


def _fit_serif(d, txt, size, maxw, maxlines, minsize=56):
    while size > minsize:
        f = serif(size)
        lines = _wrap(d, txt, f, maxw)
        if len(lines) <= maxlines:
            return f, lines
        size -= 4
    f = serif(minsize)
    return f, _wrap(d, txt, f, maxw)


def _tone(v):
    v = v.strip()
    if v.startswith("+"):
        return UP
    if v.startswith("-") or v.startswith("−"):
        return DOWN
    return INK


def _frame(d, ust_sol, ust_sag=""):
    d.text((72, 70), ust_sol, font=mono(24, 600), fill=ACC)
    if ust_sag:
        d.text((W - 72, 70), ust_sag, font=mono(22), fill=MUTED, anchor="ra")
    d.line((72, 118, W - 72, 118), fill=LINE, width=2)


def _footer(d, kaynak):
    d.line((72, H - 112, W - 72, H - 112), fill=LINE, width=2)
    d.text((72, H - 76), kaynak.upper(), font=mono(20), fill=MUTED, anchor="lm")
    d.text((W - 72, H - 76), HANDLE, font=mono(22, 600), fill=INK, anchor="rm")


LOGO_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logo")


def logo(ticker, size=150):
    """Şirket logosu (nvstly/icons, şeffaf PNG). Önce invest/logo/ önbelleği, yoksa GitHub raw'dan indirir. Yoksa None."""
    t = ticker.replace("$", "").upper()
    os.makedirs(LOGO_DIR, exist_ok=True)
    p = os.path.join(LOGO_DIR, t + ".png")
    if not os.path.exists(p):
        import urllib.request
        try:
            urllib.request.urlretrieve(f"https://raw.githubusercontent.com/nvstly/icons/main/ticker_icons/{t}.png", p)
        except Exception:
            return None
    try:
        im = Image.open(p).convert("RGBA")
    except Exception:
        return None
    bb = im.getbbox()
    if bb:
        im = im.crop(bb)
    k = size / max(im.size)
    return im.resize((max(1, int(im.width * k)), max(1, int(im.height * k))), Image.LANCZOS)


def _accent(ticker, default=ACC):
    """Logonun baskın rengi (çok koyu/çok açık değilse) -> vurgu rengi."""
    im = logo(ticker, 64) if ticker else None
    if im is None:
        return default
    px = [p for p in im.getdata() if p[3] > 200 and 60 < sum(p[:3]) / 3 < 220 and max(p[:3]) - min(p[:3]) > 40]
    if len(px) < 20:
        return default
    r = sum(p[0] for p in px) // len(px); g = sum(p[1] for p in px) // len(px); b = sum(p[2] for p in px) // len(px)
    return (r, g, b)


def _logo_badge(img, ticker, x, y, size=150, anchor="ra"):
    im = logo(ticker, size)
    if im is None:
        return False
    if anchor == "ra":
        x = x - im.width
    img.paste(im, (int(x), int(y)), im)
    return True


def _save(img, out):
    os.makedirs(os.path.dirname(os.path.abspath(out)) or ".", exist_ok=True)
    img.convert("RGB").save(out, quality=92)
    return out


def haber(ticker, kicker, baslik, satirlar, kaynak, out, etiket="HABER"):
    img = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(img)
    _frame(d, kicker.upper(), etiket)
    d.text((72, 190), ticker, font=mono(64, 700), fill=INK)
    if ticker.startswith("$"):
        _logo_badge(img, ticker, W - 72, 150, 210)
    f, lines = _fit_serif(d, baslik, 104, W - 144, 5)
    y = 400
    for ln in lines:
        d.text((72, y), ln, font=f, fill=INK); y += int(f.size * 1.05)
    y += 40
    d.line((72, y, 192, y), fill=ACC, width=4); y += 50
    fb = mono(30)
    for s in satirlar:
        for i, ln in enumerate(_wrap(d, s, fb, W - 190)):
            if i == 0:
                d.text((72, y), "—", font=fb, fill=ACC)
            d.text((120, y), ln, font=fb, fill=(205, 205, 210)); y += 46
        y += 14
    _footer(d, kaynak)
    return _save(img, out)


def rakamlar(ticker, baslik, kutular, yorum, kaynak, out, etiket="BİLANÇO"):
    """kutular: [(etiket, değer, alt_not), ...] en fazla 4."""
    img = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(img)
    _frame(d, ticker, etiket)
    has = _logo_badge(img, ticker, W - 72, 150, 190)
    f, lines = _fit_serif(d, baslik, 96, W - 144 - (220 if has else 0), 3)
    y = 180
    for ln in lines:
        d.text((72, y), ln, font=f, fill=INK); y += int(f.size * 1.05)
    y = max(y, 360 if has else 0) + 50
    cw = (W - 144 - 30) // 2
    for i, (k, v, alt) in enumerate(kutular[:4]):
        x = 72 + (i % 2) * (cw + 30); yy = y + (i // 2) * 250
        d.rectangle((x, yy, x + cw, yy + 220), outline=LINE, width=2)
        d.text((x + 30, yy + 28), k.upper(), font=mono(22, 600), fill=MUTED)
        fs = 88
        while d.textlength(v, font=serif(fs)) > cw - 60 and fs > 48:
            fs -= 4
        d.text((x + 30, yy + 64), v, font=serif(fs), fill=_tone(alt) if alt[:1] in "+-−" else INK)
        d.text((x + 30, yy + 172), alt, font=mono(24), fill=_tone(alt))
    y += 250 * ((len(kutular[:4]) + 1) // 2) + 20
    fi = serif(48, italic=True)
    for ln in _wrap(d, yorum, fi, W - 144)[:3]:
        d.text((72, y), ln, font=fi, fill=ACC); y += 58
    _footer(d, kaynak)
    return _save(img, out)


def liste(baslik, alt_baslik, satirlar, kaynak, out, etiket="ÖZET", not_satiri=""):
    """satirlar: [(sol, sağ), ...] en fazla 9. Sağ '+'/'-' ile başlarsa renklenir."""
    img = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(img)
    _frame(d, alt_baslik.upper(), etiket)
    f, lines = _fit_serif(d, baslik, 100, W - 144, 2)
    y = 175
    for ln in lines:
        d.text((72, y), ln, font=f, fill=INK); y += int(f.size * 1.05)
    y += 40
    rows = satirlar[:9]
    rh = min(100, (H - 220 - y) // max(len(rows), 1))
    for sol, sag in rows:
        d.line((72, y, W - 72, y), fill=LINE, width=1)
        d.text((72, y + rh // 2), sol, font=mono(32, 500), fill=INK, anchor="lm")
        d.text((W - 72, y + rh // 2), sag, font=mono(32, 600), fill=_tone(sag), anchor="rm")
        y += rh
    d.line((72, y, W - 72, y), fill=LINE, width=1)
    if not_satiri:
        fi = serif(42, italic=True)
        yy = y + 40
        for ln in _wrap(d, not_satiri, fi, W - 144)[:2]:
            d.text((72, yy), ln, font=fi, fill=ACC); yy += 52
    _footer(d, kaynak)
    return _save(img, out)


# ---------------- yeni düzenler ----------------

def dev_rakam(ticker, rakam, baslik, aciklama, kaynak, out, etiket="RAKAM", acik_tema=False):
    """Tek dev sayı. Logo ortada üstte, rakam devasa, altında 1-2 satır."""
    bg, ink = ((242, 238, 230), (20, 20, 22)) if acik_tema else (BG, INK)
    img = Image.new("RGB", (W, H), bg); d = ImageDraw.Draw(img)
    acc = _accent(ticker) if ticker else ACC
    d.text((72, 70), etiket, font=mono(24, 600), fill=acc)
    d.text((W - 72, 70), ticker, font=mono(26, 700), fill=ink, anchor="ra")
    lg = logo(ticker, 300) if ticker.startswith("$") else None
    y = 200
    if lg:
        img.paste(lg, ((W - lg.width) // 2, y), lg); y += lg.height + 40
    else:
        y += 60
    fs = 300
    while d.textlength(rakam, font=serif(fs)) > W - 144 and fs > 120:
        fs -= 10
    d.text((W // 2, y), rakam, font=serif(fs), fill=_tone(rakam) if rakam[:1] in "+-−" else acc, anchor="ma")
    y += int(fs * 1.0) + 30
    f, lines = _fit_serif(d, baslik, 76, W - 160, 2, 48)
    for ln in lines:
        d.text((W // 2, y), ln, font=f, fill=ink, anchor="ma"); y += int(f.size * 1.08)
    y += 20
    for ln in _wrap(d, aciklama, mono(28), W - 200)[:4]:
        d.text((W // 2, y), ln, font=mono(28), fill=MUTED, anchor="ma"); y += 42
    d.line((72, H - 112, W - 72, H - 112), fill=LINE if not acik_tema else (200, 196, 188), width=2)
    d.text((72, H - 76), kaynak.upper(), font=mono(20), fill=MUTED, anchor="lm")
    d.text((W - 72, H - 76), HANDLE, font=mono(22, 600), fill=ink, anchor="rm")
    return _save(img, out)


def grafik(ticker, baslik, etiketler, degerler, birim, not_satiri, kaynak, out, etiket="GRAFİK", tur="bar"):
    """Doğrulanmış az sayıda veri noktası (örn. 4-8 çeyrek gelir). tur: 'bar' veya 'cizgi'."""
    img = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(img)
    acc = _accent(ticker) if ticker else ACC
    _frame(d, ticker or etiket, etiket)
    has = _logo_badge(img, ticker, W - 72, 145, 170) if ticker.startswith("$") else False
    f, lines = _fit_serif(d, baslik, 84, W - 144 - (200 if has else 0), 2)
    y = 175
    for ln in lines:
        d.text((72, y), ln, font=f, fill=INK); y += int(f.size * 1.05)
    top, bot = max(y, 330 if has else 0) + 70, H - 300
    left, right = 90, W - 90
    mx = max(degerler) * 1.12; mn = 0 if tur == "bar" else min(degerler) * 0.9
    n = len(degerler); step = (right - left) / n
    pts = []
    for i, (e, v) in enumerate(zip(etiketler, degerler)):
        cx = left + step * i + step / 2
        yy = bot - (v - mn) / (mx - mn) * (bot - top)
        if tur == "bar":
            bw = step * 0.56
            last = i == n - 1
            d.rectangle((cx - bw / 2, yy, cx + bw / 2, bot), fill=acc if last else (70, 70, 78))
        pts.append((cx, yy))
        lab = (f"{v:,.1f}".rstrip("0").rstrip(".") if isinstance(v, float) else f"{v:,}").replace(",", "X").replace(".", ",").replace("X", ".")
        d.text((cx, yy - 14), lab, font=mono(24, 600), fill=INK, anchor="mb")
        d.text((cx, bot + 22), e, font=mono(22), fill=MUTED, anchor="ma")
    if tur != "bar":
        d.line(pts, fill=acc, width=6)
        for p in pts:
            d.ellipse((p[0] - 9, p[1] - 9, p[0] + 9, p[1] + 9), fill=acc)
    d.line((left - 20, bot, right + 20, bot), fill=LINE, width=2)
    d.text((72, bot + 70), birim, font=mono(22), fill=MUTED)
    fi = serif(44, italic=True); yy = bot + 120
    for ln in _wrap(d, not_satiri, fi, W - 144)[:2]:
        d.text((72, yy), ln, font=fi, fill=acc); yy += 54
    _footer(d, kaynak)
    return _save(img, out)


def karsilastir(t1, t2, baslik, satirlar, not_satiri, kaynak, out, etiket="KARŞILAŞTIRMA"):
    """İki şirket yan yana. satirlar: [(metrik, deger1, deger2), ...] en fazla 6."""
    img = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(img)
    _frame(d, f"{t1} vs {t2}", etiket)
    f, lines = _fit_serif(d, baslik, 88, W - 144, 2)
    y = 170
    for ln in lines:
        d.text((72, y), ln, font=f, fill=INK); y += int(f.size * 1.05)
    y += 30
    cx1, cx2 = 600, 880
    for t, cx in ((t1, cx1), (t2, cx2)):
        lg = logo(t, 190)
        if lg:
            img.paste(lg, (int(cx - lg.width / 2), y), lg)
        d.text((cx, y + 210), t, font=mono(28, 700), fill=INK, anchor="ma")
    y += 280
    for m, v1, v2 in satirlar[:6]:
        d.line((72, y, W - 72, y), fill=LINE, width=1)
        d.text((72, y + 45), m, font=mono(26), fill=MUTED, anchor="lm")
        d.text((cx1, y + 45), v1, font=mono(32, 600), fill=_tone(v1), anchor="mm")
        d.text((cx2, y + 45), v2, font=mono(32, 600), fill=_tone(v2), anchor="mm")
        y += 90
    d.line((72, y, W - 72, y), fill=LINE, width=1)
    fi = serif(42, italic=True); y += 40
    for ln in _wrap(d, not_satiri, fi, W - 144)[:2]:
        d.text((72, y), ln, font=fi, fill=ACC); y += 52
    _footer(d, kaynak)
    return _save(img, out)


def alinti(ticker, soz, kim, baglam, kaynak, out, etiket="AÇIKLAMA"):
    """CEO/CFO/Fed sözü. Büyük italik tırnak, logo üstte."""
    img = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(img)
    acc = _accent(ticker) if ticker.startswith("$") else ACC
    _frame(d, baglam.upper(), etiket)
    _logo_badge(img, ticker, W - 72, 150, 200) if ticker.startswith("$") else None
    d.text((60, 160), "“", font=serif(260), fill=acc)
    f, lines = _fit_serif(d, soz, 86, W - 160, 7, 52)
    fi = serif(f.size, italic=True)
    y = 400
    for ln in lines:
        d.text((80, y), ln, font=fi, fill=INK); y += int(f.size * 1.12)
    y += 40
    d.line((80, y, 200, y), fill=acc, width=4)
    d.text((80, y + 30), kim, font=mono(30, 600), fill=INK)
    _footer(d, kaynak)
    return _save(img, out)


# ---------------- temalar ----------------
TEMALAR = {
    "gece":    dict(BG=(12, 12, 14),   INK=(238, 236, 230), MUTED=(128, 128, 136), LINE=(44, 44, 50),    ACC=(212, 175, 105)),
    "lacivert":dict(BG=(10, 22, 44),   INK=(236, 240, 248), MUTED=(140, 156, 186), LINE=(34, 52, 86),    ACC=(110, 180, 255)),
    "zumrut":  dict(BG=(8, 34, 28),    INK=(232, 244, 236), MUTED=(130, 170, 150), LINE=(28, 66, 54),    ACC=(120, 230, 170)),
    "bordo":   dict(BG=(44, 10, 18),   INK=(248, 236, 236), MUTED=(190, 140, 150), LINE=(80, 30, 42),    ACC=(255, 150, 120)),
    "kagit":   dict(BG=(242, 238, 230),INK=(22, 22, 24),    MUTED=(110, 106, 100), LINE=(206, 200, 190), ACC=(190, 60, 40)),
    "grafit":  dict(BG=(30, 30, 34),   INK=(244, 244, 246), MUTED=(150, 150, 160), LINE=(60, 60, 68),    ACC=(255, 210, 60)),
    "mor":     dict(BG=(26, 14, 44),   INK=(242, 236, 252), MUTED=(160, 140, 200), LINE=(58, 40, 90),    ACC=(190, 150, 255)),
}


def tema(ad):
    """Kart temasını değiştir: gece, lacivert, zumrut, bordo, kagit, grafit, mor. Sonraki tüm kartlar bu renklerle çıkar."""
    g = globals()
    for k, v in TEMALAR[ad].items():
        g[k] = v
    return ad


def foto_kart(photo, ticker, kicker, baslik, satirlar, kaynak, out, etiket="HABER", yb=0.3):
    """Üst yarı fotoğraf (SADECE Enes'in gönderdiği foto), alt yarı yazı. Webden indirilmiş foto KULLANMA."""
    img = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(img)
    ph = Image.open(photo).convert("RGB")
    tw, th = W, 860
    k = max(tw / ph.width, th / ph.height); ph = ph.resize((int(ph.width * k) + 1, int(ph.height * k) + 1), Image.LANCZOS)
    top = int((ph.height - th) * yb); left = (ph.width - tw) // 2
    img.paste(ph.crop((left, top, left + tw, top + th)), (0, 0))
    grad = Image.new("L", (1, 240)); [grad.putpixel((0, i), int(255 * i / 239)) for i in range(240)]
    img.paste(Image.new("RGB", (W, 240), BG), (0, 620), grad.resize((W, 240)))
    tw_ = d.textlength(etiket, font=mono(24, 700))
    d.rounded_rectangle((60, 52, 60 + tw_ + 32, 96), radius=22, fill=BG)
    d.text((76, 74), etiket, font=mono(24, 700), fill=ACC, anchor="lm")
    if ticker.startswith("$"):
        _logo_badge(img, ticker, W - 72, 50, 150)
    d.text((72, 850), kicker.upper(), font=mono(24, 600), fill=ACC)
    f, lines = _fit_serif(d, baslik, 92, W - 144, 2)
    y = 892
    for ln in lines:
        d.text((72, y), ln, font=f, fill=INK); y += int(f.size * 1.05)
    y += 18
    for s_ in satirlar[:3]:
        for ln in _wrap(d, s_, mono(28), W - 190)[:2]:
            d.text((72, y), ln, font=mono(28), fill=MUTED); y += 42
        y += 8
    _footer(d, kaynak)
    return _save(img, out)

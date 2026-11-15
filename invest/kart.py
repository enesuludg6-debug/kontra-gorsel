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
HANDLE = "@enes1050392"


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


def _save(img, out):
    os.makedirs(os.path.dirname(os.path.abspath(out)) or ".", exist_ok=True)
    img.convert("RGB").save(out, quality=92)
    return out


def haber(ticker, kicker, baslik, satirlar, kaynak, out, etiket="HABER"):
    img = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(img)
    _frame(d, kicker.upper(), etiket)
    d.text((72, 190), ticker, font=mono(64, 700), fill=INK)
    f, lines = _fit_serif(d, baslik, 104, W - 144, 5)
    y = 320
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
    f, lines = _fit_serif(d, baslik, 96, W - 144, 3)
    y = 180
    for ln in lines:
        d.text((72, y), ln, font=f, fill=INK); y += int(f.size * 1.05)
    y += 50
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

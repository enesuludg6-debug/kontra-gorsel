"""EnesInvestUS kart v2 — daha dikkat çekici, profesyonel düzenler (deneme). 1080x1350.
Fontlar: Inter Display (Black/ExtraBold/Bold/SemiBold/Medium) + Instrument Serif + JetBrains Mono.
"""
import os, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import kart as K

D = K.D
W, H = 1080, 1350
HANDLE = "ENES ULUDAĞ"


# Enes 16.11 10:34: kaba/kalın yazı değil, daha ince ve keskin yazı sever. Eldeki en ince ağırlık Medium.
# Enes 16.11 11:53: ince/keskin yazi zorunlu degil, kaldirildi (normal agirliklar).
INCE = {}


def sans(s, w="Bold"):
    w = INCE.get(w, w)
    return ImageFont.truetype(os.path.join(D, f"InterDisplay-{w}.otf"), s)


def _wrap(d, t, f, mw):
    return K._wrap(d, t, f, mw)


def _fit(d, t, wname, size, mw, maxl, mn=40):
    while size > mn:
        f = sans(size, wname)
        ls = _wrap(d, t, f, mw)
        if len(ls) <= maxl:
            return f, ls
        size -= 4
    f = sans(mn, wname)
    return f, _wrap(d, t, f, mw)[:maxl]


def _brand(ticker, default=(212, 175, 105)):
    return K._accent(ticker, default) if ticker and ticker.startswith("$") else default


def _mix(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def _radial(size, inner, outer, cx=0.5, cy=0.35, r=0.9):
    w, h = size
    g = Image.new("RGB", size, outer)
    px = g.load()
    R = r * max(w, h)
    for y in range(0, h, 2):
        for x in range(0, w, 2):
            t = min(1, math.hypot(x - cx * w, y - cy * h) / R)
            c = _mix(inner, outer, t ** 1.4)
            px[x, y] = c
            if x + 1 < w: px[x + 1, y] = c
            if y + 1 < h:
                px[x, y + 1] = c
                if x + 1 < w: px[x + 1, y + 1] = c
    return g


def _vgrad(size, top, bot):
    w, h = size
    g = Image.new("RGB", size)
    d = ImageDraw.Draw(g)
    for y in range(h):
        d.line((0, y, w, y), fill=_mix(top, bot, y / (h - 1)))
    return g


def _plate_fill(lg, a=245):
    px = [p for p in lg.getdata() if p[3] > 200]
    if px and sum(sum(p[:3]) / 3 for p in px) / len(px) > 200:
        return (22, 22, 26, a)
    return (255, 255, 255, a)


LOGO_BUYUT = 1.8  # Enes 16.11 10:30+10:32: logolar daha da belirgin olsun


def _logo(ticker, size):
    return K.logo(ticker, int(size * LOGO_BUYUT)) if ticker and ticker.startswith("$") else None


def _footer(img, kaynak, ink=(235, 235, 240), muted=(150, 150, 160), line=(60, 60, 70), acc=None):
    d = ImageDraw.Draw(img)
    d.line((72, H - 120, W - 72, H - 120), fill=line, width=2)
    d.text((72, H - 74), ("KAYNAK: " + kaynak).upper(), font=K.mono(19), fill=muted, anchor="lm")
    # imza: monogram + isim
    acc = acc or (212, 175, 105)
    nf = sans(26, "ExtraBold")
    tw = d.textlength(HANDLE, font=nf)
    x1 = W - 72
    d.text((x1, H - 74), HANDLE, font=nf, fill=ink, anchor="rm")
    cx = int(x1 - tw - 34)
    d.ellipse((cx - 22, H - 96, cx + 22, H - 52), fill=acc)
    d.text((cx, H - 74), "E", font=sans(26, "Black"), fill=(10, 10, 12) if sum(acc) > 380 else (255, 255, 255), anchor="mm")


def _grain(img, amt=7):
    import numpy as np
    a = np.asarray(img.convert("RGB")).astype(np.int16)
    n = np.random.default_rng(7).normal(0, amt, a.shape[:2])[..., None]
    return Image.fromarray(np.clip(a + n, 0, 255).astype(np.uint8))


def _watermark(img, ticker, size=900, x=None, y=None, alpha=22):
    lg = _logo(ticker, size)
    if lg is None:
        return
    r, g, b, a = lg.split()
    a = a.point(lambda v: v * alpha // 255)
    lg.putalpha(a)
    img.paste(lg, (W - int(lg.width * 0.62) if x is None else x, H - int(lg.height * 0.75) if y is None else y), lg)


def _shadow_paste(img, tile, xy, r=40, blur=30, op=150):
    sh = Image.new("RGBA", (tile.width + blur * 4, tile.height + blur * 4), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle((blur * 2, blur * 2 + 14, blur * 2 + tile.width, blur * 2 + tile.height + 14), radius=r, fill=(0, 0, 0, op))
    sh = sh.filter(ImageFilter.GaussianBlur(blur))
    img.paste(sh, (xy[0] - blur * 2, xy[1] - blur * 2), sh)
    img.paste(tile, xy, tile)


def _save(img, out, grain=True):
    os.makedirs(os.path.dirname(os.path.abspath(out)) or ".", exist_ok=True)
    img = img.convert("RGB")
    if grain:
        img = _grain(img)
    img.save(out, quality=93)
    return out


# A — SPOTLIGHT: marka renginde ışık hüzmesi, dev logo, dev rakam
def spotlight(ticker, rakam, baslik, alt, kaynak, out, etiket="RAKAM"):
    br = _brand(ticker)
    img = _radial((W, H), _mix(br, (0, 0, 0), 0.55), (6, 6, 8), cy=0.28, r=0.75)
    _watermark(img, ticker, 1000, alpha=14)
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((72, 64, 72 + d.textlength(etiket, font=sans(26, "Bold")) + 40, 112), radius=24, fill=br)
    d.text((92, 88), etiket, font=sans(26, "Bold"), fill=(10, 10, 12), anchor="lm")
    d.text((W - 72, 88), ticker, font=sans(30, "ExtraBold"), fill=(255, 255, 255), anchor="rm")
    lg = _logo(ticker, 330)
    y = 170
    if lg:
        glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        gd = ImageDraw.Draw(glow)
        gd.ellipse((W / 2 - 260, y - 60, W / 2 + 260, y + lg.height + 60), fill=br + (90,))
        glow = glow.filter(ImageFilter.GaussianBlur(70))
        img.paste(glow, (0, 0), glow)
        img.paste(lg, ((W - lg.width) // 2, y), lg)
        y += lg.height + 50
    d = ImageDraw.Draw(img)
    fs = 260
    while d.textlength(rakam, font=sans(fs, "Black")) > W - 120 and fs > 120:
        fs -= 10
    col = K.UP if rakam[:1] == "+" else (K.DOWN if rakam[:1] in "-−" else (255, 255, 255))
    d.text((W // 2, y), rakam, font=sans(fs, "Black"), fill=col, anchor="ma")
    y += int(fs * 0.95) + 30
    f, ls = _fit(d, baslik, "ExtraBold", 64, W - 160, 2)
    for l in ls:
        d.text((W // 2, y), l, font=f, fill=(255, 255, 255), anchor="ma"); y += int(f.size * 1.15)
    y += 16
    for l in _wrap(d, alt, sans(32, "Medium"), W - 200)[:3]:
        d.text((W // 2, y), l, font=sans(32, "Medium"), fill=(190, 190, 200), anchor="ma"); y += 46
    _footer(img, kaynak, acc=br)
    return _save(img, out)


# B — SPLIT: üst yarı marka rengi + logo, alt yarı koyu veri
def split(ticker, baslik, satirlar, kaynak, out, etiket="HABER"):
    br = _brand(ticker)
    img = Image.new("RGB", (W, H), (12, 12, 14))
    top = _vgrad((W, 560), _mix(br, (255, 255, 255), 0.08), _mix(br, (0, 0, 0), 0.35))
    img.paste(top, (0, 0))
    d = ImageDraw.Draw(img)
    d.text((72, 70), etiket, font=sans(28, "Bold"), fill=(255, 255, 255, ))
    d.text((W - 72, 70), ticker, font=sans(30, "ExtraBold"), fill=(255, 255, 255), anchor="ra")
    lg = _logo(ticker, 300)
    if lg:
        plate = Image.new("RGBA", (lg.width + 80, lg.height + 80), (0, 0, 0, 0))
        ImageDraw.Draw(plate).rounded_rectangle((0, 0, plate.width - 1, plate.height - 1), radius=48, fill=_plate_fill(lg, 245))
        plate.paste(lg, (40, 40), lg)
        _shadow_paste(img, plate, ((W - plate.width) // 2, 280 - plate.height // 2), r=48)
    d = ImageDraw.Draw(img)
    y = 610
    f, ls = _fit(d, baslik, "Black", 84, W - 144, 3)
    for l in ls:
        d.text((72, y), l, font=f, fill=(255, 255, 255)); y += int(f.size * 1.08)
    y += 30
    for s in satirlar[:4]:
        d.rounded_rectangle((72, y + 10, 84, y + 40), radius=4, fill=br)
        for i, l in enumerate(_wrap(d, s, sans(34, "Medium"), W - 200)):
            d.text((110, y), l, font=sans(34, "Medium"), fill=(210, 210, 218)); y += 46
        y += 18
    _footer(img, kaynak)
    return _save(img, out)


# C — TERMİNAL: Bloomberg terminal havası, turuncu mono, şerit
def terminal(ticker, baslik, satirlar, kaynak, out, etiket="PİYASA"):
    OR = (255, 152, 0)
    img = Image.new("RGB", (W, H), (0, 0, 0))
    _watermark(img, ticker, 900, alpha=16)
    d = ImageDraw.Draw(img)
    for gy in range(120, H - 120, 60):
        d.line((0, gy, W, gy), fill=(14, 14, 14))
    d.rectangle((0, 0, W, 90), fill=OR)
    d.text((40, 45), f"{ticker}  <EQUITY>  {etiket}", font=K.mono(34, 800), fill=(0, 0, 0), anchor="lm")
    d.text((W - 40, 45), "ENES", font=K.mono(34, 800), fill=(0, 0, 0), anchor="rm")
    lg = _logo(ticker, 200)
    if lg:
        img.paste(lg, (W - 60 - lg.width, 130), lg)
    f, ls = _fit(d, baslik, "Black", 78, W - 120 - (380 if lg else 0), 3)
    y = 140
    for l in ls:
        d.text((40, y), l, font=f, fill=(255, 255, 255)); y += int(f.size * 1.1)
    y = max(y, 360) + 30
    d.line((40, y, W - 40, y), fill=OR, width=3); y += 30
    for k, v in satirlar[:7]:
        d.text((40, y + 34), k.upper(), font=K.mono(32, 500), fill=OR, anchor="lm")
        col = K.UP if v[:1] == "+" else (K.DOWN if v[:1] in "-−" else (255, 255, 255))
        d.text((W - 40, y + 34), v, font=K.mono(44, 800), fill=col, anchor="rm")
        y += 68
        d.line((40, y + 10, W - 40, y + 10), fill=(40, 40, 40), width=1); y += 20
    d.rectangle((0, H - 110, W, H), fill=(18, 18, 18))
    d.text((40, H - 55), kaynak.upper(), font=K.mono(22), fill=(160, 160, 160), anchor="lm")
    d.text((W - 40, H - 55), HANDLE, font=K.mono(26, 800), fill=OR, anchor="rm")
    return _save(img, out)


# D — SON DAKİKA: kırmızı bant, dev başlık, logo
def sondakika(ticker, baslik, alt, kaynak, out, bant="SON DAKİKA"):
    RED = (225, 30, 45)
    img = Image.new("RGB", (W, H), (250, 248, 244))
    _watermark(img, ticker, 1000, alpha=20)
    d = ImageDraw.Draw(img)
    d.rectangle((0, 0, W, 130), fill=RED)
    d.rectangle((0, 130, W, 140), fill=(20, 20, 22))
    d.text((72, 65), bant, font=sans(54, "Black"), fill=(255, 255, 255), anchor="lm")
    d.text((W - 72, 65), ticker, font=sans(40, "ExtraBold"), fill=(255, 255, 255), anchor="rm")
    lg = _logo(ticker, 280)
    y = 200
    if lg:
        img.paste(lg, (72, y), lg); y += lg.height + 60
    f, ls = _fit(d, baslik, "Black", 110, W - 144, 4, 60)
    for l in ls:
        d.text((72, y), l, font=f, fill=(14, 14, 16)); y += int(f.size * 1.05)
    y += 30
    d.rectangle((72, y, 200, y + 10), fill=RED); y += 50
    for l in _wrap(d, alt, sans(38, "Medium"), W - 144)[:4]:
        d.text((72, y), l, font=sans(38, "Medium"), fill=(70, 70, 76)); y += 52
    _footer(img, kaynak, ink=(14, 14, 16), muted=(120, 120, 126), line=(210, 206, 198))
    return _save(img, out)


# E — ÖNCE / SONRA: iki dev rakam, ok
def once_sonra(ticker, baslik, once, sonra, once_lbl, sonra_lbl, degisim, kaynak, out, etiket="KARŞILAŞTIRMA"):
    br = _brand(ticker)
    img = _vgrad((W, H), _mix(br, (0, 0, 0), 0.85), (6, 6, 8))
    _watermark(img, ticker, 1000, alpha=12)
    d = ImageDraw.Draw(img)
    d.text((72, 70), etiket, font=sans(28, "Bold"), fill=br)
    lg = _logo(ticker, 220)
    if lg:
        img.paste(lg, (W - 72 - lg.width, 60), lg)
    f, ls = _fit(d, baslik, "Black", 80, W - 144 - (400 if lg else 0), 3)
    y = 140
    for l in ls:
        d.text((72, y), l, font=f, fill=(255, 255, 255)); y += int(f.size * 1.08)
    y = max(y, 330) + 60
    bw = (W - 144 - 40) // 2
    for i, (v, lbl, c) in enumerate(((once, once_lbl, (60, 60, 68)), (sonra, sonra_lbl, br))):
        x = 72 + i * (bw + 40)
        d.rounded_rectangle((x, y, x + bw, y + 380), radius=36, fill=c)
        d.text((x + bw // 2, y + 70), lbl.upper(), font=sans(30, "Bold"), fill=(255, 255, 255) if i else (180, 180, 190), anchor="ma")
        fs = 150
        while d.textlength(v, font=sans(fs, "Black")) > bw - 50 and fs > 60:
            fs -= 6
        d.text((x + bw // 2, y + 160), v, font=sans(fs, "Black"), fill=(255, 255, 255), anchor="ma")
    # ok rozeti
    cx, cy = W // 2, y + 190
    d.ellipse((cx - 56, cy - 56, cx + 56, cy + 56), fill=(255, 255, 255))
    d.text((cx, cy), "→", font=sans(70, "Black"), fill=(10, 10, 12), anchor="mm")
    y += 440
    col = K.UP if degisim[:1] == "+" else K.DOWN
    d.text((W // 2, y), degisim, font=sans(150, "Black"), fill=col, anchor="ma")
    _footer(img, kaynak)
    return _save(img, out)


# F — DERGİ KAPAĞI: Enes'in fotoğrafı tam ekran, üstte büyük başlık
def kapak(photo, ticker, ust, baslik, alt, kaynak, out):
    ph = Image.open(photo).convert("RGB")
    k = max(W / ph.width, H / ph.height)
    ph = ph.resize((int(ph.width * k) + 1, int(ph.height * k) + 1), Image.LANCZOS)
    ph = ph.crop(((ph.width - W) // 2, 0, (ph.width - W) // 2 + W, H))
    img = ph.copy()
    shade = _vgrad((W, H), (0, 0, 0), (0, 0, 0))
    mask = Image.new("L", (W, H))
    md = ImageDraw.Draw(mask)
    for y in range(H):
        a = 0 if y < H * 0.35 else int(235 * min(1, (y - H * 0.35) / (H * 0.4)))
        md.line((0, y, W, y), fill=a)
    img.paste(shade, (0, 0), mask)
    top = Image.new("L", (W, H)); td = ImageDraw.Draw(top)
    for y in range(220):
        td.line((0, y, W, y), fill=int(160 * (1 - y / 220)))
    img.paste(shade, (0, 0), top)
    d = ImageDraw.Draw(img)
    d.text((72, 70), ust.upper(), font=sans(30, "ExtraBold"), fill=(255, 255, 255))
    lg = _logo(ticker, 160)
    if lg:
        plate = Image.new("RGBA", (lg.width + 40, lg.height + 40), (0, 0, 0, 0))
        ImageDraw.Draw(plate).rounded_rectangle((0, 0, plate.width - 1, plate.height - 1), radius=28, fill=_plate_fill(lg, 240))
        plate.paste(lg, (20, 20), lg)
        _shadow_paste(img, plate, (W - 72 - plate.width, 50), r=30)
    d = ImageDraw.Draw(img)
    f, ls = _fit(d, baslik, "Black", 104, W - 144, 3, 60)
    y = H - 170 - len(ls) * int(f.size * 1.04) - 120
    for l in ls:
        d.text((72, y), l, font=f, fill=(255, 255, 255)); y += int(f.size * 1.04)
    y += 20
    for l in _wrap(d, alt, sans(34, "Medium"), W - 144)[:2]:
        d.text((72, y), l, font=sans(34, "Medium"), fill=(220, 220, 226)); y += 46
    _footer(img, kaynak, line=(90, 90, 96))
    return _save(img, out)


# G — CAM PANEL: renkli gradyan + yarı saydam kartlar
def cam(ticker, baslik, kutular, yorum, kaynak, out, etiket="BİLANÇO"):
    br = _brand(ticker)
    img = _radial((W, H), _mix(br, (255, 255, 255), 0.1), _mix(br, (0, 0, 0), 0.82), cx=0.85, cy=0.1, r=1.1)
    d = ImageDraw.Draw(img, "RGBA")
    d.text((72, 70), etiket, font=sans(28, "Bold"), fill=(255, 255, 255))
    lg = _logo(ticker, 240)
    if lg:
        plate = Image.new("RGBA", (lg.width + 60, lg.height + 60), (0, 0, 0, 0))
        ImageDraw.Draw(plate).rounded_rectangle((0, 0, plate.width - 1, plate.height - 1), radius=40, fill=_plate_fill(lg, 235))
        plate.paste(lg, (30, 30), lg)
        _shadow_paste(img, plate, (W - 72 - plate.width, 60), r=40)
    d = ImageDraw.Draw(img, "RGBA")
    f, ls = _fit(d, baslik, "Black", 84, W - 144 - (460 if lg else 0), 3)
    y = 140
    for l in ls:
        d.text((72, y), l, font=f, fill=(255, 255, 255)); y += int(f.size * 1.06)
    y = max(y, 420) + 30
    cw = (W - 144 - 30) // 2
    for i, (k, v, a) in enumerate(kutular[:4]):
        x = 72 + (i % 2) * (cw + 30); yy = y + (i // 2) * 270
        d.rounded_rectangle((x, yy, x + cw, yy + 240), radius=32, fill=(255, 255, 255, 34), outline=(255, 255, 255, 70), width=2)
        d.text((x + 34, yy + 30), k.upper(), font=sans(24, "Bold"), fill=(230, 230, 236))
        fs = 92
        while d.textlength(v, font=sans(fs, "Black")) > cw - 60 and fs > 44:
            fs -= 4
        d.text((x + 34, yy + 72), v, font=sans(fs, "Black"), fill=(255, 255, 255))
        d.text((x + 34, yy + 186), a, font=sans(26, "Medium"), fill=K._tone(a) if a[:1] in "+-" else (210, 210, 220))
    y += 270 * ((len(kutular[:4]) + 1) // 2) + 10
    for l in _wrap(d, yorum, serif := K.serif(50, italic=True), W - 144)[:2]:
        d.text((72, y), l, font=serif, fill=(255, 255, 255)); y += 58
    _footer(img, kaynak, line=(255, 255, 255))
    return _save(img, out)


# H — POSTER: tipografik, tek kelime/rakam ekranı doldurur
def poster(ticker, buyuk, ust, alt, kaynak, out, renk=None):
    br = renk or _brand(ticker)
    img = Image.new("RGB", (W, H), br)
    d = ImageDraw.Draw(img)
    ink = (10, 10, 12) if sum(br) > 420 else (255, 255, 255)
    d.text((72, 70), ust.upper(), font=sans(34, "ExtraBold"), fill=ink)
    lg = _logo(ticker, 200)
    if lg:
        plate = Image.new("RGBA", (lg.width + 40, lg.height + 40), (0, 0, 0, 0))
        ImageDraw.Draw(plate).rounded_rectangle((0, 0, plate.width - 1, plate.height - 1), radius=30, fill=_plate_fill(lg, 250))
        plate.paste(lg, (20, 20), lg)
        _shadow_paste(img, plate, (W - 72 - plate.width, 50), r=30)
    d = ImageDraw.Draw(img)
    fs = 520
    while d.textlength(buyuk, font=sans(fs, "Black")) > W - 100 and fs > 140:
        fs -= 10
    d.text((W // 2, H // 2 - 40), buyuk, font=sans(fs, "Black"), fill=ink, anchor="mm")
    y = H // 2 + fs // 2 + 10
    for l in _wrap(d, alt, sans(46, "Bold"), W - 144)[:3]:
        d.text((W // 2, y), l, font=sans(46, "Bold"), fill=ink, anchor="ma"); y += 60
    _footer(img, kaynak, ink=ink, muted=ink, line=ink)
    return _save(img, out)


# I — SIRALAMA: yatay çubuklar, her satırda logo (çoklu hisse karşılaştırma)
def siralama(baslik, alt, satirlar, birim, kaynak, out, vurgu=(), etiket="SIRALAMA", renk=(110, 180, 255)):
    """satirlar: [(ticker, deger_float, etiket_str), ...] büyükten küçüğe verilir. vurgu: portföy ticker'ları."""
    img = _vgrad((W, H), (14, 16, 24), (6, 6, 8))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((72, 64, 72 + d.textlength(etiket, font=sans(24, "Bold")) + 36, 108), radius=22, fill=renk)
    d.text((90, 86), etiket, font=sans(24, "Bold"), fill=(10, 10, 12), anchor="lm")
    f, ls = _fit(d, baslik, "Black", 76, W - 144, 2)
    y = 140
    for l in ls:
        d.text((72, y), l, font=f, fill=(255, 255, 255)); y += int(f.size * 1.06)
    d.text((72, y + 6), alt, font=sans(30, "Medium"), fill=(160, 166, 180)); y += 70
    rows = satirlar[:10]
    rh = min(150, (H - 160 - y) // max(1, len(rows)))
    # 17.11 21:55: negatif degerler desteklenir (sifir ekseni), logo genisligi metni itmez (logo 1.8 kucultulmez)
    lgs = {t: _logo(t, rh - 22) for t, _, _ in rows}
    lw = max([lg.width for lg in lgs.values() if lg] + [56])
    tx = 72 + lw + 14
    tw = max(d.textlength(t.replace("$", ""), font=sans(30, "ExtraBold")) for t, _, _ in rows)
    x0, x1 = int(tx + tw + 24), W - 72 - 170
    pmx = max([v for _, v, _ in rows if v > 0] + [0]); nmx = max([-v for _, v, _ in rows if v < 0] + [0])
    tot = (pmx + nmx) or 1; xz = x0 + int((x1 - x0) * nmx / tot)
    if nmx:
        d.line((xz, y - 6, xz, y + rh * len(rows)), fill=(90, 94, 110), width=2)
    for t, v, lab in rows:
        cy = y + rh // 2
        lg = lgs[t]
        if lg:
            _px=[px for px in lg.getdata() if px[3]>128]
            if _px and sum(0.299*r+0.587*g+0.114*b for r,g,b,_ in _px)/len(_px) < 70:  # koyu logo -> beyaz plaka (17.11 kurali)
                _x0=72 + (lw - lg.width) // 2; _y0=cy - lg.height // 2
                ImageDraw.Draw(img).rounded_rectangle((_x0-10,_y0-10,_x0+lg.width+10,_y0+lg.height+10), radius=14, fill=(245,245,245))
            img.paste(lg, (72 + (lw - lg.width) // 2, cy - lg.height // 2), lg)
        hl = t in vurgu
        d.text((tx, cy), t.replace("$", ""), font=sans(30, "ExtraBold"), fill=(255, 255, 255) if hl else (200, 204, 214), anchor="lm")
        bw = int((x1 - x0) * abs(v) / tot)
        col = (255, 196, 60) if hl else (renk if v >= 0 else (214, 72, 80))
        if v >= 0:
            bh = min(rh - 34, 60) // 2
            d.rounded_rectangle((xz, cy - bh, xz + max(bw, 12), cy + bh), radius=10, fill=col)
            d.text((xz + max(bw, 12) + 16, cy), lab, font=sans(32, "Black"), fill=(255, 255, 255), anchor="lm")
        else:
            bh = min(rh - 34, 60) // 2
            d.rounded_rectangle((xz - max(bw, 12), cy - bh, xz, cy + bh), radius=10, fill=col)
            d.text((xz + 16, cy), lab, font=sans(32, "Black"), fill=(255, 255, 255), anchor="lm")
        y += rh
    d.text((72, y + 14), birim, font=K.mono(20), fill=(130, 136, 150))
    if vurgu:
        d.rounded_rectangle((72, y + 48, 96, y + 72), radius=6, fill=(255, 196, 60))
        d.text((108, y + 60), "takip listem", font=sans(22, "Medium"), fill=(200, 200, 210), anchor="lm")
    _footer(img, kaynak, acc=renk)
    return _save(img, out)


# J — GÜÇLÜ GRAFİK: kalın sütunlar, marka renginde gradyan, son değer etiketi
def grafik2(ticker, baslik, etiketler, degerler, birim, not_satiri, kaynak, out, etiket="GRAFİK"):
    br = _brand(ticker, (110, 180, 255))
    img = _vgrad((W, H), _mix(br, (0, 0, 0), 0.86), (6, 6, 8))
    _watermark(img, ticker, 1000, alpha=10)
    d = ImageDraw.Draw(img)
    d.text((72, 70), etiket, font=sans(28, "Bold"), fill=br)
    lg = _logo(ticker, 200)
    if lg:
        img.paste(lg, (W - 72 - lg.width, 60), lg)
    f, ls = _fit(d, baslik, "Black", 78, W - 144 - (380 if lg else 0), 3)
    y = 130
    for l in ls:
        d.text((72, y), l, font=f, fill=(255, 255, 255)); y += int(f.size * 1.06)
    top, bot = max(y, 290) + 90, H - 290
    n = len(degerler); left, right = 80, W - 80; step = (right - left) / n
    mx = max(degerler) * 1.1
    for gy in range(4):
        yy = bot - (bot - top) * gy / 3
        d.line((left - 10, yy, right + 10, yy), fill=(40, 40, 48), width=1)
    for i, (e, v) in enumerate(zip(etiketler, degerler)):
        cx = left + step * i + step / 2; bw = step * (0.62 if n <= 10 else 0.74)
        yy = bot - v / mx * (bot - top)
        last = i == n - 1
        bar = _vgrad((int(bw), max(2, int(bot - yy))), _mix(br, (255, 255, 255), 0.25) if last else (92, 92, 104), br if last else (56, 56, 66))
        m = Image.new("L", bar.size, 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, bar.width - 1, bar.height + 20), radius=12, fill=255)
        img.paste(bar, (int(cx - bw / 2), int(yy)), m)
        lab = (f"{v:,.1f}".rstrip("0").rstrip(".") if isinstance(v, float) else f"{v:,}").replace(",", "X").replace(".", ",").replace("X", ".")
        if n <= 12 or i % 2 == 0 or last:
            d.text((cx, yy - 12), lab, font=sans(30 if n <= 10 else 20, "Black"), fill=(255, 255, 255), anchor="mb")
        if n <= 12 or i % 3 == 0 or last:
            d.text((cx, bot + 20), e, font=sans(24 if n <= 10 else 18, "SemiBold"), fill=(170, 170, 182), anchor="ma")
    d.text((72, bot + 80), birim, font=K.mono(22), fill=(130, 130, 140))
    for l in _wrap(d, not_satiri, sans(40, "ExtraBold"), W - 144)[:2]:
        d.text((72, bot + 120), l, font=sans(40, "ExtraBold"), fill=br); bot += 50
    _footer(img, kaynak, acc=br)
    return _save(img, out)


# ================= v3: daha profesyonel düzenler =================
import numpy as np

T_BG = (9, 9, 11)
T_TILE = (22, 22, 27)


def _on(c):
    return (10, 10, 12) if (c[0] * 299 + c[1] * 587 + c[2] * 114) / 1000 > 150 else (255, 255, 255)


def _lin(w, h, c1, c2, diag=True):
    yy, xx = np.mgrid[0:h, 0:w]
    t = ((xx / max(w, 1) + yy / max(h, 1)) / 2 if diag else yy / max(h, 1))[..., None]
    return Image.fromarray((np.array(c1) * (1 - t) + np.array(c2) * t).astype(np.uint8))


def _tile(img, box, fill, r=36, fill2=None, diag=True):
    x0, y0, x1, y1 = map(int, box); w, h = x1 - x0, y1 - y0
    t = _lin(w, h, fill, fill2, diag) if fill2 else Image.new("RGB", (w, h), fill)
    m = Image.new("L", (w, h), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, w - 1, h - 1), radius=r, fill=255)
    img.paste(t, (x0, y0), m)


def _plate(lg, pad=30, r=36):
    p = Image.new("RGBA", (lg.width + pad * 2, lg.height + pad * 2), (0, 0, 0, 0))
    ImageDraw.Draw(p).rounded_rectangle((0, 0, p.width - 1, p.height - 1), radius=r, fill=_plate_fill(lg, 250))
    p.paste(lg, (pad, pad), lg)
    return p


def _pill(d, xy, text, fill, size=24):
    f = sans(size, "Bold"); w = d.textlength(text, font=f)
    d.rounded_rectangle((xy[0], xy[1], xy[0] + w + 36, xy[1] + size + 20), radius=(size + 20) // 2, fill=fill)
    d.text((xy[0] + 18, xy[1] + (size + 20) // 2), text, font=f, fill=_on(fill), anchor="lm")


def _fitnum(d, t, mw, start, w="Black", mn=40):
    fs = start
    while d.textlength(t, font=sans(fs, w)) > mw and fs > mn:
        fs -= 4
    return sans(fs, w)


# K — BENTO: Apple tarzı modüler kutular
def bento(ticker, etiket, baslik, buyuk, buyuk_lbl, kutular, seri, seri_lbl, kaynak, out):
    """kutular: [(etiket, değer, alt)] x3. seri: mini sütun grafik için sayılar (son vurgulu)."""
    br = _brand(ticker, (110, 180, 255)); img = Image.new("RGB", (W, H), T_BG); M, G = 48, 20
    _tile(img, (M, M, M + 640, 400), T_TILE)
    _tile(img, (M + 640 + G, M, W - M, 400), _mix(br, (255, 255, 255), 0.1), fill2=_mix(br, (0, 0, 0), 0.45))
    d = ImageDraw.Draw(img)
    _pill(d, (M + 36, M + 36), etiket, br)
    f, ls = _fit(d, baslik, "Black", 66, 640 - 72, 4); y = M + 112
    for l in ls:
        d.text((M + 36, y), l, font=f, fill=(255, 255, 255)); y += int(f.size * 1.08)
    lg = _logo(ticker, 200)
    if lg:
        p = _plate(lg, 28, 40); cx = (M + 640 + G + W - M) // 2
        _shadow_paste(img, p, (cx - p.width // 2, (M + 400) // 2 - p.height // 2), r=40)
    # büyük rakam
    _tile(img, (M, 420, M + 560, 840), _mix(br, (255, 255, 255), 0.06), fill2=_mix(br, (0, 0, 0), 0.5))
    d = ImageDraw.Draw(img); on = _on(_mix(br, (0, 0, 0), 0.25))
    d.text((M + 40, 462), buyuk_lbl.upper(), font=sans(28, "Bold"), fill=on)
    fb = _fitnum(d, buyuk, 480, 200)
    d.text((M + 36, 790), buyuk, font=fb, fill=on, anchor="ls")
    # mini grafik
    x0, x1 = M + 560 + G, W - M
    _tile(img, (x0, 420, x1, 840), T_TILE); d = ImageDraw.Draw(img)
    d.text((x0 + 32, 456), seri_lbl.upper(), font=sans(22, "Bold"), fill=(150, 150, 162))
    n = len(seri); bx0, bx1, by0, by1 = x0 + 36, x1 - 36, 540, 800; st = (bx1 - bx0) / n; mx = max(seri)
    for i, v in enumerate(seri):
        hh = (by1 - by0) * v / mx; cx = bx0 + st * i + st / 2; last = i == n - 1
        _tile(img, (cx - st * 0.34, by1 - hh, cx + st * 0.34, by1), br if last else (70, 70, 80), r=10)
        ImageDraw.Draw(img).text((cx, by1 - hh - 10), str(v).replace(".", ","), font=sans(24, "Black"), fill=(255, 255, 255) if last else (170, 170, 180), anchor="mb")
    # 3 kutu
    cw = (W - 2 * M - 2 * G) / 3
    for i, (k, v, a) in enumerate(kutular[:3]):
        x = M + i * (cw + G)
        _tile(img, (x, 860, x + cw, 1180), T_TILE); d = ImageDraw.Draw(img)
        d.text((x + 28, 892), k.upper(), font=sans(21, "Bold"), fill=(150, 150, 162))
        d.text((x + 28, 1040), v, font=_fitnum(d, v, cw - 56, 84), fill=(255, 255, 255), anchor="ls")
        for j, l in enumerate(_wrap(d, a, sans(24, "Medium"), cw - 56)[:2]):
            d.text((x + 28, 1070 + j * 32), l, font=sans(24, "Medium"), fill=K._tone(a) if a[:1] in "+-" else (170, 170, 182))
    _footer(img, kaynak, acc=br, line=T_BG)
    return _save(img, out)


# L — HALKA: yüzde halkası
def halka(ticker, yuzde, baslik, orta_alt, yan, kaynak, out, etiket="VERİ", renk=None):
    br = renk or _brand(ticker, (88, 200, 140))
    img = _radial((W, H), _mix(br, (0, 0, 0), 0.78), (7, 7, 9), cy=0.5, r=0.7)
    d = ImageDraw.Draw(img)
    _pill(d, (72, 64), etiket, br)
    f, ls = _fit(d, baslik, "Black", 72, W - 144, 2); y = 140
    for l in ls:
        d.text((72, y), l, font=f, fill=(255, 255, 255)); y += int(f.size * 1.06)
    S = 3; R, wd = 290, 64; cx, cy = W // 2, 640
    ring = Image.new("RGBA", (W * S, H * S), (0, 0, 0, 0)); rd = ImageDraw.Draw(ring)
    bb = ((cx - R) * S, (cy - R) * S, (cx + R) * S, (cy + R) * S)
    rd.arc(bb, 0, 360, fill=(48, 48, 56, 255), width=wd * S)
    end = -90 + 360 * yuzde / 100
    rd.arc(bb, -90, end, fill=br + (255,), width=wd * S)
    for ang in (-90, end):
        px = cx + (R - wd / 2) * math.cos(math.radians(ang)); py = cy + (R - wd / 2) * math.sin(math.radians(ang))
        rd.ellipse(((px - wd / 2) * S, (py - wd / 2) * S, (px + wd / 2) * S, (py + wd / 2) * S), fill=br + (255,))
    ring = ring.resize((W, H), Image.LANCZOS)
    glow = ring.filter(ImageFilter.GaussianBlur(28)); img.paste(glow, (0, 0), glow.split()[3].point(lambda v: v // 3))
    img.paste(ring, (0, 0), ring); d = ImageDraw.Draw(img)
    d.text((cx, cy - 10), f"%{yuzde:g}".replace(".", ","), font=sans(170, "Black"), fill=(255, 255, 255), anchor="mm")
    d.text((cx, cy + 100), orta_alt, font=sans(30, "SemiBold"), fill=(190, 190, 200), anchor="mm")
    y = 1000; cw = (W - 144) / len(yan)
    for i, (k, v) in enumerate(yan):
        x = 72 + i * cw
        if i: d.line((x, y, x, y + 150), fill=(60, 60, 70), width=2)
        d.text((x + cw / 2, y + 10), v, font=_fitnum(d, v, cw - 40, 76), fill=(255, 255, 255), anchor="ma")
        for j, l in enumerate(_wrap(d, k, sans(24, "Medium"), cw - 40)[:2]):
            d.text((x + cw / 2, y + 104 + j * 30), l, font=sans(24, "Medium"), fill=(165, 165, 178), anchor="ma")
    _footer(img, kaynak, acc=br)
    return _save(img, out)


# M — ISI HARİTASI: yeşil/kırmızı kutular (kapanış, haftanın hareketleri)
def isi(baslik, alt, kutular, kaynak, out, etiket="PİYASA", kolon=3, hane=1):
    """kutular: [(ticker, yüzde_float)]"""
    img = Image.new("RGB", (W, H), T_BG); d = ImageDraw.Draw(img)
    _pill(d, (56, 56), etiket, (255, 255, 255))
    f, ls = _fit(d, baslik, "Black", 76, W - 112, 2); y = 126
    for l in ls:
        d.text((56, y), l, font=f, fill=(255, 255, 255)); y += int(f.size * 1.06)
    d.text((56, y + 14), alt, font=sans(30, "Medium"), fill=(160, 160, 172)); y += 80
    n = len(kutular); rows = math.ceil(n / kolon); G = 14
    cw = (W - 112 - G * (kolon - 1)) / kolon; ch = (H - 150 - y - G * (rows - 1)) / rows
    mx = max(abs(v) for _, v in kutular) or 1
    for i, (t, v) in enumerate(kutular):
        x = 56 + (i % kolon) * (cw + G); yy = y + (i // kolon) * (ch + G); k = 0.35 + 0.65 * abs(v) / mx
        c = _mix((20, 44, 34), (24, 168, 96), k) if v >= 0 else _mix((52, 22, 26), (214, 48, 58), k)
        _tile(img, (x, yy, x + cw, yy + ch), _mix(c, (255, 255, 255), 0.08), r=26, fill2=_mix(c, (0, 0, 0), 0.25))
        lg = _logo(t, int(min(cw, ch) * 0.34)); ph = 0
        if lg:
            p = _plate(lg, 12, 18); img.paste(p, (int(x + 20), int(yy + 20)), p); ph = p.height; pw = p.width
        d = ImageDraw.Draw(img)
        # 17.11 21:55: logo 1.8 kucultulmez; ticker yazisi logoya carpiyorsa yazilmaz (logo zaten tanitir), rakam kalan yuksekligi asmaz
        nf = sans(34, "ExtraBold"); tw_ = d.textlength(t.replace("$", ""), font=nf)
        if not lg or (x + 20 + pw + 12) < (x + cw - 22 - tw_):
            d.text((x + cw - 22, yy + 26), t.replace("$", ""), font=nf, fill=(255, 255, 255), anchor="ra")
        s = ("+" if v > 0 else "−" if v < 0 else "") + f"%{abs(v):.{hane}f}".replace(".", ",")
        boy = int(min(76, max(30, ch - (20 + ph) - 40))) if lg else 76
        d.text((x + 22, yy + ch - 22), s, font=_fitnum(d, s, cw - 44, boy), fill=(255, 255, 255), anchor="ls")
    _footer(img, kaynak, acc=(255, 255, 255), line=T_BG)
    return _save(img, out)


# N — TAKVİM: haftalık program, logolu
def takvim(baslik, alt, gunler, kaynak, out, etiket="TAKVİM", renk=(110, 180, 255)):
    """gunler: [(gün, tarih, [(ticker_veya_metin, not)])]"""
    img = _lin(W, H, (14, 18, 30), (7, 7, 9), diag=False); d = ImageDraw.Draw(img)
    _pill(d, (56, 56), etiket, renk)
    f, ls = _fit(d, baslik, "Black", 76, W - 112, 2); y = 126
    for l in ls:
        d.text((56, y), l, font=f, fill=(255, 255, 255)); y += int(f.size * 1.06)
    d.text((56, y + 4), alt, font=sans(30, "Medium"), fill=(160, 166, 180)); y += 76
    rh = (H - 150 - y) / len(gunler)
    for gun, tarih, olaylar in gunler:
        _tile(img, (56, y, W - 56, y + rh - 14), T_TILE, r=28); d = ImageDraw.Draw(img)
        cy = y + (rh - 14) / 2
        d.text((84, cy - 16), gun, font=sans(40, "Black"), fill=(255, 255, 255), anchor="lm")
        d.text((84, cy + 26), tarih, font=sans(22, "Medium"), fill=(150, 150, 162), anchor="lm")
        x = 300
        if not olaylar:
            d.text((x, cy), "—", font=sans(30, "Medium"), fill=(90, 90, 100), anchor="lm")
        for t, nt in olaylar:
            lg = _logo(t, int(rh * 0.42)) if t.startswith("$") else None
            name = t.replace("$", ""); nf = sans(30, "ExtraBold"); sf = sans(20, "Medium")
            tw = max(d.textlength(name, font=nf), d.textlength(nt, font=sf))
            bw = (lg.width + 16 if lg else 0) + tw + 44
            th = max(rh * 0.3, (lg.height / 2 + 12) if lg else 0)  # 17.11: yuksek logo (TGT) kutudan tasmasin, logo kucultulmez
            _tile(img, (x, cy - th, x + bw, cy + th), (38, 38, 46) if lg else _mix(renk, (0, 0, 0), 0.55), r=20); d = ImageDraw.Draw(img)
            tx = x + 22
            if lg:
                img.paste(lg, (int(tx), int(cy - lg.height / 2)), lg); tx += lg.width + 16; d = ImageDraw.Draw(img)
            d.text((tx, cy - 14), name, font=nf, fill=(255, 255, 255), anchor="lm")
            d.text((tx, cy + 20), nt, font=sf, fill=(175, 175, 188), anchor="lm")
            x += bw + 14
        y += rh
    _footer(img, kaynak, acc=renk, line=(7, 7, 9))
    return _save(img, out)


# O — ÇİZGİ: parlayan alan grafik + dev değer
def cizgi(ticker, etiket, baslik, etiketler, degerler, buyuk, buyuk_lbl, kaynak, out, renk=None):
    br = renk or _brand(ticker, (110, 180, 255))
    img = _lin(W, H, _mix(br, (0, 0, 0), 0.88), (6, 6, 8), diag=False)
    _watermark(img, ticker, 1000, alpha=10); d = ImageDraw.Draw(img)
    _pill(d, (72, 64), etiket, br)
    lg = _logo(ticker, 170)
    if lg: lg = _plate(lg, 22, 28)  # logo her zaman beyaz plakada, belirgin olsun
    if lg: img.paste(lg, (W - 72 - lg.width, 56), lg)
    f, ls = _fit(d, baslik, "Black", 68, W - 144 - (420 if lg else 0), 2); y = 136
    for l in ls:
        d.text((72, y), l, font=f, fill=(255, 255, 255)); y += int(f.size * 1.06)
    y = max(y, 250) + 20
    d.text((72, y), buyuk, font=sans(170, "Black"), fill=br); y += 180
    d.text((76, y), buyuk_lbl, font=sans(30, "SemiBold"), fill=(185, 185, 198))
    top, bot, left, right = y + 110, H - 230, 90, W - 110
    n = len(degerler); mn, mx = min(degerler), max(degerler); span = (mx - mn) or 1
    pts = [(left + (right - left) * i / (n - 1), bot - (bot - top) * (v - mn * 0.6) / (mx - mn * 0.6)) for i, v in enumerate(degerler)]
    for g in range(4):
        gy = top + (bot - top) * g / 3; d.line((left - 20, gy, right + 20, gy), fill=(36, 36, 44), width=1)
    area = Image.new("L", (W, H), 0); ImageDraw.Draw(area).polygon(pts + [(right, bot), (left, bot)], fill=255)
    fade = Image.fromarray((np.clip(1 - (np.mgrid[0:H, 0:W][0] - top) / (bot - top), 0, 1) * 120).astype(np.uint8))
    img.paste(Image.new("RGB", (W, H), br), (0, 0), Image.fromarray((np.asarray(area) / 255 * np.asarray(fade)).astype(np.uint8)))
    gl = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(gl).line(pts, fill=br + (255,), width=18, joint="curve")
    gl = gl.filter(ImageFilter.GaussianBlur(16)); img.paste(gl, (0, 0), gl)
    d = ImageDraw.Draw(img); d.line(pts, fill=_mix(br, (255, 255, 255), 0.35), width=7, joint="curve")
    for i, ((px, py), e, v) in enumerate(zip(pts, etiketler, degerler)):
        last = i == n - 1; r = 15 if last else 8
        if last:
            d.ellipse((px - 34, py - 34, px + 34, py + 34), outline=br, width=3)
        d.ellipse((px - r, py - r, px + r, py + r), fill=(255, 255, 255))
        d.text((px, bot + 24), e, font=sans(24, "SemiBold"), fill=(165, 165, 178), anchor="ma")
        d.text((px, py - 30 - (16 if last else 0)), str(v).replace(".", ","), font=sans(30 if last else 24, "Black"), fill=(255, 255, 255) if last else (190, 190, 200), anchor="mb")
    _footer(img, kaynak, acc=br)
    return _save(img, out)


# P — VERSUS: çapraz bölünmüş iki taraf
def versus(sol, sag, baslik, satirlar, kaynak, out, renk1=(40, 110, 255), renk2=(255, 120, 40), etiket="KARŞILAŞTIRMA"):
    """sol/sag: '$TICKER' ya da düz isim. satirlar: [(metrik, sol_değer, sağ_değer)]"""
    c1 = _brand(sol, renk1) if sol.startswith("$") else renk1; c2 = _brand(sag, renk2) if sag.startswith("$") else renk2
    img = Image.new("RGB", (W, H), T_BG); TOP = 600
    left = _lin(W, TOP, _mix(c1, (255, 255, 255), 0.1), _mix(c1, (0, 0, 0), 0.45)); right = _lin(W, TOP, _mix(c2, (255, 255, 255), 0.1), _mix(c2, (0, 0, 0), 0.45))
    m = Image.new("L", (W, TOP), 0); ImageDraw.Draw(m).polygon([(W * 0.58, 0), (W, 0), (W, TOP), (W * 0.42, TOP)], fill=255)
    img.paste(left, (0, 0)); img.paste(right, (0, 0), m); d = ImageDraw.Draw(img)
    d.text((56, 60), etiket, font=sans(26, "Bold"), fill=(255, 255, 255))
    for name, cx, c in ((sol, W * 0.25, c1), (sag, W * 0.75, c2)):
        lg = _logo(name, 220) if name.startswith("$") else None
        if lg:
            p = _plate(lg, 30, 40); _shadow_paste(img, p, (int(cx - p.width / 2), 170), r=40); d = ImageDraw.Draw(img)
            d.text((cx, 170 + p.height + 30), name, font=sans(40, "Black"), fill=(255, 255, 255), anchor="ma")
        else:
            ff, ll = _fit(d, name, "Black", 76, W * 0.4, 2); yy = 300 - len(ll) * ff.size * 0.55
            for l in ll:
                d.text((cx, yy), l, font=ff, fill=(255, 255, 255), anchor="ma"); yy += ff.size * 1.05
    d.ellipse((W / 2 - 62, TOP / 2 - 62, W / 2 + 62, TOP / 2 + 62), fill=(255, 255, 255))
    d.text((W / 2, TOP / 2), "VS", font=sans(52, "Black"), fill=(10, 10, 12), anchor="mm")
    f, ls = _fit(d, baslik, "Black", 60, W - 112, 2); y = TOP + 44
    for l in ls:
        d.text((W / 2, y), l, font=f, fill=(255, 255, 255), anchor="ma"); y += int(f.size * 1.08)
    y += 26; rh = min(170, (H - 150 - y) / max(1, len(satirlar)))
    for mt, a, b in satirlar:
        _tile(img, (56, y, W - 56, y + rh - 12), T_TILE, r=22); d = ImageDraw.Draw(img); cy = y + (rh - 12) / 2
        d.text((W / 2, cy), mt.upper(), font=sans(22, "Bold"), fill=(150, 150, 162), anchor="mm")
        d.text((92, cy), a, font=sans(60, "Black"), fill=_mix(c1, (255, 255, 255), 0.45), anchor="lm")
        d.text((W - 92, cy), b, font=sans(60, "Black"), fill=_mix(c2, (255, 255, 255), 0.45), anchor="rm")
        y += rh
    _footer(img, kaynak, acc=(255, 255, 255), line=T_BG)
    return _save(img, out)


# R — ÜÇ RAKAM: alt alta üç dev istatistik
def uclu(ticker, etiket, baslik, satirlar, kaynak, out):
    """satirlar: [(rakam, açıklama)] x3"""
    br = _brand(ticker, (212, 175, 105))
    img = _lin(W, H, (16, 16, 20), (6, 6, 8), diag=False); _watermark(img, ticker, 1100, alpha=12); d = ImageDraw.Draw(img)
    _pill(d, (72, 64), etiket, br)
    lg = _logo(ticker, 190)
    if lg: img.paste(lg, (W - 72 - lg.width, 56), lg)
    f, ls = _fit(d, baslik, "Black", 70, W - 144 - (370 if lg else 0), 3); y = 136
    for l in ls:
        d.text((72, y), l, font=f, fill=(255, 255, 255)); y += int(f.size * 1.06)
    y = max(y, 410 if lg else 300) + 20; rh = (H - 150 - y) / 3
    for i, (r, a) in enumerate(satirlar[:3]):
        d.line((72, y, W - 72, y), fill=(52, 52, 60), width=2)
        col = K.UP if r[:1] == "+" else (K.DOWN if r[:1] in "-−" else (br if i == 0 else (255, 255, 255)))
        fn = _fitnum(d, r, 520, 150); d.text((72, y + rh / 2), r, font=fn, fill=col, anchor="lm")
        ll = _wrap(d, a, sans(34, "SemiBold"), W - 72 - 640)[:3]; ty = y + rh / 2 - len(ll) * 22
        for l in ll:
            d.text((640, ty), l, font=sans(34, "SemiBold"), fill=(205, 205, 215)); ty += 44
        y += rh
    _footer(img, kaynak, acc=br)
    return _save(img, out)


# S — ALINTI: dev tırnak, serif söz, imza
def soz(ticker, alinti_metni, kim, unvan, kaynak, out, photo=None, etiket="SÖZ"):
    br = _brand(ticker, (212, 175, 105))
    img = _radial((W, H), _mix(br, (0, 0, 0), 0.7), (7, 7, 9), cx=0.15, cy=0.1, r=0.9); d = ImageDraw.Draw(img)
    _pill(d, (72, 64), etiket, br)
    d.text((56, 90), "“", font=K.serif(520), fill=_mix(br, (255, 255, 255), 0.15))
    f = None
    for fs in range(104, 50, -4):
        f = K.serif(fs, italic=True); ls = _wrap(d, alinti_metni, f, W - 150)
        if len(ls) <= 6: break
    y = 430
    for l in ls:
        d.text((76, y), l, font=f, fill=(255, 255, 255)); y += int(f.size * 1.14)
    y = max(y + 50, 980); d.rectangle((76, y, 196, y + 8), fill=br); y += 50
    x = 76
    if photo:
        ph = Image.open(photo).convert("RGB"); s = min(ph.size); ph = ph.crop(((ph.width - s) // 2, 0, (ph.width - s) // 2 + s, s)).resize((150, 150), Image.LANCZOS)
        m = Image.new("L", (150, 150), 0); ImageDraw.Draw(m).ellipse((0, 0, 149, 149), fill=255); img.paste(ph, (x, y), m); x += 180
    else:
        lg = _logo(ticker, 110)
        if lg:
            p = _plate(lg, 18, 26); img.paste(p, (x, y), p); x += p.width + 30
    d = ImageDraw.Draw(img)
    d.text((x, y + 44), kim, font=sans(44, "Black"), fill=(255, 255, 255), anchor="lm")
    d.text((x, y + 100), unvan, font=sans(28, "Medium"), fill=(180, 180, 192), anchor="lm")
    _footer(img, kaynak, acc=br)
    return _save(img, out)


# T — EDİTORYAL: FT/dergi havası, açık zemin, serif manşet
def editoryal(ticker, kicker, baslik, spot, rakamlar3, kaynak, out, tarih="", zemin=(255, 241, 229)):
    """rakamlar3: [(rakam, açıklama)] x3"""
    INK, CL, TL = (26, 24, 22), (153, 15, 61), (13, 118, 128)
    img = Image.new("RGB", (W, H), zemin); d = ImageDraw.Draw(img)
    d.rectangle((72, 60, W - 72, 68), fill=INK)
    d.text((72, 104), "P İ Y A S A   N O T U", font=sans(28, "Black"), fill=INK, anchor="lm")
    d.text((W - 72, 104), tarih.upper(), font=K.mono(22), fill=(110, 104, 98), anchor="rm")
    d.line((72, 138, W - 72, 138), fill=INK, width=2)
    lg = _logo(ticker, 150)
    if lg:
        if _plate_fill(lg)[0] < 100: lg = _plate(lg, 22, 28)
        img.paste(lg, (W - 72 - lg.width, 170), lg)
    d.text((72, 190), kicker.replace("i", "İ").upper(), font=sans(28, "ExtraBold"), fill=CL)
    f = None
    for fs in range(128, 60, -4):
        f = K.serif(fs); ls = _wrap(d, baslik, f, W - 144 - (340 if lg else 0))
        if len(ls) <= 4: break
    y = 244
    for l in ls:
        d.text((72, y), l, font=f, fill=INK); y += int(f.size * 1.0)
    y += 34
    for l in _wrap(d, spot, sans(36, "Medium"), W - 144)[:4]:
        d.text((72, y), l, font=sans(36, "Medium"), fill=(70, 66, 62)); y += 50
    y = max(y + 40, 860); d.line((72, y, W - 72, y), fill=INK, width=2); y += 36
    cw = (W - 144) / 3
    for i, (r, a) in enumerate(rakamlar3[:3]):
        x = 72 + i * cw
        if i: d.line((x - 14, y, x - 14, y + 250), fill=(206, 190, 176), width=2)
        fs = 124
        while d.textlength(r, font=K.serif(fs)) > cw - 40 and fs > 60: fs -= 4
        d.text((x, y), r, font=K.serif(fs), fill=TL if i else CL)
        for j, l in enumerate(_wrap(d, a, sans(26, "SemiBold"), cw - 40)[:3]):
            d.text((x, y + 150 + j * 34), l, font=sans(26, "SemiBold"), fill=(70, 66, 62))
    _footer(img, kaynak, ink=INK, muted=(120, 112, 104), line=INK, acc=CL)
    return _save(img, out, grain=False)


# ================= v4: ek seçenekler =================

# U — SKOR KARTI: beklenti vs gerçekleşen, tik/çarpı
def skor(ticker, etiket, baslik, satirlar, sonuc, kaynak, out):
    """satirlar: [(metrik, beklenti, gerçekleşen, iyi_mi_bool)]; sonuc: alt kısa cümle"""
    br = _brand(ticker, (110, 180, 255)); img = Image.new("RGB", (W, H), T_BG); M = 48
    _tile(img, (M, M, W - M, 360), T_TILE); d = ImageDraw.Draw(img)
    _pill(d, (M + 36, M + 36), etiket, br)
    lg = _logo(ticker, 200)
    if lg:
        p = _plate(lg, 24, 36); _shadow_paste(img, p, (W - M - 36 - p.width, M + 40), r=36); d = ImageDraw.Draw(img)
    f, ls = _fit(d, baslik, "Black", 64, W - 2 * M - 72 - (440 if lg else 0), 3); y = M + 112
    for l in ls:
        d.text((M + 36, y), l, font=f, fill=(255, 255, 255)); y += int(f.size * 1.08)
    y = 390
    hdr = [("METRİK", M + 36, "la"), ("BEKLENTİ", 560, "ma"), ("GERÇEK", 790, "ma")]
    for t, x, a in hdr:
        d.text((x, y), t, font=sans(22, "Bold"), fill=(140, 140, 152), anchor=a)
    y += 50; rh = min(190, (1040 - y) / max(1, len(satirlar)))
    for mt, bk, gr, ok in satirlar:
        _tile(img, (M, y, W - M, y + rh - 14), T_TILE, r=26); d = ImageDraw.Draw(img); cy = y + (rh - 14) / 2
        d.text((M + 36, cy), mt, font=sans(34, "Bold"), fill=(230, 230, 238), anchor="lm")
        d.text((560, cy), bk, font=_fitnum(d, bk, 200, 40, "SemiBold"), fill=(150, 150, 162), anchor="mm")
        d.text((790, cy), gr, font=_fitnum(d, gr, 220, 48), fill=(255, 255, 255), anchor="mm")
        c = K.UP if ok else K.DOWN; bx = W - M - 70
        d.ellipse((bx - 30, cy - 30, bx + 30, cy + 30), fill=c)
        if ok:
            d.line([(bx - 14, cy), (bx - 4, cy + 11), (bx + 15, cy - 11)], fill=(10, 10, 12), width=7, joint="curve")
        else:
            d.line([(bx - 11, cy - 11), (bx + 11, cy + 11)], fill=(10, 10, 12), width=7); d.line([(bx + 11, cy - 11), (bx - 11, cy + 11)], fill=(10, 10, 12), width=7)
        y += rh
    _tile(img, (M, 1060, W - M, 1190), _mix(br, (0, 0, 0), 0.35), fill2=_mix(br, (0, 0, 0), 0.65)); d = ImageDraw.Draw(img)
    f2, l2 = _fit(d, sonuc, "ExtraBold", 40, W - 2 * M - 72, 2)
    yy = 1125 - len(l2) * f2.size * 0.55
    for l in l2:
        d.text((M + 36, yy), l, font=f2, fill=(255, 255, 255)); yy += f2.size * 1.1
    _footer(img, kaynak, acc=br, line=T_BG)
    return _save(img, out)


# V — ZAMAN ÇİZELGESİ: dikey kilometre taşları
def zaman(ticker, etiket, baslik, adimlar, kaynak, out):
    """adimlar: [(tarih, başlık, açıklama)] (son adım vurgulu)"""
    br = _brand(ticker, (212, 175, 105))
    img = _lin(W, H, _mix(br, (0, 0, 0), 0.86), (6, 6, 8), diag=False); _watermark(img, ticker, 1000, alpha=10); d = ImageDraw.Draw(img)
    _pill(d, (72, 64), etiket, br)
    lg = _logo(ticker, 170)
    if lg: img.paste(lg, (W - 72 - lg.width, 56), lg)
    f, ls = _fit(d, baslik, "Black", 70, W - 144 - (330 if lg else 0), 2); y = 136
    for l in ls:
        d.text((72, y), l, font=f, fill=(255, 255, 255)); y += int(f.size * 1.06)
    y = max(y, 260) + 40; n = len(adimlar); rh = (H - 170 - y) / n; X = 130
    d.line((X, y + 20, X, y + rh * (n - 1) + 20), fill=(70, 70, 80), width=4)
    for i, (t, b, a) in enumerate(adimlar):
        last = i == n - 1; cy = y + 20
        if last:
            d.ellipse((X - 30, cy - 30, X + 30, cy + 30), fill=_mix(br, (0, 0, 0), 0.5))
        d.ellipse((X - 16, cy - 16, X + 16, cy + 16), fill=br if last else (200, 200, 210))
        d.text((190, cy), t.upper(), font=sans(24, "Bold"), fill=br if last else (150, 150, 162), anchor="lm")
        d.text((190, cy + 26), b, font=sans(44 if last else 38, "Black"), fill=(255, 255, 255))
        for j, l in enumerate(_wrap(d, a, sans(28, "Medium"), W - 262)[:2]):
            d.text((190, cy + 84 + j * 36), l, font=sans(28, "Medium"), fill=(175, 175, 188))
        y += rh
    _footer(img, kaynak, acc=br)
    return _save(img, out)


# W — İLERLEME ÇUBUKLARI: hedefe/paya göre doluluk
def ilerleme(ticker, etiket, baslik, alt, satirlar, kaynak, out, renk=None):
    """satirlar: [(etiket, oran_0_100, değer_metni)]"""
    br = renk or _brand(ticker, (88, 200, 140)); img = Image.new("RGB", (W, H), T_BG); d = ImageDraw.Draw(img)
    _pill(d, (72, 64), etiket, br)
    lg = _logo(ticker, 170)
    if lg: img.paste(lg, (W - 72 - lg.width, 56), lg)
    f, ls = _fit(d, baslik, "Black", 72, W - 144 - (330 if lg else 0), 3); y = 136
    for l in ls:
        d.text((72, y), l, font=f, fill=(255, 255, 255)); y += int(f.size * 1.06)
    d.text((72, y + 22), alt, font=sans(30, "Medium"), fill=(160, 160, 172)); y = max(y + 110, 410 if lg else 330)
    rh = min(210, (H - 170 - y) / len(satirlar))
    for i, (k, o, v) in enumerate(satirlar):
        d.text((72, y), k, font=sans(34, "Bold"), fill=(235, 235, 242))
        d.text((W - 72, y), v, font=sans(40, "Black"), fill=(255, 255, 255), anchor="ra")
        by = y + 62; _tile(img, (72, by, W - 72, by + 40), (34, 34, 42), r=20)
        if o > 0:
            _tile(img, (72, by, 72 + max(40, (W - 144) * min(o, 100) / 100), by + 40), _mix(br, (255, 255, 255), 0.15), r=20, fill2=_mix(br, (0, 0, 0), 0.25), diag=False)
        d = ImageDraw.Draw(img); y += rh
    _footer(img, kaynak, acc=br)
    return _save(img, out)


# X — DİLİM: çok parçalı halka (dağılım)
def dilim(ticker, etiket, baslik, parcalar, orta, orta_alt, kaynak, out):
    """parcalar: [(etiket, yüzde, renk_or_None)]"""
    pal = [(110, 180, 255), (255, 196, 60), (88, 200, 140), (255, 120, 90), (190, 150, 255), (120, 120, 130)]
    img = _radial((W, H), (26, 28, 40), (7, 7, 9), cy=0.45, r=0.8); d = ImageDraw.Draw(img)
    _pill(d, (72, 64), etiket, (255, 255, 255))
    f, ls = _fit(d, baslik, "Black", 70, W - 144, 2); y = 136
    for l in ls:
        d.text((72, y), l, font=f, fill=(255, 255, 255)); y += int(f.size * 1.06)
    S = 3; R, wd = 250, 90; cx, cy = 360, 640
    ring = Image.new("RGBA", (W * S, H * S), (0, 0, 0, 0)); rd = ImageDraw.Draw(ring); a0 = -90
    for i, (k, p, c) in enumerate(parcalar):
        c = c or pal[i % len(pal)]; a1 = a0 + 360 * p / 100
        rd.arc(((cx - R) * S, (cy - R) * S, (cx + R) * S, (cy + R) * S), a0 + 0.8, a1 - 0.8, fill=c + (255,), width=wd * S); a0 = a1
    ring = ring.resize((W, H), Image.LANCZOS); img.paste(ring, (0, 0), ring); d = ImageDraw.Draw(img)
    d.text((cx, cy - 6), orta, font=sans(84, "Black"), fill=(255, 255, 255), anchor="mm")
    d.text((cx, cy + 60), orta_alt, font=sans(24, "SemiBold"), fill=(170, 170, 182), anchor="mm")
    ly = cy - len(parcalar) * 48
    for i, (k, p, c) in enumerate(parcalar):
        c = c or pal[i % len(pal)]
        d.rounded_rectangle((680, ly + 6, 708, ly + 34), radius=8, fill=c)
        d.text((724, ly + 20), k, font=sans(30, "Bold"), fill=(230, 230, 238), anchor="lm")
        d.text((W - 72, ly + 20), f"%{p:g}".replace(".", ","), font=sans(32, "Black"), fill=(255, 255, 255), anchor="rm")
        ly += 96
    _footer(img, kaynak, acc=(255, 255, 255))
    return _save(img, out)


# Y — DÖRTLÜ MİNİ KART: 4 hisse, her biri logo + değer + not
def dortlu(etiket, baslik, kartlar, kaynak, out):
    """kartlar: [(ticker, büyük_değer, alt_not)] x4"""
    img = Image.new("RGB", (W, H), T_BG); d = ImageDraw.Draw(img); M, G = 48, 20
    _pill(d, (M + 8, 56), etiket, (255, 255, 255))
    f, ls = _fit(d, baslik, "Black", 72, W - 2 * M - 16, 2); y = 126
    for l in ls:
        d.text((M + 8, y), l, font=f, fill=(255, 255, 255)); y += int(f.size * 1.06)
    y += 30; cw = (W - 2 * M - G) / 2; ch = (H - 150 - y - G) / 2
    for i, (t, v, a) in enumerate(kartlar[:4]):
        br = _brand(t, (110, 180, 255)); x = M + (i % 2) * (cw + G); yy = y + (i // 2) * (ch + G)
        _tile(img, (x, yy, x + cw, yy + ch), _mix(br, (0, 0, 0), 0.62), fill2=(20, 20, 24))
        lg = _logo(t, 120)
        if lg:
            p = _plate(lg, 16, 24); img.paste(p, (int(x + 30), int(yy + 30)), p)
        d = ImageDraw.Draw(img)
        d.text((x + cw - 30, yy + 40), t.replace("$", ""), font=sans(34, "Black"), fill=(255, 255, 255), anchor="ra")
        col = K.UP if v[:1] == "+" else (K.DOWN if v[:1] in "-−" else (255, 255, 255))
        d.text((x + 30, yy + ch - 90), v, font=_fitnum(d, v, cw - 60, 110), fill=col, anchor="ls")
        for j, l in enumerate(_wrap(d, a, sans(26, "Medium"), cw - 60)[:2]):
            d.text((x + 30, yy + ch - 70 + j * 32), l, font=sans(26, "Medium"), fill=(190, 190, 200))
    _footer(img, kaynak, acc=(255, 255, 255), line=T_BG)
    return _save(img, out)


# Z — MANŞET FOTO + BENTO: üstte Enes fotoğrafı, altta 2 veri kutusu
def manset(photo, ticker, etiket, baslik, kutular, kaynak, out):
    br = _brand(ticker, (212, 175, 105)); img = Image.new("RGB", (W, H), T_BG); M, G = 48, 20
    ph = Image.open(photo).convert("RGB"); bw, bh = W - 2 * M, 640
    k = max(bw / ph.width, bh / ph.height); ph = ph.resize((int(ph.width * k) + 1, int(ph.height * k) + 1), Image.LANCZOS)
    ph = ph.crop(((ph.width - bw) // 2, int((ph.height - bh) * 0.2), (ph.width - bw) // 2 + bw, int((ph.height - bh) * 0.2) + bh))
    sh = Image.new("L", (bw, bh)); sd = ImageDraw.Draw(sh)
    for yy in range(bh):
        sd.line((0, yy, bw, yy), fill=int(220 * max(0, (yy - bh * 0.45) / (bh * 0.55))))
    ph.paste(Image.new("RGB", (bw, bh), (0, 0, 0)), (0, 0), sh)
    m = Image.new("L", (bw, bh), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, bw - 1, bh - 1), radius=40, fill=255); img.paste(ph, (M, M), m)
    d = ImageDraw.Draw(img); _pill(d, (M + 30, M + 30), etiket, br)
    lg = _logo(ticker, 130)
    if lg:
        p = _plate(lg, 18, 28); _shadow_paste(img, p, (W - M - 30 - p.width, M + 30), r=28); d = ImageDraw.Draw(img)
    f, ls = _fit(d, baslik, "Black", 76, bw - 60, 3); ty = M + bh - 40 - len(ls) * int(f.size * 1.05)
    for l in ls:
        d.text((M + 30, ty), l, font=f, fill=(255, 255, 255)); ty += int(f.size * 1.05)
    cw = (W - 2 * M - G) / 2; y = M + bh + G
    for i, (kk, v, a) in enumerate(kutular[:2]):
        x = M + i * (cw + G)
        _tile(img, (x, y, x + cw, H - 150), _mix(br, (0, 0, 0), 0.55) if i == 0 else T_TILE, fill2=_mix(br, (0, 0, 0), 0.8) if i == 0 else None); d = ImageDraw.Draw(img)
        d.text((x + 32, y + 32), kk.upper(), font=sans(24, "Bold"), fill=(200, 200, 210))
        d.text((x + 32, y + 230), v, font=_fitnum(d, v, cw - 64, 120), fill=(255, 255, 255), anchor="ls")
        for j, l in enumerate(_wrap(d, a, sans(28, "Medium"), cw - 64)[:3]):
            d.text((x + 32, y + 262 + j * 36), l, font=sans(28, "Medium"), fill=(185, 185, 196))
    _footer(img, kaynak, acc=br, line=T_BG)
    return _save(img, out)


# AA — PANEL: sade, profesyonel iki hisse karşılaştırması (versus yerine; Enes 15.11 21:23)
def panel(sol, sag, kicker, baslik, satirlar, cubuk, kaynak, out, notu=""):
    """sol/sag: '$TICKER'. satirlar: [(etiket, sol_değer, sağ_değer)].
    cubuk: (etiket, sol_oran, sag_oran) 0-1 arası (ör. fiyatın kalan kısmı) ya da None. notu: alt kısa satır."""
    BG, INK, MUT, LINE, GOLD = (12, 12, 14), (236, 234, 228), (128, 126, 122), (44, 43, 42), (201, 168, 106)
    img = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(img); M = 72
    d.text((M, 92), kicker.replace("i", "İ").upper(), font=K.mono(22), fill=GOLD, anchor="lm")
    d.line((M, 124, W - M, 124), fill=LINE, width=2)
    f = None
    for fs in range(96, 50, -4):
        f = K.serif(fs); ls = _wrap(d, baslik, f, W - 2 * M)
        if len(ls) <= 2: break
    y = 156
    for l in ls:
        d.text((M, y), l, font=f, fill=INK); y += int(f.size * 1.02)
    # kolon başlıkları
    y = y + 70; cx = [W * 0.56, W - M]
    for i, t in enumerate((sol, sag)):
        S = 140; lg = _logo(t, S - 36); x = cx[i]
        d.rounded_rectangle((x - S, y, x, y + S), radius=28, fill=(30, 30, 33) if not lg or _plate_fill(lg)[0] < 100 else (245, 245, 245))
        if lg:
            img.paste(lg, (int(x - S / 2 - lg.width / 2), int(y + S / 2 - lg.height / 2)), lg)
        else:
            d.text((x - S / 2, y + S / 2), t.replace("$", "")[:1], font=K.serif(96), fill=INK, anchor="mm")
        d = ImageDraw.Draw(img); d.text((x, y + S + 24), t, font=K.mono(26), fill=INK, anchor="ra")
    d = ImageDraw.Draw(img); y += 140 + 84
    d.line((M, y, W - M, y), fill=LINE, width=2)
    rh = 118
    for lab, a, b in satirlar:
        cy = y + rh / 2
        d.text((M, cy), lab.upper(), font=K.mono(21), fill=MUT, anchor="lm")
        for i, v in enumerate((a, b)):
            neg = v.strip()[:1] in "-−"; col = (226, 112, 98) if neg else ((126, 196, 140) if v.strip()[:1] == "+" else INK)
            d.text((cx[i], cy), v, font=sans(50, "SemiBold"), fill=col, anchor="rm")
        y += rh; d.line((M, y, W - M, y), fill=LINE, width=1)
    if cubuk:
        lab, ra, rb = cubuk; y += 48
        d.text((M, y), lab.upper(), font=K.mono(21), fill=MUT, anchor="la"); y += 48
        for t, r in ((sol, ra), (sag, rb)):
            d.text((M, y + 10), t, font=K.mono(22), fill=INK, anchor="lm")
            x0, x1 = M + 150, W - M
            d.rounded_rectangle((x0, y, x1, y + 20), radius=10, fill=(32, 32, 35))
            d.rounded_rectangle((x0, y, x0 + (x1 - x0) * max(0.02, min(1, r)), y + 20), radius=10, fill=GOLD)
            y += 50
    if notu:
        d.text((M, H - 170), notu, font=sans(28, "Medium"), fill=MUT, anchor="ls")
    _footer(img, kaynak, ink=INK, muted=MUT, line=LINE, acc=GOLD)
    return _save(img, out, grain=False)


# BEKLENTİ — bilanço öncesi kısa konsensüs tablosu (kural 49, Enes 18.11 22:16)
def beklenti(ticker, sirket, ceyrek, tarih_saat, satirlar, kaynak, out):
    """satirlar: [(metrik, konsensüs, not_ya_da_'')] 2-4 satır. Büyük logo + sade tablo."""
    br = _brand(ticker, (212, 175, 105))
    img = _lin(W, H, (16, 16, 20), (6, 6, 8), diag=False); d = ImageDraw.Draw(img)
    _pill(d, (72, 64), f"{ticker.lstrip('$')} • BİLANÇO BEKLENTİSİ", br)
    lg = _logo(ticker, 230)
    y = 150
    if lg:
        img.paste(lg, ((W - lg.width) // 2, y), lg); y += lg.height + 40
    for txt, fs, col in ((sirket, 64, (255, 255, 255)), (ceyrek, 40, br), (tarih_saat, 32, (170, 170, 180))):
        f = sans(fs, "Black" if fs == 64 else "SemiBold")
        d.text((W // 2, y), txt, font=f, fill=col, anchor="mt"); y += int(fs * 1.35)
    y += 30
    d.rounded_rectangle((72, y, W - 72, y + 84), 18, fill=br)
    d.text((110, y + 42), "Metrik", font=sans(34, "Bold"), fill=(10, 10, 12), anchor="lm")
    d.text((W - 110, y + 42), "Konsensüs", font=sans(34, "Bold"), fill=(10, 10, 12), anchor="rm")
    y += 100; rh = min(150, (H - 170 - y) / max(1, len(satirlar)))
    for m, v, n in satirlar[:4]:
        d.rounded_rectangle((72, y, W - 72, y + rh - 16), 18, fill=(28, 28, 34))
        cy = y + (rh - 16) / 2
        d.text((110, cy - (14 if n else 0)), m, font=sans(40, "Bold"), fill=(235, 235, 240), anchor="lm")
        if n: d.text((110, cy + 28), n, font=sans(26, "Medium"), fill=(150, 150, 160), anchor="lm")
        d.text((W - 110, cy), v, font=sans(64, "Black"), fill=(255, 255, 255), anchor="rm")
        y += rh
    _footer(img, kaynak, acc=br)
    return _save(img, out)

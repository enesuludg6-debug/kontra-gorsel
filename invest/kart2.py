"""EnesInvestUS kart v2 — daha dikkat çekici, profesyonel düzenler (deneme). 1080x1350.
Fontlar: Inter Display (Black/ExtraBold/Bold/SemiBold/Medium) + Instrument Serif + JetBrains Mono.
"""
import os, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import kart as K

D = K.D
W, H = 1080, 1350
HANDLE = "ENES ULUDAĞ"


def sans(s, w="Bold"):
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


def _logo(ticker, size):
    return K.logo(ticker, size) if ticker and ticker.startswith("$") else None


def _footer(img, kaynak, ink=(235, 235, 240), muted=(150, 150, 160), line=(60, 60, 70)):
    d = ImageDraw.Draw(img)
    d.line((72, H - 112, W - 72, H - 112), fill=line, width=2)
    d.text((72, H - 76), kaynak.upper(), font=K.mono(20), fill=muted, anchor="lm")
    d.text((W - 72, H - 76), HANDLE, font=sans(24, "ExtraBold"), fill=ink, anchor="rm")


def _save(img, out):
    os.makedirs(os.path.dirname(os.path.abspath(out)) or ".", exist_ok=True)
    img.convert("RGB").save(out, quality=93)
    return out


# A — SPOTLIGHT: marka renginde ışık hüzmesi, dev logo, dev rakam
def spotlight(ticker, rakam, baslik, alt, kaynak, out, etiket="RAKAM"):
    br = _brand(ticker)
    img = _radial((W, H), _mix(br, (0, 0, 0), 0.55), (6, 6, 8), cy=0.28, r=0.75)
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
    _footer(img, kaynak)
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
        img.paste(plate, ((W - plate.width) // 2, 280 - plate.height // 2), plate)
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
    d = ImageDraw.Draw(img)
    d.rectangle((0, 0, W, 90), fill=OR)
    d.text((40, 45), f"{ticker}  <EQUITY>  {etiket}", font=K.mono(34, 800), fill=(0, 0, 0), anchor="lm")
    d.text((W - 40, 45), "ENES", font=K.mono(34, 800), fill=(0, 0, 0), anchor="rm")
    lg = _logo(ticker, 200)
    if lg:
        img.paste(lg, (W - 60 - lg.width, 130), lg)
    f, ls = _fit(d, baslik, "Black", 78, W - 120 - (240 if lg else 0), 3)
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
    d = ImageDraw.Draw(img)
    d.rectangle((0, 0, W, 130), fill=RED)
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
    img = _vgrad((W, H), (16, 16, 20), (6, 6, 8))
    d = ImageDraw.Draw(img)
    d.text((72, 70), etiket, font=sans(28, "Bold"), fill=br)
    lg = _logo(ticker, 220)
    if lg:
        img.paste(lg, (W - 72 - lg.width, 60), lg)
    f, ls = _fit(d, baslik, "Black", 80, W - 144 - (240 if lg else 0), 3)
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
        img.paste(plate, (W - 72 - plate.width, 50), plate)
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
        img.paste(plate, (W - 72 - plate.width, 60), plate)
    d = ImageDraw.Draw(img, "RGBA")
    f, ls = _fit(d, baslik, "Black", 84, W - 144 - (320 if lg else 0), 3)
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
        img.paste(plate, (W - 72 - plate.width, 50), plate)
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

from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1350
NAVY = (10, 26, 58)
MID = (27, 51, 99)
LIGHT = (167, 196, 242)
WHITE = (255, 255, 255)
ANTON = "/home/claude/font/anton.ttf"
BEBAS = "/home/claude/font/bebas.ttf"
SS = 2  # supersample


def text_layer(text, fontpath, size, color, track=0, shear=0.0):
    f = ImageFont.truetype(fontpath, size * SS)
    adv = [f.getlength(c) for c in text]
    w = int(sum(adv) + track * SS * max(len(text) - 1, 0) + size * SS)
    h = int(size * SS * 1.8)
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    x = size * SS * 0.5
    for c, a in zip(text, adv):
        d.text((x, size * SS * 0.3), c, font=f, fill=color)
        x += a + track * SS
    if shear:
        im = im.transform((int(w + h * shear), h), Image.AFFINE,
                          (1, shear, -h * shear, 0, 1, 0), resample=Image.BICUBIC)
    bb = im.getbbox()
    im = im.crop(bb)
    return im.resize((max(1, im.width // SS), max(1, im.height // SS)), Image.LANCZOS)


def put(canvas, layer, x, y, align="left", valign="top"):
    if align == "center":
        x -= layer.width // 2
    elif align == "right":
        x -= layer.width
    if valign == "middle":
        y -= layer.height // 2
    canvas.alpha_composite(layer, (int(x), int(y)))


def fit(text, fontpath, size, color, maxw, **kw):
    while True:
        l = text_layer(text, fontpath, size, color, **kw)
        if l.width <= maxw or size < 10:
            return l
        size -= 4


def rect(canvas, box, color, alpha=255, radius=0):
    lay = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    d.rounded_rectangle(box, radius=radius, fill=color + (alpha,))
    canvas.alpha_composite(lay)


K_POLYS = [
    [(230, 220), (322, 220), (322, 580), (230, 580)],
    [(340.8, 357.9), (566.8, 561.9), (550.5, 580), (449.6, 580), (279.2, 426.1)],
    [(279.5, 373.6), (454.5, 218.6), (515.5, 287.4), (340.5, 442.4)],
    [(586, 164), (554, 332), (416, 176)],
]


def logo(canvas, x, y, size=76, word=True, word_color=WHITE):
    s = size * 4
    lay = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    d.rounded_rectangle((0, 0, s - 1, s - 1), radius=int(s * 0.22), fill=WHITE + (255,))
    k = s * 1.25 / 800
    off = -s * 0.125
    for p in K_POLYS:
        d.polygon([(px * k + off, py * k + off) for px, py in p], fill=NAVY + (255,))
    lay = lay.resize((size, size), Image.LANCZOS)
    canvas.alpha_composite(lay, (int(x), int(y)))
    if word:
        wl = text_layer("KONTRA", ANTON, int(size * 0.62), word_color, track=4, shear=0.2)
        put(canvas, wl, x + size + 16, y + size / 2, valign="middle")
        return size + 16 + wl.width
    return size


def gradient(canvas, top, bottom, color):
    lay = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    for yy in range(top, bottom):
        a = int(255 * (yy - top) / (bottom - top))
        d.line([(0, yy), (W, yy)], fill=color + (a,))
    canvas.alpha_composite(lay)


def mac_sonucu():
    c = Image.new("RGBA", (W, H), NAVY + (255,))
    rect(c, (0, 0, W, 940), MID)
    gradient(c, 640, 942, NAVY)
    # logo lockup centered
    tmp = Image.new("RGBA", (W, H))
    lw = logo(tmp, 0, 0, 76)
    logo(c, (W - lw) / 2, 36, 76)
    title = text_layer("MAÇ SONUCU", ANTON, 150, WHITE, track=6, shear=0.2)
    put(c, title, W / 2, 150, align="center")
    rect(c, (W / 2 - 90, 150 + title.height + 26, W / 2 + 90, 150 + title.height + 34), LIGHT)
    put(c, text_layer("FOTOĞRAFI BURAYA KOY · ARKA PLANI SİLİNMİŞ OYUNCU", BEBAS, 34, (111, 140, 196), track=3), W / 2, 520, align="center")
    score = text_layer("SKOR", ANTON, 190, WHITE, track=6, shear=0.2)
    put(c, score, W / 2, 1065, align="center", valign="middle")
    gap = 40
    put(c, fit("EV SAHİBİ", BEBAS, 52, LIGHT, 300, track=3), W / 2 - score.width / 2 - gap, 1065, align="right", valign="middle")
    put(c, fit("DEPLASMAN", BEBAS, 52, LIGHT, 300, track=3), W / 2 + score.width / 2 + gap, 1065, align="left", valign="middle")
    rect(c, (60, 1206, 1020, 1210), (44, 74, 128))
    put(c, text_layer("LİG · KAÇINCI HAFTA YAZ", BEBAS, 38, (143, 163, 191), track=3), 60, 1262, valign="middle")
    put(c, text_layer("@KONTRA_11", BEBAS, 38, WHITE, track=3), 1020, 1262, align="right", valign="middle")
    return c


def ilk_yari():
    c = Image.new("RGBA", (W, H), MID + (255,))
    gradient(c, 820, 1350, NAVY)
    logo(c, 60, 44, 76)
    put(c, text_layer("@KONTRA_11", BEBAS, 38, LIGHT, track=3), 1020, 82, align="right", valign="middle")
    put(c, text_layer("FOTOĞRAFI BURAYA KOY · SAHNENİN TAMAMI OLABİLİR", BEBAS, 34, (111, 140, 196), track=3), W / 2, 500, align="center")
    rect(c, (60, 960, 1020, 1250), WHITE, radius=30)
    rect(c, (350, 914, 730, 1004), NAVY, radius=45)
    put(c, text_layer("İLK YARI", ANTON, 52, WHITE, track=4, shear=0.2), W / 2, 959, align="center", valign="middle")
    score = text_layer("SKOR", ANTON, 150, NAVY, track=6, shear=0.2)
    put(c, score, W / 2, 1095, align="center", valign="middle")
    put(c, fit("EV SAHİBİ", BEBAS, 48, NAVY, 230, track=3), 95, 1095, valign="middle")
    put(c, fit("DEPLASMAN", BEBAS, 48, NAVY, 230, track=3), 985, 1095, align="right", valign="middle")
    put(c, fit("GOL: GOLCÜNÜN ADINI YAZ (DK YAZ)", BEBAS, 36, (90, 111, 148), 880, track=3), W / 2, 1205, align="center", valign="middle")
    return c


def gol():
    c = Image.new("RGBA", (W, H), (230, 237, 248, 255))
    put(c, text_layer("GOOOL", ANTON, 300, NAVY, track=8, shear=0.2), W / 2, 50, align="center")
    put(c, text_layer("FOTOĞRAFI BURAYA KOY · SEVİNEN OYUNCU, ARKA PLANI SİLİNMİŞ", BEBAS, 34, (127, 147, 184), track=3), W / 2, 600, align="center")
    rect(c, (0, 880, W, H), NAVY)
    rect(c, (0, 862, W, 884), LIGHT)
    put(c, fit("OYUNCU ADINI YAZ", ANTON, 120, WHITE, 960, track=4, shear=0.2), 60, 990, valign="middle")
    rect(c, (60, 1086, 250, 1162), WHITE, radius=38)
    put(c, text_layer("DK YAZ", BEBAS, 46, NAVY, track=3), 155, 1124, align="center", valign="middle")
    put(c, fit("EV SAHİBİ  SKOR  DEPLASMAN", BEBAS, 54, WHITE, 740, track=3), 280, 1124, valign="middle")
    logo(c, 60, 1232, 76)
    put(c, text_layer("@KONTRA_11", BEBAS, 38, WHITE, track=3), 1020, 1270, align="right", valign="middle")
    return c


if __name__ == "__main__":
    import sys
    out = sys.argv[1]
    for name, fn in [("KONTRA_1_mac_sonucu", mac_sonucu), ("KONTRA_2_ilk_yari", ilk_yari), ("KONTRA_3_gol", gol)]:
        fn().convert("RGB").save(f"{out}/{name}.png")
        print(name)

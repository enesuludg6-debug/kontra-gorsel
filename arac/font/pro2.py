"""KONTRA pro2: daha geniş, profesyonel düzen seti (Inter / Lora / Poppins + Anton).
Her fonksiyon 1080x1350 JPG üretir. Kullanım: sys.path.insert(0,'/home/claude/font'); from pro2 import *"""
import sys; sys.path.insert(0, "/home/claude/font")
from kontra_stil import *
from pro import cover, vgrad, grain
from PIL import Image, ImageDraw, ImageFont, ImageFilter

G = "/usr/share/fonts/truetype/google-fonts/"
I = "/usr/share/fonts/opentype/inter/"
FONTS = {
    "inter_black": I + "Inter-Black.otf", "inter_bold": I + "Inter-Bold.otf",
    "inter_semi": I + "Inter-SemiBold.otf", "inter_med": I + "Inter-Medium.otf",
    "inter_reg": I + "Inter-Regular.otf", "inter_light": I + "Inter-Light.otf",
    "inter_blackit": I + "Inter-BlackItalic.otf",
    "lora": G + "Lora-Variable.ttf", "lora_it": G + "Lora-Italic-Variable.ttf",
    "pop_bold": G + "Poppins-Bold.ttf", "pop_med": G + "Poppins-Medium.ttf",
    "anton": "/home/claude/font/anton.ttf", "bebas": "/home/claude/font/bebas.ttf",
}

def F(name, size, wght=None):
    f = ImageFont.truetype(FONTS[name], size)
    if wght:
        try: f.set_variation_by_axes([wght])
        except Exception: pass
    return f

def yaz(c, txt, xy, font, fill, track=0, anchor="la", alpha=255):
    """Harf aralıklı metin. anchor: la (sol-üst), ra (sağ-üst), ma (orta-üst), ls (sol-taban)."""
    d = ImageDraw.Draw(c)
    if track == 0:
        d.text(xy, txt, font=font, fill=fill + (alpha,) if len(fill) == 3 else fill, anchor=anchor); return d.textbbox(xy, txt, font=font, anchor=anchor)
    w = sum(d.textlength(ch, font=font) for ch in txt) + track * (len(txt) - 1)
    x, y = xy
    if anchor[0] == "r": x -= w
    elif anchor[0] == "m": x -= w / 2
    a = "l" + anchor[1]
    for ch in txt:
        d.text((x, y), ch, font=font, fill=fill + (alpha,) if len(fill) == 3 else fill, anchor=a)
        x += d.textlength(ch, font=font) + track
    return (xy[0], y, x, y + font.size)

def sar(txt, font, maxw):
    """Kelime kaydırma."""
    d = ImageDraw.Draw(Image.new("L", (1, 1))); out, cur = [], ""
    for w in txt.split():
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= maxw: cur = t
        else: out.append(cur); cur = w
    if cur: out.append(cur)
    return out

def sigdir(txt, name, size, maxw, wght=None, minsize=30):
    f = F(name, size, wght)
    d = ImageDraw.Draw(Image.new("L", (1, 1)))
    while d.textlength(txt, font=f) > maxw and size > minsize:
        size -= 4; f = F(name, size, wght)
    return f

def blok(c, satirlar, x, y, name, size, fill, maxw, lh=1.05, wght=None, anchor="la", track=0):
    """Çok satırlı paragraf; son y'yi döndürür."""
    f = F(name, size, wght)
    for s in satirlar:
        for line in sar(s, f, maxw):
            yaz(c, line, (x, y), f, fill, track=track, anchor=anchor); y += int(size * lh)
    return y

def _alt(c, kaynak, renk=(150, 150, 160), cizgi=(255, 255, 255), cizgi_a=50, y=1290):
    rect(c, (60, y - 28, 1020, y - 26), cizgi, alpha=cizgi_a)
    yaz(c, kaynak, (60, y), F("inter_semi", 22), renk, track=3)
    yaz(c, "@KONTRA_11", (1020, y), F("inter_bold", 24), renk, track=3, anchor="ra")


# 1 ---------- GAZETE MANŞETİ (krem kağıt, serif) ----------
def gazete(photo, ust_etiket, manset, spot, alt_satirlar, kaynak, out, vurgu=(170, 20, 30), yb=0.25, tarih="13 KASIM 2026"):
    c = Image.new("RGBA", (W, H), (244, 239, 228, 255))
    ink = (22, 20, 18)
    yaz(c, "KONTRA", (W // 2, 40), F("lora", 96, 700), ink, anchor="ma", track=6)
    rect(c, (60, 160, 1020, 163), ink); rect(c, (60, 168, 1020, 169), ink)
    yaz(c, tarih, (60, 182), F("inter_semi", 20), ink, track=4)
    yaz(c, "FUTBOL  /  SON BASKI", (1020, 182), F("inter_semi", 20), ink, track=4, anchor="ra")
    rect(c, (60, 214, 1020, 215), ink)
    yaz(c, ust_etiket, (60, 240), F("inter_bold", 24), vurgu, track=5)
    y = blok(c, [manset], 60, 278, "lora", 92, ink, 960, lh=1.02, wght=700)
    y += 14
    y = blok(c, [spot], 60, y, "lora_it", 34, (70, 64, 58), 960, lh=1.3, wght=400) + 16
    ph = cover(photo, 600, 1200 - y - 20, yb).convert("L").convert("RGB")
    c.paste(ph, (60, y))
    yaz(c, "FOTOĞRAF ARŞİV", (60, 1200 - 6), F("inter_med", 16), (110, 105, 98), track=3, anchor="ls")
    x2 = 690; yy = y
    rect(c, (x2 - 15, y, x2 - 14, 1200), ink, alpha=80)
    for t in alt_satirlar:
        yy = blok(c, [t], x2, yy, "lora", 27, ink, 330, lh=1.38, wght=420) + 18
    _alt(c, kaynak, renk=(80, 74, 68), cizgi=ink, cizgi_a=120, y=1290)
    grain(c, 5)
    return kaydet(c, out)


# 2 ---------- İSVİÇRE / MİNİMAL BEYAZ GRID ----------
def swiss(photo, no, kicker, baslik, bilgiler, kaynak, out, vurgu=(225, 30, 40), yb=0.2, pill_yazi="İDDİA"):
    c = Image.new("RGBA", (W, H), (246, 246, 244, 255)); ink = (14, 14, 16)
    for x in (60, 330, 600, 870): rect(c, (x, 0, x + 1, H), ink, alpha=18)
    c.paste(cover(photo, 540, 700, yb), (480, 120))
    rect(c, (480, 120, 1020, 820), ink, alpha=0)
    rect(c, (60, 120, 160, 220), vurgu)
    yaz(c, no, (110, 170), F("inter_black", 54), (255, 255, 255), anchor="mm")
    yaz(c, "KONTRA", (60, 52), F("inter_black", 30), ink, track=2)
    yaz(c, pill_yazi, (1020, 56), F("inter_bold", 22), vurgu, track=5, anchor="ra")
    yaz(c, kicker, (60, 260), F("inter_bold", 22), vurgu, track=4)
    yy = 300
    for line in baslik:
        f = sigdir(line, "inter_black", 96, 400); yaz(c, line, (56, yy), f, ink); yy += int(f.size * 1.02)
    y = 860
    for i, (k, v) in enumerate(bilgiler):
        x = 60 + (i % 3) * 320; yy = y + (i // 3) * 170
        rect(c, (x, yy, x + 280, yy + 2), ink)
        yaz(c, k, (x, yy + 18), F("inter_semi", 20), (110, 110, 115), track=3)
        f = sigdir(v, "inter_black", 64, 280); yaz(c, v, (x, yy + 52), f, ink)
    _alt(c, kaynak, renk=(110, 110, 115), cizgi=ink, cizgi_a=60)
    return kaydet(c, out)


# 3 ---------- SİNEMA / ALTYAZI ----------
def sinema(photo, alinti, konusan, baglam, kaynak, out, yb=0.3, vurgu=(240, 200, 90)):
    c = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    ph = cover(photo, W, 860, yb)
    from PIL import ImageEnhance
    ph = ImageEnhance.Color(ph).enhance(0.7); ph = ImageEnhance.Contrast(ph).enhance(1.1)
    c.paste(ph, (0, 170))
    vgrad(c, 760, 1030, (0, 0, 0), 0, 230)
    yaz(c, "KONTRA", (60, 70), F("inter_black", 30), (255, 255, 255), track=6)
    yaz(c, "SAHNE", (1020, 76), F("inter_semi", 20), (160, 160, 160), track=8, anchor="ra")
    y = 880
    for line in sar("“" + alinti + "”", F("lora_it", 52, 500), 900):
        yaz(c, line, (W // 2, y), F("lora_it", 52, 500), (255, 255, 255), anchor="ma"); y += 66
    y += 20
    yaz(c, "—  " + konusan, (W // 2, y), F("inter_bold", 26), vurgu, track=6, anchor="ma")
    yaz(c, baglam, (W // 2, y + 44), F("inter_med", 22), (170, 170, 170), track=3, anchor="ma")
    _alt(c, kaynak, cizgi_a=40, y=1300)
    grain(c, 9)
    return kaydet(c, out)


# 4 ---------- SON DAKİKA ŞERİTLERİ ----------
def ticker(photo, baslik, alt, kaynak, out, renk=(220, 32, 44), yb=0.2, etiket="SON DAKİKA"):
    c = Image.new("RGBA", (W, H), (10, 10, 12, 255))
    c.paste(cover(photo, W, H, yb), (0, 0))
    vgrad(c, 600, 1100, (10, 10, 12), 0, 245); rect(c, (0, 1100, W, H), (10, 10, 12), alpha=245)
    band = Image.new("RGBA", (W * 2, 90), renk + (255,))
    f = F("inter_black", 44); s = ("   " + etiket + "   •") * 12
    yaz(band, s, (0, 20), f, (255, 255, 255), track=4)
    for ang, yy, a in ((-6, 120, 255), (-6, 228, 120)):
        b = band.rotate(ang, expand=True, resample=Image.BICUBIC)
        if a < 255: b.putalpha(b.getchannel("A").point(lambda v: v * a // 255))
        c.alpha_composite(b, (-200, yy))
    logo(c, 60, 46, 50)
    y = 760
    for line in baslik:
        f2 = sigdir(line, "inter_black", 104, 960); yaz(c, line, (58, y), f2, (255, 255, 255)); y += int(f2.size * 1.0)
    rect(c, (60, y + 22, 180, y + 30), renk)
    blok(c, [alt], 60, y + 56, "inter_med", 32, (220, 220, 225), 960, lh=1.35)
    _alt(c, kaynak)
    return kaydet(c, out)


# 5 ---------- TRANSFER ROTASI ----------
def transfer_rota(photo, isim, nereden, nereye, renk1, renk2, durum, detaylar, kaynak, out, yb=0.2, pill_yazi="İDDİA", vurgu=SARI):
    c = Image.new("RGBA", (W, H), (12, 13, 18, 255))
    c.paste(cover(photo, W, 720, yb), (0, 0))
    vgrad(c, 380, 720, (12, 13, 18), 0, 255); vgrad(c, 0, 180, (0, 0, 0), 150, 0)
    logo(c, 60, 46, 50); pill(c, pill_yazi, 1020, 50, vurgu, KOYU_YAZI, 30)
    f = sigdir(isim, "inter_black", 110, 960); yaz(c, isim, (58, 600), f, (255, 255, 255))
    y = 780
    for x, ad, rk, et in ((60, nereden, renk1, "NEREDEN"), (600, nereye, renk2, "NEREYE")):
        rect(c, (x, y, x + 420, y + 170), (255, 255, 255), alpha=10, radius=14)
        rect(c, (x, y, x + 12, y + 170), rk[0]); rect(c, (x + 12, y, x + 24, y + 170), rk[1])
        yaz(c, et, (x + 50, y + 30), F("inter_semi", 20), (150, 150, 160), track=5)
        ff = sigdir(ad, "inter_black", 54, 350); yaz(c, ad, (x + 50, y + 70), ff, (255, 255, 255))
    d = ImageDraw.Draw(c)
    d.polygon([(500, y + 70), (560, y + 85), (500, y + 100)], fill=vurgu + (255,)); rect(c, (486, y + 81, 505, y + 89), vurgu)
    yaz(c, durum, (60, y + 210), F("inter_black", 34), vurgu, track=4)
    yy = y + 268
    for t in detaylar:
        yaz(c, "—  " + t, (60, yy), F("inter_med", 28), (205, 205, 212)); yy += 46
    _alt(c, kaynak)
    return kaydet(c, out)


# 6 ---------- DERGİ KAPAĞI ----------
def dergi(photo, buyuk, ana_baslik, kapak_satirlari, kaynak, out, renk=(255, 255, 255), vurgu=(230, 40, 60), yb=0.15, sayi="SAYI 13"):
    c = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    c.paste(cover(photo, W, H, yb), (0, 0))
    vgrad(c, 0, 420, (0, 0, 0), 150, 0); vgrad(c, 850, H, (0, 0, 0), 0, 220)
    f = sigdir(buyuk, "anton", 300, 980); yaz(c, buyuk, (W // 2, 40), f, renk, anchor="ma", alpha=235)
    yaz(c, sayi + "  /  KONTRA", (60, 30), F("inter_bold", 18), renk, track=6)
    y = 470
    for t in kapak_satirlari:
        rect(c, (50, y - 8, 470, y + 80), (0, 0, 0), alpha=150, radius=8)
        rect(c, (60, y, 66, y + 66), vurgu)
        yaz(c, t[0], (84, y), F("inter_black", 30), (255, 255, 255))
        yaz(c, t[1], (84, y + 36), F("lora_it", 24, 450), (230, 230, 230)); y += 104
    yy = 1030
    for line in sar(ana_baslik, F("lora", 70, 700), 960):
        yaz(c, line, (60, yy), F("lora", 70, 700), (255, 255, 255)); yy += 76
    _alt(c, kaynak, renk=(200, 200, 200))
    return kaydet(c, out)


# 7 ---------- ÇAPRAZ BÖLÜNMÜŞ ----------
def capraz(photo, kicker, baslik, govde, kaynak, out, renk=(20, 40, 110), vurgu=SARI, yb=0.2, pill_yazi="İDDİA"):
    c = Image.new("RGBA", (W, H), renk + (255,))
    ph = cover(photo, W, H, yb).convert("RGBA")
    m = Image.new("L", (W, H), 0); ImageDraw.Draw(m).polygon([(0, 0), (760, 0), (420, H), (0, H)], fill=255)
    c.paste(ph, (0, 0), m)
    ImageDraw.Draw(c).line([(760, 0), (420, H)], fill=vurgu + (255,), width=10)
    logo(c, 60, 46, 50); pill(c, pill_yazi, 1020, 50, vurgu, KOYU_YAZI, 30)
    x = 660; y = 560
    yaz(c, kicker, (x, y), F("inter_bold", 22), vurgu, track=4); y += 44
    for line in baslik:
        f = sigdir(line, "inter_black", 84, 1020 - x); yaz(c, line, (x, y), f, (255, 255, 255)); y += int(f.size * 1.02)
    y += 26
    blok(c, govde, x, y, "inter_med", 27, (225, 228, 240), 1020 - x, lh=1.4)
    _alt(c, kaynak, renk=(200, 205, 220))
    return kaydet(c, out)


# 8 ---------- VERİ PANELİ ----------
def veri_panel(photo, isim, alt_isim, kutular, not_satiri, kaynak, out, vurgu=(90, 220, 160), yb=0.15, pill_yazi="İSTATİSTİK"):
    c = Image.new("RGBA", (W, H), (11, 13, 18, 255))
    for x in range(0, W, 54): rect(c, (x, 0, x + 1, H), (255, 255, 255), alpha=6)
    for y in range(0, H, 54): rect(c, (0, y, W, y + 1), (255, 255, 255), alpha=6)
    logo(c, 60, 46, 50); pill(c, pill_yazi, 1020, 50, vurgu, KOYU_YAZI, 30)
    S = 260; av = cover(photo, S, S, yb).convert("RGBA")
    m = Image.new("L", (S * 3, S * 3), 0); ImageDraw.Draw(m).ellipse((0, 0, S * 3, S * 3), fill=255); m = m.resize((S, S), Image.LANCZOS)
    ring = Image.new("RGBA", (S + 16, S + 16), (0, 0, 0, 0)); ImageDraw.Draw(ring).ellipse((0, 0, S + 15, S + 15), outline=vurgu + (255,), width=5)
    c.alpha_composite(ring, (52, 152)); c.paste(av, (60, 160), m)
    f = sigdir(isim, "inter_black", 80, 640); yaz(c, isim, (360, 210), f, (255, 255, 255))
    yaz(c, alt_isim, (362, 320), F("inter_semi", 24), (150, 155, 170), track=4)
    y0 = 500
    for i, (v, k, ek) in enumerate(kutular[:4]):
        x = 60 + (i % 2) * 490; y = y0 + (i // 2) * 290
        rect(c, (x, y, x + 470, y + 260), (255, 255, 255), alpha=12, radius=18)
        rect(c, (x, y, x + 470, y + 4), vurgu, radius=2)
        yaz(c, k, (x + 34, y + 36), F("inter_semi", 22), (150, 155, 170), track=4)
        ff = sigdir(v, "inter_black", 110, 400); yaz(c, v, (x + 30, y + 80), ff, (255, 255, 255))
        yaz(c, ek, (x + 34, y + 210), F("inter_med", 22), vurgu, track=2)
    yaz(c, not_satiri, (60, 1100), F("inter_med", 26), (190, 195, 205))
    _alt(c, kaynak)
    return kaydet(c, out)


# 9 ---------- SAHA ÇİZİMİ / ŞUT HARİTASI (fotoğrafsız) ----------
def saha_sut(mesafe, birim, kicker, baslik, satirlar, kaynak, out, zemin=(10, 22, 40), cizgi=(255, 255, 255), vurgu=SARI, pill_yazi="RESMİ",
             sut_bas=(0.5, 0.98), sut_son=(0.47, 0.06)):
    """Yarım saha çizimi + şut yayı + dev mesafe. sut_bas/son: saha kutusunda oransal (x,y)."""
    c = Image.new("RGBA", (W, H), zemin + (255,))
    for i in range(0, 14):
        if i % 2 == 0: rect(c, (60, 130 + i * 50, 1020, 180 + i * 50), (255, 255, 255), alpha=6)
    S = 2; L = Image.new("RGBA", (W * S, H * S), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    x0, y0, x1, y1 = 60 * S, 130 * S, 1020 * S, 830 * S
    col = cizgi + (150,); w = 3 * S
    d.rectangle((x0, y0, x1, y1), outline=col, width=w)
    cx = (x0 + x1) // 2
    d.arc((cx - 130 * S, y1 - 130 * S, cx + 130 * S, y1 + 130 * S), 180, 360, fill=col, width=w)
    d.rectangle((cx - 300 * S, y0, cx + 300 * S, y0 + 230 * S), outline=col, width=w)
    d.rectangle((cx - 130 * S, y0, cx + 130 * S, y0 + 80 * S), outline=col, width=w)
    d.arc((cx - 130 * S, y0 + 120 * S, cx + 130 * S, y0 + 320 * S), 20, 160, fill=col, width=w)
    d.rectangle((cx - 55 * S, y0 - 22 * S, cx + 55 * S, y0), outline=cizgi + (230,), width=w)
    bx = x0 + (x1 - x0) * sut_bas[0]; by = y0 + (y1 - y0) * sut_bas[1]
    ex = x0 + (x1 - x0) * sut_son[0]; ey = y0 + (y1 - y0) * sut_son[1]
    pts = []
    for t in [i / 60 for i in range(61)]:
        mx = (bx + ex) / 2 + 160 * S; my = (by + ey) / 2
        px = (1 - t) ** 2 * bx + 2 * (1 - t) * t * mx + t ** 2 * ex; py = (1 - t) ** 2 * by + 2 * (1 - t) * t * my + t ** 2 * ey
        pts.append((px, py))
    for i in range(0, len(pts) - 1, 2): d.line([pts[i], pts[i + 1]], fill=vurgu + (255,), width=6 * S)
    d.ellipse((bx - 16 * S, by - 16 * S, bx + 16 * S, by + 16 * S), fill=(255, 255, 255, 255))
    d.ellipse((ex - 12 * S, ey - 12 * S, ex + 12 * S, ey + 12 * S), fill=vurgu + (255,))
    c.alpha_composite(L.resize((W, H), Image.LANCZOS))
    logo(c, 60, 46, 50); pill(c, pill_yazi, 1020, 50, vurgu, KOYU_YAZI, 30)
    f = F("inter_black", 150); bb = yaz(c, mesafe, (60, 870), f, (255, 255, 255))
    yaz(c, birim, (bb[2] + 18, 940), F("inter_black", 56), vurgu)
    yaz(c, kicker, (62, 1040), F("inter_bold", 22), vurgu, track=4)
    y = 1074
    for line in baslik:
        ff = sigdir(line, "inter_black", 56, 960); yaz(c, line, (60, y), ff, (255, 255, 255)); y += int(ff.size * 1.05)
    for t in satirlar:
        yaz(c, t, (60, y + 8), F("inter_med", 26), (200, 205, 215)); y += 40
    _alt(c, kaynak, y=1310)
    return kaydet(c, out)


# 10 ---------- RAKAM İKİLİSİ (fotoğrafsız) ----------
def rakam_ikilisi(isim, takim, r1, e1, r2, e2, notlar, kaynak, out, zemin=(150, 10, 25), vurgu=(255, 255, 255), pill_yazi="İSTATİSTİK", hayalet=None):
    c = Image.new("RGBA", (W, H), zemin + (255,))
    vgrad(c, 0, H, (0, 0, 0), 0, 120)
    if hayalet:
        yaz(c, hayalet, (W // 2, 120), F("anton", 520), (255, 255, 255), anchor="ma", alpha=14)
    logo(c, 60, 46, 50); pill(c, pill_yazi, 1020, 50, (255, 255, 255), KOYU_YAZI, 30)
    yaz(c, takim, (60, 200), F("inter_bold", 24), (255, 220, 220), track=6)
    f = sigdir(isim, "inter_black", 110, 960); yaz(c, isim, (56, 236), f, (255, 255, 255))
    y = 470
    for i, (r, e) in enumerate(((r1, e1), (r2, e2))):
        x = 60 + i * 490
        yaz(c, r, (x - 6, y), F("inter_black", 300), (255, 255, 255))
        yaz(c, e, (x, y + 330), F("inter_black", 44), (255, 255, 255), track=6)
    rect(c, (540, y + 40, 542, y + 380), (255, 255, 255), alpha=90)
    yy = 960
    for t in notlar:
        rect(c, (60, yy + 14, 74, yy + 28), (255, 255, 255))
        yaz(c, t, (96, yy), F("inter_med", 30), (255, 235, 235)); yy += 56
    _alt(c, kaynak, renk=(255, 210, 210), cizgi_a=90)
    grain(c, 6)
    return kaydet(c, out)

"""KONTRA GORSEL STANDARDI v3 (11.11.2026, Enes'in 7 ornegi)
7 sablon, hepsi 1080x1350, Enes'in fotografiyla:
  1 editoryal  - foto ustte, lacivert-siyah alta erir, ortali 2 satir dev baslik (Bellingham 1)
  2 bayrak     - krem zemin + bayrak carpisi, dev isim, kesilmis oyuncular onde (Bellingham 2)
  3 dev_rakam  - tam foto, sag ustte dev egik kirmizi rakam, altta baslik (Karius)
  4 istatistik - foto ustte, iki sutun rakam karsilastirmasi (Endrick)
  5 zaman      - baslik ustte, foto ortada, 3 adimli zaman cizelgesi (Oulai)
  6 ikili      - iki foto ust/alt, ortada koyu bant baslik (Arsenal)
  7 duoton     - foto takim renginde duoton, dev egik rakam/kelime, alinti (Kuyt veda)
Ortak dil: logo sol ust (lacivert kutu + beyaz K + egik beyaz KONTRA), Anton basliklar
(egik = shear 0.2), Bebas kucuk yazilar genis aralikli, vurgu tek renk (kirmizi veya sari),
IDDIA/VEDA etiketi hap (pill), altta ince ayirici cizgi + kaynak + @KONTRA_11.
"""
import sys
sys.path.insert(0, "/home/claude/font")
from kart import text_layer, put, fit, rect, K_POLYS, ANTON, BEBAS, W, H, NAVY, WHITE
from pro import cover, duotone, vgrad, grain
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance

LACI_SIYAH = (11, 15, 32)     # editoryal / duoton alt zemin
SIYAH = (14, 13, 15)          # istatistik / zaman zemini
KIRMIZI = (220, 32, 44)
SARI = (246, 190, 30)
ACIK = (202, 214, 234)        # 2. satir acik mavi-gri
GRI = (150, 156, 172)
KREM = (236, 233, 227)
KOYU_YAZI = (20, 22, 30)


# ---------- ortak parcalar ----------
def logo(c, x, y, size=50, word=True, cerceve=False):
    S = size * 4
    lay = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    d.rounded_rectangle((0, 0, S - 1, S - 1), radius=int(S * 0.22), fill=NAVY + (255,),
                        outline=(WHITE + (255,)) if cerceve else None, width=int(S * 0.05) if cerceve else 0)
    k = S * 1.25 / 800; off = -S * 0.125
    for p in K_POLYS:
        d.polygon([(px * k + off, py * k + off) for px, py in p], fill=WHITE + (255,))
    c.alpha_composite(lay.resize((size, size), Image.LANCZOS), (int(x), int(y)))
    if word:
        wl = text_layer("KONTRA", ANTON, int(size * 0.62), WHITE, track=4, shear=0.2)
        put(c, wl, x + size + 14, y + size / 2, valign="middle")


def handle(c, x=1020, y=70, color=WHITE, size=34):
    put(c, text_layer("@KONTRA_11", BEBAS, size, color, track=7), x, y, align="right", valign="middle")


def pill(c, text, x, y, bg=KIRMIZI, fg=WHITE, size=32, align="right", track=8):
    t = text_layer(text, BEBAS, size, fg, track=track)
    pw, ph = t.width + 48, int(size * 1.45)
    x0 = x - pw if align == "right" else (x - pw / 2 if align == "center" else x)
    rect(c, (x0, y, x0 + pw, y + ph), bg, radius=ph // 2)
    put(c, t, x0 + pw / 2, y + ph / 2, align="center", valign="middle")
    return ph


def tracked(c, text, x, y, color, size=34, align="left", track=9, valign="middle"):
    l = text_layer(text, BEBAS, size, color, track=track)
    put(c, l, x, y, align=align, valign=valign)
    return l


def dev(text, size, color=WHITE, egik=True, track=2, maxw=960):
    return fit(text, ANTON, size, color, maxw, track=track, shear=0.2 if egik else 0)


def foto_ust(c, photo, h, alt_renk, fade_from=None, yb=0.25, sat=1.0, bri=1.0):
    """Fotoyu ustten h yuksekligine yerlestir, fade_from..h arasi alt_renk'e erit."""
    ph = cover(photo, W, h, yb)
    if sat != 1.0: ph = ImageEnhance.Color(ph).enhance(sat)
    if bri != 1.0: ph = ImageEnhance.Brightness(ph).enhance(bri)
    c.paste(ph, (0, 0))
    vgrad(c, fade_from or int(h * 0.6), h, alt_renk, 0, 255)
    vgrad(c, 0, 200, (0, 0, 0), 120, 0)  # logo okunsun


def alt_bilgi(c, sol, y=1300, sag="@KONTRA_11", renk=GRI, cizgi_y=None, sol_size=30):
    if cizgi_y: rect(c, (60, cizgi_y, 1020, cizgi_y + 2), WHITE, alpha=60)
    if sol: put(c, fit(sol, BEBAS, sol_size, renk, 700 if sag else 960, track=6), 60, y, valign="middle")
    if sag: tracked(c, sag, 1020, y, WHITE, 32, align="right", track=7)


def kaydet(c, out):
    grain(c, 6)
    c.convert("RGB").save(out, quality=95)
    return out


# ---------- 1 EDITORYAL ----------
def editoryal(photo, kicker, satir1, satir2, alt, kaynak, out, etiketler=(), vurgu=KIRMIZI, yb=0.25):
    """etiketler: [("JUDE", x, y), ...] foto uzerindeki isimler."""
    c = Image.new("RGBA", (W, H), LACI_SIYAH + (255,))
    foto_ust(c, photo, 850, LACI_SIYAH, 600, yb)
    logo(c, 60, 46, 50); handle(c)
    for t, x, y in etiketler: tracked(c, t, x, y, WHITE, 40, align="center", track=9)
    tracked(c, kicker, W / 2, 874, vurgu, 38, align="center", track=10)
    put(c, dev(satir1, 122, WHITE, egik=False, track=4), W / 2, 902, align="center")
    put(c, dev(satir2, 122, ACIK, egik=False, track=4), W / 2, 1036, align="center")
    rect(c, (W / 2 - 60, 1190, W / 2 + 60, 1197), vurgu)
    put(c, fit(alt, BEBAS, 36, WHITE, 960, track=5), W / 2, 1238, align="center", valign="middle")
    rect(c, (60, 1268, 1020, 1270), WHITE, alpha=70)
    put(c, fit(kaynak, BEBAS, 30, (200, 205, 215), 960, track=6), W / 2, 1305, align="center", valign="middle")
    return kaydet(c, out)


# ---------- 2 BAYRAK ----------
def bayrak(cutlar, pill_yazi, dev_isim, sol, orta, sag, alt, out, zemin=KREM, carpi=KIRMIZI,
           bant=(14, 25, 55), vurgu=KIRMIZI):
    """cutlar: [(rgba_png, x, y, yukseklik), ...] arka plani silinmis oyuncular (rembg).
    sol/sag: (AD, alt_yazi); orta: (RAKAM, alt_yazi). carpi=None -> duz zemin."""
    c = Image.new("RGBA", (W, H), zemin + (255,))
    if carpi:
        rect(c, (470, 130, 610, 1150), carpi)
        rect(c, (0, 560, W, 700), carpi)
    rect(c, (0, 0, W, 130), bant); rect(c, (0, 1150, W, H), bant)
    logo(c, 56, 42, 50, cerceve=True); handle(c, y=66)
    pill(c, pill_yazi, W / 2, 180, bant, WHITE, 34, align="center", track=9)
    put(c, dev(dev_isim, 250, bant, egik=False, track=2, maxw=1010), W / 2, 290, align="center")
    for path, x, y, hh in cutlar:
        cu = Image.open(path).convert("RGBA")
        cu = cu.crop(cu.getbbox()); sc = hh / cu.height
        cu = cu.resize((int(cu.width * sc), hh), Image.LANCZOS)
        sh = Image.new("RGBA", cu.size, (0, 0, 0, 0)); sh.putalpha(cu.getchannel("A").point(lambda v: v * 0.45))
        sh = sh.filter(ImageFilter.GaussianBlur(10))
        c.alpha_composite(sh, (int(x + 10), int(y + 12))); c.alpha_composite(cu, (int(x), int(y)))
    put(c, dev(sol[0], 74, WHITE, egik=False, maxw=400), 60, 1168)
    tracked(c, sol[1], 62, 1265, (170, 178, 196), 32, track=7)
    put(c, dev(sag[0], 74, WHITE, egik=False, maxw=400), 1020, 1168, align="right")
    tracked(c, sag[1], 1018, 1262, (170, 178, 196), 32, align="right", track=7)
    put(c, dev(orta[0], 66, vurgu, egik=False, maxw=300), W / 2, 1172, align="center")
    tracked(c, orta[1], W / 2, 1263, WHITE, 28, align="center", track=5)
    tracked(c, alt, W / 2, 1318, (120, 130, 150), 26, align="center", track=6)
    return kaydet(c, out)


# ---------- 3 DEV RAKAM ----------
def dev_rakam(photo, rakam, birim, kicker, baslik, alt_sol, alt_sag, out, pill_yazi="İDDİA",
              vurgu=KIRMIZI, zemin=(18, 9, 10), yb=0.2):
    c = Image.new("RGBA", (W, H), zemin + (255,))
    ph = cover(photo, W, H, yb); c.paste(ph, (0, 0))
    vgrad(c, 820, 1110, zemin, 0, 245); rect(c, (0, 1110, W, H), zemin, alpha=245)
    r = dev(rakam, 400, vurgu, egik=True, track=0, maxw=520)
    put(c, r, 1040, 110, align="right")
    pill(c, pill_yazi, 1020, 50, vurgu, WHITE, 30)
    put(c, dev(birim, 110, WHITE), 1040, 110 + r.height + 10, align="right")
    tracked(c, kicker, 60, 1030, vurgu, 36, track=7)
    put(c, dev(baslik, 108, WHITE, maxw=960), 60, 1070)
    y = 1218
    l = tracked(c, alt_sol, 60, y, WHITE, 40, track=4)
    rect(c, (60 + l.width + 24, y - 2, 60 + l.width + 94, y + 2), vurgu)
    tracked(c, alt_sag, 60 + l.width + 118, y, WHITE, 40, track=4)
    rect(c, (60, 1262, 1020, 1264), WHITE, alpha=60)
    logo(c, 60, 1278, 46); handle(c, y=1301)
    return kaydet(c, out)


# ---------- 4 ISTATISTIK ----------
def istatistik(photo, kicker, baslik, sol_baslik, sol, sag_baslik, sag, kaynak, out,
               pill_yazi="İDDİA", vurgu=SARI, yb=0.15):
    """sol/sag: [("21","MAÇ"), ...]; sag sutun soluk (onceki/karsit durum)."""
    c = Image.new("RGBA", (W, H), SIYAH + (255,))
    foto_ust(c, photo, 700, SIYAH, 470, yb)
    logo(c, 60, 46, 50); pill(c, pill_yazi, 1020, 50, vurgu, KOYU_YAZI, 30)
    tracked(c, kicker, 60, 654, vurgu, 36, track=10)
    put(c, dev(baslik, 110, WHITE), 60, 690)
    rect(c, (540, 840, 542, 1210), WHITE, alpha=60)
    for x, bas, rows, renk, lab in ((60, sol_baslik, sol, WHITE, WHITE), (580, sag_baslik, sag, (130, 133, 140), (150, 153, 160))):
        tracked(c, bas, x, 853, vurgu if renk == WHITE else (175, 178, 186), 34, track=8)
        for i, (n, t) in enumerate(rows):
            y = 900 + i * 110
            nl = dev(n, 88, renk); put(c, nl, x, y)
            tracked(c, t, x + nl.width + 18, y + nl.height * 0.62, lab, 34, track=5)
    rect(c, (60, 1282, 1020, 1284), WHITE, alpha=60)
    alt_bilgi(c, kaynak, 1312, sol_size=26)
    return kaydet(c, out)


# ---------- 5 ZAMAN CIZELGESI ----------
def zaman(photo, kicker, baslik, adimlar, kaynak, out, pill_yazi="İDDİA", vurgu=SARI, yb=0.2):
    """adimlar: [(ETIKET, DEGER, ALT), x3]; son adim vurgu renginde."""
    c = Image.new("RGBA", (W, H), SIYAH + (255,))
    ph = cover(photo, W, 690, yb); c.paste(ph, (0, 255))
    vgrad(c, 255, 330, SIYAH, 255, 0); vgrad(c, 760, 945, SIYAH, 0, 255)
    logo(c, 60, 46, 50); pill(c, pill_yazi, 1020, 48, vurgu, KOYU_YAZI, 30)
    tracked(c, kicker, 60, 142, vurgu, 36, track=10)
    put(c, dev(baslik, 100, WHITE, egik=False, maxw=960), 60, 165)
    ly = 1010
    rect(c, (78, ly - 1, 1010, ly + 1), WHITE, alpha=110)
    xs = [60, 400, 740]
    for i, ((et, dg, al), x) in enumerate(zip(adimlar, xs)):
        son = i == len(adimlar) - 1
        lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(lay).ellipse((x, ly - 19, x + 38, ly + 19), fill=(vurgu if son else WHITE) + (255,))
        c.alpha_composite(lay)
        tracked(c, et, x, 1062, vurgu if son else (185, 188, 195), 34, track=6)
        put(c, dev(dg, 56, WHITE, egik=False, maxw=300), x, 1088)
        tracked(c, al, x, 1168, WHITE, 32, track=4)
    rect(c, (60, 1268, 1020, 1270), WHITE, alpha=60)
    alt_bilgi(c, kaynak, 1302, sol_size=26)
    return kaydet(c, out)


# ---------- 6 IKILI ----------
def ikili(foto1, foto2, ad1, ad2, kicker, baslik, kaynak, out, pill_yazi="İDDİA", vurgu=KIRMIZI,
          yb1=0.2, yb2=0.2):
    c = Image.new("RGBA", (W, H), (12, 12, 14, 255))
    c.paste(cover(foto1, W, 640, yb1), (0, 0)); c.paste(cover(foto2, W, 600, yb2), (0, 750))
    vgrad(c, 440, 640, (12, 12, 14), 0, 255); vgrad(c, 750, 850, (12, 12, 14), 255, 0)
    vgrad(c, 0, 180, (0, 0, 0), 130, 0); vgrad(c, 1180, H, (12, 12, 14), 0, 240)
    rect(c, (0, 640, W, 750), (12, 12, 14))
    logo(c, 60, 46, 50); pill(c, pill_yazi, 1020, 50, vurgu, WHITE, 30)
    put(c, dev(ad1, 62, WHITE, egik=False, maxw=600), 60, 532)
    put(c, dev(ad2, 62, WHITE, egik=False, maxw=600), 60, 785)
    tracked(c, kicker, W / 2, 668, vurgu, 32, align="center", track=10)
    put(c, dev(baslik, 74, WHITE, egik=False, maxw=960), W / 2, 690, align="center")
    rect(c, (60, 1268, 1020, 1270), WHITE, alpha=60)
    alt_bilgi(c, kaynak, 1305)
    return kaydet(c, out)


# ---------- 7 DUOTON ----------
TAKIM_DUOTON = {  # (golge, orta, isik, vurgu)
    "FENERBAHCE": ((12, 22, 80), (40, 70, 190), (250, 215, 30), (250, 210, 20)),
    "GALATASARAY": ((60, 6, 12), (190, 25, 35), (253, 190, 30), (253, 185, 19)),
    "BESIKTAS": ((10, 10, 10), (110, 110, 110), (245, 245, 245), (255, 255, 255)),
    "TRABZONSPOR": ((50, 8, 25), (150, 25, 60), (110, 190, 240), (90, 175, 235)),
    "MILLI": ((60, 4, 10), (200, 20, 30), (250, 250, 250), (230, 30, 40)),
    "KONTRA": ((6, 14, 34), (27, 51, 99), (167, 196, 242), (167, 196, 242)),
}


def duoton(photo, takim, ust_sag, pill_yazi, dev_yazi, alinti, baslik, alt_sol, alt_sag, out, yb=0.2):
    g, m, i, v = TAKIM_DUOTON[takim]
    c = Image.new("RGBA", (W, H), LACI_SIYAH + (255,))
    ph = duotone(cover(photo, W, 960, yb), g, i, m).convert("RGBA"); c.alpha_composite(ph, (0, 0))
    vgrad(c, 620, 960, LACI_SIYAH, 0, 255); vgrad(c, 0, 180, (0, 0, 0), 110, 0)
    logo(c, 60, 52, 52)
    tracked(c, ust_sag, 1020, 80, WHITE, 32, align="right", track=9)
    pill(c, pill_yazi, 60, 690, v, KOYU_YAZI, 36, align="left", track=12)
    put(c, dev(dev_yazi, 270, WHITE, maxw=960), 60, 770)
    put(c, dev(alinti, 50, v, egik=False, maxw=960), 60, 1035)
    put(c, dev(baslik, 66, WHITE, egik=False, maxw=960), 60, 1100)
    rect(c, (60, 1192, 1020, 1194), WHITE, alpha=60)
    tracked(c, alt_sol, 60, 1240, (190, 195, 205), 40, track=5)
    tracked(c, alt_sag, 1020, 1236, v, 40, align="right", track=4)
    tracked(c, "@KONTRA_11", W / 2, 1312, (150, 156, 172), 30, align="center", track=9)
    return kaydet(c, out)


def kes(photo, out):
    """rembg ile oyuncuyu kes (bayrak sablonu ve gol karti icin)."""
    from rembg import remove, new_session
    im = Image.open(photo).convert("RGBA")
    remove(im, session=new_session("isnet-general-use")).save(out)
    return out

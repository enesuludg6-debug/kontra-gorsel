import sys; sys.path.insert(0, "/home/claude/font")
from kontra_stil import *
from pro import cover, vgrad, grain
from PIL import Image, ImageDraw, ImageFilter

def rozet(photo, ay, odul, isim, satirlar, kaynak, out, vurgu=SARI, zemin=(30, 8, 18), pill_yazi="RESMİ",
          yb=0.35, blur_kutu=None):
    """Yeni düzen: tam boy foto, sağ üstte daire rozet (ay + ödül), altta isim ve rakam satırı."""
    src = Image.open(photo).convert("RGB")
    if blur_kutu:
        x0, y0, x1, y1 = blur_kutu
        b = src.filter(ImageFilter.GaussianBlur(10)); m = Image.new("L", src.size, 0)
        ImageDraw.Draw(m).ellipse(blur_kutu, fill=255); m = m.filter(ImageFilter.GaussianBlur(10))
        src = Image.composite(b, src, m)
    tmp = "/tmp/_rz.jpg"; src.save(tmp, quality=95)
    c = Image.new("RGBA", (W, H), zemin + (255,))
    c.paste(cover(tmp, W, H, yb), (0, 0))
    vgrad(c, 0, 220, (0, 0, 0), 160, 0)
    vgrad(c, 760, 1040, zemin, 0, 240); rect(c, (0, 1040, W, H), zemin, alpha=240)
    logo(c, 60, 46, 50); pill(c, pill_yazi, 1020, 50, vurgu, KOYU_YAZI, 30)
    S = 2; R = 150; cx, cy = 860, 300
    lay = Image.new("RGBA", (W * S, H * S), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.ellipse(((cx - R) * S, (cy - R) * S, (cx + R) * S, (cy + R) * S), fill=vurgu + (255,))
    d.ellipse(((cx - R + 14) * S, (cy - R + 14) * S, (cx + R - 14) * S, (cy + R - 14) * S), outline=(30, 20, 10, 255), width=3 * S)
    c.alpha_composite(lay.resize((W, H), Image.LANCZOS))
    a = dev(ay, 92, KOYU_YAZI, egik=False, track=2, maxw=240); put(c, a, cx - a.width // 2, cy - 70)
    tracked(c, odul[0], cx, cy + 50, KOYU_YAZI, 24, track=6, align="center")
    tracked(c, odul[1], cx, cy + 82, KOYU_YAZI, 24, track=6, align="center")
    y = 1000
    d2 = dev(isim, 118, WHITE, egik=True, track=2, maxw=960); put(c, d2, 54, y); y += d2.height + 22
    for t in satirlar:
        tracked(c, t, 60, y, (220, 205, 210), 27, track=6); y += 44
    rect(c, (60, 1262, 1020, 1264), WHITE, alpha=60)
    alt_bilgi(c, kaynak, 1302, sol_size=26)
    grain(c, 6)
    return kaydet(c, out)

if __name__ == "__main__":
    rozet("/home/claude/kontra-foto/foto/nicolas_jackson_villa.jpg", "EKİM", ("PREMIER LİG", "AYIN OYUNCUSU"),
        "NICOLAS JACKSON", ["ASTON VILLA  /  EKİMDE 4 LİG MAÇI, 4 GOL"],
        "KAYNAK: PREMIER LİG", "/home/claude/kontra-gorsel/g/jackson_ekim.jpg", blur_kutu=(250, 1300, 400, 1360))
    print("ok")

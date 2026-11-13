import sys; sys.path.insert(0, "/home/claude/font")
from kontra_stil import *
from pro import cover, vgrad, grain
from PIL import Image, ImageFilter

def puan_tablosu(photo, kicker, baslik, satirlar, vurgu_satir, alt_not, kaynak, out,
                 vurgu=KIRMIZI, zemin=(16, 8, 10), pill_yazi="İSTATİSTİK", yb=0.05, blur_kutu=None):
    """Yeni düzen: üstte foto, altta puan tablosu (vurgu satırı renkli bant).
    satirlar: [(sira, takim, O, averaj, P)]"""
    src = Image.open(photo).convert("RGB")
    if blur_kutu:
        x0,y0,x1,y1 = blur_kutu
        b = src.filter(ImageFilter.GaussianBlur(14))
        m = Image.new("L", src.size, 0); from PIL import ImageDraw
        ImageDraw.Draw(m).ellipse((x0, y0, x1, y1), fill=255); m = m.filter(ImageFilter.GaussianBlur(14))
        src = Image.composite(b, src, m)
    tmp = "/tmp/_pt_src.jpg"; src.save(tmp, quality=95)
    c = Image.new("RGBA", (W, H), zemin + (255,))
    c.paste(cover(tmp, W, 760, yb), (0, 0))
    vgrad(c, 0, 220, (0, 0, 0), 170, 0)
    vgrad(c, 440, 760, zemin, 0, 255)
    logo(c, 60, 46, 50); pill(c, pill_yazi, 1020, 50, vurgu, WHITE, 30)
    rect(c, (48, 528, 60 + 21 * len(kicker) + 30, 572), zemin, alpha=215, radius=4)
    tracked(c, kicker, 60, 550, vurgu, 28, track=10)
    y = 580
    for t in baslik:
        r = dev(t, 100, WHITE, egik=True, track=2, maxw=960); put(c, r, 54, y); y += r.height + 6
    y += 30
    # başlık satırı
    cols = [(60, "left"), (150, "left"), (700, "center"), (840, "center"), (1000, "right")]
    for (x, al), h in zip(cols, ["#", "TAKIM", "O", "AV", "P"]):
        tracked(c, h, x, y + 14, (150, 140, 145), 22, track=6, align=al)
    y += 36
    for i, row in enumerate(satirlar):
        hl = (i == vurgu_satir)
        if hl: rect(c, (40, y, 1040, y + 80), vurgu, radius=6)
        else: rect(c, (40, y + 85, 1040, y + 86), WHITE, alpha=30)
        renk = WHITE
        for (x, al), val in zip(cols, row):
            d = dev(str(val), 50, renk, egik=False, track=2, maxw=500)
            xx = x if al == "left" else (x - d.width // 2 if al == "center" else x - d.width)
            sv = str(val)
            plain = sv.replace("İ","I").replace("Ü","U").replace("Ö","O")
            dot = d.height - dev(plain, 50, renk, egik=False, track=2, maxw=500).height
            base = dev(plain.replace("Ç","C").replace("Ş","S"), 50, renk, egik=False, track=2, maxw=500).height
            put(c, d, xx, y + 62 - base - dot)
        y += 92
    tracked(c, alt_not, 60, y + 30, (200, 190, 192), 24, track=6)
    rect(c, (60, 1262, 1020, 1264), WHITE, alpha=60)
    alt_bilgi(c, kaynak, 1302, sol_size=26)
    grain(c, 6)
    return kaydet(c, out)

if __name__ == "__main__":
    puan_tablosu("/home/claude/kontra-foto/foto/milli_8_uzgun_ispanya.jpg", "ULUSLAR A LİGİ  /  1. GRUP",
        ["5 MAÇ, 0 PUAN"],
        [(1, "İTALYA", 5, "11-6", 10), (2, "FRANSA", 5, "8-5", 10), (3, "BELÇİKA", 5, "8-6", 9), (4, "TÜRKİYE", 5, "3-13", 0)],
        3, "SON MAÇ: FRANSA - TÜRKİYE  /  PAZAR 22.45",
        "KAYNAK: UEFA ULUSLAR LİGİ PUAN DURUMU", "/home/claude/kontra-gorsel/g/a1_puan_durumu.jpg",
        blur_kutu=(540, 330, 740, 420))
    print("ok")

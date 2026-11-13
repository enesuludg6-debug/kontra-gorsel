import sys; sys.path.insert(0, "/home/claude/font")
from kontra_stil import *
from PIL import Image, ImageEnhance

def fiyat_talipler(photo, kicker, fiyat, birim, ad1, ad2, bilgi, talipler, kaynak, out,
                   vurgu=SARI, zemin=SIYAH, pill_yazi="İDDİA", yb=0.0):
    """Yeni düzen: foto üstte, altta dev fiyat etiketi + yanında isim,
    'TALİPLER' listesi (kulüp renk çifti + ad + durum; ilk satır vurgulu)."""
    c = Image.new("RGBA", (W, H), zemin + (255,))
    ph = ImageEnhance.Color(cover(photo, W, 700, yb)).enhance(0.8)
    c.paste(ph, (0, 0))
    vgrad(c, 380, 640, zemin, 0, 255); rect(c, (0, 640, W, 700), zemin)
    vgrad(c, 0, 190, (0, 0, 0), 140, 0)
    logo(c, 60, 46, 50); pill(c, pill_yazi, 1020, 50, vurgu, KOYU_YAZI, 30)
    tracked(c, kicker, 60, 600, vurgu, 34, track=9)
    f = dev(fiyat, 250, WHITE, egik=True, track=0, maxw=520); put(c, f, 52, 632)
    b = dev(birim, 92, vurgu, egik=True, track=2, maxw=300); put(c, b, 60 + f.width + 10, 632 + f.height - b.height)
    xr = 60 + f.width + b.width + 50
    rect(c, (xr - 24, 650, xr - 22, 632 + f.height), WHITE, alpha=60)
    a1 = dev(ad1, 70, WHITE, egik=False, track=2, maxw=1020 - xr); put(c, a1, xr, 650)
    a2 = dev(ad2, 70, ACIK, egik=False, track=2, maxw=1020 - xr); put(c, a2, xr, 650 + a1.height + 14)
    tracked(c, bilgi, xr, 632 + f.height - 12, GRI, 28, track=5)
    # talipler
    y = 948
    tracked(c, "TALİPLER", 60, y, vurgu, 32, track=12)
    rect(c, (270, y - 1, 1020, y + 1), WHITE, alpha=50)
    for i, (ad, renk1, renk2, durum) in enumerate(talipler):
        yy = 1000 + i * 82
        ilk = i == 0
        if ilk: rect(c, (40, yy - 8, 1040, yy + 70), WHITE, alpha=14, radius=10)
        rect(c, (60, yy + 6, 76, yy + 56), renk1, radius=3); rect(c, (80, yy + 6, 96, yy + 56), renk2, radius=3)
        put(c, dev(ad, 54, WHITE, egik=False, track=2, maxw=520), 120, yy + 31, valign="middle")
        tracked(c, durum, 1010, yy + 31, vurgu if ilk else (175, 178, 188), 30, align="right", track=7)
    rect(c, (60, 1262, 1020, 1264), WHITE, alpha=60)
    alt_bilgi(c, kaynak, 1302, sol_size=26)
    return kaydet(c, out)

fiyat_talipler("/mnt/user-data/uploads/e95b5fbf-image.jpg",
               "CSKA MOSKOVANIN BONSERVİS BEKLENTİSİ", "30+", "M€",
               "MATVEY", "KISLYAK", "21 YAŞ  ·  ORTA SAHA  ·  RUSYA",
               [("GALATASARAY", (169, 18, 40), (253, 185, 19), "İLK HEDEF"),
                ("BEŞİKTAŞ", (245, 245, 245), (95, 95, 100), "TAKİPTE"),
                ("TRABZONSPOR", (120, 20, 45), (90, 175, 235), "TAKİPTE")],
               "KAYNAK: HT SPOR  ·  DİĞER İLGİ: TÜRK BASINI",
               "/mnt/user-data/outputs/KONTRA_kislyak.jpg")
print("ok")

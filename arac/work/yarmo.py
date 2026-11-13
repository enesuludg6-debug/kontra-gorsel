import sys; sys.path.insert(0, "/home/claude/font")
from kontra_stil import *
from PIL import Image, ImageEnhance

def deger_artisi(photo, kicker, isim, once, sonra, kat_kicker, kat, kat_alt, koz, kaynak, out,
                 zemin=(30, 8, 18), vurgu=(90, 175, 235), pill_yazi="İDDİA", yb=0.0):
    """Yeni düzen: foto üstte zemine erir, altta iki çubuklu değer grafiği (gerçek oranlı)
    + yanda dev kat rakamı, en altta 'koz' satırı. once/sonra: (deger, etiket, yil)."""
    c = Image.new("RGBA", (W, H), zemin + (255,))
    ph = ImageEnhance.Color(cover(photo, W, 680, yb)).enhance(0.85)
    c.paste(ph, (0, 0))
    vgrad(c, 330, 600, zemin, 0, 255); rect(c, (0, 600, W, 680), zemin); vgrad(c, 0, 190, (0, 0, 0), 140, 0)
    logo(c, 60, 46, 50); pill(c, pill_yazi, 1020, 50, vurgu, KOYU_YAZI, 30)
    tracked(c, kicker, 60, 612, vurgu, 34, track=9)
    put(c, dev(isim, 104, WHITE, egik=True, track=3), 60, 642)
    # çubuk grafik (gerçek oran)
    base, hmax = 1125, 270
    v1, v2 = once[0], sonra[0]
    for i, (v, lab, yil) in enumerate((once, sonra)):
        x0 = 60 + i * 200; h = max(6, int(hmax * v / v2))
        son = i == 1
        rect(c, (x0, base - h, x0 + 160, base), vurgu if son else (150, 120, 130), radius=4)
        l = dev(lab, 52, WHITE, egik=False, track=1, maxw=170)
        if son: put(c, dev(lab, 52, zemin, egik=False, track=1, maxw=150), x0 + 80, base - h + 18, align="center")
        else: put(c, l, x0 + 80, base - h - 14 - l.height, align="center")
        tracked(c, yil, x0 + 80, base + 26, vurgu if son else GRI, 30, align="center", track=7)
    rect(c, (60, base, 420, base + 2), WHITE, alpha=90)
    # sağ: dev kat
    rect(c, (480, 840, 482, 1150), WHITE, alpha=50)
    tracked(c, kat_kicker, 530, 862, vurgu, 34, track=9)
    k = dev(kat, 210, WHITE, egik=True, track=2, maxw=490); put(c, k, 530, 895)
    tracked(c, kat_alt, 530, 895 + k.height + 36, ACIK, 32, track=6)
    # koz satırı
    ph_ = pill(c, koz[0], 60, 1200, vurgu, KOYU_YAZI, 28, align="left", track=8)
    tracked(c, koz[1], 60 + 130, 1200 + ph_ / 2, WHITE, 32, track=5)
    rect(c, (60, 1262, 1020, 1264), WHITE, alpha=60)
    alt_bilgi(c, kaynak, 1302, sol_size=26)
    return kaydet(c, out)

deger_artisi("/mnt/user-data/uploads/20328b25-image.jpg",
             "TRABZONSPORUN ORTA SAHA HEDEFİ", "YEGOR YARMOLYUK",
             (1, "1 M€", "2023"), (32, "32 M€", "BUGÜN"),
             "3 YILDA DEĞERİ", "32 KAT", "22 YAŞ  ·  SÖZLEŞME 2031",
             ("KOZ", "MENAJERLİK ŞİRKETİ BATAGOV İLE AYNI"),
             "KAYNAK: SABAH  ·  PİYASA DEĞERİ", "/mnt/user-data/outputs/KONTRA_yarmolyuk.jpg")
print("ok")

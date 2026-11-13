import sys; sys.path.insert(0, "/home/claude/font")
from kontra_stil import *
from pro import cover, vgrad, grain
from PIL import Image

def iki_asama(photo, kicker, baslik, adimlar, not_satiri, kaynak, out,
              vurgu=SARI, zemin=(24, 8, 10), pill_yazi="İDDİA", yb=0.12):
    """Yeni düzen: üstte foto, altta numaralı 2 aşamalı plan (bağlantı çizgili kutular).
    adimlar: [(ust_kucuk, buyuk, alt_kucuk), (...)]"""
    c = Image.new("RGBA", (W, H), zemin + (255,))
    c.paste(cover(photo, W, 860, yb), (0, 0))
    vgrad(c, 0, 220, (0, 0, 0), 170, 0)
    vgrad(c, 440, 800, zemin, 0, 255); rect(c, (0, 800, W, 860), zemin)
    logo(c, 60, 46, 50); pill(c, pill_yazi, 1020, 50, vurgu, KOYU_YAZI, 30)
    # başlık bloğu
    rect(c, (48, 618, 390, 662), zemin, alpha=215, radius=4)
    tracked(c, kicker, 60, 640, vurgu, 28, track=10)
    y = 668
    for t in baslik:
        r = dev(t, 104, WHITE, egik=True, track=2, maxw=960); put(c, r, 54, y); y += r.height + 8
    # aşama kutuları
    by = y + 30; bh = 190; bw = 440; gap = 80
    for i, (ust, buyuk, alt) in enumerate(adimlar):
        x = 60 + i * (bw + gap)
        rect(c, (x, by, x + bw, by + bh), (255, 255, 255), alpha=14, radius=10)
        rect(c, (x, by, x + 8, by + bh), vurgu)
        n = dev(str(i + 1), 120, vurgu, egik=False, track=1, maxw=120); put(c, n, x + 30, by + 20)
        tx = x + 30 + n.width + 24
        tracked(c, ust, tx, by + 48, (200, 190, 192), 24, track=6)
        b = dev(buyuk, 64, WHITE, egik=False, track=2, maxw=x + bw - tx - 16); put(c, b, tx - 2, by + 70)
        tracked(c, alt, x + 30, by + bh - 34, vurgu, 26, track=7)
    # bağlantı oku
    ax = 60 + bw + 10; ay = by + bh // 2
    rect(c, (ax, ay - 2, ax + gap - 26, ay + 2), vurgu)
    for k in range(14):
        rect(c, (ax + gap - 26 + k, ay - 14 + k, ax + gap - 25 + k, ay + 14 - k), vurgu)
    tracked(c, not_satiri, 60, by + bh + 36, (200, 190, 192), 24, track=6)
    rect(c, (60, 1262, 1020, 1264), WHITE, alpha=60)
    alt_bilgi(c, kaynak, 1302, sol_size=26)
    grain(c, 6)
    return kaydet(c, out)

if __name__ == "__main__":
    iki_asama("/home/claude/kontra-foto/foto/gs_45_maske.jpg", "VICTOR OSIMHEN",
        ["DÖNÜŞ PLANI", "İKİ AŞAMALI"],
        [("24 KASIM", "ASTON VILLA", "SÜRE ALACAK"), ("ARDINDAN", "BJK DERBİSİ", "90 DAKİKA HEDEF")],
        "SAMSUNSPOR MAÇINDA YOK  /  RESMİ AÇIKLAMA YOK",
        "KAYNAK: FANATİK, POSTA", "/home/claude/kontra-gorsel/g/osimhen_donus_plani.jpg")
    print("ok")

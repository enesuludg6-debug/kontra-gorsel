import sys; sys.path.insert(0, "/home/claude/font")
from kontra_stil import *
from PIL import Image, ImageEnhance

def soyledi_duzeltti(photo, dev_kelime, kicker, sol, sag, bilgi, kaynak, out, vurgu=SARI, zemin=SIYAH, pill_yazi="AÇIKLAMA", yb=0.0):
    """Yeni düzen: tam foto, ortada dev soru kelimesi, altta iki sütun: SÖYLEDİ / DÜZELTTİ."""
    c = Image.new("RGBA", (W, H), zemin + (255,))
    ph = ImageEnhance.Color(cover(photo, W, H, yb)).enhance(0.9)
    c.paste(ph, (0, 0))
    vgrad(c, 430, 740, zemin, 0, 235); rect(c, (0, 740, W, H), zemin, alpha=235)
    vgrad(c, 0, 190, (0, 0, 0), 150, 0)
    logo(c, 60, 46, 50); pill(c, pill_yazi, 1020, 50, vurgu, KOYU_YAZI, 30)
    tracked(c, kicker, 60, 640, vurgu, 34, track=10)
    put(c, dev(dev_kelime, 250, WHITE, egik=True, track=3, maxw=960), 52, 668)
    y0 = 960
    rect(c, (539, y0, 541, y0 + 190), WHITE, alpha=60)
    for x, (etiket, metin, renk) in ((60, sol), (580, sag)):
        tracked(c, etiket, x, y0 + 14, renk, 30, track=9)
        yy = y0 + 48
        for satir in metin:
            l = dev(satir, 54, WHITE if renk != vurgu else vurgu, egik=False, track=2, maxw=440)
            put(c, l, x, yy); yy += l.height + 12
    tracked(c, bilgi, 60, 1212, ACIK, 30, track=5)
    rect(c, (60, 1262, 1020, 1264), WHITE, alpha=60)
    alt_bilgi(c, kaynak, 1302, sol_size=26)
    return kaydet(c, out)

soyledi_duzeltti("/mnt/user-data/uploads/01cd070b-image.jpg", "KRONİK?",
    "GALATASARAY  ·  MEHMET CİBARA",
    ("DİVAN KURULUNDA", ["“SAKATLIĞI", "KRONİK BİR ŞEY”"], (175, 178, 188)),
    ("SONRA DÜZELTTİ", ["“KRONİK", "HASTALIĞI YOK”"], SARI),
    "7 KASIM  ·  ARTROSKOPİK DİZ AMELİYATI  ·  2-3 HAFTA",
    "KAYNAK: FANATİK  ·  KARAR", "/home/claude/kontra-gorsel/g/osimhen_kronik.jpg")
print("ok")

import sys; sys.path.insert(0, "/home/claude/font")
from kontra_stil import *
from PIL import Image

def duoton_uclu(photo, renkler, kicker, baslik, alt, hucreler, kaynak, out, pill_yazi="RESMİ", yb=0.1, zemin=(16, 8, 10)):
    """Yeni düzen: ülke/takım renginde duoton foto, dev düz başlık + ince alt satır, altta 3 bilgi hücresi."""
    g, m, i, v = renkler
    c = Image.new("RGBA", (W, H), zemin + (255,))
    ph = duotone(cover(photo, W, 980, yb), g, i, m).convert("RGBA"); c.alpha_composite(ph, (0, 0))
    vgrad(c, 560, 980, zemin, 0, 255); vgrad(c, 0, 180, (0, 0, 0), 120, 0)
    logo(c, 60, 46, 50); pill(c, pill_yazi, 1020, 50, v, KOYU_YAZI, 30)
    tracked(c, kicker, 60, 700, v, 34, track=10)
    b = dev(baslik, 200, WHITE, egik=False, track=4, maxw=960); put(c, b, 56, 730)
    tracked(c, alt, 60, 730 + b.height + 40, ACIK, 32, track=5)
    y0, hw = 1035, 300
    for k, (et, dg) in enumerate(hucreler):
        x = 60 + k * (hw + 30)
        rect(c, (x, y0, x + hw, y0 + 4), v if k == len(hucreler) - 1 else WHITE, alpha=255 if k == len(hucreler) - 1 else 90)
        tracked(c, et, x, y0 + 40, (175, 178, 188), 28, track=8)
        put(c, dev(dg, 60, v if k == len(hucreler) - 1 else WHITE, egik=True, track=2, maxw=hw), x, y0 + 70)
    rect(c, (60, 1262, 1020, 1264), WHITE, alpha=60)
    alt_bilgi(c, kaynak, 1302, sol_size=26)
    return kaydet(c, out)

BELCIKA = ((22, 8, 10), (190, 20, 40), (253, 218, 36), (253, 218, 36))
duoton_uclu("/mnt/user-data/uploads/55ff0866-image.jpg", BELCIKA,
    "BELÇİKA  ·  VAN BOMMEL DOĞRULADI", "LUKAKU YOK",
    "TÜRKİYE MAÇI KADROSUNDA YER ALMADI, İZMİRE GETİRİLMEDİ",
    [("SAKATLIK", "KALÇA"), ("YERİNE", "KİMSE YOK"), ("HEDEF", "PAZAR")],
    "KAYNAK: SABAH  ·  TAKVİM  ·  AYDINLIK", "/home/claude/kontra-gorsel/g/lukaku_yok.jpg")
print("ok")

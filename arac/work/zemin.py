import sys; sys.path.insert(0, "/home/claude/font")
from kontra_stil import *
from PIL import Image, ImageEnhance

def alinti_karsi(photo, crop_box, foto_etiket, kicker, satir1, satir2, kim, hucreler, hucre_baslik,
                 kaynak, out, vurgu=SARI, zemin=SIYAH, pill_yazi="AÇIKLAMA"):
    """Yeni düzen: fotoğrafın ilgili parçası (crop_box) üstte, köşede etiket;
    altta dev alıntı + numaralı 3 hücre şeridi."""
    c = Image.new("RGBA", (W, H), zemin + (255,))
    src = Image.open(photo).convert("RGB").crop(crop_box)
    tmp = "/tmp/_alinti_crop.png"; src.save(tmp)
    ph = ImageEnhance.Contrast(cover(tmp, W, 720, 0.5)).enhance(1.1)
    c.paste(ph, (0, 0))
    vgrad(c, 470, 720, zemin, 0, 255); vgrad(c, 0, 190, (0, 0, 0), 150, 0)
    logo(c, 60, 46, 50); pill(c, pill_yazi, 1020, 50, vurgu, KOYU_YAZI, 30)
    # foto etiketi (sol alt, foto üzerinde)
    rect(c, (60, 560, 74, 600), vurgu)
    tracked(c, foto_etiket, 90, 580, WHITE, 30, track=8)
    tracked(c, kicker, 60, 668, vurgu, 34, track=9)
    put(c, dev("“" + satir1, 112, WHITE, egik=False, track=3), 52, 700)
    put(c, dev(satir2 + "”", 112, ACIK, egik=False, track=3), 60, 834)
    tracked(c, kim, 60, 990, GRI, 30, track=6)
    # hücreler
    tracked(c, hucre_baslik, 60, 1060, vurgu, 30, track=10)
    cw, gap, y0 = 300, 30, 1090
    for i, (no, ad) in enumerate(hucreler):
        x = 60 + i * (cw + gap)
        rect(c, (x, y0, x + cw, y0 + 130), WHITE, alpha=16, radius=12)
        rect(c, (x, y0, x + 6, y0 + 130), vurgu, radius=3)
        tracked(c, no, x + 30, y0 + 36, vurgu, 30, track=6)
        put(c, dev(ad, 54, WHITE, egik=True, track=2, maxw=cw - 50), x + 30, y0 + 64)
    rect(c, (60, 1262, 1020, 1264), WHITE, alpha=60)
    alt_bilgi(c, kaynak, 1302, sol_size=26)
    return kaydet(c, out)

alinti_karsi("/mnt/user-data/uploads/b5060b1e-image.jpg", (0, 0, 380, 401), "RAMS PARK ZEMİNİ",
             "GALATASARAY  ·  MEHMET CİBARA", "DİREKT BİR SUÇLU", "GÖREMEDİM",
             "ZEMİN ELEŞTİRİLERİNE YANIT",
             [("01", "ISITMA"), ("02", "VAKUM"), ("03", "DRENAJ")],
             "ZEMİNİN ALTINDAKİ 3 SİSTEM",
             "KAYNAK: MEHMET CİBARA AÇIKLAMASI", "/mnt/user-data/outputs/KONTRA_zemin_cibara.jpg")
print("ok")

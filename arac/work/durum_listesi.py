import sys; sys.path.insert(0, "/home/claude/font")
from kontra_stil import *
from pro import cover, vgrad, grain
from PIL import Image

def durum_listesi(photo, kicker, baslik, satirlar, alt_not, kaynak, out,
                  vurgu=KIRMIZI, zemin=(10, 14, 30), pill_yazi="AÇIKLAMA", yb=0.1):
    """Yeni düzen: üst yarı foto, altta etiket:değer satırları (durum raporu gibi).
    satirlar: [(etiket, deger, vurgulu_mu)]"""
    c = Image.new("RGBA", (W, H), zemin + (255,))
    c.paste(cover(photo, W, 760, yb), (0, 0))
    vgrad(c, 0, 220, (0, 0, 0), 170, 0)
    vgrad(c, 420, 760, zemin, 0, 255)
    logo(c, 60, 46, 50); pill(c, pill_yazi, 1020, 50, vurgu, WHITE, 30)
    rect(c, (48, 548, 60 + 21 * len(kicker) + 30, 592), zemin, alpha=215, radius=4)
    tracked(c, kicker, 60, 570, vurgu, 28, track=10)
    y = 600
    for t in baslik:
        r = dev(t, 112, WHITE, egik=True, track=2, maxw=960); put(c, r, 54, y); y += r.height + 8
    y += 34
    for et, deg, vur in satirlar:
        rect(c, (60, y, 1020, y + 1), WHITE, alpha=40)
        tracked(c, et, 60, y + 40, (150, 160, 185), 24, track=7)
        d = dev(deg, 52, vurgu if vur else WHITE, egik=False, track=2, maxw=640)
        put(c, d, 1020 - d.width, y + 14)
        y += 80
    rect(c, (60, y, 1020, y + 1), WHITE, alpha=40)
    tracked(c, alt_not, 60, y + 40, (150, 160, 185), 22, track=5)
    rect(c, (60, 1262, 1020, 1264), WHITE, alpha=60)
    alt_bilgi(c, kaynak, 1302, sol_size=26)
    grain(c, 6)
    return kaydet(c, out)

if __name__ == "__main__":
    durum_listesi("/home/claude/kontra-foto/foto/fransa_sirt_mbappe_dembele.jpg", "PAZAR 22.45  /  BORDEAUX",
        ["MBAPPE", "OYNAYACAK MI"],
        [("SAKATLIK", "ARKA ADALE", False), ("İTALYA MAÇI", "KADRODA YOKTU", False),
         ("ZIDANE", "CİDDİ DEĞİL", True), ("KARAR", "SAĞLIK KONTROLÜ SONRASI", False)],
        "THURAM, TCHOUAMENI VE KALULU KAMPTAN AYRILDI",
        "KAYNAK: TF1, FRANSIZ BASINI", "/home/claude/kontra-gorsel/g/mbappe_durum.jpg")
    print("ok")

import sys; sys.path.insert(0, "/home/claude/font")
from kontra_stil import *
from PIL import Image, ImageEnhance

def iki_ses(photo, ust_etiket, satirlar, konusan, ikinci_etiket, ikinci_soz, mac_satiri, kaynak, out,
            vurgu=KIRMIZI, zemin=(14, 6, 8), pill_yazi="MİLLİ TAKIM", yb=0.0):
    """Yeni düzen: ana söz dev satırlarla altta, ikinci sesin kısa sözü kırmızı çerçeveli kartta."""
    c = Image.new("RGBA", (W, H), zemin + (255,))
    im = cover(photo, W, H, yb).convert("RGB")
    im = ImageEnhance.Color(im).enhance(0.75); im = ImageEnhance.Brightness(im).enhance(0.85)
    c.paste(im, (0, 0))
    vgrad(c, 0, 200, (0, 0, 0), 170, 0)
    vgrad(c, 480, 760, zemin, 0, 240); rect(c, (0, 760, W, H), zemin, alpha=240)
    logo(c, 60, 46, 50); pill(c, pill_yazi, 1020, 50, vurgu, WHITE, 30)
    # maç şeridi üstte, logonun altında
    # ana söz
    tracked(c, ust_etiket, 60, 668, vurgu, 30, track=10)
    rect(c, (60, 700, 70, 700 + 138 * len(satirlar) - 30), vurgu)
    y = 692
    for t in satirlar:
        r = dev(t, 98, WHITE, egik=False, track=2, maxw=920); put(c, r, 92, y); y += 138
    tracked(c, konusan, 92, y + 16, (190, 190, 196), 26, track=8)
    # ikinci ses kartı
    ky = y + 46
    rect(c, (60, ky, 1020, ky + 76), WHITE, alpha=12)
    rect(c, (60, ky, 64, ky + 76), vurgu)
    tracked(c, ikinci_etiket, 84, ky + 38, (190, 190, 196), 24, track=6)
    s = dev(ikinci_soz, 50, WHITE, egik=True, track=1, maxw=560); put(c, s, 1000 - s.width, ky + 12)
    rect(c, (60, 1262, 1020, 1264), WHITE, alpha=60)
    alt_bilgi(c, kaynak, 1302, sol_size=26)
    return kaydet(c, out)

if __name__ == "__main__":
    iki_ses("/mnt/user-data/uploads/708d7f2e-image.jpg", "BU AKŞAM 20.00  ·  TÜRKİYE - BELÇİKA",
        ["HİÇBİR ZAMAN", "MÜCADELEDEN", "VAZGEÇMEDİM"], "ENES ÜNAL",
        "SERGEN YALÇIN", "SANTRFOR YANIMIZDA",
        "BU AKŞAM 20.00  ·  TÜRKİYE - BELÇİKA  ·  İZMİR",
        "KAYNAK: BASIN TOPLANTISI  ·  T24", "/home/claude/kontra-gorsel/g/enes_unal_milli.jpg")
    print("ok")

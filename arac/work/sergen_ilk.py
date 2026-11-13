import sys; sys.path.insert(0, "/home/claude/font")
from kontra_stil import *
from pro import duotone
from PIL import Image, ImageEnhance, ImageFilter

def ilk_mac_karti(photo, crop, kicker, skor, mac, rekor, rekor_alt, goller, kaynak, out,
                  vurgu=KIRMIZI, zemin=(10, 6, 7), pill_yazi="İSTATİSTİK", ust=640):
    c = Image.new("RGBA", (W, H), zemin + (255,))
    im = Image.open(photo).convert("RGB").crop(crop).resize((W, ust), Image.LANCZOS)
    im = im.filter(ImageFilter.UnsharpMask(2, 80, 2))
    im = duotone(im, (8, 4, 6), (245, 225, 220), (150, 20, 30))
    c.paste(im, (0, 0))
    vgrad(c, 0, 180, (0, 0, 0), 150, 0); vgrad(c, ust - 240, ust, zemin, 0, 255)
    logo(c, 60, 46, 50); pill(c, pill_yazi, 1020, 50, vurgu, WHITE, 30)
    tracked(c, kicker, 60, ust - 40, vurgu, 30, track=10)
    s = dev(skor, 230, WHITE, egik=True, track=4, maxw=600); put(c, s, 52, ust - 12)
    tracked(c, mac, 60 + s.width + 36, ust + s.height // 2 - 30, WHITE, 34, track=8)
    tracked(c, goller, 60 + s.width + 36, ust + s.height // 2 + 16, (190, 180, 184), 22, track=5)
    y = ust + s.height + 20
    rect(c, (60, y, 1020, y + 2), WHITE, alpha=50)
    r = dev(rekor, 66, vurgu, egik=False, track=2, maxw=960); put(c, r, 60, y + 30)
    tracked(c, rekor_alt, 60, y + 30 + r.height + 30, WHITE, 28, track=6)
    yy = y + 30 + r.height + 90
    rect(c, (60, yy, 1020, yy + 110), WHITE, alpha=10); rect(c, (60, yy, 64, yy + 110), vurgu)
    tracked(c, "BİR ÖNCEKİ ÖRNEK", 86, yy + 32, (170, 160, 164), 22, track=6)
    put(c, dev("EYLÜL 2017  ·  UKRAYNA 2-0 TÜRKİYE", 46, WHITE, egik=False, track=1, maxw=900), 86, yy + 50)
    rect(c, (60, 1262, 1020, 1264), WHITE, alpha=60)
    alt_bilgi(c, kaynak, 1302, sol_size=26)
    return kaydet(c, out)

if __name__ == "__main__":
    ilk_mac_karti("/mnt/user-data/uploads/d4b060e5-image.jpg", (80, 198, 580, 485),
        "SERGEN YALÇIN  ·  İLK MAÇ", "1-2", "TÜRKİYE - BELÇİKA",
        "LUCESCU DAN BU YANA BİR İLK", "İLK MAÇINI KAYBEDEN İLK MİLLİ TAKIM HOCASI",
        "ARDA 20  ·  DE BRUYNE 27  ·  DE KETELAERE 30",
        "ULUSLAR LİGİ  ·  İZMİR", "/home/claude/kontra-gorsel/g/sergen_ilkmac.jpg")
    print("ok")

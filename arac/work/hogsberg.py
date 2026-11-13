import sys; sys.path.insert(0, "/home/claude/font")
from kontra_stil import *
from PIL import Image

def profil_karti(photo, kicker, isim, alt_isim, hucreler, not_satiri, kaynak, out, vurgu=SARI,
                 zemin=(8, 14, 38), pill_yazi="İDDİA", ust=730):
    """Yeni düzen (yatay fotoğraf için): üst bant foto, altta scout kartı gibi profil ızgarası."""
    c = Image.new("RGBA", (W, H), zemin + (255,))
    im = Image.open(photo).convert("RGB")
    s = ust / im.height
    im = im.resize((int(im.width * s), ust), Image.LANCZOS)
    x0 = (im.width - W) // 2; im = im.crop((x0, 0, x0 + W, ust))
    c.paste(im, (0, 0))
    vgrad(c, 0, 180, (0, 0, 0), 150, 0)
    vgrad(c, ust - 200, ust, zemin, 0, 255)
    logo(c, 60, 46, 50); pill(c, pill_yazi, 1020, 50, vurgu, KOYU_YAZI, 30)
    tracked(c, kicker, 60, ust - 30, vurgu, 30, track=10)
    n = dev(isim, 124, WHITE, egik=True, track=2, maxw=960); put(c, n, 54, ust - 6)
    tracked(c, alt_isim, 62, ust + n.height + 18, (175, 185, 210), 28, track=8)
    # ızgara 3x2
    gy = ust + n.height + 54; cw = 960 // 3; ch = 132
    for k, (et, de) in enumerate(hucreler):
        r, col = divmod(k, 3)
        x = 60 + col * cw; y = gy + r * ch
        rect(c, (x, y, x + cw - 1, y + 1), WHITE, alpha=40)
        tracked(c, et, x + 4, y + 30, (150, 160, 190), 24, track=6)
        put(c, dev(de, 58, vurgu if k == 0 else WHITE, egik=False, track=1, maxw=cw - 20), x + 4, y + 50)
    tracked(c, not_satiri, 60, 1232, WHITE, 26, track=6)
    rect(c, (60, 1262, 1020, 1264), WHITE, alpha=60)
    alt_bilgi(c, kaynak, 1302, sol_size=26)
    return kaydet(c, out)

if __name__ == "__main__":
    profil_karti("/mnt/user-data/uploads/43590fb4-image.webp", "BELÖZOĞLU STOPER İSTEDİ", "HOGSBERG",
        "LUCAS HOGSBERG  ·  STRASBOURG  ·  DANİMARKA",
        [("BONSERVİS", "18M EURO"), ("YAŞ", "20"), ("BOY", "1.87"),
         ("SÖZLEŞME", "2030"), ("MEVKİ", "STOPER"), ("ALTERNATİF", "SAĞ  /  SOL BEK")],
        "FRANSIZ KULÜBÜYLE TEMAS KURULDU", "KAYNAK: FOTOMAÇ", "/home/claude/kontra-gorsel/g/hogsberg_fb.jpg")
    print("ok")

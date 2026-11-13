import sys; sys.path.insert(0, "/home/claude/font")
from kontra_stil import *
from PIL import Image, ImageDraw

def egik_bant(photo, kicker, bant_ust, bant_alt, maddeler, kaynak, out, vurgu=KIRMIZI, zemin=(12, 8, 9),
              pill_yazi="İDDİA", yb=0.3):
    """Yeni düzen: fotoğrafın alt üçte birini kesen eğik renkli bant, içinde iki satır başlık."""
    c = Image.new("RGBA", (W, H), zemin + (255,))
    c.paste(cover(photo, W, H, yb), (0, 0))
    vgrad(c, 0, 200, (0, 0, 0), 170, 0)
    vgrad(c, 700, 1000, zemin, 0, 235); rect(c, (0, 1000, W, H), zemin, alpha=235)
    # eğik bant
    band = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(band)
    d.polygon([(0, 862), (W, 800), (W, 1010), (0, 1072)], fill=vurgu + (240,))
    c.alpha_composite(band)
    logo(c, 60, 46, 50); pill(c, pill_yazi, 1020, 50, WHITE, KOYU_YAZI, 30)
    rect(c, (48, 748, 820, 796), zemin, alpha=215)
    tracked(c, kicker, 60, 772, WHITE, 28, track=9)
    a = dev(bant_ust, 64, (255, 225, 225), egik=True, track=3, maxw=900); put(c, a, 60, 862)
    b = dev(bant_alt, 112, WHITE, egik=True, track=2, maxw=960); put(c, b, 56, 862 + a.height + 2)
    y = 1110
    for t in maddeler:
        tracked(c, "/", 60, y + 12, vurgu, 28, track=0)
        tracked(c, t, 88, y + 12, WHITE, 27, track=6)
        y += 44
    rect(c, (60, 1262, 1020, 1264), WHITE, alpha=60)
    alt_bilgi(c, kaynak, 1302, sol_size=26)
    return kaydet(c, out)

if __name__ == "__main__":
    egik_bant("/mnt/user-data/uploads/dee46a07-image.jpg", "MAYISTA TRABZONSPOR İLE KUPA KALDIRMIŞTI",
        "FATİH TEKKE İÇİN", "YENİ DURAK GAZİANTEP",
        ["YÖNETİMLE ANLAŞMA SAĞLANDIĞI İDDİA EDİLİYOR", "CUMA GÜNÜNE KADAR ŞEHRE GELMESİ BEKLENİYOR", "KULÜPTEN HENÜZ RESMİ AÇIKLAMA YOK"],
        "KAYNAK: 61SAAT  ·  YEREL BASIN", "/home/claude/kontra-gorsel/g/tekke_antep.jpg")
    print("ok")

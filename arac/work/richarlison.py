import sys; sys.path.insert(0, "/home/claude/font")
from kontra_stil import *
from pro import duotone, alpha
from PIL import Image

def ikinci_deneme(photo, buyuk, kicker, baslik, bilgiler, kaynak, out, golge=(18, 10, 30),
                  orta=(120, 24, 52), isik=(150, 205, 240), vurgu=(110, 190, 240), pill_yazi="İDDİA", yb=0.0):
    """Yeni düzen: kulüp renklerinde duoton foto, arkada dev yarı saydam rakam, altta noktalı bilgi satırları."""
    c = Image.new("RGBA", (W, H), golge + (255,))
    im = cover(photo, W, H, yb).convert("RGB")
    im = duotone(im, golge, isik, orta)
    c.paste(im, (0, 0))
    g = dev(buyuk, 900, WHITE, egik=True, track=0, maxw=700); g = alpha(g, 40)
    put(c, g, -40, 120)
    vgrad(c, 0, 200, (0, 0, 0), 150, 0)
    vgrad(c, 780, 1020, golge, 0, 240); rect(c, (0, 1020, W, H), golge, alpha=240)
    logo(c, 60, 46, 50); pill(c, pill_yazi, 1020, 50, vurgu, KOYU_YAZI, 30)
    tracked(c, kicker, 60, 900, vurgu, 32, track=10)
    b = dev(baslik, 132, WHITE, egik=True, track=2, maxw=960); put(c, b, 56, 924)
    y = 924 + b.height + 30
    for t in bilgiler:
        rect(c, (60, y + 8, 72, y + 20), vurgu)
        tracked(c, t, 90, y + 14, WHITE, 28, track=6)
        y += 44
    rect(c, (60, 1262, 1020, 1264), WHITE, alpha=60)
    alt_bilgi(c, kaynak, 1302, sol_size=26)
    return kaydet(c, out)

if __name__ == "__main__":
    ikinci_deneme("/mnt/user-data/uploads/61dc352e-image.jpg", "2", "YAZIN OLMADI, OCAKTA", "İKİNCİ DENEME",
        ["TOTTENHAM İLE ŞARTLAR İÇİN TEMAS", "SÖZLEŞMESİ HAZİRAN 2027 DE BİTİYOR", "OYUNCUNUN TRANSFERE SICAK BAKTIĞI BELİRTİLİYOR"],
        "KAYNAK: SPORX", "/home/claude/kontra-gorsel/g/richarlison_ts.jpg")
    print("ok")

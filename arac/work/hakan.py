import sys; sys.path.insert(0, "/home/claude/font")
from kontra_stil import *
from PIL import Image

def kutu_seridi(photo, kicker, satir1, satir2, kutular, kaynak, out, vurgu=SARI, zemin=(7, 13, 36),
                pill_yazi="İDDİA", yb=0.1):
    """Yeni düzen: tam foto, altta iki tonlu başlık ve çerçeveli üç bilgi kutusu."""
    c = Image.new("RGBA", (W, H), zemin + (255,))
    c.paste(cover(photo, W, H, yb), (0, 0))
    vgrad(c, 0, 220, (0, 0, 0), 170, 0)
    vgrad(c, 640, 930, zemin, 0, 235); rect(c, (0, 930, W, H), zemin, alpha=235)
    logo(c, 60, 46, 50); pill(c, pill_yazi, 1020, 50, vurgu, KOYU_YAZI, 30)
    tracked(c, kicker, 60, 756, vurgu, 30, track=10)
    a = dev(satir1, 120, vurgu, egik=True, track=2, maxw=960); put(c, a, 56, 780)
    b = dev(satir2, 120, WHITE, egik=True, track=2, maxw=960); put(c, b, 56, 796 + a.height + 14)
    y = 796 + a.height + b.height + 40
    n = len(kutular); g = 16; kw = (960 - g * (n - 1)) // n; kh = 128
    for k, (ust, alt) in enumerate(kutular):
        x = 60 + k * (kw + g)
        rect(c, (x, y, x + kw, y + kh), WHITE, alpha=14)
        rect(c, (x, y, x + kw, y + 3), vurgu)
        tracked(c, ust, x + 18, y + 34, (170, 178, 200), 24, track=5)
        put(c, dev(alt, 48, WHITE, egik=False, track=1, maxw=kw - 36), x + 18, y + 58)
    rect(c, (60, 1262, 1020, 1264), WHITE, alpha=60)
    alt_bilgi(c, kaynak, 1302, sol_size=26)
    return kaydet(c, out)

if __name__ == "__main__":
    kutu_seridi("/mnt/user-data/uploads/f6d938c8-image.jpg", "BELÖZOĞLU LİSTESİNDE", "HEDEF", "MİLLİ KAPTAN",
        [("INTER SÖZLEŞMESİ", "YAZIN BİTİYOR"), ("UZATMA", "ANLAŞMA YOK"), ("PLAN", "OCAK AYI")],
        "KAYNAK: FANATİK", "/home/claude/kontra-gorsel/g/hakan_fb.jpg")
    print("ok")

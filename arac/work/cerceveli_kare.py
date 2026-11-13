import sys; sys.path.insert(0, "/home/claude/font")
from kontra_stil import *
from pro import cover, vgrad, grain
from PIL import Image, ImageFilter

def cerceveli_kare(photo, rakam, birim, kicker, baslik, maddeler, kaynak, out,
                   vurgu=SARI, zemin=(12, 14, 24), pill_yazi="İDDİA", aksan=(240, 120, 30)):
    """Yeni düzen (küçük/kare fotolar için): bulanık foto zemin + çerçeveli kare foto, sağda dev rakam."""
    c = Image.new("RGBA", (W, H), zemin + (255,))
    bg = cover(photo, W, H, 0.3).filter(ImageFilter.GaussianBlur(28))
    c.paste(bg, (0, 0)); rect(c, (0, 0, W, H), zemin, alpha=200)
    logo(c, 60, 46, 50); pill(c, pill_yazi, 1020, 50, vurgu, KOYU_YAZI, 30)
    S = 600; x0, y0 = 60, 150
    rect(c, (x0 + 18, y0 + 18, x0 + S + 18, y0 + S + 18), aksan)
    c.paste(cover(photo, S, S, 0.2), (x0, y0))
    r = dev(rakam, 300, vurgu, egik=True, track=0, maxw=360)
    put(c, r, 1030, 230, align="right")
    put(c, dev(birim, 64, WHITE, egik=False, track=2, maxw=340), 1030, 230 + r.height + 14, align="right")
    tracked(c, "GÖZDEN ÇIKARILAN", 1030, 230 + r.height + 120, (170, 175, 195), 24, track=8, align="right")
    y = y0 + S + 70
    tracked(c, kicker, 60, y, vurgu, 28, track=10); y += 26
    for t in baslik:
        d = dev(t, 96, WHITE, egik=True, track=2, maxw=960); put(c, d, 54, y); y += d.height + 6
    y += 22
    for t in maddeler:
        rect(c, (60, y + 8, 70, y + 18), vurgu)
        tracked(c, t, 86, y + 13, (200, 204, 214), 26, track=6); y += 44
    rect(c, (60, 1262, 1020, 1264), WHITE, alpha=60)
    alt_bilgi(c, kaynak, 1302, sol_size=26)
    grain(c, 7)
    return kaydet(c, out)

if __name__ == "__main__":
    cerceveli_kare("/home/claude/kontra-foto/foto/marlon_gomes_shakhtar.jpg", "20", "MİLYON EURO",
        "FENERBAHÇE  /  ORTA SAHA", ["HEDEF MARLON", "GOMES"],
        ["İLK GÖRÜŞME 25 KASIM", "EMRE BELÖZOĞLU - ARDA TURAN MASASI", "RESMİ AÇIKLAMA YOK"],
        "KAYNAK: FOTOMAÇ", "/home/claude/kontra-gorsel/g/marlon_gomes_fb.jpg")
    print("ok")

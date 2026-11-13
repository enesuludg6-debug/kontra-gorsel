import sys; sys.path.insert(0, "/home/claude/font")
from kontra_stil import *
from pro import cover, vgrad, grain
from PIL import Image

def yarim_cizgili(photo, kicker, baslik, maddeler, kaynak, out, vurgu=WHITE, pill_yazi="İDDİA", yb=0.2):
    """Yeni düzen: sol yarı dikey foto, sağ yarı siyah-beyaz ince çizgili zemin üzerinde metin (BJK gibi çizgili kulüpler)."""
    c = Image.new("RGBA", (W, H), (8, 8, 8, 255))
    for x in range(540, W, 36): rect(c, (x, 0, x + 12, H), WHITE, alpha=22)
    c.paste(cover(photo, 540, H, yb), (0, 0))
    for i in range(120): rect(c, (420 + i, 0, 421 + i, H), (8, 8, 8), alpha=int(255 * i / 120))
    rect(c, (540, 0, 548, H), WHITE)
    vgrad(c, 0, 200, (0, 0, 0), 160, 0, 0, 540)
    logo(c, 60, 46, 50); pill(c, pill_yazi, 1020, 50, WHITE, KOYU_YAZI, 30)
    x = 590; y = 330
    tracked(c, kicker, x, y, (200, 200, 200), 26, track=9); y += 34
    for t in baslik:
        d = dev(t, 104, WHITE, egik=True, track=2, maxw=W - x - 50); put(c, d, x - 4, y); y += d.height + 8
    y += 40
    for t in maddeler:
        rect(c, (x, y + 8, x + 10, y + 18), WHITE)
        tracked(c, t, x + 26, y + 13, (215, 215, 215), 24, track=5); y += 46
    vgrad(c, 1150, 1240, (8, 8, 8), 0, 235, 0, 540); rect(c, (0, 1240, 540, H), (8, 8, 8), alpha=235)
    rect(c, (60, 1262, 1020, 1264), WHITE, alpha=60)
    alt_bilgi(c, kaynak, 1302, sol_size=26)
    grain(c, 6)
    return kaydet(c, out)

if __name__ == "__main__":
    yarim_cizgili("/home/claude/kontra-foto/foto/oumar_solet_udinese.jpg", "BEŞİKTAŞ  /  STOPER",
        ["HEDEF", "OUMAR", "SOLET"], ["UDINESE, 26 YAŞINDA", "TEMSİLCİLERİYLE İLK TEMAS", "SÖZLEŞMESİ SEZON SONU BİTİYOR", "ARA TRANSFER PLANI"],
        "KAYNAK: NEFES", "/home/claude/kontra-gorsel/g/solet_bjk.jpg")
    print("ok")

import sys; sys.path.insert(0, "/home/claude/font")
from kontra_stil import *
from pro import cover, vgrad, grain
from PIL import Image

def soru_cevap(photo, soru, cevap, konusan, kaynak, out, vurgu=SARI, zemin=(24, 6, 10), pill_yazi="AÇIKLAMA", yb=0.25):
    """Yeni düzen: üstte foto, altta röportaj gibi SORU (soluk, küçük) + CEVAP (dev, vurgulu) blokları."""
    c = Image.new("RGBA", (W, H), zemin + (255,))
    c.paste(cover(photo, W, 760, yb), (0, 0))
    vgrad(c, 0, 200, (0, 0, 0), 150, 0); vgrad(c, 460, 760, zemin, 0, 255)
    logo(c, 60, 46, 50); pill(c, pill_yazi, 1020, 50, vurgu, KOYU_YAZI, 30)
    y = 670
    rect(c, (60, y, 112, y + 52), WHITE, alpha=40, radius=6)
    tracked(c, "S", 86, y + 26, WHITE, 30, track=0, align="center")
    for t in soru:
        tracked(c, t, 140, y + 26, (190, 180, 185), 26, track=5); y += 44
    y += 30
    rect(c, (60, y, 112, y + 52), vurgu, radius=6)
    tracked(c, "C", 86, y + 26, KOYU_YAZI, 30, track=0, align="center")
    tracked(c, konusan, 140, y + 26, vurgu, 26, track=8); y += 70
    for t in cevap:
        d = dev(t, 92, WHITE, egik=True, track=2, maxw=960); put(c, d, 54, y); y += d.height + 8
    rect(c, (60, 1262, 1020, 1264), WHITE, alpha=60)
    alt_bilgi(c, kaynak, 1302, sol_size=26)
    grain(c, 6)
    return kaydet(c, out)

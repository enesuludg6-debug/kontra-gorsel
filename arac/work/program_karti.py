import sys; sys.path.insert(0, "/home/claude/font")
from kontra_stil import *
from pro import cover, vgrad, grain
from PIL import Image

def program_karti(photo, kicker, baslik, maclar, alt_not, kaynak, out, vurgu=SARI, zemin=(12, 12, 18),
                  pill_yazi="PROGRAM", yb=0.3):
    """Yeni düzen: üstte foto, altta tarih kutusu + maç + stat satırları (fikstür kartı)."""
    c = Image.new("RGBA", (W, H), zemin + (255,))
    c.paste(cover(photo, W, 700, yb), (0, 0))
    vgrad(c, 0, 200, (0, 0, 0), 150, 0); vgrad(c, 420, 700, zemin, 0, 255)
    logo(c, 60, 46, 50); pill(c, pill_yazi, 1020, 50, vurgu, KOYU_YAZI, 30)
    rect(c, (48, 538, 60 + 21 * len(kicker) + 30, 582), zemin, alpha=215, radius=4)
    tracked(c, kicker, 60, 560, vurgu, 28, track=10)
    y = 590
    for t in baslik:
        r = dev(t, 96, WHITE, egik=True, track=2, maxw=960); put(c, r, 54, y); y += r.height + 6
    y += 34
    for gun, ay, mac, stat, final in maclar:
        rect(c, (60, y, 190, y + 130), vurgu if final else (40, 40, 52), radius=8)
        g = dev(gun, 72, KOYU_YAZI if final else WHITE, egik=False, track=1, maxw=120); put(c, g, 125 - g.width // 2, y + 14)
        tracked(c, ay, 125, y + 108, KOYU_YAZI if final else (190, 190, 200), 22, track=6, align="center")
        m = dev(mac, 60, vurgu if final else WHITE, egik=False, track=2, maxw=800); put(c, m, 220, y + 16)
        tracked(c, stat, 222, y + 106, (180, 182, 195), 24, track=6)
        y += 150
    tracked(c, alt_not, 60, y + 14, (180, 182, 195), 22, track=5)
    rect(c, (60, 1262, 1020, 1264), WHITE, alpha=60)
    alt_bilgi(c, kaynak, 1302, sol_size=26)
    grain(c, 6)
    return kaydet(c, out)

if __name__ == "__main__":
    program_karti("/home/claude/kontra-foto/foto/supercopa_kupa.jpg", "İSPANYA SÜPER KUPASI  /  İSTANBUL",
        ["DEVLER İSTANBULDA"],
        [("2", "ŞUBAT", "BARCELONA - ATLETICO MADRID", "CHOBANI STADYUMU  /  22.00", False),
         ("3", "ŞUBAT", "REAL SOCIEDAD - REAL MADRID", "TÜPRAŞ STADYUMU  /  22.00", False),
         ("6", "ŞUBAT", "FİNAL", "RAMS PARK", True)],
        "TÜM MAÇLAR HT SPOR DA ŞİFRESİZ",
        "KAYNAK: RFEF, TFF", "/home/claude/kontra-gorsel/g/supercopa_istanbul.jpg")
    print("ok")

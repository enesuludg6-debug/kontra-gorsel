import sys; sys.path.insert(0, "/home/claude/font")
from kontra_stil import *
from pro import cover, vgrad, grain
from PIL import Image

def manset_seridi(photo, kicker, baslik, mansetler, kaynak, out, vurgu=KIRMIZI, zemin=(12, 10, 12),
                  pill_yazi="MİLLİ", yb=0.2):
    """Yeni düzen: tam foto, altta gazete manşeti gibi beyaz şeritler (yayın adı + kısa başlık)."""
    c = Image.new("RGBA", (W, H), zemin + (255,))
    c.paste(cover(photo, W, H, yb), (0, 0))
    vgrad(c, 0, 220, (0, 0, 0), 170, 0)
    vgrad(c, 480, 760, zemin, 0, 235); rect(c, (0, 760, W, H), zemin, alpha=235)
    logo(c, 60, 46, 50); pill(c, pill_yazi, 1020, 50, vurgu, WHITE, 30)
    rect(c, (48, 618, 60 + 21 * len(kicker) + 30, 662), zemin, alpha=215, radius=4)
    tracked(c, kicker, 60, 640, vurgu, 28, track=10)
    y = 668
    for t in baslik:
        r = dev(t, 104, WHITE, egik=True, track=2, maxw=960); put(c, r, 54, y); y += r.height + 6
    y += 34
    for i, (yayin, metin) in enumerate(mansetler):
        x0 = 60 + i * 18
        rect(c, (x0, y, 1020, y + 112), (244, 241, 234), radius=4)
        rect(c, (x0, y, x0 + 10, y + 112), vurgu)
        tracked(c, yayin, x0 + 34, y + 30, vurgu, 24, track=8)
        d = dev(metin, 46, (20, 20, 24), egik=False, track=2, maxw=1020 - x0 - 60); put(c, d, x0 + 32, y + 50)
        y += 132
    rect(c, (60, 1262, 1020, 1264), WHITE, alpha=60)
    alt_bilgi(c, kaynak, 1302, sol_size=26)
    grain(c, 6)
    return kaydet(c, out)

if __name__ == "__main__":
    manset_seridi("/home/claude/kontra-foto/foto/milli_8_sut_euro2024.jpg", "ARDA GÜLER  /  20. DAKİKA FRİKİK",
        ["AVRUPA BU GOLÜ", "KONUŞUYOR"],
        [("AS  /  İSPANYA", "BECKHAM TARZI İNANILMAZ VURUŞ"), ("FOOT MERCATO  /  FRANSA", "GÜLERE RAĞMEN TÜRKİYE YENİLDİ")],
        "KAYNAK: AS, FOOT MERCATO", "/home/claude/kontra-gorsel/g/arda_basin.jpg")
    print("ok")

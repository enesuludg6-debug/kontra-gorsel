import sys; sys.path.insert(0, "/home/claude/font")
from kontra_stil import *
from PIL import Image, ImageEnhance

def mac_istatistik(photo, kicker, dev_deger, dev_birim, baslik, satirlar, takimlar, kaynak, out,
                   vurgu=KIRMIZI, zemin=(12, 8, 10), pill_yazi="İLK 30 DK", ust=700, yb=0.42):
    c = Image.new("RGBA", (W, H), zemin + (255,))
    im = cover(photo, W, ust, yb).convert("RGB")
    im = ImageEnhance.Color(im).enhance(0.8); c.paste(im, (0, 0))
    vgrad(c, 0, 190, (0, 0, 0), 160, 0)
    vgrad(c, ust - 300, ust, zemin, 0, 255)
    logo(c, 60, 46, 50); pill(c, pill_yazi, 1020, 50, vurgu, WHITE, 30)
    tracked(c, kicker, 60, ust - 150, WHITE, 28, track=9)
    d = dev(dev_deger, 190, vurgu, egik=True, track=2, maxw=520); put(c, d, 52, ust - 128)
    tracked(c, dev_birim, 60 + d.width + 26, ust - 128 + d.height // 2 - 18, WHITE, 40, track=8)
    tracked(c, baslik, 60, ust - 128 + d.height + 34, (200, 196, 198), 26, track=6)
    # takım başlıkları
    y = ust + 190
    tracked(c, takimlar[0], 60, y, vurgu, 28, track=8)
    tracked(c, takimlar[1], 1020, y, (200, 196, 198), 28, track=8, align="right")
    y += 40
    for ad, a, b, fa, fb in satirlar:
        tracked(c, ad, W // 2, y + 6, (170, 166, 170), 24, track=7, align="center")
        put(c, dev(fa, 60, WHITE, egik=False, track=1), 60, y - 16)
        r = dev(fb, 60, WHITE, egik=False, track=1); put(c, r, 1020 - r.width, y - 16)
        top = a + b; bw = 960; sol = int(bw * a / top)
        rect(c, (60, y + 58, 60 + sol - 4, y + 72), vurgu)
        rect(c, (60 + sol + 4, y + 58, 1020, y + 72), WHITE, alpha=90)
        y += 170
    rect(c, (60, 1262, 1020, 1264), WHITE, alpha=60)
    alt_bilgi(c, kaynak, 1302, sol_size=26)
    return kaydet(c, out)

if __name__ == "__main__":
    mac_istatistik("/home/claude/kontra-foto/foto/milli_takim_gol_sevinci.jpg", "TOP BİZDE, POZİSYON YOK",
        "0.07", "xG", "İLK 30 DAKİKADA ÜRETİLEN GOL BEKLENTİSİ",
        [("TOPA SAHİP OLMA", 56, 44, "%56", "%44"), ("PAS", 169, 122, "169", "122")],
        ("TÜRKİYE", "BELÇİKA"), "TÜRKİYE - BELÇİKA  ·  ULUSLAR LİGİ", "/home/claude/work/out_ilk30.jpg")
    print("ok")

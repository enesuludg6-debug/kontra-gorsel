import sys; sys.path.insert(0, "/home/claude/font")
from kontra_stil import *
from pro import cover, grain
from PIL import Image, ImageDraw

def polaroid(photo, alt_yazi, kicker, baslik, satir, kaynak, out, renk1=(150, 20, 30), renk2=(200, 140, 20),
             zemin=(14, 10, 10), vurgu=SARI, pill_yazi="İDDİA", aci=-5):
    """Yeni düzen (çok küçük fotolar için): iki renkli çapraz zemin + eğik polaroid kart."""
    c = Image.new("RGBA", (W, H), zemin + (255,))
    d = ImageDraw.Draw(c)
    d.polygon([(0, 0), (W, 0), (W, 380), (0, 760)], fill=renk1 + (255,))
    d.polygon([(0, 760), (W, 380), (W, 470), (0, 850)], fill=renk2 + (255,))
    rect(c, (0, 0, W, H), (0, 0, 0), alpha=90)
    logo(c, 60, 46, 50); pill(c, pill_yazi, 1020, 50, vurgu, KOYU_YAZI, 30)
    pw, ph = 470, 600
    card = Image.new("RGBA", (pw + 40, ph + 130), (245, 242, 235, 255))
    card.paste(cover(photo, pw, ph, 0.2), (20, 20))
    cd = dev(alt_yazi, 44, (30, 30, 34), egik=False, track=3, maxw=pw); card.alpha_composite(cd, ((pw + 40 - cd.width) // 2, ph + 50))
    card = card.rotate(aci, expand=True, resample=Image.BICUBIC)
    sh = Image.new("RGBA", card.size, (0, 0, 0, 0)); sh.putalpha(card.getchannel("A").point(lambda v: v * 120 // 255))
    cx = (W - card.width) // 2
    c.alpha_composite(sh, (cx + 14, 150 + 18)); c.alpha_composite(card, (cx, 150))
    y = 150 + card.height + 30
    tracked(c, kicker, W // 2, y, vurgu, 28, track=10, align="center"); y += 30
    for t in baslik:
        r = dev(t, 96, WHITE, egik=True, track=2, maxw=960); put(c, r, (W - r.width) // 2, y); y += r.height + 6
    tracked(c, satir, W // 2, y + 30, (205, 200, 205), 26, track=6, align="center")
    rect(c, (60, 1262, 1020, 1264), WHITE, alpha=60)
    alt_bilgi(c, kaynak, 1302, sol_size=26)
    grain(c, 7)
    return kaydet(c, out)

if __name__ == "__main__":
    polaroid("/home/claude/kontra-foto/foto/bruno_fernandes_manu.jpg", "BRUNO FERNANDES", "GALATASARAY TAKİPTE",
        ["AYRILIĞI KAFASINA", "KOYDU"], "MANCHESTER UNITED  /  RESMİ AÇIKLAMA YOK",
        "KAYNAK: FOTOMAÇ", "/home/claude/kontra-gorsel/g/bruno_gs.jpg")
    print("ok")

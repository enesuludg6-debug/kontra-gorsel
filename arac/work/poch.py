import sys; sys.path.insert(0, "/home/claude/font")
from kontra_stil import *
from PIL import Image, ImageDraw
from pro import alpha

def sira_listesi(cut, kicker, isimler, son_isim, alt_satir, kaynak, out, vurgu=KIRMIZI,
                 zemin=(16, 7, 9), pill_yazi="ANLAŞMA", olcek=1.0, dx=0, ghost="8"):
    """Yeni düzen: solda 1'den n'e soluk isim listesi, sonuncusu dev ve renkli; sağda dekupe."""
    c = Image.new("RGBA", (W, H), zemin + (255,))
    # sağdan kırmızımsı ışık
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(glow)
    for i in range(40):
        a = int(3 + i * 0.9)
        r = 760 - i * 16
        d.ellipse((760 - r, 520 - r, 760 + r, 520 + r), fill=vurgu + (a,))
    c.alpha_composite(glow)
    # dev hayalet rakam
    g = dev(ghost, 1250, vurgu, egik=True, track=0, maxw=900)
    g = alpha(g, 70); put(c, g, 1110 - g.width, 60)
    # dekupe
    p = Image.open(cut).convert("RGBA")
    p = p.crop((0, 0, p.width, int(p.height * 0.86)))  # alt köşe filigranı dışarıda
    s = 1180 / p.height * olcek
    p = p.resize((int(p.width * s), int(p.height * s)), Image.LANCZOS)
    c.alpha_composite(p, (W - p.width + 110 + dx, H - 170 - p.height))
    vgrad(c, 980, 1180, zemin, 0, 255); rect(c, (0, 1180, W, H), zemin, alpha=255)
    vgrad(c, 0, 200, (0, 0, 0), 160, 0)
    logo(c, 60, 46, 50); pill(c, pill_yazi, 1020, 50, vurgu, WHITE, 30)
    # liste
    tracked(c, kicker, 60, 200, vurgu, 32, track=10)
    y = 252
    for k, ad in enumerate(isimler, 1):
        tracked(c, f"{k}", 60, y + 22, (120, 112, 116), 30, track=2)
        put(c, dev(ad, 50, (205, 200, 204), egik=False, track=2, maxw=440), 108, y)
        y += 76
    rect(c, (60, y + 8, 300, y + 12), vurgu)
    tracked(c, f"{len(isimler) + 1}", 60, y + 70, vurgu, 44, track=2)
    put(c, dev(son_isim, 112, WHITE, egik=True, track=2, maxw=560), 112, y + 22)
    tracked(c, alt_satir, 60, 1228, WHITE, 32, track=8)
    rect(c, (60, 1262, 1020, 1264), WHITE, alpha=60)
    alt_bilgi(c, kaynak, 1302, sol_size=26)
    return kaydet(c, out)

if __name__ == "__main__":
    sira_listesi("poch_cut.png", "FERGUSON SONRASI",
        ["MOYES", "VAN GAAL", "MOURINHO", "SOLSKJAER", "TEN HAG", "AMORIM", "CARRICK"],
        "POCHETTINO", "İLK SINAV: ANFIELD  ·  22 KASIM",
        "KAYNAK: SKY SPORTS  ·  TEAMTALK", "/home/claude/kontra-gorsel/g/pochettino_8.jpg", dx=50)
    print("ok")

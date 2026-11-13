import sys; sys.path.insert(0, "/home/claude/font")
from kontra_stil import *
from pro import alpha
from PIL import Image, ImageOps, ImageEnhance

def dakika_cubugu(photo, kicker, rakam, birim, ara_baslik, ara_deger, parcalar, kaynak, out,
                  vurgu=SARI, zemin=(10, 14, 10), pill_yazi="İDDİA", kaydir=230, olcek=0.95):
    """Yeni düzen: foto sağa kaydırılır (ayna dolgulu), solda dev sayı; altta oyuncu payları çubuğu."""
    im = Image.open(photo).convert("RGB")
    s = H / im.height * olcek * 1.06
    im = im.resize((int(im.width * s), int(im.height * s)), Image.LANCZOS)
    pad = ImageOps.mirror(im.crop((0, 0, kaydir + 40, im.height)))
    big = Image.new("RGB", (im.width + pad.width, im.height))
    big.paste(pad, (0, 0)); big.paste(im, (pad.width, 0))
    x0 = pad.width - kaydir + (im.width - W) // 2 - 40
    big = big.crop((x0, 0, x0 + W, H))
    big = ImageEnhance.Color(big).enhance(0.8); big = ImageEnhance.Brightness(big).enhance(0.72)
    c = Image.new("RGBA", (W, H), zemin + (255,)); c.paste(big, (0, 0))
    # soldan karartma
    for i in range(0, 620, 4):
        a = int(215 * (1 - i / 620) ** 1.4)
        rect(c, (i, 0, i + 4, H), zemin, alpha=a)
    vgrad(c, 0, 180, (0, 0, 0), 150, 0)
    vgrad(c, 900, 1060, zemin, 0, 245); rect(c, (0, 1060, W, H), zemin, alpha=245)
    logo(c, 60, 46, 50); pill(c, pill_yazi, 1020, 50, vurgu, KOYU_YAZI, 30)
    tracked(c, kicker, 60, 210, vurgu, 32, track=10)
    r = dev(rakam, 330, vurgu, egik=True, track=3, maxw=560); put(c, r, 52, 238)
    put(c, dev(birim, 96, WHITE, egik=True, track=2, maxw=520), 60, 238 + r.height + 6)
    yb = 238 + r.height + 130
    tracked(c, ara_baslik, 60, yb + 20, (190, 196, 190), 30, track=8)
    put(c, dev(ara_deger, 96, WHITE, egik=False, track=2, maxw=520), 60, yb + 46)
    # çubuk
    top = sum(p[1] for p in parcalar); x = 60; bw = 960
    renkler = [vurgu, WHITE, ACIK]
    for k, (ad, dk, satir) in enumerate(parcalar):
        w = int(bw * dk / top)
        rect(c, (x, 1092, x + w - (4 if k < len(parcalar) - 1 else 0), 1108), renkler[k])
        x += w
    sol, sag = parcalar[0], parcalar[-1]
    put(c, dev(sol[0], 54, vurgu, egik=False, track=2, maxw=460), 60, 1126)
    tracked(c, sol[2], 60, 1212, WHITE, 26, track=6)
    l = dev(sag[0], 54, WHITE, egik=False, track=2, maxw=460); put(c, l, 1020 - l.width, 1126)
    tracked(c, sag[2], 1020, 1212, WHITE, 26, track=6, align="right")
    rect(c, (60, 1256, 1020, 1258), WHITE, alpha=60)
    alt_bilgi(c, kaynak, 1300, sol_size=26)
    return kaydet(c, out)

if __name__ == "__main__":
    dakika_cubugu("/mnt/user-data/uploads/d45525ec-image.jpg", "İKİ KİRALIK, TOPLAM", "145", "DAKİKA",
        "SATIN ALMA OPSİYONLARI", "50 MİLYON EURO",
        [("UGOCHUKWU", 123, "7 MAÇ  ·  123 DK  ·  22.5M EURO"), ("BITSHIABU", 22, "1 MAÇ  ·  22 DK  ·  28M EURO")],
        "KAYNAK: TRT SPOR  ·  FOTOMAÇ", "/home/claude/kontra-gorsel/g/gs_145dk.jpg")
    print("ok")

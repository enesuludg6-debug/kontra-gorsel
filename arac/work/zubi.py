import sys; sys.path.insert(0, "/home/claude/font")
from kontra_stil import *
from PIL import Image, ImageEnhance

def arka_yazi_kesik(photo, cut, arka, kicker, satir1, satir2, kartlar, kaynak, out,
                    pill_yazi="AÇIKLAMA", vurgu=KIRMIZI, yb=0.0, arka_y=190, dx=250):
    """Yeni düzen: karartılmış foto + oyuncunun ARKASINDA dev eğik kelime + kesik oyuncu önde,
    altta alıntı başlık ve iki hücreli karşılaştırma bandı (son hücre vurgulu)."""
    c = Image.new("RGBA", (W, H), LACI_SIYAH + (255,))
    ph = cover(photo, W, H, yb)
    ph = ImageEnhance.Brightness(ImageEnhance.Color(ph).enhance(0.5)).enhance(0.38)
    from PIL import ImageOps
    c.paste(ImageOps.mirror(ph), (dx - W, 0)); c.paste(ph, (dx, 0))
    # dev kelime oyuncunun arkasında (sol, iki satır)
    y = arka_y
    for sat in arka:
        l = dev(sat, 260, vurgu, egik=True, track=3, maxw=600); put(c, l, 50, y); y += l.height + 18
    # kesik oyuncu önde (foto ile aynı kırpma)
    cu = Image.open(cut).convert("RGBA")
    sc = max(W / cu.width, H / cu.height)
    cu = cu.resize((int(cu.width * sc + .5), int(cu.height * sc + .5)), Image.LANCZOS)
    x0 = (cu.width - W) // 2; y0 = int((cu.height - H) * yb)
    c.alpha_composite(cu.crop((x0, y0, x0 + W - dx, y0 + H)), (dx, 0))
    vgrad(c, 640, 900, LACI_SIYAH, 0, 255); rect(c, (0, 900, W, H), LACI_SIYAH)
    vgrad(c, 0, 180, (0, 0, 0), 130, 0)
    logo(c, 60, 46, 50); pill(c, pill_yazi, 1020, 50, vurgu, WHITE, 30)
    tracked(c, kicker, 60, 842, vurgu, 36, track=10)
    put(c, dev(satir1, 92, WHITE, egik=False, track=3), 60, 872)
    put(c, dev(satir2, 92, ACIK, egik=False, track=3), 60, 978)
    # karşılaştırma bandı
    y0b = 1112
    rect(c, (540, y0b, 542, y0b + 120), WHITE, alpha=60)
    for i, (n, l1, l2) in enumerate(kartlar):
        x = 60 if i == 0 else 580
        son = i == len(kartlar) - 1
        nl = dev(n, 104, vurgu if son else WHITE, egik=True, track=1, maxw=240)
        put(c, nl, x, y0b + 60, valign="middle")
        tracked(c, l1, x + nl.width + 22, y0b + 40, (185, 190, 202) if not son else vurgu, 30, track=6)
        tracked(c, l2, x + nl.width + 22, y0b + 80, WHITE, 32, track=5)
    rect(c, (60, 1268, 1020, 1270), WHITE, alpha=60)
    alt_bilgi(c, kaynak, 1305, sol_size=26)
    return kaydet(c, out)

arka_yazi_kesik("zubi.jpg", "zubi_cut.png", ("HAZİRANA", "KADAR?"), "MARTÍN ZUBİMENDİ  ·  MARCA",
                "“UMARIM. ARSENAL DE", "MUTLUYUM”",
                [("38/38", "GEÇEN SEZON", "LİG MAÇI"), ("0", "BU SEZON", "LİGDE İLK 11")],
                "KAYNAK: MARCA  ·  VERİ: TRIVELA, ARSENALNEWS",
                "/mnt/user-data/outputs/KONTRA_zubimendi.jpg")
print("ok")

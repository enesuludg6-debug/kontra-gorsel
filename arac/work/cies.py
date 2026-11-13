import sys; sys.path.insert(0, "/home/claude/font")
from kontra_stil import *
from PIL import Image, ImageEnhance

def sira_raporu(photo, kicker, dev_sira, sira_alt, baslik, satirlar, kaynak, out, vurgu=KIRMIZI,
                zemin=(10, 11, 16), pill_yazi="RAPOR", ust=640, yb=0.45):
    """Yeni düzen: soluk stat fotosu üstte, dev sıra numarası; altta yüzdeli yatay çubuk tablosu."""
    c = Image.new("RGBA", (W, H), zemin + (255,))
    im = cover(photo, W, ust, yb).convert("RGB")
    im = ImageEnhance.Color(im).enhance(0.25); im = ImageEnhance.Brightness(im).enhance(0.6)
    c.paste(im, (0, 0))
    vgrad(c, 0, 180, (0, 0, 0), 150, 0)
    vgrad(c, ust - 260, ust, zemin, 0, 255)
    logo(c, 60, 46, 50); pill(c, pill_yazi, 1020, 50, vurgu, WHITE, 30)
    tracked(c, kicker, 60, 300, WHITE, 28, track=9)
    r = dev(dev_sira, 260, vurgu, egik=True, track=3, maxw=520); put(c, r, 52, 326)
    tracked(c, sira_alt, 60 + r.width + 30, 326 + r.height // 2 - 20, WHITE, 30, track=8)
    put(c, dev(baslik, 72, WHITE, egik=False, track=2, maxw=960), 60, 660)
    y = 800; mx = max(v for _, v, _ in satirlar if v)
    for ad, v, etiket in satirlar:
        tracked(c, ad, 60, y + 14, (190, 194, 206), 28, track=7)
        if v:
            w = int(760 * v / mx)
            rect(c, (60, y + 40, 60 + w, y + 80), WHITE, alpha=230)
            tracked(c, etiket, 60 + w + 18, y + 60, WHITE, 34, track=3)
        else:
            rect(c, (60, y + 40, 76, y + 80), (220, 32, 44))
            tracked(c, etiket, 96, y + 60, (220, 32, 44), 34, track=6)
        y += 140
    rect(c, (60, 1262, 1020, 1264), WHITE, alpha=60)
    alt_bilgi(c, kaynak, 1302, sol_size=26)
    return kaydet(c, out)

if __name__ == "__main__":
    sira_raporu("/mnt/user-data/uploads/b199ad6c-image.jpg", "CIES  ·  50 LİG ARASINDA", "50.", "SÜPER LİG",
        "ALTYAPIDAN GELENE EN AZ SÜRE",
        [("ARJANTİN  ·  LİSTENİN ZİRVESİ", 25.5, "%25.5"), ("İSPANYA  ·  5 BÜYÜK LİGİN ZİRVESİ", 17.3, "%17.3"), ("SÜPER LİG", None, "50 LİG İÇİNDE SONUNCU")],
        "KAYNAK: CIES FUTBOL GÖZLEMEVİ  ·  FOTOMAÇ", "/home/claude/kontra-gorsel/g/cies_altyapi.jpg")
    print("ok")

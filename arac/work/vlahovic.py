import sys; sys.path.insert(0, "/home/claude/font")
from kontra_stil import *
from PIL import Image, ImageEnhance

def rota_iptal(photo, kicker, iptal, iptal_alt, yeni, yeni_alt, not_satiri, kaynak, out,
               vurgu=WHITE, cizgi=KIRMIZI, zemin=(8, 8, 9), pill_yazi="KARAR", ust=860, yb=0.18):
    """Yeni düzen: üstte foto; altta üstü çizilmiş eski rota ve onun yerine geçen yeni rota."""
    c = Image.new("RGBA", (W, H), zemin + (255,))
    im = Image.open(photo).convert("RGB")
    s = W / im.width; im = im.resize((W, int(im.height * s)), Image.LANCZOS)
    y0 = int((im.height - ust) * yb); im = im.crop((0, y0, W, y0 + ust))
    im = ImageEnhance.Color(im).enhance(0.55); im = ImageEnhance.Contrast(im).enhance(1.1)
    c.paste(im, (0, 0))
    vgrad(c, 0, 200, (0, 0, 0), 170, 0)
    vgrad(c, ust - 260, ust, zemin, 0, 255)
    logo(c, 60, 46, 50); pill(c, pill_yazi, 1020, 50, cizgi, WHITE, 30)
    tracked(c, kicker, 60, ust - 60, (170, 170, 176), 32, track=10)
    # iptal edilen satır
    y = ust - 20
    r = dev(iptal, 92, (120, 120, 126), egik=False, track=2, maxw=960); put(c, r, 60, y)
    rect(c, (52, y + r.height // 2 - 4, 60 + r.width + 14, y + r.height // 2 + 6), cizgi)
    tracked(c, iptal_alt, 60, y + r.height + 24, (120, 120, 126), 26, track=6)
    # ok
    y2 = y + r.height + 62
    rect(c, (60, y2, 66, y2 + 50), cizgi)
    # yeni satır
    y3 = y2 + 62
    r2 = dev(yeni, 128, vurgu, egik=True, track=2, maxw=960); put(c, r2, 56, y3)
    tracked(c, yeni_alt, 60, y3 + r2.height + 26, WHITE, 28, track=7)
    tracked(c, not_satiri, 60, 1236, (170, 170, 176), 26, track=6)
    rect(c, (60, 1262, 1020, 1264), WHITE, alpha=60)
    alt_bilgi(c, kaynak, 1302, sol_size=26)
    return kaydet(c, out)

if __name__ == "__main__":
    rota_iptal("/mnt/user-data/uploads/f013b29e-image.jpg", "MİLLİ ARADA ROTA DEĞİŞTİ",
        "SIRBİSTAN", "MİLLİ TAKIM DAVETİ  ·  ÖZEL DURUM NEDENİYLE KATILMAYACAK",
        "İSTANBUL", "TEKNİK DİREKTÖR İZNİ  ·  TESİSTE ÇALIŞMA",
        "", "KAYNAK: POSTA  ·  A SPOR", "/home/claude/kontra-gorsel/g/vlahovic_istanbul.jpg")
    print("ok")

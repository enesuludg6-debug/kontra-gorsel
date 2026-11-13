import sys; sys.path.insert(0, "/home/claude/font")
from kontra_stil import *
from PIL import Image, ImageDraw

def halka_dakika(photo, deger, toplam, halka_alt, kicker, baslik, alt_satir, kaynak, out,
                 vurgu=SARI, zemin=(20, 6, 10), pill_yazi="İDDİA", yb=0.15):
    """Yeni düzen: altta dev dakika halkası (tek maça oran), yanında başlık bloğu."""
    c = Image.new("RGBA", (W, H), zemin + (255,))
    c.paste(cover(photo, W, H, yb), (0, 0))
    vgrad(c, 0, 200, (0, 0, 0), 160, 0)
    vgrad(c, 700, 920, zemin, 0, 240); rect(c, (0, 920, W, H), zemin, alpha=240)
    logo(c, 60, 46, 50); pill(c, pill_yazi, 1020, 50, vurgu, KOYU_YAZI, 30)
    # halka (2x çizim)
    S = 2; R = 170; cx, cy = 60 + R, 1040
    ring = Image.new("RGBA", (W * S, H * S), (0, 0, 0, 0)); d = ImageDraw.Draw(ring)
    box = ((cx - R) * S, (cy - R) * S, (cx + R) * S, (cy + R) * S)
    d.ellipse(box, outline=(255, 255, 255, 50), width=22 * S)
    d.arc(box, -90, -90 + 360 * deger / toplam, fill=vurgu + (255,), width=22 * S)
    ring = ring.resize((W, H), Image.LANCZOS); c.alpha_composite(ring)
    n = dev(str(deger), 150, WHITE, egik=False, track=1, maxw=240); put(c, n, cx - n.width // 2, cy - n.height // 2 - 18)
    tracked(c, "DAKİKA", cx, cy + 70, vurgu, 26, track=8, align="center")
    tracked(c, halka_alt, cx, cy + R + 36, (200, 190, 192), 22, track=5, align="center")
    x = cx + R + 50
    tracked(c, kicker, x, 900, vurgu, 26, track=8)
    y = 928
    for t in baslik:
        r = dev(t, 84, WHITE, egik=True, track=2, maxw=1020 - x); put(c, r, x - 4, y); y += r.height + 6
    tracked(c, alt_satir, x, y + 26, (200, 190, 192), 24, track=6)
    rect(c, (60, 1262, 1020, 1264), WHITE, alpha=60)
    alt_bilgi(c, kaynak, 1302, sol_size=26)
    return kaydet(c, out)

if __name__ == "__main__":
    halka_dakika("/mnt/user-data/uploads/638a8a42-image.jpg", 27, 90, "TEK MAÇIN ÜÇTE BİRİ BİLE DEĞİL",
        "KAZIMCAN KARATAŞ", ["SÜRE YOK", "AYRILIK", "MASADA"], "DEVRE ARASI VEDA PLANI",
        "KAYNAK: SPORX", "/home/claude/kontra-gorsel/g/kazimcan_27.jpg")
    print("ok")

import sys; sys.path.insert(0, "/home/claude/font")
from kontra_stil import *
from pro import grain
from PIL import Image, ImageDraw

def yazi_kart(dev_yazi, dev_alt, kicker, satirlar, bilgiler, kaynak, out, vurgu=KIRMIZI, zemin=(12, 12, 16),
              pill_yazi="İDDİA", stil="ust", hayalet=None):
    """Fotoğrafsız tipografik kart. stil: 'ust' (dev yazı üstte), 'orta' (dev yazı ortada, şeritli),
    'sol' (sol kenarda dikey vurgu çizgisi). hayalet: arkada silik dev kelime."""
    c = Image.new("RGBA", (W, H), zemin + (255,))
    vgrad(c, 0, H, tuple(min(255, v + 18) for v in zemin), 255, 0)
    if hayalet:
        g = dev(hayalet, 420, WHITE, egik=True, track=2, maxw=1800)
        from pro import alpha as _a
        g = _a(g, 14); put(c, g, -60, 330)
    logo(c, 60, 46, 50); pill(c, pill_yazi, 1020, 50, vurgu, WHITE if vurgu != SARI else KOYU_YAZI, 30)
    if stil == "orta":
        rect(c, (0, 360, W, 364), vurgu)
        rect(c, (0, 820, W, 824), vurgu)
        tracked(c, kicker, 60, 410, vurgu, 30, track=10)
        d = dev(dev_yazi, 250, WHITE, egik=True, track=3, maxw=960); put(c, d, 54, 440)
        put(c, dev(dev_alt, 70, vurgu, egik=True, track=2, maxw=960), 60, 440 + d.height + 22)
        y = 870
    elif stil == "sol":
        rect(c, (60, 230, 72, 800), vurgu)
        tracked(c, kicker, 100, 250, vurgu, 30, track=10)
        d = dev(dev_yazi, 230, WHITE, egik=False, track=2, maxw=900); put(c, d, 96, 280)
        put(c, dev(dev_alt, 74, (200, 204, 214), egik=False, track=2, maxw=900), 100, 280 + d.height + 8)
        y = 860
    else:
        tracked(c, kicker, 60, 250, vurgu, 30, track=10)
        d = dev(dev_yazi, 280, vurgu, egik=True, track=3, maxw=960); put(c, d, 50, 276)
        put(c, dev(dev_alt, 80, WHITE, egik=True, track=2, maxw=960), 60, 276 + d.height + 4)
        y = 820
    for t in satirlar:
        r = dev(t, 64, WHITE, egik=False, track=2, maxw=960); put(c, r, 60, y); y += r.height + 10
    y += 24
    for t in bilgiler:
        rect(c, (60, y + 8, 70, y + 18), vurgu)
        tracked(c, t, 86, y + 13, (200, 204, 214), 26, track=6); y += 42
    rect(c, (60, 1262, 1020, 1264), WHITE, alpha=60)
    alt_bilgi(c, kaynak, 1302, sol_size=26)
    grain(c, 8)
    return kaydet(c, out)

if __name__ == "__main__":
    yazi_kart("28 KASIM", "SON DANS", "MUSLERA İÇİN GERİ SAYIM",
        ["LİBERTADORES FİNALİ", "SONRASI EMEKLİLİK"],
        ["ESTUDIANTES - PALMEIRAS", "22 YILLIK KARİYERE NOKTA", "KENDİSİNDEN HENÜZ AÇIKLAMA YOK"],
        "KAYNAK: ESPECTADOR DEPORTES", "/home/claude/kontra-gorsel/g/muslera_son.jpg",
        vurgu=KIRMIZI, zemin=(14, 10, 12), stil="orta", hayalet="MUSLERA")
    print("ok")

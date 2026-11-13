import sys; sys.path.insert(0, "/home/claude/font")
from kontra_stil import *
from pro import cover, vgrad, grain
from PIL import Image, ImageFilter

def portre_sag(photo, kicker, baslik, govde, kaynak, out, crop=None,
               vurgu=KIRMIZI, zemin=(14, 10, 12), pill_yazi="AÇIKLAMA"):
    """Yeni düzen (küçük dikey portreler için): sağda uzun dikey portre şeridi, solda dev başlık + gövde satırları."""
    src = Image.open(photo).convert("RGB")
    if crop: src = src.crop(crop)
    tmp = "/tmp/_ps.jpg"; src.save(tmp, quality=95)
    c = Image.new("RGBA", (W, H), zemin + (255,))
    pw, ph = 440, 1000; px = W - pw
    c.paste(cover(tmp, pw, ph, 0.15), (px, 130))
    # sol kenara yumuşak geçiş
    for i in range(160):
        rect(c, (px + i, 130, px + i + 1, 130 + ph), zemin, alpha=int(255 * (1 - i / 160)))
    rect(c, (px - 6, 130, px, 130 + ph), vurgu)
    logo(c, 60, 46, 50); pill(c, pill_yazi, 1020, 50, vurgu, WHITE, 30)
    tracked(c, kicker, 60, 300, vurgu, 28, track=10)
    y = 330
    for t in baslik:
        d = dev(t, 118, WHITE, egik=True, track=2, maxw=px - 90); put(c, d, 54, y); y += d.height + 10
    y += 40
    rect(c, (60, y, 160, y + 6), vurgu); y += 40
    for t in govde:
        tracked(c, t, 60, y, (205, 200, 205), 27, track=5); y += 50
    rect(c, (60, 1262, 1020, 1264), WHITE, alpha=60)
    alt_bilgi(c, kaynak, 1302, sol_size=26)
    grain(c, 8)
    return kaydet(c, out)

if __name__ == "__main__":
    portre_sag("/home/claude/kontra-foto/foto/sergen_yalcin_milli.jpg", "SERGEN YALÇIN",
        ["İKİ GÜNLÜK", "ANTRENMANLA", "ÇIKTIK"],
        ["TÜRKİYE 1-2 BELÇİKA SONRASI", "SAVUNMAYA ZAMAN LAZIM", "GOL YEMEK SADECE DEFANSIN", "SUÇU DEĞİL"],
        "KAYNAK: BASIN TOPLANTISI", "/home/claude/kontra-gorsel/g/sergen_iki_gun.jpg", crop=(0, 0, 399, 440))
    print("ok")

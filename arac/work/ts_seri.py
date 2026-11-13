import sys; sys.path.insert(0, "/home/claude/font")
from kontra_stil import *
from PIL import Image

def seri_serit(photo, oran, kicker, baslik_sag, ara_satir, maclar, kaynak, out, vurgu=(90,175,235), zemin=(36,8,20), pill_yazi="SERİ", yb=0.82, vurgulu=()):
    """Yeni düzen: uzun fotoda gökyüzüne dev oran (5/5), altta maç maç skor şeridi."""
    c = Image.new("RGBA", (W, H), zemin + (255,))
    c.paste(cover(photo, W, H, yb), (0, 0))
    vgrad(c, 0, 420, (0, 0, 0), 150, 0)
    vgrad(c, 930, 1110, zemin, 0, 250); rect(c, (0, 1110, W, H), zemin, alpha=250)
    logo(c, 60, 46, 50); pill(c, pill_yazi, 1020, 50, vurgu, KOYU_YAZI, 30)
    r = dev(oran, 300, WHITE, egik=True, track=4, maxw=560); put(c, r, 48, 130)
    x2 = 48 + r.width + 36
    tracked(c, kicker, x2, 190, vurgu, 34, track=10)
    put(c, dev(baslik_sag[0], 84, WHITE, egik=False, track=2, maxw=1020 - x2), x2, 222)
    put(c, dev(baslik_sag[1], 84, ACIK, egik=False, track=2, maxw=1020 - x2), x2, 322)
    tracked(c, ara_satir, 60, 1078, WHITE, 32, track=8)
    n = len(maclar); gw = 960 // n
    for k, (rakip, skor) in enumerate(maclar):
        x = 60 + k * gw
        on = rakip in vurgulu
        rect(c, (x + 4, 1118, x + gw - 8, 1122), vurgu if on else WHITE, alpha=255 if on else 90)
        tracked(c, rakip, x + 4, 1150, (180, 184, 196), 26, track=6)
        put(c, dev(skor, 62, vurgu if on else WHITE, egik=True, track=1, maxw=gw - 16), x + 4, 1172)
    rect(c, (60, 1262, 1020, 1264), WHITE, alpha=60)
    alt_bilgi(c, kaynak, 1302, sol_size=26)
    return kaydet(c, out)

seri_serit("/mnt/user-data/uploads/3ec81cc3-image.jpg", "5/5", "İÇ SAHADA", ("26 YIL", "SONRA"),
  "15 GOL ATTI  ·  1 GOL YEDİ",
  [("BAŞAKŞEHİR", "2-1"), ("G.BİRLİĞİ", "5-0"), ("GALATASARAY", "4-0"), ("BEŞİKTAŞ", "2-0"), ("GAZİANTEP", "2-0")],
  "KAYNAK: NEFES  ·  AKŞAM  ·  ÖNCEKİ SERİ 2000-01", "/home/claude/kontra-gorsel/g/ts_5te5.jpg",
  vurgulu=("GALATASARAY", "BEŞİKTAŞ"))
print("ok")

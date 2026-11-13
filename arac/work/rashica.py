import sys; sys.path.insert(0, "/home/claude/font")
from kontra_stil import *
from PIL import Image, ImageDraw
import os

def cizgili_kesik(photo, cut, arka_kelime, kicker, baslik, satirlar, kaynak, out=None, zemin=(10,10,11), vurgu=WHITE, pill_yazi="İDDİA", yb=0.0, olcek=1.0, dx=120):
    """Yeni düzen: kulüp çizgili (pinstripe) zemin, arkada soluk dev kelime, kesik oyuncu sağda,
    solda dikey bilgi satırları, altta başlık."""
    c = Image.new("RGBA", (W, H), zemin + (255,))
    lay = Image.new("RGBA", (W, H), (0,0,0,0)); d = ImageDraw.Draw(lay)
    for x in range(0, W, 36): d.line([(x,0),(x,H)], fill=(255,255,255,16), width=2)
    c.alpha_composite(lay)
    gk = dev(arka_kelime, 330, (255,255,255), egik=True, track=4, maxw=1060)
    g2 = gk.copy(); g2.putalpha(g2.getchannel("A").point(lambda v: v*26//255))
    put(c, g2, W/2, 150, align="center")
    cu = Image.open(cut).convert("RGBA"); cu = cu.crop(cu.getbbox())
    hh = int(1000*olcek); cu = cu.resize((int(cu.width*hh/cu.height), hh), Image.LANCZOS)
    c.alpha_composite(cu, (W - cu.width + dx, 150))
    vgrad(c, 800, 1060, zemin, 0, 255); rect(c, (0, 1060, W, H), zemin)
    vgrad(c, 0, 170, (0,0,0), 150, 0)
    logo(c, 60, 46, 50); pill(c, pill_yazi, 1020, 50, WHITE, KOYU_YAZI, 30)
    y = 300
    for et, dg in satirlar:
        tracked(c, et, 60, y, (160,163,172), 28, track=8)
        l = dev(dg, 58, WHITE, egik=False, track=2, maxw=430); put(c, l, 60, y+24)
        rect(c, (60, y+24+l.height+22, 120, y+24+l.height+26), WHITE, alpha=140)
        y += l.height + 110
    tracked(c, kicker, 60, 1000, ACIK, 34, track=10)
    put(c, dev(baslik, 140, WHITE, egik=True, track=3, maxw=960), 52, 1030)
    rect(c, (60, 1262, 1020, 1264), WHITE, alpha=60)
    alt_bilgi(c, kaynak, 1302, sol_size=26)
    return kaydet(c, out)

src="/mnt/user-data/uploads/884d28c9-image.jpg"; cut="/home/claude/work/rashica_cut.png"
if not os.path.exists(cut): kes(src, cut)
cizgili_kesik(src, cut, "BEDELSİZ", "BEŞİKTAŞ  ·  MİLOT RASHICA", "YOLLAR AYRILIYOR",
    [("SÖZLEŞME", "HAZİRANDA BİTİYOR"), ("OCAK", "BEDELSİZ YA DA FESİH"), ("YERİNE", "SAĞ STOPER")],
    "KAYNAK: TAKVİM", olcek=0.97, dx=30, out="/home/claude/kontra-gorsel/g/rashica_ayrilik.jpg")
print("ok")

import sys; sys.path.insert(0, "/home/claude/font")
from kontra_stil import *
from pro import cover, vgrad, grain
from PIL import Image

def alinti_tam(photo, konusan, alinti, ikinci, hedef, kaynak, out, vurgu=KIRMIZI, zemin=(8, 10, 20),
               pill_yazi="AÇIKLAMA", yb=0.35):
    """Yeni düzen: tam ekran foto, altta dev tırnak işaretli alıntı bloğu + konuşan/hedef etiketi."""
    c = Image.new("RGBA", (W, H), zemin + (255,))
    c.paste(cover(photo, W, H, yb), (0, 0))
    vgrad(c, 0, 240, (0, 0, 0), 170, 0)
    vgrad(c, 560, 900, zemin, 0, 240); rect(c, (0, 900, W, H), zemin, alpha=240)
    logo(c, 60, 46, 50); pill(c, pill_yazi, 1020, 50, vurgu, WHITE, 30)
    q = dev("“", 260, vurgu, egik=False, track=0, maxw=200); put(c, q, 50, 700)
    rect(c, (188, 766, 620, 852), zemin, alpha=200, radius=6)
    tracked(c, konusan, 200, 790, vurgu, 30, track=10)
    tracked(c, hedef, 200, 830, (180, 185, 200), 24, track=7)
    y = 880
    for t in alinti:
        r = dev(t, 100, WHITE, egik=True, track=2, maxw=960); put(c, r, 54, y); y += r.height + 8
    y += 26
    for t in ikinci:
        tracked(c, t, 60, y, (200, 204, 214), 25, track=5); y += 42
    rect(c, (60, 1262, 1020, 1264), WHITE, alpha=60)
    alt_bilgi(c, kaynak, 1302, sol_size=26)
    grain(c, 6)
    return kaydet(c, out)

if __name__ == "__main__":
    alinti_tam("/home/claude/kontra-foto/foto/hakan_calhanoglu_inter_sirt.jpg", "TUGAY KERİMOĞLU", ["VÜCUT DİLİ", "İYİ DEĞİL"],
        ["BİZ DE ÇOK ELEŞTİRİLİRDİK, CEVABI SAHADA VERİRDİK"], "HAKAN ÇALHANOĞLU",
        "KAYNAK: YENİÇAĞ", "/home/claude/kontra-gorsel/g/tugay_hakan.jpg")
    print("ok")

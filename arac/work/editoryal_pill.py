import sys; sys.path.insert(0, "/home/claude/font")
from kontra_stil import *
from kart import fit, BEBAS

def editoryal_pill(photo, kicker, satir1, satir2, alt, kaynak, out, pill_yazi="İDDİA", vurgu=KIRMIZI, yb=0.25):
    """editoryal + sağ üst güven etiketi (handle altta)."""
    c = Image.new("RGBA", (W, H), LACI_SIYAH + (255,))
    foto_ust(c, photo, 850, LACI_SIYAH, 600, yb)
    logo(c, 60, 46, 50); pill(c, pill_yazi, 1020, 50, vurgu, WHITE, 30)
    tracked(c, kicker, W / 2, 874, vurgu, 38, align="center", track=10)
    put(c, dev(satir1, 122, WHITE, egik=False, track=4), W / 2, 902, align="center")
    put(c, dev(satir2, 122, ACIK, egik=False, track=4), W / 2, 1036, align="center")
    rect(c, (W / 2 - 60, 1190, W / 2 + 60, 1197), vurgu)
    put(c, fit(alt, BEBAS, 36, WHITE, 960, track=5), W / 2, 1232, align="center", valign="middle")
    rect(c, (60, 1262, 1020, 1264), WHITE, alpha=60)
    alt_bilgi(c, kaynak, 1302, sol_size=26)
    return kaydet(c, out)

if __name__ == "__main__":
    editoryal_pill("/home/claude/kontra-foto/foto/mert_muldur_fb.jpg", "GALATASARAY RADARINDA", "MERT", "MÜLDÜR",
        "SÖZLEŞME UZATILMAZSA SEZON SONU TEKLİF", "KAYNAK: TAKVİM", "/home/claude/kontra-gorsel/g/mert_muldur_gs.jpg",
        vurgu=(200, 30, 45), yb=0.3)
    print("ok")

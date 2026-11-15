"""KONTRA dikey video: Fransa - Turkiye on analiz (15.11.2026). 1080x1920, 30fps.
Calistir: python3 arac/video/fra_tur.py  ->  g/fra_tur_video.mp4
"""
import sys, subprocess, math, os
sys.path.insert(0, "/home/claude/font")
from kart import text_layer, K_POLYS, ANTON, BEBAS, NAVY, WHITE
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS = 1080, 1920, 30
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "g", "fra_tur_video.mp4")
INTER_B = "/usr/share/fonts/opentype/inter/Inter-Bold.otf"
INTER_K = "/usr/share/fonts/opentype/inter/Inter-Black.otf"
INTER_M = "/usr/share/fonts/opentype/inter/Inter-Medium.otf"

LACI = (11, 15, 32); KIRMIZI = (220, 32, 44); SARI = (246, 190, 30)
ACIK = (202, 214, 234); GRI = (150, 156, 172); FRA = (35, 75, 190); CIM = (24, 74, 46)


# ---------- yardimcilar ----------
def T(text, font=ANTON, size=80, color=WHITE, track=0, shear=0.0):
    return text_layer(text, font, size, color, track=track, shear=shear)


def para(lines, size=44, color=WHITE, font=INTER_B, gap=1.32):
    f = ImageFont.truetype(font, size)
    h = int(size * gap)
    lay = Image.new("RGBA", (W + 400, h * len(lines) + 10), (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    for i, (ln, col) in enumerate(lines if isinstance(lines[0], tuple) else [(l, color) for l in lines]):
        d.text((0, i * h), ln, font=f, fill=col)
    return lay.crop(lay.getbbox() or (0, 0, 1, 1))


def box(w, h, color, radius=0, alpha=255):
    lay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    ImageDraw.Draw(lay).rounded_rectangle((0, 0, w - 1, h - 1), radius=radius, fill=color + (alpha,))
    return lay


def pill(text, bg=KIRMIZI, fg=WHITE, size=36):
    t = T(text, BEBAS, size, fg, track=8)
    pw, ph = t.width + 52, int(size * 1.5)
    b = box(pw, ph, bg, radius=ph // 2)
    b.alpha_composite(t, ((pw - t.width) // 2, (ph - t.height) // 2))
    return b


def logo_layer(size=64):
    S = size * 4
    lay = Image.new("RGBA", (S, S), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.rounded_rectangle((0, 0, S - 1, S - 1), radius=int(S * 0.22), fill=NAVY + (255,),
                        outline=WHITE + (255,), width=int(S * 0.04))
    k = S * 1.25 / 800; off = -S * 0.125
    for p in K_POLYS:
        d.polygon([(px * k + off, py * k + off) for px, py in p], fill=WHITE + (255,))
    lg = lay.resize((size, size), Image.LANCZOS)
    wl = T("KONTRA", ANTON, int(size * 0.62), WHITE, track=4, shear=0.2)
    out = Image.new("RGBA", (size + 16 + wl.width, size), (0, 0, 0, 0))
    out.alpha_composite(lg, (0, 0)); out.alpha_composite(wl, (size + 16, (size - wl.height) // 2))
    return out


def ease(x):
    x = max(0.0, min(1.0, x)); return 1 - (1 - x) ** 3


def bg_base(c1, c2):
    g = Image.new("RGB", (1, 256))
    for y in range(256):
        t = y / 255; g.putpixel((0, y), tuple(int(c1[i] * (1 - t) + c2[i] * t) for i in range(3)))
    return g.resize((W, H)).convert("RGBA")


# arka plan: diagonal cizgiler (kontra cizgileri)
def stripes(color, alpha=18):
    lay = Image.new("RGBA", (W + 600, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    for x in range(-H, W + 600, 90):
        d.line([(x, H), (x + H * 0.45, 0)], fill=color + (alpha,), width=26)
    return lay


def pitch(w=960, h=1180, line=(255, 255, 255, 150)):
    """Dikey saha (Turkiye asagidan yukari hucum eder)."""
    lay = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    for i in range(10):
        col = (30, 92, 56) if i % 2 == 0 else (26, 82, 50)
        d.rectangle((0, i * h / 10, w, (i + 1) * h / 10), fill=col + (235,))
    m = 18; lw = 4
    d.rectangle((m, m, w - m, h - m), outline=line, width=lw)
    d.line((m, h / 2, w - m, h / 2), fill=line, width=lw)
    d.ellipse((w / 2 - 110, h / 2 - 110, w / 2 + 110, h / 2 + 110), outline=line, width=lw)
    for top in (True, False):
        y0 = m if top else h - m
        s = 1 if top else -1
        d.rectangle(sorted_box(w / 2 - 250, y0, w / 2 + 250, y0 + s * 200), outline=line, width=lw)
        d.rectangle(sorted_box(w / 2 - 110, y0, w / 2 + 110, y0 + s * 70), outline=line, width=lw)
    return lay


def sorted_box(x0, y0, x1, y1):
    return (min(x0, x1), min(y0, y1), max(x0, x1), max(y0, y1))


def dot(label, color, size=78, fg=WHITE):
    lay = Image.new("RGBA", (size + 8, size + 8), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.ellipse((4, 4, size + 4, size + 4), fill=color + (255,), outline=WHITE + (255,), width=4)
    t = T(label, BEBAS, int(size * 0.42), fg, track=1)
    lay.alpha_composite(t, ((lay.width - t.width) // 2, (lay.height - t.height) // 2))
    return lay


def arrow(d, p0, p1, color, width=10, dash=False):
    x0, y0 = p0; x1, y1 = p1
    L = math.hypot(x1 - x0, y1 - y0); ang = math.atan2(y1 - y0, x1 - x0)
    if dash:
        n = int(L // 36)
        for i in range(n):
            if i % 2 == 0:
                a = i / n; b = min(1, (i + 1) / n)
                d.line((x0 + (x1 - x0) * a, y0 + (y1 - y0) * a, x0 + (x1 - x0) * b, y0 + (y1 - y0) * b), fill=color, width=width)
    else:
        d.line((x0, y0, x1, y1), fill=color, width=width)
    hl = 38
    pts = [(x1, y1), (x1 - hl * math.cos(ang - 0.45), y1 - hl * math.sin(ang - 0.45)),
           (x1 - hl * math.cos(ang + 0.45), y1 - hl * math.sin(ang + 0.45))]
    d.polygon(pts, fill=color)


# ---------- sahne sistemi ----------
class Scene:
    def __init__(self, dur, bg, items, tag=None):
        self.dur = dur; self.bg = bg; self.items = items; self.tag = tag


def it(layer, x, y, t0, dx=0, dy=60, fade=0.45, anchor="lt"):
    return dict(layer=layer, x=x, y=y, t0=t0, dx=dx, dy=dy, fade=fade, anchor=anchor)


def cx(layer):
    return (W - layer.width) // 2


S = []
BG_DARK = bg_base((14, 18, 40), (6, 7, 14))
BG_RED = bg_base((120, 12, 22), (18, 6, 10))
BG_SPLIT = bg_base((16, 28, 70), (60, 10, 18))
ST_W = stripes(WHITE, 12); ST_R = stripes(KIRMIZI, 22)

# 1) GIRIS
l1 = T("BU AKŞAM", BEBAS, 70, ACIK, track=14)
l2 = T("FRANSA", ANTON, 230, WHITE, shear=0.2)
l3 = T("TÜRKİYE", ANTON, 230, KIRMIZI, shear=0.2)
vs = pill("BORDEAUX · MATMUT ATLANTIQUE", bg=WHITE, fg=LACI, size=40)
inf = para([("22.45  ·  ATV  ·  ŞİFRESİZ", WHITE)], size=48, font=INTER_K)
inf2 = para([("UEFA Uluslar Ligi A1 · Son hafta", ACIK)], size=40, font=INTER_M)
S.append(Scene(6.5, (BG_SPLIT, ST_W), [
    it(l1, cx(l1), 470, 0.1), it(l2, cx(l2), 560, 0.3, dx=-200, dy=0),
    it(l3, cx(l3), 830, 0.6, dx=200, dy=0), it(vs, cx(vs), 1150, 1.0),
    it(inf, cx(inf), 1290, 1.3), it(inf2, cx(inf2), 1380, 1.5)]))

# 2) TABLO
k = T("GRUPTA DURUM", BEBAS, 60, SARI, track=14)
r1 = T("5", ANTON, 420, WHITE, shear=0.2); e1 = T("MAÇ", BEBAS, 80, ACIK, track=10)
r2 = T("0", ANTON, 420, KIRMIZI, shear=0.2); e2 = T("PUAN", BEBAS, 80, ACIK, track=10)
n1 = para(["Türkiye grupta oynadığı 5 maçı da kaybetti.",
           "Fransa 10 puanla ikinci sırada.",
           "Raporlara göre Fransa'ya 1 puan bile yetiyor."], size=42)
S.append(Scene(7, (BG_DARK, ST_R), [
    it(k, cx(k), 330, 0.1), it(r1, 150, 460, 0.3, dy=120), it(e1, 190, 1000, 0.6),
    it(r2, 620, 460, 0.7, dy=120), it(e2, 640, 1000, 1.0),
    it(box(840, 6, KIRMIZI), 120, 1130, 1.2, dx=-300, dy=0),
    it(n1, 120, 1190, 1.4)], tag="DURUM"))

# 3) TURKIYE HABERLER
k = T("MİLLİ TAKIMDA SON DURUM", BEBAS, 58, SARI, track=12)
h = T("SERGEN'İN", ANTON, 150, WHITE, shear=0.2); h2 = T("İKİNCİ SINAVI", ANTON, 150, KIRMIZI, shear=0.2)
cards = []
rows = [("İLK MAÇ", "İzmir'de Belçika'ya 2-1 yenildik."),
        ("DÖNÜŞ", "Abdülkerim Bardakcı cezasını tamamladı."),
        ("EKSİK", "Kenan Yıldız sakat, kadroda değil."),
        ("SERGEN", "\"Santrforla oynayacağız.\"")]
for i, (a, b) in enumerate(rows):
    c = box(900, 150, (255, 255, 255), radius=22, alpha=22)
    c.alpha_composite(box(10, 150, KIRMIZI), (0, 0))
    c.alpha_composite(T(a, BEBAS, 40, SARI, track=8), (40, 22))
    c.alpha_composite(para([b], size=40), (40, 80))
    cards.append(it(c, 90, 880 + i * 180, 1.0 + i * 0.35, dx=-120, dy=0))
S.append(Scene(8, (BG_DARK, ST_W), [it(k, 90, 380, 0.1, dy=30), it(h, 90, 470, 0.3), it(h2, 90, 650, 0.55)] + cards, tag="TÜRKİYE"))

# 4) FRANSA EKSIKLER
k = T("FRANSA'DA ALARM", BEBAS, 58, SARI, track=12)
h = T("SAVUNMA", ANTON, 190, WHITE, shear=0.2); h2 = T("YAMALI", ANTON, 190, KIRMIZI, shear=0.2)
names = ["UPAMECANO", "SALIBA", "KOUNDÉ", "LACROIX", "KALULU"]
nl = []
for i, n in enumerate(names):
    p = pill(n + "  ✕" if False else n, bg=(40, 44, 66), fg=WHITE, size=46)
    nl.append(it(p, 90 + (i % 2) * 470, 960 + (i // 2) * 105, 1.0 + i * 0.18, dy=40))
nt = para([("Upamecano kamptan ayrıldı,", ACIK), ("diğer dört isim sakat.", ACIK),
           ("Mbappé İtalya maçını kaçırdı.", WHITE),
           ("Zidane oynayabileceğini söyledi.", WHITE)], size=40)
S.append(Scene(7.5, (BG_DARK, ST_R), [it(k, 90, 380, 0.1, dy=30), it(h, 90, 470, 0.3), it(h2, 90, 690, 0.55)] + nl
          + [it(nt, 90, 1310, 2.0)], tag="FRANSA"))

# 5) FRANSA MUHTEMEL 11
k = T("FRANSA MUHTEMEL 11", BEBAS, 58, SARI, track=12)
pt = pitch(960, 1180)
xi = [("MAIGNAN", 0.5, 0.90), ("GUSTO", 0.86, 0.72), ("JACQUET", 0.62, 0.77), ("KONATÉ", 0.38, 0.77), ("TRUFFERT", 0.14, 0.72),
      ("CAMAVINGA", 0.64, 0.56), ("RABIOT", 0.36, 0.56), ("OLISE", 0.84, 0.34), ("CHERKI", 0.5, 0.38), ("DOUÉ", 0.16, 0.34),
      ("MBAPPÉ", 0.5, 0.17)]
pl_items = [it(pt, 60, 400, 0.2, dy=0, fade=0.6)]
for i, (n, px, py) in enumerate(xi):
    lay = Image.new("RGBA", (240, 140), (0, 0, 0, 0))
    dd = dot("", FRA, 70); lay.alpha_composite(dd, ((240 - dd.width) // 2, 0))
    tn = T(n, BEBAS, 38, WHITE, track=3)
    lay.alpha_composite(box(tn.width + 20, 46, LACI, radius=8, alpha=220), ((240 - tn.width - 20) // 2, 84))
    lay.alpha_composite(tn, ((240 - tn.width) // 2, 88))
    # saha ters: Fransa yukaridan asagi hucum; kaleci ustte
    X = 60 + (1 - px) * 960 - 120; Y = 400 + (1 - py) * 1180 - 40
    pl_items.append(it(lay, int(X), int(Y), 0.6 + i * 0.12, dy=-30))
sm = para([("4-2-3-1 · Kaynak: Sports Mole / Hard Tackle", GRI)], size=32, font=INTER_M)
S.append(Scene(7, (BG_DARK, ST_W), [it(k, 90, 300, 0.1, dy=30)] + pl_items + [it(sm, 90, 1620, 2.0)], tag="RAKİP"))


# 6-8) TAKTIK SAHNELERI
def taktik(no, baslik1, baslik2, maddeler, cizim, tag):
    k = T(f"TAKTİK  {no}/3", BEBAS, 58, SARI, track=14)
    a = T(baslik1, ANTON, 120, WHITE, shear=0.2); b = T(baslik2, ANTON, 120, KIRMIZI, shear=0.2)
    pt = pitch(960, 700)
    d = ImageDraw.Draw(pt); cizim(d, pt)
    md = para(maddeler, size=40)
    return Scene(8.5, (BG_DARK, ST_R), [
        it(k, 60, 250, 0.1, dy=30), it(a, 60, 330, 0.3), it(b, 60, 470, 0.5),
        it(pt, 60, 650, 0.8, dy=0, fade=0.6), it(md, 60, 1400, 1.6)], tag=tag)


def c1(d, pt):  # kompakt orta blok
    w, h = pt.size
    d.rounded_rectangle((90, h * 0.42, w - 90, h * 0.80), radius=30, fill=KIRMIZI + (70,), outline=KIRMIZI + (255,), width=5)
    for yy, xs in ((0.47, (0.2, 0.4, 0.6, 0.8)), (0.62, (0.38, 0.62)), (0.74, (0.2, 0.4, 0.6, 0.8))):
        for x in xs:
            pt.alpha_composite(dot("", KIRMIZI, 52), (int(w * x) - 30, int(h * yy) - 30))
    for x in (0.2, 0.5, 0.8):
        pt.alpha_composite(dot("", FRA, 52), (int(w * x) - 30, int(h * 0.88) - 30))
    d.line((60, h * 0.80, w - 60, h * 0.80), fill=SARI + (255,), width=6)
    t = T("ARKAYI VERME", BEBAS, 40, SARI, track=6); pt.alpha_composite(t, (w - t.width - 40, int(h * 0.80) + 12))


def c2(d, pt):  # santrfor + ikinci top + Truffert arkasi
    w, h = pt.size
    pt.alpha_composite(dot("9", KIRMIZI, 60), (int(w * 0.5) - 34, int(h * 0.22) - 34))
    pt.alpha_composite(dot("", FRA, 52), (int(w * 0.42) - 30, int(h * 0.16) - 30))
    pt.alpha_composite(dot("", FRA, 52), (int(w * 0.58) - 30, int(h * 0.16) - 30))
    pt.alpha_composite(dot("", FRA, 52), (int(w * 0.84) - 30, int(h * 0.20) - 30))
    pt.alpha_composite(dot("6", KIRMIZI, 60), (int(w * 0.5) - 34, int(h * 0.74) - 34))
    pt.alpha_composite(dot("7", KIRMIZI, 60), (int(w * 0.82) - 34, int(h * 0.52) - 34))
    arrow(d, (w * 0.5, h * 0.70), (w * 0.5, h * 0.28), SARI + (255,), 9)
    arrow(d, (w * 0.82, h * 0.48), (w * 0.88, h * 0.10), WHITE + (255,), 8, dash=True)
    t = T("TRUFFERT'İN ARKASI", BEBAS, 36, WHITE, track=4); pt.alpha_composite(t, (w - t.width - 30, int(h * 0.30)))
    t = T("İKİNCİ TOP", BEBAS, 36, SARI, track=4); pt.alpha_composite(t, (int(w * 0.53), int(h * 0.42)))


def c3(d, pt):  # duran top
    w, h = pt.size
    for x, y in ((0.40, 0.12), (0.52, 0.10), (0.62, 0.14), (0.47, 0.20)):
        pt.alpha_composite(dot("", KIRMIZI, 52), (int(w * x) - 30, int(h * y) - 30))
    pt.alpha_composite(dot("", WHITE, 40, fg=LACI), (int(w * 0.97) - 22, int(h * 0.03) - 2))
    d.arc((w * 0.40, -h * 0.05, w * 1.0, h * 0.40), 180, 300, fill=SARI + (255,), width=8)
    d.rounded_rectangle((60, h * 0.55, w - 60, h * 0.92), radius=26, fill=(0, 0, 0, 90))
    t = T("İLK 20 DK: SABIR", ANTON, 70, WHITE, shear=0.2); pt.alpha_composite(t, ((w - t.width) // 2, int(h * 0.60)))
    t = T("FRANSA 1 PUANA RAZI OLABİLİR", BEBAS, 40, SARI, track=5); pt.alpha_composite(t, ((w - t.width) // 2, int(h * 0.78)))


S.append(taktik(1, "KOMPAKT", "ORTA BLOK", [
    ("Mbappé, Doué ve Olise hızlı. Arkada boşluk = gol.", WHITE),
    ("Savunma hattı çok derine düşmeden kalsın,", WHITE),
    ("hatlar arası 30 metreyi geçmesin.", ACIK)], c1, "PLAN"))
S.append(taktik(2, "YENİ STOPERLERE", "BASKI", [
    ("Saliba ve Upamecano yok, stoper ikilisi yeni.", WHITE),
    ("Santrfora direkt top, ikinci topları topla.", WHITE),
    ("Hücumcu bek Truffert'in arkasına koşu at.", ACIK)], c2, "PLAN"))
S.append(taktik(3, "DURAN TOP", "SİLAHI", [
    ("Bardakcı'nın dönüşü hava toplarında güç demek.", WHITE),
    ("Kornerler ve serbest vuruşlar en net fırsat.", WHITE),
    ("Erken gol yeme, oyunu sona taşı.", ACIK)], c3, "PLAN"))

# 9) KAPANIS
k = T("SON SÖZ", BEBAS, 60, SARI, track=14)
q1 = T("EYLÜL'DE", ANTON, 150, WHITE, shear=0.2)
q2 = T("1-0", ANTON, 380, KIRMIZI, shear=0.2)
q3 = para([("Fransa kazanmıştı, golü Mbappé atmıştı.", WHITE),
           ("Bu akşam grubu puansız kapatmamak", ACIK), ("için son şans.", ACIK)], size=42)
hk = pill("HAKEM: CHRIS KAVANAGH", bg=WHITE, fg=LACI, size=40)
hd = T("@KONTRA_11", ANTON, 110, WHITE, track=4, shear=0.2)
S.append(Scene(7, (BG_SPLIT, ST_W), [
    it(k, cx(k), 360, 0.1), it(q1, cx(q1), 450, 0.3), it(q2, cx(q2), 640, 0.6, dy=150),
    it(q3, 90, 1080, 1.2), it(hk, cx(hk), 1270, 1.6), it(hd, cx(hd), 1480, 2.2)]))

# ---------- render ----------
LOGO = logo_layer(66)
TOTAL = sum(s.dur for s in S)
NF = int(TOTAL * FPS)


def frame(fi):
    t = fi / FPS
    acc = 0
    for si, s in enumerate(S):
        if t < acc + s.dur or si == len(S) - 1:
            break
        acc += s.dur
    lt = t - acc
    bg, st = s.bg
    c = bg.copy()
    off = int((lt * 30) % 90)
    c.alpha_composite(st, (-300 - off, 0))
    out_a = 1 - ease((lt - (s.dur - 0.35)) / 0.35) if lt > s.dur - 0.35 and si < len(S) - 1 else 1.0
    for e in s.items:
        p = ease((lt - e["t0"]) / e["fade"])
        if p <= 0:
            continue
        a = p * out_a
        lay = e["layer"]
        if a < 1:
            lay = lay.copy(); al = lay.getchannel("A").point(lambda v: int(v * a)); lay.putalpha(al)
        x = int(e["x"] + e["dx"] * (1 - p)); y = int(e["y"] + e["dy"] * (1 - p))
        c.alpha_composite(lay, (x, y)) if x >= 0 and y >= 0 else c.paste(lay, (x, y), lay)
    # ust bar: logo + etiket + ilerleme
    c.alpha_composite(LOGO, (60, 90))
    if s.tag:
        pl = pill(s.tag, size=34); c.alpha_composite(pl, (W - 60 - pl.width, 98))
    d = ImageDraw.Draw(c)
    d.rectangle((0, 0, W, 10), fill=(255, 255, 255, 40))
    d.rectangle((0, 0, int(W * t / TOTAL), 10), fill=KIRMIZI + (255,))
    # alt
    d.line((60, H - 150, W - 60, H - 150), fill=(255, 255, 255, 70), width=2)
    f = ImageFont.truetype(INTER_M, 28)
    d.text((60, H - 125), "Kaynak: A Spor, Habertürk, Sports Mole, NTV", font=f, fill=GRI)
    d.text((W - 60, H - 125), "@KONTRA_11", font=ImageFont.truetype(INTER_K, 30), fill=WHITE, anchor="ra")
    return c.convert("RGB")


if __name__ == "__main__":
    if "--still" in sys.argv:
        tt = [float(x) for x in sys.argv[sys.argv.index("--still") + 1:]]
        for x in tt:
            frame(int(x * FPS)).save(os.path.join(ROOT, "arac", "video", f"still_{x:05.1f}.jpg"), quality=85)
        sys.exit()
    bpm = 0.5  # 120 bpm
    audio = (f"aevalsrc='0.55*sin(2*PI*52*t)*exp(-9*mod(t,{bpm}))"
             f"+0.10*sin(2*PI*110*t)*sin(2*PI*0.25*t)^2"
             f"+0.05*(random(0)*2-1)*exp(-40*mod(t+{bpm/2},{bpm}))"
             f"+0.07*sin(2*PI*220*t)*(0.5+0.5*sin(2*PI*0.125*t))':s=44100:d={TOTAL}")
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
           "-f", "lavfi", "-i", audio, "-af", f"afade=t=in:d=1,afade=t=out:st={TOTAL-1.5}:d=1.5,volume=0.8",
           "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k",
           "-shortest", "-movflags", "+faststart", OUT]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for fi in range(NF):
        p.stdin.write(frame(fi).tobytes())
    p.stdin.close(); p.wait()
    print(OUT, TOTAL, "sn")

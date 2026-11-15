"""KONTRA PRO EDIT: Turkiye (Fransa maci oncesi). Yazisiz, sinematik, 130 BPM.
Teknikler: velocity hiz rampasi (vurus aninda %18'e yavaslama), whip-pan hareket bulaniklikli gecis,
sadece darbe aninda sarsinti, sinematik renk (teal-orange + kirmiziyi koru), bloom/halation, film grain,
whoosh + impact sesleri.
Kaynak klipler klip/ klasorunde (git'e girmez).  Calistir: python3 arac/video/fra_tur_pro.py
"""
import sys, os, math, subprocess, wave
import numpy as np
from PIL import Image, ImageFilter

W, H, FPS = 1080, 1920, 30
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
KLIP = os.path.join(ROOT, "klip")
OUT = os.path.join(ROOT, "g", "tur_pro_edit_klipli.mp4" if "--yazisiz" in sys.argv else "tur_pro_edit_yazili_klipli.mp4")
TMP = "/tmp/claude-0/edit_pro"; os.makedirs(TMP, exist_ok=True)
BPM = 130; B = 60 / BPM; SR = 44100
BU, DROP, OUTRO, END = 8, 16, 48, 56

# shot: (bas_vurus, vurus, klip, kaynak_sn, hiz)
#   hiz: sayi = sabit hiz;  ("ramp", anahtar_sn) = velocity: hizli -> anahtar anda %18 -> hizli
#   whip: True = gecis bulanikligi ile girer;  hit: shot icindeki darbe anlari (vurus cinsinden, sarsinti + impact)
S = [
    dict(b=0, n=4, k="f4_bayrak", t=3.0, v=0.55),
    dict(b=4, n=4, k="f2_atmosfer", t=8.0, v=0.8),
    # ---------------- FRANSA (gerilim) ----------------
    dict(b=8, n=2, k="r3_fransa", t=0.5, v=0.85),                         # Fransa isinmaya cikiyor
    dict(b=10, n=2, k="r1_mbappe_final", t=9.6, v=0.55, whip=True),       # sirtta MBAPPE 10
    dict(b=12, n=1, k="r2_mbappe_legend", t=4.8, v=1.1, whip=True),       # Mbappe depar
    dict(b=13, n=1, k="r4_fransa_son", t=0.3, v=0.9, whip=True, z=1.28, oy=500, hit=[0.0]),  # Mbappe bagiriyor
    dict(b=14, n=1, k="r1_mbappe_final", t=15.2, v=0.6, whip=True),       # Mbappe yakin
    dict(b=15, n=1, k="f9_futbolcular", t=27.6, v=0.35, z=1.15, oy=160),  # cevap: Arda sirttan
    # ---------------- DROP ----------------
    dict(b=16, n=2, k="k8_arda_euro", t=("ramp", 4.28), whip=True, hit=[0.8]),
    dict(b=18, n=1, k="k8_arda_euro", t=5.45, v=1.0, whip=True),
    dict(b=19, n=1, k="k6_kerem", t=0.6, v=1.1, whip=True),
    dict(b=20, n=2, k="k9_futbolcular", t=("ramp", 12.38), whip=True, hit=[0.8]),
    dict(b=22, n=1, k="k9_futbolcular", t=19.2, v=0.8, whip=True),
    dict(b=23, n=1, k="k9_futbolcular", t=22.3, v=0.8, whip=True, hit=[0.0]),
    dict(b=24, n=2, k="k2_arda_dortmund", t=3.2, v=1.0, whip=True),
    dict(b=26, n=1, k="k10_milli_mac", t=4.0, v=0.9, whip=True),
    dict(b=27, n=1, k="f9_futbolcular", t=6.5, v=0.8, whip=True),
    dict(b=28, n=2, k="f3_red_aesthetic", t=6.3, v=0.8),
    dict(b=30, n=2, k="k6_kerem", t=("ramp", 3.4), whip=True, hit=[0.8]),
    dict(b=32, n=1, k="k6_kerem", t=12.9, v=1.0, whip=True),
    dict(b=33, n=1, k="k9_futbolcular", t=24.0, v=0.9, whip=True, hit=[0.0]),
    dict(b=34, n=2, k="f9_futbolcular", t=28.4, v=0.4, z=1.15, oy=160),
    dict(b=36, n=1, k="k1_milli", t=1.3, v=1.0, whip=True),
    dict(b=37, n=1, k="f6_soyunma", t=64.0, v=1.0, whip=True),
    dict(b=38, n=2, k="k9_futbolcular", t=29.5, v=0.7, whip=True),
    dict(b=40, n=2, k="k5_dortmund_taraftar", t=6.0, v=0.7),
    dict(b=42, n=1, k="k10_milli_mac", t=0.0, v=1.0, whip=True, hit=[0.0]),
    dict(b=43, n=1, k="k6_kerem", t=21.0, v=1.0, whip=True),
    dict(b=44, n=2, k="k2_arda_dortmund", t=6.0, v=1.0, whip=True),
    dict(b=46, n=2, k="f6_soyunma", t=50.0, v=1.0, whip=True),
    # ---------------- OUTRO ----------------
    dict(b=48, n=8, k="f4_bayrak", t=10.0, v=0.45),
]
TOTAL = END * B + 0.3
NF = int(TOTAL * FPS)


def ramp_speed(x):
    """0..1 shot ilerlemesi -> hiz. %40'ta dip (0.18)."""
    d = (x - 0.4) / 0.16
    return 0.18 + 1.6 * (1 - math.exp(-d * d))


def src_time(s, lt):
    """Shot icindeki lt (sn) -> kaynak klipte saniye."""
    sd = s["n"] * B
    if isinstance(s["t"], tuple):
        key = s["t"][1]
        steps = 200
        integ = lambda upto: sum(ramp_speed((i + 0.5) / steps * upto / sd) for i in range(steps)) * upto / steps
        return key - integ(0.4 * sd) + integ(lt)
    return s["t"] + lt * s["v"]


# ---------------- kare okuma (shot bazli onbellek) ----------------
_clip = {"key": None}


def load_shot(s, si):
    if _clip["key"] == si: return
    sd = s["n"] * B
    t0 = max(0.0, src_time(s, 0) - 0.05); t1 = src_time(s, sd) + 0.1
    src = os.path.join(KLIP, s["k"] + ".mp4")
    info = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=r_frame_rate",
                           "-of", "csv=p=0", src], capture_output=True, text=True).stdout.strip().split("/")
    fps = float(info[0]) / float(info[1] if len(info) > 1 else 1)
    tw, th = 810, 1440
    vf = f"scale={tw}:{th}:force_original_aspect_ratio=increase,crop={tw}:{th}"
    raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t0:.3f}", "-i", src, "-t", f"{t1 - t0:.3f}", "-an",
                          "-vf", vf, "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True).stdout
    n = len(raw) // (tw * th * 3)
    _clip.update(key=si, frames=np.frombuffer(raw[: n * tw * th * 3], np.uint8).reshape(n, th, tw, 3),
                 t0=t0, fps=fps)


def get_src(ts):
    fr = _clip["frames"]; x = (ts - _clip["t0"]) * _clip["fps"]
    i = int(math.floor(x)); a = x - i
    i0 = min(max(i, 0), len(fr) - 1); i1 = min(i0 + 1, len(fr) - 1)
    if a < 0.08 or i0 == i1: return fr[i0].astype(np.float32)
    return fr[i0].astype(np.float32) * (1 - a) + fr[i1].astype(np.float32) * a   # frame blend (yumusak slow-mo)


# ---------------- renk / doku ----------------
def build_lut():
    x = np.arange(256) / 255.0
    s = x + 0.12 * np.sin(2 * np.pi * x) * -0.5 * 0          # yer tutucu
    s = 1 / (1 + np.exp(-(x - 0.5) * 7.0)); s = (s - s.min()) / (s.max() - s.min())   # S-egri
    s = 0.035 + s * 0.93                                       # kalkik siyah, yumusak beyaz
    r = np.clip(s * 1.04 + 0.01, 0, 1); g = np.clip(s * 0.99, 0, 1); b = np.clip(s * 0.93 + 0.045 * (1 - x), 0, 1)
    return [(c * 255).astype(np.float32) for c in (r, g, b)]


LUT = build_lut()
yy, xx = np.mgrid[0:H, 0:W]
rr = np.sqrt(((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2)
VIG = np.clip(1 - 0.42 * np.clip(rr - 0.5, 0, 1) ** 1.5, 0, 1)[..., None].astype(np.float32)
rng = np.random.default_rng(3)
GR = [rng.normal(0, 5.5, (H // 2, W // 2, 1)).astype(np.float32).repeat(2, 0).repeat(2, 1) for _ in range(8)]


def grade(a):
    """a: HxWx3 float 0-255."""
    lum = (a[..., 0] * 0.3 + a[..., 1] * 0.59 + a[..., 2] * 0.11)[..., None]
    sat = 1.12
    a = lum + (a - lum) * sat
    # kirmiziyi koru, yesili hafif teal'e cek
    a[..., 1] = a[..., 1] * 0.97 + a[..., 2] * 0.03
    idx = np.clip(a, 0, 255).astype(np.uint8)
    out = np.stack([LUT[c][idx[..., c]] for c in range(3)], -1)
    # bloom / halation
    im = Image.fromarray(np.clip(out, 0, 255).astype(np.uint8)).resize((W // 8, H // 8), Image.BILINEAR)
    sm = np.asarray(im).astype(np.float32)
    hl = np.clip(sm - 175, 0, 255) * 1.6
    bl = np.asarray(Image.fromarray(np.clip(hl, 0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(6))
                    .resize((W, H), Image.BILINEAR)).astype(np.float32)
    out = out + bl * np.array([0.55, 0.32, 0.22], np.float32)
    return out


def motion_blur(a, dx, dy, n=7):
    if abs(dx) + abs(dy) < 2: return a
    acc = np.zeros_like(a)
    for k in range(n):
        f = (k / (n - 1) - 0.5)
        acc += np.roll(np.roll(a, int(dx * f), 1), int(dy * f), 0)
    return acc / n


def ease(x): x = max(0.0, min(1.0, x)); return 1 - (1 - x) ** 3



# ---------------- tipografi ----------------
# Ana: Big Shoulders Display Black (dar, sert). Vurgu: Instrument Serif Italic. Etiket: Inter SemiBold, genis aralik.
from PIL import ImageDraw, ImageFont
FD = os.path.join(ROOT, "arac", "font")
F_MAIN = os.path.join(FD, "BigShoulders-Black.ttf")
F_SERIF = os.path.join(FD, "InstrumentSerif-Italic.ttf")
F_LABEL = "/usr/share/fonts/opentype/inter/Inter-SemiBold.otf"
WHITE = (255, 255, 255); RED = (255, 62, 62); SOFT = (255, 244, 236)
YAZISIZ = "--yazisiz" in sys.argv

# (bas_vurus, bitis_vurus, y_merkez_orani, [(tur, yazi, boyut, renk)])
TITLES = [
    (0.6, 3.8, 0.50, [("label", "UEFA ULUSLAR LİGİ  ·  15.11", 34, WHITE), ("serif", "son", 150, SOFT), ("main", "SINAV", 330, WHITE)]),
    (4.4, 7.8, 0.50, [("label", "5 MAÇ  ·  0 PUAN", 34, WHITE), ("serif", "kaybedecek", 130, SOFT), ("main", "BİR ŞEYİMİZ YOK", 170, WHITE)]),
    (10.2, 11.9, 0.70, [("serif", "karşımızda", 120, SOFT), ("main", "MBAPPÉ", 280, WHITE)]),
    (28.2, 31.8, 0.50, [("serif", "bu gece", 140, SOFT), ("main", "PES YOK", 300, WHITE)]),
    (40.2, 41.9, 0.70, [("serif", "haydi", 130, SOFT), ("main", "TÜRKİYE", 270, RED)]),
    (49.0, 55.2, 0.47, [("label", "BORDEAUX  ·  22.45  ·  ATV", 34, WHITE), ("main", "FRANSA", 250, WHITE),
                        ("serif", "ve", 120, SOFT), ("main", "TÜRKİYE", 250, RED)]),
]


def tracked_text(txt, font, color, track):
    """Harf aralikli metin katmani (RGBA), tam bbox ile."""
    asc, desc = font.getmetrics()
    ws = [font.getlength(ch) for ch in txt]
    w = int(sum(ws) + track * (len(txt) - 1)) + 40
    lay = Image.new("RGBA", (w, asc + desc + 40), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    x = 20
    for ch, cw in zip(txt, ws):
        d.text((x, 20), ch, font=font, fill=color + (255,)); x += cw + track
    return lay.crop(lay.getbbox())


def line_layer(kind, txt, size, color):
    if kind == "main":
        t = tracked_text(txt, ImageFont.truetype(F_MAIN, size), color, size * 0.01)
    elif kind == "serif":
        t = tracked_text(txt, ImageFont.truetype(F_SERIF, size), color, 0)
    else:
        t = tracked_text(txt, ImageFont.truetype(F_LABEL, size), color, size * 0.42)
        t.putalpha(t.getchannel("A").point(lambda v: int(v * 0.8)))
    # yumusak golge (kontur yok)
    pad = 40
    out = Image.new("RGBA", (t.width + pad * 2, t.height + pad * 2), (0, 0, 0, 0))
    sh = Image.new("RGBA", out.size, (0, 0, 0, 0)); sh.paste((0, 0, 0, 255), (pad, pad + 6), t)
    sh = sh.filter(ImageFilter.GaussianBlur(14)); sh.putalpha(sh.getchannel("A").point(lambda v: int(v * 0.55)))
    out.alpha_composite(sh); out.alpha_composite(t, (pad, pad))
    return out


GAP = {("label", "serif"): 30, ("label", "main"): 34, ("serif", "main"): -26,
       ("main", "serif"): -6, ("main", "main"): 6}   # satir arasi (onceki, sonraki); serif ana kelimeye hafif biner
_tl = {}


def title_layers(i):
    if i not in _tl:
        _tl[i] = [line_layer(*ln) for ln in TITLES[i][3]]
    return _tl[i]


def draw_titles(img, bt):
    for i, (b0, b1, yc, lines) in enumerate(TITLES):
        if not (b0 <= bt < b1): continue
        lays = title_layers(i)
        hs = [l.height - 80 for l in lays]
        total = sum(hs) + sum(GAP[(lines[j-1][0], lines[j][0])] for j in range(1, len(lines)))
        y = H * yc - total / 2 - 40
        lt = (bt - b0) * B; rem = (b1 - bt) * B
        for k, (lay, ln) in enumerate(zip(lays, lines)):
            if k: y += GAP[(lines[k-1][0], ln[0])]
            d = lt - k * 0.11                         # satir satir giris
            if d <= 0: y += hs[k]; continue
            pin = ease(d / 0.42); pout = min(1.0, rem / 0.22)
            a = pin * pout
            l2 = lay
            blur = (1 - pin) * 16 + (1 - pout) * 10
            if blur > 0.6: l2 = l2.filter(ImageFilter.GaussianBlur(blur))
            sc = 1.06 - 0.06 * pin
            if abs(sc - 1) > 0.003: l2 = l2.resize((int(l2.width * sc), int(l2.height * sc)), Image.BILINEAR)
            if a < 0.999: l2 = l2.copy(); l2.putalpha(l2.getchannel("A").point(lambda v: int(v * a)))
            img.alpha_composite(l2, (int((W - l2.width) / 2), int(y - 40 + (1 - pin) * 26)))
            y += hs[k]
    # kapanista kucuk imza
    if bt >= 50.5 and bt < 55.2:
        a = ease((bt - 50.5) * B / 0.5) * min(1.0, (55.2 - bt) * B / 0.22)
        sig = _tl.setdefault("sig", line_layer("label", "@KONTRA_11", 30, WHITE))
        s2 = sig.copy(); s2.putalpha(s2.getchannel("A").point(lambda v: int(v * a)))
        img.alpha_composite(s2, ((W - s2.width) // 2, int(H * 0.86)))
    return img


def frame(fi):
    t = fi / FPS; bt = t / B
    si = max(i for i, s in enumerate(S) if s["b"] <= bt) if bt < END else len(S) - 1
    s = S[si]; load_shot(s, si)
    lt = (bt - s["b"]) * B; sd = s["n"] * B; p = lt / sd
    a = get_src(src_time(s, lt))
    # kamera: yavas itme + whip girisi + darbe sarsintisi
    zoom = s.get("z", 1.0) * (1.0 + 0.06 * p)
    if s["b"] >= OUTRO: zoom = 1.12 - 0.10 * ease(p)
    ox = 0.0; oy = float(s.get("oy", 0)); mbx = mby = 0.0
    if s.get("whip") and lt < 0.16:
        k = 1 - lt / 0.16; dirn = 1 if si % 2 else -1
        ox = dirn * 140 * k * k; mbx = dirn * 160 * k; zoom += 0.05 * k
    for hb in s.get("hit", []):
        dt = lt - hb * B
        if 0 <= dt < 0.45:
            e = math.exp(-dt * 9); ox += 16 * e * math.sin(fi * 2.7); oy += 16 * e * math.cos(fi * 3.3); zoom += 0.07 * e
    th, tw = a.shape[:2]
    cw, ch = tw / zoom, th / zoom
    x0 = (tw - cw) / 2 + ox * tw / W * 0.5; y0 = (th - ch) / 2 + oy * th / H * 0.5
    x0 = min(max(0, x0), tw - cw); y0 = min(max(0, y0), th - ch)
    im = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)).resize((W, H), Image.BICUBIC, box=(x0, y0, x0 + cw, y0 + ch))
    a = np.asarray(im).astype(np.float32)
    a = motion_blur(a, mbx, mby)
    a = grade(a) * VIG + GR[fi % 8]
    # beyaz flas sadece drop aninda; outro ve giriste siyahtan acilis/kapanis
    if DROP <= bt < DROP + 0.5: a = a + (255 - a) * math.exp(-(bt - DROP) * B * 10) * 0.8
    if t < 0.6: a *= t / 0.6
    if t > TOTAL - 1.4: a *= max(0, (TOTAL - t) / 1.4)
    out = np.clip(a, 0, 255).astype(np.uint8)
    if YAZISIZ: return out
    img = draw_titles(Image.fromarray(out).convert("RGBA"), bt)
    return np.asarray(img.convert("RGB"))


# ---------------- ses: phonk beat + whoosh + impact ----------------
def synth_audio():
    n = int(TOTAL * SR) + SR; out = np.zeros(n, np.float32)
    tt = lambda L: np.arange(L) / SR
    env = lambda L, d: np.exp(-tt(L) / d).astype(np.float32)
    def add(sig, t, g=1.0):
        i = int(t * SR)
        if i >= n: return
        j = min(n, i + len(sig)); out[i:j] += sig[: j - i] * g
    L = int(0.7 * SR); f = 42 + 90 * np.exp(-tt(L) * 30); kick = np.tanh(2.5 * np.sin(2 * np.pi * np.cumsum(f) / SR) * env(L, 0.35))
    def b808(fr, d):
        L = int(d * SR); fq = fr * (1 + 0.6 * np.exp(-tt(L) * 40))
        return np.tanh(3 * np.sin(2 * np.pi * np.cumsum(fq) / SR)) * env(L, d * 0.6) * 0.55
    L = int(0.25 * SR); nz = rng.normal(0, 1, L).astype(np.float32); clap = (nz - np.roll(nz, 1)) * env(L, 0.07) * 0.5
    L = int(0.06 * SR); hz = rng.normal(0, 1, L).astype(np.float32); hat = (hz - np.roll(hz, 1)) * env(L, 0.012) * 0.22
    def cow(fr):
        L = int(0.28 * SR); x = tt(L)
        s = np.sign(np.sin(2 * np.pi * fr * x)) + np.sign(np.sin(2 * np.pi * fr * 1.48 * x))
        return np.tanh(1.5 * s * env(L, 0.09)) * 0.2
    def whoosh(d=0.35):
        L = int(d * SR); z = rng.normal(0, 1, L).astype(np.float32)
        k = int(SR * 0.002); z = np.convolve(z, np.ones(k) / k, "same")
        e = np.sin(np.pi * tt(L) / d) ** 2
        return z * e * 0.9
    def impact():
        L = int(1.0 * SR); f = 30 + 60 * np.exp(-tt(L) * 12)
        return (np.tanh(3 * np.sin(2 * np.pi * np.cumsum(f) / SR)) * env(L, 0.4) * 0.7 + rng.normal(0, 1, L) * env(L, 0.05) * 0.3).astype(np.float32)
    N = {"F#": 370, "A": 440, "C#": 554, "E": 659, "G#": 415, "F#5": 740}
    mel = ["F#", None, "A", "F#", None, "C#", None, "F#", "E", None, "C#", None, "A", None, "G#", None,
           "F#", None, "A", "F#", None, "C#", None, "E", "F#5", None, "E", None, "C#", None, "A", None]
    bassn = [46.25, 46.25, 55.0, 41.2]
    for k in range(END * 4):
        t = k * B / 4; beat = k / 4; s16 = k % 4; bar = int(beat // 4)
        intro = beat < BU; build = BU <= beat < DROP - 1; gap = DROP - 1 <= beat < DROP
        drop = DROP <= beat < OUTRO; outro = beat >= OUTRO
        if gap: continue
        note = mel[k % 32]
        if note and not (outro and beat >= OUTRO + 4): add(cow(N[note]), t, 0.45 if intro else (0.75 if build else 1.0))
        if drop or (outro and beat < OUTRO + 2):
            if s16 == 0 and int(beat) % 2 == 0: add(kick, t, 0.9)
            if s16 == 2 and int(beat) % 4 == 3: add(kick, t, 0.7)
            if s16 == 0 and int(beat) % 4 == 0: add(b808(bassn[bar % 4], 4 * B * 0.9), t, 1.0)
            if s16 == 0 and int(beat) % 2 == 1: add(clap, t, 1.0)
            add(hat, t, 1.0 if s16 % 2 == 0 else 0.55)
        if build:
            if s16 == 0: add(kick, t, 0.4)
            rate = 1 if beat < BU + 4 else (2 if beat < BU + 6 else 4)
            if s16 % (4 // rate) == 0: add(clap, t, 0.3 + 0.5 * (beat - BU) / 7)
    i0, i1 = int(BU * B * SR), int((DROP - 1) * B * SR); L = i1 - i0
    rz = rng.normal(0, 1, L).astype(np.float32); out[i0:i1] += (rz - np.roll(rz, 1)) * np.linspace(0, 0.2, L) ** 1.5 * 2
    add(impact(), DROP * B, 1.0)
    for s in S:   # gecis ve darbe sesleri
        if s.get("whip") and s["b"] != DROP: add(whoosh(), s["b"] * B - 0.17, 0.35)
        for hb in s.get("hit", []):
            if s["b"] + hb != DROP: add(impact(), (s["b"] + hb) * B, 0.45)
    out = np.tanh(out * 1.05) * 0.85
    e = int(TOTAL * SR); fd = int(1.4 * SR); out[e - fd:e] *= np.linspace(1, 0, fd); out[e:] = 0
    fp = os.path.join(TMP, "audio.wav")
    with wave.open(fp, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((out * 32767).astype(np.int16).tobytes())
    return fp


if __name__ == "__main__":
    if "--still" in sys.argv:
        for x in [float(v) for v in sys.argv[sys.argv.index("--still") + 1:]]:
            Image.fromarray(frame(int(x * FPS))).save(os.path.join(TMP, f"still_{x:05.2f}.jpg"), quality=85)
        sys.exit()
    aud = synth_audio()
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
           "-i", aud, "-c:v", "libx264", "-preset", "slow", "-crf", "19", "-maxrate", "14M", "-bufsize", "28M",
           "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", OUT]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for fi in range(NF): p.stdin.write(frame(fi).tobytes())
    p.stdin.close(); p.wait()
    sil = OUT.replace(".mp4", "_sessiz.mp4")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", OUT, "-c:v", "copy", "-an", sil])
    print(OUT, round(TOTAL, 2), "sn")

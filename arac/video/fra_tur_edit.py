"""KONTRA TikTok edit: Fransa - Turkiye (15.11.2026). 1080x1920, 30fps, 130 BPM phonk beat (kodla uretilir, telifsiz).
Calistir: python3 arac/video/fra_tur_edit.py  ->  g/fra_tur_edit.mp4
Kesimler 130 BPM vurusuna oturur; TikTok'ta 130 BPM civari bir ses secilirse kesimler o sese de oturur.
"""
import sys, os, math, subprocess, wave
import numpy as np
sys.path.insert(0, "/home/claude/font")
from kart import text_layer, K_POLYS, ANTON, BEBAS, NAVY, WHITE
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageOps

W, H, FPS = 1080, 1920, 30
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FOTO = os.path.join(ROOT, "foto")
OUT = os.path.join(ROOT, "g", "fra_tur_edit.mp4")
TMP = "/tmp/claude-0/edit"; os.makedirs(TMP, exist_ok=True)
BPM = 130; B = 60 / BPM; BAR = 4 * B
KIRMIZI = (227, 10, 23); MAVI = (60, 110, 255)
SR = 44100

# ---------------- gorseller ----------------
FOCUS = {
    "fransa_10_sevinc": (0.45, 0.62), "fransa_sirt_mbappe_dembele": (0.5, 0.55), "doue_dis_italya": (0.62, 0.5),
    "fransa_11_20_diz": (0.5, 0.6), "fransa_11_7_10_12": (0.5, 0.5), "milli_gol_sevinci_8_10_18_21": (0.5, 0.6),
    "milli_8_sut_euro2024": (0.5, 0.5), "milli_beyaz_bayrak_11_9_8": (0.62, 0.5), "sergen_yalcin_milli": (0.5, 0.45),
    "hakan_calhanoglu_inter_sirt": (0.5, 0.62), "milli_8_uzgun_ispanya": (0.35, 0.5),
}
_cache = {}


def grade(im, mode):
    if mode == "fra":      # soguk, mavi, hafif soluk
        im = ImageEnhance.Color(im).enhance(0.55); a = np.asarray(im).astype(np.float32)
        a = a * [0.82, 0.92, 1.12] + [0, 4, 18]
    elif mode == "tur":    # sicak, kirmizi patlayan, kontrast
        im = ImageEnhance.Contrast(ImageEnhance.Color(im).enhance(1.35)).enhance(1.18); a = np.asarray(im).astype(np.float32)
        a = a * [1.12, 0.93, 0.88] + [6, 0, -4]
    else:                  # dark: siyah-beyaza yakin, koyu
        im = ImageEnhance.Color(im).enhance(0.15); a = np.asarray(im).astype(np.float32) * 0.72
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))


def big(name, mode):
    """9:16'ya kirpilmis, 1.3x buyuk, renk islenmis kaynak (zoom/shake payi icin)."""
    key = (name, mode)
    if key in _cache: return _cache[key]
    im = Image.open(os.path.join(FOTO, name + ".jpg")).convert("RGB")
    fx, fy = FOCUS[name]; tw, th = int(W * 1.3), int(H * 1.3)
    s = max(tw / im.width, th / im.height); im = im.resize((int(im.width * s) + 1, int(im.height * s) + 1), Image.LANCZOS)
    x = min(max(0, int(im.width * fx - tw / 2)), im.width - tw); y = min(max(0, int(im.height * fy - th / 2)), im.height - th)
    im = grade(im.crop((x, y, x + tw, y + th)), mode)
    _cache[key] = im
    return im


# ---------------- video klip destegi ----------------
# Shot'taki isim "klip:dosya@baslangic_sn" ya da "klip:dosya@baslangic_sn@hiz" ise klip/<dosya>.mp4'ten okunur.
# hiz < 1 = slow-motion (0.5 = yari hiz). Kareler sirayla, ffmpeg borusundan akar.
KLIP = os.path.join(ROOT, "klip")
_pipe = {"key": None, "proc": None}


def klip_frame(spec, mode, shot_key, n_frames):
    """Bu shot icin sradaki klip karesini 1.3x buyuk, renk islenmis PIL olarak dondurur."""
    parts = spec[5:].split("@"); fn = parts[0]; st = float(parts[1]) if len(parts) > 1 else 0.0
    spd = float(parts[2]) if len(parts) > 2 else 1.0
    tw, th = int(W * 1.3) // 2 * 2, int(H * 1.3) // 2 * 2
    if _pipe["key"] != shot_key:
        if _pipe["proc"]: _pipe["proc"].kill()
        src = next(os.path.join(KLIP, f) for f in os.listdir(KLIP) if os.path.splitext(f)[0] == fn)
        vf = (f"setpts=PTS/{spd},fps={FPS},scale={tw}:{th}:force_original_aspect_ratio=increase,crop={tw}:{th}")
        _pipe["proc"] = subprocess.Popen(["ffmpeg", "-v", "error", "-ss", str(st), "-i", src, "-an", "-vf", vf,
                                          "-frames:v", str(n_frames + 2), "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
                                         stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        _pipe["key"] = shot_key; _pipe["last"] = None
    raw = _pipe["proc"].stdout.read(tw * th * 3)
    if len(raw) == tw * th * 3:
        _pipe["last"] = grade(Image.frombytes("RGB", (tw, th), raw), mode)
    return _pipe["last"]


# vinyet + grain
yy, xx = np.mgrid[0:H, 0:W]
r = np.sqrt(((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2)
VIG = np.clip(1 - 0.55 * np.clip(r - 0.45, 0, 1) ** 1.6, 0, 1)[..., None].astype(np.float32)
rng = np.random.default_rng(7)
GRAINS = [rng.normal(0, 9, (H // 2, W // 2, 1)).astype(np.float32).repeat(2, 0).repeat(2, 1) for _ in range(6)]


# ---------------- yazilar ----------------
def stroke_text(txt, size, color, font=ANTON, shear=0.18, stroke=10, track=2):
    base = text_layer(txt, font, size, color, track=track, shear=shear)
    a = base.getchannel("A")
    pad = stroke * 2
    out = Image.new("RGBA", (base.width + pad * 2, base.height + pad * 2), (0, 0, 0, 0))
    m = Image.new("L", out.size, 0); m.paste(a, (pad, pad)); m = m.filter(ImageFilter.MaxFilter(stroke * 2 + 1))
    out.paste(Image.new("RGBA", out.size, (0, 0, 0, 255)), (0, 0), m)
    out.alpha_composite(base, (pad, pad))
    return out


def logo_layer(size=70):
    S = size * 4
    lay = Image.new("RGBA", (S, S), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.rounded_rectangle((0, 0, S - 1, S - 1), radius=int(S * 0.22), fill=NAVY + (255,), outline=WHITE + (255,), width=int(S * 0.04))
    k = S * 1.25 / 800; off = -S * 0.125
    for p in K_POLYS: d.polygon([(px * k + off, py * k + off) for px, py in p], fill=WHITE + (255,))
    lg = lay.resize((size, size), Image.LANCZOS)
    wl = text_layer("KONTRA", ANTON, int(size * 0.62), WHITE, track=4, shear=0.2)
    out = Image.new("RGBA", (size + 16 + wl.width, size), (0, 0, 0, 0))
    out.alpha_composite(lg, (0, 0)); out.alpha_composite(wl, (size + 16, (size - wl.height) // 2))
    return out


LOGO = logo_layer(64)
_tcache = {}


def T(txt, size=170, color=WHITE, font=ANTON, shear=0.18):
    k = (txt, size, color, font, shear)
    if k not in _tcache: _tcache[k] = stroke_text(txt, size, color, font, shear)
    return _tcache[k]


# ---------------- kurgu (zaman: vurus cinsinden) ----------------
# (bas_vurus, vurus_sayisi, foto|None, mod, [ (yazi, boyut, renk, y, gecikme_vurus) ], efekt)
I0 = 0; BU = 8; DROP = 16; OUTRO = 48; END = 56
OUT = os.path.join(ROOT, "g", "fra_tur_edit_klipli.mp4")
SHOTS = [
    (0, 4, "klip:k5_dortmund_taraftar@2.0@0.5", "dark", [("5 MAÇ.", 190, WHITE, 0.40, 0), ("0 PUAN.", 190, KIRMIZI, 0.52, 2)], "slow"),
    (4, 4, "sergen_yalcin_milli", "dark", [("SON", 230, WHITE, 0.36, 0), ("ŞANS.", 230, KIRMIZI, 0.49, 1.5)], "slow"),
    (8, 2, "fransa_10_sevinc", "fra", [("MBAPPÉ", 200, WHITE, 0.72, 0)], "build"),
    (10, 2, "fransa_sirt_mbappe_dembele", "fra", [("10 PUAN", 190, WHITE, 0.72, 0)], "build"),
    (12, 1, "doue_dis_italya", "fra", [("DOUÉ", 200, WHITE, 0.72, 0)], "build"),
    (13, 1, "fransa_11_20_diz", "fra", [], "build"),
    (14, 0.5, "fransa_11_7_10_12", "fra", [], "build"),
    (14.5, 0.5, "fransa_10_sevinc", "fra", [], "build"),
    (15, 1, None, "black", [("AMA...", 210, WHITE, 0.46, 0)], "none"),
    # ---- DROP: hepsi video kesiti ----
    (16, 2, "klip:k6_kerem@0.0", "tur", [("AY", 260, WHITE, 0.30, 0), ("YILDIZ", 260, KIRMIZI, 0.43, 0.5)], "drop"),
    (18, 2, "klip:k8_arda_euro@3.7@0.5", "tur", [("PES", 260, WHITE, 0.70, 0), ("YOK.", 260, KIRMIZI, 0.83, 0.5)], "drop"),
    (20, 1, "klip:k8_arda_euro@5.5", "tur", [], "drop"),
    (21, 1, "klip:k6_kerem@3.0", "tur", [], "drop"),
    (22, 2, "klip:k2_arda_dortmund@3.0", "tur", [("BİZ", 330, WHITE, 0.72, 0)], "drop"),
    (24, 1, "klip:k10_milli_mac@4.0", "tur", [], "drop"),
    (25, 1, "klip:k9_futbolcular@22.0", "tur", [], "drop"),
    (26, 1, "klip:k9_futbolcular@24.0", "tur", [], "drop"),
    (27, 0.5, "klip:k6_kerem@12.9", "tur", [], "drop"),
    (27.5, 0.5, "klip:k10_milli_mac@2.6", "tur", [], "drop"),
    (28, 4, "klip:k5_dortmund_taraftar@6.0@0.6", "tur", [("90", 420, WHITE, 0.62, 0), ("DAKİKA", 200, KIRMIZI, 0.80, 1)], "push"),
    (32, 2, "klip:k9_futbolcular@18.9@0.6", "tur", [("İNAN.", 280, WHITE, 0.72, 0)], "drop"),
    (34, 1, "klip:k1_milli@1.3", "tur", [], "drop"),
    (35, 1, "klip:k6_kerem@4.2", "tur", [], "drop"),
    (36, 1, "klip:k10_milli_mac@0.0", "tur", [], "drop"),
    (37, 1, "klip:k1_milli@9.1", "tur", [], "drop"),
    (38, 2, "klip:k9_futbolcular@29.5", "tur", [("HAYDİ", 230, WHITE, 0.70, 0)], "drop"),
    (40, 2, "klip:k6_kerem@21.0", "tur", [], "drop"),
    (42, 1, "klip:k8_arda_euro@5.9", "tur", [], "drop"),
    (43, 1, "klip:k10_milli_mac@12.0", "tur", [], "drop"),
    (44, 2, "klip:k2_arda_dortmund@6.0", "tur", [("TÜRKİYE", 220, KIRMIZI, 0.72, 0)], "drop"),
    (46, 1, "klip:k1_milli@14.4", "tur", [], "drop"),
    (47, 1, "klip:k9_futbolcular@26.0", "tur", [], "drop"),
    # ---- OUTRO ----
    (48, 8, "klip:k5_dortmund_taraftar@0.0@0.5", "tur", [("FRANSA", 190, WHITE, 0.30, 0.5), ("TÜRKİYE", 190, KIRMIZI, 0.40, 1.5),
                                                          ("BU AKŞAM 22.45", 92, WHITE, 0.52, 2.5)], "outro"),
]
TOTAL = END * B + 0.4
NF = int(TOTAL * FPS)


def ease(x): x = max(0.0, min(1.0, x)); return 1 - (1 - x) ** 3


def frame(fi):
    t = fi / FPS; bt = t / B
    shot = SHOTS[-1]
    for s in SHOTS:
        if s[0] <= bt < s[0] + s[1]: shot = s; break
    b0, nb, name, mode, texts, fx = shot
    lt = (bt - b0) * B; sd = nb * B; p = lt / sd
    since_beat = (bt % 1) * B
    since_cut = lt
    # --- kamera ---
    zoom, ox, oy, rgb, flash = 1.0, 0.0, 0.0, 0, 0.0
    if fx == "slow": zoom = 1.0 + 0.10 * p
    elif fx == "build": zoom = 1.05 + 0.10 * p; rgb = int(8 * math.exp(-since_cut * 10))
    elif fx == "drop":
        zoom = 1.04 + 0.05 * p + 0.13 * math.exp(-since_beat * 9)
        sh = 22 * math.exp(-since_beat * 11)
        ox = sh * math.sin(fi * 2.3); oy = sh * math.cos(fi * 3.1)
        rgb = int(26 * math.exp(-since_beat * 12)); flash = 0.85 * math.exp(-since_cut * 14)
    elif fx == "push": zoom = 1.0 + 0.22 * ease(p); rgb = int(18 * math.exp(-since_beat * 12)) if bt % 2 < 1 else 0
    elif fx == "outro": zoom = 1.25 - 0.20 * ease(p * 1.4); flash = 0.9 * math.exp(-since_cut * 6)
    if mode == "black":
        frame_a = np.zeros((H, W, 3), np.float32)
    else:
        src = (klip_frame(name, mode, (b0, name), int(sd * FPS) + 1) if name.startswith("klip:") else big(name, mode))
        cw, ch = W * 1.3 / zoom, H * 1.3 / zoom
        cx0 = (src.width - cw) / 2 + ox; cy0 = (src.height - ch) / 2 + oy
        im = src.resize((W, H), Image.BILINEAR, box=(cx0, cy0, cx0 + cw, cy0 + ch))
        frame_a = np.asarray(im).astype(np.float32)
        if rgb:
            frame_a[:, :, 0] = np.roll(frame_a[:, :, 0], rgb, axis=1); frame_a[:, :, 2] = np.roll(frame_a[:, :, 2], -rgb, axis=1)
    frame_a = frame_a * VIG + GRAINS[fi % 6]
    if flash > 0.01: frame_a = frame_a * (1 - flash) + 255 * flash
    if fx == "outro" and p > 0.82: frame_a *= max(0, 1 - (p - 0.82) / 0.18)
    im = Image.fromarray(np.clip(frame_a, 0, 255).astype(np.uint8)).convert("RGBA")
    # --- yazilar: vurusta "pop" ---
    for (txt, size, col, yr, dl) in texts:
        tl = lt - dl * B
        if tl < 0: continue
        pop = 1 + 0.35 * math.exp(-tl * 14)
        if fx == "outro" and p > 0.82: continue
        lay = T(txt, size, col)
        if abs(pop - 1) > 0.01: lay = lay.resize((int(lay.width * pop), int(lay.height * pop)), Image.BILINEAR)
        jx = int(6 * math.sin(fi * 2.1) * math.exp(-tl * 6)) if fx in ("drop", "push") else 0
        im.alpha_composite(lay, ((W - lay.width) // 2 + jx, int(H * yr - lay.height / 2)))
    if fx == "outro" and lt > 3.5 * B and p <= 0.82:
        a = ease((lt - 3.5 * B) / 0.4); lg = LOGO.copy(); lg.putalpha(lg.getchannel("A").point(lambda v: int(v * a)))
        im.alpha_composite(lg, ((W - lg.width) // 2, int(H * 0.88)))
    im.alpha_composite(T("@KONTRA_11", 44, WHITE, BEBAS, 0), (W - 60 - T("@KONTRA_11", 44, WHITE, BEBAS, 0).width, 120))
    return im.convert("RGB")


# ---------------- muzik: 130 BPM phonk (cowbell + 808 + clap + hat) ----------------
def synth_beat():
    n = int(TOTAL * SR) + SR; out = np.zeros(n, np.float32)
    def env(L, d): return np.exp(-np.arange(L) / SR / d).astype(np.float32)
    def add(sig, t, g=1.0):
        i = int(t * SR); j = min(n, i + len(sig)); out[i:j] += sig[: j - i] * g
    tt = lambda L: np.arange(L) / SR
    # sesler
    L = int(0.7 * SR); f = 42 + 90 * np.exp(-tt(L) * 30); ph = 2 * np.pi * np.cumsum(f) / SR
    kick = np.tanh(2.5 * np.sin(ph) * env(L, 0.35))
    def bass808(freq, dur):
        L = int(dur * SR); fq = freq * (1 + 0.6 * np.exp(-tt(L) * 40)); ph = 2 * np.pi * np.cumsum(fq) / SR
        return np.tanh(3 * np.sin(ph)) * env(L, dur * 0.6) * 0.55
    L = int(0.25 * SR); nz = rng.normal(0, 1, L).astype(np.float32)
    clap = (nz - np.roll(nz, 1)) * env(L, 0.07) * 0.5
    L = int(0.06 * SR); hz = rng.normal(0, 1, L).astype(np.float32); hat = (hz - np.roll(hz, 1)) * env(L, 0.012) * 0.25
    def cowbell(freq):
        L = int(0.28 * SR); x = tt(L)
        s = np.sign(np.sin(2 * np.pi * freq * x)) + np.sign(np.sin(2 * np.pi * freq * 1.48 * x))
        return np.tanh(1.5 * s * env(L, 0.09)) * 0.22
    # F# minor phonk melodi (16'liklarda), 2 bar
    N = {"F#": 370, "A": 440, "C#": 554, "E": 659, "D": 587, "B": 494, "G#": 415, "F#5": 740}
    mel = ["F#", None, "A", "F#", None, "C#", None, "F#", "E", None, "C#", None, "A", None, "G#", None,
           "F#", None, "A", "F#", None, "C#", None, "E", "F#5", None, "E", None, "C#", None, "A", None]
    bass_notes = [46.25, 46.25, 55.0, 41.2]  # F#1 F#1 A1 E1 (bar basi)
    for k in range(END * 4):          # 16'liklar
        t = k * B / 4; beat = k / 4; s16 = k % 4
        if beat >= END: break
        bar = int(beat // 4)
        note = mel[k % 32]
        intro = beat < BU; build = BU <= beat < DROP - 1; gap = DROP - 1 <= beat < DROP
        drop = DROP <= beat < OUTRO; outro = beat >= OUTRO
        if gap: continue
        if note and not (outro and beat >= OUTRO + 4):
            g = 0.55 if intro else (0.8 if build else 1.0)
            add(cowbell(N[note]), t, g)
        if drop or (outro and beat < OUTRO + 2):
            if s16 == 0 and int(beat) % 2 == 0: add(kick, t, 0.9)
            if s16 == 2 and int(beat) % 4 == 3: add(kick, t, 0.7)
            if s16 == 0 and int(beat) % 4 == 0: add(bass808(bass_notes[bar % 4], BAR * 0.9), t, 1.0)
            if s16 == 0 and int(beat) % 2 == 1: add(clap, t, 1.0)
            add(hat, t, 1.0 if s16 % 2 == 0 else 0.6)
            if int(beat) % 8 == 7 and s16 in (1, 3): add(hat, t + B / 8, 0.8)  # hat roll
        if build:
            if s16 == 0: add(kick, t, 0.45)
            rate = 1 if beat < BU + 4 else (2 if beat < BU + 6 else 4)   # hizlanan clap
            if s16 % (4 // rate) == 0: add(clap, t, 0.35 + 0.5 * (beat - BU) / 7)
    # riser (build boyunca)
    i0, i1 = int(BU * B * SR), int((DROP - 1) * B * SR); L = i1 - i0
    rz = rng.normal(0, 1, L).astype(np.float32); rz = rz - np.roll(rz, 1)
    out[i0:i1] += rz * np.linspace(0, 0.18, L) ** 1.5 * 2
    # drop'ta impact
    L = int(1.2 * SR); out[int(DROP * B * SR): int(DROP * B * SR) + L] += (kick[:L] if len(kick) >= L else np.pad(kick, (0, L - len(kick)))) * 0.6
    out = np.tanh(out * 1.1) * 0.85
    fade = int(1.0 * SR); e = int(TOTAL * SR); out[e - fade:e] *= np.linspace(1, 0, fade); out[e:] = 0
    fp = os.path.join(TMP, "beat.wav")
    with wave.open(fp, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((out * 32767).astype(np.int16).tobytes())
    return fp


if __name__ == "__main__":
    if "--still" in sys.argv:
        for x in [float(v) for v in sys.argv[sys.argv.index("--still") + 1:]]:
            frame(int(x * FPS)).save(os.path.join(TMP, f"still_{x:05.2f}.jpg"), quality=85)
        sys.exit()
    beat = synth_beat()
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
           "-i", beat, "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-maxrate", "14M", "-bufsize", "28M", "-pix_fmt", "yuv420p",
           "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", OUT]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for fi in range(NF): p.stdin.write(frame(fi).tobytes())
    p.stdin.close(); p.wait()
    print(OUT, round(TOTAL, 2), "sn")

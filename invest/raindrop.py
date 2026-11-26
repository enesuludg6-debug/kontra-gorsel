#!/usr/bin/env python3
"""raindrop.py — hacim ağırlıklı 'yağmur damlası' mumları (TrendSpider Raindrop karşılığı).
Kullanım: python3 invest/raindrop.py <T> [--gun 30] [--out g/x.png]
Her gün iki yarıya bölünür (ABD seansı ilk/ikinci yarı, saatlik veriden). Her yarı için fiyat seviyelerinde işlem gören hacim
dağılımı damla şeklinde çizilir (sol yarı = sabah, sağ yarı = öğleden sonra). Çizgiler her yarının VWAP'ı.
Renk: ikinci yarının VWAP'ı ilkinden yüksekse yeşil (alıcı gün içinde güçlendi), düşükse kırmızı.
Okuma: damlanın şişkin olduğu yer = hacmin yoğunlaştığı fiyat (kabul bölgesi); uzun ince kuyruk = reddedilen fiyat.
"""
import sys, warnings
import numpy as np, pandas as pd
warnings.filterwarnings("ignore")
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
from smc_ek import gun_ici

def main():
    a = sys.argv[1:]; t = a[0] if a else "^NDX"; n = int(a[a.index("--gun") + 1]) if "--gun" in a else 30
    out = a[a.index("--out") + 1] if "--out" in a else f"/tmp/raindrop_{t.strip('^')}.png"
    d = gun_ici(t, "1h"); d = d[d.volume > 0] if d.volume.sum() else d.assign(volume=1.0)
    d["gun"] = d.index.date; gunler = sorted(set(d.gun))[-n:]
    fig, ax = plt.subplots(figsize=(10.8, 6.8), dpi=100); fig.patch.set_facecolor("#0b0f14"); ax.set_facecolor("#0b0f14")
    for k, g_ in enumerate(gunler):
        s = d[d.gun == g_]
        if len(s) < 2: continue
        yar = [s.iloc[:len(s) // 2 + len(s) % 2], s.iloc[len(s) // 2 + len(s) % 2:]]
        vw = [(z.close * z.volume).sum() / z.volume.sum() if len(z) else np.nan for z in yar]
        renk = "#35d0a5" if vw[1] >= vw[0] else "#ff5c5c"
        lo, hi = s.low.min(), s.high.max(); bins = np.linspace(lo, hi, 25); mids = (bins[:-1] + bins[1:]) / 2
        for taraf, z in enumerate(yar):
            if not len(z): continue
            prof = np.zeros(len(mids))
            for _, r in z.iterrows():   # her saatin hacmini o saatin aralığına yay
                m = (mids >= r.low) & (mids <= r.high); prof[m] += r.volume / max(1, m.sum())
            prof = prof / (prof.max() + 1e-12) * 0.42
            x0 = k + (0 if taraf == 0 else 0.0); sgn = -1 if taraf == 0 else 1
            ax.fill_betweenx(mids, x0, x0 + sgn * prof, color=renk, alpha=.85 if taraf else .55, lw=0)
            ax.plot([x0 + sgn * .02, x0 + sgn * .42], [vw[taraf]] * 2, color="white", lw=1)
    ax.set_xticks(range(0, len(gunler), max(1, len(gunler) // 8)))
    ax.set_xticklabels([pd.Timestamp(gunler[i]).strftime("%d.%m") for i in range(0, len(gunler), max(1, len(gunler) // 8))], color="#9aa")
    ax.tick_params(colors="#9aa"); [s_.set_color("#223") for s_ in ax.spines.values()]; ax.yaxis.tick_right()
    ax.set_title(f"{t} • yağmur damlası (hacim dağılımı, sabah | öğleden sonra) • {len(gunler)} gün", color="white", loc="left", fontsize=13)
    fig.text(.01, .01, "yeşil: öğleden sonra VWAP > sabah VWAP • beyaz çizgi: yarım gün VWAP", color="#889", fontsize=9)
    fig.text(.99, .01, "ENES ULUDAĞ", color="#667", ha="right", fontsize=9, weight="bold")
    fig.tight_layout(); fig.savefig(out, facecolor=fig.get_facecolor()); print(f"raindrop: {out}")

if __name__ == "__main__":
    main()

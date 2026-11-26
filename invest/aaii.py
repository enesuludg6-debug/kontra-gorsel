#!/usr/bin/env python3
"""aaii.py — kural 91: AAII bireysel yatırımcı duygu anketi, haftada 2 tweet (Enes 26.11 08:45).
Veri: WebFetch https://www.aaii.com/sentimentsurvey ; istem: "son haftanın tarihi, boğa/nötr/ayı %, önceki haftaya göre değişim,
      tarihsel ortalamalar ve sayfadaki geçmiş tablo satırları 'MM/DD/YYYY,boğa,nötr,ayı' CSV; yorum yok"
Kullanım:
  python3 invest/aaii.py ekle < satirlar.csv      (MM/DD/YYYY,boga,notr,ayi)
  python3 invest/aaii.py ozet                     son hafta, değişim, boğa-ayı farkı, tarihsel ortalamaya uzaklık, kaç haftadır ayı > ortalama, yeni veri var mı
  python3 invest/aaii.py kart g/YYYYMMDD_HHMM_aaii.jpg [--tip yeni|perspektif]
Tarihsel ortalamalar (AAII, 1987'den): boğa %37,5, nötr %31,0, ayı %31,5. Boğa-ayı farkı ortalaması ~+6.
"""
import sys, os, io, json, datetime as dt
import pandas as pd, numpy as np
D = os.path.dirname(os.path.abspath(__file__)); SERI = os.path.join(D, "alt_veri", "aaii.csv"); SON = os.path.join(D, "alt_veri", "aaii_son_tweet.json")
ORT = {"boga": 37.5, "notr": 31.0, "ayi": 31.5}

def oku():
    if not os.path.exists(SERI): return pd.DataFrame(columns=["t", "boga", "notr", "ayi"])
    s = pd.read_csv(SERI); return s.drop_duplicates("t", keep="last").sort_values("t").reset_index(drop=True)

def ekle(metin):
    y = pd.read_csv(io.StringIO(metin.strip()), header=None, names=["t", "boga", "notr", "ayi"])
    y["t"] = pd.to_datetime(y.t, format="%m/%d/%Y").dt.strftime("%Y-%m-%d")
    s = pd.concat([oku(), y]).drop_duplicates("t", keep="last").sort_values("t"); s.to_csv(SERI, index=False)
    print(f"AAII {len(s)} hafta, son {s.iloc[-1].t}: boğa {s.iloc[-1].boga} ayı {s.iloc[-1].ayi}")

def ozet():
    s = oku(); r = s.iloc[-1]; o = s.iloc[-2] if len(s) > 1 else None; fark = r.boga - r.ayi
    print(f"SON HAFTA {r.t}: boğa %{r.boga} | nötr %{r.notr} | ayı %{r.ayi} | boğa-ayı farkı {fark:+.1f} (tarihsel ~+6)")
    if o is not None: print(f"önceki hafta {o.t}: boğa {r.boga - o.boga:+.1f} puan, ayı {r.ayi - o.ayi:+.1f} puan")
    print(f"tarihsel ortalamaya göre: boğa {r.boga - ORT['boga']:+.1f}, ayı {r.ayi - ORT['ayi']:+.1f} puan")
    n = 0
    for v in s.ayi[::-1]:
        if v > ORT["ayi"]: n += 1
        else: break
    print(f"ayı oranı {n} haftadır üst üste tarihsel ortalamanın üstünde")
    if len(s) >= 4: print(f"4 hafta ortalama: boğa %{s.boga.tail(4).mean():.1f}, ayı %{s.ayi.tail(4).mean():.1f}")
    uc = "AŞIRI KARAMSAR (ayı ≥%50 ya da fark ≤−20)" if r.ayi >= 50 or fark <= -20 else "AŞIRI İYİMSER (boğa ≥%50 ya da fark ≥+30)" if r.boga >= 50 or fark >= 30 else "uç değil"
    print(f"uç durum: {uc}")
    son = json.load(open(SON)) if os.path.exists(SON) else {}
    print("YENİ HAFTA VAR -> 'yeni' tweet" if son.get("yeni") != r.t else f"yeni hafta yok (son tweetlenen {son.get('yeni')}) -> 'yeni' tweet atma")

def kart(out, tip="yeni"):
    import kart3 as K
    import matplotlib.dates as mdates
    s = oku(); r = s.iloc[-1]; fark = r.boga - r.ayi
    tarih = dt.date.fromisoformat(r.t); alt = f"Haftalık anket • {tarih.day:02d}.{tarih.month:02d}.{tarih.year} haftası"
    baslik = (f"Bireysel yatırımcıda ayı oranı %{r.ayi:.0f}".replace(".", ",") if r.ayi >= r.boga else f"Bireysel yatırımcıda boğa oranı %{r.boga:.0f}")
    sonuc = f"Boğa-ayı farkı {fark:+.0f} puan; tarihsel ortalama yaklaşık +6".replace("+-", "−").replace("-", "−")
    if tip == "perspektif" and len(s) >= 4:
        neg = 0
        for v in (s.boga - s.ayi)[::-1]:
            if v < 0: neg += 1
            else: break
        baslik = f"Boğa-ayı farkı {neg} haftadır eksi" if neg >= 2 else baslik
        alt = "Boğa eksi ayı, puan • " + alt
    fig, rr = K.cerceve("Piyasa nabzı • AAII anketi", baslik, alt, sonuc, "AAII Sentiment Survey")
    if tip == "perspektif" and len(s) >= 4:
        ax = K._ax(fig, rr, (0.04, 0.06, 0.10, 0.02))
        x = [dt.date.fromisoformat(t) for t in s.t]; f_ = (s.boga - s.ayi).values
        ax.bar(x, f_, width=5, color=[K.UP if v >= 0 else K.DOWN for v in f_])
        ax.axhline(6, color=K.GOLD, lw=1.6, ls=(0, (2, 3))); ax.text(x[-1], 7.5, "tarihsel ort. +6", color=K.GOLD, fontsize=16, family=K.FAM, fontweight="bold", ha="right")
        ax.axhline(0, color=K.GREY, lw=1.2); ax.yaxis.tick_right()
        ax.set_xticks(x); ax.set_xticklabels([f"{d.day:02d}.{d.month:02d}" for d in x])
        for xi, v in zip(x, f_): ax.text(xi, v + (1 if v >= 0 else -1), f"{v:+.0f}".replace("-", "−"), ha="center", va="bottom" if v >= 0 else "top", fontsize=18, color=K.INK, family=K.FAM, fontweight="bold")
        ax.set_ylim(min(f_.min() - 5, -2), max(f_.max() + 5, 10))
    else:
        ax = K._ax(fig, rr, (0.16, 0.06, 0.06, 0.02)); ax.grid(False); ax.set_xticks([])
        satir = [("Bu hafta", r.boga, r.notr, r.ayi)]
        if len(s) > 1: o = s.iloc[-2]; satir.append(("Geçen hafta", o.boga, o.notr, o.ayi))
        satir.append(("Tarihsel ort.", ORT["boga"], ORT["notr"], ORT["ayi"]))
        for i, (et, b, n_, a) in enumerate(satir[::-1]):
            for sol, w, c, ad in ((0, b, K.UP, "boğa"), (b, n_, K.GREY, "nötr"), (b + n_, a, K.DOWN, "ayı")):
                ax.barh(i, w, left=sol, color=c, height=0.6)
                ax.text(sol + w / 2, i, f"{ad} %{w:.0f}".replace(".", ","), ha="center", va="center", fontsize=17, color="white", family=K.FAM, fontweight="bold")
        ax.set_yticks(range(len(satir))); ax.set_yticklabels([z[0] for z in satir[::-1]], fontsize=20, color=K.INK, fontweight="bold"); ax.set_xlim(0, 100)
    K.kaydet(fig, out); print("kart:", out)

def tweetlendi(tip, t, buf):
    j = json.load(open(SON)) if os.path.exists(SON) else {}; j[tip] = t; j[f"{tip}_buffer"] = buf; json.dump(j, open(SON, "w")); print("kaydedildi", j)

if __name__ == "__main__":
    a = sys.argv[1:]
    if not a: print(__doc__)
    elif a[0] == "ekle": ekle(sys.stdin.read())
    elif a[0] == "ozet": ozet()
    elif a[0] == "kart": kart(a[1], a[a.index("--tip") + 1] if "--tip" in a else "yeni")
    elif a[0] == "tweetlendi": tweetlendi(a[1], a[2], a[3])

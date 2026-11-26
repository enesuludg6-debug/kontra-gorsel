#!/usr/bin/env python3
"""korku.py — kural 90: CNN Korku-Açgözlülük endeksi günlük kısa tweeti (Enes 26.11 08:40).
Veri: WebFetch https://production.dataviz.cnn.io/index/fearandgreed/graphdata
      istem: "fear_and_greed_historical'dan son 70 günü 'YYYY-MM-DD,skor' CSV ver (ms -> UTC tarih, 1 ondalık), eskiden yeniye; ayrıca güncel skor ve zaman damgası"
Kullanım:
  python3 invest/korku.py ekle < seri.csv        seriyi alt_veri/korku_seri.csv ile birleştirir (aynı gün = son değer)
  python3 invest/korku.py ozet                    son değer, bölge, 1 hafta/1 ay önce, bölge değişimi, 3 ay dip/zirve, tweet gerekli mi
  python3 invest/korku.py kart g/YYYYMMDD_1040_korku.jpg
Bölgeler (CNN): 0-24 aşırı korku, 25-44 korku, 45-55 nötr, 56-75 açgözlülük, 76-100 aşırı açgözlülük.
"""
import sys, os, io, json
import pandas as pd
D = os.path.dirname(os.path.abspath(__file__)); SERI = os.path.join(D, "alt_veri", "korku_seri.csv"); SON = os.path.join(D, "alt_veri", "korku_son_tweet.json")
def bolge(v): return "aşırı korku" if v < 25 else "korku" if v < 45 else "nötr" if v <= 55 else "açgözlülük" if v <= 75 else "aşırı açgözlülük"
def oku():
    s = pd.read_csv(SERI, header=None, names=["t", "v"]); s = s.drop_duplicates("t", keep="last").sort_values("t"); return s.reset_index(drop=True)
def ekle(metin):
    y = pd.read_csv(io.StringIO(metin.strip()), header=None, names=["t", "v"])
    s = pd.concat([oku(), y]) if os.path.exists(SERI) else y
    s.drop_duplicates("t", keep="last").sort_values("t").to_csv(SERI, header=False, index=False); print(f"seri {len(oku())} gün, son {oku().iloc[-1].t} {oku().iloc[-1].v}")
def ozet():
    s = oku(); r = s.iloc[-1]; v = r.v; t = r.t
    h = s.iloc[-6].v if len(s) > 5 else None; a = s.iloc[-22].v if len(s) > 21 else None; once = s.iloc[-2].v
    s3 = s.tail(63); dip = s3.loc[s3.v.idxmin()]; zir = s3.loc[s3.v.idxmax()]
    son = json.load(open(SON)) if os.path.exists(SON) else {}
    print(f"SON {t}: {v:.1f} ({bolge(v)}) | önceki gün {once:.1f} ({bolge(once)}) | 1 hafta önce {h:.1f} | 1 ay önce {a:.1f}")
    print(f"3 ay: dip {dip.v:.1f} ({dip.t}), zirve {zir.v:.1f} ({zir.t})")
    if bolge(v) != bolge(once): print(f"BÖLGE DEĞİŞTİ: {bolge(once)} -> {bolge(v)} (tweetin ana konusu bu)")
    if v <= dip.v: print("3 AYIN DİBİ (tweetin ana konusu bu)")
    if son.get("tarih") == t: print(f"TWEET YOK: {t} değeri zaten paylaşıldı ({son.get('deger')}); borsa kapalı/yeni veri yok.")
    else: print("TWEET GEREKLİ")
def kart(out):
    import kart3 as K
    s = oku().tail(70); seri = list(zip(s.t, s.v)); v = s.v.iloc[-1]; h = s.v.iloc[-6]
    d = v - h; ok = ("+" if d >= 0 else "−") + f"{abs(d):.0f}".replace(".", ",")
    K.cizgi_pro("Piyasa nabzı • Duygu", f"Korku-Açgözlülük {v:.0f}: {bolge(v)}".replace(".", ","), "CNN endeksi, 0 aşırı korku, 100 aşırı açgözlülük",
                seri, [], f"Bir haftada {ok} puan", "CNN Business Fear & Greed Index", out, zirve=False,
                ref=[r for r in [(25, "25 aşırı korku"), (75, "75 aşırı açgözlülük")] if s.v.min() - 3 <= r[0] <= s.v.max() + 3], kahraman=(f"{v:.0f}", bolge(v), K.DOWN if v < 45 else K.UP))
    print("kart:", out)
def kaydet_tweet(t, deger, buffer_id):
    json.dump({"tarih": t, "deger": deger, "buffer": buffer_id}, open(SON, "w")); print("son tweet kaydedildi")
if __name__ == "__main__":
    a = sys.argv[1:]
    if not a: print(__doc__)
    elif a[0] == "ekle": ekle(sys.stdin.read())
    elif a[0] == "ozet": ozet()
    elif a[0] == "kart": kart(a[1])
    elif a[0] == "tweetlendi": kaydet_tweet(a[1], float(a[2]), a[3])

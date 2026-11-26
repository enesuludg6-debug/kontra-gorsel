#!/usr/bin/env python3
"""canli.py — gün içi canlı panel (Enes 26.11 08:21: "anlık veri eksiği").
Yahoo 1 dakikalık grafik verisi (seans öncesi/sonrası dahil). Nasdaq hisselerinde Yahoo fiyatı pratikte anlıktır;
NYSE ve endekslerde birkaç dakika gecikme olabilir: çıktıdaki 'son veri' saatine bak.
Kullanım:
  python3 invest/canli.py <T> [T2 ...]          tek bakış: son fiyat, seans öncesi/sonrası, gün içi VWAP, açılış aralığı (ilk 30 dk),
                                                 zamana göre göreli hacim (RVOL), gün içi tepe/dip, önemli seviyelere uzaklık
  python3 invest/canli.py izle <T> <seviye> <yukari|asagi> [--dk 5] [--sure 120]
                                                 seans içinde her N dakikada bir kontrol eden döngü (en çok --sure dk); kırılımda çıktı verir.
                                                 Uzun izleme için send_later ile 10-15 dk'lık kontrol zinciri kur (Enes isterse).
"""
import sys, json, time, urllib.request, datetime as dt
import numpy as np, pandas as pd

def bir_dk(t, rng="5d"):
    u = f"https://query1.finance.yahoo.com/v8/finance/chart/{t}?interval=1m&range={rng}&includePrePost=true"
    r = json.load(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=20))["chart"]["result"][0]
    q = r["indicators"]["quote"][0]
    d = pd.DataFrame({k: q[k] for k in ("open", "high", "low", "close", "volume")},
                     index=pd.to_datetime(r["timestamp"], unit="s", utc=True).tz_convert("America/New_York")).dropna(subset=["close"])
    return d, r["meta"]

def panel(t):
    d, m = bir_dk(t); son = d.index[-1]; f = d.close.iloc[-1]
    seans = d.between_time("09:30", "15:59"); gun = seans.index.date
    son_gun = gun[-1] if len(gun) else son.date(); bug = seans[seans.index.date == son_gun]
    once = d[(d.index.date == son.date()) & (d.index.time < dt.time(9, 30))]; sonra = d[(d.index.date == son.date()) & (d.index.time >= dt.time(16, 0))]
    onceki_kap = m.get("chartPreviousClose") or m.get("previousClose")
    gunluk = pd.Series(seans.close.values, index=seans.index).groupby(seans.index.date).last()
    if len(gunluk) >= 2:
        seans_bitti = son.date() > son_gun or son.time() >= dt.time(16, 0)
        onceki_kap = gunluk.iloc[-1] if seans_bitti else gunluk.iloc[-2]
    print(f"== {t} {f:,.2f}  (son veri {son.tz_convert('Europe/Istanbul'):%d.%m %H:%M} TSİ"
          + (f", önceki kapanışa {(f / onceki_kap - 1) * 100:+.2f}%" if onceki_kap else "") + ")")
    if len(once): print(f"   seans öncesi: son {once.close.iloc[-1]:,.2f}, aralık {once.low.min():,.2f}–{once.high.max():,.2f}, hacim {int(once.volume.sum()):,}")
    if len(sonra): print(f"   seans sonrası: son {sonra.close.iloc[-1]:,.2f}, aralık {sonra.low.min():,.2f}–{sonra.high.max():,.2f}")
    if len(bug):
        v = bug.volume.replace(0, np.nan); tp = (bug.high + bug.low + bug.close) / 3
        vwap = (tp * v).sum() / v.sum() if v.sum() else np.nan
        orh = bug.iloc[:30]; dk = len(bug)
        # zamana göre göreli hacim: son 5 günün aynı dakikasına kadar ortalama
        gecmis = [seans[seans.index.date == g_].volume.iloc[:dk].sum() for g_ in sorted(set(gun))[:-1][-5:]]
        rvol = bug.volume.sum() / np.mean(gecmis) if gecmis and np.mean(gecmis) else np.nan
        print(f"   seans ({son_gun:%d.%m}, {dk} dk): açılış {bug.open.iloc[0]:,.2f}, tepe {bug.high.max():,.2f}, dip {bug.low.min():,.2f}, son {bug.close.iloc[-1]:,.2f}")
        if not np.isnan(vwap): print(f"   VWAP {vwap:,.2f} -> fiyat {'ÜSTÜNDE (alıcı kontrolü)' if bug.close.iloc[-1] > vwap else 'ALTINDA (satıcı kontrolü)'}")
        print(f"   açılış aralığı (ilk 30 dk) {orh.low.min():,.2f}–{orh.high.max():,.2f} -> "
              + ("YUKARI kırıldı" if bug.close.iloc[-1] > orh.high.max() else "AŞAĞI kırıldı" if bug.close.iloc[-1] < orh.low.min() else "içinde"))
        if not np.isnan(rvol): print(f"   göreli hacim (aynı saate kadar, 5 gün ort.) {rvol:.1f}x" + (" — olağan dışı ilgi" if rvol > 1.8 else ""))

def izle(t, sev, yon, dk=5, sure=120):
    bas = time.time()
    while time.time() - bas < sure * 60:
        d, _ = bir_dk(t, "1d"); f = d.close.iloc[-1]
        if (yon == "yukari" and f >= sev) or (yon == "asagi" and f <= sev):
            print(f"TETİKLENDİ: {t} {f:,.2f} {'≥' if yon == 'yukari' else '≤'} {sev:,.2f} ({d.index[-1].tz_convert('Europe/Istanbul'):%H:%M} TSİ)"); return
        time.sleep(dk * 60)
    print(f"süre doldu: {t} {sev} {yon} tetiklenmedi")

if __name__ == "__main__":
    a = sys.argv[1:]
    if not a: print(__doc__)
    elif a[0] == "izle":
        izle(a[1], float(a[2]), a[3], int(a[a.index("--dk") + 1]) if "--dk" in a else 5, int(a[a.index("--sure") + 1]) if "--sure" in a else 120)
    else:
        for t in a: panel(t)

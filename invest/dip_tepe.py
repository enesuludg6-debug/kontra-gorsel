#!/usr/bin/env python3
"""DİP / TEPE / TREND DEĞİŞİMİ RADARI (Enes 25.11.2026 22:22: "dip tahmini, trend değişimi, tepeye yakınken
çok iyi analiz et ve bana çok basit anlat").

Günlük veriden 10 dip işareti ve 10 tepe işareti puanlanır (her biri 0/1), trend değişimi 3 aşamada okunur
(erken / gelişiyor / onaylı) ve aynı puanın son 20 yılda verdiği sonuçlar gösterilir (kalibrasyon).
Kullanım: python3 invest/dip_tepe.py ^NDX   |   python3 invest/dip_tepe.py NVDA
Çıktının sonunda "BASİT ANLATIM" bloğu var: Enes'e bunu aynen (gerekirse kısaltarak) yaz.
"""
import sys, json, urllib.request, warnings
import numpy as np, pandas as pd
warnings.filterwarnings("ignore")

def yahoo(t, aralik="1d", rng="20y"):
    try:
        from veri_kalite import temiz
        return temiz(t, aralik, rng)[0]
    except Exception:
        pass
    u = f"https://query1.finance.yahoo.com/v8/finance/chart/{t}?interval={aralik}&range={rng}"
    d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=25))["chart"]["result"][0]
    q = d["indicators"]["quote"][0]
    return pd.DataFrame({"open": q["open"], "high": q["high"], "low": q["low"], "close": q["close"], "volume": q["volume"]},
                        index=pd.to_datetime(d["timestamp"], unit="s").normalize()).dropna(subset=["close"])

def isaretler(d, vix):
    import pandas_ta as ta
    c, h, l, o = d.close, d.high, d.low, d.open
    rsi = ta.rsi(c, 14); e50 = ta.ema(c, 50); e20 = ta.ema(c, 20)
    e200 = ta.ema(c, 200) if len(c) > 210 else ta.ema(c, max(20, len(c) // 2))  # kısa geçmiş (yeni halka arz): uzun ortalama yerine yarı ömür
    atr = ta.atr(h, l, c, 14); bb = ta.bbands(c, 20, 2); bl, bu = bb.iloc[:, 0], bb.iloc[:, 2]
    uzak = (c - e200) / atr                       # 200 EMA'dan kaç ATR uzak
    dd = c / c.cummax() - 1
    vol = d.volume.replace(0, np.nan); vort = vol.rolling(50).mean()
    govde = (c - o).abs(); alt_fitil = np.minimum(o, c) - l; ust_fitil = h - np.maximum(o, c)
    ardisik_dusus = (c < c.shift()).astype(int).groupby((c >= c.shift()).cumsum()).cumsum()
    ardisik_yuks = (c > c.shift()).astype(int).groupby((c <= c.shift()).cumsum()).cumsum()
    v = vix.reindex(d.index).ffill()
    rsi_min10 = rsi.rolling(10).min(); fiyat_min10 = l.rolling(10).min()
    DIP = pd.DataFrame({
        "RSI 30 altında ya da yakın (≤32)": rsi <= 32,
        "Fiyat 200 günlük ortalamanın 4 ATR'den fazla altında": uzak <= -4,
        "Zirveden en az %15 düşüş": dd <= -0.15,
        "Bollinger alt bandının altına sarkma (son 3 gün)": (l < bl).rolling(3).max() == 1,
        "Korku endeksi (VIX) 30 üstü": v >= 30,
        "Teslimiyet mumu: uzun alt fitil + yüksek hacim": (alt_fitil > 1.5 * govde) & (vol > 1.5 * vort),
        "5+ gün üst üste düşüş": ardisik_dusus.shift().fillna(0) >= 5,
        "RSI boğa uyumsuzluğu (fiyat yeni dip, RSI değil)": (l <= fiyat_min10) & (rsi > rsi_min10.shift() + 3),
        "Gün içi dipten güçlü dönüş (kapanış gün aralığının üst %70'inde)": ((c - l) / (h - l + 1e-9) >= 0.7) & (dd <= -0.10),
        "Önceki günün tepesinin üstünde kapanış (ilk dönüş sinyali)": (c > h.shift()) & (rsi.shift() < 40),
    }).fillna(False)
    rsi_max10 = rsi.rolling(10).max(); fiyat_max10 = h.rolling(10).max()
    TEPE = pd.DataFrame({
        "RSI 70 üstünde ya da yakın (≥68)": rsi >= 68,
        "Fiyat 200 günlük ortalamanın 4 ATR'den fazla üstünde": uzak >= 4,
        "Zirveye %3'ten yakın": dd >= -0.03,
        "Bollinger üst bandının üstüne taşma (son 3 gün)": (h > bu).rolling(3).max() == 1,
        "Korku endeksi (VIX) 14 altında, rehavet": v <= 14,
        "Uzun üst fitil + yüksek hacim (satıcı geldi)": (ust_fitil > 1.5 * govde) & (vol > 1.5 * vort),
        "5+ gün üst üste yükseliş": ardisik_yuks.shift().fillna(0) >= 5,
        "RSI ayı uyumsuzluğu (fiyat yeni tepe, RSI değil)": (h >= fiyat_max10) & (rsi < rsi_max10.shift() - 3),
        "50 günlük ortalamadan %10'dan fazla yukarıda": (c / e50 - 1) >= 0.10,
        "Önceki günün dibinin altında kapanış (ilk dönüş sinyali)": (c < l.shift()) & (rsi.shift() > 60),
    }).fillna(False)
    trend = pd.DataFrame({"e20": e20, "e50": e50, "e200": e200, "c": c, "rsi": rsi})
    return DIP, TEPE, trend, atr

def trend_okuma(d, tr):
    c = d.close; son = tr.iloc[-1]
    # yapı: son 2 swing dip ve tepe (5 günlük pencere)
    sh = d.high[(d.high == d.high.rolling(5, center=True).max())].tail(3)
    sl = d.low[(d.low == d.low.rolling(5, center=True).min())].tail(3)
    yukselen_dip = len(sl) >= 2 and sl.iloc[-1] > sl.iloc[-2]
    son_tepe = sh.iloc[-1] if len(sh) else np.nan
    tepe_kirildi = c.iloc[-1] > son_tepe if pd.notna(son_tepe) else False
    alcalan_tepe = len(sh) >= 2 and sh.iloc[-1] < sh.iloc[-2]
    son_dip = sl.iloc[-1] if len(sl) else np.nan
    dip_kirildi = c.iloc[-1] < son_dip if pd.notna(son_dip) else False
    asagi_trend = son.c < son.e200 and son.e20 < son.e50
    if asagi_trend:
        adim = sum([c.iloc[-1] > son.e20, yukselen_dip, tepe_kirildi, son.e20 > son.e50])
        asama = ["YOK — düşüş trendi sürüyor", "ERKEN — ilk işaret var, onay yok", "GELİŞİYOR — dönüşün yarısı tamam", "GÜÇLÜ — dönüş büyük ölçüde onaylı", "ONAYLI — yükselişe dönüş tamam"][adim]
        kosullar = [("Fiyat 20 günlük ortalamanın üstünde kapanış", c.iloc[-1] > son.e20, son.e20),
                    ("Bir önceki dipten daha yüksek dip", yukselen_dip, sl.iloc[-1] if len(sl) else np.nan),
                    ("Son tepenin üstünde kapanış (yapı kırılımı)", tepe_kirildi, son_tepe),
                    ("20 günlük ortalama 50 günlüğü yukarı kesti", son.e20 > son.e50, son.e50)]
        return "DÜŞÜŞTEN YÜKSELİŞE DÖNÜŞ", asama, kosullar
    adim = sum([c.iloc[-1] < son.e20, alcalan_tepe, dip_kirildi, son.e20 < son.e50])
    asama = ["YOK — yükseliş trendi sürüyor", "ERKEN — ilk işaret var, onay yok", "GELİŞİYOR — dönüşün yarısı tamam", "GÜÇLÜ — dönüş büyük ölçüde onaylı", "ONAYLI — düşüşe dönüş tamam"][adim]
    kosullar = [("Fiyat 20 günlük ortalamanın altında kapanış", c.iloc[-1] < son.e20, son.e20),
                ("Bir önceki tepeden daha düşük tepe", alcalan_tepe, sh.iloc[-1] if len(sh) else np.nan),
                ("Son dibin altında kapanış (yapı kırılımı)", dip_kirildi, son_dip),
                ("20 günlük ortalama 50 günlüğü aşağı kesti", son.e20 < son.e50, son.e50)]
    return "YÜKSELİŞTEN DÜŞÜŞE DÖNÜŞ", asama, kosullar

def kalibrasyon(d, skor, esik, yon):
    """Aynı skora (>= esik) ilk ulaşılan günlerden sonra 10/20/60 gün getiri (olaylar arası 40 gün)."""
    c = d.close.values; idx = np.where(skor.values >= esik)[0]; sec = []
    for i in idx:
        if not sec or i - sec[-1] >= 40: sec.append(i)
    sonuc = {}
    for n in (10, 20, 60):
        g = [c[i + n] / c[i] - 1 for i in sec if i + n < len(c)]
        if g: sonuc[n] = (np.mean(g) * 100, np.mean([x > 0 for x in g]) * 100 if yon == "dip" else np.mean([x < 0 for x in g]) * 100, len(g))
    return sonuc, [d.index[i].date() for i in sec[-4:]]


def onayli_giris(d, ds, tr, esik=7):
    """Dip skoru >= esik olduktan sonra ilk '20 günlük ortalama üstünde kapanış' günü giriş sayılırsa sonuçlar."""
    c = d.close.values; e20 = tr.e20.values; sec = []
    for i in np.where(ds.values >= esik)[0]:
        if not sec or i - sec[-1] >= 40: sec.append(i)
    R = []
    for i in sec:
        j = next((k for k in range(i, min(i + 30, len(c))) if c[k] > e20[k]), None)
        if j is not None and j + 60 < len(c): R.append((c[j + 20] / c[j] - 1, c[j + 60] / c[j] - 1))
    if not R: return None
    a = np.array(R); return len(R), a[:, 0].mean() * 100, (a[:, 0] > 0).mean() * 100, a[:, 1].mean() * 100, (a[:, 1] > 0).mean() * 100

def main(t):
    d = yahoo(t); vix = yahoo("^VXN" if t in ("^NDX", "QQQ", "NQ=F") else "^VIX").close
    DIP, TEPE, tr, atr = isaretler(d, vix)
    ds = DIP.astype(int).rolling(5).max().sum(axis=1)   # her işaret son 5 günde en az bir kez yandıysa sayılır
    ts = TEPE.astype(int).rolling(5).max().sum(axis=1)
    son = d.close.iloc[-1]; dd = (son / d.close.cummax().iloc[-1] - 1) * 100
    print(f"== {t}  son {son:,.2f}  zirveden {dd:+.1f}%  ({d.index[-1].date()})")
    # son 5 günün en yüksek skoru (sinyaller birkaç güne yayılır)
    d5, t5 = int(ds.iloc[-1]), int(ts.iloc[-1])
    print(f"DİP SKORU {d5}/10 (işaret son 5 günde en az bir kez yandıysa sayılır)")
    for k, v in DIP.iloc[-5:].any().items(): print(f"  {'✔' if v else '·'} {k}")
    print(f"TEPE SKORU {t5}/10")
    for k, v in TEPE.iloc[-5:].any().items():
        if v: print(f"  ✔ {k}")
    yon, asama, kos = trend_okuma(d, tr)
    print(f"TREND DEĞİŞİMİ ({yon}): {asama}")
    for ad, ok, sv in kos: print(f"  {'✔' if ok else '✗'} {ad}" + (f" — seviye {sv:,.0f}" if pd.notna(sv) else ""))
    # kalibrasyon
    for ad, sk, yon_, e in (("DİP", ds, "dip", max(d5, 5)), ("TEPE", ts, "tepe", max(t5, 5))):
        if (ad == "DİP" and d5 >= 4) or (ad == "TEPE" and t5 >= 4):
            k, son_olay = kalibrasyon(d, sk, e, yon_)
            if k:
                print(f"GEÇMİŞ ({ad} skoru ≥{e}, 20 yıl, ilk ulaşma, olaylar arası 40 gün):")
                for n, (ort, oran, adet) in k.items():
                    print(f"  {n} gün sonra: ortalama {ort:+.1f}% | {'yukarıda' if yon_=='dip' else 'aşağıda'} olma oranı %{oran:.0f} ({adet} olay)")
                print("  son olaylar: " + ", ".join(map(str, son_olay)))
    oo = onayli_giris(d, ds, tr, max(d5, 6)) if d5 >= 6 else None
    if oo:
        print(f"ONAYLI GİRİŞ TESTİ (dip skoru ≥{max(d5,6)} + sonra ilk 20 günlük ortalama üstü kapanışta giriş): {oo[0]} olay | 20 gün sonra ort {oo[1]:+.1f}%, pozitif %{oo[2]:.0f} | 60 gün sonra ort {oo[3]:+.1f}%, pozitif %{oo[4]:.0f}")
    # basit anlatım
    print("\nBASİT ANLATIM:")
    if d5 >= 7: dip_cumle = f"Dip işaretleri çok güçlü ({d5}/10): satış yorgunluğu belirgin, dip bölgesine yakınız."
    elif d5 >= 5: dip_cumle = f"Dip işaretleri orta-güçlü ({d5}/10): dip oluşuyor olabilir ama henüz onay yok."
    elif d5 >= 3: dip_cumle = f"Dip işaretleri zayıf ({d5}/10): düşüş yorgun ama dip için erken."
    else: dip_cumle = f"Dip işareti yok denecek kadar az ({d5}/10)."
    tepe_cumle = f"Tepe işaretleri {'güçlü' if t5 >= 6 else 'orta' if t5 >= 4 else 'zayıf'} ({t5}/10)."
    onay = [ad for ad, ok, sv in kos if not ok]
    sonraki = kos[[ok for _, ok, _ in kos].index(False)] if onay else None
    print(f"- {dip_cumle}")
    print(f"- {tepe_cumle}")
    print(f"- Trend: {asama.split(' — ')[0].lower()} aşamada. " + (f"Dönüşü onaylamak için sıradaki şart: {sonraki[0].lower()}" + (f" ({sonraki[2]:,.0f})." if pd.notna(sonraki[2]) else ".") if sonraki else "Dönüş şartlarının hepsi tamam."))
    if oo: print(f"- Geçmiş ne diyor: bu kadar dip işareti tek başına güvenilir değil; ama ardından fiyat 20 günlük ortalamanın üstüne çıktığında girilseydi 20 gün sonra kazanma oranı %{oo[2]:.0f} olurdu ({oo[0]} olay).")
    print("- Kural: dip skoru yüksek + trend 'erken' = dipte olabiliriz ama acele etme; trend 'gelişiyor/onaylı' olmadan büyük pozisyon yok.")

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "^NDX")

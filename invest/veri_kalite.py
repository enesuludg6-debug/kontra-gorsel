#!/usr/bin/env python3
"""veri_kalite.py — Enes 26.11 00:04 "kaliteli veri, daha iyi analiz".
Kullanım:
  python3 invest/veri_kalite.py <T>            veri sağlık raporu (temizlenmiş seri + uyarılar)
  python3 invest/veri_kalite.py <T> --dogrula  yöntem doğrulaması: benzer-gün ve dip sinyallerinin
                                               GEÇMİŞTE, o günün verisiyle yapılsaydı ne kadar tuttuğu (ileriye dönük test)
Kütüphane:
  temiz(t, aralik, rng) -> (df, uyarilar)   temettü/bölünme düzeltmeli OHLC, bozuk mum ayıklama, canlı mum işareti
  kanit(sonuclar, taban) -> dict            Wilson %95 güven aralığı + taban orana göre fark + hüküm
Shell'den yalnız query1.finance.yahoo.com erişilebiliyor; ikinci kaynak çapraz kontrolü için son kapanışı
WebFetch ile (ör. stockanalysis.com, investing.com) doğrula ve farkı %0,5'ten büyükse söyle.
"""
import sys, json, math, urllib.request, warnings, datetime as dt
import numpy as np, pandas as pd
warnings.filterwarnings("ignore")

TATIL = {"2025-01-01","2025-01-09","2025-01-20","2025-02-17","2025-04-18","2025-05-26","2025-06-19","2025-07-04","2025-09-01",
         "2025-11-27","2025-12-25","2026-01-01","2026-01-19","2026-02-16","2026-04-03","2026-05-25","2026-06-19","2026-07-03",
         "2026-09-07","2026-11-26","2026-12-25","2027-01-01"}

def _ham(t, aralik, rng):
    u = f"https://query1.finance.yahoo.com/v8/finance/chart/{t}?interval={aralik}&range={rng}&events=div,splits"
    return json.load(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=25))["chart"]["result"][0]

def beklenen_son_gun(simdi=None):
    """ABD saatine göre en son TAMAMLANMIŞ işlem günü."""
    simdi = simdi or dt.datetime.utcnow() - dt.timedelta(hours=5)   # ET (kışın UTC-5)
    g = simdi.date() if simdi.hour >= 16 else simdi.date() - dt.timedelta(days=1)
    while g.weekday() >= 5 or g.isoformat() in TATIL: g -= dt.timedelta(days=1)
    return g

def temiz(t, aralik="1d", rng="20y"):
    r = _ham(t, aralik, rng); q = r["indicators"]["quote"][0]; uy = []
    idx = pd.to_datetime(r["timestamp"], unit="s")
    d = pd.DataFrame({k: q[k] for k in ("open", "high", "low", "close", "volume")}, index=idx.normalize() if aralik == "1d" else idx)
    adj = r["indicators"].get("adjclose", [{}])[0].get("adjclose")
    n0 = len(d); d = d[~d.index.duplicated(keep="last")].dropna(subset=["close"])
    if n0 - len(d): uy.append(f"{n0 - len(d)} boş/çift mum atıldı")
    if adj is not None and aralik == "1d":
        a = pd.Series(adj, index=idx.normalize()); a = a[~a.index.duplicated(keep="last")].reindex(d.index)
        oran = (a / d.close).fillna(1.0)
        if (oran.iloc[0] < 0.97): uy.append(f"temettü düzeltmesi uygulandı (20 yıl önceki fiyatlar ×{oran.iloc[0]:.2f})")
        for k in ("open", "high", "low", "close"): d[k] = d[k] * oran
    for k in ("open", "high", "low"): d[k] = d[k].fillna(d.close)
    bozuk = (d.high < d[["open", "close"]].max(axis=1) - 1e-9) | (d.low > d[["open", "close"]].min(axis=1) + 1e-9)
    if bozuk.sum():
        d.loc[bozuk, "high"] = d.loc[bozuk, ["open", "close", "high"]].max(axis=1); d.loc[bozuk, "low"] = d.loc[bozuk, ["open", "close", "low"]].min(axis=1)
        uy.append(f"{int(bozuk.sum())} mumda tepe/dip tutarsızlığı düzeltildi")
    g = np.log(d.close).diff(); s = g.rolling(60, min_periods=20).std()
    sivri = (g.abs() > 8 * s) & (g.shift(-1) * g < 0) & (g.shift(-1).abs() > 6 * s)
    if sivri.sum():
        for i in d.index[sivri]: uy.append(f"şüpheli tek günlük sıçrama {i:%d.%m.%Y} (ertesi gün geri döndü) — bozuk veri olabilir, ayıklandı")
        d = d[~sivri]
    if "volume" in d and not t.startswith("^"):
        sifir = (d.volume.fillna(0) == 0).iloc[-250:].sum()
        if sifir: uy.append(f"son 1 yılda {sifir} gün sıfır hacim — hacim analizleri zayıf")
    if aralik == "1d":
        son = d.index[-1].date(); bek = beklenen_son_gun(); meta = r.get("meta", {})
        canli = meta.get("regularMarketTime") and (dt.datetime.utcfromtimestamp(meta["regularMarketTime"]) - dt.timedelta(hours=5)).date() > bek
        if son > bek or canli: uy.append(f"son mum {son:%d.%m} henüz kapanmadı (canlı): göstergeler gün sonunda değişebilir")
        elif son < bek: uy.append(f"VERİ ESKİ: son mum {son:%d.%m}, beklenen {bek:%d.%m}")
        eksik = [x for x in pd.bdate_range(d.index[-min(250, len(d))], d.index[-1]) if x not in d.index and x.strftime("%Y-%m-%d") not in TATIL]
        if len(eksik) > 2: uy.append(f"son 1 yılda {len(eksik)} işlem günü eksik (ör. {eksik[0]:%d.%m.%Y})")
        if len(d) < 300: uy.append(f"kısa geçmiş ({len(d)} gün): 200 günlük ortalama ve 20 yıllık istatistikler güvenilmez")
    return d, uy

def wilson(k, n, z=1.96):
    if n == 0: return 0, 0, 100
    p = k / n; m = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n); c = (p + z * z / (2 * n)) / (1 + z * z / n)
    return p * 100, max(0, c - m) * 100, min(1, c + m) * 100

def kanit(sonuclar, taban):
    """sonuclar: getiriler listesi; taban: aynı ufukta koşulsuz kazanma oranı (%)."""
    n = len(sonuclar); k = sum(1 for x in sonuclar if x > 0); p, alt, ust = wilson(k, n)
    if n < 10: h = "KANIT YOK (olay <10)"
    elif alt > taban: h = "GÜÇLÜ KANIT (alt sınır bile taban oranın üstünde)"
    elif p - taban >= 8: h = "ZAYIF KANIT (fark var ama aralık geniş)"
    elif p - taban <= -8: h = "TERS İŞARET (taban oranın altında)"
    else: h = "FARK YOK (sıradan bir günden farksız)"
    return {"n": n, "oran": p, "alt": alt, "ust": ust, "taban": taban, "fark": p - taban, "hukum": h}

def taban_oran(c, ufuk=20):
    f = (c.shift(-ufuk) / c - 1).dropna(); return (f > 0).mean() * 100

def dogrula(t):
    """İleriye dönük test: her 15 işlem gününde bir, O GÜNE KADARKİ veriyle benzer-gün tahmini yap, 20 gün sonrasıyla karşılaştır."""
    from teknik_plus import ozellik
    d, _ = temiz(t); f = ozellik(d); c = d.close.reindex(f.index); ileri = (c.shift(-20) / c - 1)
    noktalar = range(800, len(f) - 20, 15); kayit = []
    for i in noktalar:
        gecmis = f.iloc[:i - 60]; mu, sd = gecmis.mean(), gecmis.std()
        z = (gecmis - mu) / sd; bug = (f.iloc[i] - mu) / sd
        mes = ((z - bug) ** 2).sum(axis=1).sort_values(); sec = []
        for tt in mes.index:
            if all(abs((tt - s).days) > 30 for s in sec): sec.append(tt)
            if len(sec) == 12: break
        sonra = [ileri.loc[s] for s in sec if not np.isnan(ileri.loc[s])]
        if len(sonra) < 8: continue
        tahmin = np.mean([x > 0 for x in sonra]) * 100
        kayit.append((f.index[i], tahmin, ileri.iloc[i]))
    k = pd.DataFrame(kayit, columns=["tarih", "tahmin", "gercek"]).dropna(); tb = taban_oran(c)
    print(f"YÖNTEM DOĞRULAMASI — {t}: benzer günler ({len(k)} ayrı tarihte, yalnız o güne kadarki veriyle)")
    print(f"  taban oran (herhangi bir günden 20 gün sonra yukarıda): %{tb:.0f}")
    for ad, m in (("benzerlerin ≥%75'i yukarı dediğinde", k.tahmin >= 75), ("benzerlerin ≤%42'si yukarı dediğinde", k.tahmin <= 42)):
        s = k.gercek[m].tolist(); r = kanit(s, tb if "≥" in ad else tb)
        print(f"  {ad}: {r['n']} kez, gerçekten yukarı %{r['oran']:.0f} (%95 aralık {r['alt']:.0f}-{r['ust']:.0f}), medyan {np.median(s) * 100 if s else 0:+.1f}% -> {r['hukum']}")
    try:
        from dip_tepe import isaretler, yahoo
        vix = yahoo("^VXN" if t in ("^NDX", "QQQ") else "^VIX").close
        DIP, _, _, _ = isaretler(d, vix); cv = d.close.values
        print("  DİP SİNYALLERİ taban orana göre (20 gün, olaylar arası ≥10 gün):")
        sat = []
        for col in DIP.columns:
            idx = np.where(DIP[col].values)[0]; sec = []
            for i in idx:
                if not sec or i - sec[-1] >= 10: sec.append(i)
            g = [cv[i + 20] / cv[i] - 1 for i in sec if i + 20 < len(cv)]
            if len(g) >= 5: sat.append((col, kanit(g, tb)))
        for col, r in sorted(sat, key=lambda x: -x[1]["alt"]):
            print(f"    %{r['oran']:3.0f} ({r['alt']:.0f}-{r['ust']:.0f}, {r['n']} olay, fark {r['fark']:+.0f}) {col} -> {r['hukum'].split(' (')[0]}")
    except Exception as e:
        print("  dip sinyal testi atlandı:", e)

if __name__ == "__main__":
    t = sys.argv[1] if len(sys.argv) > 1 else "^NDX"
    if "--dogrula" in sys.argv: dogrula(t); sys.exit()
    d, uy = temiz(t)
    print(f"VERİ SAĞLIĞI — {t}: {len(d)} gün ({d.index[0]:%d.%m.%Y} – {d.index[-1]:%d.%m.%Y}), son kapanış {d.close.iloc[-1]:,.2f}")
    print("  " + ("\n  ".join(uy) if uy else "temiz: eksik/bozuk/eski veri yok"))
    print(f"  ikinci kaynak: son kapanışı WebFetch ile doğrula (shell yalnız Yahoo'ya erişiyor)")

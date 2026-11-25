#!/usr/bin/env python3
"""TEKNİK ÜST KATMAN (Enes 25.11.2026 23:58 "teknik analizi daha da geliştir").

1) PİYASA GENİŞLİĞİ (Nasdaq 100 bileşenleri): 20/50/200 günlük ortalama üstündeki hisse oranı, 52 hafta dibine
   %3 yakın hisse oranı, yükselen/düşen oranı. Dip/tepe kararının en güvenilir filtresi.
2) HİSSEYE ÖZEL SİNYAL KARNESİ: dip_tepe.py'deki 10 dip işaretinin HER BİRİNİN bu hissede geçmişte (eldeki tüm veri)
   20 gün sonra kazandırma oranı — hangi sinyal BU hissede işe yarıyor.
3) HACİM ANALİZİ: OBV ve birikim/dağıtım (A/D) çizgisi fiyatla uyumsuz mu, göreli hacim (bugün / 50 gün ort.).
4) GÜVEN SKORU (0-100): MTF, dip skoru (hisseye özel ağırlıklı), trend aşaması, genişlik, hacim uyumsuzluğu,
   seviye çakışması -> tek sayı + basit Türkçe hüküm.
Opsiyon verisi (put/call, gamma) Yahoo'da kimlik doğrulama istediği için yok (401).

Kullanım: python3 invest/teknik_ust.py <TICKER>     |    python3 invest/teknik_ust.py genislik
"""
import sys, json, urllib.request, warnings, concurrent.futures as cf
import numpy as np, pandas as pd
warnings.filterwarnings("ignore")
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from dip_tepe import yahoo, isaretler, trend_okuma

NDX100 = ("AAPL MSFT NVDA AMZN GOOGL GOOG META AVGO TSLA COST NFLX PLTR AMD ASML CSCO TMUS AZN LIN INTU PEP ISRG "
          "BKNG TXN QCOM AMGN ADBE AMAT SHOP GILD PDD HON ARM PANW CMCSA MU LRCX ADP KLAC APP ADI MELI CRWD VRTX "
          "SBUX INTC CEG MSTR CDNS DASH SNPS ORLY MAR CTAS MDLZ ABNB REGN FTNT PYPL MRVL WDAY ADSK CSX AXON ROP "
          "NXPI CHTR AEP PAYX MNST FAST CPRT TTWO ROST DDOG PCAR KDP BKR ZS EXC TEAM IDXX XEL CCEP FANG EA VRSK "
          "KHC TTD GEHC LULU CTSH ODFL CSGP DXCM ANSS ON BIIB CDW WBD GFS MDB").split()

def _seri(t):
    try:
        u = f"https://query1.finance.yahoo.com/v8/finance/chart/{t}?interval=1d&range=1y"
        d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=20))["chart"]["result"][0]
        q = d["indicators"]["quote"][0]
        return t, pd.DataFrame({"c": q["close"], "l": q["low"]}, index=pd.to_datetime(d["timestamp"], unit="s").normalize()).dropna()
    except Exception:
        return t, None

def genislik():
    with cf.ThreadPoolExecutor(16) as ex: S = dict(ex.map(_seri, NDX100))
    a20 = a50 = a200 = dip = yuk = n = 0
    for t, d in S.items():
        if d is None or len(d) < 60: continue
        c = d.c; n += 1
        a20 += c.iloc[-1] > c.ewm(span=20).mean().iloc[-1]; a50 += c.iloc[-1] > c.ewm(span=50).mean().iloc[-1]
        a200 += c.iloc[-1] > (c.ewm(span=200).mean().iloc[-1] if len(c) > 200 else c.mean())
        dip += c.iloc[-1] <= d.l.tail(252).min() * 1.03; yuk += c.iloc[-1] > c.iloc[-2]
    p = lambda x: x / max(n, 1) * 100
    r = {"n": n, "20": p(a20), "50": p(a50), "200": p(a200), "dip": p(dip), "yuk": p(yuk)}
    yorum = ("AŞIRI SATIM — tarihsel dip bölgeleri genelde 50 günlük üstü oranı %15'in altındayken oluşur" if r["50"] < 15 else
             "ZAYIF — çoğunluk 50 günlüğün altında, dip için genişlik henüz yıkanmadı" if r["50"] < 35 else
             "NÖTR" if r["50"] < 65 else "GÜÇLÜ" if r["50"] < 85 else "AŞIRI ALIM — tepe bölgelerinde genişlik %85 üstüne çıkar")
    return r, yorum

def sinyal_karnesi(d, DIP):
    c = d.close.values; out = []
    for k in DIP.columns:
        idx = np.where(DIP[k].values)[0]; sec = []
        for i in idx:
            if not sec or i - sec[-1] >= 10: sec.append(i)
        g = [c[i + 20] / c[i] - 1 for i in sec if i + 20 < len(c)]
        if len(g) >= 5: out.append((k, len(g), np.mean([x > 0 for x in g]) * 100, np.mean(g) * 100))
    return sorted(out, key=lambda x: -x[2])

def hacim(d):
    import pandas_ta as ta
    obv = ta.obv(d.close, d.volume); ad = ta.ad(d.high, d.low, d.close, d.volume)
    son = d.tail(20); o = obv.tail(20); a = ad.tail(20)
    fiyat_dip = son.low.iloc[-1] <= son.low.min() * 1.01
    obv_yuks = o.iloc[-1] > o.iloc[:10].min(); ad_yuks = a.iloc[-1] > a.iloc[:10].mean()
    rv = d.volume.iloc[-1] / d.volume.tail(50).mean()
    notlar = []
    if fiyat_dip and obv_yuks: notlar.append("OBV boğa uyumsuzluğu: fiyat dipte ama hacim tabanlı para akışı (OBV) dipte değil — sessiz birikim izi")
    if ad_yuks and son.close.iloc[-1] < son.close.mean(): notlar.append("Birikim/dağıtım çizgisi yükseliyor, fiyat düşüyor — kapanışlar gün içi aralığın üst kısmında")
    if not notlar: notlar.append("Hacimde belirgin uyumsuzluk yok (para akışı fiyatla aynı yönde)")
    return notlar, rv, (1 if (fiyat_dip and obv_yuks) or (ad_yuks and son.close.iloc[-1] < son.close.mean()) else 0)

def main(t):
    if t == "genislik":
        r, y = genislik(); print(f"NASDAQ 100 GENİŞLİĞİ ({r['n']} hisse): 20G üstü %{r['20']:.0f} | 50G üstü %{r['50']:.0f} | 200G üstü %{r['200']:.0f} | 52 hafta dibine %3 yakın %{r['dip']:.0f} | bugün yükselen %{r['yuk']:.0f}\n -> {y}"); return
    d = yahoo(t); vix = yahoo("^VXN" if t in ("^NDX", "QQQ", "NQ=F") else "^VIX").close
    DIP, TEPE, tr, atr = isaretler(d, vix)
    ds = DIP.astype(int).rolling(5).max().sum(axis=1); d5 = int(ds.iloc[-1])
    yon, asama, kos = trend_okuma(d, tr); adim = sum(1 for _, ok, _ in kos if ok)
    print(f"== {t} {d.close.iloc[-1]:,.2f}")
    kar = sinyal_karnesi(d, DIP); yanan = set(k for k, v in DIP.iloc[-5:].any().items() if v)
    print("HİSSEYE ÖZEL SİNYAL KARNESİ (20 gün sonra kazanma oranı, bu hissenin tüm geçmişi):")
    agirlik = []
    for k, n_, oran, ort in kar:
        isaret = "✔ şimdi yanıyor" if k in yanan else ""
        print(f"  %{oran:3.0f}  ort {ort:+5.1f}%  ({n_:3d} olay)  {k}  {isaret}")
        if k in yanan: agirlik.append(oran)
    guvenilir = np.mean(agirlik) if agirlik else 50
    notlar, rv, hacim_puan = hacim(d)
    print(f"HACİM: göreli hacim {rv:.1f}x (bugün / 50 gün ort.)"); [print("  " + x) for x in notlar]
    r, y = genislik(); print(f"GENİŞLİK (Nasdaq 100): 50G üstü %{r['50']:.0f}, 200G üstü %{r['200']:.0f}, dibe yakın %{r['dip']:.0f} -> {y}")
    from teknik_pro import yon_ozet
    from smc_analiz import veri
    mtf = 0
    for k_, sw in {"1d": 10, "4h": 6}.items():
        try: mtf += yon_ozet(veri(t, k_), sw)["puan"]
        except Exception: pass
    # güven skoru (yukarı dönüş için)
    skor = 0
    skor += min(25, d5 * 2.5)                                  # dip işaretleri (0-25)
    skor += (guvenilir - 50) * 0.4                             # bu hissede yanan sinyallerin geçmiş başarısı (−20..+20)
    skor += adim * 7.5                                         # trend onay adımları (0-30)
    skor += 10 if r["50"] < 15 else 5 if r["50"] < 35 else 0    # genişlik yıkanmış mı
    skor += 8 * hacim_puan                                     # hacim birikimi
    skor += max(-10, min(10, mtf))                             # kısa vade yapı (−10..+10)
    skor = int(max(0, min(100, skor + 10)))
    hk = ("YÜKSEK — dip ve dönüş birlikte destekleniyor" if skor >= 70 else "ORTA — dip olası, onay eksik" if skor >= 45 else "DÜŞÜK — dönüş için erken")
    print(f"\nYUKARI DÖNÜŞ GÜVEN SKORU: {skor}/100 -> {hk}")
    print(f"  bileşenler: dip {d5}/10 | yanan sinyallerin bu hissedeki geçmiş başarısı %{guvenilir:.0f} | trend {adim}/4 ({asama.split(' — ')[0]}) | genişlik 50G %{r['50']:.0f} | hacim birikimi {'var' if hacim_puan else 'yok'} | 1d+4h yapı {mtf:+d}")
    print("BASİT HÜKÜM: " + (f"Dip ihtimali güçleniyor ama trend {adim}/4 onaylı; " if d5 >= 5 else "Dip işaretleri zayıf; ") +
          ("piyasa genişliği yıkanmış, bu dip için olumlu; " if r["50"] < 15 else "piyasa genişliği henüz tam yıkanmadı; " if r["50"] < 35 else "") +
          ("hacimde sessiz birikim izi var." if hacim_puan else "hacimde birikim izi yok."))

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "genislik")

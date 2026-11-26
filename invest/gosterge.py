#!/usr/bin/env python3
"""gosterge.py — ortak gösterge motoru (tarama.py, backtest.py, teknik.py kullanır).
veri(t, rng)      : temiz günlük veri (veri_kalite.temiz), /tmp/tcache'de 6 saat önbellek
hesapla(d, ref)   : 60+ sütun; DSL'de bu adlar kullanılır (ADLAR sözlüğü açıklamalarıyla)
dsl(ifade)        : Türkçe ifadeyi pandas ifadesine çevirir ("rsi<30 ve kapanis>ema200")
"""
import os, time, pickle, warnings, re
import numpy as np, pandas as pd
warnings.filterwarnings("ignore")
import contextlib, io
with contextlib.redirect_stdout(io.StringIO()):
    import pandas_ta as ta
from veri_kalite import temiz

CACHE = "/tmp/tcache"; os.makedirs(CACHE, exist_ok=True)

def veri(t, rng="10y", ttl=6 * 3600):
    f = os.path.join(CACHE, f"{t.replace('^', '_').replace('=', '_')}_{rng}.pkl")
    if os.path.exists(f) and time.time() - os.path.getmtime(f) < ttl:
        return pickle.load(open(f, "rb"))
    d = temiz(t, "1d", rng)[0]; pickle.dump(d, open(f, "wb")); return d

ADLAR = {
    "kapanis/acilis/yuksek/dusuk/hacim": "fiyat ve hacim",
    "ema20 ema50 ema200 sma50 sma200": "hareketli ortalamalar",
    "rsi rsi2": "RSI 14 ve 2", "atr atr_yuzde": "ATR 14 ve fiyata oranı %",
    "uz20 uz50 uz200": "kapanışın ilgili EMA'dan ATR cinsinden uzaklığı",
    "macd macd_sinyal macd_hist": "MACD 12/26/9", "adx dip_plus dip_minus": "ADX 14 ve DI+/DI-",
    "bb_ust bb_alt bb_genislik bb_yuzde sikisma": "Bollinger 20/2; sikisma = genişlik 1 yılın en dar %10'u",
    "supertrend_yon": "1 yukarı, -1 aşağı", "stoch_k stoch_d": "stokastik 14/3",
    "mfi obv_egim cmf": "para akışı: MFI 14, OBV 20 gün eğimi, Chaikin 20",
    "hacim_oran": "hacim / 20 gün ortalaması",
    "zirve52 dip52": "52 hafta zirve/dibe uzaklık %", "yuksek20 dusuk20 yuksek55": "önceki N günün tepesi/dibi (kırılım için)",
    "getiri1 getiri5 getiri20 getiri60 getiri120": "N günlük getiri %",
    "rs20 rs60 rs_tepe": "referansa (QQQ) göre N gün fark puanı; rs_tepe = göreli güç çizgisi 3 ay tepesinde (1/0)",
    "ema20_50_yukari ema20_50_asagi ema50_200_yukari ema50_200_asagi macd_yukari macd_asagi st_yukari st_asagi": "kesişim günü (1/0)",
    "kirilim20 kirilim55 kirilim52": "kapanış önceki 20/55 gün ya da 52 hafta tepesinin üstünde (1/0)",
    "sup_boga sup_ayi": "günlük likidite süpürmesi: dünkü 20 gün dibinin altına fitil, kapanış geri üstünde (1/0)",
    "ic_bar dis_bar cekic": "mum kalıpları (1/0)", "ardisik_dusus ardisik_yukselis": "üst üste düşen/yükselen gün sayısı",
    "gun_hafta": "0 Pazartesi ... 4 Cuma",
    "bosluk_yukari bosluk_asagi": "bugün ≥0,3 ATR açılış boşluğu (1/0)",
    "h_kapanis h_rsi h_ema10 h_ema20 h_ema40 h_supertrend_yon h_macd_hist h_trend": "HAFTALIK (son tamamlanan hafta) değerler: çoklu zaman dilimi tarama/test; h_trend = kapanış>EMA10>EMA40",
}

def _g(s, idx):
    """pandas_ta kısa geçmişte None döndürür: NaN seriyle değiştir."""
    return s if s is not None else pd.Series(np.nan, index=idx)

def hesapla(d, ref=None):
    o, h, l, c, v = d.open, d.high, d.low, d.close, d.volume.fillna(0)
    x = pd.DataFrame(index=d.index)
    x["kapanis"], x["acilis"], x["yuksek"], x["dusuk"], x["hacim"] = c, o, h, l, v
    for n in (20, 50, 200): x[f"ema{n}"] = _g(ta.ema(c, n), d.index)
    for n in (50, 200): x[f"sma{n}"] = _g(ta.sma(c, n), d.index)
    x["rsi"], x["rsi2"] = ta.rsi(c, 14), ta.rsi(c, 2)
    x["atr"] = ta.atr(h, l, c, 14); x["atr_yuzde"] = x.atr / c * 100
    for n in (20, 50, 200): x[f"uz{n}"] = (c - x[f"ema{n}"]) / x.atr
    m = ta.macd(c); x["macd"], x["macd_hist"], x["macd_sinyal"] = m.iloc[:, 0], m.iloc[:, 1], m.iloc[:, 2]
    a = ta.adx(h, l, c); x["adx"], x["dip_plus"], x["dip_minus"] = a.iloc[:, 0], a.iloc[:, 1], a.iloc[:, 2]
    b = ta.bbands(c, 20, 2); x["bb_alt"], x["bb_ust"] = b.iloc[:, 0], b.iloc[:, 2]
    x["bb_genislik"] = (x.bb_ust - x.bb_alt) / c * 100
    x["sikisma"] = (x.bb_genislik.rolling(252, min_periods=100).rank(pct=True) <= 0.10).astype(int)
    st = ta.supertrend(h, l, c, 10, 3); x["supertrend_yon"] = st.iloc[:, 1]
    sk = ta.stoch(h, l, c); x["stoch_k"], x["stoch_d"] = sk.iloc[:, 0], sk.iloc[:, 1]
    x["mfi"] = ta.mfi(h, l, c, v.astype(float), 14) if v.sum() else 50
    obv = ta.obv(c, v); x["obv_egim"] = (obv - obv.shift(20)) / (v.rolling(20).mean() * 20 + 1e-9)
    x["cmf"] = ta.cmf(h, l, c, v.astype(float), length=20) if v.sum() else 0
    x["hacim_oran"] = v / (v.rolling(20).mean() + 1e-9)
    x["zirve52"] = (c / h.rolling(252, min_periods=60).max() - 1) * 100
    x["dip52"] = (c / l.rolling(252, min_periods=60).min() - 1) * 100
    x["yuksek20"], x["dusuk20"], x["yuksek55"] = h.shift(1).rolling(20).max(), l.shift(1).rolling(20).min(), h.shift(1).rolling(55).max()
    for n in (1, 5, 20, 60, 120): x[f"getiri{n}"] = c.pct_change(n) * 100
    if ref is not None:
        r = ref.close.reindex(c.index).ffill()
        x["rs20"] = (c.pct_change(20) - r.pct_change(20)) * 100; x["rs60"] = (c.pct_change(60) - r.pct_change(60)) * 100
        rl = c / r; x["rs_tepe"] = (rl >= rl.rolling(63).max() * 0.995).astype(int)
    else:
        x["rs20"] = x["rs60"] = 0.0; x["rs_tepe"] = 0
    def kes(a_, b_, yon): return ((a_ > b_) & (a_.shift() <= b_.shift())).astype(int) if yon > 0 else ((a_ < b_) & (a_.shift() >= b_.shift())).astype(int)
    x["ema20_50_yukari"], x["ema20_50_asagi"] = kes(x.ema20, x.ema50, 1), kes(x.ema20, x.ema50, -1)
    x["ema50_200_yukari"], x["ema50_200_asagi"] = kes(x.ema50, x.ema200, 1), kes(x.ema50, x.ema200, -1)
    x["macd_yukari"], x["macd_asagi"] = kes(x.macd, x.macd_sinyal, 1), kes(x.macd, x.macd_sinyal, -1)
    x["st_yukari"] = ((x.supertrend_yon == 1) & (x.supertrend_yon.shift() == -1)).astype(int)
    x["st_asagi"] = ((x.supertrend_yon == -1) & (x.supertrend_yon.shift() == 1)).astype(int)
    x["kirilim20"], x["kirilim55"] = (c > x.yuksek20).astype(int), (c > x.yuksek55).astype(int)
    x["kirilim52"] = (c >= h.shift(1).rolling(252, min_periods=60).max()).astype(int)
    x["sup_boga"] = ((l < x.dusuk20) & (c > x.dusuk20)).astype(int)
    x["sup_ayi"] = ((h > x.yuksek20) & (c < x.yuksek20)).astype(int)
    x["ic_bar"] = ((h < h.shift()) & (l > l.shift())).astype(int)
    x["dis_bar"] = ((h > h.shift()) & (l < l.shift())).astype(int)
    govde = (c - o).abs(); alt_f = np.minimum(o, c) - l; ust_f = h - np.maximum(o, c)
    x["cekic"] = ((alt_f > 2 * govde) & (ust_f < govde) & (x.rsi < 40)).astype(int)
    dus = (c < c.shift()).astype(int); yuk = (c > c.shift()).astype(int)
    x["ardisik_dusus"] = dus.groupby((dus == 0).cumsum()).cumsum()
    x["ardisik_yukselis"] = yuk.groupby((yuk == 0).cumsum()).cumsum()
    x["gun_hafta"] = x.index.dayofweek
    x["bosluk_yukari"] = (l > h.shift() + 0.3 * x.atr.shift()).astype(int)
    x["bosluk_asagi"] = (h < l.shift() - 0.3 * x.atr.shift()).astype(int)
    # HAFTALIK (çoklu zaman dilimi) sütunlar: h_ önekli; TAMAMLANMIŞ hafta değeri (ileriye bakma yok)
    w = d.resample("W-FRI").agg({"open": "first", "high": "max", "low": "min", "close": "last", "volume": "sum"}).dropna()
    if len(w) > 60:
        hw = pd.DataFrame(index=w.index); hw["h_kapanis"] = w.close; hw["h_rsi"] = ta.rsi(w.close, 14)
        hw["h_ema10"], hw["h_ema20"], hw["h_ema40"] = ta.ema(w.close, 10), ta.ema(w.close, 20), ta.ema(w.close, 40)
        hw["h_supertrend_yon"] = ta.supertrend(w.high, w.low, w.close, 10, 3).iloc[:, 1]
        hw["h_macd_hist"] = ta.macd(w.close).iloc[:, 1]; hw["h_trend"] = ((w.close > hw.h_ema10) & (hw.h_ema10 > hw.h_ema40)).astype(int)
        hw = hw.shift(1); hw.index = hw.index + pd.Timedelta(days=1)
        x = x.join(hw.reindex(x.index, method="ffill"))
    return x

def dsl(ifade):
    s = " " + ifade.strip() + " "
    s = re.sub(r"\s+ve\s+", " & ", s, flags=re.I); s = re.sub(r"\s+veya\s+", " | ", s, flags=re.I)
    s = re.sub(r"\s+değil\s+|\s+degil\s+", " ~ ", s, flags=re.I)
    s = s.replace("=<", "<=").replace("=>", ">=")
    s = re.sub(r"(?<![<>=!])=(?!=)", "==", s)
    # her karşılaştırmayı paranteze al: & | önceliği için
    parca = re.split(r"(\&|\|)", s)
    return " ".join(p if p in ("&", "|") else f"({p.strip()})" for p in parca if p.strip())

def degerlendir(x, ifade):
    return x.eval(dsl(ifade), engine="python").fillna(False).astype(bool)

if __name__ == "__main__":
    print("DSL adları (tarama.py / backtest.py ifadelerinde kullan; 've' 'veya' 'değil'):")
    for k, v in ADLAR.items(): print(f"  {k:<60} {v}")

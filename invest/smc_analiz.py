#!/usr/bin/env python3
"""SMC / ICT + klasik indikatör analizi (Enes 25.11.2026 22:11 onayı: pip smartmoneyconcepts + pandas_ta).

Kullanım:
  python3 invest/smc_analiz.py ^NDX 1d            # günlük, 2 yıl
  python3 invest/smc_analiz.py ^NDX 4h            # 60m veriden 4 saatlik (60 gün)
  python3 invest/smc_analiz.py NVDA 1h --png g/x.png
Gerekirse önce: pip install --break-system-packages -q smartmoneyconcepts pandas_ta
Veri: Yahoo chart uç noktası (ham, düzeltmesiz). Çıktı: metin özet (+ istenirse işaretli grafik PNG).
Not: Yahoo 4 saatlik mum vermez; 60m mumlardan seans başına (ABD 16:30 TSİ) 4h üretilir, IG/TradingView mumlarıyla birkaç puan fark olabilir.
"""
import sys, json, urllib.request, warnings
import pandas as pd
warnings.filterwarnings("ignore")

def veri(t, aralik):
    i, r = {"1d": ("1d", "2y"), "4h": ("60m", "60d"), "1h": ("60m", "30d"), "1wk": ("1wk", "10y")}[aralik]
    u = f"https://query1.finance.yahoo.com/v8/finance/chart/{t}?interval={i}&range={r}"
    d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=20))["chart"]["result"][0]
    q = d["indicators"]["quote"][0]
    df = pd.DataFrame({"open": q["open"], "high": q["high"], "low": q["low"], "close": q["close"], "volume": q["volume"]},
                      index=pd.to_datetime(d["timestamp"], unit="s", utc=True).tz_convert("Europe/Istanbul")).dropna()
    if aralik == "4h":
        df = df.resample("4h", offset="30min").agg({"open": "first", "high": "max", "low": "min", "close": "last", "volume": "sum"}).dropna()
    return df

def main(a):
    from smartmoneyconcepts import smc
    import pandas_ta as ta
    t, aralik = a[0], (a[1] if len(a) > 1 else "1d")
    df = veri(t, aralik); df["volume"] = df["volume"].fillna(0)
    c = df["close"]; son = c.iloc[-1]
    sw = 10 if aralik in ("1d", "1wk") else 6
    shl = smc.swing_highs_lows(df, swing_length=sw)
    bc = smc.bos_choch(df, shl, close_break=True)
    fvg = smc.fvg(df, join_consecutive=True)
    ob = smc.ob(df, shl, close_mitigation=False)
    liq = smc.liquidity(df, shl, range_percent=0.01)
    out = []
    out.append(f"{t} {aralik}  son {son:,.1f}  ({df.index[-1]:%d.%m %H:%M})")
    e20, e50, e200 = ta.ema(c, 20).iloc[-1], ta.ema(c, 50).iloc[-1], ta.ema(c, 200).iloc[-1] if len(c) > 200 else float("nan")
    rsi = ta.rsi(c, 14).iloc[-1]; atr = ta.atr(df.high, df.low, c, 14).iloc[-1]
    st = ta.supertrend(df.high, df.low, c, 10, 3); st_yon = int(st.iloc[-1, 1]) if st is not None else 0
    macd = ta.macd(c); mh = macd.iloc[-1, 1] if macd is not None else float("nan")
    bb = ta.bbands(c, 20, 2)
    out.append(f"EMA20 {e20:,.0f} | EMA50 {e50:,.0f} | EMA200 {e200:,.0f} | RSI14 {rsi:.1f} | ATR14 {atr:,.0f} | Supertrend {'YUKARI' if st_yon > 0 else 'AŞAĞI'} | MACD hist {mh:,.1f}")
    if bb is not None: out.append(f"Bollinger: alt {bb.iloc[-1,0]:,.0f} orta {bb.iloc[-1,1]:,.0f} üst {bb.iloc[-1,2]:,.0f}")
    # yapı
    sh = shl.dropna(subset=["HighLow"]).tail(6)
    out.append("Son swingler: " + ", ".join(f"{'T' if r.HighLow == 1 else 'D'} {r.Level:,.0f} ({i:%d.%m})" for i, r in zip(df.index[shl['HighLow'].notna()][-6:], sh.itertuples())))
    b = bc.dropna(subset=["BOS", "CHOCH"], how="all").tail(4)
    for i, r in zip(df.index[bc[['BOS','CHOCH']].notna().any(axis=1)][-4:], b.itertuples()):
        tip = "BOS" if pd.notna(r.BOS) else "CHoCH"; yon = (r.BOS if pd.notna(r.BOS) else r.CHOCH)
        out.append(f"  {tip} {'yukarı' if yon > 0 else 'aşağı'} seviye {r.Level:,.0f} ({i:%d.%m})")
    # açık FVG ve OB (fiyata yakın, doldurulmamış)
    f = fvg.copy(); f["t"] = df.index; f = f.dropna(subset=["FVG"]); f = f[f["MitigatedIndex"].fillna(0) == 0].tail(6)
    for r in f.itertuples(): out.append(f"  Açık {'boğa' if r.FVG > 0 else 'ayı'} FVG {r.Bottom:,.0f}–{r.Top:,.0f} ({r.t:%d.%m})")
    o = ob.copy(); o["t"] = df.index; o = o.dropna(subset=["OB"]); o = o[o["MitigatedIndex"].fillna(0) == 0].tail(4)
    for r in o.itertuples(): out.append(f"  Emir bloğu {'boğa' if r.OB > 0 else 'ayı'} {r.Bottom:,.0f}–{r.Top:,.0f} ({r.t:%d.%m})")
    l = liq.copy(); l["t"] = df.index; l = l.dropna(subset=["Liquidity"]); l = l[l["Swept"].fillna(0) == 0].tail(4)
    for r in l.itertuples(): out.append(f"  Alınmamış likidite {'tepe (BSL)' if r.Liquidity > 0 else 'dip (SSL)'} {r.Level:,.0f} ({r.t:%d.%m})")
    if aralik in ("4h", "1h"):
        ph = smc.previous_high_low(df, time_frame="1D"); out.append(f"Önceki gün T/D: {ph['PreviousHigh'].iloc[-1]:,.0f} / {ph['PreviousLow'].iloc[-1]:,.0f}")
    hi, lo = df.high.tail(60).max(), df.low.tail(60).min(); eq = (hi + lo) / 2
    out.append(f"Dealing range (son 60 mum) {lo:,.0f}–{hi:,.0f}, denge {eq:,.0f} -> fiyat {'PAHALI (premium)' if son > eq else 'UCUZ (discount)'}")
    print("\n".join(out))
    if "--png" in a:
        import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
        d = df.tail(120); fig, ax = plt.subplots(figsize=(10.8, 6.5), dpi=100, facecolor="#0B0E14"); ax.set_facecolor("#0B0E14")
        for k, (i, r) in enumerate(d.iterrows()):
            col = "#2BD47D" if r.close >= r.open else "#FF5A5F"
            ax.plot([k, k], [r.low, r.high], color=col, lw=0.8); ax.add_patch(plt.Rectangle((k - 0.3, min(r.open, r.close)), 0.6, abs(r.close - r.open) or 0.1, color=col))
        n0 = len(df) - len(d)
        for r in f.itertuples():
            k = df.index.get_loc(r.t) - n0
            if k > 0: ax.add_patch(plt.Rectangle((k, r.Bottom), len(d) - k, r.Top - r.Bottom, color="#3D8BFF" if r.FVG > 0 else "#E8B44C", alpha=0.18))
        for r in l.itertuples(): ax.axhline(r.Level, color="#8A94A6", ls=":", lw=1)
        ax.tick_params(colors="#8A94A6"); [s.set_color("#222A36") for s in ax.spines.values()]
        ax.set_title(f"{t} {aralik} • SMC (FVG mavi/sarı, likidite noktalı)", color="#F2F4F8")
        fig.savefig(a[a.index("--png") + 1], facecolor=fig.get_facecolor(), bbox_inches="tight")

if __name__ == "__main__":
    main(sys.argv[1:])

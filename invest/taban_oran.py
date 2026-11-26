"""KURAL 96 — Tarihsel taban oranı (Enes 26.11 18:59: 'Bu tarz tweetler istiyorum ... tweet'in tarzı').
Bir koşul ilk kez oluştuğunda (olaylar arası en az --ara gün) endeksin sonraki getirilerini Yahoo günlük kapanışından hesaplar.
Veri yalnız ham Yahoo kapanışı; uydurma yok. Çıktı tweete 'kendi hesabım' olarak girer, yöntem satırı kartta yazılır.

Kullanım:
  python3 invest/taban_oran.py vix_ust 30            VIX kapanışı >= 30 ilk kez (^GSPC sonrası)
  python3 invest/taban_oran.py vix_ust 30 --endeks ^NDX
  python3 invest/taban_oran.py zirveden -20          endeks zirveden en az %20 aşağıda ilk kez
  python3 invest/taban_oran.py dusus_gun 5           art arda 5 düşüş günü
  python3 invest/taban_oran.py rsi_alt 30            14 günlük RSI 30 altı
  python3 invest/taban_oran.py gunluk -3             tek günde en az %3 düşüş
Seçenekler: --endeks ^GSPC|^NDX|QQQ|... (varsayılan ^GSPC)  --bas 1990-01-01  --ara 30  --json
Çıktı: olay sayısı, 1/3/6/12 ay sonra pozitif oranı, ortalama ve medyan getiri, en kötü, son 5 olay tarihi, bugün koşul sağlanıyor mu.
"""
import sys, json, urllib.request, datetime as dt
import pandas as pd

def yahoo(s, bas):
    p1 = int(dt.datetime.fromisoformat(bas).replace(tzinfo=dt.timezone.utc).timestamp()); p2 = int(dt.datetime.now(dt.timezone.utc).timestamp())
    u = f"https://query1.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(s)}?period1={p1}&period2={p2}&interval=1d"
    d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=60))["chart"]["result"][0]
    t = [dt.datetime.fromtimestamp(x, dt.timezone.utc).date() for x in d["timestamp"]]
    return pd.Series(d["indicators"]["quote"][0]["close"], index=pd.to_datetime(t)).dropna()

def rsi(s, n=14):
    d = s.diff(); u = d.clip(lower=0).ewm(alpha=1/n, adjust=False).mean(); a = (-d.clip(upper=0)).ewm(alpha=1/n, adjust=False).mean()
    return 100 - 100 / (1 + u / a)

def main(a):
    import urllib.parse  # noqa
    if len(a) < 2: print(__doc__); return
    kosul, esik = a[0], float(a[1])
    op = lambda k, v: a[a.index(k) + 1] if k in a else v
    endeks, bas, ara = op("--endeks", "^GSPC"), op("--bas", "1990-01-01"), int(op("--ara", "30"))
    px = yahoo(endeks, bas)
    if kosul == "vix_ust": v = yahoo("^VIX", bas).reindex(px.index).ffill(); m = v >= esik; ad = f"VIX kapanışı {esik:g} ve üstü"
    elif kosul == "zirveden": dd = 100 * (px / px.cummax() - 1); m = dd <= esik; ad = f"{endeks} zirveden %{abs(esik):g} ve fazla aşağıda"
    elif kosul == "dusus_gun":
        dn = (px.diff() < 0).astype(int); seri = dn.groupby((dn != dn.shift()).cumsum()).cumsum() * dn; m = seri >= esik; ad = f"art arda {esik:g} düşüş günü"
    elif kosul == "rsi_alt": m = rsi(px) < esik; ad = f"{endeks} 14 günlük RSI {esik:g} altı"
    elif kosul == "gunluk": m = 100 * px.pct_change() <= esik; ad = f"{endeks} tek günde %{abs(esik):g} ve fazla düşüş"
    else: print("bilinmeyen koşul"); return
    olay, son = [], None
    for t, ok in m.items():
        if ok and (son is None or (t - son).days >= ara): olay.append(t); son = t
    ufuk = {"1 ay": 21, "3 ay": 63, "6 ay": 126, "12 ay": 252}; sonuc = {}
    idx = list(px.index)
    for u, n in ufuk.items():
        g = []
        for t in olay:
            i = idx.index(t)
            if i + n < len(idx): g.append(100 * (px.iloc[i + n] / px.iloc[i] - 1))
        if g:
            s = pd.Series(g); sonuc[u] = {"n": len(g), "pozitif_%": round(100 * (s > 0).mean(), 1), "ort_%": round(s.mean(), 1), "medyan_%": round(s.median(), 1), "en_kotu_%": round(s.min(), 1)}
    taban = {}
    for u, n in ufuk.items():
        r = 100 * (px.shift(-n) / px - 1); r = r.dropna()
        taban[u] = {"pozitif_%": round(100 * (r > 0).mean(), 1), "ort_%": round(r.mean(), 1)}
    out = {"kosul": ad, "endeks": endeks, "donem": f"{px.index[0].date()} - {px.index[-1].date()}", "olay": len(olay), "son_olaylar": [str(t.date()) for t in olay[-5:]],
           "bugun_saglaniyor": bool(m.iloc[-1]), "sonra": sonuc, "her_gun_taban": taban, "yontem": f"Yahoo günlük kapanış, koşulun ilk görüldüğü gün, olaylar arası en az {ara} gün"}
    if "--json" in a: print(json.dumps(out, ensure_ascii=False, indent=1)); return
    print(f"{ad} | {endeks} | {out['donem']} | {len(olay)} olay (en az {ara} gün ara) | bugün sağlanıyor: {out['bugun_saglaniyor']}")
    for u, v in sonuc.items():
        tb = taban[u]; print(f"  {u} sonra: n={v['n']} pozitif %{v['pozitif_%']} (her gün tabanı %{tb['pozitif_%']}) | ort %{v['ort_%']} (taban %{tb['ort_%']}) | medyan %{v['medyan_%']} | en kötü %{v['en_kotu_%']}")
    print("  son olaylar:", ", ".join(out["son_olaylar"]))
    print("  KURAL 96: tweete yalnız tabandan FARKLI olan ufku yaz; fark yoksa 'tarih bu koşulda ek avantaj göstermiyor' de ya da tweet atma.")

if __name__ == "__main__":
    import urllib.parse
    main(sys.argv[1:])

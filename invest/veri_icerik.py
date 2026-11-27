#!/usr/bin/env python3
"""veri_icerik.py — kural 92: veri tabanlı haftalık kısa tweet paketi (Enes 26.11 08:49 "1-8 hepsi okey").
Her alt komut: ÖZET (tweet için rakamlar + okuma) ve --kart ile kart3 görseli üretir.
  vix        Korku vade yapısı: VIX / VIX3M (Yahoo). >1 = ters dönmüş (panik), 20 yıllık kanıt (Nasdaq 100 20 gün sonrası, taban oranlı).
  kredi      Yüksek getirili tahvil primi (FRED BAMLH0A0HYM2, WebFetch -> fred_ekle).
  genislik   Nasdaq 100: 50G ve 200G üstü hisse oranı + yıllık dibine %5 yakın hisse sayısı (kendi hesabım, gosterge önbelleği).
  putcall    CBOE hisse put/call 5 günlük ortalama (nabiz.json'da biriken günlük değerlerden).
  aciga      Portföy açığa satış radarı (ORTEX, Bigdata.com -> alt_veri.py si): 4 haftalık değişim sıralaması.
  fed        Fed net likidite = Fed bilançosu (WALCL) − Hazine hesabı (WTREGEN) − ters repo (RRPONTSYD) (FRED, kendi hesabım).
  iceriden   Yönetici piyasadan alım radarı (Alpha Vantage INSIDER_TRANSACTIONS -> iceriden_ekle), son 30 gün.
  faiz       Faiz eğrisi 10Y−2Y (T10Y2Y) ve 10 yıllık reel faiz (DFII10) (FRED).
Kullanım: python3 invest/veri_icerik.py <komut> [--kart g/YYYYMMDD_HHMM_<komut>.jpg]
          python3 invest/veri_icerik.py fred_ekle <SERİ> < csv   (WebFetch: https://fred.stlouisfed.org/graph/fredgraph.csv?id=<SERİ> ; istem "son 120 satırı 'YYYY-MM-DD,değer' CSV ver, yorum yok")
          python3 invest/veri_icerik.py iceriden_ekle <T> < av.json
"""
import sys, os, io, json, datetime as dt, warnings
import numpy as np, pandas as pd
warnings.filterwarnings("ignore")
D = os.path.dirname(os.path.abspath(__file__)); AV = os.path.join(D, "alt_veri"); os.makedirs(AV, exist_ok=True)
def arg(a, k): return a[a.index(k) + 1] if k in a else None
def fred(s):
    f = os.path.join(AV, f"fred_{s}.csv")
    if not os.path.exists(f): sys.exit(f"FRED {s} kaydı yok: WebFetch https://fred.stlouisfed.org/graph/fredgraph.csv?id={s} -> fred_ekle {s}")
    x = pd.read_csv(f, header=None, names=["t", "v"]); x["v"] = pd.to_numeric(x.v, errors="coerce"); return x.dropna().drop_duplicates("t", keep="last").sort_values("t")
def fred_ekle(s, metin):
    y = pd.read_csv(io.StringIO(metin.strip()), header=None, names=["t", "v"]); y = y[y.t.str.match(r"\d{4}-\d{2}-\d{2}")]
    f = os.path.join(AV, f"fred_{s}.csv"); x = pd.concat([pd.read_csv(f, header=None, names=["t", "v"]) if os.path.exists(f) else None, y])
    x.drop_duplicates("t", keep="last").sort_values("t").to_csv(f, header=False, index=False); print(f"FRED {s}: {len(x.drop_duplicates('t'))} satır, son {y.iloc[-1].t} {y.iloc[-1].v}")
def kart_cizgi(out, kicker, baslik, alt, seri, sonuc, kaynak, ref=(), kahraman=None, renk=None):
    import kart3 as K
    K.cizgi_pro(kicker, baslik, alt, [(str(a), float(b)) for a, b in seri], [], sonuc, kaynak, out, zirve=False, ref=list(ref), kahraman=kahraman, **({"renk": renk} if renk else {}))
    print("kart:", out)

def vix(a):
    from gosterge import veri
    from veri_kalite import kanit
    v, v3, n = veri("^VIX", "20y").close, veri("^VIX3M", "20y").close, veri("^NDX", "20y").close
    r = (v / v3).dropna(); son = r.iloc[-1]; yuz = (r < son).mean() * 100
    gun = 0
    for x in r[::-1]:
        if x > 1: gun += 1
        else: break
    giris = r[(r > 1) & (r.shift() <= 1)]; ileri = (n.shift(-20) / n - 1).reindex(giris.index).dropna()
    sec = [];
    for t_ in ileri.index:
        if not sec or (t_ - sec[-1]).days > 30: sec.append(t_)
    g = ileri.loc[sec].tolist(); tb = ((n.shift(-20) / n - 1).dropna() > 0).mean() * 100; k = kanit(g, tb)
    print(f"VIX {v.iloc[-1]:.2f} / VIX3M {v3.iloc[-1]:.2f} = {son:.3f} ({'TERS DÖNMÜŞ: kısa vadeli korku uzun vadeliden yüksek' if son > 1 else 'normal: kısa vade uzun vadenin altında'}) | 20 yılın %{yuz:.0f}. yüzdeliği | {gun} gündür 1 üstünde")
    print(f"KANIT: oran 1'in üstüne ilk çıktığında ({k['n']} olay, ≥30 gün arayla) Nasdaq 100 20 gün sonra yukarı %{k['oran']:.0f} (taban %{tb:.0f}) -> {k['hukum'].split(' (')[0]}; medyan {np.median(g) * 100:+.1f}%")
    if arg(a, "--kart"):
        s = r.tail(250); kart_cizgi(arg(a, "--kart"), "Piyasa nabzı • Korku vade yapısı", f"VIX / VIX3M: {son:.2f}".replace(".", ","),
            "Kısa vadeli korkunun 3 aylığa oranı; 1 üstü = ters", list(zip(s.index.date, s.values)),
            f"20 yılda {k['n']} olay: Nasdaq 20 günde %{k['oran']:.0f} yukarı (tüm günler %{tb:.0f})", "Cboe VIX ve VIX3M (Yahoo Finance), kendi hesabım", ref=[(1.0, "")])

def kredi(a):
    x = fred("BAMLH0A0HYM2"); son = x.iloc[-1]; h = x.iloc[-6] if len(x) > 5 else x.iloc[0]
    print(f"Yüksek getirili tahvil primi {son.t}: %{son.v:.2f} | 1 hafta önce %{h.v:.2f} ({(son.v - h.v) * 100:+.0f} baz puan) | kayıt aralığı %{x.v.min():.2f}-%{x.v.max():.2f} ({len(x)} gün)")
    print("okuma: " + ("kredi stresi YÜKSEK (>%5)" if son.v > 5 else "gerilim var ama panik yok (%4-5)" if son.v > 4 else "kredi piyasası sakin (<%4): hisse satışı tahvile sıçramamış"))
    if arg(a, "--kart"):
        kart_cizgi(arg(a, "--kart"), "Piyasa nabzı • Kredi", f"Yüksek getirili tahvil primi %{son.v:.2f}".replace(".", ","), "ABD yüksek getirili tahvil getirisi eksi hazine, yüzde puan",
                   list(zip(x.t.tail(120), x.v.tail(120))), f"Bir haftada {(son.v - h.v) * 100:+.0f} baz puan".replace("-", "−"), "ICE BofA / FRED (St. Louis Fed)")

def genislik(a):
    from gosterge import veri
    from teknik_ust import NDX100
    C = {}
    for t in NDX100:
        try: C[t] = veri(t, "2y").close
        except Exception: pass
    P = pd.DataFrame(C).ffill().iloc[-300:]
    u50 = (P > P.rolling(50).mean()).sum(axis=1) / P.notna().sum(axis=1) * 100
    u200 = (P > P.rolling(200).mean()).sum(axis=1) / P.notna().sum(axis=1) * 100
    dip = (P <= P.rolling(252, min_periods=120).min() * 1.05).sum(axis=1)
    s50 = u50.dropna().iloc[-120:]
    print(f"Nasdaq 100 genişlik {s50.index[-1].date()}: 50G üstü %{u50.iloc[-1]:.0f} (1 hafta önce %{u50.iloc[-6]:.0f}), 200G üstü %{u200.iloc[-1]:.0f}, yıllık dibine %5 yakın {int(dip.iloc[-1])} hisse ({len(C)} hisse tarandı)")
    print("okuma: " + ("yıkanmış (<%15): dip bölgesi bağlamı" if u50.iloc[-1] < 15 else "aşırı geniş (>%85): tepe riski bağlamı" if u50.iloc[-1] > 85 else "orta bölge"))
    if arg(a, "--kart"):
        kart_cizgi(arg(a, "--kart"), "Piyasa nabzı • Genişlik", f"Nasdaq 100'ün %{u50.iloc[-1]:.0f}'i 50 günlüğün üstünde", "50 günlük ortalamanın üstünde kapanan hisse oranı, kendi taramam",
                   list(zip(s50.index.date, s50.values)), f"200 günlük üstü %{u200.iloc[-1]:.0f}; yıllık dibe yakın {int(dip.iloc[-1])} hisse", "Kendi hesabım, Yahoo Finance kapanışları", ref=[(15, "15"), (85, "85")])

def putcall(a):
    N = json.load(open(os.path.join(AV, "nabiz.json"))) if os.path.exists(os.path.join(AV, "nabiz.json")) else []
    s = pd.Series({z["tarih"]: z["pc_hisse"] for z in N if "pc_hisse" in z}).sort_index()
    if len(s) == 0: sys.exit("put/call kaydı yok (sabah nabız rutini biriktirir)")
    o5 = s.tail(5).mean(); print(f"CBOE hisse put/call son {s.index[-1]}: {s.iloc[-1]:.2f} | 5 gün ort {o5:.2f} ({len(s.tail(5))} gün) | kayıt {len(s)} gün, aralık {s.min():.2f}-{s.max():.2f}")
    print("okuma (5 gün ort.): " + ("korunma yüksek (>0,75), kalabalık korkuyor" if o5 > .75 else "call kovalanıyor (<0,50), kalabalık iyimser" if o5 < .5 else "olağan bölge"))
    if arg(a, "--kart") and len(s) >= 5:
        kart_cizgi(arg(a, "--kart"), "Piyasa nabzı • Opsiyon", f"Hisse put/call 5 günlük ort. {o5:.2f}".replace(".", ","), "CBOE hisse opsiyonları, put hacmi / call hacmi",
                   list(zip(s.index, s.values)), "0,75 üstü korunma, 0,50 altı iyimserlik", "Cboe Global Markets", ref=[(0.75, "0,75"), (0.5, "0,50")])

def aciga(a):
    import kart3 as K
    rows = []
    for f in os.listdir(AV):
        if not f.endswith(".json") or f.startswith(("fred", "nabiz", "av_", "bigdata", "aaii", "korku", "insider")): continue
        S = json.load(open(os.path.join(AV, f))).get("si", []) if f[:-5].isupper() else []
        if len(S) >= 5: rows.append((f[:-5], S[-1]["kisa_yuzde"], S[-1]["kisa_yuzde"] - S[-5]["kisa_yuzde"], (S[-1]["fiyat"] / S[-5]["fiyat"] - 1) * 100, S[-1]["tarih"]))
    if not rows: sys.exit("açığa satış kaydı yok (Pazartesi bigdata_history_tearsheet -> alt_veri.py si)")
    rows.sort(key=lambda z: -z[2])
    for t, k, d, p, tr in rows: print(f"{t:<5} açığa satış %{k:.2f} | 4 haftada {d:+.2f} puan | fiyat {p:+.1f}% | {tr}")
    if arg(a, "--kart"):
        K.siralama("Piyasa nabzı • Açığa satış", "Portföyde açığa satış, 4 haftalık değişim", "Serbest dolaşıma oran, yüzde puan değişim (ORTEX tahmini)",
                   [(t, round(d, 2)) for t, k, d, p, tr in rows], f"En çok artan {rows[0][0]}, en çok azalan {rows[-1][0]}", "ORTEX (Bigdata.com)", arg(a, "--kart"), birim=" puan")
        print("kart:", arg(a, "--kart"))

def fed(a):
    W, T, R = fred("WALCL"), fred("WTREGEN"), fred("RRPONTSYD")
    w = W.set_index("t").v / 1e6; tg = T.set_index("t").v / 1e6; rr = R.set_index("t").v / 1e3   # trilyon $ (WALCL ve WTREGEN milyon, RRP milyar)
    idx = sorted(set(w.index)); s = pd.Series({d: w[d] - tg.loc[:d].iloc[-1] - rr.loc[:d].iloc[-1] for d in idx if len(tg.loc[:d]) and len(rr.loc[:d])})
    son, once = s.iloc[-1], s.iloc[-2] if len(s) > 1 else s.iloc[-1]
    print(f"Fed net likidite {s.index[-1]}: {son:.3f} trilyon $ (önceki hafta {once:.3f}, {(son - once) * 1000:+.0f} milyar $) | bilanço {w.iloc[-1]:.3f}, Hazine hesabı {tg.iloc[-1]:.3f}, ters repo {rr.iloc[-1] * 1000:.0f} milyar")
    if arg(a, "--kart"):
        kart_cizgi(arg(a, "--kart"), "Piyasa nabzı • Likidite", f"Fed net likidite {son:.2f} trilyon $".replace(".", ","), "Fed bilançosu − Hazine hesabı − ters repo, kendi hesabım",
                   list(zip(s.index, s.values)), f"Bir haftada {(son - once) * 1000:+.0f} milyar $".replace("-", "−"), "Federal Reserve H.4.1 / FRED, kendi hesabım")

def iceriden_ekle(t, metin):
    j = json.loads(metin); json.dump(j, open(os.path.join(AV, f"insider_{t.upper()}.json"), "w")); print(f"içeriden işlem kaydedildi {t}: {len(j.get('data', []))} satır")
def iceriden(a):
    import kart3 as K
    sinir = (dt.date.today() - dt.timedelta(days=30)).isoformat(); rows = []
    for f in os.listdir(AV):
        if not f.startswith("insider_"): continue
        t = f[8:-5]; df = pd.DataFrame(json.load(open(os.path.join(AV, f))).get("data", []))
        if df.empty: continue
        df = df[df.transaction_date >= sinir]; df["tutar"] = df.shares.astype(float) * df.share_price.astype(float)
        al = df[(df.acquisition_or_disposal == "A") & (df.share_price.astype(float) > 0)]; sat = df[df.acquisition_or_disposal.isin(["S", "D"])]
        rows.append((t, al.tutar.sum() / 1e6, al.executive.nunique(), sat.tutar.sum() / 1e6))
    rows.sort(key=lambda z: -z[1])
    for t, al, n, sat in rows: print(f"{t:<5} son 30 gün piyasadan alım {al:,.1f} Mn $ ({n} kişi) | satış {sat:,.1f} Mn $")
    alimci = [r for r in rows if r[1] > 0]
    print("okuma: " + (f"alım var: {', '.join(r[0] for r in alimci)} (birden çok yönetici = güçlü sinyal)" if alimci else "son 30 günde piyasadan yönetici alımı yok; satışlar çoğunlukla planlı (10b5-1)"))
    if arg(a, "--kart") and rows:
        K.siralama("Piyasa nabzı • Yönetici işlemleri", "Son 30 gün yönetici alım ve satışı", "Milyon $, piyasadan alım (+) ve satış (−)",
                   [(t, round(al - sat, 1)) for t, al, n, sat in rows], "Anlamlı sinyal birden çok yöneticinin aynı anda alımıdır", "SEC Form 4 (Alpha Vantage)", arg(a, "--kart"), birim=" Mn $")
        print("kart:", arg(a, "--kart"))

def faiz(a):
    e, r = fred("T10Y2Y"), fred("DFII10"); se, sr = e.iloc[-1], r.iloc[-1]
    print(f"10Y−2Y {se.t}: {se.v:+.2f} puan ({'pozitif eğim' if se.v > 0 else 'TERS eğri'}) | 1 ay önce {e.iloc[-22].v if len(e) > 21 else e.iloc[0].v:+.2f}")
    print(f"10 yıllık reel faiz {sr.t}: %{sr.v:.2f} | 1 ay önce %{r.iloc[-22].v if len(r) > 21 else r.iloc[0].v:.2f} -> büyüme hisselerinin iskonto oranı")
    if arg(a, "--kart"):
        kart_cizgi(arg(a, "--kart"), "Piyasa nabzı • Faiz", f"Reel faiz %{sr.v:.2f}, eğri {se.v:+.2f}".replace(".", ","), "10 yıllık enflasyondan arındırılmış faiz (TIPS), yüzde",
                   list(zip(r.t.tail(120), r.v.tail(120))), f"10 yıl − 2 yıl farkı {se.v:+.2f} puan".replace(".", ","), "US Treasury / FRED")

if __name__ == "__main__":
    a = sys.argv[1:]
    if not a: print(__doc__); sys.exit()
    k = a[0]
    if k == "fred_ekle": fred_ekle(a[1], sys.stdin.read())
    elif k == "iceriden_ekle": iceriden_ekle(a[1], sys.stdin.read())
    else: globals()[k](a)

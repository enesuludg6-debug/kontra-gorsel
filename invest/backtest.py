#!/usr/bin/env python3
"""backtest.py — strateji test motoru (TrendSpider Strategy Tester karşılığı + fazlası).
Kullanım:
  python3 invest/backtest.py <T|evren> --giris "<ifade>" [--cikis "<ifade>"] [--stop 2] [--hedef 4] [--sure 20]
         [--yon uzun|kisa] [--maliyet 0.1] [--yil 10] [--png g/bt.png] [--hazir <tarama_adı>]
  <T>   : tek hisse (AVGO, ^NDX)   evren: portfoy | ndx | hepsi | A,B,C (çok hisseli test: aşırı uydurmaya karşı)
  --stop/--hedef ATR katı (0 = kapalı), --sure en çok gün, --maliyet gidiş-dönüş % (komisyon+kayma)
Kurallar: sinyal kapanışta, giriş ERTESİ GÜN AÇILIŞTA (ileriye bakma yok); stop/hedef gün içinde, ikisi aynı gün = stop sayılır (kötümser).
Çıktı: işlem sayısı, kazanma oranı (+Wilson aralığı, TABAN: aynı günlerde rastgele giriş), ortalama R, kâr faktörü, beklenti,
       yıllık getiri, maksimum düşüş, al-tut kıyası, Sharpe; ÖRNEK DIŞI (ilk %70 / son %30); PARAMETRE DUYARLILIĞI (eşikler ±%10/±%20);
       MONTE CARLO (işlem sırası 2000 kez karıştırılır: düşüş ve getiri dağılımı); HÜKÜM; isteğe bağlı sermaye eğrisi PNG.
DSL adları: python3 invest/gosterge.py
"""
import sys, re, warnings
import numpy as np, pandas as pd
warnings.filterwarnings("ignore")
from gosterge import veri, hesapla, degerlendir
from veri_kalite import kanit

def arg(a, k, v=None, tip=str):
    return tip(a[a.index(k) + 1]) if k in a else v

def islemler(x, giris, cikis, stop, hedef, sure, yon, maliyet):
    g = giris if isinstance(giris, np.ndarray) else degerlendir(x, giris).values
    c_ = degerlendir(x, cikis).values if cikis else np.zeros(len(x), bool)
    o, h, l, c, atr = x.acilis.values, x.yuksek.values, x.dusuk.values, x.kapanis.values, x.atr.values
    s = 1 if yon == "uzun" else -1; T = []; i = 0; n = len(x)
    while i < n - 1:
        if not g[i] or np.isnan(atr[i]): i += 1; continue
        j = i + 1; gp = o[j]; risk = atr[i] * (stop if stop else 2)
        sp = gp - s * atr[i] * stop if stop else None; hp = gp + s * atr[i] * hedef if hedef else None
        cik, neden = None, "süre"
        for k in range(j, min(n, j + sure)):
            if sp is not None and ((s > 0 and l[k] <= sp) or (s < 0 and h[k] >= sp)): cik, neden = (min(o[k], sp) if s > 0 else max(o[k], sp)), "stop"; break
            if hp is not None and ((s > 0 and h[k] >= hp) or (s < 0 and l[k] <= hp)): cik, neden = (max(o[k], hp) if s > 0 else min(o[k], hp)), "hedef"; break
            if c_[k] and k > j: cik, neden = c[k], "çıkış"; break
        else:
            k = min(n - 1, j + sure - 1); cik = c[k]
        if cik is None: k = min(n - 1, j + sure - 1); cik = c[k]
        get = s * (cik / gp - 1) * 100 - maliyet
        T.append({"giris_t": x.index[j], "cikis_t": x.index[k], "giris": gp, "cikis": cik, "getiri": get,
                  "R": s * (cik - gp) / risk - maliyet / 100 * gp / risk, "gun": k - j + 1, "neden": neden})
        i = k + 1
    return pd.DataFrame(T)

def taban(x, giris_say, sure, yon, maliyet, tekrar=300, stop=2.0, hedef=4.0, cikis=""):
    """Rastgele girişler AYNI çıkış kurallarıyla (stop/hedef/süre): stratejinin giriş üstünlüğünü adil ölçer."""
    rng = np.random.default_rng(7); G = []
    for _ in range(3):
        m = np.zeros(len(x), bool); m[rng.integers(0, len(x) - 2, size=max(5, len(x) // 40))] = True
        T = islemler(x, m, cikis, stop, hedef, sure, yon, maliyet)
        if not T.empty: G.extend(T.getiri.tolist())
    G = np.array(G) if G else np.array([0.0])
    return (G > 0).mean() * 100, G.mean()

def ozet(T, x_list, yil_say, w=None):
    if T.empty: return None
    g = T.getiri.values; kaz = g[g > 0]; kay = g[g <= 0]
    pf = kaz.sum() / abs(kay.sum()) if len(kay) and kay.sum() else np.inf
    w = w if w is not None else (1 / min(len(x_list), 5) if len(x_list) > 1 else 1)
    T = T.sort_values("cikis_t"); eq = (1 + T.getiri / 100 * w).cumprod()
    dd = (eq / eq.cummax() - 1).min() * 100
    yillik = (eq.iloc[-1] ** (1 / max(yil_say, .5)) - 1) * 100
    sh = (g.mean() / g.std() * np.sqrt(252 / max(T.gun.mean(), 1))) if g.std() else 0
    return {"n": len(T), "kazanma": (g > 0).mean() * 100, "ort": g.mean(), "medyan": np.median(g), "R": T.R.mean(), "pf": pf,
            "dd": dd, "yillik": yillik, "sharpe": sh, "gun": T.gun.mean(), "eq": eq,
            "nedenler": T.neden.value_counts().to_dict(), "en_iyi": g.max(), "en_kotu": g.min()}

def monte_carlo(g, n=2000, w=1):
    g = np.asarray(g) * w
    rng = np.random.default_rng(11); dds, sonlar = [], []
    for _ in range(n):
        s = rng.permutation(g) if rng.random() < .5 else rng.choice(g, size=len(g), replace=True)
        eq = np.cumprod(1 + s / 100); dds.append((eq / np.maximum.accumulate(eq) - 1).min() * 100); sonlar.append((eq[-1] - 1) * 100)
    return np.percentile(dds, [50, 5]), np.percentile(sonlar, [5, 50, 95]), (np.array(sonlar) < 0).mean() * 100

def calistir(uni, a):
    giris = arg(a, "--giris"); cikis = arg(a, "--cikis", ""); stop = arg(a, "--stop", 2.0, float); hedef = arg(a, "--hedef", 4.0, float)
    sure = arg(a, "--sure", 20, int); yon = arg(a, "--yon", "uzun"); mal = arg(a, "--maliyet", 0.1, float); yil = arg(a, "--yil", 10, int)
    ref = veri("QQQ", f"{max(yil, 5)}y"); TT, XX = [], []
    for t in uni:
        try:
            x = hesapla(veri(t, f"{yil}y"), ref).iloc[200:]
            T = islemler(x, giris, cikis, stop, hedef, sure, yon, mal)
            if not T.empty: T["t"] = t; TT.append(T)
            XX.append(x)
        except Exception as e:
            print(f"  {t}: atlandı ({str(e)[:60]})")
    return (pd.concat(TT) if TT else pd.DataFrame()), XX, dict(giris=giris, cikis=cikis, stop=stop, hedef=hedef, sure=sure, yon=yon, mal=mal, yil=yil)

def satir(ad, o):
    if not o: return f"   {ad:<14} işlem yok"
    return (f"   {ad:<14} {o['n']:4d} işlem  kazanma %{o['kazanma']:.0f}  ort {o['ort']:+.2f}%  R {o['R']:+.2f}  "
            f"kâr faktörü {o['pf']:.2f}  yıllık {o['yillik']:+.1f}%  maks düşüş {o['dd']:.1f}%")

def main():
    a = sys.argv[1:]
    if not a or "--giris" not in a and "--hazir" not in a: print(__doc__); return
    if "--hazir" in a:
        from tarama import HAZIR
        a += ["--giris", HAZIR[arg(a, "--hazir")][1]]
    from tarama import evren
    hedef_ad = a[0]; uni = evren(hedef_ad) if hedef_ad in ("portfoy", "ndx", "hepsi") or "," in hedef_ad else [hedef_ad.upper()]
    T, XX, p = calistir(uni, a)
    print(f"== BACKTEST {hedef_ad} ({len(uni)} enstrüman, {p['yil']} yıl, {p['yon']}) | giriş [{p['giris']}]" + (f" | çıkış [{p['cikis']}]" if p['cikis'] else "")
          + f" | stop {p['stop']} ATR, hedef {p['hedef']} ATR, en çok {p['sure']} gün, maliyet %{p['mal']}")
    if T.empty: print("   hiç işlem oluşmadı: koşul çok dar"); return
    o = ozet(T, XX, p["yil"])
    tb = [taban(x, 0, p["sure"], p["yon"], p["mal"], stop=p["stop"], hedef=p["hedef"], cikis=p["cikis"]) for x in XX if len(x) > p["sure"] + 30]
    tb_k, tb_o = np.mean([z[0] for z in tb]), np.mean([z[1] for z in tb])
    k = kanit(T.getiri.tolist(), tb_k)
    print("\nSONUÇ" + (f"  (çok hisseli: her işlem sermayenin 1/{min(len(XX), 5)}'i ile)" if len(XX) > 1 else ""))
    print(satir("strateji", o))
    print(f"   taban (rastgele giriş, AYNI stop/hedef/süre kuralları): kazanma %{tb_k:.0f}, ort {tb_o:+.2f}%  -> fark {o['kazanma'] - tb_k:+.0f} puan, beklenti farkı {o['ort'] - tb_o:+.2f}%")
    print(f"   kazanma güven aralığı %{k['alt']:.0f}-{k['ust']:.0f} -> {k['hukum']}")
    print(f"   ortalama {o['gun']:.1f} gün, en iyi {o['en_iyi']:+.1f}%, en kötü {o['en_kotu']:+.1f}%, Sharpe ~{o['sharpe']:.2f}; çıkış nedenleri {o['nedenler']}")
    if len(uni) == 1:
        x = XX[0]; ah = (x.kapanis.iloc[-1] / x.kapanis.iloc[0]) ** (1 / max(p['yil'], .5)) * 100 - 100
        print(f"   al-tut aynı dönemde yıllık {ah:+.1f}%  (piyasada kalma süresi %{T.gun.sum() / len(x) * 100:.0f})")
    else:
        h = T.groupby("t").getiri.agg(["count", "mean"]).sort_values("mean")
        print(f"   hisse bazında: {int((h['mean'] > 0).sum())}/{len(h)} hissede pozitif beklenti; en iyi {', '.join(h.index[-3:][::-1])}; en kötü {', '.join(h.index[:3])}")
    # örnek dışı
    T = T.sort_values("giris_t"); kes = T.giris_t.quantile(.7)
    o1, o2 = ozet(T[T.giris_t <= kes], XX, p["yil"] * .7), ozet(T[T.giris_t > kes], XX, p["yil"] * .3)
    print("\nÖRNEK DIŞI TEST (ilk %70 'öğrenme', son %30 'gerçek hayat')")
    print(satir("ilk %70", o1)); print(satir("son %30", o2))
    bozul = o1 and o2 and (o2["ort"] < 0 < o1["ort"] or o2["kazanma"] < o1["kazanma"] - 12)
    # duyarlılık
    sayilar = list(re.finditer(r"(?<![\w.])(-?\d+(?:\.\d+)?)", p["giris"]))
    if sayilar:
        print("\nPARAMETRE DUYARLILIĞI (girişteki eşikler birlikte oynatılır)")
        sonuclar = []
        for f in (0.8, 0.9, 1.1, 1.2):
            yeni = p["giris"]
            for m in reversed(sayilar):
                v = float(m.group(1)); yv = v * f if abs(v) > 1 else v
                yeni = yeni[:m.start()] + (f"{yv:.2f}".rstrip("0").rstrip(".")) + yeni[m.end():]
            a2 = [z for z in a]; a2[a2.index("--giris") + 1] = yeni
            T2, X2, _ = calistir(uni, a2); o3 = ozet(T2, X2, p["yil"]) if not T2.empty else None
            print(satir(f"eşik x{f}", o3)); sonuclar.append(o3["ort"] if o3 else np.nan)
        kirilgan = np.nanmin(sonuclar) < 0 < o["ort"] if sonuclar else False
    else: kirilgan = False
    # monte carlo
    (dd50, dd5), (s5, s50, s95), zarar = monte_carlo(T.getiri.values, w=(1 / min(len(XX), 5) if len(XX) > 1 else 1))
    print(f"\nMONTE CARLO (2000 senaryo): toplam getiri %5/%50/%95 = {s5:+.0f}% / {s50:+.0f}% / {s95:+.0f}%; "
          f"maks düşüş medyan {dd50:.0f}%, kötü senaryo (%5) {dd5:.0f}%; zararla biten senaryo %{zarar:.0f}")
    # hüküm
    ustun = k["fark"] >= 5 or (o["ort"] - tb_o) >= 0.5
    puan = int(ustun) + (o["pf"] >= 1.3) + (o["n"] >= 30) + (not bozul) + (not kirilgan) + (zarar < 20)
    etiket = "SAĞLAM" if puan >= 6 else "UMUT VERİCİ" if puan >= 4 and ustun else "ZAYIF"
    print(f"\nHÜKÜM: {etiket} ({puan}/6) — tabanı geçiyor mu {'evet' if ustun else 'hayır (rastgele girişten farksız)'}, kâr faktörü ≥1,3 {'evet' if o['pf'] >= 1.3 else 'hayır'}, "
          f"≥30 işlem {'evet' if o['n'] >= 30 else 'hayır'}, örnek dışında {'bozuldu' if bozul else 'dayandı'}, eşiklere {'KIRILGAN' if kirilgan else 'dayanıklı'}, "
          f"Monte Carlo zarar riski %{zarar:.0f}")
    png = arg(a, "--png")
    if png:
        import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(10.8, 6), dpi=100); fig.patch.set_facecolor("#0b0f14"); ax.set_facecolor("#0b0f14")
        eq = (1 + T.sort_values("cikis_t").set_index("cikis_t").getiri / 100).cumprod()
        ax.plot(eq.index, (eq - 1) * 100, color="#35d0a5", lw=2, label="strateji (işlem bazlı bileşik)")
        ax.fill_between(eq.index, 0, (eq / eq.cummax() - 1) * 100, color="#ff5c5c", alpha=.25, label="düşüş")
        ax.axhline(0, color="#445", lw=.8); ax.tick_params(colors="#9aa"); [s.set_color("#223") for s in ax.spines.values()]
        ax.set_title(f"Backtest • {hedef_ad} • {o['n']} işlem • kazanma %{o['kazanma']:.0f} • {etiket}", color="white", loc="left", fontsize=13)
        ax.legend(facecolor="#0b0f14", labelcolor="#ccd", frameon=False, loc="upper left")
        fig.text(.99, .01, "ENES ULUDAĞ", color="#667", ha="right", fontsize=9, weight="bold")
        fig.tight_layout(); fig.savefig(png, facecolor=fig.get_facecolor()); print(f"\ngrafik: {png}")

if __name__ == "__main__":
    main()

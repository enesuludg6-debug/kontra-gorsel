#!/usr/bin/env python3
"""ml.py — makine öğrenmesi laboratuvarı (TrendSpider ML Quant Lab karşılığı, dürüst sürüm).
Kullanım: python3 invest/ml.py <T|evren> [--ufuk 10] [--model orman|lojistik] [--yil 10]
- Özellikler: gosterge.py'nin ~40 sayısal sütunu (oranlara çevrilmiş; fiyat seviyesi yok).
- Hedef: ufuk gün sonra yukarıda mı.
- İLERİYE DÖNÜK (walk-forward) eğitim: her yıl, yalnız o yıldan ÖNCEKİ veriyle eğit, o yılı tahmin et (ufuk kadar boşluk bırakılır).
- Ölçüm: AUC (0,5 = yazı tura), en güvenli %20 tahminin isabeti vs taban oran (kanıt kuralı), yıllara göre istikrar.
- Bugünkü olasılık ve onu en çok etkileyen özellikler. AUC < 0,53 ise modeli KULLANMA diye söyler.
"""
import sys, warnings
import numpy as np, pandas as pd
warnings.filterwarnings("ignore")
from gosterge import veri, hesapla
from veri_kalite import kanit
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_auc_score

OZ = ["rsi", "rsi2", "atr_yuzde", "uz20", "uz50", "uz200", "macd_hist_n", "adx", "dip_plus", "dip_minus", "bb_genislik", "bb_yuzde",
      "supertrend_yon", "stoch_k", "mfi", "obv_egim", "cmf", "hacim_oran", "zirve52", "dip52", "getiri1", "getiri5", "getiri20",
      "getiri60", "getiri120", "rs20", "rs60", "sikisma", "ardisik_dusus", "ardisik_yukselis", "h_rsi", "h_supertrend_yon", "h_trend", "gun_hafta"]

def cerceve(t, ref, yil, ufuk):
    x = hesapla(veri(t, f"{yil}y"), ref)
    x["macd_hist_n"] = x.macd_hist / x.kapanis * 100; x["bb_yuzde"] = (x.kapanis - x.bb_alt) / (x.bb_ust - x.bb_alt + 1e-9)
    x["hedef"] = (x.kapanis.shift(-ufuk) > x.kapanis).astype(float); x.loc[x.index[-ufuk:], "hedef"] = np.nan
    x["t"] = t
    return x.iloc[220:]

def main():
    a = sys.argv[1:]; hedef = a[0] if a else "^NDX"
    ufuk = int(a[a.index("--ufuk") + 1]) if "--ufuk" in a else 10
    tip = a[a.index("--model") + 1] if "--model" in a else "orman"; yil = int(a[a.index("--yil") + 1]) if "--yil" in a else 10
    from tarama import evren
    uni = evren(hedef) if hedef in ("portfoy", "ndx", "hepsi") or "," in hedef else [hedef.upper()]
    ref = veri("QQQ", f"{yil}y")
    P_ = []
    for t in uni:
        try:
            c_ = cerceve(t, ref, yil, ufuk)
            if len(c_) >= 500: P_.append(c_)
            else: print(f"   {t}: geçmiş kısa ({len(c_)} gün), modele alınmadı")
        except Exception as e: print(f"   {t}: atlandı ({str(e)[:50]})")
    X = pd.concat(P_); uni = [t for t in uni if t in set(X.t)]
    oz = [c for c in OZ if c in X.columns]; X[oz] = X[oz].replace([np.inf, -np.inf], np.nan)
    X = X.dropna(subset=oz)
    def model():
        return RandomForestClassifier(300, max_depth=5, min_samples_leaf=50, n_jobs=-1, random_state=1) if tip == "orman" \
            else make_pipeline(StandardScaler(), LogisticRegression(C=0.1, max_iter=500))
    yillar = sorted(set(X.index.year)); tahmin = []
    for y in yillar[3:]:
        egit = X[(X.index < pd.Timestamp(f"{y}-01-01") - pd.Timedelta(days=ufuk * 2)) & X.hedef.notna()]
        test = X[(X.index.year == y) & X.hedef.notna()]
        if len(egit) < 500 or len(test) < 50: continue
        m = model().fit(egit[oz], egit.hedef); p = m.predict_proba(test[oz])[:, 1]
        tahmin.append(pd.DataFrame({"p": p, "y": test.hedef.values, "yil": y, "t": test.t.values}, index=test.index))
    T = pd.concat(tahmin); auc = roc_auc_score(T.y, T.p); tb = T.y.mean() * 100
    ust = T[T.p >= T.p.quantile(.8)]; alt = T[T.p <= T.p.quantile(.2)]
    k1 = kanit([1 if v else -1 for v in ust.y], tb); k2 = kanit([1 if not v else -1 for v in alt.y], 100 - tb)
    print(f"== ML {hedef} ({len(uni)} enstrüman, {tip}, hedef: {ufuk} gün sonra yukarıda mı) | {len(T):,} örnek dışı tahmin, {T.yil.min()}-{T.yil.max()}")
    print(f"   AUC {auc:.3f}  (0,50 yazı tura; 0,55+ işe yarar; 0,60+ güçlü)")
    print(f"   taban oran: %{tb:.0f} yukarı")
    print(f"   modelin EN İYİMSER %20'si: %{k1['oran']:.0f} isabet ({k1['alt']:.0f}-{k1['ust']:.0f}, fark {k1['fark']:+.0f}) -> {k1['hukum'].split(' (')[0]}")
    print(f"   modelin EN KÖTÜMSER %20'si: düşüş isabeti %{k2['oran']:.0f} (taban %{100 - tb:.0f}, fark {k2['fark']:+.0f}) -> {k2['hukum'].split(' (')[0]}")
    yy = T.groupby("yil").apply(lambda z: roc_auc_score(z.y, z.p) if z.y.nunique() > 1 else np.nan)
    print("   yıllara göre AUC: " + "  ".join(f"{y}:{v:.2f}" for y, v in yy.items()) + f"  -> 0,5 üstü yıl {int((yy > .5).sum())}/{yy.notna().sum()}")
    egit = X[X.hedef.notna()]; m = model().fit(egit[oz], egit.hedef)
    print("\nBUGÜN (son kapanış verisiyle):")
    for t in uni[:12]:
        s = X[X.t == t]
        if s.empty: continue
        r = s.iloc[[-1]]; p = m.predict_proba(r[oz])[0, 1]
        print(f"   {t:<6} {ufuk} gün sonra yukarıda olma olasılığı %{p * 100:.0f} (taban %{tb:.0f}, fark {p * 100 - tb:+.0f})")
    if tip == "orman":
        imp = pd.Series(m.feature_importances_, index=oz).sort_values(ascending=False)[:6]
        print("   en etkili özellikler: " + ", ".join(f"{k} ({v * 100:.0f})" for k, v in imp.items()))
    karar = "KULLANILABİLİR (yardımcı kanıt)" if auc >= .55 and (yy > .5).mean() >= .7 else "ZAYIF — tek başına kullanma" if auc >= .52 else "İŞE YARAMIYOR — kullanma"
    print(f"\nHÜKÜM: {karar}")

if __name__ == "__main__":
    main()

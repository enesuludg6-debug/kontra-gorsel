#!/usr/bin/env python3
"""nabiz.py — ÜCRETSİZ piyasa nabzı kaydedici ve okuyucu (Enes 26.11 08:35 "ücretsiz sitelere de bağlanalım").
Shell bu sitelere çıkamaz; değerler WebFetch ile alınır (istem: "sadece sayılar, yorum yok"), bu betik kaydeder ve okur.
KAYNAKLAR (hepsi ücretsiz, test edildi 26.11):
  korku_acgozluluk  https://production.dataviz.cnn.io/index/fearandgreed/graphdata   (skor 0-100 + 7 alt gösterge)
  cboe_pc           https://www.cboe.com/us/options/market_statistics/daily/         (toplam / hisse / endeks / SPX put-call)
  aaii              https://www.aaii.com/sentimentsurvey                              (bireysel yatırımcı boğa/ayı %, haftalık Perşembe)
  hy_spread         https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2   (yüksek getirili tahvil primi = kredi stresi)
  FRED diğer        ...?id=T10Y2Y (eğri), VIXCLS, DGS10, DFII10 (reel faiz), WALCL (Fed bilanço), RRPONTSYD (ters repo)
  hisse istatistik  https://stockanalysis.com/stocks/<t>/statistics/                 (resmi açığa satış %, kurumsal sahiplik, değerleme)
  opsiyon/karanlık  chartexchange + tapeboard (alt_veri.py)
ÇALIŞMAYANLAR: finviz, openinsider (erişim yok), SEC EDGAR (robots), quiverquant ve NAAIM (veri JS ile yükleniyor).
Kullanım:
  python3 invest/nabiz.py kaydet --fg 17.4 --fg_hafta 29.9 --pc 0.88 --pc_hisse 0.61 --pc_endeks 1.01 --aaii_boga 33.3 --aaii_ayi 42.2 --hy 3.63 [--tarih 2026-11-25]
  python3 invest/nabiz.py oku
"""
import sys, os, json, datetime as dt
import numpy as np

YOL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "alt_veri", "nabiz.json")
ALAN = ["fg", "fg_hafta", "pc", "pc_hisse", "pc_endeks", "aaii_boga", "aaii_ayi", "hy", "t10y2y", "vix"]

def kaydet(a):
    D = json.load(open(YOL)) if os.path.exists(YOL) else []
    t = a[a.index("--tarih") + 1] if "--tarih" in a else dt.date.today().isoformat()
    k = {"tarih": t}
    for f in ALAN:
        if f"--{f}" in a: k[f] = float(a[a.index(f"--{f}") + 1])
    D = [z for z in D if z["tarih"] != t] + [k]; D.sort(key=lambda z: z["tarih"])
    json.dump(D, open(YOL, "w"), indent=1); print(f"nabız kaydedildi {t}: {k}")

def oku():
    D = json.load(open(YOL)) if os.path.exists(YOL) else []
    if not D: print("kayıt yok"); return
    s = D[-1]; puan, satir = [], []
    def son(f): return next((z[f] for z in reversed(D) if f in z), None)
    fg = son("fg")
    if fg is not None:
        satir.append(f"Korku-Açgözlülük {fg:.0f}/100 " + ("AŞIRI KORKU" if fg < 25 else "korku" if fg < 45 else "nötr" if fg <= 55 else "açgözlülük" if fg <= 75 else "AŞIRI AÇGÖZLÜLÜK")
                     + (f" (1 hafta önce {son('fg_hafta'):.0f})" if son("fg_hafta") is not None else "")); puan.append((50 - fg) / 50)
    pc = son("pc_hisse")
    if pc is not None:
        satir.append(f"CBOE hisse put/call {pc:.2f} " + ("(korunma yüksek)" if pc > 0.75 else "(kalabalık call, iyimser)" if pc < 0.5 else "(olağan)")
                     + (f", endeks {son('pc_endeks'):.2f}" if son("pc_endeks") is not None else "")); puan.append(np.clip((pc - 0.62) / 0.2, -1, 1))
    b, y = son("aaii_boga"), son("aaii_ayi")
    if b is not None and y is not None:
        fark = b - y; satir.append(f"AAII boğa %{b:.0f} / ayı %{y:.0f} (fark {fark:+.0f}; tarihsel ort +6)"); puan.append(np.clip(-(fark - 6) / 30, -1, 1))
    hy = son("hy")
    if hy is not None:
        H = [z["hy"] for z in D if "hy" in z]; deg = hy - H[0] if len(H) > 1 else 0
        satir.append(f"Yüksek getirili tahvil primi %{hy:.2f}" + (f" ({len(H)} kayıtta {deg:+.2f})" if len(H) > 1 else "") + (" — kredi stresi var" if hy > 4.5 else " — kredi sakin"))
    print(f"== PİYASA NABZI ({s['tarih']})")
    for z in satir: print("   " + z)
    if puan:
        p = float(np.mean(puan)) * 100
        print(f"   KARŞIT GÖSTERGE: {p:+.0f} (+100 = herkes korkuyor -> tarihsel olarak dip bölgesi; −100 = herkes iyimser -> tepe riski)")
        print("   " + ("Duygu dip bölgesine yakın; fiyat onayı (trend dönüşü) gelirse güçlü bir bağlam olur." if p > 50 else
                     "Duygu aşırı iyimser; yükselişlerde temkin." if p < -50 else "Duygu uç değil."))
    print(f"   ({len(D)} gün kayıt; 30+ gün olunca 10/20 gün sonrası kanıtı taban oranla ölçülecek)")

if __name__ == "__main__":
    a = sys.argv[1:]
    if not a: print(__doc__)
    elif a[0] == "kaydet": kaydet(a)
    else: oku()

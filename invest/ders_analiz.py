#!/usr/bin/env python3
"""DERS ANALIZI (kesin kural 26). Goruntulenmelerden ders cikarmanin tek yolu bu script; elle "bence su iyi gitti" yok.

Veri: invest/performans_veri.csv (her tweet bir satir; sabah 09:00 gorevi metrikleri 24-48 saat sonra yazar/gunceller).
  sutunlar: tarih,saat,kaynak(sistem|enes),tur,gorus(evet|hayir|?),konu,duzen,buffer_id,gorunt,begeni,yanit,repost,er,olcum
  tur sonunda * = otomatik tahmin edilmis tur (guven dusuk).

Kullanim:
  python3 ders_analiz.py                 # son 28 gun, sistem tweetleri
  python3 ders_analiz.py --gun 14 --hepsi  # enes tweetleri dahil
  python3 ders_analiz.py --test "saat:18-21" # tek bir boyut/deger icin ders testi (ESIK kontrolu)

Yontem:
  - GORELI SKOR = tweet goruntulenmesi / o gunden onceki 7 gunun (tum tweetler) medyani. Hesap buyudukce ham sayi artar;
    goreli skor buyumeyi ve gunun piyasa havasini temizler. 1,00 = normal; 1,30 = %30 ustu.
  - Grup degeri MEDYAN goreli skor (tek viral tweet grubu tasimasin). Ayrica etkilesim % medyani.
  - DERS ESIGI (hepsi saglanmali): grupta >= 8 tweet, >= 2 farkli takvim haftasi, medyan farki >= %25 (1,25x ya da 0,80x),
    her iki haftada da ayni yon (tutarlilik). Saglanmazsa yalniz GOZLEM.
  - Karistirici kontrolu: tur karsilastirmasi ayni saat diliminde de bakilir (--test cikti satiri 'ayni dilimde').
"""
import csv, sys, statistics as st, datetime as dt, collections, os
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "performans_veri.csv")
DILIM = lambda h: f"{(h//3)*3:02d}-{(h//3)*3+3:02d}"

def yukle(gun, hepsi):
    R = [r for r in csv.DictReader(open(P, encoding="utf-8")) if r["gorunt"] not in ("", None)]
    def olgun(r):  # metrik en az 12 saatlik olmali (Buffer ~24 saat gecikmeli); olcum UTC
        try:
            o = dt.datetime.fromisoformat(r["olcum"][:16]) + dt.timedelta(hours=3)
            return (o - dt.datetime.fromisoformat(r["tarih"] + "T" + r["saat"])).total_seconds() >= 12 * 3600
        except Exception: return True
    R = [r for r in R if olgun(r)]
    for r in R:
        r["t"] = dt.date.fromisoformat(r["tarih"]); r["g"] = float(r["gorunt"]); r["er"] = float(r["er"] or 0)
        r["dilim"] = DILIM(int(r["saat"][:2])); r["hafta"] = r["t"].isocalendar()[1]; r["tur_"] = r["tur"].rstrip("*")
    R.sort(key=lambda r: (r["tarih"], r["saat"]))
    # goreli skor: onceki 7 gun medyani (yoksa ayni gun dahil ilk gunlerin medyani)
    for r in R:
        ref = [x["g"] for x in R if r["t"] - dt.timedelta(days=7) <= x["t"] < r["t"] and x["g"] > 0]
        if len(ref) < 10: ref = [x["g"] for x in R if x["t"] <= r["t"] and x["g"] > 0]
        r["skor"] = r["g"] / (st.median(ref) or 1)
    son = max(r["t"] for r in R) - dt.timedelta(days=gun)
    return [r for r in R if r["t"] > son and (hepsi or r["kaynak"] == "sistem")]

def grup(R, alan):
    G = collections.defaultdict(list)
    for r in R: G[r[alan]].append(r)
    return G

def ozet(v):
    hf = grup(v, "hafta"); yon = {h: st.median(x["skor"] for x in xs) for h, xs in hf.items() if len(xs) >= 3}
    return len(v), st.median(x["skor"] for x in v), st.median(x["er"] for x in v), len(hf), yon

def esik(n, med, hafta_sayi, yon):
    if n < 8 or hafta_sayi < 2: return "GOZLEM (az veri)"
    if 0.80 < med < 1.25: return "FARK YOK"
    tutarli = all((y >= 1) == (med >= 1) for y in yon.values()) and len(yon) >= 2
    return ("DERS ADAYI (esik saglandi)" if tutarli else "CELISKILI (haftalar farkli yon)")

def main(a):
    gun = int(a[a.index("--gun")+1]) if "--gun" in a else 28; hepsi = "--hepsi" in a
    R = yukle(gun, hepsi)
    print(f"DERS ANALIZI: {len(R)} tweet, son {gun} gun, {'tum' if hepsi else 'sistem'} | genel medyan goruntulenme {st.median(r['g'] for r in R):.0f}")
    if "--test" in a:
        alan, deger = a[a.index("--test")+1].split(":", 1); alan = {"tur": "tur_"}.get(alan, alan)
        ic = [r for r in R if r[alan] == deger]; dis = [r for r in R if r[alan] != deger]
        n, med, er, hs, yon = ozet(ic) if ic else (0, 1, 0, 0, {})
        print(f"{alan}={deger}: n={n} goreli medyan={med:.2f} ER={er:.2f} hafta={hs} haftalik={ {k: round(v,2) for k,v in yon.items()} } -> {esik(n, med, hs, yon)}")
        if alan == "tur_":
            for d, xs in sorted(grup(ic, "dilim").items()):
                ayni = [r for r in dis if r["dilim"] == d]
                if len(xs) >= 3 and len(ayni) >= 3:
                    print(f"   ayni dilimde {d}: {st.median(x['skor'] for x in xs):.2f} vs digerleri {st.median(x['skor'] for x in ayni):.2f}")
        return
    for alan in ("tur_", "dilim", "gorus", "duzen", "kaynak"):
        print(f"\n[{alan}]")
        for k, v in sorted(grup(R, alan).items(), key=lambda kv: -st.median(x["skor"] for x in kv[1])):
            if not k: continue
            n, med, er, hs, yon = ozet(v)
            print(f"  {k:12} n={n:3} goreli={med:4.2f} ER={er:4.2f} hafta={hs} -> {esik(n, med, hs, yon)}")
    top = sorted(R, key=lambda r: -r["skor"])[:5]; bot = sorted(R, key=lambda r: r["skor"])[:5]
    print("\nEN IYI 5:", *[f"\n  {r['tarih']} {r['saat']} {r['tur']} {r['skor']:.2f} {r['konu'][:50]}" for r in top])
    print("EN KOTU 5:", *[f"\n  {r['tarih']} {r['saat']} {r['tur']} {r['skor']:.2f} {r['konu'][:50]}" for r in bot])

if __name__ == "__main__": main(sys.argv[1:])

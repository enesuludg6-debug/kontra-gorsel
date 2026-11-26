#!/usr/bin/env python3
"""alt_veri.py — opsiyon ve karanlık havuz verisi (Enes 26.11 08:21 "eksikleri çöz").
Shell yalnız Yahoo'ya çıkabildiği için veri WebFetch ile alınır, bu betik KAYDEDER ve ANALİZ eder; geçmiş biriktikçe kanıt ölçülür.

KAYNAKLAR (WebFetch ile; istem: "CSV olarak ver, yorum yok"):
  OPSİYON  https://chartexchange.com/symbol/nasdaq-<t>/optionchain/summary/   (NYSE hissesi: nyse-<t>)
           -> vade, call OI, put OI, put/call, max pain
  KARANLIK https://chartexchange.com/symbol/nasdaq-<t>/stats/                 -> bugünkü borsa dışı (dark pool + OTC) hacim %, 30 gün ort %
           https://chartexchange.com/symbol/nasdaq-<t>/short-volume/          -> FINRA günlük kısa satış hacmi %
           https://tapeboard.com/dark-pool/<T>                                -> FINRA haftalık ATS (dark pool) hacmi, 4 hafta değişim, en büyük havuzlar
           https://cdn.finra.org/equity/regsho/daily/CNMSshvol<YYYYMMDD>.txt  -> resmi FINRA dosyası (büyük; offset ile)
  ÖDÜNÇ    https://chartexchange.com/symbol/nasdaq-<t>/borrow-fee/            -> ödünç ücreti, kullanılabilir hisse

Kullanım:
  python3 invest/alt_veri.py opsiyon <T> <fiyat> < opsiyon.csv      (başlık: expiration,call_open_interest,put_open_interest,...,put_call_ratio,max_pain)
  python3 invest/alt_veri.py karanlik <T> --offex 44.5 --offex30 46.1 [--kisa 19.8] [--ats_degisim -39.8] [--odunc 0.28]
  python3 invest/alt_veri.py analiz <T>
"""
import sys, os, io, json, datetime as dt
import pandas as pd, numpy as np

KLAS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "alt_veri"); os.makedirs(KLAS, exist_ok=True)
def yol(t): return os.path.join(KLAS, f"{t.upper().replace('^', '')}.json")
def oku(t): return json.load(open(yol(t))) if os.path.exists(yol(t)) else {"opsiyon": [], "karanlik": []}
def yaz(t, D): json.dump(D, open(yol(t), "w"), ensure_ascii=False, indent=1)
def arg(a, k, tip=float):
    return tip(a[a.index(k) + 1]) if k in a else None

def opsiyon(t, fiyat, csv):
    df = pd.read_csv(io.StringIO(csv)); df = df[df.expiration.astype(str).str.match(r"\d{4}-\d{2}-\d{2}")]
    for c in ("call_open_interest", "put_open_interest", "max_pain"): df[c] = pd.to_numeric(df[c], errors="coerce")
    bugun = dt.date.today().isoformat(); D = oku(t)
    kayit = {"tarih": bugun, "fiyat": fiyat, "toplam_call": int(df.call_open_interest.sum()), "toplam_put": int(df.put_open_interest.sum()),
             "vadeler": df[["expiration", "call_open_interest", "put_open_interest", "max_pain"]].to_dict("records")}
    D["opsiyon"] = [k for k in D["opsiyon"] if k["tarih"] != bugun] + [kayit]; yaz(t, D); print(f"opsiyon kaydedildi: {t} {bugun}, {len(df)} vade")

def karanlik(t, a):
    bugun = dt.date.today().isoformat(); D = oku(t)
    k = {"tarih": bugun, "offex": arg(a, "--offex"), "offex30": arg(a, "--offex30"), "kisa": arg(a, "--kisa"),
         "ats_degisim": arg(a, "--ats_degisim"), "odunc": arg(a, "--odunc")}
    D["karanlik"] = [z for z in D["karanlik"] if z["tarih"] != bugun] + [k]; yaz(t, D); print(f"karanlık havuz kaydedildi: {t} {bugun}")

def analiz(t):
    D = oku(t); print(f"== ALTERNATİF VERİ {t}")
    if D["opsiyon"]:
        o = D["opsiyon"][-1]; f = o["fiyat"]; V = pd.DataFrame(o["vadeler"]); V["exp"] = pd.to_datetime(V.expiration)
        pc = o["toplam_put"] / max(1, o["toplam_call"])
        print(f"OPSİYON ({o['tarih']}): toplam açık pozisyon put/call {pc:.2f} " +
              ("(korunma ağırlıklı)" if pc > 1.2 else "(call ağırlıklı, iyimser konumlanma)" if pc < 0.7 else "(dengeli)"))
        ay = V[V.exp.dt.day.between(15, 21) & (V.exp.dt.weekday == 4)].sort_values("exp")
        yak = V[V.exp >= pd.Timestamp(o["tarih"])].sort_values("exp")
        for ad, r in (("en yakın vade", yak.iloc[0] if len(yak) else None), ("en yakın aylık vade", ay[ay.exp >= pd.Timestamp(o["tarih"])].iloc[0] if len(ay[ay.exp >= pd.Timestamp(o['tarih'])]) else None)):
            if r is None: continue
            print(f"   {ad} {r.expiration}: max pain {r.max_pain:,.2f} (fiyata {(r.max_pain / f - 1) * 100:+.1f}%), put/call OI {r.put_open_interest / max(1, r.call_open_interest):.2f}, "
                  f"açık pozisyon {int(r.call_open_interest + r.put_open_interest):,}")
        en = V.assign(oi=V.call_open_interest + V.put_open_interest).sort_values("oi", ascending=False).iloc[0]
        print(f"   en büyük açık pozisyon {en.expiration} ({int(en.oi):,} kontrat, put/call {en.put_open_interest / max(1, en.call_open_interest):.2f}, max pain {en.max_pain:,.2f})")
        if len(D["opsiyon"]) >= 2:
            p0 = D["opsiyon"][-2]; pc0 = p0["toplam_put"] / max(1, p0["toplam_call"])
            print(f"   önceki kayda ({p0['tarih']}) göre put/call {pc0:.2f} -> {pc:.2f} ({'korunma artıyor' if pc > pc0 + .03 else 'korunma azalıyor' if pc < pc0 - .03 else 'değişmedi'})")
        print("   not: max pain vadeye yakın günlerde mıknatıs etkisi gösterebilir; tek başına yön sinyali değildir. Geçmiş kayıt birikince kanıt ölçülecek.")
    else: print("OPSİYON: kayıt yok (WebFetch: chartexchange optionchain/summary)")
    if D["karanlik"]:
        k = D["karanlik"][-1]; print(f"KARANLIK HAVUZ / BORSA DIŞI ({k['tarih']}):")
        if k["offex"] is not None:
            fark = k["offex"] - (k["offex30"] or k["offex"])
            print(f"   borsa dışı hacim %{k['offex']:.1f} (30 gün ort %{k['offex30']:.1f}, fark {fark:+.1f} puan) -> "
                  + ("kurumsal blok/dark pool ilgisi ARTTI" if fark > 5 else "ortalamanın altında" if fark < -5 else "olağan"))
        if k["kisa"] is not None:
            H = [z["kisa"] for z in D["karanlik"][:-1] if z.get("kisa") is not None]
            ek = f", geçmiş {len(H)} kayıt ort %{np.mean(H):.1f}" if H else ""
            print(f"   FINRA kısa satış hacmi payı %{k['kisa']:.1f}{ek} (DIX mantığı: borsa dışı kısa hacim piyasa yapıcı ALIMINI yansıtır; yüksek pay = alım baskısı, düşük = satış)")
        if k["ats_degisim"] is not None: print(f"   haftalık dark pool (ATS) hacmi 4 haftada {k['ats_degisim']:+.1f}%")
        if k["odunc"] is not None: print(f"   ödünç ücreti %{k['odunc']:.2f} " + ("(açığa satış pahalı, sıkışma riski)" if k["odunc"] > 5 else "(kolay ödünç, açığa satış ucuz)"))
    else: print("KARANLIK HAVUZ: kayıt yok (WebFetch: chartexchange stats / short-volume, tapeboard)")

if __name__ == "__main__":
    a = sys.argv[1:]
    if not a: print(__doc__); sys.exit()
    if a[0] == "opsiyon": opsiyon(a[1], float(a[2]), sys.stdin.read())
    elif a[0] == "karanlik": karanlik(a[1], a)
    elif a[0] == "analiz": analiz(a[1])

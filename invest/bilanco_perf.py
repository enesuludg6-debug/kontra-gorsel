#!/usr/bin/env python3
"""KURAL 70 (F-002, Enes 24.11 09:53): bilanço tweetlerinin TÜRE göre performansı ve 6 hakkın dağılımı.

Kullanım: python3 invest/bilanco_perf.py [--gun 30]
- performans_veri.csv'deki olgun (gorunt dolu) bilanço tweetlerini 6 türe ayırır:
  BEKLENTI, RAKAM, ANALIZ, DETAY, CAGRI, HAREKET (beklenen hareket / opsiyon).
- Göreli = tweetin görüntülenmesi / o günün tüm olgun tweet medyanı.
- Her tür için n, göreli medyan; ve kural 70 dağılım önerisi.
Yeni bilanço tweetlerinin `tur` alanı şu etiketlerle kaydedilir: BILANCO-BEKLENTI, BILANCO-RAKAM,
BILANCO-ANALIZ, BILANCO-DETAY, BILANCO-CAGRI, BILANCO-HAREKET.
"""
import csv, os, sys, statistics as st, collections, datetime as dt
D = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(D, "performans_veri.csv")
gun = 30
if "--gun" in sys.argv: gun = int(sys.argv[sys.argv.index("--gun") + 1])

def tur6(t):
    u = (t or "").upper().replace("*", "")
    if "BEKLENTI" in u: return "BEKLENTI"
    if "RAKAM" in u: return "RAKAM"
    if "DETAY" in u: return "DETAY"
    if "CAGRI" in u or "ÇAĞRI" in u or "GORUSME" in u: return "CAGRI"
    if "HAREKET" in u or "OPSIYON" in u or "BEKLENEN" in u: return "HAREKET"
    if "BILANCO-ANALIZ" in u or u == "BILANCO-ANALIZ": return "ANALIZ"
    return None

rows = [r for r in csv.DictReader(open(P, encoding="utf-8")) if (r.get("gorunt") or "").strip()]
sinir = (dt.date.today() - dt.timedelta(days=gun)).isoformat()
rows = [r for r in rows if r["tarih"] >= sinir]
gm = collections.defaultdict(list)
for r in rows:
    try: gm[r["tarih"]].append(float(r["gorunt"]))
    except ValueError: pass
med = {k: st.median(v) for k, v in gm.items() if v}
g = collections.defaultdict(list)
for r in rows:
    k = tur6(r.get("tur"))
    if not k or not med.get(r["tarih"]): continue
    try: g[k].append(float(r["gorunt"]) / med[r["tarih"]])
    except ValueError: pass
print(f"BILANCO TUR PERFORMANSI (son {gun} gun, goreli = gun medyanina oran)")
sira = sorted(g.items(), key=lambda kv: -st.median(kv[1]))
for k, v in sira:
    print(f"  {k:9s} n={len(v):3d} goreli_medyan={st.median(v):.2f}")
eksik = [k for k in ["BEKLENTI", "RAKAM", "ANALIZ", "DETAY", "CAGRI", "HAREKET"] if k not in g]
if eksik: print("  veri yok:", ", ".join(eksik))
yeter = [k for k, v in g.items() if len(v) >= 3]
print("ONERI (kural 70):", end=" ")
if len(yeter) < 3:
    print("veri az (tur basina en az 3 olgun tweet gerek); varsayilan dagilim: BEKLENTI 1, RAKAM 1, ANALIZ 1, DETAY 2, CAGRI/HAREKET 1")
else:
    iyi = [k for k, v in sira if len(v) >= 3]
    print(f"guclu={iyi[0]} zayif={iyi[-1]} -> zayif turun 1 hakkini guclu ture kaydir (BEKLENTI/RAKAM/ANALIZ en az 1 kalir)")

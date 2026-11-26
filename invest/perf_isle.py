#!/usr/bin/env python3
"""PERFORMANS ISLEME (kural 26 + 57). Buffer list_posts (includeMetrics) dokumunu performans_veri.csv'ye isler.

Kullanim:
  python3 invest/perf_isle.py <dokum_dosyasi> [<dokum2> ...]
    dokum: Buffer MCP list_posts ciktisi (cok buyukse arac /tmp/claude-tool-results/... dosyasina kaydeder; o yol verilir)
           ya da ayni JSON'u iceren herhangi bir dosya ([{type,text}] dizisi ya da dogrudan {"edges":[...]}).
  python3 invest/perf_isle.py --ozet [--gun 7]   # olgun (>=24 saat) metriklerle hizli ozet: saat dilimi, tur, uzunluk, gorsel, portfoy

Yaptigi:
  - buffer_id eslesen satirin gorunt/begeni/yanit/repost/er/olcum sutunlarini gunceller (yalniz metricsUpdatedAt gonderimden >= 12 saat sonraysa;
    >= 24 saat sonraysa: Buffer metrikleri ~24 saat gecikmeli; erken olcum 0 gorunur ve dersleri bozar).
  - CSV'de olmayan gonderileri ekler: via=network ise kaynak=enes (Enes'in elle attigi), degilse sistem; tur tahmini '*' ile.
  - Ciktinin sonunda 'SONRAKI OLCUM' satiri: metrigi henuz olgunlasmamis en eski gonderinin olgunlasacagi zaman.
"""
import csv, json, sys, os, datetime as dt, statistics as st, collections, re
D = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(D, "performans_veri.csv")
ALAN = ["tarih","saat","kaynak","tur","gorus","konu","duzen","buffer_id","gorunt","begeni","yanit","repost","er","olcum"]
PORT = ["DOCN","RKLB","Rocket Lab","SITM","SiTime","AXON","Axon","CBRS","Cerebras","VRT","Vertiv","AVGO","Broadcom"]

def tur_tahmin(t):
    l = t.lower()
    if "13f" in l: return "13F*"
    if "beklenti" in l and ("açıklıyor" in l or "açıklayacak" in l): return "BEKLENTI*"
    if "çeyre" in l or "bilanço" in l: return "BILANCO*"
    if "grafi" in l or "destek" in l or "direnç" in l: return "TEKNIK*"
    if "portföy güncellemesi" in l: return "PORTFOY*"
    if "kapan" in l and ("nasdaq" in l or "s&p" in l): return "KAPANIS*"
    return "HABER*"

def oku_dokum(yol):
    raw = open(yol, encoding="utf-8").read()
    try:
        j = json.loads(raw)
        if isinstance(j, list) and j and isinstance(j[0], dict) and "text" in j[0]: raw = j[0]["text"]
        elif isinstance(j, dict): return j.get("edges", [])
    except Exception: pass
    d = json.JSONDecoder().raw_decode(raw[raw.find("{"):])[0]
    return d.get("edges", [])

def zaman(s): return dt.datetime.fromisoformat(s.replace("Z", "+00:00"))

def isle(yollar):
    R = list(csv.DictReader(open(P, encoding="utf-8")))
    for r in R:  # bozuk satır koruması: fazla alan varsa konu'ya ekle, yazımı çökertmesin
        fazla = r.pop(None, None)
        if fazla: r["konu"] = (r.get("konu") or "") + " " + " ".join(fazla)
    idx = {r["buffer_id"]: r for r in R if r.get("buffer_id")}
    guncel = yeni = bekleyen = 0; en_erken = None
    for y in yollar:
        for e in oku_dokum(y):
            p = e.get("node", e)
            if p.get("status") != "sent": continue
            m = {x["type"]: x["value"] for x in (p.get("metrics") or [])}
            gond = zaman(p.get("sentAt") or p["dueAt"]); upd = p.get("metricsUpdatedAt")
            olgun = bool(upd) and (zaman(upd) - gond).total_seconds() >= 12 * 3600
            if not olgun:
                bekleyen += 1; t = gond + dt.timedelta(hours=14)
                en_erken = t if en_erken is None or t < en_erken else en_erken
            tsi = gond + dt.timedelta(hours=3)
            r = idx.get(p["id"])
            if r is None:
                r = {k: "" for k in ALAN}
                r.update(tarih=tsi.strftime("%Y-%m-%d"), saat=tsi.strftime("%H:%M"),
                         kaynak="enes" if p.get("via") == "network" else "sistem", tur=tur_tahmin(p["text"]), gorus="?",
                         konu=p["text"].replace("\n", " ")[:60], buffer_id=p["id"])
                R.append(r); idx[p["id"]] = r; yeni += 1
            if olgun:
                r.update(gorunt=str(m.get("impressions", 0)), begeni=str(m.get("reactions", 0)), yanit=str(m.get("comments", 0)),
                         repost=str(m.get("reposts", 0)), er=str(m.get("engagementRate", 0)), olcum=upd[:16])
                guncel += 1
    R.sort(key=lambda r: (r["tarih"], r["saat"]))
    with open(P, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=ALAN); w.writeheader(); w.writerows(R)
    print(f"guncellenen(olgun) {guncel} | yeni satir {yeni} | olgunlasmamis {bekleyen}")
    if en_erken:
        print("SONRAKI OLCUM (en erken olgunlasma, TSI): " + (en_erken + dt.timedelta(hours=3)).strftime("%Y-%m-%d %H:%M"))

def ozet(gun):
    R = [r for r in csv.DictReader(open(P, encoding="utf-8")) if r["gorunt"] not in ("", None)]
    son = dt.date.today() - dt.timedelta(days=gun)
    R = [r for r in R if dt.date.fromisoformat(r["tarih"]) >= son]
    if not R: print("veri yok"); return
    g = lambda S: (len(S), round(st.median([float(r["gorunt"]) for r in S])) if S else 0)
    print(f"OLGUN TWEET {len(R)} | medyan gorunt {g(R)[1]}")
    def grup(ad, f):
        b = collections.defaultdict(list)
        for r in R: b[f(r)].append(r)
        print(ad + ": " + " | ".join(f"{k} n={g(v)[0]} med={g(v)[1]}" for k, v in sorted(b.items())))
    grup("saat", lambda r: f"{(int(r['saat'][:2])//3)*3:02d}-{(int(r['saat'][:2])//3)*3+3:02d}")
    grup("kaynak", lambda r: r["kaynak"])
    grup("tur", lambda r: r["tur"].rstrip("*").lower())
    grup("portfoy", lambda r: "evet" if any(p in r["konu"] for p in PORT) else "hayir")
    en = sorted(R, key=lambda r: -float(r["gorunt"]))[:5]
    print("EN IYI 5: " + " || ".join(f"{r['tarih'][5:]} {r['saat']} {r['gorunt']} {r['konu'][:40]}" for r in en))

if __name__ == "__main__":
    a = sys.argv[1:]
    if not a: print(__doc__); sys.exit(0)
    if a[0] == "--ozet": ozet(int(a[a.index("--gun") + 1]) if "--gun" in a else 7)
    else: isle(a)

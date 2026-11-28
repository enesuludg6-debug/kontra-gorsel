#!/usr/bin/env python3
"""gun_ozet.py — kural 99 (27.11, Claude Academy 'tekrar eden talimat skill'e, durum dosyaya'): turun ihtiyaç duyduğu
günlük sayaçları kayıtlardan HESAPLAR; tur mesajına sayaç/liste yazmaya gerek kalmaz.
Kaynaklar: performans_veri.csv (sistem tweetleri), kalite_defteri.json (kalıp, yapı imzası), DONGU.md (ENES-TASLAK, biçim).
Gün penceresi 02:00-02:00 TSİ. Kullanım: python3 invest/gun_ozet.py
"""
import csv, json, os, re, datetime as dt
D = os.path.dirname(os.path.abspath(__file__))
n = dt.datetime.now(dt.timezone(dt.timedelta(hours=3))); g = n - dt.timedelta(hours=2); gun = g.date()
haftasonu = gun.weekday() >= 5; pazar = gun.weekday() == 6
def bugun(t, s):
    d = dt.date.fromisoformat(t); h = int(s[:2])
    return (d == gun and h >= 2) or (d == gun + dt.timedelta(days=1) and h < 2)
R = [r for r in csv.DictReader(open(os.path.join(D, "performans_veri.csv"), encoding="utf-8"))
     if r.get("tarih") and r.get("saat") and r.get("kaynak") == "sistem" and bugun(r["tarih"], r["saat"])]
R.sort(key=lambda r: (r["tarih"], r["saat"]))
K = [k for k in json.load(open(os.path.join(D, "kalite_defteri.json"))) if k.get("gun") == gun.strftime("%d.%m")]
gg = gun.strftime("%d.%m"); dongu = [l for l in open(os.path.join(D, "DONGU.md"), encoding="utf-8") if f"({gg})" in l]
taslak = len({re.search(r"\d\d:\d\d", l).group() for l in dongu if "ENES-TASLAK" in l and re.search(r"\d\d:\d\d", l)})
kon = " ".join(r["konu"] for r in R).upper()
acik = sum(1 for r in R if "AÇIKLAYICI" in r["konu"].upper() or "ACIKLAYICI" in r["konu"].upper())
egit = sum(1 for r in R if r["tur"].upper().startswith("EGITICI"))
tar = sum(1 for r in R if r["tur"].upper().startswith("TARIHSEL"))
ta_stil = sum(1 for r in R if "TA-STİL" in r["konu"].upper() or "TA-STIL" in r["konu"].upper())  # kural 110: en az 2
temel = sum(1 for r in R if "K107" in r["konu"].upper())  # kural 110: favori 4 hesap fikri, en az 1
patlama = sum(1 for r in R if "K111" in r["konu"].upper())  # kural 111-Y: yabancı patlayan tweet uyarlaması, en az 2
kartsiz = sum(1 for r in R if not r["duzen"] or r["duzen"] in ("yok", "kartsiz"))
gorus = sum(1 for l in dongu if "biçim: görüş" in l or "bicim: gorus" in l)
ust = 8 if haftasonu else 20; alt = 0 if haftasonu else 15
ts_hedef = 2 if pazar else 3 if haftasonu else 6
print(f"GÜN {gg} ({'hafta sonu' if haftasonu else 'hafta içi'}) | sistem tweeti {len(R)} (hedef {alt}-{ust}{', ÜST SINIR DOLDU' if len(R) >= ust else ''})")
print(f"  KURAL 110: TA-STİL {ta_stil}/2+ | TEMEL-FİKİR (K107) {temel}/1+ | PATLAMA (K111) {patlama}/2+{'  <- EKSİK' if ta_stil < 2 or temel < 1 or patlama < 2 else ''}")
print(f"  AÇIKLAYICI {acik}/{0 if haftasonu else 5}{'(hafta sonu 2)' if haftasonu else ''} | ENES-TASLAK {taslak}/{ts_hedef} | EGITICI {egit}/1 | TARIHSEL {tar}/1-2 | kartsız {kartsiz}/3 | tartışma görüşü {gorus}/2")
if R:
    s = R[-1]; st = dt.datetime.fromisoformat(f"{s['tarih']}T{s['saat']}").replace(tzinfo=n.tzinfo)
    en_erken = st + dt.timedelta(minutes=35); fark = int((n - st).total_seconds() // 60)
    print(f"  son sistem tweeti {s['saat']} ({fark} dk önce) -> en erken sonraki {en_erken.strftime('%H:%M')}{'  ŞİMDİ UYGUN' if n >= en_erken else '  BEKLE / customScheduled'}")
print("  son 3 düzen: " + ", ".join(r["duzen"] or "kartsız" for r in R[-3:]))
print("  son 4 kalıp: " + ", ".join(k.get("kalip", "?") for k in K[-4:]) + " | son 3 yapı imzası: " + ", ".join(k.get("imza", "?") for k in K[-3:]))
sira = len(R) + 1
print(f"  sıradaki tweet {sira}. -> kural 79 {'iddia açılışı' if sira % 2 == 0 else 'normal açılış'}")
print("  bugün işlenen konular (tekrar etme):")
for r in R: print(f"    {r['saat']} {r['tur']:<12} {r['konu'][:70]}")

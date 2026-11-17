#!/bin/bash
# TUR BASI TEK CAGRI (kesin kural 28, tasarruf). Kurallari DEGISTIRMEZ; tur basinda tek tek yapilan okumalari tek ciktida toplar.
# Kullanim: bash invest/tur_basi.sh [A]   (hesap etiketi, varsayilan A)
cd "$(dirname "$0")" || exit 1
H=${1:-A}
git pull -q --rebase 2>/dev/null || git pull -q
echo "=== KILIT: $(grep -m1 '^AKTIF:' AKTIF_HESAP.md) (bu gorev HESAP=$H)"
grep -qE "^AKTIF: $H[[:space:]]*$" AKTIF_HESAP.md || { echo "!!! AKTIF $H DEGIL -> HICBIR SEY YAPMA, GOREVI KAPAT"; exit 2; }
tail -n 40 DONGU.md | grep -q '^DURDUR' && { echo "!!! DURDUR VAR -> DUR"; exit 3; }
echo "=== SAAT (TSI): $(TZ=Europe/Istanbul date '+%d.%m %a %H:%M')"
echo "=== DURUM.md"; cat DURUM.md
echo "=== DONGU son 30"; tail -n 30 DONGU.md | cut -c1-400
echo "=== SON OTOMATIK/ENES PAYLASIM"; grep -E '^- [0-9]{2}:[0-9]{2} \([0-9.]+\) (AUTO|ENES-ISTEGI)' DONGU.md | tail -n 3 | cut -c1-120
echo "=== DERSLER (aktif + operasyon basliklari)"; sed -n '/^## AKTİF DERSLER/,/^## Gözlemler/p' DERSLER.md | grep -E '^(D|O)-0' | cut -c1-140
echo "=== BUGUN SISTEM TWEETI (kural 42)"; python3 - <<'P'
import csv,datetime as dt
n=dt.datetime.now(dt.timezone(dt.timedelta(hours=3))); g=n-dt.timedelta(hours=2)
b=g.strftime("%Y-%m-%d")
R=[r for r in csv.DictReader(open("performans_veri.csv",encoding="utf-8")) if (r["tarih"]==b and int(r["saat"][:2])>=2) or (r["tarih"]==(g+dt.timedelta(days=1)).strftime("%Y-%m-%d") and int(r["saat"][:2])<2)]
pazar=g.weekday()==6; alt=0 if pazar else 30
son=(g.replace(hour=0,minute=0,second=0)+dt.timedelta(days=1,hours=2)); kalan_dk=max(0,int((son-n).total_seconds()//60))
eksik=max(0,alt-len(R)); tempo=(kalan_dk//eksik) if eksik else None
ak=sum(1 for r in R if 18<=int(r["saat"][:2])<21)
print(f"  bugun {len(R)} tweet | hedef {'Pazar: ust 40' if pazar else '30-40'} | kalan sure {kalan_dk} dk | {'ortalama gereken ~'+str(tempo)+' dk (aralik serbest)' if tempo else 'alt sinir tamam'}")
P
echo "=== IS DEFTERI (kural 43)"; python3 isler.py kontrol; python3 isler.py liste 2>/dev/null | head -8
echo "=== OPSIYON KONTROL (kural 39)"; python3 - <<'P'
import re,datetime as dt
n=dt.datetime.now(dt.timezone(dt.timedelta(hours=3)))
gun=[(n+dt.timedelta(days=k)).strftime("%d.%m") for k in (0,1)]
dongu=open("DONGU.md",encoding="utf-8").read()
for l in open("takvim.md",encoding="utf-8"):
    if l.startswith("|") and any(l[1:].strip().startswith(g) for g in gun) and "bilanço" in l:
        m=re.search(r"\(([A-Z]{1,5})\)",l)
        if m and not re.search(r"OPSIYON: "+m.group(1)+r"\b",dongu) and not re.search(r"\(BILANCO[^\n]*\b"+m.group(1)+r"\b",dongu): print("  EKSIK OPSIYON:",m.group(1),"->",l.split("|")[1].strip())
P
echo "=== CAGRI KONTROL (kural 40)"; python3 - <<'P'
import re,datetime as dt
n=dt.datetime.now(dt.timezone(dt.timedelta(hours=3)))
gun=[(n+dt.timedelta(days=k)).strftime("%d.%m") for k in (-1,0)]
dongu=open("DONGU.md",encoding="utf-8").read()
for l in open("takvim.md",encoding="utf-8"):
    if l.startswith("|") and any(l[1:].strip().startswith(g) for g in gun) and "bilanço" in l:
        m=re.search(r"\(([A-Z]{1,5})\)",l)
        if m and not re.search(r"CAGRI: "+m.group(1)+r"\b",dongu): print("  EKSIK CAGRI:",m.group(1),"->",l.split("|")[1].strip())
P
echo "=== DETAY KONTROL (kural 41)"; python3 - <<'P'
import re,datetime as dt
n=dt.datetime.now(dt.timezone(dt.timedelta(hours=3)))
gun=[(n+dt.timedelta(days=k)).strftime("%d.%m") for k in (-1,0)]
dongu=open("DONGU.md",encoding="utf-8").read()
for l in open("takvim.md",encoding="utf-8"):
    if l.startswith("|") and any(l[1:].strip().startswith(g) for g in gun) and "bilanço" in l:
        m=re.search(r"\(([A-Z]{1,5})\)",l)
        if m and len(re.findall(r"DETAY: "+m.group(1)+r"\b",dongu))<2: print("  EKSIK DETAY:",m.group(1),"->",l.split("|")[1].strip())
P
echo "=== PERIYOT"; python3 periyot.py durum | grep -E 'YAPILMALI|BEKLE' | head -n 12
echo "=== TAKVIM (bugun/yarin)"; D1=$(TZ=Europe/Istanbul date +%d.%m); D2=$(TZ=Europe/Istanbul date -d tomorrow +%d.%m); grep -E "$D1|$D2" takvim.md | head -n 15 | cut -c1-200
echo "=== GUNDEM (son 5)"; tail -n 5 gundem.md | cut -c1-250
echo "=== PIYASA (Yahoo)"; python3 - <<'E'
import urllib.request, json
for t in ["ES=F","NQ=F","^TNX","DX-Y.NYB","^GSPC","^NDX"]:
    try:
        m = json.load(urllib.request.urlopen(urllib.request.Request(f"https://query1.finance.yahoo.com/v8/finance/chart/{t}?interval=5m&range=1d", headers={"User-Agent": "Mozilla/5.0"}), timeout=10))["chart"]["result"][0]["meta"]
        p, pc = m["regularMarketPrice"], m.get("chartPreviousClose") or m.get("previousClose")
        print(f"  {t:9} {p:>10} ({(p/pc-1)*100:+.2f}%)")
    except Exception as e: print("  ", t, "hata", e)
E

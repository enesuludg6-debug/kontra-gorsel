#!/usr/bin/env python3
"""KURAL 85 — seans içi hisse-tahvil ayrışma ölçüsü (Enes 25.11 18:02 kabul).

Nasdaq 100 (^NDX) günlük % değişimi ile 10 yıllık faiz (^TNX) baz puan değişimini
yan yana koyar. Normal ilişki: faiz yükselirken büyüme hissesi düşer (ya da tersi).
SİNYAL: ikisi aynı anda düşüyorsa (faiz düşüyor + hisse düşüyor) satış faizle
açıklanamaz -> risk/büyüme kaygısı tweeti adayı.

Kullanım: python3 invest/ayrisma.py           (özet + sinyal; çıkış 0)
          python3 invest/ayrisma.py --sessiz  (yalnız sinyal varsa yazar)
Eşik: NDX <= -1,0% VE TNX <= -3 bp  -> SINYAL
      NDX >= +1,0% VE TNX >= +5 bp  -> TERS SINYAL (faiz yükselirken hisse yükseliyor: büyüme iyimserliği)
Tek kaynak (Yahoo); tweete yazılan rakam için kural 3/78 geçerli.
"""
import json, sys, urllib.request

def son(t):
    u = f"https://query1.finance.yahoo.com/v8/finance/chart/{t}?interval=5m&range=1d"
    m = json.load(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=10))["chart"]["result"][0]["meta"]
    return m["regularMarketPrice"], (m.get("chartPreviousClose") or m.get("previousClose"))

def main():
    sessiz = "--sessiz" in sys.argv
    try:
        n, npc = son("^NDX"); y, ypc = son("^TNX")
    except Exception as e:
        print("AYRISMA veri hatası:", e); return 0
    nd = (n / npc - 1) * 100
    bp = (y - ypc) * 100
    sinyal = None
    if nd <= -1.0 and bp <= -3:
        sinyal = "SINYAL: hisse ve faiz birlikte düşüyor -> satış faizle açıklanmıyor; büyüme/risk kaygısı tweeti adayı (somut yaz: hangi hisseler, ne kadar)"
    elif nd >= 1.0 and bp >= 5:
        sinyal = "TERS SINYAL: faiz yükselirken hisse yükseliyor -> büyüme iyimserliği; tweet adayı"
    if sessiz and not sinyal:
        return 0
    print(f"AYRISMA  NDX {nd:+.2f}%  |  10Y {y:.3f} ({bp:+.1f} bp)")
    print("  " + (sinyal or "normal ilişki, sinyal yok"))
    return 0

if __name__ == "__main__":
    sys.exit(main())

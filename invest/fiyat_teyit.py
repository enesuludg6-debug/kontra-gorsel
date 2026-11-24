#!/usr/bin/env python3
"""KURAL 78 (F-008): gün içi fiyat hareketinin ikinci kaynakla teyidi.
Kullanım: python3 fiyat_teyit.py <TICKER> <ikinci_kaynak_yuzde> "<kaynak adı>"
Yahoo anlık % değişimini çeker; ikinci kaynakla fark <= 0,5 puan ise TEYITLI (2 kaynak, net rakam yazılır),
değilse TEYITSIZ ('civarı' yazılır, DONGU'ya not). İkinci kaynak: shell'den Stooq/Nasdaq kapalı olduğu için
WebSearch '<TICKER> stock today' sonucundaki yüzde (MarketWatch, CNBC, Investing, Google Finance özeti) ya da haber metni.
Shell'den erişim açılırsa (stooq.com izinli alan) otomatik çekim eklenecek."""
import sys, json, urllib.request
if len(sys.argv) < 4: print(__doc__); sys.exit(2)
t, ikinci, kaynak = sys.argv[1].upper(), float(sys.argv[2].replace(",", ".")), sys.argv[3]
m = json.load(urllib.request.urlopen(urllib.request.Request(f"https://query1.finance.yahoo.com/v8/finance/chart/{t}?interval=5m&range=1d", headers={"User-Agent": "Mozilla/5.0"}), timeout=10))["chart"]["result"][0]["meta"]
y = (m["regularMarketPrice"] / m["chartPreviousClose"] - 1) * 100
fark = abs(y - ikinci)
print(f"{t} Yahoo {y:+.2f}% | {kaynak} {ikinci:+.2f}% | fark {fark:.2f} puan -> " + ("TEYITLI (2 kaynak, net yaz)" if fark <= 0.5 else "TEYITSIZ ('civarı' yaz, DONGU'ya not)"))
sys.exit(0 if fark <= 0.5 else 1)

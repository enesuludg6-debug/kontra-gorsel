#!/usr/bin/env python3
"""Kural 102 (Enes 27.11 23:34 'artık her tweet benim sesimle yazılacak'): Enes sesi kapısı.
Enes'in en çok okunan tweetleri kısa, konuşur gibi, süssüz. Bu betik metni stdin'den okur:
- 28 kelimeyi aşan cümle = HATA (Enes'in en uzun cümleleri ~25 kelime)
- cümle ortalaması 18 kelimeyi aşarsa = HATA
- rapor dili kalıpları (söz konusu, ilgili olarak, bu bağlamda, dikkat çekici, önemle, mevcut durumda, ...) = HATA
Çıktı: 'SES TEMIZ' ya da 'SES HATA' + nedenler."""
import sys, re
t = sys.stdin.read()
cumle = [c.strip() for c in re.split(r"(?<=[.!?])\s+|\n+", t) if c.strip() and not c.strip().startswith(("-", "•"))]
uz = [(len(c.split()), c) for c in cumle]
hata = []
for n, c in uz:
    if n > 28: hata.append(f"çok uzun cümle ({n} kelime): '{c[:60]}...' -> böl, Enes kısa konuşur")
if uz and sum(n for n, _ in uz) / len(uz) > 18: hata.append(f"cümle ortalaması {sum(n for n,_ in uz)/len(uz):.1f} kelime > 18 -> kısalt")
RAPOR = r"söz konusu|ilgili olarak|bu bağlamda|dikkat çekici|önemle|mevcut durumda|bu çerçevede|göz önünde bulundur|altını çiz|belirtmek gerek|ifade etmek gerek|kayda değer|nitelendir|yadsınamaz|şüphesiz ki|bir yandan .* öte yandan"
for m in set(re.findall(RAPOR, t.lower())): hata.append(f"rapor dili: '{m}' -> Enes böyle konuşmaz")
print("SES TEMIZ" if not hata else "SES HATA (kural 102) -> Enes sesiyle yeniden yaz:\n  - " + "\n  - ".join(hata))
sys.exit(1 if hata else 0)

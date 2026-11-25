---
name: enes-konu-secimi
description: Enes'in X hesabında her paylaşım turunda konu adaylarını beğeni verisine göre puanlayıp (konu_puan.py) atılacak tweeti seçerken ve zayıf konuyu elerken kullanılır (kural 87).
---
# Konu seçimi puanı (kural 87)

Amaç: hafta içi 18-26 tweet sınırında her tweet güçlü olsun. Sayı doldurmak için zayıf konu atılmaz; konu hisle değil veriyle seçilir.

## Adımlar (her turda, yazmadan önce)
1. 2-4 konu adayı çıkar (son dakika taraması, tur mesajındaki adaylar, portföy hisselerinin günlük hareketi, `ayrisma.py` sinyali).
2. Her aday için:
   `python3 invest/konu_puan.py --tur <TÜR> --saat <SS> --portfoy 0/1 --kaynak <n> --taze 0/1 --tekrar 0/1`
   - tür: HABER, PORTFOY, EGITICI, MAKRO, BILANCO, TEKNIK, BAGLAM-GORUS…
   - portföy: Enes'in portföy/ilgi listesi (DURUM.md, enes-portfoy-analiz).
   - tekrar: son 7 günde aynı konu (`grep` performans_veri.csv + DONGU).
3. En yüksek puanlıyı yaz. 60 ve üstü: at. 50-59: ancak günün 18 alt sınırına yetişmek gerekiyorsa ve saat 23'ten sonraysa. 50 altı: atma.
4. DONGU satırına tüm adayların puanını yaz: `KONU-PUAN: NBIS düşüş=88, PCE eğitici=74, RKLB Mizuho=41 (tek kaynak)`.

## Puan neye bakar
- Tür (25): o türün geçmiş beğeni ortalaması / hesap ortalaması (portföy ve eğitici en yüksek).
- Saat (20): o saatin geçmiş beğeni ortalaması (13, 17, 20-23 güçlü).
- Portföy bağı (20), kaynak sayısı (2+ = 20, 1 = 8), tazelik (son 2 saat = 15), tekrar cezası (−30).

## Önceliği artıranlar (puan eşitse)
- Kural 66 testinin sonucu çıktıysa (tutan yorum).
- `ayrisma.py` SİNYAL verdiyse ve bugün kullanılmadıysa.
- Günün portföy dosyası (86-c) ya da akşam eğiticisi (86-d) eksikse.

## Haftalık ayar
- Pazar performans raporunda `konu_puan.py` ağırlıkları gözden geçirilir: puanı 70+ olup 2'den az beğeni alan tweetler listelenir, nedeni DERSLER.md'ye yazılır.

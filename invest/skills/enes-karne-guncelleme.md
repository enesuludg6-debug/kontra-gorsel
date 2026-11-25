---
name: enes-karne-guncelleme
description: Enes'in X hesabında iyi giden tweete yeni veriyle güncelleme tweeti (kural 86-h) ve Cumartesi 20:25 yalnız tutan yorumların haftalık karnesi (kural 86-g) hazırlanırken kullanılır.
---
# Güncelleme tweeti ve haftalık karne (kural 86-g, 86-h)

## A) Güncelleme tweeti (86-h)
- Tetik: tweet atıldıktan sonraki 2 saat içinde 2.000+ gösterim YA DA 15+ beğeni (Buffer `get_post` / `list_posts` metrikleri ya da `perf_isle.py`), VE o konuda 2 kaynaklı YENİ veri (fiyat 2 puandan fazla değişti, şirket açıklaması, resmi veri).
- Zaman: yeni veriden sonraki 20-60 dk. Günde en çok 2; kural 80 alıntı sayısına dahil değil, günlük tweet sayısına dahil.
- Metin: ilk satır "Saat SS:DD tweetine güncelleme:" + tek yeni olgu (rakamla). En çok 2 paragraf, en çok 3 rakam. Önceki tweetteki iddia doğrulandıysa bunu sade söyle, abartma; ters gittiyse sadece yeni olguyu yaz.
- Kart: önceki kartın aynı düzeni, yeni son veriyle (kart3 "son veri" damgası değişir).
- Tür GUNCELLEME; kayıtta `--konu` içine önceki Buffer id.

## B) Haftalık karne (86-g) — Cumartesi 20:25, sabit görev `karne`
- Kaynak: son 7 günün kural 66 TEST-xxx kayıtları (`python3 invest/isler.py`, DONGU 'TEST-' satırları, enes-sonuc-takibi defteri).
- YALNIZ TUTAN yorumlar paylaşılır (Enes 25.11 18:06: "tutmayanları paylaşma sadece tutanlar"). Tutmayan ve kısmen tutanlar tweete, karta, alt metne yazılmaz; yalnız DONGU iç notu. İsabet oranı ya da "X/Y tuttu" yazılmaz.
- Tutan 2'den azsa karne atılmaz; DONGU'ya "karne: yeterli tutan yok".
- Metin: "Bu hafta tutan yorumlarım" + en çok 6 satır "GG.AA • konu • ne dedim • ne oldu (rakam)" + tek kapanış cümlesi (gelecek haftanın izlenecek tek eşiği).
- Abartı yok ("hep bildim", "yine haklı çıktık"). Getiri yüzdesi/işlem bildirimi yok.
- Kart: kart3 `siralama` (yeşil), satır başına tarih + konu + sonuç rakamı. Tür KARNE, kalıp N ya da C.

---
name: "enes-taslak"
description: "Enes'in X hesabında Enes'in kendisinin atacağı günlük kısa, iddialı tweet taslakları (hafta içi günde 4: 12-15, 15-18, 18-21, 21-24) hazırlanıp Enes'e gönderilirken ve bu taslakların performansı ölçülürken kullanılır (kural 69, F-001)."
---

# KURAL 69 — Enes için günlük kısa taslaklar (F-001, Enes 24.11.2026 09:53 kabul)

Gerekçe: Enes'in kısa elle tweetleri medyan 472 görüntülenme, sistemin uzun tweetleri 327 (İÇERİK AYARI, 21.11). Enes'in kendi sesiyle attığı kısa iddialı tweetler daha iyi gidiyor.

Repo `/home/claude/kontra-gorsel/invest`. Her zaman Türkçe. Yazım kuralları (enes-analiz-kalitesi, yasak.py, 54-C/D/E, 60, 64) ve doğruluk kuralları (her rakam 2 kaynak, kural 23) aynen geçerli.

## 1. Ne zaman
- Hafta içi ve Cumartesi her gün 2 taslak: biri 12:00-15:00, biri 21:00-24:00 arasındaki ilk uygun turda. Pazar 1 taslak (21:00-24:00).
- Sayaç: DONGU'daki o günün "ENES-TASLAK n/4" satırları. Saat dilimindeki ilk tur taslak gönderilmemişse gönderir.
- Taslak sistemin tweet hakkından sayılmaz (Enes atar); BUFFER'A GÖNDERİLMEZ, sistem bu metni kendisi paylaşmaz.

## 2. İçerik
- 1-2 cümle, en fazla ~240 karakter. İlk cümle kısa ve iddialı: net bir hüküm + onu taşıyan tek rakam.
- Konu: o dilimin en güçlü gelişmesi; öncelik portföy (DOCN RKLB SITM AXON CBRS VRT AVGO NBIS), sonra YZ/uzay/Nasdaq son dakika. Sistem aynı konuda tweet attıysa taslak farklı bir açı verir (aynı cümleyi tekrar etmez).
- Enes'in görüş profiline (ENES_GORUS_PROFILI.md) uygun; Enes'in ağzından, "ben" dili serbest. Al/sat emri, emoji, hashtag, link, soru yok.
- Kural 59: Enes'in bilinen görüşüyle çelişen bir hüküm yazılmaz.
- yasak.py temiz olmalı.

## 3. Gönderim
SendUserMessage, tweet mesajlarından ayrı ve kısa:
"ENES TASLAK (öğle|akşam): <metin>" + bir satır "Kaynak: <2 kaynak adı>" + varsa "Görsel önerisi: <kart düzeni ya da grafik>". Enes isterse kart çizilir ve SendUserFile ile gönderilir.

## 4. Kayıt ve ölçüm
- DONGU: "- SS:DD (GG.AA) ENES-TASLAK n/4: <konu> | <metin ilk 60 karakter>".
- perfogren (10:15) Enes'in elle attığı tweetleri (via=network) taslaklarla eşleştirir (aynı konu ve benzer ilk cümle); eşleşenleri performans_veri.csv'de tur=ENES-TASLAK olarak işaretler.
- 2 hafta sonra (08.12) karşılaştırma: ENES-TASLAK medyanı ile sistem medyanı ve Enes'in diğer elle tweetleri. Sonuç DERSLER Gözlemler'e; işe yaramadıysa Enes'e kaldırma önerilir.


## 26.11 15:06 GÜNCELLEME (Enes 'arttır', kural 95)
- Hafta içi günde 4 taslak (12-15, 15-18, 18-21, 21-24 dilimlerinin ilk uygun turu), Cumartesi 2, Pazar 1. Sayaç 'ENES-TASLAK n/4'.
- Her taslağın altına: 'Atarsan ilk 1 saatte gelen yanıtlara cevap ver.' Ayrıntı skills/enes-x-algoritma.md bölüm 4.

---
name: "enes-buyuk-cerceve"
description: "Enes'in X hesabında büyük bir kurumun (Citadel, Goldman, Morgan Stanley vb.) yeni notunu ya da piyasa rejimini tarihsel bir dönemle (2018, 2022, 2000 gibi) takvim takvime eşleyen, erişimi takipçi sayısının çok üstüne çıkabilen 'büyük çerçeve' makro tweetleri ve haftalık eşleme serisini hazırlarken kullanılır (kural 81-82)."
---

# KURAL 81-82 — Büyük çerçeve tweeti ve haftalık eşleme serisi (Enes 24.11.2026 21:12)

Çıkış noktası: 3.000 takipçili bir hesabın Citadel Securities'in 2018 benzetmesi üzerine yazdığı uzun gönderi 50.000 görüntülenme aldı (takipçisinin ~16 katı). Bizim aynı dönemdeki medyanımız ~340. Fark konudan değil YAPIDAN geliyor. Repo `/home/claude/kontra-gorsel/invest`, her zaman Türkçe.

## 1. Gönderiyi çok okutan 8 yapı taşı
1. **Ödünç otorite + tazelik:** İlk cümlede büyük bir kurum ve BUGÜN çıkan not ("Citadel Securities bugün ... not yayımladı"). Okur "bunu ilk burada gördüm" der, paylaşır.
2. **Herkesin hatırladığı bir dönem:** 2018 Noel dibi, 2022 ayı piyasası, 2000. Korku anında okur "bu sefer de öyle mi" sorusunun cevabını arar.
3. **Kesin tarihli hikâye:** "3 Ekim Powell, 19 Aralık artırım, 24 Aralık dip, 4 Ocak dönüş". Tarihler okura uzmanlık hissi verir ve kaydedilir.
4. **Düşünce değişimi:** "Hafta sonu 2022 dedim, inceledim, 2018'e daha çok benziyor." Fikrini veriyle değiştiren biri güven verir.
5. **Somut yol haritası:** Endeks için tarih + seviye (27.000 → 22.600 → 25.000 → 30.000). Tartışma, yanıt ve alıntı üretir; okur kaydeder.
6. **En kritik tek nokta:** "Bence işin en kritik kısmı şu" + bir mekanizma (enflasyon %3 üstündeyken Fed dönüş yapamaz).
7. **Okurun takvimine bağlanan sonuç:** "Noel Baba rallisi beklemiyorum." Herkesin aklındaki mevsimsel inanca karşı net cümle.
8. **Seri sözü:** "Bu tabloyu her hafta güncelleyeceğim." Takip etmek için sebep verir. Takipçi buradan gelir.

## 2. KURAL 81 — Büyük çerçeve tweeti (haftada 2, tercihen 12-15 ya da 21-24)
- Tetikleyici: (a) büyük kurumun aynı gün/dün çıkan makro notu (2 kaynak: Bloomberg/Reuters + Investing/Yahoo vb.), ya da (b) Nasdaq 100'de zirveden %10 ve üstü düşüş, %10 üstü sıçrama, Fed rejim değişikliği.
- Yapı (sıra serbest ama hepsi olur): kurum + tazelik açılışı → tarihsel dönemin kesin tarihli 3-5 durağı → bugünle 2-3 ortak işaret ve EN AZ 1 kritik fark (biz bu farkı bulduğumuz için daha bilgili görünürüz) → "takvim takvime eşleme" sonucu → bizim mekanizma yorumumuz → seri sözü.
- Eşleme seviyeleri BİZİM tahminimiz olarak değil, tarihsel yolun mekanik sonucu olarak yazılır: "2018'in yolunu bugünkü zirveye uygularsam dip 24.100 civarına denk geliyor." Hesap Yahoo verisiyle `python3 invest/esleme.py` ile yapılır (kendi hesabım), kapanış bazlı. Hedef fiyat, al/sat, "nakit yapın / ekleyin" YOK (kesin kurallar). Enes kendi planını yazmak isterse bu enes-taslak ile ona taslak olarak gider.
- Uzun tek tweet (uzun yazı tavanı, kural 32 kalıbı serbest); kart: eşleme grafiği (cizgi/zaman) ya da takvim.
- Kural 74 uzmanlık izi en az 3 (kesin emsal U4 + kendi hesap U3 + ikinci derece etki U5).
- DONGU türü BUYUK-CERCEVE; performans ayrıca ölçülür.

## 3. KURAL 82 — Haftalık eşleme serisi ("Nasdaq 100: 2018 ve 2022 haritası #N")
- Her Cuma 22:30 (ABD kapanışından önce son tur) ya da Cumartesi 12:30: tek tweet + kart. Numaralı seri (#1, #2 ...), DURUM.md'de sıradaki numara.
- İçerik: bugünkü Nasdaq 100 zirveden kayıp ve zirveden bu yana geçen işlem günü; aynı günde 2018 ve 2022 yolu nerede (kendi hesabım); hangisine daha yakın gidiyoruz (fark puanı); önümüzdeki haftanın takvimi (Fed, PCE, TÜFE, büyük bilanço).
- KURAL 23 ile uyum: seri BİZİM tahminimizi değil, tarihsel yolları gerçekleşenle karşılaştırır. Tarihsel yoldan ayrışma "tutmayan tahmin" değil, veridir ve yazılabilir. Kendi tahminimizi ölçen cümle yazılmaz.
- Seri başlangıcı: Cuma 27.11 (Şükran Günü sonrası yarım gün) ya da Cumartesi 28.11.

## 4. Ölçüm
- 08.12 ve sonrası her Pazar: BUYUK-CERCEVE ve seri tweetlerinin göreli görüntülenmesi, beğeni/1000, yanıt+repost, kaydedilme; takipçi değişimi (Buffer kanal). Hedef: göreli görüntülenme ≥ 2,0.

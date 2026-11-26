---
name: "enes-buyuk-cerceve"
description: "Enes'in X hesabında büyük bir kurumun yeni makro notunu ya da piyasayı 2018/2022 gibi bir dönemle takvim takvime eşleyen 'büyük çerçeve' tweetleri ve haftalık eşleme serisi hazırlanırken kullanılır (kural 81-82)."
---

# KURAL 81-82 — Büyük çerçeve tweeti ve haftalık eşleme serisi (Enes 24.11.2026 21:12)

Çıkış noktası: 3.000 takipçili bir hesabın Citadel Securities'in 2018 benzetmesi üzerine yazdığı uzun gönderi 50.000 görüntülenme aldı (takipçisinin ~16 katı). Bizim aynı dönemdeki medyanımız ~340. Fark konudan değil YAPIDAN geliyor. Repo `/home/claude/kontra-gorsel/invest`, her zaman Türkçe.

## 1. Gönderiyi çok okutan 8 yapı taşı
1. **Ödünç otorite + tazelik:** İlk cümlede büyük bir kurum ve BUGÜN çıkan not. Okur "bunu ilk burada gördüm" der, paylaşır.
2. **Herkesin hatırladığı bir dönem:** 2018 Noel dibi, 2022 ayı piyasası, 2000. Korku anında okur "bu sefer de öyle mi" sorusunun cevabını arar.
3. **Kesin tarihli hikâye:** "3 Ekim Powell, 19 Aralık artırım, 24 Aralık dip, 4 Ocak dönüş". Tarihler uzmanlık hissi verir ve kaydedilir.
4. **Düşünce değişimi:** "Hafta sonu 2022 dedim, inceledim, 2018'e daha çok benziyor." Fikrini veriyle değiştiren biri güven verir.
5. **Somut yol haritası:** Endeks için tarih + seviye. Tartışma, yanıt ve alıntı üretir; okur kaydeder.
6. **En kritik tek nokta:** bir mekanizma (enflasyon %3 üstündeyken Fed dönüş yapamaz).
7. **Okurun takvimine bağlanan sonuç:** "Noel Baba rallisi beklemiyorum" gibi mevsimsel inanca karşı net cümle.
8. **Seri sözü:** "Bu tabloyu her hafta güncelleyeceğim." Takip etmek için sebep verir.

## 2. KURAL 81 — Büyük çerçeve tweeti (haftada 2, tercihen 12-15 ya da 21-24)
- Tetikleyici: (a) büyük kurumun aynı gün/dün çıkan makro notu (2 kaynak), ya da (b) Nasdaq 100'de zirveden %10 ve üstü düşüş, %10 üstü sıçrama, Fed rejim değişikliği.
- Yapı: kurum + tazelik açılışı → tarihsel dönemin kesin tarihli 3-5 durağı → bugünle 2-3 ortak işaret ve EN AZ 1 kritik fark (bizi daha bilgili gösteren) → takvim takvime eşleme sonucu → bizim mekanizma yorumumuz → seri sözü.
- Eşleme seviyeleri tahminimiz olarak değil, tarihsel yolun mekanik sonucu olarak yazılır ("2018'in yolunu bugünkü zirveye uygularsam dip 24.100 civarına denk geliyor"). Hesap `python3 invest/esleme.py` (Yahoo verisi, kapanış bazı, kendi hesabım). Hedef fiyat, al/sat, "nakit yapın / ekleyin" YOK. Enes kendi planını yazmak isterse enes-taslak ile ona taslak gider.
- Uzun tek tweet; kart: eşleme grafiği ya da takvim. Kural 74 uzmanlık izi en az 3 (U4 kesin emsal + U3 kendi hesap + U5 ikinci derece etki). DONGU türü BUYUK-CERCEVE.

## 3. KURAL 82 — Haftalık eşleme serisi ("Nasdaq 100: 2018 ve 2022 haritası #N")
- Her Cuma 22:30 ya da Cumartesi 12:30: tek tweet + kart, numaralı seri; sıradaki numara DURUM.md'de.
- İçerik: Nasdaq 100 zirveden kayıp ve zirveden beri geçen işlem günü; aynı günde 2018 ve 2022 yolu nerede (esleme.py); hangisine daha yakınız; haftanın takvimi (Fed, PCE, TÜFE, büyük bilanço).
- KURAL 23 ile uyum: seri kendi tahminimizi değil tarihsel yolları gerçekleşenle karşılaştırır; tarihsel yoldan ayrışma veridir, yazılabilir. Kendi tahminimizi ölçen cümle yazılmaz.
- #1: Cuma 27.11 ya da Cumartesi 28.11.

## 4. Ölçüm
- Her Pazar ve 08.12: BUYUK-CERCEVE ve seri tweetlerinin göreli görüntülenmesi, beğeni/1000, yanıt+repost; takipçi değişimi. Hedef göreli görüntülenme ≥ 2,0.
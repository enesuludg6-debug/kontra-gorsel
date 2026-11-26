---
name: "enes-tarihsel-istatistik"
description: "Enes'in X hesabında 'şu anda X seviyesindeyiz, tarihte bu seviyeden sonra endeks şöyle getirdi' tarzı kısa, maddeli tarihsel istatistik tweeti hazırlanırken kullanılır (kural 96)."
---

# Enes tarihsel istatistik tweeti (kural 96, Enes 26.11 18:59)

Enes'in örnek gösterdiği tweet (TARZ örneği, rakamları bizim değil, kullanılmaz):
```
Şu anda "9" ile Aşırı Korku bölgesindeyiz.

<25 bölgesinin ardından, S&P 500'ün 12 ay sonraki ortalama getirileri şöyleydi:

- Vakaların %86'sında pozitif
- Son 14 yılda Mandala geriye dönük testlerinde ortalama %15,2 getiri.

Daha uzun vadelerde görünüm genellikle daha olumlu olma eğilimindedir.
```
Enes: "Bu tarz tweetler istiyorum, önemli olan konu değil, tweetin tarzı." Konu her şey olabilir (VIX, korku endeksi, zirveden düşüş, art arda düşüş günleri, RSI, put/call, AAII, kredi primi...).

## 1. Tarz (birebir uygula)
1. İlk satır: bugünkü durum, tek kısa cümle, rakamla ("Şu anda VIX 27 ile korku bölgesinde." / "Nasdaq 100 zirvesinden yüzde 20 aşağıda.").
2. İkinci paragraf: koşul + ufuk + "şöyleydi:" ile biten tek cümle ("VIX 25'in üstüne çıktığında S&P 500'ün 12 ay sonraki getirileri şöyleydi:").
3. 2-3 madde, her biri "- " ile başlar, kısa, rakamlı: pozitif oran, ortalama/medyan getiri, olay sayısı ve dönem. Maddelerde iki nokta etiketi YOK.
4. Son satır: tek, sakin, genel bir sonuç cümlesi (uzun vade / sabır / tarihin tekrar etmek zorunda olmadığı). Soru, emoji, hashtag, al/sat YOK.
5. Toplam kısa: ~250-420 karakter. Kart ZORUNLU değil ama tercih: kart3 siralama ya da sutun (ufuklara göre pozitif oran ve ortalama), YÖNTEM satırıyla.

## 2. Veri (kural 3, 23, 84: yalnız doğru rakam)
- Rakamlar başka hesaplardan KOPYALANMAZ (Mandala vb.). Her istatistik ya kendi hesabımız ya da 2 bağımsız kaynak.
- Kendi hesabımız: `python3 invest/taban_oran.py <koşul> <eşik> [--endeks ^GSPC|^NDX] [--bas 1990-01-01] [--ara 30]`
  koşullar: vix_ust, zirveden, dusus_gun, rsi_alt, gunluk. Çıktıdaki olay sayısı, dönem ve yöntem maddeye ya da karta girer ("1990'dan beri 128 olay, kendi hesabım").
- CNN Korku-Açgözlülük endeksinin uzun geçmişi bizde yok (alt_veri/korku_seri.csv yalnız Ağustos 2026'dan beri). Korku endeksi istatistiği ancak 2 bağımsız kaynakta aynı rakam varsa yazılır; yoksa VIX ya da zirveden düşüş vekil koşuluyla kendi hesabımızı kullan ve bunu açıkça söyle ("korku endeksinin vekili olarak VIX").
- DÜRÜSTLÜK: taban_oran.py her ufku "her gün tabanı" ile kıyaslar. Koşul tabandan belirgin daha iyi değilse (pozitif oran farkı < 3 puan ve ortalama farkı < 1 puan) bunu gizleme: ya o ufku yazma ya da tweeti atma. Tabandan iyi olan ufku seç ("12 ay" yerine "6 ay" daha güçlüyse onu yaz). Yanıltıcı seçim yasak: en kötü sonuç çok kötüyse (ör. −%40) ikinci maddede "en kötü vakada %X" ile yaz.
- Tarih her zaman tekrar etmez; son cümle kesinlik vermez ("eğilimindedir", "çoğu zaman").

## 3. Ne zaman
- Günde 1, en çok 2 (kural 95 aynı tema günde 2). Tetikleyici: sabah korku/VIX/AAII/put-call görevleri, sert endeks hareketi, zirveden kayıp eşikleri (-%10, -%20), art arda düşüş serileri.
- AÇIKLAYICI sayacına sayılmaz; tür TARIHSEL. kalite.py için --tur HABER --kalip F (hareketi normalleştirme: 'olağan' ya da tarihsel sıklık cümlesi) ya da B.
- Kural 95: önceki sistem tweetinden en az 35 dk sonra.

## 4. Kayıt
- kayit.py --tur TARIHSEL; DONGU'ya taban_oran.py komutu ve çıktısının ilgili satırı.
- Ölçüm: 10.12 perfogren, TARIHSEL medyan görüntülenme vs HABER.

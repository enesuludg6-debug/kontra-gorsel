---
name: "enes-x-algoritma"
description: "Enes'in X hesabında her tweet, tur aralığı, Enes taslağı ve açıklayıcı tweet planlanırken X For You algoritmasının (Phoenix) ağırlıklarına göre erişimi büyütmek için kullanılır (kural 95)."
---

# Enes X algoritması (kural 95, Enes 26.11 15:06: "X algoritmasını çok iyi analiz et ve geliştirmek için yetenek ekle")

Repo `/home/claude/kontra-gorsel/invest`, her zaman Türkçe. Bu dosya kural 46-94'ü DEĞİŞTİRMEZ; çelişkide yeni (büyük numaralı) kural geçerli. Kaynak: xai-org/x-algorithm (açık kaynak, Phoenix sıralayıcı), espressio.ai'nin 23.11.2026 commit 269340c ağırlık tablosu, ppc.land 13.08.2026 ağırlık yayını. Ağırlıklar değişebilir: ayda bir (ayın ilk Pazartesi'si, perfogren görevi) güncel tabloyu WebSearch "X algorithm weights" + github.com/xai-org/x-algorithm ile kontrol et, fark varsa bu dosyayı güncelle.

## 1. Algoritma nasıl çalışıyor (26.11.2026 itibarıyla)
- For You akışını tek bir Grok tabanlı model (Phoenix) sıralar. Her izleyici için her eylemin olasılığını tahmin eder, olasılığı ağırlıkla çarpıp toplar. Ağırlıklar ham sayıyı değil, O İZLEYİCİNİN tahmini olasılığını çarpar.
- Pozitif ağırlıklar (beğeni = 1x): karşılıklı takipleşen kişiden yanıt 28x (5+15), copy-link paylaşımı 28x (20), yanıt 7,1x (5), alıntı 7,1x (5), DM ile paylaşım 7,1x (5), gönderiden yazarı takip 5,6x (4), paylaş düğmesi 3x, repost 1,4x, beğeni 1x (0,708), tıklama 0,39x, link açma 0,28x, video açma 0, yer imi formülde yok. Okuma süresi (dwell) küçük ama pozitif; 5.11'de sürekli okuma süresi ağırlığı yükseltildi.
- Negatif: şikâyet −330x, yazarı sessize alma −83x, "ilgilenmiyorum" −75x, engelleme −44x, okumadan geçme −0,03x.
- Yazar çeşitliliği: aynı yazarın aynı akıştaki 2. gönderisi ×0,5, 3.'sü ×0,25 (taban 0,25). Kısa sürede çok tweet atmak birbirinin erişimini yer.
- Takip edilmeyen hesap (ağ dışı) ×0,75.
- Yeni yazar desteği (≤50.000 takipçi, bizim hesap 2.070): akış başına 1 orijinal gönderi, gönderi 2 saatten yeni ve 200 Ana Sayfa görüntülenmesinin altındayken yukarı taşınır. İlk 2 saat ve ilk 200 görüntülenme belirleyici.
- Link: Musk (29.07.2026) bir yıldır link cezası olmadığını söyledi, OpenTweet verisi de fark görmedi; yine de bizim kuralımız link koymamak (kural D, değişmez).

## 2. Bizim hesaba çevirisi (veri: 388 tweet, 12-26.11; sistem medyanı 347 = takipçinin %17'si, Enes 532 = %26; yalnız 6 tweet takipçi sayısını geçti)
1. ARALIK: sistem tweetleri arası EN AZ 35 dk (yazar çeşitliliği cezası). Turlar 35-50 dk arayla, turda 1 tweet. Bilanço/son dakika istisna ama aynı saatte 2'yi geçme. Günlük sayı kural 86 (hafta içi 18-26) içinde kalır; 18'in altına inmek gerekirse DONGU'ya gerekçe.
2. İLK 2 SAAT: en güçlü tweetler (açıklayıcı, portföy, Enes'in sesi) Türkiye'de ve ABD'de okurun aktif olduğu 13, 17, 20-23 slotlarına (kural 86-e). Tweet atıldıktan sonraki 60 dk içinde başka güçlü tweet atma (yeni yazar desteği akış başına 1 gönderiyi taşır).
3. YANIT ÜRETEN İÇERİK (7-28x): her tweetin sonu okurun cevap yazmak isteyeceği net, tartışılabilir bir hükümle biter (soru DEĞİL, Enes kuralı). Enes'e her paylaşımdan sonraki mesajda "ilk 1 saatte gelen yanıtlara sen cevap ver; karşılıklı takipleştiğin birinden gelen yanıt beğeninin 28 katı değerinde" hatırlatması (günde 1 kez yeter).
4. PAYLAŞILAN/KAYDEDİLEN İÇERİK (copy-link 28x, DM 7x): kendi hesabımızla üretilmiş veri kartları, "X nedir" açıklamaları, sıralama tabloları. Bunlar AÇIKLAYICI türde (bölüm 3).
5. TAKİP KAZANDIRAN İÇERİK (5,6x): okurun "bu hesap bunu hep anlatıyor" diyeceği tekrarlanan formatlar (numarasız, kural 88): bellek döngüsü, yapay zekâ altyapısı zinciri, uzay fırlatma ekonomisi.
6. NEGATİFTEN KAÇ (sessize alma −83x, ilgilenmiyorum −75x): aynı konunun aynı gün 2'den fazla işlenmesi, art arda benzer haber tweetleri, uzun ve kuru rakam yığınları. Aynı tema günde en çok 2 (bugünkü Asya çip 3 kez tekrarı ders).
7. OKUMA SÜRESİ: açıklayıcı tweetler 700-1.100 karakter, kısa satırlı, kartla birlikte; okur durup okur.
8. VİDEO: video açma ağırlığı 0, kart3 dosya_video yalnız gerçekten değer katıyorsa (okuma süresi için), erişim için değil.

## 3. AÇIKLAYICI tweet (yeni tür, Enes 26.11 15:06 "haber tweetlerinin bir kısmını açıklayıcıya çevir")
- Hafta içi EN AZ 5, hafta sonu en az 2 sistem tweeti AÇIKLAYICI türde (DONGU 'AÇIKLAYICI n/5'). Örnek ve model: 23.11 "Bellek DRAM ve NAND ayrımı" (4.008 görüntülenme, son 2 haftanın 1 numarası), 23.11 "AVGO Kuo TPU kesintisi" (3.167).
- Yapı: günün haberinden çıkan TEK kavram ya da ayrım (DRAM/NAND, HBM, CoWoS, TPU/GPU, gizli hesaplama, fırlatma fiyatı, kredi notu izlemesi, sipariş defteri) + bugün neden önemli + hangi şirkete nasıl yansıyor + Enes'in net hükmü. Haber cümlesi en çok 1, gerisi açıklama.
- Kural 86-d akşam eğiticisinden farkı: eğitici akşam 1 kez ve kavram odaklı; AÇIKLAYICI gün boyu ve haber odaklı (haberi açıklayarak verir). İkisi aynı gün aynı kavramı işlemez.
- Tür adı AÇIKLAYICI; kalite.py için --tur DERIN-ANALIZ (tavan 1200; kural 63 günde en çok 2 DERIN-ANALIZ -> 3. AÇIKLAYICI'dan itibaren portföy hissesiyse --tur PORTFOY (tavan 800), değilse --tur HABER (tavan 600)), kalıp E/J/A/H. Kart: kucuk_coklu, sutun, siralama ya da dosya; kartta kavramı anlatan tek satır.
- Haber turunda konu seçilirken konu_puan.py ile birlikte şu soru: "Bu haberi açıklayıcıya çevirebilir miyim?" Cevap evetse ve günün AÇIKLAYICI sayısı 5'in altındaysa açıklayıcı yaz.

## 4. Enes taslakları (kural 69 güncel, Enes 26.11 15:06 "arttır")
- Günde 4 taslak (hafta içi): 12-15, 15-18, 18-21, 21-24 dilimlerinin ilk uygun turunda 1'er. Cumartesi 2 (12-15, 21-24), Pazar 1 (akşam). DONGU 'ENES-TASLAK n/4'.
- Taslak = Enes'in kısa, iddialı, kişisel sesi (son 2 haftanın en çok görüntülenen 6 tweetinden 3'ü onun böyle tweetleri). 1-2 cümle, ~240 karakter, en çok 1 rakam, 2 kaynak, yasak.py temiz, soru yok. Sistem tweetiyle aynı konuyu aynı saatte verme; taslak sistem tweetinin daha keskin, daha kişisel hâli olabilir ama 2 saat ara olsun.
- Her taslağın altına tek satır: "Atarsan ilk 1 saatte gelen yanıtlara cevap ver."

## 5. Ölçüm (perfogren görevi, haftalık)
- Takipçi sayısı (Enes 26.11: 2.070) DURUM.md'de; her Pazar performans raporunda Enes'e sor değil, Buffer/kendi verisinden bilinmiyorsa son bilinen değer kullanılır.
- Ölçütler: tweet başına medyan görüntülenme / takipçi (hedef %17 → %25), takipçi sayısını geçen tweet oranı (hedef %1,5 → %5), AÇIKLAYICI türün medyanı vs HABER medyanı, aralık ≥35 dk olan tweetlerle <35 dk olanların medyan farkı (yazar çeşitliliği etkisi).
- 2 hafta sonra (10.12) sonuç DERSLER.md'ye; tutan değişiklik kalıcı, tutmayan geri alınır.

## KURAL 98 (Enes 27.11 17:39 'hepsini yeteneklere ekle') — hacim, taslak, biçim
Veri 13-26.11: Enes'in elle attıkları medyan 522, sistem 341 (her saat diliminde); sistem hacmi düşünce medyan 420+'ya çıktı. X kodunda zamanlanmış/yapay zekâ yazımı gönderiye ceza yok; fark hacim (yazar çeşitliliği cezası), kalıp görünüm ve yanıt farkından.
- (a) SİSTEM TWEETİ hafta içi günde 15-20, Cumartesi/Pazar en çok 8 (kural 86'nın 18-26'sının yerine). Yalnız GÜÇLÜ konu: konu_puan ≥75, son dakika, bilanço ya da 2 kaynaklı yeni haber. Zayıf konuda tur TWEETSİZ kapanır, DONGU'ya gerekçe. Sabit veri zincirleri bu sayıya dahil; verisi zayıf haftada atlanır. tur_basi.sh hedefi '15-20' gösterir, 20'de 'UST SINIR DOLDU'.
- (b) ENES-TASLAK hafta içi 6 (11-13, 13-15, 15-17, 17-19, 19-21, 21-24 dilimlerinde birer), Cumartesi 3, Pazar 2. Her biri 1-3 kısa cümle, 'ben' dili, tartışma açan net hüküm, en çok 1 rakam, kart yok. Altına 'Atarsan ilk 1 saatte gelen yanıtlara cevap ver.'. Sayaç 'ENES-TASLAK n/6'.
- (c) BİÇİM ROTASYONU her gün: sistem tweetlerinin en az 3'ü KARTSIZ tek-iki cümle (görselsiz, yalnız metin; Buffer'a asset gönderme), en az 2'si TARTIŞMA AÇAN GÖRÜŞ (karşı görüşü davet eden net iddia; Enes kuralı gereği SORU İŞARETİYLE BİTMEZ), kalanı kartlı analiz. Art arda iki tweet aynı biçimde olmaz. DONGU satırına 'biçim: kartsız | görüş | kartlı' yazılır.
- Ölçüm 04.12: sistem medyanı ≥450 hedef; tutmazsa hacim 12-15'e iner (Enes'e bildir).

# DERSLER (kesin kural 26) — ölç, ders al, uygula
Her tur konu seçmeden ve yazmadan önce "AKTİF DERSLER"i okur ve uygular. Dersler kuralları değiştirmez; konu, saat, biçim, adet tercihlerini değiştirir.

## DERS SİSTEMİ PROTOKOLÜ (kesin kural 26, Enes 17.11 17:24: "görüntülenmelerden ders çıkaracaksın; nasıl ekleyeceksin, yeni ders eskiyle çakışırsa ne yapacaksın, hepsini düşün")

A) VERİ
- Her tweet `invest/performans_veri.csv`'de bir satır: tarih, saat, kaynak (sistem | enes), tür, görüş (evet/hayır), konu, düzen, Buffer id, görüntülenme, beğeni, yanıt, repost, etkileşim %, ölçüm zamanı. Tweet atan tur satırı metrik boş olarak hemen ekler; sabah 09:00 görevi Buffer `list_posts includeMetrics` ile 12+ saati dolan tweetlerin metriklerini doldurur (ilk 24 saatte erken okunanları ertesi gün günceller).
- Enes'in elle attığı tweetler `kaynak=enes`: sistemin derslerine karışmaz (ayrı bakılır), ama "Enes'in tarzında ne tutuyor" gözlemi için kullanılabilir.
- Tür sonundaki `*` = tahmini tür (güven düşük); yeni satırlarda tür DONGU'daki kesin türdür.

B) ÖLÇÜ (elle "bence iyi gitti" yok; tek yol `python3 ders_analiz.py`)
- GÖRELİ SKOR = görüntülenme / önceki 7 günün medyanı. Hesap büyüdükçe ham sayı artar; göreli skor büyümeyi ve günün piyasa havasını temizler. Gruplar MEDYAN ile karşılaştırılır (tek viral tweet grubu taşımasın). Etkileşim % ikinci ölçü.
- Boyutlar: tür, saat dilimi (3 saatlik), görüş var/yok, kart düzeni, uzunluk, ticker türü (portföy/ilgi/büyük teknoloji), gün.
- Karıştırıcı kontrolü: tür karşılaştırması aynı saat diliminde de yapılır (`--test "tur:13F"` çıktısındaki "aynı dilimde" satırları). Büyük piyasa günü (S&P ±%1,5) ayrıca not edilir.

C) DERS EŞİĞİ VE SEVİYELER
- GÖZLEM: herhangi bir dikkat çeken fark (DERSLER.md "Gözlemler", tarih + rakam).
- ADAY DERS: ≥ 8 tweet, ≥ 2 farklı hafta, medyan farkı ≥ %25 (≥1,25x ya da ≤0,80x) ve iki haftada da aynı yön (`ders_analiz.py` "DERS ADAYI"). Pazar raporunda Enes'e bildirilir.
- AKTİF DERS: aday + bir sonraki hafta da aynı yönde (toplam 3 hafta) → turlar uygular. Adet/karışım/sabit seri değiştiren dersler Enes "onay" deyince aktif olur; saat, kart, uzunluk, ifade gibi küçük dersler otomatik aktif olur ve Pazar raporunda bildirilir.
- SAĞLAM DERS: 6+ hafta tutarlı.
- Her ders kaydı: ID (D-001), ifade (yap/yapma, ölçülebilir), kapsam (hangi tür/saat/sezon), kanıt (n, göreli medyan, haftalar, karşılaştırma grubu), seviye, eklenme tarihi, son test tarihi, yerine geçtiği ders.

D) ÇAKIŞMA KURALLARI
1. Hiyerarşi: Enes'in açık talimatı > kesin kurallar (al/sat yok, 2 kaynak, kural 23, 25 vb.) > Enes onaylı dersler > otomatik aktif dersler > adaylar > gözlemler. Ders hiçbir zaman kesin kuralı değiştiremez; çelişen ders yazılmaz.
2. Yeni bulgu aktif bir dersle çelişirse eski ders HEMEN SİLİNMEZ: ikisi "ÇELİŞKİ" diye işaretlenir, 1-2 haftalık A/B DENEY kurulur (aynı türde tweetlerin yarısı eski kurala, yarısı yeni bulguya göre; deney DERSLER.md "Deneyler"de: başlangıç, bitiş, ölçü). Bitince kanıtı güçlü olan kalır.
3. Kapsam farkı çatışma değildir: farklı bağlamda (bilanço sezonu / dışı, 13F haftası, büyük düşüş günü, hafta sonu) iki ders birlikte geçerlidir ve kapsam yazılır ("sezonda X, dışında Y"). Daha dar kapsamlı ders genel dersi o kapsamda geçersiz kılar.
4. Eşit kanıtta daha yeni veri öncelikli (hesap ve kitle değişir); ama yeni veri en az eski dersin örneklemi kadar olmalı.
5. Kazanan yeni bulgu: yeni ID ile eklenir ("D-007, D-003'ün yerine"); eski "Silinen dersler"e tarih ve gerekçeyle taşınır (geçmiş silinmez). Enes onaylı bir dersin yerine geçecekse Enes'e sorulur. [İPTAL 18.11 01:18 — Enes: 18-21 sınırı kaldırıldı]
6. Aynı tur içinde iki ders çakışırsa seviyesi yüksek olan, eşitse kapsamı dar olan uygulanır.

E) YAŞAM DÖNGÜSÜ
- Her aktif ders 4 haftada bir yeniden test edilir (Pazar raporu, `ders_analiz.py --test`). Tutmadıysa ADAY'a iner; arka arkaya 2 test tutmazsa silinir.
- En çok 15 aktif ders; fazlası birleştirilir ya da en zayıfı düşer. Gözlemler 6 hafta içinde adaya dönüşmezse silinir.
- KEŞİF: tweetlerin yaklaşık %10-15'i bilerek yeni tür/saat/biçim dener (derslere kilitlenip yeni şeyi hiç ölçmemek yok); keşif tweeti DONGU'da "(keşif)" diye işaretlenir.
- Yanılgı korumaları: tek viral tweet ders değildir; kendi tweetimi övmek yok, yalnız rakam; Buffer metrikleri gecikmeli, 12 saatten taze tweet ölçüme girmez; tahmini türlü (*) eski veriyle çıkan ders en çok ADAY olur.

F) TAKVİM
- Her gün 09:00: metrikleri doldur + `python3 ders_analiz.py --gun 7` → 1-2 gözlem.
- Pazar 21:30: `python3 ders_analiz.py` (28 gün) → adayları ve aktifleri güncelle, çelişki/deney kararları, Enes'e "bu hafta öğrendiklerim" (3-5 madde, rakamlı, eklenen/silinen/çatışan ders).
- 3 haftada bir (periyot.py karisim_onerisi): karışım önerisi.
- OPERASYON DERSLERİ (hatalardan) ayrı bölümdür: metrikle değil hata günlüğüyle eklenir, süresi dolmaz, ancak süreç değişince güncellenir.

## AKTİF DERSLER
Durum notu (17.11 17:35): aşağıdaki D-001..D-005 Enes ONAYLI DENEME olarak uygulanıyor. ders_analiz.py ile ilk ölçümde (120 tweet, 1,5 hafta) hiçbiri eşiği henüz geçmedi (saat dilimleri: 21-24 1,21x, 12-15 1,20x, 18-21 0,98x; tür farkları < %25). Bu yüzden seviye = ONAYLI DENEME; 01.12 ve 13.12 raporlarında eşiğe göre AKTİF'e çıkar ya da silinir.
D-001 Fikir kazanır: görüş/duruş içeren tweetler (YTD, RKLB grafik görüşü, NBIS, "tepeden almanızı") 1.200-3.300 görüntülenme; düz haber/bilanço medyanı ~340-370. Her tweette net düşünce (kural 25).
D-002 Adet değil kalite: 16.11'de 78 tweet, tweet başı görüntülenme artmadı. Günde toplam 12-15 tweet hedefi.
D-003 Saat: 12-15 (~633) ve 21-24 (~602) en iyi; görüşlü analizleri 12-15 ve 21-24'e koy. [18-21 'en çok 2 tweet' kısmı GEÇERSİZ: Enes 18.11 01:18 kaldırdı, 19.11 20:20 tekrar: 'iki saat arası tweet sınırı olmasın'. Saat dilimine göre tweet sınırı YOK.]
D-004 13F ve eğitici en düşük etkileşim (%1,2-1,4): 13F sezonda günde en çok 2; eğitici haftada 3 (alt sınır) ve 21-24'te dene.
D-005 Günlük karışım: görüşlü hisse/tema analizi 4-5 | bilanço 2-4 (bilanço günü, büyük isimler) | son dakika 1-2 (yorumlu) | vadeli + key levels + kapanış 3 | makro veri günü 1 (yorumlu) | analist notu 0-1 | 13F en çok 2.

## OPERASYON DERSLERİ (17.11 hatalarından; her tur uygular)
O-001 Açıklama saatini tahmin etme: önceki 2 çeyreğin bülten zaman damgasıyla doğrula; yayın turu T-5 dk başlasın (DIS 6:30 vs 6:40 → 14 dk gecikme).
O-002 Hazır kartta etiket ve kaynak satırı her zaman parametre; GAAP/düzeltilmiş ve kaynak adı gerçekte okunandan (HD, DIS).
O-003 Göndermeden önce satır başı "kelime + iki nokta" taraması (key levels "Takvim (TSİ):").
O-004 Makro veri tweeti tek tweet bile olsa yorumlu (kural 25); Fed beklentisini (artırım mı indirim mi) o an 2 kaynakla kontrol et, varsayma.
O-005 Census sayfası Chrome'da metin vermiyor: doğrudan `census.gov/retail/marts/www/marts_current.pdf` aç, ekran görüntüsünden oku; kontrol grubu 4. sayfa tablosunda (hız için hazırlıkta sayfa koordinatını bul).
O-006 Yayından sonra 10 dk içinde ikinci kaynak: arama indeksi ~10-15 dk geride; Chrome ile Reuters/CNBC canlı sayfası daha hızlı.
O-007 skor ve bento 1.8 logoyu taşımıyor (17.11 21:55: isi ve siralama kodda düzeltildi): bilanço rakamı uclu, analiz ilerleme/dortlu; logo rakama yakınsa başlığı tek satıra indir.
O-008 WebFetch "PROVENANCE_REQUIRED" cevapsız kalıyor: tekrar deneme, WebSearch ya da Chrome get_page_text.
O-009 60 dk ara kuralı varken zinciri yayın saatine göre kur (perakende 16:31 → sonraki tur 17:35).
O-010 Buffer'da sistem dışı gönderiler olabilir (Enes elle atıyor): tekrar kontrolünde onları da konu tekrarı sayarak bak.
O-011 (18.11 00:24, Enes) Bilanço rakam tweeti CRWV formatından ASLA eksik çıkmaz (gelir, HBK, şirkete özgü 2-3 metrik, 'X. ÇEYREK TAHMİNİ' bölümü). Bülten açılamazsa ilk bakılacak yer Yahoo Finance canlı blogu (finance.yahoo.com/technology/live/...; aramada başlık 'Nvidia earnings live' gibi) ve CNBC; rakamlar orada dakikalar içinde çıkıyor. Bir satır tek kaynaktaysa o satır 2-3 dk içinde teyit edilip tam format atılır; formatı bozan 'yıllık büyüme' gibi yedek satır konmaz.

## Gözlemler (doğrulanmayı bekleyen, tarih + kanıt)
- 21.11 sabah (7 gün): en iyi skorlar RKLB grafik/haber (7.45, 4.19) ve NBIS/NVDA bilanço tweetleri; en kötüler bilanço DETAY tweetleri (PANW, WMT, TGT 0.5-0.6). Detay tweetlerini azalt, portföy hissesi grafik/haberine ağırlık ver.
- 19.11: 18.11'de 46 tweet, ort. 113 görüntülenme (16.11 78 tweette de düşük); en iyiler kapanış özeti (818) ve büyük isim analizi (NVDA 563). Gece detay tweetleri henüz ölçülmedi.
- 18.11 (ders_analiz --gun 7): 'görüş: evet' işaretli 9 tweet göreli 0,77 (genel 1,00) ve ER 1,57 vs 1,82; analiz 'DERS ADAYI' dedi ama 9 tweetin çoğu 17.11 gece (az ölçüm) — 3. hafta ve 12+ saat ölçümüyle yeniden bakılacak, görüşlü tweet kuralı (25) değişmez.
- 18.11: en iyi 5'in 4'ü 16.11 13:20-14:57 arası (RKLB, NBIS, NVDA önizleme, vadeli); öğlen dilimi (12-15) güçlü görünüyor, tek günden ders yok. 17.11 16:31/17:36/19:32 tweetlerinde Buffer metrikleri hep 0 geldi (ölçüm gecikmesi olabilir), boş bırakıldı, yarın tekrar ölçülecek.
- 17.11: Buffer metrikleri ~24 saat gecikmeli; aynı günün tweetleri ertesi sabah ölçülür.
- 17.11 (ders_analiz, 120 tweet, 15-17.11, türler tahmini*): saat 21-24 göreli 1,21 (n=27), 12-15 1,20 (n=15, tek hafta), 18-21 0,98 (n=36), 09-12 0,88; tür farkları < %25 (13F 0,83 n=8). Enes'in kendi tweetleri göreli 1,37 (n=15, haftalar çelişkili). En yüksek tekil tweetler hepsi görüş/duruş içeriyor (YTD 9,35x, RKLB grafik görüşü 4,19x, NBIS 4,16x).

## Deneyler
- (yok)

## Silinen dersler
- (yok)

- 20.11 (perf_isle --ozet 7 gün, 184 olgun tweet): saat medyanları 21-24 416, 00-03 376, 12-15 364, 18-21 337, 15-18 322, 09-12 303. Enes elle (n=17) 472 vs sistem 327. 13F 247 (D-004 ile uyumlu). En iyiler portföy hissesi grafik/teknik (RKLB 2.243). ders_analiz eşiği henüz geçmedi (tek hafta) → DURUM İÇERİK AYARI "DENE" satırları.

- 20.11 gözlem (248 olgun, 15-19.11): detay/bilanço-detay med 212-226 en zayıf; son-dakika 497, vadeli 497, kapanış 534, haber 382; portföy evet 400 vs hayır 318; Enes elle 486 vs sistem 318. 19.11: 59 tweet, toplam 22.679 gösterim, medyan 261.

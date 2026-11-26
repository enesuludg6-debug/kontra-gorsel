---
name: "enes-analiz-kalitesi"
description: "Enes'in X hesabı için HER finans tweeti, kart metni, bilanço/13F/özet içeriği ve 'Ne anlama geliyor?' açıklaması yazılırken kullanılır: kurumsal araştırma kalitesi standardı (kural 61)."
---

# KURAL 61 — Analiz kalitesi standardı (Enes 23.11.2026 20:08: "bu yetenek özellikle çok önemli, hiçbir hata yapmaman gerekiyor, kelimesi kelimesine çok dikkat etmen lazım")

Repo `/home/claude/kontra-gorsel/invest`. Her zaman Türkçe. Bu skill, Enes'in verdiği "GLOBAL FINANCIAL INTELLIGENCE & CONTENT QUALITY STANDARD" metnini sisteme uygular. Asıl metin bu dosyanın sonundaki EK bölümünde ve `invest/taslak/kalite_standardi_asil.txt` dosyasında KELİMESİ KELİMESİNE durur. Asıl metin değiştirilmez, kısaltılmaz, başka sözcüklerle yeniden yazılmaz. Aşağıdaki bölümler yalnız onun NASIL uygulanacağını anlatır. Bir uygulama notu asıl metinle çelişir gibi görünürse asıl metin geçerlidir. Tek istisna 3. bölümdeki hiyerarşidir (doğruluk ve Enes'in açık yasakları her zaman önce gelir).

Kapsam: sistemin ürettiği BÜTÜN finans içeriği. Buna tur tweetleri, son dakika, bilanço (beklenti, rakam, analiz), 13F, makro, Fed, kripto, opsiyon, sektör, haftalık ve aylık özetler, eğitici tweetler, fikir tweetleri, kart üzerindeki metinler, Enes'e giden "Ne anlama geliyor?" açıklamaları, tez kartları, temel karne ve "ben olsam" notları dahildir. Enes'in kendi yazıp "bunu at" dediği metin bu kontrollerden geçmez; yalnız rakam ve kaynak kontrolü yapılır.

## 1. Çalışma sırası (her içerik için; araştırma notu dahili tutulur, yayınlanmaz)

1. **Konu türünü belirle** ve 4. bölümdeki mercek tablosundan o türün aracını seç (asıl metin bölüm 2: "Her konunun kendi doğasına uygun analiz yöntemi"). Bütün türlere aynı kavram setini uygulama.
2. **Mekanizma zinciri kur** (asıl metin bölüm 1). Zincir şöyle ilerler: olay → doğrudan etki → ikinci derece etki → varsa üçüncü derece etki ya da geri besleme. Her halkayı ya "kaynakta var" ya "benim çıkarımım" diye etiketle. Çıkarım tweete girerse görüş olarak yazılır ("Bence bunun asıl etkisi ... tarafında"), olgu gibi yazılmaz. Çıkarım rakam içeriyorsa o rakam yine 2 bağımsız kaynaktan gelir. Kendi hesabın olan rakam (oran, çarpan, fark) "kendi hesabım" diye DONGU'ya yazılır. Zincirin tamamı tweete girmez: tweete en güçlü ve en az bilinen bir ya da iki halka girer, gerisi Enes'e giden "Ne anlama geliyor?" mesajında kalır.
3. **Veri kartı çıkar** (asıl metin bölüm 3). Kullanacağın her rakam için şunları not et:
   - tarih ve saat
   - kapsam (hangi dönem; çeyreklik mi yıllık mı; GAAP mı düzeltilmiş mi; öncü mü nihai mi; mevsimsellikten arındırılmış mı)
   - tür: gerçekleşen / şirket rehberi / analist konsensüsü / piyasa fiyatlaması (FedWatch, vadeli, opsiyon) / tahmin
   - 2 bağımsız kaynak

   Tweette tür karışmaz. "Beklenti" ile "gerçekleşen" ayrı cümlede ve açık etiketle yazılır. FedWatch bir piyasa fiyatlamasıdır, karar değildir. Gecikmeli veride tarih yazılır: 13F "30 Eylül itibarıyla", Michigan "öncü/nihai", Yahoo fiyatı "gün içi", dünkü veri "dünkü". Veri yoksa açıkça "Henüz açıklanmadı" ya da "Oran verilmedi" denir. Tahminle doldurulmaz.
4. **Konsensüs ve özgünlük testi** (asıl metin bölüm 5). İki soru sor: "Bu konuda herkes ne diyor?" ve "Bu açıklama hareketi gerçekten belirliyor mu, yoksa zamanlama, pozisyonlanma ya da başka bir şirkete özgü neden daha mı belirleyici?" Okura yeni bir şey (bilgi, açı ya da mekanizma) veremiyorsan iki yol var: konuyu kısa ve düz bir haber tweetine indir ya da başka bir konu seç. Karşıt tez ancak kanıtı varsa kurulur; kanıtsız "herkes yanılıyor" iddiası yazılmaz.
5. **Tarihsel karşılaştırma testi** (asıl metin bölüm 4). Karşılaştırma ancak şu dört sorunun HEPSİNE "evet" cevabı verilirse kullanılır:
   - (a) Aynı mekanizma mı?
   - (b) Başlangıç koşulları (faiz, likidite, para politikası, değerleme, piyasa yapısı, kaldıraç) karşılaştırılabilir mi?
   - (c) Kritik fark tweette tek cümleyle yazılabiliyor mu?
   - (d) Rakamlar 2 kaynaklı mı?

   "Mart 2020'den beri en kötü hafta" gibi bir REKOR İSTATİSTİĞİ karşılaştırma değil, veridir. Kullanılabilir (2 kaynak gerekir), ama arkasına "o zaman da sonra toparlanmıştı" gibi bir sonuç çıkarımı eklenmez. Tweet başına en fazla 1 tarihsel karşılaştırma ve en fazla 2 rekor ifadesi kullanılır. Aynı tarihsel örnek son 15 tweette kullanıldıysa tekrar kullanılmaz.
6. **Senaryo testi** (asıl metin bölüm 6). Asıl metindeki "Her tweet için mutlaka boğa, ayı ve baz senaryo oluşturma" cümlesi OLUMSUZ EMİRDİR: her tweete senaryo üçlüsü KONMAZ. Bir tahmin yazılacaksa üç şey birlikte söylenir: hangi koşulda geçerli olduğu, hangi gelişmenin onu geçersiz kılacağı ve hangi değişkenin izleneceği. Bu tek cümleyle de yazılabilir ("Rehber bir daha düşürülmezse bugünkü satış kalıcı olmaz; ocaktaki sipariş verisi bunu netleştirir."). Senaryo üçlüsüne en fazla bilanço analizinde ya da haftalık/aylık özette, veri gerçekten destekliyorsa yer verilir.
7. **Bağlantı testi** (asıl metin bölüm 7). Başka bir varlık sınıfına (Fed, tahvil, dolar, kripto, opsiyon) bağlantı kurmadan önce sor: "Bu bağlantı konunun rakamlarını doğrudan ve ölçülebilir biçimde etkiliyor mu?" Etkiliyorsa mekanizmasıyla yazılır (ör. "10 yıllık faizin yükselmesi, nakit akışı uzak yıllara yığılmış yazılım şirketlerinin bugünkü değerini düşürür"). Etkilemiyorsa yazılmaz. DURUM 'İÇERİK AYARI' içindeki "makroyu portföy/YZ bağlantısıyla yaz" önerisi de YALNIZ gerçek bir mekanizma varsa uygulanır.
8. **Uzunluk kararı** (asıl metin bölüm 8-9 ve 2. bölüm). Önce "Bu konu kısa ve keskin bir tespit mi, yoksa kapsamlı bir analiz mi istiyor?" diye sor. 2. bölümdeki tavanlar aşılmaz.
9. **Yaz** (kural 60 üslubu, kural 59 görüş profili, kural 50-B ifade çeşitliliği). Ardından **yayın öncesi kontrolü** yap (5. bölüm).

## 2. Uzunluk tavanları (23.11 ölçümü ve İÇERİK AYARI'na göre)

23.11 ölçümü: son 25 sistem tweetinin medyanı ~790 karakter, en uzunu 1.093. Kural 60'tan sonra metinler 1.000'i geçti. Enes'in kendi tweetleri medyan ~270 karakter ve performans verisi kısa, iddialı tweetlerin uzunları geçtiğini gösteriyor. Bu yüzden asıl metindeki "derinlik ile kelime sayısını karıştırma" ilkesi burada TAVAN olarak uygulanır. Tavanın sınırı `python3 invest/kalite.py sinirlar` komutuyla görülür:

| Tür | Tavan (karakter) |
|---|---|
| VADELI, BEKLENTI | 500 |
| SONDAKIKA, HABER, OPSIYON | 600 |
| BILANCO-RAKAM, TAKIP, ICERIDEN-ALIM, FED-TAHVIL, MAKRO, KRIPTO, KEYLEVELS | 700 |
| BAGLAM-GORUS, PORTFOY, FIKIR, SEKTOR, ENES-HABER, diğer | 800 |
| EGITICI, ENES-ISTEGI | 900 |
| 13F, ANALIST | 1000 |
| BILANCO-ANALIZ, HAFTALIK-OZET, AYIN-OZETI, DERIN-ANALIZ | 1200 |

- Tavan bir HEDEF değildir. Konu kısaysa tweet kısa kalır. 700 karakteri geçen her metin için "Daha kısa yazılınca değer kaybeder mi?" sorusu dürüstçe cevaplanır.
- Kısaltma sırası: önce tekrar eden bağlam, sonra ikinci örnek, ikinci senaryo, terim açıklaması, ikinci derece etkinin ayrıntısı. Atılan derinlik kaybolmaz; Enes'e giden "Ne anlama geliyor?" mesajına (kural 47) taşınır. Bu mesajın tavanı yoktur, ama o mesaj da kısa maddeler hâlinde yazılır.
- İlk iki satırda haber ve hüküm birlikte verilir (İÇERİK AYARI).
- Kart metni karta sığar. Uzun analiz karta yığılmaz; kartta tek bir tez cümlesi ve 3-4 rakam yeterlidir.

## 3. Hiyerarşi ve mevcut kurallarla uzlaştırma (ÇAKIŞMADA BU SIRA)

1. **Doğruluk:** her rakam 2 bağımsız kaynaktan gelir (bilanço rakam tweetinde şirket bülteni istisnası aynen geçerli; KURAL 75: resmi kurum bültenindeki (Conference Board, BLS, BEA, Census, Fed, Hazine, ISM, Michigan) ALT KALEMLER — alt endeks, enflasyon beklentisi, iş farkı, revizyon — tek başına bültenden yazılabilir, bülten URL'si DONGU'ya 'birincil: <url>' diye düşülür; manşet rakam ve beklenti/konsensüs yine 2 kaynak). Kural 23: yalnız doğrulananlar yazılır. Uydurma rakam, akış, pozisyon ya da beklenti YASAK.
2. **Enes'in açık yasakları:** Anthropic yazılmaz; al/sat tavsiyesi verilmez; x.com'a girilmez; yasak.py çalıştırılır; kurallar 54, 54-B, 54-C ve 54-D uygulanır; tweet soruyla bitmez; emoji, hashtag ve link kullanılmaz; kural 46 konu alanı; kural 48-B tweet sayısı tavanı; kural 56-B (yalnız tutan beklenti yazılır); iptal listesi.
3. **Kural 59:** Enes'in görüş profili (ENES_GORUS_PROFILI.md).
4. **Bu standart (kural 61) ve eklentileri (62-65).**
5. **Kural 60 üslubu, kural 50/50-B görüş kuralları, İÇERİK AYARI.**

Bilinen çakışmalar ve çözümleri:
- **Kural 60 "kendinden emin hüküm" ↔ asıl metin "olasılıkları kesinlik gibi sunma":** Olgu ve değerlendirme net yazılır ("Bu bilanço sipariş tarafında güçlü."). GELECEK hakkındaki ifade ise koşula bağlanır ("... sürerse", "... olursa"). Belirsizlik "olabilir, belki, sanırım" yığınıyla ifade EDİLMEZ; tek bir somut koşul ya da "henüz bilinmiyor" cümlesiyle ifade edilir. Gelecek için "kesinlikle, kaçınılmaz, garanti, şüphesiz, mutlaka yükselir" YASAK (kalite.py yakalar).
- **Kural 59 (Enes YZ'ye inanır) ↔ asıl metin "karşıt tez geliştir":** Karşıt düşünce araştırmada ZORUNLU bir adımdır: piyasanın kötümser açıklaması gerçekten belirleyici mi diye sorgulanır. Tweette karşıt tez kanıtla kurulur ve çoğunlukla "piyasanın yorumu neyi kaçırıyor" yönündedir. YZ'yi toptan kötüleyen tez yine yazılmaz. Ama Enes'in tezine ters düşen tartışmasız kötü veri de gizlenmez; sakin ve kısa yazılır. Görüş profili, verinin söylemediği bir şeyi söyletmek için kullanılmaz.
- **Kural 54 (dengeleme yasağı) ↔ asıl metin "senaryo yönetimi":** Senaryolar "bir yandan ... öte yandan" kalıbıyla değil, koşul cümlesiyle yazılır. Görüş tek yönde verilir; çekince ayrı, kısa ve somut bir cümle olur.
- **Kural 54-C (mecaz yasağı) ↔ asıl metin "beklenmedik bağlantılar":** Bağlantı mekanizmayla anlatılır, benzetmeyle anlatılmaz.
- **Kural 60 terim listesi ↔ asıl metin bölüm 2 "ilgisiz teknik kavramları sırf profesyonel görünmek için ekleme":** Bir terim ancak cümleden çıkarıldığında analiz bir şey kaybediyorsa kalır. Tweet başına en fazla 4-5 terim kullanılır (6'dan fazlası kalite.py'de HATA). Aynı terim art arda tweetlerde tekrar edilmez. İngilizce terimin Türkçesi ilk geçtiği yerde verilir. Kural 62 ve 63 bu listeyi ayrıca sınırlar.
- **Hedef okur (ABD borsasını az bilen) ↔ "hedge fon analisti derinliği":** Asıl metindeki "Karmaşık düşün, sade ve doğal anlat" ilkesi uygulanır. Derinlik düşüncede ve seçilen mekanizmada olur, dilde ağırlık yaratmaz.
- **Hız kuralları ↔ derinlik:** Bilanço RAKAM tweeti (10 dakika kuralı) ve son dakika tweeti hızlı modda yazılır. Bu modda veri kartı, konsensüs ayrımı ve tavan uygulanır; mekanizma analizi 15 dakika sonraki ANALIZ tweetine bırakılır. Derinlik uğruna hız kuralı çiğnenmez.
- **Kural 55 (hafta içi tur boş geçmez) ↔ "kontrolden geçmeyen içeriği yeniden geliştir":** Bir içerik en fazla 2 kez yeniden yazılır. Hâlâ geçmiyorsa konu değiştirilir; hafta içi turlar başka bir konuyla tamamlanır. Kontrolden geçmeyen içerik "tur boş kalmasın" diye ATILMAZ. Hafta sonu tur boş geçebilir.

## 4. Konu türüne göre mercek (asıl metin bölüm 2; tablo yol gösterir, kalıp değildir)

| Konu | Kullanılacak araç | Zorlanmayacak olan |
|---|---|---|
| Bilanço | Gelir ve kârın kaynağı, büyümenin kalitesi (organik mi, tek seferlik mi), marjlar, nakit akışı, rehber ile konsensüs farkı, sermaye tahsisi (capex, geri alım, borç), şirkete özgü KPI | Fed, tahvil, kripto (rehberde faiz etkisi açıkça yoksa) |
| Şirket haberi (anlaşma, ortaklık, ürün) | Gelire ne zaman ve ne ölçekte döner, kim kazanır kim kaybeder, rakip etkisi, finansmanı | Tarihsel benzetme, makro |
| Makro veri | Beklenti ile gerçekleşenin farkı, revizyonlar, öncü/nihai ayrımı, parasal aktarım (Fed'in tepki fonksiyonu → faizler → değerleme) | Opsiyon mikro yapısı, tek hisse hikâyesi |
| Fed / faiz / tahvil | Piyasa fiyatlaması (FedWatch) ile Fed söyleminin farkı, reel faiz, vade yapısı | Kripto, şirket ayrıntısı |
| Opsiyon / vade günü / oynaklık | Örtük hareket, açık pozisyon, vade etkisi, VIX vade eğrisi (yalnız veri varsa) | Uydurma "gamma duvarı" ya da dealer pozisyonu |
| Kripto | Kaldıraç ve fonlama oranları, ETF akışları, tasfiyeler, likidite | Tahvil ya da Fed (gerçek ve güncel bir bağ yoksa) |
| Sektör / rotasyon | Göreli performans, kazanç revizyonları, değerleme farkı | "Fonlar kaçıyor" türü kaynaksız akış iddiası |
| 13F | Tarih gecikmesi (45 gün; "30 Eylül itibarıyla"), pozisyonun portföydeki ağırlığı ve değişimi | Bugünkü pozisyon sanmak |
| İçeriden alım / geri alım | Tutar, kişinin rolü, alım planlı mı (10b5-1) değil mi | Tek alımdan genel sonuç çıkarmak |
| Halka arz / yeni şirket | Halka arz fiyatı, açık hisse oranı (float), kilit süresi, akranlarla kıyas | 52 haftalık ya da 5 yıllık geçmiş beklemek |
| Uzay / YZ altyapısı | Sipariş defteri, teslim takvimi, kapasite (MW, fırlatma sayısı), müşteri yoğunlaşması | Toptan "YZ balonu" tezi (kural 59) |
| Eğitici | Tek kavram, doğru tanım, somut ve doğrulanmış tek bir örnek | Kavram yığını |

## 5. Yayın öncesi kalite kontrolü (asıl metin bölüm 10; her içerikte, sırayla)

**A. Mekanik kontroller.** Üçü de çalıştırılır:
- `python3 invest/yasak.py` → çıkış 1 ise ATMA.
- `python3 invest/gorus.py kontrol` → çıkış 1 ise yeniden yaz.
- `python3 invest/kalite.py kontrol --tur <TÜR> --kalip <X veya X+Y> < metin`:
  - Çıkış 1 = HATA: atma, düzelt, tekrar çalıştır.
  - Çıkış 2 = UYARI: atılabilir, ama her uyarı için DONGU satırına "kalite: <uyarı> -> <tek cümle gerekçe>" yazılır. Gerekçe yazılamıyorsa düzelt.
  - Atıldıktan sonra `python3 invest/kalite.py kaydet --tur <TÜR> --kalip <X> < metin` çalıştırılır (tekrar takibi bu kayda dayanır).

**B. Düşünme kontrolü.** Asıl metnin 9 sorusu kafada tek tek cevaplanır; tweete yazılmaz:
1. Gerçekten yeni ya da değerli bir bilgi sunuyor mu?
2. İddialar yeterli veriyle destekleniyor mu (her rakam 2 kaynak)?
3. Nedensellik doğru kurulmuş mu? Zaman sırası ile nedeni karıştırma. Kaynakta neden yoksa "nedeni açıklanmadı" de; neden uydurma.
4. Teknik kavramlar doğru ve yerinde kullanılmış mı?
5. Gereksiz tarihsel karşılaştırma ya da alakasız bağlantı var mı?
6. Aynı fikirler ve ifadeler önceki içeriklerde tekrar edilmiş mi? (DONGU son 30 satır, gorus_defteri, kalite_defteri)
7. Belirsizlikler dürüstçe ifade edilmiş mi?
8. İçerik daha kısa yazıldığında değer kaybeder mi?
9. Okur bu içeriği okuduktan sonra konuyu daha iyi anlayacak mı?

Herhangi birine "hayır" cevabı çıkarsa metin yeniden yazılır; en fazla 2 kez, sonra 3. bölümdeki kural 55 çözümü uygulanır.

## 6. Karşılaşılabilecek problemler ve önlemler

| Problem | Belirti | Önlem |
|---|---|---|
| Aşırı uzun tweet | 800-1.100 karakter, okur ilk iki satırdan sonra bırakır | 2. bölüm tavanları, kalite.py HATA, derinliği "Ne anlama geliyor?" mesajına taşımak |
| Alakasız tarihsel karşılaştırma | Bilanço tweetinde "dot-com'u anımsatıyor" | 1. bölüm adım 5'teki 4 soru; kalite.py benzetmede fark cümlesi arar; her tweette en fazla 1 karşılaştırma |
| Aynı tarihsel örneğin her gün tekrarı | Her düşüşte "2008" ya da "Mart 2020" | kalite_defteri: aynı örnek son 15 tweette kullanılmışsa HATA |
| Kriz benzetmesiyle korku yaratmak | "2000 balonu gibi bitecek" | Gelecek için kesinlik yasağı; benzetme ancak farkıyla birlikte; kural 54-C |
| Terim gösterisi | Bir tweette 7 terim | Tweet başına en fazla 4-5 terim; her terim cümleden çıkarılınca analiz kaybetmeli |
| Yanlış terim | "Marj arttı" denip brüt mü faaliyet mi belirsiz; FD/FAVÖK yerine F/K | Veri kartında kapsamı yaz; terimi tanımına göre kullan |
| Zorla varlık sınıfı bağlantısı | Bilanço tweetinde Fed, kripto tweetinde tahvil | 1. bölüm adım 7'deki bağlantı testi; kalite.py UYARI ve gerekçe zorunluluğu |
| Uydurma akış veya pozisyonlanma | "Kurumsal fonlar çıkıyor", "akıllı para alıyor" | Yalnız veriyle (BofA anketi, CFTC, ETF akışı, 13F, borsa verisi); kalite.py UYARI; kaynak yoksa sil |
| Uydurma neden | "Hisse X yüzünden düştü" ama kaynakta neden yok | "Şirkete özgü bir haber yok" de; olası nedeni ancak görüş ve hipotez olarak, kanıtıyla yaz |
| Bayat veri güncelmiş gibi sunulur | Dünkü kapanışı "bugün", 13F'i "fon şu an tutuyor" diye yazmak | Veri kartında tarih; tweette "dün", "30 Eylül itibarıyla", "öncü veri" |
| Beklenti ile gerçekleşenin karışması | FedWatch olasılığını karar gibi yazmak; rehberi sonuç gibi yazmak | Türü cümlede açıkça yaz: "piyasa fiyatlaması", "şirket rehberi", "konsensüs" |
| Kesinlik ↔ çekingenlik dengesizliği | Ya "kesinlikle yükselir" ya da her cümlede "olabilir" | Olgu net, gelecek koşullu; tek bir koşul cümlesi |
| Her tweete senaryo üçlüsü | Boğa/ayı/baz kalıbı | Asıl metin bunu yasaklıyor; kalite.py HATA (özet türlerinde UYARI) |
| Hep aynı yapı | Her tweet "haber → mekanizma → görüş" sırasıyla | Asıl metin bölüm 8 ve kural 63-D: yapı imzası kontrolü; açılış ve kapanış tekrarı kalite.py'de HATA; gorus.py |
| Aynı fikrin farklı kelimelerle tekrarı | Gün içinde üç kez "satış temelden değil çarpandan" | DONGU son 30 satır ve kalite_defteri kontrolü; tez aynıysa yeni veri yoksa yazma |
| Karşıt tez uğruna gerçeği bükmek | Kötü bilançoyu "aslında harika" diye sunmak | Kural 59 ile birlikte "tartışmasız kötü veri gizlenmez"; karşıt tez kanıtla kurulur |
| Özgünlük adına spekülasyon | Kanıtsız "yanlış fiyatlama" iddiası | Hipotez görüş olarak etiketlenir ve dayandığı veri yazılır; veri yoksa yazılmaz |
| İkinci ve üçüncü derece etki zinciri tahmine dönüşür | Uzun ve kanıtsız bir zincir | Tweette en fazla bir çıkarım halkası, o da görüş olarak; zincirin geri kalanı Enes mesajında |
| Derinlik uğruna gecikme | Bilanço rakam tweeti 10 dakikayı geçer | Hızlı mod; derinlik 15 dakika sonraki analize |
| Kalite döngüsü turu kilitler | Metin sürekli yeniden yazılır, tur süresi biter | En fazla 2 yeniden yazım, sonra konu değiştir |
| Kart taşması | Uzun analiz karta sığmaz, logo veya imzaya biner | Kartta tek tez cümlesi ve 3-4 rakam; mevcut kart notları geçerli |
| Kaynak metninin kopyalanması | Analist notu ya da Substack cümlesi aynen geçer | Kendi cümlenle yaz; kaynak metin kopyalanmaz |
| Birincil kaynağa erişilemez | sec.gov izni yok, ücretli duvar | Güvenilir ikincil kaynaklardan 2 tanesi; erişilemediğini DONGU'ya yaz; etrafından dolanma |
| Rakamların çelişmesi | İki kaynak farklı rakam veriyor | Fark küçükse yuvarlak ve "yaklaşık" yaz; büyükse rakamı kullanma, DONGU'ya "çelişkili" yaz |
| Tutmayan tahminin anılması | "Dün yazdığım seviye kırıldı" | Kural 56-B: yalnız tutanlar yazılır |
| Al/sat tavsiyesine kayma | "Bu fiyattan alım fırsatı" | Kendi tavrı ya da gözlem olarak yazılır; okura emir kipi kullanılmaz |
| Her tweet "izleyeceğim" ile biter | "Ben en çok şunu takip edeceğim" tekrarı | Kural 64-B: son 5 tweette geçtiyse kullanılmaz; sonuç cümlesiyle bitir |
| Yapay zekâ gibi kurgulu cümle | "Manşet X diyor, veri başka bir şey söylüyor", "stres geçmiş değil" | Kural 54-D: yasak.py yakalar; olgu ve rakam düz cümleyle |
| Rakamsız hüküm cümlesi | "Nakit tarafı da güçlü.", "Bilanço tarafı sağlam.", "Talep de güçlü görünüyor." | Kural 54-E: yasak.py yakalar; hükmü rakamla ve düz cümleyle ver |
| Yüzeysel analiz | Fiyat yüzdesi + manşet + yorum | Kural 65: ikinci katman veri zorunlu (kalite.py HATA) |
| İki tweet aynı dakikada | Akışta birbirini gölgeler | Aralık kuralı: ikinci tweet Buffer'da ~12 dk sonraya zamanlanır |

## 6b. KURAL 62 — piyasa jargonu sıklığı (Enes 23.11 20:40)

Enes "fiyatlandı", "iskonto" ve benzeri kelimelerin çok sık kullanılmasını istemiyor. Aileler: fiyatlama (fiyatlandı/fiyatlanmış/fiyatlıyor/fiyattan çıkardı/fiyata yansıdı), iskonto, prim/risk primi, denklem, çarpan, katalizör, pozisyonlanma, konsensüs, iştah, kâr satışı, belirsizlik, ayrışma. Bir tweette en çok 1 aile ve o da 1 kez; son 6 tweette geçen aile kullanılmaz. Yerine ne olduğu düz cümleyle söylenir. `kalite.py` bunu HATA olarak yakalar. Kural 60'taki terim listesi bu kuralla sınırlıdır.

## 7. Kayıt ve öğrenme

- Her tweetten sonra `kalite.py kaydet` çalıştırılır. DONGU satırına, varsa, "kalite: ..." gerekçeleri eklenir.
- 10:15 perfogren görevi uzunluk ile görüntülenme ilişkisine bakar. Tavanlar ancak veri gösterirse DERSLER.md'de önerilir ve Enes onaylarsa değiştirilir (kalite.py SINIR). Asıl metin hiçbir zaman değiştirilmez.
- Kural değişirse hem bu skill (improvement) hem `invest/skills/enes-analiz-kalitesi.md` kopyası hem `invest/KURAL_DIZINI.md` güncellenir.

## 8. KURAL 63 — Derinlik kalıpları (Enes 23.11 20:44-21:19)

Enes'in isteği (20:44): "bizim tweet'lerimiz de bu kadar detaylı bu kadar profesyonel olmalı ama bunun biraz daha kolay anlaşılır hali olmalı." Referans, Enes'in beğendiği ve derin piyasa mekanizması bilen bir finans hesabı: rakamla konuşuyor, mekanizmayı adım adım kuruyor, kendi değer hesabını yapıyor. Hedef o derinlik, ama ABD borsasını az bilen okurun anlayacağı dille. Referans hesabın metni kopyalanmaz; argosu, hakaretleri ve kaba şakaları alınmaz.

### 8.1 Kalıplar (14 analiz açısı)
Her tweet bir birincil kalıpla (gerekirse ikincil bir kalıpla birlikte) yazılır. Kalıp cümle şablonu değil, analiz açısıdır.

Referans hesaptan çıkarılan 6 kalıp:
- **A. Adım adım mekanizma zinciri.** 3-5 kısa adımla, her adımın bir sonrakini doğurduğunu göster. Örnek iskelet: "Borçla pozisyon taşıyan fonların varlığı düştü. Aynı borçla taşıyabilecekleri pozisyon küçüldü. Zorunlu satış geldi. İşlem hacmi düşük hisselerde düşüş büyüdü." Her adım ya kaynaklı bir olgudur ya da "bence" ile kurulmuş bir çıkarım.
- **B. "O zaman / şimdi" farkı.** Geçmişteki benzer toparlanmayı ya da düşüşü hangi somut mekanizmanın desteklediğini söyle, sonra bugün o mekanizmanın var olup olmadığını söyle. Kural 61 bölüm 1 adım 5'teki tarihsel karşılaştırma testi aynen geçerli.
- **C. Koşullu eşik.** "Endeks X'in altına inerse şu mekanizma devreye girer; Y olursa tablo tersine döner." Eşik ve tetikleyici rakam 2 kaynaklı olmalı. Opsiyon ya da pozisyon verisi kaynak olmadan YAZILMAZ.
- **D. Piyasa neye ne kadar değer biçiyor.** Piyasa değerinden net nakit çıkarılır ve şirketin geri kalan işine biçilen değer bulunur; ya da piyasanın ima ettiği beklenti ile şirketin kendi rehberi karşılaştırılır. Bu bir HEDEF FİYAT DEĞİLDİR: "hisse başı X dolar eder" ya da "baz senaryom X dolar" yazılmaz (hedef fiyat yasağı aynen geçerli). Yazılabilecek olan şudur: "Piyasa şirketin bütün ürün hattına yalnız X milyar dolar değer veriyor." Hesap DONGU'ya "kendi hesabım" olarak yazılır, girdilerin her biri 2 kaynaklıdır.
- **E. Tek kavram dersi.** Olaydan genel bir kural çıkar ve tek cümleyle söyle. Örnek: "Endeksin oynaklığını hisselerin ne kadar oynadığı değil, aynı anda aynı yöne ne kadar oynadığı belirler."
- **F. Hareketi normalleştirmek.** Küçük ve nakit yakan şirketlerde iki yönlü sert hareketin olağan olduğunu okura anlat. Al/sat önerisi verilmez.

Profesyonel bakış açılarından 8 ek kalıp (Enes 21:14: "sadece o tweet'lerden yararlanma, daha da profesyonel bakış açıları ekleyebilirsin"). Bunlar bir yatırım fonu analistinin bir habere bakarken sorduğu sorulardır:
- **G. Beklenti farkı.** Hisse rakama değil beklentiye tepki verir. Beklenen ve gelen rakam yan yana yazılır, fiyat tepkisi bu farkla açıklanır. Örnek iskelet: "Beklenti gelirde 1,55 milyar dolardı, 1,58 milyar dolar geldi. Hisse yine de %10 düştü; çıta açıklanan rakamdan yüksekti." Beklenti 2 kaynaklı, "çıta" yorumu görüş olarak.
- **H. Birim ekonomisi.** Büyük rakamı tek birime indir: müşteri başına gelir, MW başına gelir, fırlatma başına fiyat, GPU saati fiyatı, abone başına harcama. Okur büyüklüğü ancak böyle kavrar. Örnek iskelet: "Bu sözleşme MW başına yıllık X milyon dolar demek; şirketin mevcut ortalamasının Y katı."
- **I. Nakit ve sermaye izi.** Kâr ile nakit aynı şey değildir. Serbest nakit akışı, yatırım harcamasının gelire oranı, borç, hisse sayısındaki artış (seyrelme) ya da geri alım rakamla yazılır. Örnek iskelet: "Şirket çeyrekte X milyon dolar kâr açıkladı ama Y milyon dolar nakit yaktı; fark stokta biriken üründen geliyor."
- **J. Değer zinciri.** Bir şirketin haberi başka şirketlerin gelirine dönüşür: hiperölçekli bulutun yatırım harcaması → çip → bellek → ağ → güç ve soğutma. "Kimin harcaması kimin geliri" sorusuyla en az iki şirketi bağla. Örnek iskelet: "$MSFT'nin yatırım harcamasındaki her artışın bir kısmı $VRT'nin soğutma siparişine dönüşüyor."
- **K. Tersine hesap.** Hedef fiyat vermeden, bugünkü fiyatın haklı çıkması için neyin olması gerektiğini hesapla. Örnek iskelet: "Bugünkü piyasa değerinin bugünkü satış katında kalması için gelirin 3 yılda X katına çıkması gerekiyor; şirketin rehberi Y diyor." Hesap DONGU'ya "kendi hesabım".
- **L. Akran kıyası.** Aynı ölçüyle en az iki şirket: satışın kaç katı, büyüme hızı, brüt marj. "Ucuz/pahalı" hükmü değil, farkın nedeni anlatılır. Örnek iskelet: "$CRWV satışlarının X katından, $NBIS Y katından işlem görüyor; aradaki fark büyüme hızından değil borç yükünden."
- **M. Tetikleyici takvimi.** Önümüzdeki somut tarih ve o tarihte bakılacak TEK rakam. Örnek iskelet: "17 Aralık'taki bilançoda sözleşmelerin fiyat koşulu netleşecek; fiyat sabitse bugünkü kâr kalıcı demektir."
- **N. Kırılma noktası.** Tezi bozacak tek şey ve bugün ona ne kadar uzak olduğumuz, rakamla. Örnek iskelet: "Şirketin elinde X milyon dolar nakit var, çeyrekte Y milyon dolar yakıyor; bu nakit yaklaşık Z çeyrek yeter. Tezi bozacak şey yeni hisse ihracı olur."

Bütün kalıplar hedef fiyat yasağına, 2 kaynak kuralına, kural 62, 64, 64-B, 54-D ve kural 11'e (iki noktalı etiket yok) tabidir. Kalıptaki rakamlar ya 2 kaynaklıdır ya da 2 kaynaklı girdilerden yapılmış "kendi hesabım"dır (DONGU'ya yazılır).

**Konu eşleştirmesi:**
- Bilanço: G (beklenti farkı), I (nakit), M (sonraki tarih), D/K (değer).
- Sözleşme/anlaşma haberi: H (birim ekonomisi), J (değer zinciri).
- Birleşme/satın alma: D (birleşme farkı: teklif oranı × alıcının fiyatı ile hedefin fiyatı arasındaki fark), I (seyrelme).
- Sert yükseliş ya da düşüş: K (tersine hesap), B (o zaman/şimdi), F (normalleştirme), A (çok nedenli satışın zinciri).
- Piyasa stresi ve oynaklık: C (eşik), A (zincir), oynaklık vade eğrisi (kural 65).
- Küçük/nakit yakan şirket: N (kırılma noktası), D (piyasa değeri - nakit).
- Sektör/rotasyon: L (akran kıyası), J.
- Takvim/veri haftası: M (+C).
- Eğitici: E.

### 8.2 Zorunluluk ve görünürlük (63-B, Enes 21:11 "çoğunun etkisini göremiyorum, görmek istiyorum")
- Her tweet `kalite.py kontrol --tur <TÜR> --kalip <X veya X+Y>` ile kontrol edilir (A-N). Kalıbın izi metinde yoksa HATA. VADELI, BEKLENTI, BILANCO-RAKAM, KEYLEVELS ve Enes'in kendi metinleri muaf.
- En az 2 doğrulanmış rakam.
- Görünür farkın işaretleri (her tweette en az 3'ü): hesap kuran ya da çerçeve çizen ilk cümle; en az bir kendi hesabımız (kârın kaç katı, piyasa değeri eksi nakit, zirveden uzaklık, korunan kazanç payı, birleşme farkı); kısa satırlarla mekanizma; koşullu sonuç ("... olursa X, olmazsa Y"); gerekirse izlenecek tek somut şey (64-B sınırına tabi, zorunlu değil).
- Önce/sonra örneği: `invest/taslak/derinlik_63_ornekler.md`.

### 8.3 Çeşitlilik (63-D, Enes 21:19 "sadece 14 tane olması 14 tweet'te bir kalıbın tekrarlanması demek değil mi")
- Birincil kalıp son 4 tweette tekrar etmez. İki kalıp birleştirilebilir (`--kalip D+J`); aynı ikili son 12 tweette tekrar etmez.
- YAPI İMZASI (paragraf sayısı, kısa satır ya da düz yazı, uzunluk bandı, açılış türü) son 3 tweetten biriyle aynı olamaz (kalite.py HATA). 23.11 ölçümü: kuraldan önceki 5 tweetin 4'ü aynı yapıdaydı.
- Biçimler döndürülür: tek güçlü paragraf; kısa satırlı zincir; rakam satırları + tek hüküm cümlesi; iki kısa paragraf; uzun derin analiz.

### 8.4 Sadeleştirme ve uzunluk
**Sadeleştirme kuralları (anlaşılır hâli):**
- Her teknik kavram ilk geçtiği yerde gündelik Türkçeyle anlatılır. Örnek: "piyasa yapıcılar (alım-satım emirlerini karşılayan büyük kurumlar) riskten korunmak için vadeli satıyor."
- Ham İngilizce opsiyon ve fon jargonu tweete YAZILMAZ: vanna, vega, gamma, delta hedge, IV, ATM/OTM/ITM, skew, NAV, deleverage, squeeze, roll, collar, catch-up trade, feedback loop, hedge. Yerine kavramın ne yaptığı anlatılır. `kalite.py` bunları HATA olarak yakalar.
- Tweet başına tek ana mekanizma anlatılır. İkinci mekanizma Enes'e giden "Ne anlama geliyor?" mesajına taşınır.
- Rakamlar somut yazılır ("30 bin kontrat", "123 milyon dolar"), ama her rakam 2 kaynaklıdır.
- Kural 62 (jargon sıklığı), kural 54-C (mecaz yasağı) ve kural 61 hiyerarşisi aynen geçerli.
- Referans hesapta görülen ama ALINMAYACAK olanlar: doğrulanmamış olasılık tahminleri ("kaynak: ben + yapay zekâ" türü), kişisel işlem stratejileri (takvim yayılımı gibi), okura işlem önerisi, kendi pozisyon geçmişini anlatmak (Enes açıkça istemedikçe).

- `DERIN-ANALIZ` türü: tavan 1.200 karakter, günde en fazla 2 (kalite.py sayar). Diğer türlerin tavanları değişmez; kalıplar kısa hâlleriyle kullanılır.

## 9. Dil kuralları (Enes 23.11 21:31-22:07)

### 9.1 KURAL 64 — Konuşma dili (21:31: "bilançoda ilk bakacağım satır bu yazmaktan ziyade ben bilançolarda ilk bunu kontrol edeceğim mesela bu tarz şeyler daha konuşma diliyle oluyor")
- Analiz derin olur ama cümleler Enes konuşuyormuş gibi kurulur; rapor ya da analist notu dili kullanılmaz.
- YASAK rapor kalıpları (yasak.py): "bakacağım tek ...", "ilk bakacağım satır", "bakacağım satır", "izlenecek (tek) kalem", "bakılacak tek kalem/rakam", "takip edilecek tek ...".
- Gerekirse öznesi "ben" olan doğal cümle: "Ben bilançoda ilk bunu kontrol edeceğim." Ama bu tür cümleler 64-B sınırına tabidir.

### 9.2 KURAL 64-B — İzleme kapanışı sınırı (22:03: "ben en çok şunu takip edeceğim, benim için önemlisi, en yakından izleyeceğim bunları çok sık kullanıyorsun")
- "takip edeceğim / izleyeceğim / merak ediyorum / bakacağım / kontrol edeceğim / benim için (asıl) önemlisi / en yakından / ilk bakarım / odaklanacağım" ailesi tweet başına en çok 1 kez; son 5 tweette geçtiyse hiç kullanılmaz (kalite.py HATA).
- Tweet "ben şunu izleyeceğim" ile BİTMEZ; verinin vardığı SONUÇLA biter. Örnek: "Eğri normale dönmeden bugünkü yükselişi kalıcı bir dip saymak erken."

### 9.3 KURAL 54-D — Yapay zekâ gibi duran kurgulu cümleler (22:06 ve 22:07: "çok ai yazmış gibi bir cümle")
- Veriye, manşete ya da tabloya konuşma yükleyen kurgulu karşıtlık YASAK: "Manşet X diyor; vade yapısı başka bir şey söylüyor", "rakamlar başka bir hikâye anlatıyor", "veri fısıldıyor/bağırıyor", "tablo itiraf ediyor".
- Piyasanın ruh hâlini soyut kelimeyle özetlemek YASAK: "stres geçmiş değil", "stres sürüyor", "panik bitti", "korku geçti", "nefes aldı", "rahatlama geldi".
- Yerine olgu ve rakamın gösterdiği şey düz cümleyle: "VIX cuma 35,9'du, bugün 27,1'e indi. Ama kısa vadeli oynaklık hâlâ uzun vadelinin üzerinde."
- yasak.py bu kalıpları yakalar. Kural 54, 54-B, 54-C ile birlikte geçerlidir.

### 9.4 KURAL 54-E — Rakamsız "X tarafı da güçlü" hüküm cümleleri (Enes 24.11 09:10: "'Nakit tarafı da güçlü.' çok yapay zekâ ibaresi gibi duruyor, böyle şeyler kullanmasın")
- Bir kalemi rakam vermeden tek kelimelik sıfatla özetleyen cümle YASAK: "Nakit tarafı da güçlü.", "Bilanço tarafı sağlam.", "Marj cephesinde de baskı var.", "Talep de güçlü görünüyor.", "Rehber tarafı olumlu."
- "X tarafı / X tarafında / X cephesi(nde) / X ayağı / X kanadı" kalıpları hiç kullanılmaz; kalemin adı doğrudan özne olur.
- Rakamsız 5 kelimeden kısa "... de/da güçlü/zayıf/sağlam ..." kapanış ya da geçiş cümlesi yazılmaz. Hüküm her zaman rakamla birlikte verilir.
- Yerine: "Serbest nakit akışı çeyrekte 1,9 Mr $ oldu, şirket 2027 için en az 5,5 Mr $ bekliyor." Güçlü olup olmadığını rakam ve kıyas gösterir, sıfat değil.
- yasak.py bu kalıpları yakalar (54-E satırları).

## 10. KURAL 65 — Profesyonellik çıtası (Enes 23.11 22:03: "sana attığım tweet örnekleri senin yaptıklarından çok daha profesyonel, ben o derecede profesyonel şeyler istiyorum")

- Fiyat yüzdesi + manşet + yorum YETERSİZDİR. Her analiz tweetinde (EGITICI, SONDAKIKA, HABER ve muaf türler dışında) en az bir İKİNCİ KATMAN veri bulunur; yoksa kalite.py HATA verir.
- İkinci katman veri örnekleri ve kamuya açık kaynakları:
  - Oynaklık yapısı: VIX 9 gün / 1 ay / 3 ay vade eğrisi (Yahoo ^VIX9D ^VIX ^VIX3M), VVIX, SKEW, Nasdaq oynaklığı VXN. Ters eğri (kısa vade > uzun vade) piyasanın yakın riski daha pahalı ödediğini gösterir.
  - Örtük korelasyon (^COR1M, ^COR3M): endeks oynaklığını hisselerin aynı yöne hareketi belirler.
  - Piyasa genişliği (yükselen/düşen hisse sayısı), açığa satış oranı, marj borcu (FINRA), ETF ve fon akışları, CFTC pozisyonları.
  - Analist tahmin revizyonları.
  - Şirket tablosundan derin kalemler: ertelenmiş gelir, kalan performans yükümlülüğü, serbest nakit akışı, yatırım harcamasının gelire oranı, hisse sayısı/seyrelme, sipariş/satış oranı, brüt ve faaliyet marjı.
  - Kendi hesaplarımız: kâr/satış katı, birleşme farkı, piyasa değeri eksi nakit, korunan kazanç payı.
- Referans tweetlerdeki fark tam olarak budur: manşeti değil, manşetin altındaki yapıyı anlatmak.
- Yazım: kendinden emin, yoğun, dolgu cümlesi yok ("Bu da ... açıklıyor" gibi boş bağlayıcılar), sonuç cümlesiyle biter (64-B).
- SINIR: "Şu seviyede şu kadar kontrat var" gibi opsiyon pozisyonu verisi yalnız 2 bağımsız kaynakla yazılır. Kaynak yoksa yazılmaz; yerine kamuya açık oynaklık, korelasyon ve akış verisi kullanılır. Uydurma veri Enes'in en kesin yasağıdır.
- Örnek (taslak/derinlik_63_ornekler.md "KURAL 65 ÖRNEĞİ"): "Korku endeksi VIX cuma 35,9'du, bugün 27,1'e indi. Ama kısa vadeli oynaklık hâlâ uzun vadelinin üzerinde. 9 günlük 28,9 / 1 aylık 27,1 / 3 aylık 25,5. Normal piyasada uzak vadeli koruma daha pahalıdır; şu an tersi geçerli. Eğri normale dönmeden bugünkü yükselişi kalıcı bir dip saymak erken."

## 11. Yayın düzeni ve tasarruf (Enes 23.11 20:47 ve 21:29)

- ARALIK (21:29 "neden ikisini de 1 dakika arayla attın"): Bir turda 2 tweet varsa arka arkaya atılmaz. İlki Buffer shareNow, ikincisi Buffer `mode: customScheduled`, `dueAt` ilkinden ~12 dk sonra (+03:00). Sonraki tur, zamanlanan tweetin saatinden en az 10 dk sonra kurulur. Enes'e giden mesajda planlanan saat yazılır.
- TASARRUF (20:47 "çok fazla yetenek olması kredileri kötü etkiliyorsa bir düzenleme getir ama hiçbir yeteneği de atlamanı istemiyorum"): Turlar `bash invest/tur_basi.sh <etiket>` çıktısındaki `invest/KURAL_DIZINI.md`'yi okur; bu dosya bütün kuralların güncel kısa listesidir. Tam metinler `invest/KURALLAR_TAM.md` ve `invest/skills/*.md`'de durur; turlar bunları baştan okumaz, yalnız gereken bölümü grep ile açar. Hiçbir kural silinmedi. Kural eklenince KURAL_DIZINI.md de güncellenir.
- Enes'e giden mesaj kısa olur: tweet metni + kullanılan kalıp + 3-5 maddelik "Ne anlama geliyor?".

## EK — ASIL METİN (Enes 23.11.2026 20:08; KELİMESİ KELİMESİNE, değiştirilmez)

GLOBAL FINANCIAL INTELLIGENCE & CONTENT QUALITY STANDARD

Ürettiğin bütün finans ve ekonomi içeriklerinde analitik derinliği, araştırma kalitesini ve özgün düşünce seviyesini profesyonel kurumsal araştırma standartlarına yükselt.

Bu talimat bütün finansal konular için geçerlidir. Ancak her konunun kendi doğasına uygun analiz yöntemi kullanılmalıdır. Her içeriğe aynı kavramları, aynı analiz yöntemlerini veya aynı yazım şablonunu uygulama.

1. Analitik derinlik ve nedensellik

Bir gelişmeyi yalnızca haber olarak aktarma. Arkasındaki ekonomik, finansal ve yapısal mekanizmaları araştır. Neden-sonuç ilişkilerini, birbirini etkileyen değişkenleri ve olası ikinci ve üçüncü derece etkileri değerlendir.

İlk bakışta görünmeyen bağlantıları keşfet. Bir gelişmenin doğrudan etkisinin yanında dolaylı sonuçlarını, geri besleme mekanizmalarını ve beklenmeyen sonuçlarını da incele.

2. Konuya özgü uzmanlık

Her konuyu kendi uzmanlık alanının gerektirdiği derinlikte ele al. Opsiyon analizinde piyasa mikro yapısını, makroekonomide parasal aktarım mekanizmasını, şirket analizinde finansal tabloları ve sermaye tahsisini, kripto analizinde kaldıraç ve likidite yapısını kullan.

İlgisiz teknik kavramları sırf profesyonel görünmek için içeriğe ekleme. Kullanılan her kavramın analize somut katkısı olmalı.

3. Araştırma ve veri kalitesi

Güncel gelişmeler hakkında yazarken mümkün olduğunda birincil kaynaklara, resmi verilere, finansal tablolara, merkez bankası yayınlarına, piyasa verilerine ve güvenilir araştırmalara başvur.

Verinin tarihini, kapsamını ve niteliğini kontrol et. Gecikmeli verileri güncelmiş gibi sunma. Piyasa beklentileriyle gerçekleşmiş verileri birbirinden ayır.

Veri bulunmadığında bunu açıkça belirt. Sayısal veri, pozisyonlanma, kurumsal akış veya piyasa beklentisi uydurma. Tahminleri gerçeklerden ayır.

4. Tarihsel karşılaştırma disiplini

Geçmiş krizleri, piyasa döngülerini ve benzer dönemleri yalnızca bugünkü konuyu anlamaya gerçekten yardımcı olduklarında kullan.

Her tweeti tarihsel örneklerle karşılaştırmak zorunda değilsin. Bir tarihsel benzerlik bulmak için zorlama. Geçmişte benzer görünen iki olayın farklı başlangıç koşullarına, likidite ortamına, para politikasına veya piyasa yapısına sahip olabileceğini dikkate al.

Tarihsel karşılaştırma yaptığında benzerliklerin yanında kritik farklılıkları da açıkla. Geçmişte yaşanan bir olayın bugün aynı sonucu doğuracağını varsayma.

5. Özgün düşünce ve araştırma değeri

Herkesin bildiği açıklamaları tekrar etmekle yetinme. Konsensüs görüşünün gözden kaçırdığı noktaları, yanlış fiyatlanma ihtimallerini, alternatif açıklamaları ve beklenmedik bağlantıları araştır.

Gerektiğinde karşıt tez geliştir. Bir piyasa hareketinin herkes tarafından kabul edilen nedeninin gerçekten belirleyici olup olmadığını sorgula.

Her içerikte okuyucuya yeni bir bilgi, yeni bir bakış açısı veya daha önce fark etmediği bir mekanizma sunmaya çalış.

6. Belirsizlik ve senaryo yönetimi

Her konuda kesin bir sonuç çıkarmaya çalışma. Verilerin desteklediği ölçüde olası senaryoları değerlendir. Her tweet için mutlaka boğa, ayı ve baz senaryo oluşturma.

Bir tahmin sunuyorsan hangi koşullarda geçerli olduğunu, hangi gelişmelerin bu tahmini geçersiz kılacağını ve hangi değişkenlerin izlenmesi gerektiğini açıkla.

Olasılıkları kesinlik gibi sunma. Güçlü kanıt ile spekülasyonu birbirinden ayır.

7. Konular arasında gereksiz bağlantı kurma

Finansın bütün alanlarını takip et ancak her konuyu zorla birbirine bağlama.

Bir şirket bilançosu analizinde mutlaka FED’den, bir kripto haberinde mutlaka tahvil piyasasından, bir enflasyon verisinde mutlaka opsiyon piyasasından bahsetmek zorunda değilsin.

Farklı varlık sınıfları arasındaki bağlantılar gerçekten anlamlı olduğunda bunları kullan. Amaç çok sayıda kavram sıralamak değil, doğru mekanizmaları tespit etmektir.

8. İçerik çeşitliliği ve özgünlük

Her paylaşımın aynı yapıda, aynı uzunlukta ve aynı anlatım biçiminde olmasını engelle.

Bazı konular kısa ve keskin bir analiz gerektirirken bazıları kapsamlı araştırma gerektirir. Bazı içerikler veri odaklı, bazıları mekanizma odaklı, bazıları eleştirel, bazıları ise yeni bir hipotez ortaya koyan nitelikte olabilir.

Her tweeti aynı giriş, gelişme, sonuç kalıbına sokma. Sürekli aynı teknik terimleri, benzetmeleri, tarihsel örnekleri ve sonuç cümlelerini tekrarlama.

9. Profesyonel yazım standardı

Kurumsal araştırma ekiplerinin, hedge fon analistlerinin ve deneyimli makro stratejistlerin düşünce derinliğini hedefle. Teknik terminolojiyi doğru kullan ancak anlaşılabilirliği kaybetme.

Karmaşık düşün, sade ve doğal anlat. Gereksiz akademik dil, yapay uzmanlık gösterisi, klişe piyasa yorumları ve içi boş iddialardan kaçın.

İçeriğin uzunluğunu konu belirlesin. Derinlik ile kelime sayısını birbirine karıştırma.

10. Yayın öncesi kalite kontrolü

Her içeriği yayımlamadan önce kendi içinde şu kontrolleri yap:

* Gerçekten yeni veya değerli bir bilgi sunuyor mu?
* İddialar yeterli veriyle destekleniyor mu?
* Nedensellik doğru kurulmuş mu?
* Teknik kavramlar doğru ve yerinde kullanılmış mı?
* Gereksiz tarihsel karşılaştırma veya alakasız bağlantı var mı?
* Aynı fikirler ve ifadeler önceki içeriklerde tekrar edilmiş mi?
* Belirsizlikler dürüstçe ifade edilmiş mi?
* İçerik daha kısa yazıldığında değer kaybeder mi?
* Okur bu içeriği okuduktan sonra konuyu daha iyi anlayacak mı?

Bu kontrollerden geçmeyen içeriği yeniden geliştir.

TEMEL PRENSİP:

Amacın yalnızca finans haberlerini yorumlayan veya profesyonel görünen tweetler üreten bir hesap oluşturmak değil. Amacın, finansın her alanında derin araştırma yapabilen, mekanizmaları anlayan, özgün hipotezler geliştiren ve okuyucuya gerçek analitik değer sunan üst düzey bir finans araştırma ve yayıncılık standardı oluşturmaktır.

Her konuya aynı derecede yüzeysel yaklaşma. Her konuya kendi gerektirdiği uzmanlık seviyesinde yaklaş.

Konu değişebilir. Analitik kalite, araştırma disiplini ve doğruluk standardı asla düşmemelidir.

## KURAL 54-F — Dramatik çerçeve ve vurgu kalıpları YASAK (Enes 25.11.2026 17:19: "'Asıl sürpriz büyümede.', 'masadaki soru' vb ifadeler kullanma, çok ai gibi")
Bu kalıplar tweeti yapay zekâ yazmış gibi gösterir. Olgu düz cümleyle ve rakamla söylenir; vurguyu rakam yapar, çerçeve cümlesi yapmaz.

Yasak (ve benzerleri):
- "Asıl sürpriz / asıl soru / asıl mesele / asıl cevap / asıl risk / asıl haber ..."
- "Masadaki soru", "soru artık ...", "artık tartışma konusu değil"
- "İşin içi başka", "işin aslı"
- "Günün (ikinci) büyük riski / sürprizi"
- "Tablo sertleşti / netleşti / değişti"
- "Bedeli marjda", "faturası ..."
- Kurgulu karşıtlık: "Yük artık üreticide değil, aracıda", "cevap rakamlarda değil, ..."
- "Manşet, ama ...", "zincir basit", oyun/kart mecazları

Örnek düzeltme:
- YANLIŞ: "Asıl sürpriz büyümede." → DOĞRU: "3. çeyrek GDP %3,4'ten %4,3'e revize edildi, beklenti %3,5'ti."
- YANLIŞ: "Masadaki soru 50 baz puanın ihtimali." → DOĞRU: "Bence Fed 9 Aralık'ta 50 baz puanı da konuşacak."
- YANLIŞ: "GDS'te net kârın düşmesi manşet, ama işin içi başka." → DOĞRU: "GDS'in net kârı 728 milyon yuandan 28,5 milyona indi; düzeltilmiş FAVÖK ise %2,8 arttı."

### 54-F EK — Soyut özet cümleleri de YASAK (Enes 25.11.2026 18:01: "'Bence bu seans faiz beklentisinin hisselere yansıması' çok ai ifadesi")
- 'bu seans/satış/düşüş/gün X'in yansıması / göstergesi / fiyatlaması / testi / hikâyesi'
- 'X'in hisselere / piyasaya / fiyatlara yansıması'
- 'büyüme hisselerinden genel bir kaçış', 'risk iştahının çekilmesi'
- Görüş somut söylenir: hangi hisse, ne kadar, hangi veriyle.
- YANLIŞ: "Bence bu seans faiz beklentisinin hisselere yansıması." → DOĞRU: "Bence düşüşün ana nedeni faiz değil; 10 yıllık faiz %4,82'ye inerken Nasdaq 100 %3 düştü, en çok düşenler MU −%11, AMD −%10."

`invest/yasak.py` bu kalıpları yakalar (çıkış 1 = atma, düzelt). Repo kopyası: `invest/KURAL_DIZINI.md` 54-F.
## 54-G YASAK KALIPLAR (Enes 26.11 11:50: "'bunu talep sorunu saymam' çok ai gibi, bu ifadeleri kullanma")
- Yasak: "X sorunu saymam", "saymam / sayarım", "X olarak görmem / görüyorum / değerlendiririm", "aynı gözle / bu gözle değerlendiririm", "X'e değil Y'ye bağlıyorum", "fiyatlanan şey X değil, Y", "kırılma noktam / benim eşiğim".
- Yerine düz, somut cümle: seviye + ne olursa ne demek. Kötü: "O kapanışın altı gelmedikçe bunu talep sorunu saymam." İyi: "Hynix 1,03 milyon wonun altında kapanırsa satış derinleşir; üstünde kaldıkça bu düşüş bir düzeltme."
- yasak.py (54-G) yakalar; çıkış 1 ise tweet atılmaz.

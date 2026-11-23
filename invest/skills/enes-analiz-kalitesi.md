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
6. **Senaryo testi** (asıl metin bölüm 6). Asıl metindeki "Her tweet için mutlaka boğa, ayı ve baz senaryo oluşturma" cümlesi OLUMSUZ EMİRDİR: her tweete senaryo üçlüsü KONMAZ. Bir tahmin yazılacaksa üç şey birlikte söylenir: hangi koşulda geçerli olduğu, hangi gelişmenin onu geçersiz kılacağı ve hangi değişkenin izleneceği. Bu tek cümleyle de yazılabilir ("Rehber bir daha düşürülmezse bu fiyatlama kalıcı olmaz; izlenecek rakam ocaktaki sipariş verisi."). Senaryo üçlüsüne en fazla bilanço analizinde ya da haftalık/aylık özette, veri gerçekten destekliyorsa yer verilir.
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
| BILANCO-ANALIZ, HAFTALIK-OZET, AYIN-OZETI | 1200 |

- Tavan bir HEDEF değildir. Konu kısaysa tweet kısa kalır. 700 karakteri geçen her metin için "Daha kısa yazılınca değer kaybeder mi?" sorusu dürüstçe cevaplanır.
- Kısaltma sırası: önce tekrar eden bağlam, sonra ikinci örnek, ikinci senaryo, terim açıklaması, ikinci derece etkinin ayrıntısı. Atılan derinlik kaybolmaz; Enes'e giden "Ne anlama geliyor?" mesajına (kural 47) taşınır. Bu mesajın tavanı yoktur, ama o mesaj da kısa maddeler hâlinde yazılır.
- İlk iki satırda haber ve hüküm birlikte verilir (İÇERİK AYARI).
- Kart metni karta sığar. Uzun analiz karta yığılmaz; kartta tek bir tez cümlesi ve 3-4 rakam yeterlidir.

## 3. Hiyerarşi ve mevcut kurallarla uzlaştırma (ÇAKIŞMADA BU SIRA)

1. **Doğruluk:** her rakam 2 bağımsız kaynaktan gelir (bilanço rakam tweetinde şirket bülteni istisnası aynen geçerli). Kural 23: yalnız doğrulananlar yazılır. Uydurma rakam, akış, pozisyon ya da beklenti YASAK.
2. **Enes'in açık yasakları:** Anthropic yazılmaz; al/sat tavsiyesi verilmez; x.com'a girilmez; yasak.py çalıştırılır; kurallar 54, 54-B ve 54-C uygulanır; tweet soruyla bitmez; emoji, hashtag ve link kullanılmaz; kural 46 konu alanı; kural 48-B tweet sayısı tavanı; kural 56-B (yalnız tutan beklenti yazılır); iptal listesi.
3. **Kural 59:** Enes'in görüş profili (ENES_GORUS_PROFILI.md).
4. **Bu standart (kural 61).**
5. **Kural 60 üslubu, kural 50/50-B görüş kuralları, İÇERİK AYARI.**

Bilinen çakışmalar ve çözümleri:
- **Kural 60 "kendinden emin hüküm" ↔ asıl metin "olasılıkları kesinlik gibi sunma":** Olgu ve değerlendirme net yazılır ("Bu bilanço sipariş tarafında güçlü."). GELECEK hakkındaki ifade ise koşula bağlanır ("... sürerse", "... olursa"). Belirsizlik "olabilir, belki, sanırım" yığınıyla ifade EDİLMEZ; tek bir somut koşul ya da "henüz bilinmiyor" cümlesiyle ifade edilir. Gelecek için "kesinlikle, kaçınılmaz, garanti, şüphesiz, mutlaka yükselir" YASAK (kalite.py yakalar).
- **Kural 59 (Enes YZ'ye inanır) ↔ asıl metin "karşıt tez geliştir":** Karşıt düşünce araştırmada ZORUNLU bir adımdır: piyasanın kötümser açıklaması gerçekten belirleyici mi diye sorgulanır. Tweette karşıt tez kanıtla kurulur ve çoğunlukla "piyasanın yorumu neyi kaçırıyor" yönündedir. YZ'yi toptan kötüleyen tez yine yazılmaz. Ama Enes'in tezine ters düşen tartışmasız kötü veri de gizlenmez; sakin ve kısa yazılır. Görüş profili, verinin söylemediği bir şeyi söyletmek için kullanılmaz.
- **Kural 54 (dengeleme yasağı) ↔ asıl metin "senaryo yönetimi":** Senaryolar "bir yandan ... öte yandan" kalıbıyla değil, koşul cümlesiyle yazılır. Görüş tek yönde verilir; çekince ayrı, kısa ve somut bir cümle olur.
- **Kural 54-C (mecaz yasağı) ↔ asıl metin "beklenmedik bağlantılar":** Bağlantı mekanizmayla anlatılır, benzetmeyle anlatılmaz.
- **Kural 60 terim listesi ↔ asıl metin bölüm 2 "ilgisiz teknik kavramları sırf profesyonel görünmek için ekleme":** Bir terim ancak cümleden çıkarıldığında analiz bir şey kaybediyorsa kalır. Tweet başına en fazla 4-5 terim kullanılır (6'dan fazlası kalite.py'de HATA). Aynı terim art arda tweetlerde tekrar edilmez. İngilizce terimin Türkçesi ilk geçtiği yerde verilir.
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
| Opsiyon / vade günü | Örtük hareket, açık pozisyon, vade etkisi (yalnız veri varsa) | Uydurma "gamma duvarı" ya da dealer pozisyonu |
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
- `python3 invest/kalite.py kontrol --tur <TÜR> < metin`:
  - Çıkış 1 = HATA: atma, düzelt, tekrar çalıştır.
  - Çıkış 2 = UYARI: atılabilir, ama her uyarı için DONGU satırına "kalite: <uyarı> -> <tek cümle gerekçe>" yazılır. Gerekçe yazılamıyorsa düzelt.
  - Atıldıktan sonra `python3 invest/kalite.py kaydet --tur <TÜR> < metin` çalıştırılır (tekrar takibi bu kayda dayanır).

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
| Hep aynı yapı | Her tweet "haber → mekanizma → görüş" sırasıyla | Asıl metin bölüm 8: türü değiştir (veri odaklı, mekanizma odaklı, eleştirel, hipotez); açılış ve kapanış tekrarı kalite.py'de HATA; gorus.py |
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

## 6b. KURAL 62 — piyasa jargonu sıklığı (Enes 23.11 20:40)

Enes "fiyatlandı", "iskonto" ve benzeri kelimelerin çok sık kullanılmasını istemiyor. Aileler: fiyatlama (fiyatlandı/fiyatlanmış/fiyatlıyor/fiyattan çıkardı/fiyata yansıdı), iskonto, prim/risk primi, denklem, çarpan, katalizör, pozisyonlanma, konsensüs, iştah, kâr satışı, belirsizlik, ayrışma. Bir tweette en çok 1 aile ve o da 1 kez; son 6 tweette geçen aile kullanılmaz. Yerine ne olduğu düz cümleyle söylenir. `kalite.py` bunu HATA olarak yakalar. Kural 60'taki terim listesi bu kuralla sınırlıdır.

## 7. Kayıt ve öğrenme

- Her tweetten sonra `kalite.py kaydet` çalıştırılır. DONGU satırına, varsa, "kalite: ..." gerekçeleri eklenir.
- 10:15 perfogren görevi uzunluk ile görüntülenme ilişkisine bakar. Tavanlar ancak veri gösterirse DERSLER.md'de önerilir ve Enes onaylarsa değiştirilir (kalite.py SINIR). Asıl metin hiçbir zaman değiştirilmez.
- Kural değişirse hem bu skill (improvement) hem `invest/skills/enes-analiz-kalitesi.md` kopyası güncellenir.

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
* Okuyucu bu içeriği okuduktan sonra konuyu daha iyi anlayacak mı?

Bu kontrollerden geçmeyen içeriği yeniden geliştir.

TEMEL PRENSİP:

Amacın yalnızca finans haberlerini yorumlayan veya profesyonel görünen tweetler üreten bir hesap oluşturmak değil. Amacın, finansın her alanında derin araştırma yapabilen, mekanizmaları anlayan, özgün hipotezler geliştiren ve okuyucuya gerçek analitik değer sunan üst düzey bir finans araştırma ve yayıncılık standardı oluşturmaktır.

Her konuya aynı derecede yüzeysel yaklaşma. Her konuya kendi gerektirdiği uzmanlık seviyesinde yaklaş.

Konu değişebilir. Analitik kalite, araştırma disiplini ve doğruluk standardı asla düşmemelidir.

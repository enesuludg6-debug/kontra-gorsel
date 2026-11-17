---
name: "enes-bilanco-13f"
description: "Enes'in X hesabı için bilanço önizleme, bilanço rakam tweeti, 15 dk sonraki bilanço analizi ve çeyreklik 13F yatırımcı serisi hazırlanırken kullanılır."
---

# Bilanço ve 13F tweetleri

Genel tur kuralları (kontrol, kaynak, yazım, kart, paylaşım, kayıt) için `enes-tweet-turu` skill'i geçerlidir; bu skill onun üstüne bilanço ve 13F'e özel kuralları ekler. Repo `/home/claude/kontra-gorsel/invest`; ayrıntı `DEVIR_TAM.md` (bölüm 4, kesin kural 7 ve 10), kalıplar `ORNEKLER.md`.

## A. Bilanço döngüsü

Portföy (DOCN RKLB SITM AXON CBRS VRT AVGO) ve ilgi listesi (ON AAOI HOOD TEM CRDO PLTR ISRG ASTS MU + büyük yapay zekâ/yarı iletken/bulut/uzay: NVDA AMD AVGO TSM MSFT GOOGL AMZN META ORCL CRWV SNOW vb.) şirketlerinde öncesi ve sonrası KESİN atılır.

### 1. Önizleme (1 gün önce akşam ya da bilanço günü sabah)
Enes'in 17.11 NVDA isteği bu formatın örneğidir: "çok profesyonel, bilanço tahmincisi gibi, benim aklıma gelmeyen metrikleri de araştır". Tek uzun tweet (Enes flood istemezse). İçerik sırası, başlıksız akan paragraflar:
1. Bağlam cümlesi: ne zaman, neden önemli, hisse son dönemde ne yaptı.
2. Geçen çeyrek: gelir, ana segment, marj, HBK; şirketin kendi rehberini ne kadar aştı. Kaynak: şirketin 8-K/10-Q'su (SEC) + IR.
3. Bu çeyreğin şirket rehberi ve piyasa beklentisi (gelir, HBK, ana segment; Visible Alpha, LSEG, FactSet, Earnings Whispers, Zacks; en az 2 kaynak).
4. BENİM BEKLENTİM: aralıklı rakamlarla (gelir, segment, marj, HBK, sonraki çeyrek rehberi) ve dayanağı (geçmiş rehber aşım büyüklüğü, müşterilerin harcama planları, sektör verisi). Tahmin olduğu açık olsun.
5. Yönü belirleyecek eşikler: "X'in üstü güçlü mesaj, Y'nin altı yavaşlama diye okunur".
6. Çoğu kişinin bakmadığı metrikler (şirkete göre seç): müşteri dağılımı ve yoğunlaşması, alacak ve stokların gelire göre büyümesi (DSO/DIO), faaliyet gideri rehberi, yeni ürün geçişi, bölge/Çin payı ve ihracat kuralı, tedarik taahhütleri, serbest nakit ve geri alım, yönetim değişikliği ve tonu, sektöre özel KPI (bulutta backlog/RPO/güç MW, yazılımda ARR/NRR, perakendede aynı mağaza satışı ve sepet, bankada net faiz marjı).
7. Fiyatlama: hisse ne kadar düştü/yükseldi, son bilanço tepkisi, opsiyonların fiyatladığı hareket (yalnız 2 kaynak tutarlıysa).
8. Görüş cümlesi ("Bence ..." en fazla bir kez) + "rakamlar açıklandığında yayınlayacağım". Soruyla bitmez, al/sat yok.
Kart: `bento` (büyük rakam = gelir tahminim, kutular = segment/marj/HBK tahmin vs piyasa, seri = son çeyrek gelirleri + tahmin).
Tahminleri DONGU'ya yaz; tahmin tuttuysa analizde söylenebilir; tutmadıysa tweette hiç anılmaz (kural 23, yalnız doğru çıkanlar).

### 2. Rakam tweeti (açıklanır açıklanmaz, YORUMSUZ)
Enes'in $CRWV formatı (kesin kural 7):
```
$TICKER 3. ÇEYREK BİLANÇOSU
• Gelir: 3,66 Mr $ / Beklenti: 3,54 Mr $
• Hisse başı kâr: -1,24 $ / Beklenti: -1,55 $
• Düzeltilmiş faaliyet kârı: 379 Mn $ / Beklenti: 246 Mn $
• (şirkete özgü 2-3 metrik)

2026 TAHMİNİ   (ya da "4. ÇEYREK TAHMİNİ")
• Gelir: 13,2 Mr $ / Beklenti: 12,5 Mr $
• Yatırım harcaması: 38 Mr $ / Beklenti: 36 Mr $
```
- Her satır "metrik: gerçek / Beklenti: X". Terimler Türkçe ve sade.
- KAYNAK İSTİSNASI (ONAYLANDI, Enes 17.11 12:58): bilanço RAKAM tweetinde şirketin kendi resmi bülteni (IR sayfası, GlobeNewswire/Business Wire/PR Newswire, SEC 8-K) tek başına yeterli kaynaktır; ikinci kaynak beklenmez. Beklenti rakamları önceden 2 kaynakla doğrulanmış olur. Yayından sonra 10 dk içinde ikinci kaynakla (Reuters/CNBC/Benzinga) teyit; fark varsa Enes'e hemen söyle, gerekirse düzeltme tweeti. Bu istisna YALNIZ bilanço rakam tweeti içindir; analiz ve diğer tüm tweetlerde 2 kaynak kuralı aynen geçerli.
- Kart `skor(ticker, etiket, baslik, [(metrik, beklenti, gerçek, ok)], sonuc, kaynak, out)` ya da `terminal`.
- Açıklama saatini önceden bil; gece 01:00-09:00 arasına düşen bilinen açıklama için ayrı tek seferlik tur kurulur (gece istisnası).
- Mali yıl takvim yılından farklı olabilir (NVDA, TSN): çeyrek adını şirketin mali yılına göre yaz ve kontrol et.

### 3. Kapsamlı analiz (rakam tweetinden 15 dk sonra)
- Sayfanın stiline uyan hisselerde (portföy, ilgi listesi, yapay zekâ/yarı iletken/bulut/uzay/büyük teknoloji) rakam tweetinin hemen ardından `send_later` ile 15 dk sonrasına tek seferlik tur kur; bu otomatik zinciri değiştirmez.
- İçerik: ne iyi, ne kötü, rehber neden önemli, okuyucunun aklındaki soruya cevap ("organik mi, tek seferlik mi, düzeltince ne kalıyor": ne kadar olduğunu 2 kaynakla bul), önizlemedeki tahminlerle kıyas, hisse tepkisi, net görüş. Kart: bento/uclu/panel.
- Bilanço açıklayan portföy hissesinin temel karnesi aynı gün yenilenir (`enes-portfoy-analiz`).

### 4. Takvim ve HIZ PROTOKOLÜ (kesin kural 16, 17.11; Enes: "bulamadın, sonra açıklandı, sonraki tur 5 dk sonra, geç paylaşırız, tweetin değeri kaybolur, bizden önce başkaları paylaşır")
- `invest/takvim.md`: her Pazar 20:00 (sabit görev) gelecek 7 gün, her gün 09:05 ve 10:30 key levels tweetinde güncellenir. Kapsam: portföy, ilgi listesi, büyük yapay zekâ/yarı iletken/bulut/uzay/büyük teknoloji ve piyasayı oynatacak diğerleri (HD, WMT, TGT, DIS, büyük bankalar) + Fed kararı, TÜFE, istihdam, perakende satışlar, FOMC notları, büyük konuşmalar. Her satır: tarih, AÇIKLAMA SAATİ TSİ (IR duyurusu ya da önceki çeyreklerin dakikası; belirsizse "tahmini"), beklenti (2 kaynak), bülten kaynağı URL'si. ABD kış saatinde TSİ = ET + 8 saat.
- Takvime yazılan HER olay için iki tek seferlik görev hemen kurulur (gece 01:00-09:00 dahil):
  a) HAZIRLIK, T-45/60 dk: beklentileri son kez 2 kaynakla doğrula; tweet iskeletini (CRWV formatı, gerçek rakam alanları boş) ve skor kartı kodunu `/tmp/hazir_<ticker>.py` olarak hazır yaz; bülten URL'lerini hazırla; DONGU'ya `HAZIR: <ticker>`.
  b) YAYIN, T-2 dk: en çok 30 dk boyunca 45-60 sn arayla bülten kaynaklarını kontrol et (WebFetch şirket IR haber sayfası / GlobeNewswire / Business Wire / PR Newswire şirket sayfası; WebSearch "<şirket> reports third quarter results"; Yahoo chart `includePrePost=true` ile mesai dışı fiyatta ani sıçrama = açıklama işareti). Bülten bulununca rakamları BÜLTENDEN al (tek kaynak yeterli, yukarıdaki istisna), hazır karta gir, Read ile tek bakış, push, raw URL 200, Buffer shareNow. HEDEF: bülten çıktıktan sonra 3-5 dk içinde yayında. Sonra 10 dk içinde ikinci kaynak teyidi ve 15 dk sonrasına analiz turu.
- Yayın turu otomatik zincirden bağımsızdır, 20 dk kuralına takılmaz; bekleyen otomatik tur yayına ±15 dk denk geliyorsa `update_trigger` ile yayından 20+ dk sonraya kaydırılır.
- Bilanço ve saati belli veri başlıklarında `enes-tweet-turu` bölüm 9'daki "+3 dk tek seferlik tur" yerine bu protokol uygulanır.
- Konferans görüşmesinde rehber değişikliği ya da önemli söz çıkarsa ayrı kısa tweet.

## B. 13F serisi (kesin kural 10)

- Ne zaman: her çeyreğin 13F son gününden sonraki ilk turlarda Enes'e SORMADAN başlar: yaklaşık 14-17 Şubat, 15-18 Mayıs, 14-17 Ağustos, 14-17 Kasım (tatil/hafta sonu ise sonraki iş günü).
- Her otomatik turda 1 kişi, her kişi ayrı tweet; seri o günlerde öncelikli konu, son dakika ve bilanço araya girer.
- Liste (öncelik: en çok merak edilen ve en büyük değişiklik önce): Berkshire Hathaway (Greg Abel), Pershing Square (Bill Ackman), Duquesne (Stanley Druckenmiller), Appaloosa (David Tepper), Soros Fund Management, Third Point (Dan Loeb), Greenlight (David Einhorn), Coatue, Tiger Global, Baupost (Seth Klarman), Himalaya (Li Lu), Pabrai, Icahn, Bridgewater, Lone Pine, Viking + gündemdeki diğerleri. Scion/Michael Burry 10.11.2025'te SEC kaydını sildi, 13F vermiyor: listeden çıkarıldı.
- İçerik: yeni pozisyonlar, tamamen çıkılanlar, en büyük artırma ve azaltmalar (hisse adedi, değer, portföy payı), portföy değeri. Tablo değil düz metin + kart.
- Görüş zorunlu, etiketsiz ("Benim okumam:" yok): hareketin olası mantığı, kişinin bilinen tarzı, piyasa bağlamı, önceki 13F'lerle ortak tema (17.11 serisi temaları: bellek/depolama, Nvidia'da ayrışma, 13F gecikmesi). Gerekirse etiketsiz tek cümle: "Tablo 30 Eylül itibarıyla, sonrasındaki işlemler dosyada yok." 13F yalnız ABD uzun pozisyonlarını gösterir; açığa satış ve yabancı hisseler yok, opsiyonlar dayanak değeriyle görünür.
- "X aldı, siz de alın" dili yok.
- Doğrulama: EDGAR 13F-HR (birincil; sec.gov izin isterse 13f.info EDGAR aynası) + en az 1 haber/izleme kaynağı (mlq.ai, FourWeekMBA, GuruFocus, StockHub, 24/7 Wall St, CNBC, Reuters, Bloomberg, WhaleWisdom, Dataroma, HedgeFollow, Fintel, Valuesider). Aynı yazının başka sitedeki kopyası ikinci kaynak sayılmaz. Tek kaynaklı rakam ve isim atılmaz (rakamsız yön verilebilir), Enes'e "Ne anlama geliyor?"da söylenir. Çeyrek/yıl kontrolü şart (geçen yılın aynı çeyreği sık karışır). Pozisyon değerleri çeyrek sonu fiyatıyladır.
- Kart: panel, bento, uclu, dortlu, ilerleme, editoryal, siralama (son 3'ü tekrar etme).
- Enes'in portföy hisselerinde büyük yatırımcı hareketi varsa (tek kaynaklı bile olsa) Enes'e ayrıca not: ne oldu, doğrulandı mı, "ben olsam" etkisi.
- DONGU: `- 13F SERİSİ: <isim> atıldı / sıradaki: <isim>`. Seri bitince Enes'e kısa özet: kim ne yaptı, ortak temalar.
- `ORNEKLER.md` bölüm 19 kalıbı: [fon + çeyrek] → [en dikkat çekici hareket, rakamla] → [diğer 1-3 hareket] → [görüş: tarz ve piyasayla bağ] → [gerekirse 13F sınırı].
## Kural 22 eklemeleri (17.11 14:35)

- Önizleme tweetine opsiyon piyasasının beklediği hareket (±%X; Barchart / Market Chameleon / OptionCharts + haber, 2 kaynak). Ertesi gün açılıştan sonraki ilk turda "beklenen ±%X, gerçekleşen %Y" (BEKLENEN-HAREKET, şablon 5).
- Portföy ve ilgi listesi bilançolarında analiz tweeti ya da sonraki tur en yakın rakiple panel/dortlu kart (RAKIP, şablon 6; büyüme, brüt marj, ileri F/K, tahmin).
- Bilanço sezonu karnesi: Pazar 14:25 sabit görev; raporlayan oran ilk kez %50 ve %90'ı geçince (SEZON-KARNESI, şablon 19).
- 13F serisi bitince sonraki turda 13F-OZET (şablon 20): en az 3 yatırımcının ortak aldığı/sattığı hisseler.
- Yalnız doğru çıkanlar (kural 23); yanlış rakamda kural 21 düzeltme.

- PERİYOT DEFTERİ (kural 24): 13F çeyrek özeti, sezon karnesi eşikleri `python3 periyot.py kontrol 13f_ozet|sezon_karnesi_50|sezon_karnesi_90`; yapılınca `yap`.

## Kural 25 ve 36 eklemeleri (17.11)
- Rakam tweeti yorumsuz kalır; 15 dk sonraki ANALİZ kural 25'e göre şu soruları cevaplar: ne demek (sade), büyük resim (sektör/yapay zekâ zinciri), faiz/Fed bağlamı gerekiyorsa, piyasaya ve ilgili hisselere etkisi, net düşüncemiz. Etiketli giriş ve paragraf başında "X şu:" yok.
- YAYIN ÖNCELİĞİ (kural 36d): tek oturum sırayla çalışır; bilanço/veri yayını 60 dk içindeyse ağır görevler (teknik analiz, karne, uzun yazı) yayından 15 dk önce bitecek şekilde kısaltılır. Hazırlık/yayın/analiz görevleri bu sohbette send_later (kural 29).
- Bugünlük adet kuralı varsa kayit.py `--hak ayrilan` ile sayaç düşer; blok yalnız kendi tarihinde geçerli (paylaşım günü 01:00'de biter).

## Opsiyon beklenen hareket güvencesi (kesin kural 39)
OPSİYON BEKLENEN HAREKET GÜVENCESİ (kural 22n eki, Enes 17.11 23:47: "opsiyon piyasası tahminleri vardı, Nvidia için paylaştın mı, paylaşmadıysan neden, sistemdeki sıkıntıyı çöz").
- Sorun: 22n kuralı 14:35'te geldi, NVDA önizlemesi 12:22'de çıkmıştı; opsiyon verisi ancak 21:07 bağlam tweetinde girdi. Kural "önizlemeye ekle" diyordu ama önizleme zaten çıktıysa ne olacağı ve kontrol eden bir adım yoktu; ertesi gün kıyas görevi de yalnız yayın görevinin içinde kurulacaktı (yayın aksarsa kaybolur).
- Çözüm: (a) Takvimdeki her bilanço (portföy, ilgi listesi, büyük isimler, piyasayı oynatan TGT/WMT/HD vb.) için açıklamadan ÖNCE en az bir tweette opsiyonların fiyatladığı hareket (±% ve mümkünse dolar karşılığı, 2 kaynak) yer alır: önizleme varsa onda; önizleme önceden çıktıysa ya da yoksa günün başlıkları (10:30) / bağlam tweeti / ayrı kısa tweette. Atılınca DONGU'ya "- OPSIYON: <T> ±%X (kaynaklar)" satırı. (b) `tur_basi.sh` bugün ve yarın bilançosu olup DONGU'da OPSIYON satırı olmayanları "EKSİK OPSİYON" diye yazar; ilk uygun tur onu tamamlar. (c) Hazırlık görevi (T-60) OPSIYON satırını kontrol eder; yoksa veriyi bulur, Enes'e yazar ve yayından önce kalan tur/tweet ile atılmasını sağlar. (d) Ertesi gün "Beklenen hareket: <T>" kıyas görevi HAZIRLIK görevinde kurulur (yayın görevine bırakılmaz); kıyasta yalnız gerçek hareket ile opsiyon fiyatlaması karşılaştırılır (kural 23: kendi tutmayan tahminlerimiz anılmaz).

## Bilanço görüşmesi tweetleri (kesin kural 40)
BİLANÇO GÖRÜŞMESİ (KAZANÇ ÇAĞRISI) TWEETLERİ (kesin kural 40, Enes 18.11 00:31: "bilanço açılış öncesi açıklandıysa aynı gün, kapanışta açıklandıysa bir sonraki gün bilançonun kazanç çağrılarını dinleyeceksin ya da transkriptine ulaşacaksın ve onunla alakalı önemli yerleri tweet atacaksın; birkaç önemli yer varsa hepsini ayrı ayrı tweetlere böl, tek tweete hepsini atma").
- Kapsam: bilanço döngüsündeki bütün şirketler (portföy, ilgi listesi, büyük yapay zekâ/yarı iletken/bulut/uzay/teknoloji, piyasayı oynatan perakende/banka vb.).
- Zaman: açılış öncesi açıklanan bilançoda AYNI GÜN (görüşme bitip transkript çıkınca, genelde görüşmeden 1-3 saat sonra); kapanış sonrası açıklananda ERTESİ GÜN (sabah 11:00-12:30 arası, transkript hazır olur).
- Kaynak: transkript (şirket IR webcast/transkript, Motley Fool, Seeking Alpha, Investing, Yahoo, Quartr) + en az 1 haber (Reuters, CNBC, Bloomberg, Barron's). Her rakam ve iddia 2 kaynak; tek kaynaktaki söz tweete girmez, Enes'e not.
- İçerik: görüşmenin rakam tweetinde OLMAYAN önemli yerleri: rehberin dayanağı, talep/sipariş/backlog yorumu, marj açıklaması, yeni ürün/geçiş takvimi, müşteri yoğunlaşması, Çin/ihracat, sermaye harcaması ve geri alım, yönetim değişikliği, analist sorularında öne çıkan konu. Her önemli konu AYRI TWEET (2-4 tweet; tek konu varsa tek tweet). Her tweet: ne dendi (yönetimin sözünü kendi cümlemizle aktar; doğrudan alıntı en çok 1 kısa ifade, 15 kelimeden az) + ne demek + etkisi + net düşüncemiz (kural 25). Etiketli giriş, "X şu:", deyim yok.
- Sıra ve aralık: en önemli konu ilk; tweetler arasında 20-30 dk (send_later zinciri, aynı görev adı + sıra no). Bu tweetler Enes isteğidir, günlük tweet sınırına takılmaz ama 18-21 dilimine düşerse 21:00 sonrasına kaydırılır.
- NETLEŞTİRME (Enes 18.11 01:05): "ertesi gün" = TSİ ile bilançonun açıklandığı gecenin SABAHI. Ör. Nvidia 00:10-00:20 TSİ açıkladı, görüşme 01:00 → görüşme tweetleri aynı sabah (09:30-12:00 arası; transkript hazır olunca). Açılış öncesi bilançoda görüşme tweetleri aynı gün, görüşmeden sonra.
- Kurulum: bilançonun YAYIN görevi (rakam tweetinden sonra) ya da 10:30 günün başlıkları görevi "Çağrı: <T>" send_later görevini kurar (aynı ad varsa kurma). DONGU'ya her tweet için "- CAGRI: <T> <konu>"; `tur_basi.sh` dün/bugün bilançosu olup CAGRI satırı olmayanları "EKSİK CAGRI" diye yazar.

## Bilanço detay tweetleri (kesin kural 41)
BİLANÇO DETAY TWEETLERİ (kesin kural 41, Enes 18.11 00:57: "insanlar bilançolardan sonra bilançonun detaylarıyla ilgili böyle şeyler paylaşıyor, senin de benzerlerini her bilançodan sonra paylaşmanı istiyorum; en az iki, en fazla yedi, ne kadar önemli şey bulursan o kadar; illa bu örnekler gibi olmak zorunda değil, farklı şeyler bulup farklı şekillerde de yapabilirsin").
- NE: rakam tweetinin (yorumsuz) ve 15 dk sonraki analizin ÖTESİNDE, bilançonun içinden çıkan, çoğu kişinin bakmadığı somut detaylar. Kaynak belgeler: basın bülteninin tabloları, CFO yorumu (CFO commentary), 10-Q/10-K, yatırımcı sunumu slaytları, segment tabloları, nakit akış tablosu, bilanço (varlık/borç), taahhütler dipnotu, müşteri yoğunlaşması notu, rehber dipnotları.
- ÖRNEK TÜRLER (17.11 Nvidia örnekleri + daha fazlası; her bilançoda şirkete göre seç, hep aynı türleri kullanma): (1) taahhütler/sipariş defteri değişimi (Nvidia: tedarik taahhütleri 279 → 390 Mr $, toplam 366 → 518 Mr $, çoğu çok yıllık bellek alımı); (2) serbest nakit akışı ve nakit dönüşümü (çeyreklik sıçrama, analist yıllık tahmin serisi); (3) müşteri grubu/segment kırılımı ve yıllık değişim (Nvidia slaytı: büyük bulut 35,1 → 60,1; yapay zekâ bulutları, sanayi ve kurumsal 16,1 → 47,5 Mr $); (4) koşullu/riskli anlaşmalar (Nvidia: neo-bulut koşullu anlaşmaları 36 → 32 Mr $); (5) yeni ürün geçiş hızı ve yönetimin yazılı ifadesi; (6) marj köprüsü (neden düştü/arttı), faaliyet gideri rehberi; (7) alacak, stok, tedarik günleri; (8) geri alım, temettü, nakit/borç; (9) coğrafya/Çin payı; (10) en büyük müşteri payları (%10 üstü müşteriler); (11) rehberin içindeki takvim etkisi (ekstra hafta gibi); (12) önceki çeyrek rehberine göre aşım geçmişi; (13) hisse bazlı ödeme ve seyrelme; (14) şirkete özgü KPI tablosu (backlog, RPO, ARR, NRR, aynı mağaza satışı, sepet, trafik vb.).
- KAÇ TANE: en az 2, en çok 7; sayıyı önem belirler (az ama güçlü olan iyi). Her detay AYRI TWEET. Kural 40 görüşme tweetleriyle aynı konuyu tekrar etme (detaylar belgeden, görüşme tweetleri yönetimin sözlerinden).
- NASIL: her tweet kendi kartıyla (rakamı gösteren grafik: iki dönem çubuk, seri, kırılım; slayt/tablo görüntüsü KOPYALANMAZ, kendi kartımız çizilir) + kural 25 (ne demek, neden önemli, büyük resim, hisselere/zincire etkisi, net düşünce). İlk satır durdurmalı (rakam ya da tezat). Etiketli giriş, "X şu:", deyim, emoji, hashtag yok; X'teki başka hesapların tweeti kopyalanmaz/çevrilmez, kendi cümlemizle ve kendi açımızla.
- KAYNAK: şirketin kendi resmi belgesinden (bülten, CFO yorumu, 10-Q, sunum, SEC) doğrudan okunan rakam tek başına yeterli (kural 16 gibi; belge adı kartın kaynak satırında). Belgeye ulaşılamaz ve rakam yalnız ikinci elden (X görüntüsü, haber) geliyorsa en az 2 bağımsız kaynak. Enes'in ilettiği belge görüntüsü belge sayılır ama yine bir haber/ikinci platformla teyit edilir. Analist tahmini serileri (ör. Fiscal.ai FCF tahminleri) tahmin olduğu açıkça yazılarak ve 2 kaynakla.
- ZAMAN: rakam ve analiz tweetlerinden hemen sonra, belgeler ulaşılabilir olduğu anda (gece de dahil, bekleme yok).
- NETLEŞTİRME (Enes 18.11 01:05): detay tweetleri için BEKLEME YOK. Bilanço ne zaman açıklanırsa açıklansın, belgeler (bülten, CFO yorumu, sunum, 10-Q) ulaşılabilir olduğu anda analiz tweetinden sonra başlar; gece bilançolarında da 01:00-09:00 paylaşım yasağı bu tweetler için UYGULANMAZ (kural 16 gece istisnası gibi). Tweetler arası aralık serbest (kural 42). Ertesi sabaha bırakılmaz. Tweetler arası aralık serbest (kural 42); 18:00-21:00 dilimine düşen 21:00 sonrasına kayar; görüşme tweetleriyle (kural 40) sırayla ve iç içe değil.
- KURULUM: bilançonun YAYIN görevi (ya da 10:30 günün başlıkları görevi) "Detay: <T>" send_later görevini kurar (aynı ad varsa kurma); görev ilk tweeti atar, kalanları "Detay: <T> (2)" ... zinciriyle kurar ve her mesaja taslak + kaynak yazar. DONGU'ya her tweet için "- DETAY: <T> <konu>"; `tur_basi.sh` dün/bugün bilançosu olup DETAY satırı 2'den az olanları "EKSİK DETAY" diye yazar. Bu tweetler Enes isteğidir; günlük tweet sınırına takılmaz.

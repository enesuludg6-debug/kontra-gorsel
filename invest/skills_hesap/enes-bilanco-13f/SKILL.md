---
name: "enes-bilanco-13f"
description: "Enes'in X hesabı için bilanço önizleme, bilanço rakam tweeti, 15 dk sonraki bilanço analizi, bilanço detay ve görüşme tweetleri ve çeyreklik 13F yatırımcı serisi hazırlanırken kullanılır."
---

# Bilanço ve 13F tweetleri

> **23.11.2026 GÜNCELLEMESİ (ÖNCE BUNU UYGULA):** Bu skill ile yazılan her içerik `enes-analiz-kalitesi` skill'ine (kural 61-65) ve `invest/KURAL_DIZINI.md`'ye uyar. Bilanço için uygun kalıplar: G beklenti farkı (beklenen ve gelen rakam yan yana; hisse rakama değil beklentiye tepki verir), I nakit ve sermaye izi (serbest nakit, yatırım harcaması/gelir, seyrelme), M sonraki tarih, D/K değer hesabı ve tersine hesap; birleşme/satın almada D birleşme farkı (teklif oranı × alıcının fiyatı ile hedefin fiyatı arasındaki fark). Bilanço RAKAM tweeti (BILANCO-RAKAM) kalıp zorunluluğundan muaftır ve hızlı moddadır; derinlik 15 dk sonraki BILANCO-ANALIZ tweetine (tavan 1.200 karakter, en az bir ikinci katman veri, kural 65). Kapanış "bilançoda ilk bakacağım satır" gibi rapor diliyle ya da her seferinde "takip edeceğim" ile kurulmaz (64, 64-B); verinin vardığı sonuçla biter. Bir turda 2 bilanço tweeti varsa ikincisi Buffer'da ~12 dk sonraya zamanlanır.

Genel tur kuralları (kontrol, kaynak, yazım, kart, paylaşım, kayıt) için `enes-tweet-turu` skill'i geçerlidir; bu skill onun üstüne bilanço ve 13F'e özel kuralları ekler. Repo `/home/claude/kontra-gorsel/invest`; ayrıntı `DEVIR_TAM.md` (bölüm 4, kesin kural 7 ve 10), kalıplar `ORNEKLER.md`.

## A. Bilanço döngüsü

- KONU FİLTRESİ (kesin kural 46, Enes 18.11 17:12): bilanço önizleme, rakam, analiz, detay ve görüşme tweetleri yalnız yapay zekâ, uzay ve Nasdaq/büyük teknoloji şirketleri için. Perakende/tüketim, banka, sanayi, ilaç bilançoları için görev kurulmaz, tweet atılmaz.

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
- DERİNLİK VE KAYNAK: analiz kesin kural 45'e göre ÇOK DETAYLI ve ÇOK KAYNAKLI yazılır (10-15 paragraf, en az 6 kaynak / 4 tür, 13 maddelik sıra); ayrıntı bu skill'in sonundaki "Detaylı analiz yazısı" bölümünde. Veri toplanamadıysa analiz en geç 45 dk'ya kayar.
- Bilanço açıklayan portföy hissesinin temel karnesi aynı gün yenilenir (`enes-portfoy-analiz`).

### 4. Takvim ve HIZ PROTOKOLÜ (kesin kural 16, 17.11; Enes: "bulamadın, sonra açıklandı, sonraki tur 5 dk sonra, geç paylaşırız, tweetin değeri kaybolur, bizden önce başkaları paylaşır")
- `invest/takvim.md`: her Pazar 20:00 (sabit görev) gelecek 7 gün, her gün 09:05 ve 10:30 key levels tweetinde güncellenir. Kapsam: portföy, ilgi listesi, büyük yapay zekâ/yarı iletken/bulut/uzay/büyük teknoloji ve piyasayı oynatacak diğerleri (HD, WMT, TGT, DIS, büyük bankalar) + Fed kararı, TÜFE, istihdam, perakende satışlar, FOMC notları, büyük konuşmalar. Her satır: tarih, AÇIKLAMA SAATİ TSİ (IR duyurusu ya da önceki çeyreklerin dakikası; belirsizse "tahmini"), beklenti (2 kaynak), bülten kaynağı URL'si. ABD kış saatinde TSİ = ET + 8 saat.
- Takvime yazılan HER olay için iki tek seferlik görev hemen kurulur (gece 01:00-09:00 dahil):
  a) HAZIRLIK, T-45/60 dk: beklentileri son kez 2 kaynakla doğrula; tweet iskeletini (CRWV formatı, gerçek rakam alanları boş) ve skor kartı kodunu `/tmp/hazir_<ticker>.py` olarak hazır yaz; bülten URL'lerini hazırla; DONGU'ya `HAZIR: <ticker>`.
  b) YAYIN, T-2 dk: en çok 30 dk boyunca 45-60 sn arayla bülten kaynaklarını kontrol et (WebFetch şirket IR haber sayfası / GlobeNewswire / Business Wire / PR Newswire şirket sayfası; WebSearch "<şirket> reports third quarter results"; Yahoo chart `includePrePost=true` ile mesai dışı fiyatta ani sıçrama = açıklama işareti). Bülten bulununca rakamları BÜLTENDEN al (tek kaynak yeterli, yukarıdaki istisna), hazır karta gir, Read ile tek bakış, push, raw URL 200, Buffer shareNow. HEDEF: bülten çıktıktan sonra 3-5 dk içinde yayında. Sonra 10 dk içinde ikinci kaynak teyidi ve 15 dk sonrasına analiz turu.
- Yayın turu otomatik zincirden bağımsızdır, 20 dk kuralına takılmaz; bekleyen otomatik tur yayına ±15 dk denk geliyorsa `update_trigger` ile yayından 20+ dk sonraya kaydırılır.
- Bilanço ve saati belli veri başlıklarında `enes-tweet-turu` bölüm 9'daki "+3 dk tek seferlik tur" yerine bu protokol uygulanır.
- Konferans görüşmesinde rehber değişikliği ya da önemli söz çıkarsa ayrı kısa tweet.

## KURAL 67 — Bilanço başına tweet tavanı (Enes 24.11 09:47: "bilanço başına en fazla 6 twit hakkın olsun")
- Bir bilanço için toplam EN FAZLA 6 tweet: beklenti, opsiyon, rakam, analiz, detay, görüşme (çağrı), beklenen hareket hepsi bu 6'ya dahil. Eski "en çok 2 tweet + beklenti" sınırı geçersiz.
- 6 tavandır, hedef değil: detay ve çağrı tweetleri yalnız gerçekten yeni bilgi varsa atılır. Sayaç: DONGU'daki o tickerın bilanço satırları.

## KURAL 70 — Bilanço hak dağılımı veriyle (F-002, Enes 24.11 09:53 kabul)
- Bilanço tweetleri performans_veri.csv `tur` alanına şu etiketlerle yazılır: BILANCO-BEKLENTI, BILANCO-RAKAM, BILANCO-ANALIZ, BILANCO-DETAY, BILANCO-CAGRI, BILANCO-HAREKET (kayit.py --tur ile).
- perfogren her gün `python3 invest/bilanco_perf.py --gun 30` çalıştırır; her türde en az 3 olgun tweet olunca zayıf türün 1 hakkı güçlü türe kaydırılır. BEKLENTI, RAKAM, ANALIZ en az 1 kalır; kaydırılan hak güçlü türün ikinci tweeti olur. Dağılım DURUM.md İÇERİK AYARI 'BILANCO DAGILIM' satırında; bilanço görevleri oradan okur. Toplam yine en fazla 6.

## KURAL 71 — Beklenti tweetinde belirleyici kalem (F-003, Enes 24.11 09:53 kabul)
- Kural 49 beklenti tweeti rakamlardan sonra TEK cümleyle o çeyreği belirleyecek kalemi ve eşiğini ya da iki dalını yazar. Örnek: "Bu çeyrekte belirleyici kalem brüt marj: gelir beklentiyi geçip marj gerilerse sipariş defteri kâra aynı oranda dönmüyor demektir."
- Kalem 2 kaynaklı veriye ve şirket rehberine dayanır; mecaz yok, yasak.py temiz. Beklenti tweetinin geri kalanı yorumsuz kalır.
- Aynı anda kural 66 kaydı (skill enes-sonuc-takibi): `isler.py ekle TEST-<T>-<GGAA> ... --tur sonuctakip` ve o bilançonun ANALİZ görevine test eklenir; analiz tweeti bu testle açılır.

## B. 13F serisi (kesin kural 10)

- KURAL 46: 13F tweetinde yalnız fonun yapay zekâ / uzay / teknoloji hamleleri anlatılır; bu alanda anlamlı hamlesi olmayan fon (ör. Baupost, Pabrai, Icahn) atlanır.

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

## C. Kural 22 eklemeleri (17.11 14:35)

- Önizleme tweetine opsiyon piyasasının beklediği hareket (±%X; Barchart / Market Chameleon / OptionCharts + haber, 2 kaynak). Ertesi gün açılıştan sonraki ilk turda "beklenen ±%X, gerçekleşen %Y" (BEKLENEN-HAREKET, `invest/sablonlar.md` şablon 5).
- Portföy ve ilgi listesi bilançolarında analiz tweeti ya da sonraki tur en yakın rakiple panel/dortlu kart (RAKIP, şablon 6; büyüme, brüt marj, ileri F/K, tahmin).
- Bilanço sezonu karnesi: Pazar 14:25 sabit görev; raporlayan oran ilk kez %50 ve %90'ı geçince (SEZON-KARNESI, şablon 19).
- 13F serisi bitince sonraki turda 13F-OZET (şablon 20): en az 3 yatırımcının ortak aldığı/sattığı hisseler.
- Yalnız doğru çıkanlar (kural 23); yanlış rakamda kural 21 düzeltme.
- PERİYOT DEFTERİ (kural 24): 13F çeyrek özeti ve bilanço sezonu %50/%90 eşik tweetleri `python3 invest/periyot.py kontrol 13f_ozet|sezon_karnesi_50|sezon_karnesi_90` ile kontrol edilir; yapılınca `yap`.

## Bilanço sonrası seri: zamanlama (kural 40-41, Enes 18.11 00:57 + 01:05)
- DETAY TWEETLERİ (belgeden: bülten tabloları, CFO yorumu, 10-Q, sunum): BEKLEME YOK. Bilanço ne zaman açıklanırsa açıklansın, belgeler ulaşılabilir olduğu anda analiz tweetinden sonra başlar; gece bilançolarında 01:00-09:00 paylaşım yasağı bu tweetlere uygulanmaz. En az 2, en çok 7; her detay ayrı tweet; arası 15-25 dk. Taslaklar tek dosyada (invest/taslak/<ticker>_detay_<tarih>.md) hazırlanır, "Detay: <T>" zinciri atılmamış ilk bölümü atar. CFO yorumu SEC'de: sec.gov/Archives/edgar/data/0001045810/<accession>/q3fy27cfocommentary.htm gibi; arama sonuçlarında "CFO commentary" ile bulunur.
- Tür örnekleri: taahhütler/sipariş defteri; serbest nakit ve geri alım; müşteri/segment kırılımı; garantiler ve koşullu anlaşmalar; alacak/stok/tahsil süresi; Çin/coğrafya; marj köprüsü ve gider rehberi; rehberdeki takvim etkisi; seyrelme; şirkete özgü KPI. Her tweet kendi kartımızla (slayt kopyalanmaz) + kural 25 yorum. Şirket belgesinden doğrudan okunan rakam tek başına yeterli.
- GÖRÜŞME TWEETLERİ (yönetimin sözleri, transkript): açılış öncesi bilançoda AYNI GÜN görüşmeden sonra; kapanış sonrası (TSİ gece) bilançoda o gecenin SABAHI 09:30-12:00 (ör. Nvidia 00:20 açıkladı, görüşme 01:00 → aynı sabah). Her önemli konu ayrı tweet, 2-4 tane, detay tweetleriyle aynı konu tekrar edilmez.

## Bilanço detay tweetleri (kesin kural 41, Enes 18.11 00:57)
- Her bilançodan sonra rakam tweeti ve analizin ÖTESİNDE, bilançonun içinden çıkan ve çoğu kişinin bakmadığı somut detaylar: EN AZ 2, EN ÇOK 7, sayıyı önem belirler; HER DETAY AYRI TWEET.
- Kaynak belgeler: bülten tabloları, CFO yorumu, 10-Q/10-K, yatırımcı sunumu, segment/nakit akış/bilanço tabloları, taahhütler dipnotu, müşteri yoğunlaşması notu.
- Tür örnekleri (hep aynıları değil, şirkete göre): taahhütler/sipariş defteri değişimi; serbest nakit akışı sıçraması; müşteri grubu/segment kırılımı ve yıllık değişim; koşullu/riskli anlaşmalar; yeni ürün geçiş hızı; marj köprüsü ve gider rehberi; alacak/stok; geri alım ve nakit/borç; coğrafya/Çin; %10 üstü müşteriler; rehberdeki takvim etkisi (ekstra hafta); aşım geçmişi; seyrelme; şirkete özgü KPI tablosu.
- Her tweet kendi kartıyla (sayfa/slayt kopyalanmaz, kendi grafiğimiz) + kural 25 yorum (ne demek, neden önemli, zincire/hisselere etkisi, net düşünce). İlk satır durdurmalı; etiketli giriş, deyim, emoji yok; X'teki tweetler kopyalanmaz, kendi açımızla yazılır.
- Kaynak: şirketin kendi resmi belgesinden doğrudan okunan rakam tek başına yeterli (belge adı kartın kaynak satırında); yalnız ikinci elden gelen rakam 2 bağımsız kaynakla. Analist tahmin serileri "tahmin" diye ve 2 kaynakla.
- Zaman: gece bilançolarında ertesi sabah 09:30'dan, gün içinde analizden 30 dk sonra; tweetler arası 20-30 dk; 18-21 dilimine düşen 21:00 sonrasına kayar; görüşme tweetleriyle (kural 40) aynı konu tekrar edilmez.
- Kurulum: yayın ya da 10:30 görevi "Detay: <T>" send_later görevini kurar; ilk tweet atılır, kalanlar "Detay: <T> (2)"... zinciriyle. DONGU'ya "- DETAY: <T> <konu>"; `tur_basi.sh` "EKSİK DETAY" uyarır. Bu tweetler günlük tweet sınırına takılmaz.

## Bilanço görüşmesi tweetleri (kesin kural 40, Enes 18.11 00:31)
- Açılış öncesi açıklanan bilançoda AYNI GÜN (görüşmeden 1-3 saat sonra), kapanış sonrası açıklananda ERTESİ GÜN (11:00-12:30) kazanç çağrısı transkripti (Motley Fool, Seeking Alpha, Investing, Yahoo, Quartr, şirket IR) + en az 1 haber okunur.
- Rakam tweetinde olmayan önemli yerler (rehberin dayanağı, talep/backlog, marj, yeni ürün takvimi, müşteri yoğunlaşması, Çin, sermaye dağıtımı, yönetim, analist sorularında öne çıkan konu) HER KONU AYRI TWEET (2-4; en önemlisi ilk, kalanlar 20-30 dk arayla send_later). Tek tweete hepsi konmaz.
- Her tweet kural 25 (ne dendi kendi cümlemizle, ne demek, etkisi, net düşünce), 2 kaynak, doğrudan alıntı en çok 1 kısa ifade, etiketli giriş ve deyim yok.
- Yayın görevi ya da 10:30 görevi "Çağrı: <T>" görevini kurar; DONGU'ya "- CAGRI: <T> <konu>"; `tur_basi.sh` "EKSİK CAGRI" uyarır.

## Rakam tweeti formatı (O-011, Enes 18.11 00:24)
- Bilanço rakam tweeti CRWV formatından asla eksik çıkmaz (gelir, HBK, şirkete özgü 2-3 metrik, "X. ÇEYREK TAHMİNİ"). Bülten açılamazsa ilk bakılacak yer Yahoo Finance canlı blogu ve CNBC; tek kaynakta kalan satır 2-3 dk içinde teyit edilip tam format atılır, yerine başka satır konmaz.

## Opsiyon beklenen hareket güvencesi (kesin kural 39, Enes 17.11 23:47)
- Takvimdeki her bilanço için açıklamadan ÖNCE en az bir tweette opsiyonların fiyatladığı hareket (±%, mümkünse dolar karşılığı, 2 kaynak) yer alır: önizlemede; önizleme önceden çıktıysa ya da yoksa günün başlıkları (10:30), bağlam tweeti ya da ayrı kısa tweet. Atılınca DONGU'ya "- OPSIYON: <T> ±%X (kaynaklar)".
- `tur_basi.sh` bugün/yarın bilançosu olup OPSIYON satırı olmayanları "EKSİK OPSİYON" diye yazar; ilk uygun tur tamamlar.
- HAZIRLIK görevi (T-60) OPSIYON satırını kontrol eder ve ertesi gün 17:45 "Beklenen hareket: <T>" kıyas görevini kurar (yayın görevine bırakılmaz; aynı ad varsa kurulmaz). Kıyasta gerçek hareket opsiyon fiyatlamasıyla karşılaştırılır; kendi tutmayan tahminlerimiz anılmaz (kural 23).

## Kural 25, 29 ve 36 eklemeleri (17.11)
- Rakam tweeti yorumsuz kalır; 15 dk sonraki ANALİZ kural 25'e göre şu soruları cevaplar: ne demek (sade), büyük resim (sektör/yapay zekâ zinciri), faiz/Fed bağlamı gerekiyorsa, piyasaya ve ilgili hisselere etkisi, net düşüncemiz. Etiketli giriş, paragraf başında "X şu:" ve deyim yok.
- Hazırlık, yayın, analiz ve beklenen hareket görevleri bu sohbette send_later (kural 29); mesaj "HESAP=A ..." ile başlar.
- YAYIN ÖNCELİĞİ (kural 36): tek oturum sırayla çalışır; yayın 60 dk içindeyse ağır görevler yayından 15 dk önce bitecek şekilde kısaltılır.
- Kayıt `CS=<oturum> python3 invest/kayit.py ... --hak ayrilan`; bugünlük adet bloğu yalnız kendi tarihinde geçerli (paylaşım günü 01:00'de biter).

## Detaylı analiz yazısı (kesin kural 45, Enes 18.11 07:40: "hisse analizi veya bilanço sonrası analiz yazılarımız çok çok daha detaylı olmalı ... çok detaylı çok kaynaklı")
KAPSAM: bilanço sonrası ANALİZ tweeti ve bir hisse üzerine her analiz/uzun görüş yazısı. (Yorumsuz rakam tweeti, detay ve görüşme tweetleri kendi kurallarıyla kalır.)
- UZUNLUK: tek uzun tweet, 10-15 kısa paragraf (yaklaşık 2000-4000 karakter). Kısa, yüzeysel analiz atılmaz; veri toplanamadıysa analiz 15 dk yerine en geç 45 dk'ya kayar, aceleye getirilmez.
- KAYNAK: en az 6 bağımsız kaynak, en az 4 farklı türden: (1) şirket belgesi (bülten tabloları, 8-K/10-Q, yatırımcı sunumu, CFO yorumu), (2) görüşme transkripti ya da canlı özeti (görüşme bitmediyse atlanır), (3) en az 2 haber kuruluşu (Reuters, CNBC, Bloomberg, AP, WSJ, FT, Barron's), (4) analist tepkisi (en az 2 kurumun not/hedef değişikliği: TheFly, StreetInsider, MarketBeat, Benzinga, TipRanks), (5) konsensüs/veri sitesi (LSEG, Zacks, FactSet, StockAnalysis, Yahoo), (6) gerekiyorsa sektör/rakip kaynağı. Her rakam yine 2 kaynak; tek kaynak tweete girmez. DONGU satırına kaynakların tamamı yazılır; Enes'e mesajda kaynak listesi (link) verilir.
- İÇERİK SIRASI (etiketsiz, düz paragraflar; veri yoksa o paragraf atlanır, uydurma yok):
  1. Açılış: tek cümlelik net tespit (rakam ya da tezat).
  2. Beklenti ve gerçek: gelir, hisse başı kâr ve şirkete özgü 2-3 ana KPI; önceki çeyrek ve geçen yılın aynı çeyreğiyle.
  3. Büyümenin kaynağı: segment/ürün/coğrafya kırılımı, organik ve satın alma payı, fiyat ve hacim, tek seferlik kalemler, düzeltilmiş ile GAAP farkı.
  4. Marjlar: brüt ve faaliyet marjı, neden değişti (maliyet kalemleri, karışım, ölçek).
  5. Nakit ve bilanço: serbest nakit akışı, yatırım harcaması, nakit/borç, geri alım ve temettü, stok ve alacak değişimi.
  6. Rehber: şirketin tahmini ile beklenti, ima ettiği büyüme ve marj, değişikliğin sebebi.
  7. Yönetimin sözü: bülten ve (bittiyse) görüşmeden en önemli 2-3 nokta; görüşme tweetleriyle aynı cümleyi tekrar etmez.
  8. Analist tepkisi: kaç kurum hedef/not değiştirdi, yön ve ortalama, öne çıkan gerekçe.
  9. Hisse tepkisi: ilk tepki, opsiyonların fiyatladığı hareketle kıyas, son 4 çeyreğin bilanço tepkileri.
  10. Değerleme: ileri F/K ya da EV/satış (şirkete uygun olan), kendi 3-5 yıllık geçmişine ve 2-3 rakibe göre ("kendi geçmişine göre yüksek/düşük"; ucuz/pahalı ve hedef fiyat yok).
  11. Rakip ve zincir etkisi: rakipler, tedarikçiler, müşteriler, sektör için ne söylüyor.
  12. Riskler ve izlenecekler: sonraki çeyrekte bakılacak 2-3 somut KPI/eşik.
  13. Net görüş (kural 25): ne demek, büyük resim, gerekiyorsa faiz/Fed, piyasaya etkisi, bizim düşüncemiz.
- BİLANÇO DIŞI HİSSE ANALİZİ: aynı derinlik; 2-3. maddelerin yerine iş modeli + son 4-8 çeyrek trendi, ayrıca içeriden alım/satım, kurumsal sahiplik (13F) ve katalizör takvimi.
- GÖNDERMEDEN ÖNCE KONTROL: 13 maddeden en az 10'u var mı, kaynak ≥6 ve tür ≥4 mü, her rakam 2 kaynaklı mı, yasak kalıp (etiketli giriş, al/sat, emoji, soru ile bitiş) var mı. Eksikse tamamla, sonra at.
- Kart: panel/bento/uclu (son 3 düzen kuralı); kartta en önemli 3-4 rakam.
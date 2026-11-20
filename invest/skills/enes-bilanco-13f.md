---
name: "enes-bilanco-13f"
description: "Enes'in X hesabı için bilanço önizleme, bilanço rakam tweeti, 15 dk sonraki bilanço analizi ve çeyreklik 13F yatırımcı serisi hazırlanırken kullanılır."
---

## !!! KESİN KURAL 50 (Enes 19.11 13:01: "tweetlere daha fazla yorum ekle, bilançoyu beğendiysem beğendim de, beğenmediysem beğenmedim de, haberlere bence bunu yapmaları şu yüzden iyi vs de, ama daha çok arttır, insanlar benden yorum düşünce bekliyor"): HER tweette net, birinci tekil kişi görüş ZORUNLU ve ağırlığı artır. Bilanço rakam/analiz/detay/çağrı tweetlerinde açık hüküm: "Bilançoyu beğendim / beğenmedim / karışık buldum" + neden (2-3 somut gerekçe) + neyi izleyeceğim. Haber tweetlerinde: "Bence bu hamle doğru/yanlış, çünkü ..." ya da "Bence bu ... için iyi/kötü". 13F tweetlerinde: fonun hamlesine katılıp katılmadığım ve nedeni. Görüş en az 1 tam paragraf, tweetin sonunda; ilk paragraf yine haber/rakam. Sınırlar aynen: al/sat tavsiyesi yok (okura "alın/satın" yok), portföy güncellemesi ve teknik analiz yok, rakamlar yine 2 kaynak, yorum kendi görüşümüz olarak işaretli (bence, beğendim, bana göre). Kural 23 aynen.

## !!! KESİN KURAL 50-B (Enes 19.11 13:32: "görüş bildirmelerini sevdim ... ama her tweette aynı kalıpları kullanabilirsin, bunu istemeyiz, farklı farklı anlatımlarda bulun görüşlerini açıklarken"): Görüş paragrafı HER tweette farklı kurulur. (1) Aynı açılış (ilk 3 kelime) son 12 görüşte yok; aynı hüküm kalıbı ("karışık buldum", "beğendim", "bence ... çıkmıyor", "bununla uyumlu" vb.) son 6 görüşte yok. (2) Kontrol: tweet metni yazılınca `python3 invest/gorus.py kontrol < metin` (çıkış 1 = yeniden yaz), atınca `python3 invest/gorus.py kaydet < metin`. yasak.py ile birlikte çalışır. (3) Anlatım havuzu, sırayla değil bağlama göre seç ve kelimeleri her seferinde değiştir:
- Doğrudan hüküm: "Bu bilanço beni tatmin etmedi", "Rakamlar hoşuma gitti", "Bu çeyrekten memnun kaldım", "Beklediğim gibi değil", "Açıkçası hayal kırıklığı"
- Gerekçeyle başlayan: "Bulut tarafı güçlü ama kârdaki kaçış gözümden kaçmadı...", "Marjlar toparlanmasa daha sert düşünürdüm..."
- Kıyas: "Geçen çeyreğe göre çok daha temiz bir tablo", "Rakiplerine göre bir adım önde duruyor"
- Soru-cevap kurgusu YOK (tweet soruyla bitmez); onun yerine "Şunu merak ediyordum, cevabı geldi..." gibi düz anlatım
- Senaryo: "Marj bu hızla toparlanırsa ...", "Bu tempo iki çeyrek daha sürerse ..."
- Ölçülü/şüpheci: "Henüz ikna olmadım", "Kâğıt üzerinde iyi, ama ...", "Tek çeyrek yetmez"
- Kişisel öncelik: "Benim için asıl rakam ...", "Ben en çok ... kısmına takıldım"
- Hamle/haber yorumu: "Doğru zamanlama", "Pahalı ama mantıklı bir alım", "Bu adımı yerinde buluyorum", "Bunu riskli buluyorum çünkü"
- 13F: "Bu hamleye katılıyorum / katılmıyorum", "Ben olsam ... tarafında dururdum" (okura tavsiye değil, kendi tavrım)
(4) Görüş uzunluğu ve yeri de değişebilir: bazen tek güçlü cümle, bazen 3-4 cümle; bazen son paragraf, bazen ikinci paragraf. Hüküm her zaman net olmalı. Kural 50 sınırları aynen (al/sat tavsiyesi yok, rakamlar 2 kaynak).

## !!! KESİN KURAL 51 (Enes 19.11 13:35: "öyle yaz"): Bilanço tweetlerinde (beklenti, rakam, analiz, detay, çağrı, beklenen hareket) ve kartlarında dönem HER ZAMAN takvim + mali yıl birlikte yazılır: "$T Eylül 2026 çeyreği (mali 2027 2. çeyrek)". Takvim kısmı = çeyreğin bittiği ay ve takvim yılı (bültendeki 'quarter ended ...' tarihinden). Başlık örneği: "$BABA EYLÜL 2026 ÇEYREĞİ (MALİ 2027 2. ÇEYREK) BİLANÇOSU". Kartta etiket kısa tutulabilir: "EYLÜL 2026 ÇEYREĞİ". Mali yıl = takvim yılı olan şirketlerde (ör. çoğu ABD şirketi) yalnız "2026 3. çeyrek" yeterli.

## !!! KESİN KURAL 58 (Enes 20.11 09:44: "Chrome'a bağlıysan Reddit ve Substack gönderilerini oku, finansla ilgili en çok etkileşim alanları oku, tweet fikirleri çıkar, 10:15'teki öğrenmeyle harmanla, arada sırada buradan tweet at"): REDDIT / SUBSTACK FİKİR TARAMASI.
NOT (20.11 09:50 test): Claude in Chrome uzantısı reddit.com'u "güvenlik kısıtlaması" ile ENGELLİYOR (Enes'in ayarı değil, uzantı politikası); Reddit atlanır, etrafından dolanılmaz (old.reddit, ayna, önbellek YOK). Substack açılıyor: substack.com/browse/finance → "En üst" + "Rising in Finance". (1) Yalnız Claude in Chrome BAĞLIYSA (mcp__claude-in-chrome__list_connected_browsers / tabs_context_mcp çalışıyorsa). Bağlı değilse adımı ATLA, Enes'e kurulum anlatma, DONGU'ya "- FIKIR: Chrome yok, atlandı" yaz. X hesabına ASLA girme; Reddit/Substack'te yalnız OKU (oy, yorum, abonelik, giriş, beğeni YOK).
(2) Ne zaman: her gün 10:15 performans öğrenme görevinin sonunda (gorevler/perfogren.md adım 7) + Chrome bağlıysa akşam bir turda (21:00-23:00 arası ilk tur) bir kez daha.
(3) Nereden: Reddit r/stocks, r/investing, r/StockMarket, r/wallstreetbets, r/SecurityAnalysis, r/ValueInvesting, r/semiconductors, r/AIstocks → "Top / Today" ya da "Hot", en çok oy+yorum alan 5-8 finans gönderisi; Substack → finans/yatırım kategorisinde "Trending/Top" ve tanınmış yazarlar (ör. yapay zekâ, yarı iletken, makro), en çok beğeni/yorum alan 3-5 yazı. Yeni sekmede aç, işin bitince kapat.
(4) Çıktı: invest/fikir_havuzu.md'ye her fikir için bir satır (kaynak, etkileşim, fikri KENDİ cümlemle, ticker). Kural 46 alanı (yapay zekâ, uzay, Nasdaq + makro) ve kural 55 (yapay zekâyla ilgili her hisse) içindekiler.
(5) Harmanlama: fikirleri DURUM 'İÇERİK AYARI (kural 57)' ile süz (iyi giden saat, tür, uzunluk, ilk cümle). Turlar günde 1-3 tweeti havuzdan seçebilir ("arada sırada"); seçilen fikrin içindeki her rakam 2 bağımsız kaynakla doğrulanır, Reddit/Substack metni kopyalanmaz, kişi adı/kullanıcı adı yazılmaz, tweet yine net görüşle biter. Kullanılan satır "kullanıldı GG.AA SS:DD" olur. Fikir tweetlerinin AYRI performansına BAKILMAZ (Enes 20.11 09:46: "onun performansına bakmayacaksın, genel tweet performanslarına bakılıp oradan bulduğun fikirleri en çok etkileşim alacak şekilde harmanlayacaksın"): fikir, genel performans öğreniminin (İÇERİK AYARI, en iyi giden saat/tür/uzunluk/ilk cümle/portföy-grafik) en çok etkileşim getiren kalıbına oturtularak yazılır; sıklık fikir türünün kendi sonucuna göre DEĞİŞTİRİLMEZ.

## !!! KESİN KURAL 57 (Enes 20.11 09:08: "gösterim iyi mi, baktıkça öğrenip içerikleri ona göre ayarla, yeteneklere kaydet, her baktığında bir sonraki için ne zaman bakacağını ayarla, ayarlanmışsa dokunma ya da geliştir; ben sürekli farklı sohbetlere geçiyorum"): PERFORMANSTAN ÖĞRENME DÖNGÜSÜ. (1) Sabit zincir "Sabit: performans öğrenme 10:15" her gün (sonraki.py perfogren, gorevler/perfogren.md): Buffer metriklerini çeker, `perf_isle.py` ile performans_veri.csv'ye işler, `perf_isle.py --ozet` + `ders_analiz.py` çalıştırır, DERSLER.md'ye gözlem/ders yazar, aşağıdaki İÇERİK AYARI bloğunu günceller, Enes'e kısa özet atar. (2) Zincir mantığı: her çalışma İLK İŞ bir sonrakini kurar; list_triggers'ta aynı adlı bekleyen varsa KURMAZ (çift kurulum yok). Sabah 09:00 kontrolü 13 sabit zinciri (sonraki.py hepsi) doğrular, eksik olanı kurar. (3) Yeni sohbete geçişte: HESAP_DEVRI/DEVIR_TAM'daki sabit zincir listesi + `python3 invest/sonraki.py hepsi` + `python3 invest/isler.py devir` tek kaynak; yeni sohbet önce list_triggers'a bakar, var olanlara dokunmaz, yalnız eksikleri kurar. (4) Turlar her tweet seçiminde İÇERİK AYARI bloğunu uygular. Buffer metrikleri ~12-24 saat gecikmeli: 12 saatten genç tweetin metriği ders için kullanılmaz.

## !!! KESİN KURAL 56 (Enes 20.11 09:07: "bu tarz tweetlerden sonra ertesi gününde bunlarla alakalı tweetler atman lazım"): "Yarın/cuma/haftaya bakacağım şeyler", "izleyeceğim seviyeler", senaryo ya da beklenti tweeti atıldığında İÇİNDEKİ HER MADDE için takip tweeti ZORUNLU. (1) Tweeti atan görev, aynı anda her madde için iş defterine `TAKIP-<GGAA>-<konu>` işi açar ve uygun saate send_later kurar (açılışa bağlı maddeler 16:45-17:30, kapanışa bağlı maddeler 00:05-00:20 TSİ, veriye bağlı olanlar veriden 10-20 dk sonra). (2) Takip tweeti önceki tweete atıf yapar ("Dün yazdığım ... seviyesi"), ne olduğunu 2 kaynakla söyler, beklentinin tutup tutmadığını açıkça yazar. (3) Kural 23 burada geçerli DEĞİL: tutmayan beklenti de takip tweetinde dürüstçe yazılır (Enes isteği öncelikli). (4) Teknik analiz tweetlerindeki senaryolar (ör. NDX 26.244 / 25.350) da bu kurala girer.

## !!! KESİN KURAL 55 (Enes 19.11 23:04: "ai. ilgilendiren her hisseyle ilgili tweet atabilirsin"): Yapay zekâyla ilgili HER hisse konu olabilir (yalnız portföy/ilgi listesi/büyük takip değil: çip, hafıza, ağ, enerji/veri merkezi, bulut, yazılım, robotik, yapay zekâ halka arzları vb.). Tur turu "2 kaynaklı yeni haber yok" diye BOŞ GEÇMEZ: portföy ve listelerde haber yoksa yapay zekâ evreninin tamamında (en çok hareket edenler, analist notları, ortaklıklar, 13F, after-hours) tara ve en az 1 tweet at. 3 saat ticker kuralı yapay zekâ hisselerinde yeni bilgi/farklı açı varsa (ör. 13F, şirket yanıtı, yeni haber) tweeti ENGELLEMEZ; yalnız aynı bilginin tekrarını engeller. 2 kaynak, kural 46 dışı konular (perakende vb.) ve Anthropic yasağı aynen.

## !!! KESİN KURAL 54 (Enes 19.11 21:51: "Bu düşüşü abartılı buluyorum ama riski de hafife almıyorum. çok ai yazmış gibi bir ifade bidaha kullanma"): İki tarafı dengeleyen yapay zekâ kalıpları YASAK: "X buluyorum ama Y'yi de hafife almıyorum", "hafife almıyorum / göz ardı etmiyorum / küçümsememek lazım", "bir yandan ... öte yandan", "her ne kadar", "madalyonun iki yüzü", "altını çizmek", "unutmamak gerek". Görüşü TEK yönde, sade ve insan gibi söyle: "Bence düşüş fazla sert.", "Ben bu iddiaya şimdilik pek inanmıyorum.", "Bu riski ciddiye alırım." Gerekiyorsa çekinceyi ayrı, kısa ve somut bir cümleyle yaz ("Bakanlık soruşturma açarsa iş değişir."). yasak.py bu kalıpları yakalar (çıkış 1 = ATMA).

## !!! KESİN KURAL 53 (Enes 19.11 20:20: "iki saat arası tweet sınırı olmasın"): Hiçbir saat diliminde tweet adedi sınırı YOK (18-21 dahil). D-003 yalnız 'görüşlü analizi 12-15 / 21-24'e koy' tercihi olarak kalır, tweet atmayı ENGELLEMEZ. Görev mesajlarında '18-21 en çok 2' yazsa bile UYGULANMAZ. Günlük adet yine kural 48 (Pzt-Cmt 30-50, Pazar 10); turlar 15-25 dk arayla, her turda 1-2 tweet.

## !!! KESİN KURAL 52 (Enes 19.11 17:39: "şöyle okuyorum, böyle okuyorum vs gibi ifadeler ya da benim okumam vs gibi ifadeler kullanma"): Tweetlerde "okuyorum", "okumam", "benim okumam", "okunuşu", "... olarak okumak gerekiyor", "şöyle/böyle okuyorum", "okuyabiliriz" gibi "okuma" kalıpları YASAK. Görüşü doğrudan söyle: "Bunu dürüst buluyorum", "Bence bu ...", "Bu rakam hoşuma gitti", "Bu bana ... gösteriyor". yasak.py bu kalıpları yakalar (çıkış 1 = ATMA).





# Bilanço ve 13F tweetleri

Genel tur kuralları (kontrol, kaynak, yazım, kart, paylaşım, kayıt) için `enes-tweet-turu` skill'i geçerlidir; bu skill onun üstüne bilanço ve 13F'e özel kuralları ekler. Repo `/home/claude/kontra-gorsel/invest`; ayrıntı `DEVIR_TAM.md` (bölüm 4, kesin kural 7 ve 10), kalıplar `ORNEKLER.md`.

## A. Bilanço döngüsü

- KONU FİLTRESİ (kural 46): yalnız yapay zekâ, uzay, Nasdaq/büyük teknoloji şirketleri. Perakende/tüketim/banka/sanayi bilançoları için görev kurulmaz, tweet atılmaz.

Portföy (DOCN RKLB SITM AXON CBRS VRT AVGO) ve ilgi listesi (ON AAOI HOOD TEM CRDO PLTR ISRG ASTS MU + büyük yapay zekâ/yarı iletken/bulut/uzay: NVDA AMD AVGO TSM MSFT GOOGL AMZN META ORCL CRWV SNOW vb.) şirketlerinde öncesi ve sonrası KESİN atılır.

### 0. Konsensüs beklenti tweeti (kural 49)
KURAL 49 (Enes 18.11 22:16: 'bizim yatırımcılık tarzımıza uyan tüm hisseler için bilanço açıklanmadan önce konsensüs beklentilerini tweet at bu şekilde kısaca'): kural 46 alanındaki (yapay zekâ / uzay / Nasdaq teknoloji + portföy, ilgi listesi, büyük takip; WMT 19.11 istisnası dahil) HER bilançodan önce AYRI, KISA bir konsensüs tweeti. Zaman: HAZIRLIK görevi içinde, açıklamadan 30-60 dk önce (önizleme tweeti olsa da ayrıca atılır; 3 saat ticker kuralına takılmaz, Enes'in açık isteği). Kart: kart2.beklenti(ticker, şirket adı, 'Mali YYYY • N. çeyrek', 'GG Ay, açılış öncesi/kapanış sonrası (TSİ ~SS:DD)', [(metrik, konsensüs, alt not)], kaynak, out) — büyük logo + Metrik/Konsensüs tablosu; satırlar gelir + hisse başı kâr (+ şirkete özgü 1-2 KPI ya da şirket rehberi). Metin 2-4 kısa satır, yorumsuz: '$T bu gece/yarın sabah ... bilançosunu açıklıyor. Piyasa beklentisi gelirde X, hisse başı kârda Y.' + varsa şirket rehberi ve opsiyon hareketi tek cümle. Her rakam 2 kaynak. DONGU '- BEKLENTI: T'.

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

- KURAL 46 (Enes 18.11 17:12): 13F tweetinde yalnız fonun yapay zekâ / uzay / teknoloji hamleleri; bu alanda anlamlı hamlesi olmayan fon atlanır. Bilanço önizleme/rakam/analiz de yalnız bu alandaki şirketler için (perakende, banka, sanayi vb. yok).

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
- Sıra ve aralık: en önemli konu ilk; tweetler arasında 20-30 dk (send_later zinciri, aynı görev adı + sıra no). Bu tweetler Enes isteğidir, günlük tweet sınırına takılmaz.
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

## İş defteri ve sohbet devri (kesin kural 43)
İŞ DEFTERİ VE SOHBET DEVRİ GÜVENCESİ (kesin kural 43, Enes 18.11 01:29: "başka sohbete geçince bazı şeyler o tarafa geçmedi çünkü o sohbette hiç NVDA bilançosunu konuşmamıştık; sorunu tamamen anla ve çöz, bundan sonraki sohbet değişikliklerinde de hallolsun").
- SORUNUN KÖKÜ (18.11 tespiti): (1) devam eden işlerin durumu (ne yapıldı, ne bekliyor, ne iptal) yalnız sohbet geçmişinde ve görev mesajlarındaydı; yeni sohbet bunları göremez. (2) Elle yazılmış "bekleyen görevler" listesi eksik/yanlış kaldı. (3) Enes'in bir cümlesi fazla geniş yorumlandı ("bu bilanço için atman gereken bir şey kalmadı" = yalnız DETAY tweetleri; görüşme tweetleri de yanlışlıkla iptal edildi) ve bu yanlış karar kayda geçtiği için yeni sohbet de aynen uyguladı.
- ÇÖZÜM 1 — İŞ DEFTERİ: zamanı belli her tek seferlik iş invest/is_defteri.json'da durur (python3 invest/isler.py). Bilanço takvime girer girmez `python3 invest/isler.py bilanco <T> <YYYY-MM-DDTHH:MM> <acilis_oncesi|kapanis_sonrasi> [görüşme HH:MM]` ile 7 adım eklenir: opsiyon (39), hazırlık, yayın, analiz, detay (41), çağrı (40), beklenen hareket (22n). Veri yayınları ve Enes'in istediği zamanlı işler `isler.py ekle` ile. send_later kurulunca `isler.py durum <id> kuruldu --trigger <trig>`, iş bitince `durum <id> yapildi --not "saat, Buffer id"`.
- ÇÖZÜM 2 — İPTAL KURALI: Enes bir şeyi iptal ettiğinde YALNIZ açıkça söylediği kapsam iptal edilir; birden fazla işi kapsayabilecek cümlede EN DAR yorum alınır. İptal `isler.py durum <id> iptal --soz "Enes'in aynen sözü"` ile yazılır (söz olmadan iptal kaydı reddedilir). İptal edilen her iş Enes'e tek satırda adıyla söylenir; emin olunmayan kısım iptal edilmez ve "X devam ediyor" denir.
- ÇÖZÜM 3 — DEVİR: yeni sohbet (HESAP_DEVRI.md "SOHBET DEVRİ") açık işleri hafızadan değil `python3 invest/isler.py devir` çıktısından kurar; list_triggers ile karşılaştırır, eksikleri kurar; sonra Enes'e açık işleri tek tek (saat + ad) listeler. Eski sohbet "dur" denince görevlerini kapatır ama defter aynen kalır.
- ÇÖZÜM 4 — GÜNLÜK KONTROL: tur_basi.sh her turda `isler.py kontrol` çalıştırır; zamanı geçip yapılmamış iş "EKSIK IS" diye çıkar ve o tur önce onu tamamlar ya da Enes'e yazar. Sabah 09:00 kontrolü `isler.py devir` ile list_triggers'ı karşılaştırır.
- ÇÖZÜM 5 — KONUŞMADAKİ KARARLAR: Enes'in sohbette verdiği her karar (tek bilanço, tek hisse, tek gün için olanlar dahil) ilgili defter satırının "not" alanına ve DONGU'ya aynen yazılır; kalıcı kural ise DEVIR_TAM'a. "Bu sohbette konuşuldu, kayda gerek yok" diye bir şey yoktur.

## Detaylı analiz yazısı (kesin kural 45, Enes 18.11 07:40: "hisse analizi veya bilanço sonrası analiz yazılarımız çok çok daha detaylı olmalı ... çok detaylı çok kaynaklı")
KAPSAM: bilanço sonrası ANALİZ tweeti ve bir hisse üzerine her analiz/uzun görüş yazısı. (Yorumsuz rakam tweeti, detay ve görüşme tweetleri kendi kurallarıyla kalır.)
- UZUNLUK: tek uzun tweet, 10-15 kısa paragraf (yaklaşık 2000-4000 karakter). Kısa, yüzeysel analiz atılmaz; veri toplanamadıysa analiz 15 dk yerine en geç 45 dk'ya kayar, aceleye getirilmez.
- KAYNAK: en az 6 bağımsız kaynak, en az 4 farklı türden: (1) şirket belgesi (bülten tabloları, 8-K/10-Q, yatırımcı sunumu, CFO yorumu), (2) görüşme transkripti ya da canlı özeti (görüşme bitmediyse atlanır), (3) en az 2 haber kuruluşu (Reuters, CNBC, Bloomberg, AP, WSJ, FT, Barron's), (4) analist tepkisi (en az 2 kurumun not/hedef değişikliği: TheFly, StreetInsider, MarketBeat, Benzinga, TipRanks), (5) konsensüs/veri sitesi (LSEG, Zacks, FactSet, StockAnalysis, Yahoo), (6) gerekiyorsa sektör/rakip kaynağı. Her rakam yine 2 kaynak (kural 3); tek kaynak tweete girmez. DONGU satırına kaynakların tamamı yazılır; Enes'e mesajda kaynak listesi (link) verilir.
- İÇERİK (KONTROL LİSTESİ, SABİT SIRA DEĞİL; Enes 18.11 07:44: "yapısını sürekli kopyalama"): her analiz kendi konusuna göre farklı akışla kurulur; tek ana tezle aç, rakamları düşüncenin kanıtı olarak cümlelere yerleştir, olayları rakiplere/zincire bağla, iki tarafı dürüstçe tart, akılda kalan net bir hükümle kapat (ruh örneği ORNEKLER.md 22). Aşağıdaki başlıklar yazıda bulunmalı ama sırası, paragraf sayısı, açılış ve kapanış her seferinde değişir (etiketsiz düz paragraflar; veri yoksa atlanır, uydurma yok):
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
- BİLANÇO DIŞI HİSSE ANALİZİ: aynı derinlik; 2-3. maddelerin yerine iş modeli + son 4-8 çeyrek trendi, ayrıca içeriden alım/satım ve kurumsal sahiplik (13F) ve katalizör takvimi.
- GÖNDERMEDEN ÖNCE `python3 invest/yasak.py` (kural 11-B, Enes 18.11 14:55; 'Benim görüşüm:' ve 'Not:' yasak).
- GÖNDERMEDEN ÖNCE KONTROL: 13 maddeden en az 10'u var mı, kaynak ≥6 ve tür ≥4 mü, her rakam 2 kaynaklı mı, yasak kalıp (etiketli giriş, al/sat, emoji, soru ile bitiş) var mı. Eksikse tamamla, sonra at.
- Kart: panel/bento/uclu (son 3 düzen kuralı); kartta en önemli 3-4 rakam.

# ENESINVESTUS — TAM DEVİR NOTU (v8, 17.11.2026 12:40 TSİ) (eski: v7 16.11 21:20, v6 16:50)

Bu dosya, Enes Uludağ'ın 15-16 Kasım 2026 boyunca verdiği TÜM kuralların birleşik ve güncel hâlidir.
Kaynaklar: invest/DEVIR.md (15.11 v1), invest/DEVIR_OZET.md (15.11 21:05 + 16.11 ekleri), invest/ORNEKLER.md, invest/DONGU.md ve 16.11 canlı sohbet.
Çelişki çözümü: EN YENİ tarihli kural geçerlidir. Eski hâli "(eski: ...)" diye not edildi, böylece hiçbir şey kaybolmadı.
!!! v8 DEVİR ÖZETİ (17.11 12:40, Enes "devir") — YENİ OTURUM ÖNCE BUNU OKU !!!
- SKILL'LER (17.11 12:30-12:45, Enes kaydetti): enes-tweet-turu, enes-bilanco-13f, enes-portfoy-analiz. Kurallar artık bu skill'lerde; her tur/kontrol/bilanço işinde ilgili skill YÜKLENİR (Skill aracı). Bu dosya başvuru (portföy, seviyeler, geçmiş, kayıt tablosu) olarak kalır. Çelişkide EN YENİ tarihli kural geçerli. Yeni kural gelince hem bu dosya hem ilgili skill güncellenir (propose_skills improvement, Enes kaydeder).
- LOGO: kart2.LOGO_BUYUT = 1.8, KÜÇÜLTME YOK (bölüm 7). 17.11 sabah 13F kartlarında *0.62 küçültme yapıldı, HATAYDI; taşarsa başlığı kısalt ya da başka düzen seç.
- 17.11'DE ATILANLAR (Buffer): 09:06 vadeli; 09:38 13F Berkshire; 10:13 13F Ackman; 10:48 13F Druckenmiller; 11:13 13F Tepper; 11:41 13F Soros; 12:14 Nasdaq düşüş analizi (Enes isteği, tek uzun tweet, 5 sebep + çözüm + görüş); 12:22 NVDA bilanço önizlemesi (Enes isteği). Son 3 düzen: editoryal, siralama, bento.
- 13F SERİSİ DEVAM: sıradaki Third Point/Loeb (ön bilgi mlq: Meta aldı, doğrula) → Greenlight/Einhorn → Coatue → Tiger Global → Baupost/Klarman → Himalaya/Li Lu → Pabrai → Icahn → Bridgewater → Lone Pine/Viking; seri bitince Enes'e özet. Burry/Scion 10.11.2025'te SEC kaydını sildi, listeden çıktı. Tepper'ın AVGO ve AMD'den çıkışı tek kaynak (GuruFocus): doğrulanırsa Enes'e not (AVGO portföyde).
- BUGÜN BEKLEYENLER (17.11): HD ve Disney bilançoları sabah açıklandı mı kontrol et, atılmadıysa rakam tweeti (CRWV formatı; HD beklenti HBK 3,84 $, gelir 42,81 Mr $). 16:30 Ekim perakende satışları (beklenti +%0,2). ~15:00-15:25 vadeli. 18:00 ve 23:30 teknik kontrol (Nasdaq 100 ilk mesaj, kural 12). NVDA bilançosu ~00:20 TSİ 18.11: rakam tweeti + 15 dk sonra analiz; analizde 12:22 önizlemedeki TAHMİNLERLE kıyas yaz (gelir 111-113 Mr $, veri merkezi 103-105, brüt marj %74,2-74,5, HBK 2,53-2,58 $; 4. çeyrek rehberi 122-126 Mr $, marj ~%72; eşikler: rehber 125+ güçlü, 118 altı yavaşlama, marj rehberi %71 altı kötü). Tahmin tutmazsa açıkça söyle.
- YENİ KESİN KURAL 13 (17.11 12:45): her ABD işlem günü 10:30 TSİ key levels + günün önemli başlıkları tweeti; başlık açıklanınca rakam tweeti (o saate tek seferlik tur). Zincir 'Günlük key levels + başlıklar', A5'te kurulur. İlk çalışma 17.11 13:15 (bugün 10:30 geçtiği için).
- 18.11: TGT, FOMC toplantı notları 22:00 TSİ, PANW kapanış sonrası. 19.11: WMT.
- Enes'e verilen öneri (17.11 12:28): bilgisayarı uykuya almamak (TradingView için), sec.gov iznini bir kez onaylamak. Cevap bekleniyor.

!!! KESİN KURALLAR 18-21 (17.11 13:28, Enes: "4 ve 5'i ve bu 3 ek fikri kesinlikle ekle hemen") !!!
18) KULLANIM TASARRUFU (hak çabuk bitmesin):
   - invest/DURUM.md = tek sayfa güncel durum (en çok 80 satır): aktif hesap, portföy, son teknik seviyeler, son 3 düzen, 13F sırası, bugün/yarın takvimi, son 10 tweet ve ticker saatleri, görev kimlikleri, bekleyen kararlar. HER tur ve görev sonunda güncellenir (commit + push).
   - OKUMA KURALI: turlar ve görevler DEVIR_TAM.md ve DEVIR_OZET.md'yi BAŞTAN OKUMAZ. Okunan: ilgili skill (ya da invest/skills/ kopyası) + DURUM.md + `tail -n 30 DONGU.md` (+ gerekiyorsa takvim.md). DEVIR_TAM'dan yalnız gereken bölüm `grep -n` ile bulunup o kısım okunur (ör. kart signature, 14h metrik listesi). İstisna: yeni oturum ilk kurulumda (HESAP_DEVRI.md / DEVIR A bölümü) tam okur.
   - OTOMATİK TUR send_later ŞABLONU (uzun mesaj yerine, köşeli yerleri güncelle): "HESAP=A. Önce invest/AKTIF_HESAP.md oku; AKTIF: A değilse hiçbir şey yapma ve bu görevi kapat. OTOMATİK PAYLAŞIM TURU: enes-tweet-turu skill'ini uygula (yoksa invest/skills/enes-tweet-turu.md). Oku: invest/DURUM.md + tail -n 30 DONGU.md (+ takvim.md). DURDUR varsa dur. Bu tur: [konu/sıradaki 13F]. Son 3 düzen: [..]. Ticker 3 saat: [..]. Bekleyen yayınlar: [saat]. Bitince DURUM.md güncelle, push, 20-40 dk sonrasına bu şablonla send_later."
   - Buffer tekrar kontrolü: list_posts first 5 (50 değil). WebSearch varsayılan mode standard; extended yalnız son dakika taramasında ilk arama sonuç vermezse. ta2.py -v tam çıktısı yalnız teknik kontrollerde ve key levels'ta; turlardaki portföy taramasında kısa çıktı (`python3 ta2.py <tickerlar> > /tmp/ta.txt` ve yalnız fiyat + dilim özet satırları). Kart Read kontrolü bir kez (sorun varsa tekrar).
   - ARŞİV: Pazar 20:00 görevi DONGU.md'de 7 günden eski satırları invest/arsiv/DONGU_YYYY-AA.md'ye taşır (DONGU kısa kalır).
   - ÖLÇÜM: 18.11 günü boyunca hangi adımın en çok hak harcadığı gözlenir (en uzun okunan dosyalar, en çok arama yapılan tur türü); 18.11 23:45'te Enes'e kısa rapor + önerilen ek tasarruf.
19) HAFTALIK ÖZET (Cumartesi 11:00 TSİ, tekrarlayan görev, HESAP=A): "bu hafta ne oldu" tek tweet + kart. S&P 500, Nasdaq 100, Dow, Russell 2000 haftalık % (Yahoo, Cuma kapanışı vs önceki Cuma; ikinci kaynak haber), en çok konuşulan 3 olay (her biri tek cümle + kısa görüş, 2 kaynak), haftanın en iyi ve en kötü büyük hissesi (S&P 500 içinden, 2 kaynak). Tür HAFTALIK-OZET. Kart: dortlu/siralama/isi (son 3 düzen kuralı).
20) PAZAR "GELECEK HAFTA" TWEETİ: Pazar 20:00 takvim görevi takvim.md'yi hazırladıktan sonra haftanın önemli bilançolarını ve verilerini gün + TSİ saatiyle tek tweet + takvim kartı olarak paylaşır (en fazla 8-10 satır, en önemliler; beklentiler 2 kaynak). Tür TAKVIM. Enes'e ayrıca mesaj gerekmez.
21) DÜZELTME KURALI + AYIN ÖZETİ:
   - DÜZELTME: atılmış bir tweette yanlış rakam/bilgi çıkarsa (ikinci kaynak teyidi, okuyucu fark etmesi, sonradan revizyon dahil) 1) Enes'e HEMEN SendUserMessage (ne yanlış, doğrusu ne, kaynak), 2) aynı gün açık ve sade düzeltme tweeti: "Az önceki $X tweetinde Y'yi Z yazdım, doğrusu W." (etiket yok, savunma yok, kart gerekmez; görselde hata varsa düzeltilmiş kart), 3) DONGU'ya "DUZELTME:" satırı ve invest/HATA_GUNLUGU.md'ye kayıt (tarih, tweet, hata, sebep, önlem); aynı tür hata tekrar ederse ilgili skill'e önlem maddesi eklenir. Bu yalnız yanlış yazılmış RAKAM/BİLGİ içindir; tutmayan tahminler paylaşılmaz (kural 23).
   - AYIN ÖZETİ: her ayın ilk ABD işlem günü 11:00 TSİ (tekrarlayan görev ayın 1-7'si hafta içi çalışır, o ay zaten atıldıysa ya da ilk işlem günü değilse hiçbir şey yapmaz): geçen ayın S&P 500, Nasdaq 100, Dow, Russell ve portföy hisselerinin (DOCN RKLB SITM AXON CBRS VRT AVGO) aylık %'si (Yahoo + 1 kaynak; portföy kelimesi tweete yazılmaz, "takip ettiğim hisseler" denebilir, ağırlık/tutar yok), en önemli 3 olay, tek tweet + kart. Tür AYLIK-OZET.

!!! KESİN KURAL 22 (Enes 17.11 14:35, "tüm tamam dediklerimi ekle"): YENİ İÇERİK VE SİSTEM ÖZELLİKLERİ
 a) PERFORMANSA GÖRE KARIŞIM (5): Pazar 21:30 raporu 3 haftalık veri olunca "önerilen karışım" tablosu (tür → günlük adet, en iyi saat dilimi) çıkarır. Enes "onay" yazınca DURUM.md "İçerik karışımı" bölümüne ve enes-tweet-turu skill'ine işlenir; turlar konu seçerken bu karışıma uyar. Onaysız değişiklik yok.
 b) ŞABLON KÜTÜPHANESİ (6): invest/sablonlar.md. Sık türler için metin iskeleti + kart çağrısı. Turlar sıfırdan yazmaz, şablondan doldurur; yazım kuralları aynen geçerli. Yeni sık tür çıkarsa şablon eklenir.
 c) İÇERİDEN ALIM + GERİ ALIM RADARI (10, 29): hafta içi 14:20 sabit görev. Son 24 saatin SEC Form 4'leri (OpenInsider + EDGAR/haber teyidi): kod P piyasadan alım, 1 Mn $ üstü, küme alımı; 10b5-1 planlı satış ve kod F hariç. Aynı taramada büyük hisse geri alım açıklamaları (piyasa değerinin %3'ü ya da 5 Mr $ üstü). En güçlü 1 tanesi tweet (tür ICERIDEN ya da GERI-ALIM); kısa liste DURUM.md'ye.
 d) MAKRO VERİ SÖZLÜĞÜ (14): invest/makro_sozluk.md. Her makro veri tweetine sözlükten tek cümle "neden önemli" eklenir; aynı cümle 2 hafta içinde tekrar edilmez (sözlükteki varyasyon kullanılır).
 e) 1 YIL ÖNCE BUGÜN (16): ayda 2-3 kez menüden. Geçen yılın aynı haftasındaki piyasa olayı ya da hesabın eski tweeti bugünle karşılaştırılır. YALNIZ DOĞRU ÇIKAN tespit/beklenti paylaşılır, tutmayanlar paylaşılmaz (kural 23). Rakamlar 2 kaynak. Tür BIR-YIL.
 f) SEKTÖR ISI HARİTASI (20): Cumartesi 13:25 sabit görev. 11 S&P sektör ETF'si (XLK XLC XLY XLP XLE XLF XLV XLI XLB XLRE XLU) haftalık %, isi kartı (kolon=3), para nereye aktı tek cümle. Tür SEKTOR.
 g) FED VE TAHVİL TAKİBİ (21): her turda Yahoo ^TNX ve DX-Y.NYB. Gün içinde 10 yıllık faiz ±8 baz puan, dolar endeksi ±%0,6 ya da CME FedWatch'ta bir sonraki toplantı olasılığında 15 puan üstü değişim varsa "ne değişti, teknoloji/büyüme hisselerini neden etkiler" tweeti (2 kaynak; tür FED-TAHVIL). Günde en fazla 1.
 h) BİLANÇO SEZONU KARNESİ (22): Pazar 14:25 sabit görev. Sezonda S&P 500 şirketlerinin raporlayan oranı ilk kez %50'yi ve ilk kez %90'ı geçtiği haftalarda tek tweet: kaçı açıkladı, yüzde kaçı HBK ve gelir beklentisini aştı, en iyi/en kötü sektör, 5 yıllık ortalamayla kıyas (FactSet Earnings Insight + LSEG/Reuters). Her eşik bir kez (DONGU/arsiv kontrolü). Tür SEZON-KARNESI.
 i) 13F ÇEYREK ÖZETİ (23): 13F serisinin son yatırımcısı atıldıktan sonraki turda tek tweet: büyük yatırımcıların ortak aldığı ve ortak sattığı hisseler (en az 3 yatırımcı), siralama kartı. Tür 13F-OZET.
 j) KURUMSAL OLAY TAKVİMİ (25): Pazar takvim görevi büyük halka arzları, hisse bölünmelerini, büyük temettü kararlarını ve S&P 500 / Nasdaq 100 endeks giriş-çıkışlarını da takvim.md'ye yazar; günü gelen tur tweetler (tür KURUMSAL).
 k) ANALİST HEDEF ÖZETİ (27): ayın ilk Pazarı 12:25 sabit görev. Portföy + genişletilmiş ilgi listesi + adaylar için geçen ayın hedef fiyat değişimleri (yukarı/aşağı revizyon sayısı, ortalama hedef değişimi, ortalama hedefin mevcut fiyata uzaklığı); siralama kartı tweet (tür ANALIST-OZET) + Enes'e "beklentiler hangi hisselerde yukarı/aşağı kayıyor" notu.
 l) RAKİP KARŞILAŞTIRMA (33): portföy ya da ilgi listesi şirketi bilanço açıkladığında analiz tweeti (ya da sonraki tur) en yakın rakiple yan yana kart (panel ya da dortlu): büyüme, brüt marj, ileri F/K, verilen tahmin. Örnek eşler: VRT-ETN, AVGO-MRVL, ANET-CSCO, CRWD-PANW, NET-AKAM, AXON-MSI; diğerlerinde en yakın rakip araştırılır. Tür RAKIP.
 m) DEĞERLEME BANDI (34): ayın ikinci Pazarı 12:25 (aynı sabit görev). Portföy + ilgi listesi için ileri F/K ve fiyat/satış, hissenin kendi 3 ve 5 yıllık ortalamasıyla (2 kaynak). Enes'e not; en çarpıcı 1-2 tanesi tweet (tür DEGERLEME). "Ucuz/pahalı" yerine "kendi geçmişine göre yüksek/düşük"; al/sat yok.
 n) OPSİYON BEKLENEN HAREKET (36): bilanço önizleme tweetine "opsiyon piyasası bilanço sonrası ±%X hareket fiyatlıyor" (Barchart / Market Chameleon / OptionCharts + haber, 2 kaynak). Ertesi gün açılıştan sonraki ilk turda portföy ve büyük şirketlerde "beklenen ±%X, gerçekleşen %Y" kısa tweet (tür BEKLENEN-HAREKET).
 o) MEVSİMSELLİK (37): ayın İKİNCİ ABD işlem günü 11:00 (ayın özeti görevi yapar): S&P 500 ve Nasdaq'ın o ayki tarihsel ortalama getirisi ve pozitif kapanma oranı (en az 20 yıl, 2 kaynak), "geçmiş garanti değil" cümlesi. Tür MEVSIMSELLIK.
 p) İLGİ LİSTESİ SIRALAMA (40): Cumartesi 16:25 sabit görev. Genişletilmiş ilgi listesinin haftalık %, siralama kartı, ilk 2 ve son 2'ye tek cümle sebep. Tür ILGI-HAFTALIK.
 q) LANSMAN TAKVİMİ (41): Pazar takvim görevi büyük teknoloji etkinliklerini (Nvidia GTC, Apple etkinlikleri, AWS re:Invent, CES, Google I/O, Microsoft Build, Computex, Tesla etkinlikleri) takvim.md'ye yazar. Etkinlikten önce "ne bekleniyor", sonra "ne açıklandı ve hisseye etkisi" (tür LANSMAN).
 r) İLGİ LİSTESİ GENİŞLEDİ: ON AAOI HOOD TEM CRDO PLTR ISRG ASTS MU + yeni adaylar ANET ALAB MRVL COHR LITE ETN GEV CRWD NET DDOG APP RBRK PL LUNR. Yeni adayların temel karnesi (/50) turlarda zaman kaldıkça (günde 1-2) çıkarılır; 30 altı listeden çıkar. Güncel liste DURUM.md "İlgi listesi" bölümünde.
 Sabit görev ID'leri bölüm 16-G ve DURUM.md'de.

!!! KESİN KURAL 34 — TEMEL ANALİZ EKLERİ (Enes 17.11 21:43) !!!
- TEMEL ANALİZ EKLERİ (kesin kural 34, Enes 17.11 21:43: "temelini de geliştir"; mevcut 10 başlık /50, /45, metrik listesi, öz-denetim ve kırmızı bayraklar AYNEN, yalnız ekleme): her karnede ayrıca (a) KARNE TRENDİ: önceki karneye göre her başlıkta ve toplamda değişim (↑/↓/=) ve sebebi; (b) BEKLENTİ REVİZYON GENİŞLİĞİ: son 30/90 günde HBK ve gelir tahminindeki % değişim + yukarı/aşağı revize eden analist sayısı (2 kaynak); (c) KAZANÇ KALİTESİ: serbest nakit / net kâr, tahakkuk oranı, SBC/gelir eğilimi, tek seferlik kalemlerin payı; (d) ARTIMLI MARJ ve faaliyet kaldıracı: son 4 çeyrekte gelir artışının ne kadarı faaliyet kârına dönüştü; (e) KPI İVMESİ: sektöre özel ana KPI'ın son 3-4 çeyrekte hızlanıyor mu yavaşlıyor mu; (f) BİLANÇO STRESİ: küçük ve borçlu şirketlerde Altman Z, nakit pisti (ay), yakın vade borç; (g) DEĞERLEME BANDI: ileri F/K ya da EV/Satış'ın kendi 3/5 yıllık ortalamasına göre konumu (aylık bant görevinden ya da 2 kaynakla); (h) BİLANÇO TEPKİ GEÇMİŞİ: son 4 çeyrek aşım/kaçırma ve ertesi gün hisse tepkisi; (i) TEZ KARTI: her portföy hissesi için 3-5 maddelik yatırım tezi + "tezi bozan 3 sinyal"; her karnede maddeler tek tek güçlendi/zayıfladı/aynı diye işaretlenir. Eksik portföy karneleri (temel_karne.md'de "eksik" olanlar) bitene kadar her otomatik turun "zaman kalırsa karne" adımı ÖNCE portföy eksiklerini doldurur.

!!! KESİN KURAL 41 — BİLANÇO DETAY TWEETLERİ (Enes 18.11 00:57) !!!
- BİLANÇO DETAY TWEETLERİ (kesin kural 41, Enes 18.11 00:57: "insanlar bilançolardan sonra bilançonun detaylarıyla ilgili böyle şeyler paylaşıyor, senin de benzerlerini her bilançodan sonra paylaşmanı istiyorum; en az iki, en fazla yedi, ne kadar önemli şey bulursan o kadar; illa bu örnekler gibi olmak zorunda değil, farklı şeyler bulup farklı şekillerde de yapabilirsin").
- NE: rakam tweetinin (yorumsuz) ve 15 dk sonraki analizin ÖTESİNDE, bilançonun içinden çıkan, çoğu kişinin bakmadığı somut detaylar. Kaynak belgeler: basın bülteninin tabloları, CFO yorumu (CFO commentary), 10-Q/10-K, yatırımcı sunumu slaytları, segment tabloları, nakit akış tablosu, bilanço (varlık/borç), taahhütler dipnotu, müşteri yoğunlaşması notu, rehber dipnotları.
- ÖRNEK TÜRLER (17.11 Nvidia örnekleri + daha fazlası; her bilançoda şirkete göre seç, hep aynı türleri kullanma): (1) taahhütler/sipariş defteri değişimi (Nvidia: tedarik taahhütleri 279 → 390 Mr $, toplam 366 → 518 Mr $, çoğu çok yıllık bellek alımı); (2) serbest nakit akışı ve nakit dönüşümü (çeyreklik sıçrama, analist yıllık tahmin serisi); (3) müşteri grubu/segment kırılımı ve yıllık değişim (Nvidia slaytı: büyük bulut 35,1 → 60,1; yapay zekâ bulutları, sanayi ve kurumsal 16,1 → 47,5 Mr $); (4) koşullu/riskli anlaşmalar (Nvidia: neo-bulut koşullu anlaşmaları 36 → 32 Mr $); (5) yeni ürün geçiş hızı ve yönetimin yazılı ifadesi; (6) marj köprüsü (neden düştü/arttı), faaliyet gideri rehberi; (7) alacak, stok, tedarik günleri; (8) geri alım, temettü, nakit/borç; (9) coğrafya/Çin payı; (10) en büyük müşteri payları (%10 üstü müşteriler); (11) rehberin içindeki takvim etkisi (ekstra hafta gibi); (12) önceki çeyrek rehberine göre aşım geçmişi; (13) hisse bazlı ödeme ve seyrelme; (14) şirkete özgü KPI tablosu (backlog, RPO, ARR, NRR, aynı mağaza satışı, sepet, trafik vb.).
- KAÇ TANE: en az 2, en çok 7; sayıyı önem belirler (az ama güçlü olan iyi). Her detay AYRI TWEET. Kural 40 görüşme tweetleriyle aynı konuyu tekrar etme (detaylar belgeden, görüşme tweetleri yönetimin sözlerinden).
- NASIL: her tweet kendi kartıyla (rakamı gösteren grafik: iki dönem çubuk, seri, kırılım; slayt/tablo görüntüsü KOPYALANMAZ, kendi kartımız çizilir) + kural 25 (ne demek, neden önemli, büyük resim, hisselere/zincire etkisi, net düşünce). İlk satır durdurmalı (rakam ya da tezat). Etiketli giriş, "X şu:", deyim, emoji, hashtag yok; X'teki başka hesapların tweeti kopyalanmaz/çevrilmez, kendi cümlemizle ve kendi açımızla.
- KAYNAK: şirketin kendi resmi belgesinden (bülten, CFO yorumu, 10-Q, sunum, SEC) doğrudan okunan rakam tek başına yeterli (kural 16 gibi; belge adı kartın kaynak satırında). Belgeye ulaşılamaz ve rakam yalnız ikinci elden (X görüntüsü, haber) geliyorsa en az 2 bağımsız kaynak. Enes'in ilettiği belge görüntüsü belge sayılır ama yine bir haber/ikinci platformla teyit edilir. Analist tahmini serileri (ör. Fiscal.ai FCF tahminleri) tahmin olduğu açıkça yazılarak ve 2 kaynakla.
- ZAMAN: rakam ve analiz tweetlerinden hemen sonra, belgeler ulaşılabilir olduğu anda (gece de dahil, bekleme yok).
- NETLEŞTİRME (Enes 18.11 01:05): detay tweetleri için BEKLEME YOK. Bilanço ne zaman açıklanırsa açıklansın, belgeler (bülten, CFO yorumu, sunum, 10-Q) ulaşılabilir olduğu anda analiz tweetinden sonra başlar; gece bilançolarında da 01:00-09:00 paylaşım yasağı bu tweetler için UYGULANMAZ (kural 16 gece istisnası gibi). Tweetler arası 15-25 dk. Ertesi sabaha bırakılmaz. Tweetler arası 20-30 dk; 18:00-21:00 dilimine düşen 21:00 sonrasına kayar; görüşme tweetleriyle (kural 40) sırayla ve iç içe değil.
- KURULUM: bilançonun YAYIN görevi (ya da 10:30 günün başlıkları görevi) "Detay: <T>" send_later görevini kurar (aynı ad varsa kurma); görev ilk tweeti atar, kalanları "Detay: <T> (2)" ... zinciriyle kurar ve her mesaja taslak + kaynak yazar. DONGU'ya her tweet için "- DETAY: <T> <konu>"; `tur_basi.sh` dün/bugün bilançosu olup DETAY satırı 2'den az olanları "EKSİK DETAY" diye yazar. Bu tweetler Enes isteğidir; günlük tweet sınırına takılmaz.

!!! KESİN KURAL 40 — BİLANÇO GÖRÜŞMESİ TWEETLERİ (Enes 18.11 00:31) !!!
- BİLANÇO GÖRÜŞMESİ (KAZANÇ ÇAĞRISI) TWEETLERİ (kesin kural 40, Enes 18.11 00:31: "bilanço açılış öncesi açıklandıysa aynı gün, kapanışta açıklandıysa bir sonraki gün bilançonun kazanç çağrılarını dinleyeceksin ya da transkriptine ulaşacaksın ve onunla alakalı önemli yerleri tweet atacaksın; birkaç önemli yer varsa hepsini ayrı ayrı tweetlere böl, tek tweete hepsini atma").
- Kapsam: bilanço döngüsündeki bütün şirketler (portföy, ilgi listesi, büyük yapay zekâ/yarı iletken/bulut/uzay/teknoloji, piyasayı oynatan perakende/banka vb.).
- Zaman: açılış öncesi açıklanan bilançoda AYNI GÜN (görüşme bitip transkript çıkınca, genelde görüşmeden 1-3 saat sonra); kapanış sonrası açıklananda ERTESİ GÜN (sabah 11:00-12:30 arası, transkript hazır olur).
- Kaynak: transkript (şirket IR webcast/transkript, Motley Fool, Seeking Alpha, Investing, Yahoo, Quartr) + en az 1 haber (Reuters, CNBC, Bloomberg, Barron's). Her rakam ve iddia 2 kaynak; tek kaynaktaki söz tweete girmez, Enes'e not.
- İçerik: görüşmenin rakam tweetinde OLMAYAN önemli yerleri: rehberin dayanağı, talep/sipariş/backlog yorumu, marj açıklaması, yeni ürün/geçiş takvimi, müşteri yoğunlaşması, Çin/ihracat, sermaye harcaması ve geri alım, yönetim değişikliği, analist sorularında öne çıkan konu. Her önemli konu AYRI TWEET (2-4 tweet; tek konu varsa tek tweet). Her tweet: ne dendi (yönetimin sözünü kendi cümlemizle aktar; doğrudan alıntı en çok 1 kısa ifade, 15 kelimeden az) + ne demek + etkisi + net düşüncemiz (kural 25). Etiketli giriş, "X şu:", deyim yok.
- Sıra ve aralık: en önemli konu ilk; tweetler arasında 20-30 dk (send_later zinciri, aynı görev adı + sıra no). Bu tweetler Enes isteğidir, günlük tweet sınırına takılmaz ama 18-21 dilimine düşerse 21:00 sonrasına kaydırılır.
- NETLEŞTİRME (Enes 18.11 01:05): "ertesi gün" = TSİ ile bilançonun açıklandığı gecenin SABAHI. Ör. Nvidia 00:10-00:20 TSİ açıkladı, görüşme 01:00 → görüşme tweetleri aynı sabah (09:30-12:00 arası; transkript hazır olunca). Açılış öncesi bilançoda görüşme tweetleri aynı gün, görüşmeden sonra.
- Kurulum: bilançonun YAYIN görevi (rakam tweetinden sonra) ya da 10:30 günün başlıkları görevi "Çağrı: <T>" send_later görevini kurar (aynı ad varsa kurma). DONGU'ya her tweet için "- CAGRI: <T> <konu>"; `tur_basi.sh` dün/bugün bilançosu olup CAGRI satırı olmayanları "EKSİK CAGRI" diye yazar.

!!! KESİN KURAL 39 — OPSİYON BEKLENEN HAREKET GÜVENCESİ (Enes 17.11 23:47) !!!
- OPSİYON BEKLENEN HAREKET GÜVENCESİ (kural 22n eki, Enes 17.11 23:47: "opsiyon piyasası tahminleri vardı, Nvidia için paylaştın mı, paylaşmadıysan neden, sistemdeki sıkıntıyı çöz").
- Sorun: 22n kuralı 14:35'te geldi, NVDA önizlemesi 12:22'de çıkmıştı; opsiyon verisi ancak 21:07 bağlam tweetinde girdi. Kural "önizlemeye ekle" diyordu ama önizleme zaten çıktıysa ne olacağı ve kontrol eden bir adım yoktu; ertesi gün kıyas görevi de yalnız yayın görevinin içinde kurulacaktı (yayın aksarsa kaybolur).
- Çözüm: (a) Takvimdeki her bilanço (portföy, ilgi listesi, büyük isimler, piyasayı oynatan TGT/WMT/HD vb.) için açıklamadan ÖNCE en az bir tweette opsiyonların fiyatladığı hareket (±% ve mümkünse dolar karşılığı, 2 kaynak) yer alır: önizleme varsa onda; önizleme önceden çıktıysa ya da yoksa günün başlıkları (10:30) / bağlam tweeti / ayrı kısa tweette. Atılınca DONGU'ya "- OPSIYON: <T> ±%X (kaynaklar)" satırı. (b) `tur_basi.sh` bugün ve yarın bilançosu olup DONGU'da OPSIYON satırı olmayanları "EKSİK OPSİYON" diye yazar; ilk uygun tur onu tamamlar. (c) Hazırlık görevi (T-60) OPSIYON satırını kontrol eder; yoksa veriyi bulur, Enes'e yazar ve yayından önce kalan tur/tweet ile atılmasını sağlar. (d) Ertesi gün "Beklenen hareket: <T>" kıyas görevi HAZIRLIK görevinde kurulur (yayın görevine bırakılmaz); kıyasta yalnız gerçek hareket ile opsiyon fiyatlaması karşılaştırılır (kural 23: kendi tutmayan tahminlerimiz anılmaz).

!!! KESİN KURAL 38 — ENES'İN TEKNİK ANALİZİNDEN TWEET TASLAĞI (Enes 17.11 22:30) !!!
- ENES'İN TEKNİK ANALİZİNDEN TWEET (kesin kural 38, Enes 17.11 22:30: "artık teknik analizi ben sana atacağım, sen de tweet yazım kurallarına bakıp sade dilde, mecaz kullanmadan yazacaksın ve bana tweeti yollayacaksın").
- Enes teknik analizini (metin, sesli not ya da grafik görüntüsü) atınca: Claude kendi teknik analizini YAPMAZ, gösterge/seviye EKLEMEZ, Enes'in seviye ve görüşlerini değiştirmez; yalnız onları tweet diline çevirir.
- Yazım kuralları aynen: arkadaşına anlatır gibi sade cümle; DEYİM/MECAZ YOK ("hikâye değişir/biter", "resim bozulur", "asıl sınav", "kapı açılır", "nefes alıyor", "ters köşe" vb. yerine düz ve ölçülebilir cümle: "69'un altında günlük kapanış gelirse düşüş devam edebilir"); terimler sade (FVG = boşluk, order block = alıcıların daha önce toplandığı bölge, Supertrend = trend göstergesi); etiketli giriş ve paragraf başında "X şu:" yok; emoji, hashtag, mention, link yok; soruyla bitmez; okura emir kipi ve al/sat tavsiyesi yok ("ben şuradan eklerim" Enes'in kendi dili olarak kalabilir, "alın" yok); "aldım", portföy, tutar, ağırlık yok; Anthropic adı geçmez.
- Grafikte okunamayan değer uydurulmaz; eksik ya da çelişkili bir şey varsa tweet yine yazılır, altına Enes'e tek cümle not.
- Çıktı: Enes'e SendUserMessage ile kopyalanmaya hazır tweet metni (gerekirse 1 kısa alternatif). Claude bu tweeti PAYLAŞMAZ, Buffer'a göndermez; Enes kendisi atar. DONGU'ya "- SS:DD ENES-TA-TASLAK: <ticker>" satırı.

!!! KESİN KURAL 37 — TEKNİK ANALİZ YOK, TEMEL ANALİZ (Enes 17.11 22:17) !!!
- TEKNİK ANALİZ KALDIRILDI, TEMEL ANALİZE YOĞUNLAŞ (kesin kural 37, Enes 17.11 22:17: "teknik analize bakmıyoruz bir daha, onunla alakalı her şeyi kaldır, onun yerine temel analize daha da yoğunlaş").
- Kaldırılan: 18:00 ve 23:30 teknik kontrol zincirleri (devre dışı), TradingView ve ekran görüntüleri (kural 27), teknik tweet taslakları, gösterge rotasyonu, çizimler (kural 31), ta_ek ve seviye karnesi (kural 33), KARAR'ın teknik ayağı (kural 35), key levels tweetindeki destek/direnç seviyeleri, turlardaki ta2 portföy taraması, TA-FARK (36f). ta2.py, ta_ek.py, seviye_takip.csv repoda arşiv olarak durur, KULLANILMAZ. Kural 12, 27, 31, 33 ve 30/35/36'nın teknik kısımları geçersiz.
- Yerine: her ABD işlem günü 18:00 TEMEL ANALİZ görevi (zincir temel1800, gorevler/temel1800.md): haber/8-K/Form 4/analist revizyonu taraması, günde en az 2 karne, tez kartı kontrolü (tez_kartlari.md), değerleme bölgeleri (kendi 3 yıllık bandı + akran + ters DCF; ucuz/adil/pahalı fiyat aralığı), temel KARAR tablosu, her gün 2-3 yeni aday tam karneyle, adayların en zayıf 2 portföy hissesiyle kıyası, özet tablo. Ben olsam notları değerleme bölgesi ve tez durumuna dayanır, grafik seviyesine değil.
- Key levels 10:30 görevi: seviye yok; "günün başlıkları" tweeti (takvim, vadeliler yönü, bilanço/veri beklentileri, kural 25 yorum) + takvim güncelleme + hazırlık/yayın görevleri.
- Turlarda tweetten sonra portföy hisselerinde haber taraması (ta2 yerine).
- Tweetlerde grafik/teknik görüş yok; görüş temel veriye dayanır.

!!! KESİN KURAL 36 — SİSTEM DENETİMİ VE TUTARLILIK (Enes 17.11 21:46) !!!
- SİSTEM DENETİMİ VE TUTARLILIK (kesin kural 36, Enes 17.11 21:46: "tüm sistemi araştır, çok detaylı düşün, tamamen geliştir"). Denetimde bulunan çelişki ve boşlukların çözümü (hiçbir kural kaldırılmadı; çelişkide en yeni tarihli kural geçerli ilkesi uygulandı):
a) TUR SIKLIĞI ve GÜNLÜK ADET: otomatik tur zinciri 20-40 dk aralıkla çalışmaya devam eder (16.11 kuralı), ama TWEET ATMA kararı DERSLER D-002/D-003'e (Enes onayı 17.11 17:18, daha yeni) bağlıdır: sistem tweeti günde en çok 15 (`periyot.py kontrol tweet_gunluk`), 18-21 arası en çok 2; hedefe ulaşıldıysa ya da değerli konu yoksa tur paylaşmadan geçer ve zamanı karne/aday/uzun yazı hazırlığına kullanır. GÜNE ÖZEL İSTİSNA: Enes'in o güne verdiği adet kuralı (ör. 17.11 15:23 "01:00'e kadar 10 tweet") geçerliyse o gün tweet_gunluk sınırı yerine o kural uygulanır (Enes talimatı > onaylı ders). Enes'in istediği tweetler ve bilanço/veri yayınları her zaman atılır (sayaca yazılır, sınıra takılmaz). tur_basi.sh "BUGUN SISTEM TWEETI" satırı bunu gösterir; kayit.py her tweette `tweet_gunluk` sayacını otomatik artırır.
b) GÜNE ÖZEL KURALLAR ve SÜRESİ: DURUM.md'deki "BUGÜNLÜK KURAL" bloğu yalnız başlığındaki tarih için geçerlidir; kayit.py başka günde sayacı düşürmez; sabah kontrolü (09:00) önceki güne ait blokları DURUM.md'den siler ve DONGU'ya "bugünlük kural süresi doldu" yazar.
c) SKILL ile KOPYA: hesaptaki skill'ler Enes kartları kaydettikçe güncellenir; kaydedilmemiş bir öneri olabilir. Bu yüzden skill ile invest/skills/ kopyası ya da DEVIR_TAM kesin kuralları çelişirse KOPYA ve en yeni kesin kural geçerlidir. Her görev skill'i yükledikten sonra çelişki şüphesinde ilgili kopya bölümünü grep ile okur.
d) GÖREV ÇAKIŞMASI (tek oturum sırayla çalışır): bilanço/veri YAYIN görevi ile ağır görevler (teknik analiz, uzun yazı, karne) çakışırsa yayın önceliklidir. Bir YAYIN görevi 60 dk içinde başlayacaksa ağır görev zaman kutusuna girer: yayından en az 15 dk önce bitecek şekilde kısaltılır (teknik analizde portföy 4s tek görüntü + KARAR satırları, adaylar 2'ye iner, rotasyon kısalır; atlanan kısım bir sonraki çalışmaya not edilir). Kapanış gibi kısa görevler yayından önce sıraya girerse 10 dk içinde biter.
e) KART DÜZENLERİ (O-007 eki): isi ve siralama 17.11 21:55'te düzeltildi (siralama negatif değerleri sıfır ekseniyle çizer; isi logoya çarpan ticker yazısını gizler, rakamı kalan yüksekliğe sığdırır; LOGO_BUYUT 1.8 korunur). Yeni kart düzeni kullanmadan önce Read ile tek bakış zorunlu kalır.
f) ÖLÇÜM FARKI: ta2.py ile TradingView arasında %2'den büyük fark olursa (ör. 17.11 DOCN 4s Supertrend ta2 91,4 SAT / TV 73,30 AL) TradingView esas; fark DONGU'ya "TA-FARK" etiketiyle yazılır, Pazar raporu farkların sık olduğu göstergeyi inceler.
g) DENETİM DÖNGÜSÜ: her Pazar performans raporundan sonra kısa sistem denetimi: (1) bütün zincirler bekliyor mu (sonraki.py hepsi vs list_triggers), (2) DURUM.md 100 satırı aştı mı (eski bölümler arsiv/'e), (3) HATA_GUNLUGU ve TA-FARK satırlarından tekrar eden hata var mı (varsa O-xxx operasyon dersi), (4) skill kopyası ile DEVIR_TAM kesin kurallar listesi aynı numaraya kadar mı. Sonuç Enes'e 3-5 madde.

!!! KESİN KURAL 35 — TEMEL + TEKNİK BİRLİKTE KARAR (Enes 17.11 21:43) !!!
- TEMEL + TEKNİK BİRLİKTE KARAR (kesin kural 35, Enes 17.11 21:43: "temele de bakılacak tekniğe de bakılacak ama ekstra yük oluşturma; saatleri gelince ikisini bir arada düşünüp her hisse için karar verilecek"): 18:00 ve 23:30 analizlerinde her hisse (portföy ve adaylar) için "ben olsam" notunun sonunda tek satır KARAR yazılır. EK YÜK YOK: temel taraf yeniden araştırılmaz, temel_karne.md'deki son karne (/45, kırmızı bayrak, tez kartı, karne tarihi) okunur; karne 7 günden eskiyse ya da arada bilanço varsa satıra "(karne eski, X tarihli)" eklenir, karne yoksa "(temel karne yok, karar teknik ağırlıklı, güven düşük)" yazılır ve hisse karne kuyruğunun başına alınır.
Temel sınıf (/45): GÜÇLÜ 34+, ORTA 26-33, ZAYIF 25 ve altı ya da kırmızı bayrak. Teknik durum: A = dip bölgesinde + dönüş teyidi (uyumsuzluk, mum, hacim, CHoCH); B = dip bölgesinde ama teyit yok; C = yukarı trend ya da orta bölge; D = düşüş trendi sürüyor, kademeye henüz gelmedi; E = tez seviyesi kırıldı.
Karar tablosu: GÜÇLÜ+A → ilk kademeden ekle | GÜÇLÜ+B → küçük kademe, teyitle ikinci | GÜÇLÜ+C → tut, geri çekilmeyi bekle | GÜÇLÜ+D → bekle, k1/k2'de ekle | GÜÇLÜ+E → ekleme yok, yeni dip yapısı bekle, haftalık kapanış teyidiyle azaltmayı değerlendir. ORTA+A → küçük kademe | ORTA+B → bekle | ORTA+C → tut | ORTA+D → ekleme yok | ORTA+E → azaltmayı düşün. ZAYIF+A → ekleme yok, tepkiyi azaltma fırsatı olarak gör | ZAYIF+B/C → tut, ekleme yok | ZAYIF+D/E → azalt ya da daha iyi adaya geç.
Satır biçimi: "KARAR (temel + teknik): GÜÇLÜ 37/45 + B (dipte, teyit yok) → ben olsam 323-330'dan küçük bir kademe ekler, MACD yukarı dönerse ikinciyi eklerdim." Adaylarda aynı tablo + portföyün en zayıf 2 hissesiyle kıyas; değişim önerisi için adayın karnesi zorunlu. Son özet mesajında bütün hisselerin KARAR satırları tek tabloda (hisse | temel | teknik | karar). Karar Enes'e özeldir, tweete girmez; tweet taslağında al/sat yok.

!!! KESİN KURAL 33 — TEKNİK ANALİZ EKLERİ (Enes 17.11 21:37) !!!
- TEKNİK ANALİZ EKLERİ (kesin kural 33, Enes 17.11 21:37: "teknik analizle ilgili her şeyi araştır, geliştir, bir şey çıkarma, sadece ekle"). ta2.py'nin 21 göstergesi ve mevcut bütün kurallar AYNEN; her teknik analizde ayrıca `python3 invest/ta_ek.py <semboller> > /tmp/ek.txt` çalıştırılır ve tamamı okunur. Eklenen kontrol listesi (her hisse notunda ilgili olanlar yazılır):
1. ZAMAN DİLİMİ HİZALAMASI: haftalık → günlük → 4s → 1s trend yönü (+/-/0). Üst dilime karşı kademe verilirken bu açıkça yazılır ("haftalık yukarı, günlük aşağı: geri çekilme alımı" ya da "hepsi aşağı: dip teyidi beklenmeli").
2. GÖRELİ GÜÇ: 1 ay / 3 ay QQQ'ya ve sektör ETF'ine (SMH, IGV, UFO, XLI...) göre puan farkı + RS çizgisi (20 günlük ortalamanın üstü/altı, 3 ay zirvesi). Endeks düşerken RS çizgisi zirvedeki hisse = liderlik işareti.
3. HACİM TEYİDİ: son gün RVOL, 5 gün/50 gün oranı (0,7 altı = hacim kuruması, kırılım öncesi tipik), son 25 günde dağıtım günü sayısı. Kırılım ya da dip dönüşü RVOL 1,5x altında ise "hacimle teyit edilmedi" yazılır.
4. SIKIŞMA: Bollinger bantlarının Keltner kanalı içine girmesi (TTM squeeze) ve bant genişliğinin 6 aylık yüzdeliği. Sıkışma yön söylemez, yalnız sert hareketin yakın olduğunu söyler; yönü kırılım + hacim belirler.
5. HAFTALIK PİVOT ve önceki gün/hafta tepe-dip: kademe kanıtına ek çakışma kaynağı.
6. UYUMSUZLUK: swing tabanlı RSI/MACD pozitif-negatif ve gizli uyumsuzluk (günlük ve 4s).
7. MUM TEYİDİ: kademe bölgesinde çekiç, yutan mum, doji gibi son mum formasyonu; bölgeye gelişte teyit mumu yoksa "teyit bekleniyor".
8. AÇIK FİYAT BOŞLUKLARI (gap, FVG'den ayrı): son 60 günün doldurulmamış boşlukları hedef/mıknatıs olarak.
9. YAPI İPUCU: son 40 mumun tepe/dip regresyonu → yükselen/düşen kanal, sıkışan/yükselen/alçalan üçgen, yatay bant, genişleyen formasyon + bugünkü üst/alt çizgi seviyesi. Kural 31 çizimleri bu ipucundan başlar, gözle doğrulanır.
10. 52 HAFTA uzaklığı, ANCHORED VWAP (52 hafta dibinden ve son 6 ay tepesinden), ÖLÇÜMLÜ HAREKET hedefi (son salınım genişliği kadar).
11. RİSK/ÖDÜL: her k1 için (hedef - k1 orta) / (k1 orta - tez) hesaplanır ve yazılır; 2'nin altındaysa "risk/ödül zayıf" denir.
12. PİYASA REJİMİ (NDX mesajının başında): VIX seviyesi ve yönü, 10 yıllık faiz ve dolar yönü, NDX MTF hizalaması; rejim "riskten kaçış" ise yüksek betalı hisselerde kademe aralıkları bir alt bölgeye kaydırılır (mevcut kural 12 ile aynı yönde).
13. SEVİYE KARNESİ: her teknik analizde verilen k1/k2/tez invest/seviye_takip.csv'ye yazılır; Pazar performans raporu `python3 invest/ta_ek.py --karne` ile kademelerin tutma oranını hesaplar ve DERSLER.md'ye teknik ders olarak işler (iç ölçüm; tweette yalnız doğru çıkanlar, kural 23).
14. BİLANÇO YAKINLIĞI: takvim.md'de 10 gün içinde bilançosu olan hisseye "bilanço X tarihinde, opsiyonların fiyatladığı hareket ±%Y" notu (kural 22n verisiyle).

!!! KESİN KURAL 32 — UZUN GÖRÜŞ YAZISI (Enes 17.11 21:13 + 21:30 çerçeve havuzu, sablonlar.md 20: 10 farklı yapı, son 3 tekrar yok) !!!
- UZUN GÖRÜŞ YAZISI (kesin kural 32, Enes 17.11 21:13, örnek: "GÜNCELLENMİŞ $NBIS DÜŞÜNCELERİM" metni, invest/ORNEKLER.md bölüm 21): arada sırada (haftada 2-3, periyot.py uzun_gorus) tek uzun tweet. Konu: portföy, ilgi listesi ya da büyük yapay zekâ/yarı iletken/bulut şirketi; tercihen duyarlılığın sert değiştiği, çok konuşulan ama yanlış anlaşıldığını düşündüğümüz bir hisse. Yapı (başlıksız akan paragraflar, 6-9 paragraf): (1) ilk satır büyük harf başlık "GÜNCELLENMİŞ $TICKER DÜŞÜNCELERİM" ya da "$TICKER HAKKINDA DÜŞÜNCELERİM"; (2) ne oldu, duyarlılık nasıl değişti, dürüst bir giriş; (3) piyasanın endişeleri ve hangilerinin haklı olduğu (rakamlarla: gecikme, capex, rehber, finansman); (4) iyi giden taraf (marj, sözleşme, müşteri, nakit, ürün) rakamlarla; (5) takaslar ve riskler; (6) "uzun vadede haklı olmak, zamanlamada haklı olmak demek değil" türünden denge; (7) yönetimin göstermesi gerekenler (ölçülebilir); (8) net sonuç: uzun vadeli inanç + neye bakacağımız. Her rakam 2 kaynak (tek kaynaklı rakam yazılmaz). YASAK: al/sat tavsiyesi, "aldım/alım yapıyorum", pozisyon/ağırlık, hedef fiyat, emoji, hashtag, link, soruyla bitirme, etiketli görüş girişi ("Benim okumam:" vb.), deyim/mecaz yerine sade dil (kural 30), tutmayan eski tahmin (kural 23). "Bence" birkaç kez olabilir ama tekrar eden kalıp olmasın. Kart: editoryal ya da panel (son 3 düzen kuralı). Zaman: 21-24 ya da 12-15 dilimi (D-003). Tür UZUN-GORUS; DONGU ve performans_veri.csv'ye yazılır (ders sistemi bu türü ayrıca ölçer).

!!! KESİN KURAL 31 — TEKNİK ANALİZDE GEREKLİ ÇİZİMLER (Enes 17.11 21:01) !!!
- ÇİZİM GEREKTİĞİNDE MUTLAKA (kesin kural 31, Enes 17.11 21:01 + 21:03: "sıkışan kanallar, yükselen kanallar ve aklına gelebilecek her şeyi çizebilirsin demiştim, yapmadın" / "hepsinde gerekli olmayabilir tabii ki ama gerekli olanları yap"): grafikte belirgin bir yapı (kanal, sıkışma, formasyon) ya da kararı anlatan seviye varsa çizim YAPILIR; yoksa zorla çizilmez ve mesajda "belirgin bir formasyon yok" denir. Gerekli olduğunda: (a) yapı çizgisi: yükselen/düşen kanal (paralel kanal), sıkışan üçgen ya da takoz (iki yakınsayan trend çizgisi), yatay bant, bayrak; en az iki dip ve iki tepeye dokunmalı; (b) seviye çizgisi: kademe ve tez bozulma seviyeleri yatay ışın, destek/direnç ya da talep bölgesi kutu; gerekiyorsa (c) son ana salınıma Fibonacci düzeltmesi (OTE 0.618-0.786). Formasyonlar: yükselen/düşen kanal, simetrik/yükselen/alçalan üçgen, yükselen/alçalan takoz, bayrak/flama, çift dip/tepe, omuz-baş-omuz ve tersi, kırılım + geri test. Nasıl: TradingView kısayolları Alt+T trend çizgisi, Alt+J yatay ışın, Alt+H yatay çizgi, Alt+F Fibonacci, Alt+Shift+R dikdörtgen; paralel kanal sol araç çubuğundaki trend çizgisi grubundan "Paralel kanal". Tıklama noktalarını ekran görüntüsündeki fiyat ekseni etiketlerinden fiyat→piksel oranıyla hesapla (iki etiket arası doğrusal), çizimden sonra küçük ölçekli bakışla kontrol et, yanlışsa ctrl+z ile geri al ve düzelt. Görüntü çizimler ve 2 gösterge açıkken alınır; caption'da çizilen formasyon yazılır ("düşen kanal alt bandı 72", "sıkışan üçgen, tepe 2 gün sonra"). Tweet taslağında formasyon sade dille anlatılır (kural 30: "fiyat iki haftadır daralan bir üçgenin içinde, 190 üstüne çıkarsa yukarı kırılım olur"). Bitince tüm çizimler silinir (sağ tıklama → "Tüm çizimleri kaldır" ya da sol araç çubuğu çöp kutusu), sonra ctrl+s. Zaman darsa önce çizim, sonra gösterge rotasyonu kısaltılır; çizimsiz görüntü gönderilmez.

!!! KESİN KURAL 30 — TEKNİK ANALİZDE SADE DİL (Enes 17.11 20:19) !!!
- SADE DİL (kesin kural 30, Enes 17.11 20:19: "teknik analiz tweetlerinde hikâye biter vesaire gibi deyimler istemiyorum, sade bir dilde anlat"): teknik analiz tweet taslaklarında deyim, mecaz ve süslü ifade YOK. Yasak örnekler: "hikâye değişir/biter", "resim bozulur", "asıl sınav", "ters köşe", "top ... sahasında", "nefes alıyor/soluklanıyor", "bir alt kata iner", "kapı açılır", "fırtına", "yorgunluk". Yerine düz ve ölçülebilir cümle: "69'un altında günlük kapanış gelirse düşüş devam edebilir, ben o seviyeyi önemli sınır olarak görüyorum." / "Fiyat 72-74 arasına gelirse ilk alım bölgesi burası." / "Bu seviyenin altında bir sonraki destek 50-52."
- Bu dil kuralı "ben olsam" notlarında ve tweet taslaklarında da geçerli; teknik terim kullanılırsa parantez içinde sade karşılığı.
- 18:00 ve 23:30 bulut cron teknik kontrolleri 17.11 20:19'da kapatıldı (Enes "her şeyi hallet"); teknik analizler yalnız bu sohbetteki zincirden gelir.

!!! KESİN KURAL 29 — HER ŞEY BU SOHBETE (Enes 17.11 18:07: "her şeyin bu sohbete gelmesi lazım") !!!
- Bulut sabit görevleri (create_trigger cron) her çalışmada AYRI oturum açtığı için mesajları bu sohbete gelmiyordu. Bütün sabit görevler artık bu sohbette send_later ZİNCİRİ: her çalışma ilk iş `python3 invest/sonraki.py <anahtar>` ile bir sonrakini kurar, sonra invest/gorevler/_ORTAK.md + invest/gorevler/<anahtar>.md'yi uygular. 14 zincir: sabah, keylevels, radar, teknik1800, teknik2330, haftalikozet, sektor, ilgisira, analist, sezon, takvim, performans, ayinozeti, 13f.
- Bulut cron görevleri kapatıldı (enabled=false); 18:00 ve 23:30 bulut teknik kontrolünü kapatma izni verilmedi → Enes uygulamadan kapatacak (kapatılana kadar onlar da ayrı oturumda çalışır, tweet atmazlar).
- Sabah kontrolü zincirlerin hepsinin bekleyen görevi var mı bakar, kopan zinciri kurar. Teknik kontroller artık bu sohbette ve Chrome ile ekran görüntülü (kural 27).
- Hesap devrinde yeni oturum aynı 14 zinciri kendi sohbetinde kurar (HESAP_DEVRI 6).

!!! KESİN KURAL 28 — KREDİ TASARRUFU, KURALLAR AYNEN (Enes 17.11 17:41) !!!
- Hiçbir kural değişmez; tasarruf ekleme yoluyla: tur_basi.sh (tur başı tek çağrı), yayinla_gorsel.sh (push + raw 200), kayit.py (DURUM/DONGU/performans/csv/periyot/push tek çağrı), paralel çağrı, tek ToolSearch, grep ile okuma, büyük çıktıyı dosyada süzme, standard arama önce, Chrome get_page_text önce ve browser_batch, Buffer metriksiz kontrol. Ayrıntı: skills/enes-tweet-turu.md bölüm 15. Çelişkide kural kazanır.

!!! KESİN KURAL 26 — ÖLÇ, DERS AL, UYGULA (Enes 17.11 17:18: "kontrol edeceksin, ders alacaksın, bir sonrakileri ona göre yapacaksın") !!!
- invest/DERSLER.md: performanstan çıkan dersler (kısa, uygulanabilir maddeler, tarih + kanıt). Her tur konu seçmeden ve yazmadan önce DERSLER.md'nin "AKTİF DERSLER" bölümünü okur ve uygular.
- Döngü: (1) Her gün 09:00 sabah görevi önceki günün tweet metriklerini performans.md'ye yazar ve önceki güne göre dikkat çeken 1-2 gözlemi DERSLER.md "Gözlemler"e ekler. (2) Her Pazar 21:30 performans raporu: gözlemleri en az 2 hafta ve 5+ tweetle destekleniyorsa "AKTİF DERSLER"e taşır, tutmayanları siler, Enes'e "bu hafta öğrendiklerim" 3-5 madde. (3) 3 haftada bir (periyot.py karisim_onerisi) içerik karışımı yeniden önerilir. (4) Deney: bir ders belirsizse 1 hafta A/B dener (ör. aynı tür 12-15 vs 18-21), sonuç DERSLER.md'ye.
- TAM PROTOKOL (17.11 17:24): DERSLER.md başı. Veri performans_veri.csv, ölçü ders_analiz.py (göreli skor, medyan), eşik ≥8 tweet / ≥2 hafta / ≥%25 / aynı yön, seviyeler gözlem→aday→aktif→sağlam, çakışmada A/B deney, 4 haftada yeniden test, %10-15 keşif.
- Ders, kuralları (al/sat yok, 2 kaynak, kural 23, kural 25) değiştiremez; yalnız konu, saat, biçim, uzunluk, kart ve adet tercihlerini değiştirir.

!!! KESİN KURAL 27 — TEKNİK ANALİZ EKRAN GÖRÜNTÜLERİNİ CLAUDE ALIR (Enes 17.11 17:18) !!!
EKRAN GÖRÜNTÜSÜNÜ CLAUDE ALIR VE GÖNDERİR (kesin kural 27, Enes 17.11 17:18: "artık teknik analizlerde ben almayacağım, sen atacaksın"; eski kural 5f kaldırıldı). Chrome bağlıysa her teknik analizde (18:00/23:30 kontrol + TradingView teyidi, Enes'in istediği analizler) her hisse için: TradingView'da `...chart/QdeLE4v4/?symbol=<BORSA>%3A<TICKER>&interval=<dilim>` aç, 8-10 sn bekle, çıkan ipucu/popup'ı kapat ("Tamam"/X), alt çubuktan uygun aralık (4s için 3A, günlük için 6A/1Y, 1s için 5G), kararı en çok belirleyen 2 gösterge açık (basic plan sınırı; rotasyonla çizimler: destek/direnç kutuları, trend çizgisi, Fibonacci, kademe seviyeleri yatay ışın olarak), fareyi grafikten çek (sağ fiyat eksenine hover) ki imleç çizgisi görünmesin, `computer zoom` ile yalnız grafik alanını (sol araç çubuğu ve sağ izleme listesi hariç, ör. region [52,40,992,860]) `save_to_disk: true` al, dönen yolu `SendUserFile` ile Enes'e gönder (caption: "$TICKER 4 saatlik: RSI 14 + OBV, 79-84 bölgesi"). Sıra (5d): o hissenin ekran görüntüsü → hemen ardından o hissenin tweet taslağı + ben olsam notu; sonra sıradaki hisse. Gerekirse ikinci dilim için 2. görüntü. Bitince çizimleri sil ya da kaydetmeden çık (düzeni bozma), varsayılan Supertrend + SMC'yi geri koy, ctrl+s, sekmeyi kapat. Chrome yoksa (bulut sabit görevler): ekran görüntüsü yerine eski talimat satırı ("TradingView'da $TICKER aç → dilim → göstergeler → bölge") yazılır ve 'Chrome bağlı değil, görüntü alamadım' denir. Görüntüler YALNIZ Enes'e; tweete Claude teknik görsel koymaz, teknik analiz tweetini Enes atar.

!!! KESİN KURAL 25 — FİKİR ÖNCELİKLİ İÇERİK !!!
KESİN KURAL 25 (Enes 17.11 16:51, "insanlar bizi haberlere ulaşmak için takip ediyor ama asıl takip ettiği şey bizim fikirlerimiz, olaylara dair düşüncelerimiz"): Haberi vermek yetmez; her haber ve veri tweetinin ağırlığı YORUMDUR (yaklaşık üçte biri haber, üçte ikisi düşünce). Okur tweeti bitirdiğinde şu sorulara cevap almış olmalı: (1) Bu ne demek, sade dille? (2) Neden şimdi önemli, büyük resimde neye işaret ediyor (büyüme, enflasyon, tüketici, şirket kârları, yapay zekâ döngüsü)? (3) Fed ne düşünür, faiz beklentisi nasıl değişir (FedWatch/vadeli fiyatlama, 2 kaynak)? (4) Piyasaya, sektörlere ve takip edilen hisselere etkisi ne? (5) Bizim net düşüncemiz ne? Makro veri tweeti TEK tweet olsa bile bu beşini içerir; ayrı 'sonuç' ve 'etki' tweeti yerine tek, yorumlu tweet. Bilanço rakam tweeti yorumsuz kalır ama 15 dk sonraki analiz tweeti bu beş soruyu cevaplar. Görüş etiketsiz, düz cümleyle (kural 11), al/sat yok, tahmin dili ölçülü.

!!! KESİN KURAL 24 (Enes 17.11 16:33, "her pazar, üç haftada bir dediklerimizi sohbet değişince diğer sohbet nasıl anlayacak, düzelt"): PERİYOT DEFTERİ !!!
- invest/periyot.json + invest/periyot.py. Haftada/ayda/N günde bir, "günde en çok N", "haftada 3-5", "ayın ilk Pazarı", "3 haftalık veri olunca", "her 5 karnede bir", "sözlük cümlesi 2 hafta tekrar yok" gibi her kural defterden kontrol edilir; hafızadan ya da DONGU'dan (7 günde arşivlenir) değil.
- Her tur/görev başında `python3 periyot.py durum`; iş yapılınca `python3 periyot.py yap <anahtar> "<not>"` + push. Yeni periyodik kural: `periyot.py ekle`. Ayrıntı: skills/enes-tweet-turu.md bölüm 13.
- ETİKETLİ TEKRAR KONTROLÜ (17.11 21:35, Enes: "farklı sohbete geçince tarihleri bilemez, kalıcı çözüm"): "son N günde/son N kayıtta aynısı olmasın" kuralları da hafızadan değil periyot.json'dan: `python3 invest/periyot.py etiket kontrol <grup> <değer> <gün> [son_n]` (çıkış 0 = uygun), kullanınca `etiket yap <grup> <değer>`. Gruplar: aday (teknik analiz adayı, 5 gün), cerceve (uzun yazı çerçevesi, son 3 kayıt: `etiket kontrol cerceve B 0 3`), uzun_ticker (uzun yazı hissesi, 30 gün). Yeni benzer kural gelirse yeni grup açılır. Haftalık alt sınırı olan işler `periyot.py durum`da "YAPILMALI" ya da geride kalınca "ACIL BUGUN YAP" yazar; tur_basi.sh bunu her turda gösterir, tur o işi o gün planlar.
- Sabit cron görevleri hesaba bağlıdır, sohbet değişince silinmez ve saatleri doğru çalışır; yalnız oturuma bağlı send_later zinciri devirde yeniden kurulur.

!!! KESİN KURAL 23 (Enes 17.11 14:35): YALNIZ DOĞRU ÇIKANLAR. Enes: "yanıldıklarımızı paylaşma, sadece bildiklerimizden bahsedilecek." Eski "yanılınca açıkça söyle (şunu demiştim, olmadı)" kuralı KALDIRILDI. Tutmayan tahmin, beklenti ya da "ben olsam" notundan tweette bahsedilmez; tutan tahmin bağlama uyuyorsa söylenebilir. Önizleme tahminleri DONGU'ya iç kayıt olarak yine yazılır. AYRI KONU: atılmış tweetteki yanlış RAKAM/BİLGİ için kural 21 DÜZELTME aynen geçerli (Enes'in 13:28 isteği).

!!! KESİN KURAL 17 — HESAP KİLİDİ VE HESAP DEVRİ (17.11 13:11, Enes: "hakkım bitince arkadaşımın hesabından devam edeceğim, orada skill vs hiçbir şey yok; tek seferde kopyalayabileceğim bir şey yaz, aynılarını yapsın, olası bütün sorunları düşün") !!!
- invest/AKTIF_HESAP.md: "AKTIF: A" (A = Enes'in hesabı, B = arkadaşının hesabı). Her tur/görev/yayın EN BAŞTA bu dosyayı okur; kendi mesajındaki HESAP=<etiket> farklıysa hiçbir şey yapmaz (tweet yok, push yok) ve kendi tekrarlayan görevlerini kapatır. Bütün görev ve send_later mesajları HESAP=<etiket> içerir.
- Başka hesaba geçiş: invest/HESAP_DEVRI.md (sıfırdan kurulum, kontrol listesi, sorun tablosu). Skill'lerin kopyası invest/skills/ altında; skill değişince kopya da güncellenir.
- Her commit'ten önce `git pull --rebase -q` (iki oturum aynı anda yazabilir), --force yok. Paylaşmadan hemen önce Buffer son 3 gönderi + DONGU son satır kontrolü: son 20 dk içinde aynı konu varsa atma.

!!! YENİ KESİN KURALLAR 14-16 (17.11 12:54, Enes: "2'yi yap kesinlikle, 3'ü de yap, 6'yı da yap; bilanço gibi haberlerde araştırdın bulamadın, sonra açıklandı, sonraki tur 5 dk sonra olduğu için geç paylaşmış oluruz, tweetin değeri kaybolur, bizden önce başka hesaplar paylaşır; ona da çözüm bul") !!!
14) PERFORMANS RAPORU (hangi tweet işe yarıyor):
   - Kayıt: invest/performans.md. Her tweet DONGU'da TÜR ile kayıtlı (VADELI, 13F, BILANCO-RAKAM, BILANCO-ANALIZ, BILANCO-ONIZLEME, ANALIST, SONDAKIKA, BAGLAM-GORUS, KAPANIS, TAKVIM, EGITICI, ENES-ISTEGI). Yeni tweetlerde DONGU satırında tür bu listeden yazılır.
   - Her gün ilk turda (09:05) önceki günün tweetleri için Buffer get_post(includeMetrics true) ile görüntülenme, beğeni, yanıt, repost çekilir, performans.md tablosuna eklenir (metrikler ~24 saatte tazelenir; gerekirse get_aggregated_post_metrics).
   - Her Pazar 21:30 TSİ haftalık rapor (sabit görev, kural 15): türe göre ortalama görüntülenme ve etkileşim oranı, en iyi 5 / en kötü 5 tweet, saat dilimine göre performans, kart düzenine göre performans; sonuç ve ÖNERİLEN İÇERİK KARIŞIMI Enes'e mesaj. Enes onaylarsa tür ağırlıkları DEVIR ve skill'e işlenir. Tek haftalık veriyle kesin karar verilmez, 3 haftalık trende bakılır.
15) SABİT SAATLİ GÖREVLER (zincir kopmasın):
   - Tekrarlayan görev (create_trigger, cron, CRON_TZ=Europe/Istanbul) olarak kurulur: (a) Teknik kontrol 18:00 hafta içi, (b) Teknik kontrol 23:30 hafta içi, (c) Haftalık bilanço takvimi Pazar 20:00, (d) Haftalık performans raporu Pazar 21:30, (e) Günlük key levels + başlıklar 10:30 hafta içi (kural 13; şu an zincir, sabit göreve çevrilir), (f) Çeyreklik 13F serisi başlangıcı: 15 Şubat, 16 Mayıs, 15 Ağustos, 15 Kasım 09:05 (hafta sonuna denk gelirse ilk turda başlar), (g) Günlük sabah kontrolü 09:00 (DURDUR, zincir canlı mı, takvim, performans çekimi).
   - Her görev mesajı bağımsız ve tam olmalı (yeni oturumda ateşlenebilir): repo yolu, ilgili skill adı, DEVIR_TAM v8 özeti, DONGU kontrolü, DURDUR kuralı.
   - Rastgele aralıklı otomatik paylaşım turu ZİNCİR olarak kalır (20-40 dk). Ama (g) sabah kontrolü zincir kopmuşsa (son otomatik tur > 60 dk önce ve 09:00-01:00 arası) zinciri yeniden kurar ve Enes'e söyler.
   - ABD tatillerinde (26.11 Şükran Günü, 25.12, 1.1 vb.) teknik kontrol görevi çalışınca "piyasa kapalı" diye kısa not düşer, analiz yapmaz. Yarım günlerde (27.11, 24.12) 23:30 kontrolü 20:30'da yapılır (o gün tek seferlik görev kurulur).
   - Kurulan görevlerin ID'leri DEVIR_TAM bölüm 16'ya yazılır; devirde eski oturum bunları siler, yeni oturum yeniden kurar (ya da görev oturumdan bağımsızsa korunur, list_triggers ile kontrol).
16) BİLANÇO TAKVİMİ VE HIZ PROTOKOLÜ (tweetin değeri ilk dakikalarda):
   - KURAL 13 İLE BİRLEŞİM: kural 13'teki "başlık açıklanınca +3 dk tek seferlik tur" yerine bilanço ve saati belli veri başlıklarında bu protokol uygulanır (hazırlık T-45/60 dk + yayın T-2 dk ve 45-60 sn arayla izleme). 10:30 key levels tweetindeki başlıklar takvim.md'ye de yazılır.
   - TAKVİM: invest/takvim.md. Her Pazar 20:00 (ve her gün 09:05 güncelleme) gelecek 7 günün bilançoları: portföy (DOCN RKLB SITM AXON CBRS VRT AVGO), ilgi listesi, büyük yapay zekâ/yarı iletken/bulut/uzay/büyük teknoloji ve piyasayı oynatacak diğerleri (HD, WMT, TGT, DIS, büyük bankalar vb.). Her satır: şirket, tarih, AÇIKLAMA SAATİ TSİ (şirketin IR duyurusu ya da önceki çeyreklerin saati; "açılış öncesi" ise şirketin tipik saati, ör. HD 06:00 ET), konferans saati, beklenti (gelir, HBK, şirkete özgü 2-3 metrik, 2 kaynak), bülten kaynağı (IR sayfası URL'si, GlobeNewswire/Business Wire/PR Newswire), son 4 çeyrekte açıklama dakikası. Saat 1 kaynakla bile olsa yazılır, belirsizse "tahmini" işaretlenir.
   - Her bilanço için iki tek seferlik görev, takvim yazılırken HEMEN kurulur (send_later; gece 01:00-09:00 dahil, bilinen açıklama istisnası):
     a) HAZIRLIK TURU: açıklamadan 45-60 dk önce. Beklentileri 2 kaynakla son kez doğrula; tweet iskeletini (CRWV formatı, gerçek rakam alanları boş) ve skor kartı kodunu /tmp/hazir_<ticker>.py olarak HAZIR yaz (yalnız gerçek rakamlar girilecek); bülten kaynak URL'lerini hazırla; DONGU'ya "HAZIR: <ticker>".
     b) YAYIN TURU: açıklama saatinden 2 dk ÖNCE başlar. Döngü: en çok 30 dk boyunca 45-60 sn arayla bülten kaynaklarını kontrol et (WebFetch şirket IR haber sayfası / GlobeNewswire veya Business Wire şirket sayfası; WebSearch "<şirket> reports third quarter results"; Yahoo chart includePrePost=true ile mesai dışı fiyatta ani sıçrama = açıklama işareti). Bülten bulunur bulunmaz rakamları BÜLTENDEN al, hazır karta gir, Read ile tek bakış, push, raw URL 200, Buffer shareNow. Hedef: bülten çıktıktan sonra 3-5 dk içinde yayında.
   - KAYNAK İSTİSNASI — ONAYLANDI (17.11 12:58, Enes: "bilanço rakam tweetinde şirketin kendi resmi bülteni tek başına yeterli sayılsın, ikinci kaynak teyidi yayından sonraki 10 dakika içinde yapılsın"). GEÇERLİ KURAL: bilanço RAKAM tweetinde şirketin kendi resmi bülteni (IR/bülten servisi/SEC 8-K) birincil ve TEK BAŞINA yeterli kaynak sayılır; beklentiler önceden 2 kaynakla doğrulanmış olur. Yayından sonra 10 dk içinde ikinci kaynakla (Reuters/CNBC/Benzinga) teyit; fark varsa Enes'e söyle, gerekirse düzeltme tweeti.
   - Otomatik zincirle çakışma: yayın turu zincirden bağımsızdır, 20 dk kuralına takılmaz. Bekleyen otomatik tur yayın saatine ±15 dk denk geliyorsa update_trigger ile yayından 20+ dk sonraya kaydırılır.
   - Analiz turu: rakam tweetinden 15 dk sonra (enes-bilanco-13f). Konferans görüşmesinde önemli bir açıklama (rehber değişikliği, CEO sözü) çıkarsa ayrı kısa tweet.
   - BEKLENMEDİK HABER HIZI: takvimde olmayan son dakika haberleri için her otomatik turun ilk işi son 30 dk taraması; bulunduğu anda tur beklenmeden atılır (zaten kural). Ayrıca bilinen olay saatleri (Fed kararı, TÜFE, istihdam, büyük konuşmalar) takvim.md'ye yazılır ve aynı hazırlık + yayın protokolü uygulanır (veri 2 dk önce izlenir, açıklanınca 3-5 dk içinde).

!!! KESİN KURALLAR (Enes 16.11 13:54-13:56, "bir sonraki devirde kesinlikle bu şekilde devam edilecek") !!!
1) PORTFÖY GÜNCELLEMESİ TWEETİNİ ENES ATAR. Claude portföy güncellemesi tweeti/kartı HAZIRLAMAZ, ATMAZ, SORMAZ. Eski "günlük portföy sorusu" görevi durduruldu, yeniden KURULMAZ. (bölüm 1)
2) (tam test: 21 gösterge x 4 dilim, ta2.py -v + TradingView 2'şerli rotasyon, bölüm 13) GÜNDE 2 SABİT TEKNİK KONTROL: her ABD işlem günü 18:00 TSİ (açılış +30 dk) ve 23:30 TSİ (kapanış -30 dk). Portföyün tamamı + Claude'un yatırıma uygun bulduğu en iyi 3-4 hisse. 21 gösterge, 4 zaman dilimi, TradingView varsa. Enes'e her seferinde "ben olsam" kararlarıyla mesaj (değişiklik olmasa da). Tweet değil. (bölüm 14b)
3) HİSSE SEÇİMİ PROFESYONEL YÖNTEMLE: temel (13 maddelik kontrol listesi) + teknik (bölüm 13) puan kartı; adaylar portföyle aynı kartla karşılaştırılır; daha iyisi varsa önerilir, yoksa önerilmez. (bölüm 14c)
3b) TEMEL KARNE ÖNCEDEN HAZIR OLUR (16.11 18:14, Enes: "neden temelleri yapmadın, turlarda vaktin vardı"). Temel analiz 18:00/23:30 kontrolünün içine SIKIŞTIRILMAZ. Otomatik turlarda, tweet atıldıktan sonra her turda 1-2 hissenin temel kartı invest/temel_karne.md dosyasına yazılır/yenilenir (bölüm 14g). Kontroller kartı buradan okur. "Temel puan kartı kısmi" diye geçmek YASAK; kart eksikse kontrol mesajında hangi hissenin eksik olduğu açıkça yazılır ve bir sonraki tur o hisseyle başlar.
3c) TEMEL KARNE = PROFESYONEL DERİNLİK (16.11 18:19, Enes: "daha çok metrikle, profesyonel bir borsacı gibi çok fazla detaya bak"). Karne bölüm 14h'deki GENİŞLETİLMİŞ METRİK LİSTESİYLE yapılır: 10 başlık, ~120 metrik, sektöre özel KPI'lar, değerleme senaryoları (ayı/baz/boğa), akran karşılaştırması. Puan 10 başlık x 1-5 = /50. 14c-A ve 14g aynen geçerli, 14h onların üstüne eklenir.
3d) TEMEL KARNE ÖZ-DENETİMİ (16.11 21:16, Enes: "sürekli temel analiz yaparken yanlış veya adaletsiz sonuç nasıl çıkar düşün, ne eklenebilir düşün ve gittikçe geliştir"). Her karne yazıldıktan sonra bölüm 14i HATA/ADALETSİZLİK KONTROL LİSTESİ tek tek uygulanır, bulunan sorun karnede düzeltilir ve 14i-D HATA GÜNLÜĞÜ'ne yazılır. Her 5 karnede bir (ve her gün ilk turda) tüm tablo birlikte yeniden kalibre edilir (14i-C). Liste sabit değildir: her yeni hata türü 14i-A'ya yeni madde olarak eklenir (gittikçe geliştir).
4) TEKNİK ANALİZ TWEETİ: 'bence dibe yakın / ben şuradan kademe eklerim, orayı kırarsa şuradan' dili serbest; tavsiye ve emir kipi yok; sade konuşma dili. (bölüm 6)
5b) TEKNİK ANALİZ GÖRSELİ = TRADINGVIEW EKRAN GÖRÜNTÜSÜ (16.11 18:05, Enes: "kendin oluşturma teknik analiz görsellerini, ss at bana"). Kendi çizdiğimiz grafik (ta_grafik.py) teknik analiz görseli olarak GÖNDERİLMEZ. Her hisse için TradingView (UN09ZFN8) ekran görüntüsü alınır (gerekirse ilgili dilim ve göstergeler), SendUserFile ile gönderilir. tk_auto.py yalnız seviye hesabı için kullanılır. Bilgisayar/Chrome kapalıysa görsel gönderilemez, Enes'e söylenir. (eski: matplotlib grafik)
5d) GÖNDERİM SIRASI (16.11 18:09, Enes: "tweet ekran görüntüsü tweet ekran görüntüsü"): her hisse SIRAYLA gönderilir: önce o hissenin TradingView ekran görüntüsü (SendUserFile, başlık "1/10 RKLB" gibi), HEMEN ARDINDAN o hissenin tweet taslağı (SendUserMessage, sadece tweet metni, kopyalanmaya hazır). Görseller toplu, tweetler ayrı mesajda GÖNDERİLMEZ. Sonra kısa özet mesajı.
5e) EKRAN GÖRÜNTÜSÜNDE KARARI BELİRLEYEN GÖSTERGELER AÇIK OLUR (16.11 21:41, Enes: "sadece o ikisi açıkken yapma, karar vermende en etkili indikatörler açıkken yap"). Her hissenin TradingView ekran görüntüsü, varsayılan Supertrend + SMC ile DEĞİL, o hissenin kararını en çok belirleyen 2 gösterge açıkken ve kararı belirleyen dilimde alınır (ör. DOCN'da OBV uyumsuzluğu + RSI belirleyiciyse onlar açılır; kademe seviyesi FVG + Supertrend çakışmasından geliyorsa SMC + Supertrend). Belirleyici gösterge 2'den fazlaysa 2'şerli birden fazla görüntü (en çok 2-3). Hangi göstergelerin açık olduğu görselin başlığında yazılır ("1/10 RKLB - 4s - OBV + RSI"). Bitince varsayılan düzen (Supertrend + LuxAlgo SMC) geri kurulur, ctrl+s. (eski: görüntüler varsayılan Supertrend + SMC ile alınıyordu)
5f) (KALDIRILDI 17.11 17:18, yerine kesin kural 27: ekran görüntüsünü CLAUDE alır ve gönderir) ESKİ: EKRAN GÖRÜNTÜSÜNÜ ENES ALIR (16.11 21:43, Enes: "ekran görüntüsü alma, bana şunu de: gir, şu zaman diliminde şu şu indikatörler açıkken ekran görüntüsü al; ben alayım. Sen sadece tweeti yaz, düşüncelerini yaz"). Claude TradingView ekran görüntüsü ALMAZ, göndermez. 18:00/23:30 kontrollerinde HER hisse için SIRAYLA tek mesaj (SendUserMessage): (1) EKRAN GÖRÜNTÜSÜ TALİMATI: "TradingView'da $TICKER aç → [dilim, ör. 4 saatlik] → şu göstergeler açık olsun: [kararı en çok belirleyen 2 gösterge, ayarlarıyla, ör. RSI 14 + OBV] → [gerekirse 2. görüntü: dilim + 2 gösterge]" ve görüntüde neye bakılacağı (ör. "79-84 bölgesi ve OBV'nin yükselen dipleri görünsün"); (2) TWEET TASLAĞI (kopyalanmaya hazır, bölüm 6 TA dili, seviyelerin gerekçesiyle); (3) DÜŞÜNCELERİM: "ben olsam" kararı, ekleme/azaltma bölgeleri, tezin bozulduğu seviye, hedef, portföyle/adaylarla kıyas, temel /50 ve /45. Göstergeler Claude'un kendi 21x4 tam testiyle (ta2.py -v) ve gerekirse Chrome'da TradingView'da OKUNARAK belirlenir; okumak serbest, görüntü göndermek yok. Talimattaki göstergeler kararı belirleyen göstergelerdir (kural 5e mantığı). Sonunda kısa özet + kıyas mesajı. (eski: 5b/5d/5e — Claude TradingView ekran görüntüsünü alıp SendUserFile ile gönderiyordu; 21:43'ten itibaren İPTAL, 5e'nin 'belirleyici gösterge' mantığı talimatta yaşar)
9) GÜNLÜK TWEET SINIRI KALDIRILDI (16.11 22:48, Enes: "tweet sınırını kaldır"). Günde 45 (eski 40) tavanı YOK. Geçerli olanlar aynen: otomatik turlar arası 20-40 dk rastgele, 01:00-09:00 TSİ paylaşım yok (bilinen açıklama istisnası), aynı ticker 3 saat, tekrar yok, her rakam 2 kaynak. Bilgi: Buffer planı aylık ~1000 gönderi (Enes 16.11); günlük sayım yalnız takip için DONGU'ya yazılır, paylaşımı durdurmaz. Aylık sayım 900'ü geçerse Enes'e söylenir. (eski: 'Günde en fazla 45', A6 'Buffer günlük 45 doldu -> ertesi gün 09:05')
10) 13F SERİSİ — HER YATIRIMCI İÇİN AYRI GÖRÜŞLÜ TWEET (17.11 02:31, Enes: "13F dosyalarına bak, açıklanmış; farklı farklı isimler için yaptığı değişiklikleri söylediğin ve bu değişikliklerle ilgili yorumlarını söylediğin tweetler yaz, çok fazla kişi açıklamış, her kişi için ayrı ayrı yap, hepsinde görüş bildir; bir sonraki açıklamalarda da ben söylemeden bunları sen kendin paylaş"). KESİN KURAL:
   - Her çeyreğin 13F son gününden sonraki ilk turlarda (yaklaşık 14-17 Şubat, 15-18 Mayıs, 14-17 Ağustos, 14-17 Kasım; tatil/hafta sonunda bir sonraki iş günü) Enes'e sormadan 13F serisine başlanır.
   - Liste (bulunabildiği kadar, öncelik sırasıyla): Berkshire Hathaway (Greg Abel), Scion (Michael Burry), Pershing Square (Bill Ackman), Duquesne Family Office (Stanley Druckenmiller), Appaloosa (David Tepper), Soros Fund Management, Bridgewater, Third Point (Dan Loeb), Greenlight (David Einhorn), Coatue (Philippe Laffont), Tiger Global, Lone Pine, Viking, Baupost (Seth Klarman), Himalaya (Li Lu), Pabrai, Icahn, Elliott, Renaissance, Citadel (sadece belirgin hareket varsa) + o çeyrekte gündem olan diğer isimler.
   - HER KİŞİ İÇİN AYRI TWEET, her otomatik turda 1 kişi (turlar arası 20-40 dk kuralı geçerli; 13F serisi o günlerde öncelikli konu, son dakika haberi çıkarsa araya girer). Sıra: en çok merak edilen ve en büyük değişikliği olan önce.
   - İçerik: yeni pozisyonlar, tamamen çıkılanlar, en büyük artırma ve azaltmalar (hisse adedi ve/veya değer, portföy payı), portföy değeri. Tablo değil düz metin + kart (panel/bento/skor/ilerleme gibi uygun düzen; ticker'lar $ ile, logo).
   - GÖRÜŞ ZORUNLU (bölüm 6 "bağlam + görüş" tarzı, ORNEKLER 18): hareketin olası mantığı, kişinin bilinen yaklaşımıyla ve piyasa durumuyla bağlantısı, dikkat edilmesi gereken nokta. 13F'nin 45 gün gecikmeli olduğu, sadece ABD hisse uzun pozisyonlarını gösterdiği (açığa satış, opsiyonların yönü ve yabancı hisseler eksik olabilir) gerektiğinde tek cümleyle söylenir. Al/sat tavsiyesi yok; "X aldı, siz de alın" dili yok.
   - Doğrulama: rakamlar EDGAR 13F-HR (birincil) + 1 haber/izleme kaynağı (CNBC, Reuters, Bloomberg, WhaleWisdom, 13f.info, Dataroma, HedgeFollow, Fintel, Investing, Yahoo, Benzinga). Çeyrek ve yıl kontrolü (14i-A3: önceki çeyreğin haberleri sık karışır). Pozisyon değerleri çeyrek sonu fiyatıyladır, bugünkü değil — gerekirse söylenir.
   - DONGU'ya "13F SERİSİ: [isim] atıldı / sıradaki: ..." satırı; seri bitince Enes'e kısa özet (kim ne yaptı, ortak temalar).
   - Enes'in portföyündeki hisselerde (DOCN RKLB SITM AXON CBRS VRT AVGO) büyük yatırımcı hareketi varsa Enes'e ayrıca "ben olsam" notu.

11) ETİKETLİ GÖRÜŞ GİRİŞİ YASAK (17.11 10:40, Enes: "'benim okumam:' gibi ifadeleri kaldır, kurala da ekle, çok yapay zekâ yazmış gibi duruyor"). KESİN KURAL — tweet, flood, DM taslağı, her metin:
   - Görüş paragrafı etiketle/başlıkla açılmaz. YASAK: "Benim okumam:", "Benim görüşüm:", "Görüşüm:", "Yorumum:", "Bence önemli nokta şu:", "Asıl ilginci", "Burada kritik olan", "İşin özü", "Not:" (sonda açıklama etiketi), "Önemli nokta:", "Peki ne anlama geliyor?" ve iki noktalı her benzeri.
   - Görüş, rakamlardan sonra doğrudan cümleyle gelir. Örnek: YANLIŞ "Benim okumam: Abel'in tercihleri ayrışıyor." DOĞRU "Abel'in tercihleri Buffett döneminden ayrışmaya başladı."
   - 13F uyarısı gerekiyorsa etiketsiz düz cümle: "Tablo 30 Eylül itibarıyla, sonrasındaki işlemler dosyada yok."
   - Gönder öncesi kontrol: metinde "kelime(ler) + iki nokta" ile başlayan satır var mı? Varsa yeniden yaz (ticker listeleri ve portföy güncellemesi başlığı hariç).

12) TEKNİK KONTROLDE NASDAQ ENDEKSİ DE ANALİZ EDİLİR (17.11 11:10, Enes: "yeni kural: TradingView teknik analizinde Nasdaq'ta bak" → seçim: "Nasdaq endeksini de ekle"). KESİN KURAL — 18:00 ve 23:30 teknik kontrollerinin HEPSİNDE:
   - İLK mesaj Nasdaq 100: `python3 invest/ta2.py -v ^NDX` (21 gösterge x 4 dilim) + Chrome bağlıysa TradingView'da OKUYARAK teyit (sembol NASDAQ:NDX; açılmazsa QQQ ya da NQ1!). Aynı 3 parçalı format (kural 5f): ekran görüntüsü talimatı (TradingView'da NDX → dilim → kararı belirleyen 2 gösterge → görünecek bölge), tweet taslağı, düşüncelerim (endeks dibe yakın mı, destek/direnç bölgeleri, trend bozulma seviyesi).
   - Sonra her hisse mesajında endeksle KIYAS: hisse endeksten güçlü mü zayıf mı (aynı dilimlerde yön, RSI, Supertrend, son 5 gün ve 1 ay % farkı), endeks desteğe gelirse hisse ne yapar. Yüksek betalı hisselerde (RKLB, CBRS, DOCN) endeks yönü ekleme kararına bağlanır.
   - Özet + kıyas mesajına (14c-D) "Nasdaq durumu" satırı eklenir; endeks ana desteği kırmışsa kademe ekleme önerileri bir alt bölgeye kaydırılır ya da beklenir.
   - Hisse sembolleri değişmez (DOCN, VRT: NYSE; CBRS önek yok; diğerleri NASDAQ).

13) GÜNLÜK KEY LEVELS + GÜNÜN ÖNEMLİ BAŞLIKLARI (17.11 12:45, Enes: "her gün aynı saatte key levelları yapmanı, önemli başlıkları yazmanı istiyorum ve bu başlıklar açıklanınca onunla ilgili tweet yazmanı da istiyorum; devirde yeni sohbete geçerken bu kural da yapılsın"). KESİN KURAL:
   - SAAT: her ABD işlem günü 10:30 TSİ (sabah notu slotu; ABD verileri ve açılış öncesi bilançolardan önce). Hafta sonu/tatil yok (26.11 Şükran Günü yok). Saati Enes değiştirebilir.
   - TWEET (otomatik, Buffer shareNow, kart ile): (a) KEY LEVELS: S&P 500 ve Nasdaq 100 için önceki kapanış + vadeli yönü, 2 destek ve 2 direnç; seviyeler ta2.py (^GSPC, ^NDX; 21 gösterge x 4 dilim) çakışmalarından gelir, her seviyenin sade gerekçesi tek kısa ifade ("önceki dip", "200 günlük ortalama", "doldurulmamış boşluk"). Yalnız en az 2 gösterge/dilim çakışan seviye yazılır. Al/sat, emir kipi, "hedef fiyatım" yok; dil "şu seviye kırılırsa satış hızlanabilir" gibi gözlem. (b) GÜNÜN ÖNEMLİ BAŞLIKLARI: o gün açıklanacak makro veriler (saat TSİ + beklenti), önemli bilançolar (açılış öncesi/kapanış sonrası, HBK ve gelir beklentisi), Fed konuşmaları/tutanak, büyük şirket etkinlikleri, 13F/vade/endeks olayları. En fazla 5-6 başlık, saat sırasıyla. Her saat ve beklenti 2 kaynak (takvim: Investing, TradingEconomics, Earnings Whispers, Nasdaq, Yahoo; resmi: BLS/BEA/Census/Fed). Uzunsa tek uzun tweet; kart düzeni isi/takvim/dortlu/zaman (son 3 düzen kuralı geçerli).
   - BAŞLIK AÇIKLANINCA TWEET: 10:30 turunda saati belli her başlık için o saat +2-5 dk'ya ayrı tek seferlik send_later kurulur (ad: "Başlık açıklandı: <başlık>"); bu tur sonucu 2 kaynakla doğrulayıp yorumsuz RAKAM tweeti atar (veri: "beklenti → sonuç"; bilanço: CRWV formatı, enes-bilanco-13f), sonra gerekirse etki/analiz turu (bilançoda 15 dk sonra). Sonuç henüz yayınlanmadıysa 5-10 dk sonrasına kendini yeniden kurar (en çok 3 kez). Kapanış sonrası 01:00 TSİ'den önceki açıklamalar bilinen açıklama istisnasıdır (NVDA ~00:20 gibi). Saati belirsiz başlıklar (ör. "gün içinde") otomatik turlarda öncelikli olarak kontrol edilir.
   - Bu tweetler ve başlık-açıklandı tweetleri otomatik zincirin zamanlamasını DEĞİŞTİRMEZ; normal turlar 3 saat ticker ve tekrar kuralıyla aynı konuyu yeniden atmaz.
   - ZİNCİR: send_later adı "Günlük key levels + başlıklar"; her çalışma sonunda sıradaki ABD işlem gününün 10:30 TSİ'sine kendini kurar. Her otomatik tur list_triggers ile kontrol eder, yoksa kurar.
   - DONGU'ya "- SS:DD (GG.AA) AUTO (KEY LEVELS+BAŞLIKLAR): ... | başlıklar: <liste ve saatleri> | kurulan başlık turları: ..." satırı.
   - DEVİR: yeni oturum A5'te bu zinciri MUTLAKA kurar; devir notu yeniden yazılırsa bu kural aynen korunur.

5) TEKNİK ANALİZ TWEETLERİ: her kontrolde bakılan HER hisse için ayrı görsel + ayrı tweet taslağı Enes'e gönderilir; Claude teknik analiz tweeti PAYLAŞMAZ (Enes paylaşır). Her kademe/stop/hedef seviyesinin nedeni (çakışan göstergeler ve dilimler) yazılır. (bölüm 14d, 14e)
6) TWEET AKIŞI: her turda analist notu akışları (TheFly, StreetInsider, Investing, MarketBeat, TipRanks, Benzinga, Futu) + lansman/ortaklık kaynakları taranır; boş tur geçilmez, 09:00-01:00 her tur bir tweet hedefi (günde en çok 45). (bölüm 4)
8) ZAMANLAMA: otomatik tweet 20-40 dk'da bir (rastgele); Enes'in yapıştırdığı tweet hemen atılır ama otomatik zincirin zamanlamasını etkilemez. (bölüm 2)
7) BİLANÇO TWEETİ: ilk tweet madde madde "metrik: gerçek / Beklenti" + şirkete özgü metrikler + tahmin bloğu (Enes'in $CRWV formatı); sayfa stiline uyan hisselerde 15 dk sonra kapsamlı analiz tweeti. (bölüm 4)
Yeni oturum A5'te bu iki teknik kontrol zincirini ve günlük key levels + başlıklar zincirini (kural 13) MUTLAKA kurar. Devir notu yeniden yazılırsa bu 3 kural aynen korunur.

YENİ OTURUMSAN ÖNCE A BÖLÜMÜNÜ UYGULA. Her turun başında bu dosya BAŞTAN SONA okunur. Sonra DEVIR_OZET.md (ek ayrıntı) ve DONGU.md'nin TAMAMI okunur.
Bölüm 18'de her kuralın hangi Enes mesajından geldiğini gösteren kontrol listesi var.

## A. YENİ OTURUM — İLK 15 DAKİKA (bu bölümü ilk iş uygula)
Enes bu dosyayı yeni bir sohbete attıysa, bu sohbeti yürüten oturum kapanmış ya da devredilmiş demektir. Amaç: HİÇBİR ŞEY SORMADAN aynı işi aynı kalitede sürdürmek. Adımları sırayla yap. Bir adım başarısız olursa "A6 SORUN ÇÖZÜM" tablosundaki çözümü uygula ya da Enes'e oradaki tek cümlelik talimatı yaz, sonra kalan adımlara devam et.

A1. REPO
- mcp__claude-code-remote__add_repo(owner="enesuludg6-debug", repo="kontra-gorsel", access="push").
- Ardından: `git clone --depth 1 https://github.com/enesuludg6-debug/kontra-gorsel /home/claude/kontra-gorsel`. Klasör zaten varsa `git pull`.
- mcp__claude-code-remote__register_repo_root(owner, repo, directory="/home/claude/kontra-gorsel").
- Git kimliği yoksa: `git config user.email "noreply@anthropic.com"; git config user.name "Claude"`.
- Kontrol: `ls invest/` içinde kart2.py, ta2.py, font/, logo/, DONGU.md görünmeli.
- `pip install pillow --break-system-packages` (PIL yoksa).

A2. ARAÇLARI YÜKLE (tek ToolSearch çağrısıyla)
- ToolSearch "select:mcp__buffer__list_posts,mcp__buffer__create_post,mcp__claude-code-remote__send_later,mcp__claude-code-remote__list_triggers,mcp__claude-code-remote__delete_trigger".
- Chrome için ayrı tek çağrı: ToolSearch "select:mcp__claude-in-chrome__list_connected_browsers,mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__computer,mcp__claude-in-chrome__browser_batch,mcp__claude-in-chrome__find".

A3. SİSTEM KONTROLÜ (hepsini yap, sonucu Enes'e tek mesajda bildir)
a) Buffer: list_posts(organizationId 6af5719777bce44fa736607b, channelIds ["6af99a1aece6dfde5fd109c7"], status ["sent"], first 5). Cevap gelirse ✓.
b) Kart: `cd /home/claude/kontra-gorsel/invest && python3 -c "import kart2"` hatasız olmalı.
c) Push: boş olmayan küçük bir değişikliği (DONGU.md'ye "oturum devraldı" satırı) commit + push et. Sonra raw URL testi yap:
   `curl -s -o /dev/null -w "%{http_code}" https://raw.githubusercontent.com/enesuludg6-debug/kontra-gorsel/main/invest/DONGU.md` → 200 olmalı.
d) Yahoo verisi: `python3 ta2.py RKLB > /tmp/ta.txt; head -5 /tmp/ta.txt` (pipe ile head kullanma, BrokenPipe verir) → "[1H] son ..." satırı gelmeli.
e) Zamanlayıcı: send_later aracı var mı? (A2'de yüklendiyse ✓.)
f) Chrome/TradingView: list_connected_browsers. Tarayıcı listeleniyorsa ✓. Yoksa "bilgisayar kapalı", Yahoo ile devam (sorun sayılmaz).
g) Web arama: WebSearch "stock market news today" (mode standard) sonuç vermeli.
h) Bellek: Enes'in kalıcı tercihleri bellekte (profile/preferences) zaten var; bu dosyayla çelişirse bu dosya geçerli.

A4. ESKİ ZİNCİRİ KAPAT (ÇİFT PAYLAŞIM OLMASIN)
- mcp__claude-code-remote__list_triggers ile adı "Otomatik paylaşım turu" olan BAŞKA oturuma bağlı bekleyen görevleri bul. delete_trigger ile sil (silebildiklerini).
- Silinemiyorsa Enes'e yaz: "Eski sohbette bekleyen bir tur var; eski sohbete 'durdur' yazarsan çift tweet olmaz."
- Ek güvenlik: son OTOMATİK tweet 20 dk'dan yeniyse paylaşma kuralı çift atımı zaten engeller (Enes kaynaklı tweetler sayılmaz). Yine de aynı konunun iki kez atılmaması için her turda DONGU.md + Buffer son 50 kontrol edilir.
- DİKKAT: DONGU.md'ye "DURDUR" YAZMA (yeni zinciri de durdurur). DURDUR'u sadece Enes isterse yaz.

A5. BAŞLA
- DONGU.md'nin TAMAMINI ve DEVIR_OZET.md'yi oku (bu dosya bunların hepsini içerir, ama son satırlardaki "SIRADAKİ" notları ve son 3 düzen orada).
- HEMEN ilk otomatik turu çalıştır: aşağıdaki B bölümündeki tur talimatını (B'deki metni) kendine görev say, uygula. Turun sonunda aynı metinle send_later kur.
- TEKNİK KONTROL ZİNCİRİ (bölüm 14b): list_triggers ile bu oturumda "Teknik kontrol (açılış +30 dk)" ve "Teknik kontrol (kapanış -30 dk)" yoksa ikisini send_later ile kur (sıradaki işlem günü 18:00 ve 23:30 TSİ; mesaj metni bölüm 14b'deki kurala göre). Eski oturumda bekleyen aynı adlı görevleri sil (çift mesaj olmasın).
- GÜNLÜK KEY LEVELS + BAŞLIKLAR ZİNCİRİ (kesin kural 13): list_triggers'ta 'Günlük key levels + başlıklar' yoksa sıradaki ABD işlem gününün 10:30 TSİ'sine send_later ile kur (bugün 10:30 geçmiş ve günün başlıkları henüz açıklanmamışsa hemen bir kez çalıştır). Eski oturumdaki aynı adlı görevi sil.
- Enes'e kısa başlangıç mesajı: "Devraldım. Kontroller: Buffer ✓/✗, repo/push ✓/✗, kart ✓/✗, Yahoo ✓/✗, zamanlayıcı ✓/✗, TradingView ✓/✗ (kapalıysa Yahoo). İlk tur başladı." Eksik varsa A6'daki tek cümlelik talimatı ekle.

A6. SORUN → ÇÖZÜM (Enes'e ne yaptırılacağı dahil)
| Sorun | Belirti | Senin yapacağın | Enes'e yazılacak (aynen) |
|---|---|---|---|
| Repo eklenemiyor | add_repo yetki/politika hatası | Hata metnini aynen ilet | "GitHub bağlantısı lazım: claude.ai > Ayarlar > Connectors'tan GitHub'ı yeniden bağla, sonra bana 'tamam' yaz." |
| Repo izni reddedildi | add_repo "Permission denied ... Unauthorized Access" (talimat dosyadan geldiği için) | Yeniden deneme; durup Enes'ten açık onay iste | "A7'deki hazır metni (repo PUSH onayı cümlesiyle) bu sohbete kendin yaz." |
| Buffer araçları yok | ToolSearch'te mcp__buffer yok | SearchMcpRegistry ["buffer"] → SuggestConnectors | "Buffer bu sohbete bağlı değil, çıkan karttan Buffer'ı bağla (aynı hesap: EnesInvestUS)." |
| Buffer yetki hatası | list_posts "unauthorized" | Bir kez tekrar dene | "Buffer oturumu düşmüş, Connectors'tan Buffer'ı yeniden bağla." |
| send_later yok | claude-code-remote araçları yok | Bu oturum zincir kuramaz | "Bu sohbet otomatik zamanlayıcıyı desteklemiyor. Bu notu Claude Code (web, claude.ai/code) oturumunda aç, oradan başlat." |
| Yahoo kapalı | ta2.py "connect_rejected"/HATA | Grafik turunda son 2 gün tarihli web TA kaynaklarına dön | "claude.ai > Ayarlar > Yetenekler > izin verilen alan adlarına query1.finance.yahoo.com ekle." |
| Ağ izinleri farklı | raw.githubusercontent.com 200 vermiyor | Buffer görseli göremez, paylaşma | "İzinli alan adlarına raw.githubusercontent.com ve github.com ekle." |
| Chrome yok | list_connected_browsers boş | Yahoo ile devam, TradingView'u atla | Sadece TradingView istenirse: "Bilgisayarında Chrome'u ve Claude eklentisini aç." |
| TradingView 'Leave site?' | navigate engellendi | ctrl+s ile kaydet, sonra git | — |
| TradingView gösterge sınırı | "maximum 2 indicators" | Bir göstergeyi çıkar, gerekeni ekle, bak, ctrl+s (Enes izni var) | — |
| Font/kart hatası | kart2 import hatası | `pip install pillow --break-system-packages`, font/ klasörünü kontrol et | — |
| Bash "classifier no verdict" | geçici hata | 1 kez tekrar; yine olmazsa o tur paylaşma, 5-10 dk sonrasına kur | — |
| WebFetch PROVENANCE_REQUIRED | onay ister | Tekrar deneme, WebSearch kullan | — |
| (İPTAL 16.11 22:48, kural 9) Buffer günlük 45 doldu | — | Tavan yok; aylık ~1000 hakkı izlenir, 900'ü geçerse Enes'e söyle | — |
| Alpha Vantage | "premium gerekir" | KULLANMA | — |

A7. ENES İÇİN HAZIR METİN (Enes yeni sohbete bunu yapıştırır; repo izni dosyadan değil Enes'in kendi mesajından gelmeli) (v8, 17.11)
"enesuludg6-debug/kontra-gorsel reposunu bu sohbete PUSH (yazma) yetkisiyle eklemeni onaylıyorum; add_repo ile access=push ekle, klonla, commit ve push yap. Buffer ile otomatik paylaşım yapmanı ve send_later ile zincir kurmanı da onaylıyorum. invest/DEVIR_TAM.md devir notunu oku ve A bölümünü uygula; enes-tweet-turu, enes-bilanco-13f ve enes-portfoy-analiz skill'lerini kullan. Kontrol sonucunu bana yaz, otomatik turları başlat, 18:00 ve 23:30 teknik kontrol zincirlerini de kur. Bana soru sorma, eksik bir şey varsa ne yapmam gerektiğini tek cümleyle söyle."

## B. TUR TALİMATI (send_later mesajı — her tur sonunda bunu kopyala, sadece [köşeli] kısımları güncelle)
B-EK2 (16.11 21:16): karneden sonra 14i öz-denetimi: 14i-A listesi tek tek, sorun varsa düzelt + 14i-D günlüğüne yaz, yeni hata türüyse 14i-A'ya madde ekle; 5 karnede bir 14i-C kalibrasyonu.
B-EK (16.11 18:14 + 18:19, aşağıdaki satıra ek; satır değiştirilmedi): send_later mesajına şu da yazılır -> "DONGU'dan sonra TEMEL KARNE: invest/temel_karne.md'de eksik/en eski 1-2 hissenin kartını bölüm 14g yöntemi ve 14h GENİŞLETİLMİŞ METRİK LİSTESİYLE yaz (/50), DONGU'ya KARNE satırı, push."
OTOMATİK PAYLAŞIM TURU (Enes 15.11 21:15 "oto atmaya devam"). ÖNCE invest/DEVIR_TAM.md (tam devir notu) ve invest/DEVIR_OZET.md'yi BAŞTAN SONA oku ve uygula; DONGU.md'nin TAMAMINI oku. Özet: /home/claude/kontra-gorsel/invest'te git pull. DURDUR (satır başında, tek başına) varsa hiçbir şey yapma ve send_later kurma. Buffer list_posts (organizationId 6af5719777bce44fa736607b, channelIds ["6af99a1aece6dfde5fd109c7"], first 50, status sent) ile bugün TSİ gönderilenleri say; son OTOMATİK paylaşım 20 dk'dan yeniyse paylaşma, 20-40 dk içinde kur (Enes kaynaklı paylaşımlar sayılmaz). 01:00-09:00 TSİ paylaşma (09:05 için kur; tek istisna önceden bilinen açıklama). (Günlük tavan YOK, kesin kural 9; eski: Günde en fazla 45.) ÖNCE SON DAKİKA TARA (WebSearch extended), taze ve 2 kaynakla doğrulanmış gelişme varsa onu at; yoksa daha önce atılmamış konu (DONGU'daki konular tekrar edilmez; aynı ticker 3 saat içinde yok: [son ticker saatleri]). Her rakam ve yan bilgi 2 kaynak; yıl kontrolü (2025/2026 karışıyor). Tweette kusur/şart yazarsan ne kadar olduğunu araştır, iyi mi kötü mü, rakamlar gerçek mi cevapla. Anthropic adı/konusu yok; al/sat tavsiyesi yok; emoji/hashtag/mention/link yok; soru ile bitirme yok. Kart: kart2.py, son 3 düzen ([son 3 düzen]) kullanılmasın; ticker '$' ile (logo için), halka logo çizmez; Türkçe büyük harf etiketlerini 'İ' ile hazır yaz; Read ile kontrol, yeni dosya adıyla düzelt, push, raw URL 200. Buffer create_post (channelId 6af99a1aece6dfde5fd109c7, automatic, shareNow, image + altText). SendUserMessage: metin + "Ne anlama geliyor?". Vadeli tweeti her işlem günü 09:05 ve ~15:00-15:25 TSİ (kart2.isi kolon=2 hane=2). [takvim notları]. HER TURDA PORTFÖY + GRAFİK: portföy DOCN RKLB SITM AXON CBRS VRT AVGO (16.11 23:44; eski: NBIS RKLB DOCN SITM AXON CBRS VRT) + yatırıma uygun bulduğun HERHANGİ bir hisse; `python3 ta2.py <tickerlar>` (21 gösterge, 1s/4s/günlük/haftalık) + bilgisayar açıksa TradingView (Chrome, düzen UN09ZFN8: Vol + Supertrend + LuxAlgo SMC; X'e asla girme). Enes YATIRIMCI, amacı EN DİPLERİ bulmak: dip bölgeleri, aşırı satım, pozitif uyumsuzluk, kademeli alım seviyeleri, tezin bozulduğu seviye. Notlar "BEN OLSAM" diliyle, sadece Enes'e mesajla, değişiklik/fırsat olunca. Portföy güncellemesi tweeti ATMA (Enes atar). Teknik analiz tweeti ATMA (Enes paylaşır, bölüm 14d). 18:00 ve 23:30 TSİ teknik kontroller ayrı zincirdir (bölüm 14b-14d), bu turda yoksa kur. DONGU.md'ye "AUTO" + tür + konu işle, push et. Ardından TEMEL KARNE: invest/temel_karne.md'de eksik ya da en eski 1-2 hissenin kartını yaz/yenile (bölüm 14g), DONGU'ya "KARNE", push. Son olarak bu mesajın aynısıyla (son 3 düzen ve ticker saatlerini güncelle) 20-40 dk rastgele gecikmeyle (random.randint(20,40)) yeni send_later kur.

## C. DEVRİN SINIRLARI (yeni oturum bunları bilsin, Enes'e de söylesin)
- Bu sohbetin konuşma geçmişi yeni oturuma geçmez; geçen her şey bu dosyada, DEVIR_OZET.md, ORNEKLER.md, DONGU.md ve Enes'in kalıcı belleğinde.
- send_later görevleri oturuma bağlıdır: eski oturumun kurduğu tur, eski oturumda çalışır (A4).
- TradingView yalnız Enes'in bilgisayarı ve Chrome açıkken çalışır; değilse Yahoo hesapları kullanılır (sonuç aynı göstergeler, sadece SMC/Supertrend yaklaşık).
- Enes'in Claude planı en düşük ücretli plan: uzun oturumlar kullanım limitine takılabilir. Limit dolarsa zincir durur; Enes'e "limit doldu, şu saatte yeniden başlat" diye söylenir ve DONGU'ya not düşülür. Kullanımı azaltmak için gereksiz tekrar araması yapma, grafik taramasında ta2.py çıktısını özetle.

---------------------------------------------------------------------------------------------------

## 0. KİM, NE, NEDEN
- Kişi: Enes Uludağ. X hesabı @enes1050392, görünen ad "Enes Uludağ", hesap adı EnesInvestUS. Türkçe, ABD borsası odaklı.
- Enes bir YATIRIMCI (16.11 12:48). Portföy yönetiminde amacı yükselişin başını yakalamak değil, EN DİPLERİ bulmak (16.11 13:32).
- HESABIN AMACI (15.11 18:10, her şeyin üstünde): en iyi getiriyi yakalamak ya da borsayı en iyi bilen görünmek DEĞİL. Amaç GÜVEN sağlamak ve İYİ İÇERİK üretmek.
  - Doğru olmayan rakam yerine eksik tweet. Her kartta kaynak.
  - Yalnız doğru çıkan tahminlerden bahsedilir; tutmayan paylaşılmaz (kural 23, 17.11). Yanlış rakam için kural 21 düzeltme geçerli.
  - Abartı, heyecan, "kaçırmayın" yok. Sade, dürüst, anlaşılır.
  - Okuru eğit: neden önemli, kime etkisi var.
- Hedef okur (15.11 16:25, EN ÖNEMLİ YAZIM KURALI): ABD borsasını az bilen biri. Olabildiğince KISA ve BASİT.
- Enes'i geliştirmek de amaç: her tweetle birlikte "Ne anlama geliyor?" öğretici bölümü gönderilir (bölüm 9).

## 1. PORTFÖY VE LİSTELER
- GÜNCEL PORTFÖY (16.11 23:44, Enes'in uygulama ekran görüntüsü): DOCN RKLB SITM AXON CBRS VRT AVGO. NBIS çıktı, AVGO girdi (23:30 kontrolündeki NBIS -> AVGO kıyası sonrası). 16.11 23:48 Enes: "NBIS YOK" -> NBIS portföyde değil; teknik kontrollerde ve portföy notlarında NBIS'e bakılmaz, aday/izleme listesine de konmaz (Enes yeniden isterse eklenir). (eski 16.11 12:49: NBIS RKLB DOCN SITM AXON CBRS VRT)
  - SPCX çıktı, SITM girdi.
  - Enes piyasa açılışında hepsini EŞİT AĞIRLIKLA alacağını söyledi. Benim "ben olsam" görüşüm kademeli girmekti; karar onun.
  - (eski 15.11 16:55: AXON NBIS RKLB CBRS DOCN VRT SPCX)
- İLGİ LİSTESİ: ON AAOI HOOD TEM CRDO PLTR ISRG ASTS MU + büyük yapay zeka/yarı iletken/bulut/uzay şirketleri (NVDA AMD AVGO TSM MSFT GOOGL AMZN META ORCL CRWV SNOW vb.).
- FIRSAT HİSSESİ SINIRSIZ (16.11 13:25): fırsat önerisi ilgi listesiyle sınırlı değil. ABD borsasında yatırıma uygun bulduğum HERHANGİ bir hisse önerilebilir; gerekçesi (temel + teknik), seviyesi ve riskiyle.
- Portföyde ağırlık/tutar/para ASLA tweete yazılmaz. Enes'in ağzından "aldım / sattım / ekledim / portföyüm / YTD %" cümlesi kurulmaz.
- PORTFÖY GÜNCELLEMESİ TWEETİ (16.11 23:44 EK): Enes açıkça isterse atılır. Format (Enes 23:44): ilk satır 'PORTFÖY GÜNCELLEMESİ', altında Enes'in verdiği 'YTD %X' ve 'Günlük değişim %Y' satırları aynen, boş satır, sonra ABD hisseleri alt alta $TICKER. Tutar, para, ağırlık ASLA yazılmaz; rakamlar Enes'in verdiği gibi değiştirilmeden. Enes istemedikçe otomatik atılmaz (aşağıdaki kural geçerli).
- PORTFÖY GÜNCELLEMESİ TWEETİ YOK (16.11 13:54): Portföy güncellemesi tweetini Enes kendisi atar. Claude portföy güncellemesi tweeti/kartı hazırlamaz, atmaz, sormaz. (eski: ana sohbetten Enes onayıyla atılırdı)
- Eski 'EnesInvestUS günlük portföy sorusu' görevi (trig_019TTCnsx74Nsi9DjkY7M5MF) 16.11 13:54'te DURDURULDU. Kapanış tweeti normal turların içerik menüsünden (00:05-00:45) atılır.

## 2. PAYLAŞIM MODU (güncel: TAM OTOMATİK)
- Buffer create_post:
  - organizationId 6af5719777bce44fa736607b, channelId 6af99a1aece6dfde5fd109c7 (X)
  - schedulingType automatic, mode shareNow
  - text + assets [{image:{url, metadata:{altText}}}]
  - altText'te yazım hatası yapma.
- Zincir:
  - Her tur sonunda mcp__claude-code-remote__send_later ile yeni tur kurulur.
  - Gecikme 20-40 dk arası RASTGELE (python random.randint(20,40)) (16.11 16:46, Enes: "artık 20-40 dk'da bir atacaksın"; eski: 16:36'da 12-27, önce 5-20). "Tam 10 dk olmasın" (15.11 20:43).
  - ENES'İN ATTIĞI TWEETLER ZAMANLAMAYI ETKİLEMEZ (16.11 16:46): Enes bir tweet/haber yapıştırırsa HEMEN araştırılıp atılır, ama otomatik zincirin zamanlaması değişmez: bekleyen tur iptal edilmez/ertelenmez, yeni tur kurulmaz; Enes kaynaklı paylaşımlar "son paylaşım ne zaman" hesabına KATILMAZ.
  - Otomatik turlarda: son OTOMATİK paylaşımdan bu yana 20 dk geçmediyse (ör. tur erken tetiklendiyse) paylaşma, kalan süreye göre 20-40 dk içinde kur. Bilanço 15 dk analiz turu ayrı tek seferlik turdur, zinciri değiştirmez.
  - Mesaj = sabit tur talimatı; son 3 düzen ve ticker saatleri her seferinde güncellenir.
  - Turlar DURMAYACAK (16.11 11:12 "turlar durmasın otomatik devam et").
- Son OTOMATİK paylaşım 20 dk'dan yeniyse o tur paylaşma, 20-40 dk içinde kur (eski: 5 dk / 5-20).
- GECE: 01:00-09:00 TSİ paylaşım yok, 09:05 için tur kurulur.
  - Tek istisna (16.11 01:53): önceden BİLİNEN bir açıklama varsa (takvimdeki bilanço rakamı, veri, konuşma) o saat için ayrıca tur kurulur.
  - Beklenmedik haber 09:05'e kalır.
- GÜNLÜK TAVAN KALDIRILDI (16.11 22:48, kesin kural 9). (eski: GÜNLÜK TAVAN 45 tweet (15.11 21:46; eski 40).) Enes'in elle attıkları dahil, Buffer list_posts ile sayılır (00:00 TSİ = önceki gün 21:00Z).
- DURDUR: Enes "durdur" derse DONGU.md'ye satır başında tek başına "DURDUR" yaz ve zinciri kurma. Her tur başında DURDUR kontrol edilir.
- Mod geçmişi (bilgi için):
  - 15.11 16:10 sohbet modu (Buffer yok)
  - 17:30 istek modu
  - 18:30 10 dk modu
  - 19:30 OTOMATİK (shareNow)
  - 20:40 "10 dakikada 1, otomatik at, benden sadece foto iste"
  - 15.11 21:15 "oto atmaya devam"
  - Taslak (saveToDraft) modu İPTAL; şu an shareNow geçerli.
- X Original Content Rewards otomatik içeriği ödeme dışı tutabilir. Enes'e söylendi, Enes yine otomatik istedi.

## 3. TUR AKIŞI (her turda sırayla)
1. ReadNotifications (bildirim varsa). Ardından `cd /home/claude/kontra-gorsel/invest && git pull`.
2. Oku: DEVIR_TAM.md (bu dosya), DEVIR_OZET.md, DONGU.md TAMAMI (özellikle son satırlardaki "SIRADAKİ" notları).
3. DURDUR kontrolü.
4. Buffer list_posts: bugün kaç tweet atıldı, son tweet ne zaman, hangi konu/ticker.
5. ÖNCE SON DAKİKA TARAMASI (bölüm 4). Taze ve 2 kaynakla doğrulanmış gelişme varsa onu at. Yoksa içerik menüsünden daha önce ATILMAMIŞ bir konu seç.
6. Rakamları 2 kaynakla doğrula (bölüm 5).
7. Kart yap → Read ile kontrol et → push → raw URL 200 → Buffer (bölüm 7).
8. Enes'e SendUserMessage: paylaşılan metin + "Ne anlama geliyor?" (bölüm 9).
9. PORTFÖY + GRAFİK TARAMASI (bölüm 11-14): her turda grafiklere bakılır. Değişiklik ya da fırsat varsa Enes'e "ben olsam" notu atılır.
10. DONGU.md'ye `- HH:MM AUTO (TÜR): dosya.jpg - özet (kaynaklar) | düzen:...` yaz. Commit ve push.
10b. TEMEL KARNE (16.11 18:14, bölüm 14g): invest/temel_karne.md'de eksik ya da en eski 1-2 hissenin kartını yaz/yenile, DONGU'ya "KARNE: <hisse> <toplam>", commit + push.
11. Yeni send_later kur (20-40 dk rastgele).
- Bash "classifier no verdict" verirse bir kez tekrar dene. Olmazsa o tur paylaşma, 5-10 dk sonrasına aynı mesajla kur.
- WebFetch PROVENANCE_REQUIRED derse tekrar deneme, WebSearch ile devam et.
- Buffer hata verirse 1 kez tekrar dene; olmazsa DONGU'ya yaz, atla.
- Push reddedilirse görselsiz tweet atma.

## 4. İÇERİK ÖNCELİĞİ VE KONU SEÇİMİ
- ÖNCELİK SIRASI (16.11 11:21, EN ÖNEMLİ):
  - Her turda ÖNCE son dakika ve en yeni gelişmeyi tara (son 1-3 saat, WebSearch extended).
  - Taranacaklar: Reuters, AP, Bloomberg, CNBC; Asya/Avrupa/ABD; vadeliler; şirket IR, 8-K, 6-K, Form 4; Fed ve veriler; analist notları; portföy + ilgi listesi; son 1 haftada açıklanmış ama paylaşılmamış bilançolar.
  - Taze yoksa terim/analiz/eski içerik. Eski konulara yaslanma alışkanlığı bırakılacak.
- HABER HIZI KAYNAKLARI (16.11 01:49):
  - Sıra: (1) SEC EDGAR, IR ve bülten siteleri (PR Newswire, Business Wire, GlobeNewswire, Accesswire); (2) Reuters, CNBC, Bloomberg, Benzinga son dakika; (3) ekonomik ve bilanço takvimi; (4) menü.
  - Diğer kaynaklar:
    - Resmi veri: Fed, BLS, BEA, Treasury, Census.
    - Takvimler: Investing.com, TradingEconomics, Forex Factory, MarketWatch, Econoday, Earnings Whispers, Nasdaq, Yahoo, Zacks, StockAnalysis.
    - İçeriden/kurum: OpenInsider, Quiver, Capitol Trades, WhaleWisdom, Dataroma, Unusual Whales.
    - Hareket: Finviz, Chartmill, Stocktwits.
    - Derin: Semianalysis, The Information, Nikkei, DigiTimes, TrendForce, Axios, Techmeme, SpaceNews.
  - Sosyal sinyal (Walter Bloomberg, DeItaone, FirstSquawk vb.) 2 güvenilir kaynakla doğrulanmadan KULLANILMAZ.
  - X hesaplarına Claude girmez.
- ENES'İN ATTIĞI TWEETLERDEN DERS (16.11 15:42, Enes: "attığım tweetlerden öğren hangi sitelere bakman gerektiğini ve ne kadar tweet atman gerektiğini"):
  - Enes'in örnekleri (12:22 Kuo/TPU, 15:39 Uber/Zoox, 15:42 Citi/NBIS) üç tür: (a) ANALİST NOTU: "X price target lowered/raised to $A from $B at Kurum" (TheFly/StreetInsider formatı), (b) ŞİRKET/ORTAKLIK LANSMANI (bugün başlayan ürün, şehir, anlaşma), (c) ANALİST TAHMİNİ (Kuo gibi tanınmış isim + rakam).
  - HER TURDA BAKILACAK KAYNAKLAR (son dakika taramasına ek): analist not akışları: TheFly (thefly.com/news), StreetInsider ratings, Investing.com "analyst ratings", MarketBeat ratings, TipRanks news, Benzinga analyst ratings, Futu/Moomoo haber başlıkları, aktiencheck/finanzen (Almanca ama hızlı). Lansman/ortaklık: Business Wire, PR Newswire, GlobeNewswire, şirket IR, TechCrunch, The Verge, Electrek. Gerekirse Chrome'da açılır (bölüm 10). Portföy + ilgi listesi + büyük yapay zeka/yarı iletken/bulut/uzay/robotaksi şirketleri öncelikli.
  - ANALİST NOTU TWEETİ KALIBI: kurum + analist (biliniyorsa) + eski → yeni hedef + tavsiye + neden (notun gerekçesi) + bağlam (son 2-4 haftadaki önceki değişiklik, bilanço) + mevcut fiyata göre fark (Yahoo fiyatıyla hesapla) + tek cümle görüş. Hedef ve tavsiye 2 kaynakla (ör. Futu + aktiencheck/TipRanks); notun içeriği (gerekçe) tek kaynaktaysa sadece doğrulanmış kısmı yaz.
  - NE KADAR TWEET: Enes daha sık ve sürekli akış istiyor. 09:00-01:00 arasında her otomatik tur (20-40 dk) bir tweet hedeflenir, günlük tavan 45. "Taze haber yok" diye BOŞ TUR GEÇİLMEZ: son dakika yoksa sırasıyla (1) son 24 saatin analist notları, (2) bugünkü lansman/ortaklık/anlaşmalar, (3) bu hafta takvimi, (4) menü. Boş tur yalnızca hiçbir şey 2 kaynakla doğrulanamazsa olur ve DONGU'ya nedeni yazılır.
  - Enes tweet yapıştırınca: 3 saat ticker kuralı ve tur sırası beklenmez, hemen araştırılıp atılır; örnek ORNEKLER.md'ye eklenir.
- VADELİ İŞLEMLER HER İŞLEM GÜNÜ (16.11 02:05):
  - 09:05 turunda ve ABD açılışından önce (~15:00-15:25 TSİ) tekrar. Dow, S&P 500, Nasdaq 100, Russell 2000 vadelilerinin önceki kapanışa göre %'si.
  - %1+ sürprizde ek tweet.
  - Düzen: kart2.isi(kolon=2, hane=2, etiket="VADELİ İŞLEMLER"). Yüzde 2 basamak.
  - "Vadeli = açılışı gösteren işaret, garanti değil."
- TEKRAR YOK:
  - DONGU.md tamamı + Buffer son 50'de olan konu tekrar atılmaz. Yeni gelişme varsa yeni açıyla atılabilir (DONGU'ya "devam: önceki dosya").
  - Aynı ticker 3 saatte bir. Aynı haber 24 saatte tekrar yok.
- ÖNCELİKLİ TÜRLER:
  - Son dakika.
  - Bu hafta ne var / yarın ne var.
  - Bilanço rakamları (YORUMSUZ, ilk tweet).
  - Bilanço analizi (YORUMLU, 30-90 dk sonra ayrı tur).
  - İçeriden alım-satım: günde 1-2. SEC Form 4; piyasadan alım (kod P) daha anlamlı; 1 Mn$ üstü; küme alımı; 10b5-1 planlı satış ya da vergi için bırakma (kod F) açıkça yazılır.
- İÇERİK MENÜSÜ (DEVIR.md bölüm 3 tam liste):
  - Zamana bağlı: sabah notu 09:30-11:00, premarket 16:15-17:15, açılış 17:30-18:30, kapanış 00:05-00:45, Cuma/Cumartesi haftanın karnesi, Pazar/Pazartesi bu hafta ne var, hafta içi 22:00 yarın ne var. Makro veri günü: beklenti → sonuç (yorumsuz) → etki (yorumlu).
  - Şirket: bilanço öncesi/rakam/analiz, opsiyonların beklediği hareket, analist notu (kurum + eski/yeni hedef), içeriden işlem, geri alım/temettü, anlaşma/satın alma, endeks girişi, halka arz, kilometre taşı, CEO/Fed sözü (foto Enes'ten).
  - Fon: 13F, haftalık fon akışları, açığa satış oranı.
  - Karşılaştırma ve veri: 1 yıl önce vs bugün, iki rakip, sektör sıralaması, uzun dönem tek metrik, yapay zeka capex, emtia/dolar/tahvil/kripto, haftanın rakamı.
  - Eğitici (haftada 3-5): terim sözlüğü, "bu şirket ne iş yapar", strateji/psikoloji, teknik analiz.
- BİLANÇO TWEETİ FORMATI (16.11 16:33, Enes, KESİN KURAL): bilanço açıklanınca İLK tweet aşağıdaki sayfa düzeninde, madde madde, yorumsuz yazılır (Enes'in $CRWV örneği):
    $TICKER 3. ÇEYREK BİLANÇOSU
    • Gelir: 3,66 Mr $ / Beklenti: 3,54 Mr $
    • Hisse başı kâr: -1,24 $ / Beklenti: -1,55 $
    • Düzeltilmiş faaliyet kârı: 379 Mn $ / Beklenti: 246 Mn $
    • (şirkete özgü ana metrikler: ör. sözleşmeli güç ~3,7 GW, aktif güç ~1,7 GW, sipariş birikimi 133 Mr $ (+%30 çeyreklik))
    (boş satır)
    2026 TAHMİNİ
    • Gelir: 13,2 Mr $ / Beklenti: 12,5 Mr $
    • Yatırım harcaması: 38 Mr $ / Beklenti: 36 Mr $
    • Yıl sonu yıllık gelir hızı: 21 Mr $
  - Kurallar: başlık satırı ticker + çeyrek; her satır "metrik: gerçek / Beklenti: X"; şirkete özgü 2-3 metrik (bulut için güç/backlog, yazılım için ARR/NRR, çip için brüt marj/veri merkezi geliri, perakende için aynı mağaza satışı); ardından tahmin (guidance) bloğu. Terimler Türkçe ve sade (EPS -> hisse başı kâr, guidance -> tahmin, capex -> yatırım harcaması, backlog -> sipariş birikimi, ARR -> yıllık gelir hızı). Madde işareti "•" kullanılır (emoji değil). Her rakam 2 kaynak (birincil kaynak: şirket bülteni + 1 haber). Görsel: skor/terminal düzeni.
  - KAPSAMLI ANALİZ 15 DK SONRA: hisse sayfanın stiline uyuyorsa (portföy, ilgi listesi, yapay zeka/yarı iletken/bulut/uzay/büyük teknoloji ve benzerleri) bilanço açıklandıktan 15 dakika sonra kapsamlı analiz tweeti atılır (ilk tweetin hemen ardından send_later ile 15 dk sonrasına tur kurulur). İçerik: ne iyi ne kötü, tahminin anlamı, kusur/şart varsa ne kadar (bölüm 6), hisse tepkisi, tek cümle görüş. Sayfa stiline uymayan şirketlerde (ör. gıda) analiz 30-90 dk içinde ve kısa olabilir. (eski: analiz 30-90 dk sonra ayrı tur)
- Bilanço öncesi ve sonrası, kısa + uzun (DEVIR 5g):
  - Portföy ve ilgi listesi şirketlerinde öncesi ve sonrası KESİN atılır.
  - Uzun format 5-7 tweetlik flood. Zamanlama: öncesi 1 gün önce akşam ya da sabah; sonrası ilk tur.
- Sabit seriler (DEVIR 5f): sabah notu, kapanış, haftanın karnesi, gelecek hafta takvimi.
- Uzun seri ve çoklu hisse grafikleri (DEVIR 5k):
  - Fiscal.ai tarzı 5-10 yıllık tek metrik.
  - Forward F/K sıralaması, NTM büyüme sıralaması.
  - Hepsi aynı kaynak ve tarih. Başkasının grafiği kopyalanmaz.
- Gündem dosyası (DEVIR 5c): invest/gundem.md'de Enes'in elle eklediği konular öncelikli. Doğrula, kullanınca DONGU'ya "(gündem)" yaz.
- ANTHROPIC (çıkar çatışması):
  - Konu otomatik atılmaz (halka arz dahil).
  - Adı tweete YAZILMAZ; gerekirse "bir başka büyük yapay zeka şirketi" denir.
  - Enes'e soruldu: bu yasak gevşetilsin mi? Cevap bekleniyor.

## 5. DOĞRULAMA KURALLARI
- Her rakam en az 2 bağımsız kaynakla doğrulanır.
  - Kaynaklar çelişirse rakam kullanılmaz (ya da şirketin kendi rakamı kullanılıp not düşülür).
  - Tek kaynaktaki iddia KULLANILMAZ.
- YIL KONTROLÜ: arama sonuçları 2025 ile 2026'yı karıştırıyor; tarih mutlaka kontrol edilir.
- "Şu an / bugün" iddiaları güncel fiyatla doğrulanır.
- Tweetteki YAN BİLGİLER de 2 kaynakla doğrulanır ("borsa sert düştü", çeyreklik/yıllık ayrımı, "Huawei gibi" vb.). Doğrulanmayan yan cümle yazılmaz.
- Fiyat ve yüzde uydurulmaz, tahmin edilmez.
- Doğrulanamayanı Enes'e dürüstçe söyle. Enes'in tercihi: birincil kaynak, doğrulanamıyorsa belirt.
- Yanlış atılmış bir şey çıkarsa Enes'e açıkça söyle. Örnekler: INTC tweetindeki doğrulanmamış "şu an zararda" iddiası; Japonya GDP tweetindeki zayıf doğrulanmış yan cümleler.

## 6. YAZIM STİLİ
- Arkadaşına anlatır gibi, konuşma dili. Kısa cümle. 2-4 cümle. En fazla 2-3 rakam. Bir tweette tek fikir.
- Basit ve doğal cümleler (Enes tercihi). Yapay zeka gibi duran ifadeler yok.
- Şirketi ilk geçtiği yerde ne iş yaptığıyla tanıt: "$NBIS (yapay zeka şirketlerine GPU bulut gücü kiralayan Nebius)".
- Terimleri sadeleştir: EPS → hisse başı kâr; guidance → şirketin önümüzdeki dönem için verdiği tahmin; capex → yatırım harcaması; YoY → geçen yıla göre; tutanak → toplantı notları.
- Saatler gündelik dille: "akşam 8'de", "gece yarısı".
- Ticker'lar $TICKER biçiminde.
- İlk satır durdurmalı: rakam, tezat ya da net görüş.
- Her tweette 1 cümle net görüş. Bilanço rakam tweeti hariç.
  - "Bence" tekrarı yok (15.11 16:58).
  - Kapanışlar çeşitli olsun: "gösteriyor bana / düşünüyorum / sanmıyorum" tekrar etmez. Son 5 tweetin kapanışına bak.
  - Seçenekler: düz tespit, kısa yargı, sonuca bağlama, karşıtlık, takip, farklı fiilli kişisel cümle, yorumu başa koyma.
- ENES'İN EN SEVDİĞİ TARZ — GÖRÜŞLÜ BAĞLAM TWEETİ (16.11 22:44, Enes: "olaya çok hakim yazmış, çok iyi bağ kurmuş, bu tarz tweetleri çok sevdiğimi not al"): haberi tekrar etmek yerine arkasındaki yapıyı anlatan, farklı olayları birbirine bağlayan, karşılaştırmayla (ör. "Nvidia, Apple ya da McDonald's değil") net görüş savunan, kısa ve kendinden emin tweet. Kalıp: tez cümlesi -> 2-3 doğrulanmış olgu -> iki taraf/çatışma -> karşılaştırma/tarih -> net görüş. Büyük olaylarda düz haber yerine bu tarz tercih edilir, günde en az 1-2 hedef. Örnek ve kalıp: ORNEKLER.md 18. Olgular yine 2 kaynak, al/sat yok.
- ENES'İN BEĞENDİĞİ TARZ (16.11 12:22): kısa, haber odaklı, analist/kaynak adı + rakam + net sonuç. Tahmin "tahmin" diye belirtilir.
  - Örnek: Ming-Chi Kuo'nun "GOOGL 2029'da 16-18 milyon TPU" tahmini.
  - Enes bir tweet yapıştırırsa: tarzını öğren + konuyu hemen araştır (2 kaynak) + tur beklemeden hemen tweet at.
- OKUYUCUNUN AKLINDAKİ SORUYU CEVAPLA (16.11 13:07):
  - Tweette bir kusur/şart yazarsan ("organik değil", "tek seferlik", "satın almadan", "bilanço dışı") havada bırakma.
  - Ne kadar olduğunu 2 kaynakla bul. Okuyucunun soracağı soruları önceden cevapla: Bu iyi mi kötü mü? Rakamlar şişirilmiş mi, yanlış mı, çakma mı? Düzeltince ne kalıyor?
  - Rakam bulunamazsa ya da tek kaynaktaysa o cümleyi yazma ya da "ne kadarı belli değil" de. Tahmin yürütürsen "tahminen" de ve dayanağını yaz.
  - Örnek: SITM'de satın alma hariç gelir +%154 (212,4 Mn$), satın alınan birimin katkısı 86,3 Mn$ (~%29). Doğrusu "satın alınan birim hariç bile +%154" demekti.
  - Örnek: NBIS'te "düşüşün sebebi talep değil zamanlama" (13:20 tweetinde uygulandı).
- YASAK KALIPLAR (kesin kural 11): "Benim okumam:", "Benim görüşüm:", "Görüşüm:", "Yorumum:", "Not:", "Asıl ilginci", "Bence önemli nokta şu:", "Sonuç olarak", "Özetle", "Kısaca", "Risk tarafı da var", "Bir de şu var:", "X neden önemli?", "Kısa bir flood açayım", "Bu bence çok şey anlatıyor", "mesaj net", "dikkat çekiyor", "öne çıkıyor", "önemli bir gelişme", "kritik / kritik nokta", "vb.", "nabız tutmak", "sınavda", "mercek altında", "gözler ... üzerinde", "ayrıca", "bununla birlikte". Haber ajansı dili ve slogan kapanış yok.
- YASAKLAR (kesin):
  - Al/sat/hedef fiyatım/kesin yükselir tavsiyesi (analist hedefi kaynağıyla aktarılabilir).
  - @mention, link, hashtag kalabalığı (gerekmedikçe hiç).
  - Yanıt/beğeni/takip/DM otomasyonu.
  - Emoji.
  - Soruyla bitirmek (soru çok nadir).
  - Doğrulanmamış rakam.
  - Kişisel/özel hayat detayı (Huang olayında yalnız şirket/piyasa yönü).
  - Başkasının tweetini kopyalamak/çevirmek.
  - Gerçek kişi fotoğrafını internetten indirmek.
- TEKNİK ANALİZ TWEETİ DİLİ (16.11 14:07, Enes, KESİN KURAL): teknik analiz tweetlerinde Enes'in kendi bakışı ve planı anlatılır, ama tavsiye verilmez ve "oyun planı" diye başlık atılmaz. Arkadaşa anlatır gibi, konuşma dili, sade.
  - Örnek dil: "Bence bu hisse dibe yakın." / "Bence daha dip arıyor." / "Ben 80-82 arasından bir kademe eklerim, orayı da aşağı kırarsa 70-72'den bir kademe daha eklerim." / "69'un altında kapanırsa benim için hikaye değişir."
  - Seviyeler bölüm 13 tam testinden gelir (21 gösterge x 4 dilim). Teknik terimleri sadeleştir: FVG -> "boşluk", order block -> "alıcıların daha önce toplandığı bölge", OTE -> "geri çekilmenin ideal bölgesi", Supertrend -> "trend göstergesi".
  - YASAK kalır: "alın / satın / siz de ekleyin / kaçırmayın / hedef fiyatım kesin", miktar/ağırlık/para, "portföyümün %X'i". Okura yönelik emir kipi yok; sadece "ben" dili.
  - (eski: "Enes'in ağzından aldım/ekledim cümlesi kurulmaz" -> teknik analiz tweetlerinde "ben şuradan kademe eklerim" planı ARTIK SERBEST; gerçekleşmiş alım ("aldım") ve portföy güncellemesi yine yazılmaz, onu Enes atar.)
  - Teknik analiz tweeti görseli: göstergeli grafik (g/ta/ matplotlib koyu tema veya TradingView ekran görüntüsü), seviyeler işaretli.
- Şablonlar: invest/ORNEKLER.md (13 şablon). O zaman/şimdi, iki çarpıcı istatistik, bilanço skor kartı, haber + sektör etkisi, teknik analiz, uzun dönem sütun, çoklu hisse sıralama, uzun tez, eğitici strateji, yanıt kalıbı, araştırma raporu, çeyrek sonu vs bugün, kurum araştırma grafiği. Enes'in attığı her yeni tweet buraya şablon olarak eklenir.

## 7. GÖRSELLER (KART)
- Kod: invest/kart2.py (ana), kart.py (yedek). Fontlar invest/font: Inter Display, Instrument Serif, JetBrains Mono. Enes koyu tema + minimal sever.
- Düzenler (önce bunlar): bento, halka, isi, takvim, cizgi, panel, uclu, soz, editoryal, skor, zaman, ilerleme, dilim, dortlu, manset. Yedek: spotlight, split, terminal, sondakika, once_sonra, kapak, cam, poster, siralama, grafik2.
- KALDIRILDI: versus (15.11 21:23 "kaba"). Yerine panel.
- Son 3 turda kullanılan düzen tekrar edilmez. Şu an son 3: skor (15:55), uclu (16:12), cizgi (16:33). (eski 13:40: editoryal, uclu, bento) Bunu tur mesajında güncelle.
- Tür → düzen:
  - Bilanço rakam: skor/terminal. Analiz: bento/uclu/panel.
  - İki hisse: panel. Takvim: takvim. Kapanış: isi/dortlu.
  - Son dakika: sondakika/manset. İçeriden işlem: uclu/skor. Kişi: manset/soz (Enes fotosuyla). Vadeli: isi.
- LOGO ÇOK BELİRGİN (16.11 10:30-10:38): kart2.LOGO_BUYUT = 1.8. Küçültme yok, gerekirse daha da büyüt.
  - Koyu logolar beyaz plakada.
  - Logo yoksa logo/XXX.png ticker yazı logosu oluştur (örnek: 16.11'de logo/BIDU.png).
  - Ticker MUTLAKA "$" ile verilir ("$GOOGL"), yoksa logo çizilmez.
  - halka düzeni logo ÇİZMEZ, logo gereken konuda kullanma.
  - cizgi'de büyük rakam logoyla çakışabilir; başlık ve rakam kısa tutulur.
- YAZI TİPİ: ince/keskin yazı kuralı İPTAL (16.11 11:53). Normal ağırlıklar. (eski 10:34: ince istenmişti)
- Font tuzakları:
  - "OpenAI" kart fontunda "OpenAl" gibi görünür; kartta kullanma.
  - "AI" → "Al" gibi görünür; "Yapay zeka" yaz.
  - Türkçe büyük harf: Python .upper() "i" harfini "I" yapar ("GELIRI"). Etiketleri "İ" ile hazır büyük yaz ("GELİRİ").
  - Kicker'da şirket adı bozulabilir ("SİTİME"); ticker kullan ("SITM • 3. ÇEYREK").
- "Kaynak:" önekini verme (kart kendisi ekliyor). Kaynak ve alt başlığı kısa tut. Açıklamalar 3 satıra sığsın.
- HER KART Read ile kontrol edilir. Hata varsa YENİ dosya adıyla yeniden çiz (raw URL önbelleği) ve kötüsünü sil.
- Akış: invest/g/YYYYMMDD_HHMM_konu.jpg → git add/commit (attribution satırlarıyla) → push → curl ile raw URL 200 kontrolü → Buffer.
  - URL: https://raw.githubusercontent.com/enesuludg6-debug/kontra-gorsel/main/invest/g/<dosya>
- Haber ve kişi fotoğrafı internetten indirilmez. Kişi haberinde foto gerekiyorsa Enes'e sadece "X'in fotosunu at" yazılır. Beklenmez, o tur başka konu atılır; Enes'in fotoları invest/foto/.
- Signature'lar:
  - uclu(ticker, etiket, baslik, [(rakam, açıklama)]x3, kaynak, out)
  - cizgi(ticker, etiket, baslik, etiketler, degerler, buyuk, buyuk_lbl, kaynak, out, renk=None)
  - sondakika(ticker, baslik, alt, kaynak, out, bant=)
  - dortlu(etiket, baslik, [(ticker, değer, not)]x4, kaynak, out)
  - editoryal(ticker, kicker, baslik, spot, rakamlar3, kaynak, out, tarih="")
  - skor(ticker, etiket, baslik, [(metrik, beklenti, gerçek, ok)], sonuc, kaynak, out)
  - zaman(ticker, etiket, baslik, [(tarih, başlık, açıklama)], kaynak, out)
  - isi(baslik, alt, kutular, kaynak, out, etiket, kolon, hane)
  - panel(sol, sag, kicker, baslik, satirlar, cubuk, kaynak, out, notu="")
  - bento(ticker, etiket, baslik, buyuk, buyuk_lbl(str), [(ETİKET, değer, alt)]x3, seri, seri_lbl, kaynak, out)
  - halka(ticker, yuzde, baslik, orta_alt, [(etiket, değer)]x3, kaynak, out, etiket, renk)

## 8. ENES BİR ŞEY ATARSA
- Başkasının tweeti/grafiği: araştır, her rakamı doğrula, KENDİ cümlenle benzerini yaz, kendi kartını çiz. Tutmayan rakamı Enes'e söyle. Hemen at (tur bekleme).
- "Yorum yaz" derse yanıt metni hazırla (Enes kendisi atar; otomatik yanıt yok). İstenirse İngilizcesi de.
- Grafik ekran görüntüsü atarsa teknik analiz tweeti hazırla (DEVIR 5h 2. yol). Okunamayan değer uydurulmaz.
- Gönderdiği her tweet ORNEKLER.md'ye şablon olarak eklenir.

## 9. "NE ANLAMA GELİYOR?" (ÖĞRETME, 15.11 19:15)
- Her paylaşımdan sonra Enes'e SendUserMessage atılır. İçinde paylaşılan metin + "Ne anlama geliyor?" bölümü olur. 3-6 kısa madde:
  1. Bu bilgi/terim nedir, sade anlatım.
  2. Piyasada neden önemli, genelde neye yol açar.
  3. Nasıl yorumlanır, iyi/kötü sinyal ne olur.
  4. Varsa tarihten kısa bir örnek.
- Doğrulanamayıp tweete girmeyen rakamları da kısaca söyle. Bu bölüm tweete girmez.

## 10. TARAYICI / BİLGİSAYAR ERİŞİMİ
- Enes'in X hesabına HİÇBİR ŞEKİLDE girilmez. Tarayıcı otomasyonu ve scraping X kurallarına aykırı.
- Tarayıcı ve bilgisayar: tradingview.com + HABER ARAŞTIRMASI (16.11 15:29, Enes: "istersen Chrome'dan araştır haberleri"). (eski: SADECE tradingview.com)
  - Haber için Chrome kullanım sırası: önce WebSearch; sonuç gelmezse, sayfa JS ile yükleniyorsa (ör. ir.tyson.com haber listesi) veya WebFetch PROVENANCE_REQUIRED/izin isterse Chrome'da YENİ sekme aç (tabs_create_mcp), navigate + get_page_text ile oku, iş bitince sekmeyi kapat (tabs_close_mcp). TradingView sekmesine dokunma.
  - Sadece okuma: form doldurma, giriş, abonelik, yorum, paylaşım YOK. Çerez bannerlarında en gizli seçenek. X.com'a ASLA girilmez.
  - HER HABERDE EN İYİ ARAÇ (16.11 15:31, Enes: "her haber için nasıl daha iyi ve kapsamlı yapabileceksen onu kullan"): haberi en doğru ve kapsamlı hâliyle almak için hangi araç gerekiyorsa o kullanılır: WebSearch, WebFetch, Chrome'da birincil kaynak (şirket IR, SEC EDGAR, Fed/BLS, Reuters/CNBC/Bloomberg sayfası), Yahoo verisi. Birincil kaynağı Chrome'dan açıp okumak kaliteyi artıracaksa açılır. (eski 15:29: Chrome yalnız gerektiğinde)
  - Kullanım limiti yine dikkate alınır: aynı bilgi WebSearch ile 2 kaynaktan netse Chrome açılmaz; limit dolmaya yaklaşırsa Enes'e söylenir.
  - TradingView'da paylaşım, yorum, fikir yayınlama, hesap/abonelik ayarı YOK. Kayıtlı çizim şablonları silinmez.
- Enes'in bilgisayarı: Windows, Claude in Chrome eklentisi, deviceId 2c13b0fb-418e-4a79-aee9-34fd79d23bef. Bilgisayar ve Chrome açıksa çalışır, kapalıysa Yahoo hesaplarına geçilir.
- TradingView planı Basic: grafik başına en fazla 2 gösterge.

## 11. PORTFÖY YÖNETİMİ — HER TURDA (16.11 12:47 → 13:25 kalıcı)
- 12:47 kuralı (EN ÖNEMLİ YENİ KURAL o an): araştırma yaparken portföyü de yönet. Ekle/çıkar fikirleri ver, grafikleri incele. Ancak 12:51'de "arada bir" denmişti.
- 13:09 / 13:25 GÜNCELLEME: grafik kaynağı bağlandığı için HER TURDA tweet işinin YANINDA:
  1. Portföydeki 7 hisse + fırsat gördüğüm hisselerin grafiklerine bakılır (bölüm 12-13).
  2. Beğendiğim/beğenmediğim bir şey, EKLEME fırsatı, AZALTMA/SATMA işareti, portföy dışı fırsat varsa Enes'e özel mesaj (SendUserMessage) atılır.
  3. Değişiklik yoksa her tur mesaj atmak zorunlu değil, ama grafiklere her tur bakılır. Önceki durumla karşılaştır, değişeni bildir.
- TWEETLERDE al/sat ASLA yok. Portföy notları yalnız Enes'e özel.
- Grafik kaynağı bağlı değilse eski kural geçerli: sadece SON 2 GÜN tarihli grafik/teknik analiz kaynakları (tarih kontrolü zorunlu).

## 12. GRAFİK KAYNAKLARI (öncelik sırası)
1. TRADINGVIEW (bilgisayar/Chrome açıksa):
   - Düzen adı "Adsız", id UN09ZFN8. URL: https://www.tradingview.com/chart/UN09ZFN8/?symbol=NASDAQ%3ATICKER (DOCN, VRT: NYSE%3A; CBRS: sadece CBRS).
   - Mevcut göstergeler (16.11 13:22'de Enes onayıyla): Vol 20 + Supertrend (10, hl2, 3) + LuxAlgo Smart Money Concepts. EMA 20/50/100/200 çıkarıldı, kaydedildi (ctrl+s).
   - Enes izni (13:22): ihtiyaç olursa bir göstergeyi çıkar, başkasını ekle, tekrar bak. Değişiklikten sonra ctrl+s ile kaydet; kaydedilmezse sembol değiştirirken "Leave site?" uyarısı çıkar.
   - SMC ve Supertrend için TradingView ESAS (benim hesabım yaklaşık).
   - Bakılacak dilimler: 1 saat, 4 saat, günlük, haftalık.
2. YAHOO FINANCE (Enes 13:16'da query1.finance.yahoo.com alan adını izinli listeye ekledi):
   - `python3 ta2.py <tickerlar>`: 21 gösterge, 4 zaman dilimi.
   - `python3 ta.py <tickerlar>`: eski kısa set.
3. ALPHA VANTAGE: bağlı ama ücretsiz anahtar ABD hisse verisi vermiyor ("premium gerekir"). KULLANMA.
4. TWELVE DATA: bağlantı sayfası telefonda açılmadı. Bilgisayardan bağlanması önerildi, henüz bağlı değil.

## 13. GÖSTERGE SETİ — HEPSİ ZORUNLU (16.11 13:27 + 13:28)
- Her analizde AŞAĞIDAKİLERİN HEPSİNE, FARKLI ZAMAN DİLİMLERİNDE (1s / 4s / günlük / haftalık) bakılır:
  RSI, MACD, EMA, SMA, Bollinger Bands, VWAP, Stochastic RSI, ADX, Ichimoku Cloud, ATR, OBV, CCI, Williams %R, Parabolic SAR, Supertrend, MFI, Fibonacci Retracement, Keltner Channels, Aroon, Volume Profile, SMC (Smart Money Concepts).
- Her birinin amacı (Enes 13:27):
  - EMA 200: ana trend yönü.
  - VWAP: SMC bölgelerinde fiyatın adil değeri (20 günlük + son ana dip/tepeden anchored).
  - RSI 14: likidite süpürmesi sonrası momentum kontrolü.
  - MACD: trend dönüşü ve momentum değişimini doğrulamak.
  - ATR: stop-loss ve hedef mesafeleri.
  - Volume Profile: önemli hacim bölgeleri ve likidite alanları (POC, değer alanı).
  - ADX: trendin gücü (+DI / -DI).
  - Fibonacci Retracement: OTE (Optimal Trade Entry) bölgeleri, 0.618-0.786.
  - OBV: hacim akışı ve olası uyumsuzluklar.
- SMC İÇİN ANA KOMBİNASYON (teyit): SMC + EMA 200 + VWAP + RSI 14 + ATR + Volume Profile + Fibonacci.
  - SMC zaten fiyat yapısını, order block, FVG, BOS, CHoCH ve likidite süpürmelerini analiz eder. Diğerleri teyit içindir.
- TAM TEST ZORUNLU (16.11 14:05, Enes, KESİN KURAL): kararı vermeden önce 21 göstergenin HEPSİ, 4 zaman diliminin HEPSİNDE (1s / 4s / günlük / haftalık) tek tek kontrol edilir. "Birkaç göstergeye bakıp karar" YASAK.
  1. `python3 ta2.py -v <tickerlar> > /tmp/ta.txt` (-v ŞART: tüm dilimlerde 21 göstergenin hepsini basar). Çıktının tamamı okunur.
  2. Bilgisayar açıksa TradingView'da da test edilir: Basic plan aynı anda 2 gösterge -> göstergeleri 2'şerli kapat-aç: (Supertrend + SMC), (RSI + MACD), (EMA 200 + VWAP), (Bollinger + Stoch RSI), (ADX + Ichimoku), (ATR + OBV), (CCI + Williams %R), (Parabolic SAR + MFI), (Fibonacci + Keltner), (Aroon + Volume Profile), (SMA). Her çift 1s/4s/G/H dillimlerinde bakılır, kararı destekleyenlerin ekran görüntüsü alınır. Sonunda varsayılan düzen geri kurulur (Supertrend + LuxAlgo SMC) ve ctrl+s.
  3. Karar mesajında her zaman dilimi için özet: "yukarı / aşağı / nötr" sayısı + kararı belirleyen göstergeler + dilimler arası çelişki (örn. 1s aşağı, 4s yukarı) açıkça yazılır.
  4. Kullanım limiti: TradingView rotasyonu her hisse için uzun sürer. Tam rotasyon karar verilen / değişen hisseler için yapılır; diğerleri ta2.py -v ile 21x4 tam test edilir (o da tam testtir, atlanmaz).
- Araç: invest/ta2.py. Günlükte 23 sinyalin hepsini, diğer dilimlerde özet basar; `-v` ile tüm dilimlerde hepsini. Her dilim için "yukarı / aşağı / nötr" sayısı verir.

## 14. ENES'E PORTFÖY NOTU — DİL VE İÇERİK
- "BEN OLSAM" DİLİ (16.11 13:31): tavsiye/öneri dili yok. Örnekler:
  - "Ben olsam bugün RKLB'den biraz eklerdim."
  - "Ben olsam bugün AXON'a girmezdim, 291 kırılmadan dipte dönüş görürsem 295-300 civarında eklerdim."
  - "Ben olsam elimde NBIS varsa 109 altında kapanırsa azaltırdım."
  - Bu dil SADECE Enes'e özel mesajlarda. Tweette al/sat yok kuralı aynen geçerli.
- DİP AVCISI (16.11 13:32): Enes yükselişin başında almak istemiyor, EN DİPLERİ bulmak istiyor. Not içeriği:
  - Dip bölgesi: SMC talep/order block, bull FVG, Fibonacci OTE 0.618-0.786, Volume Profile değer alanı altı/yüksek hacim düğümleri, haftalık destek.
  - Dip işaretleri: RSI / StochRSI / Williams %R / MFI aşırı satım; OBV ve RSI pozitif uyumsuzluk; likidite süpürmesi sonrası geri dönüş; kapitülasyon hacmi; CHoCH yukarı.
  - Kademeli alım seviyeleri: "ben olsam şu 2-3 seviyeden parça parça alırdım".
  - Tezin bozulduğu seviye (stop = ATR'ye göre ya da yapı altı). Hedef = VP POC / bear FVG / direnç.
  - Trend teyidi beklemek yerine fiyatın dip bölgesine yaklaştığını bildir.
- Kısa format: hisse + ne oldu + seviye(ler) + "ben olsam ...". Karar Enes'in.
- EN SON TAM TEST (16.11 14:15-14:25, bölüm 14e): RKLB portföyde alım için en uygun (1. kademe ~59,5, 2. kademe 53-55, azalt <50,6, tez biter <43,9). DOCN dibe yakın, teyit yok (1. kademe 79-84, 2. kademe 70-73, tez biter haftalık <69,8). Açılış öncesi RKLB 59,46, DOCN 84,00.
- SON TARAMA REFERANSI (16.11 13:30, Cuma kapanışı + açılış öncesi; açılış öncesi hepsi -%3 ile -%5,5):
  - RKLB: tek "Buy" (TradingView Supertrend desteği 57,2; günlük SMC 61,13'te yukarı CHoCH). Talep 44-50, bull FVG 53-55. ATR 4,9.
  - VRT: eşikte. Supertrend 202,2 altında kalırsa "Sell"e döner. Talep 160-170, 4s bull FVG 184-197. Haftalıkta 220,9 aşağı kırılmış.
  - SITM: Supertrend Sell 494. Bull FVG 398-426, talep 310-335. 4 saatlikte OBV pozitif uyumsuzluk.
  - DOCN: Supertrend Sell 102,3. Dip 69,8. Günlük ve 4 saatlikte OBV pozitif uyumsuzluk. Fiyat OTE içinde. Talep 51-56.
  - CBRS: Supertrend Sell 116. Dip 77,8. 4s bull FVG 85-92,5. 1 saatlikte toparlanma.
  - NBIS: Supertrend Sell 173,8. Günlük ve 4 saatlikte 23 sinyalin 20'si aşağı. Talep 100,7 ve 86,6. Williams %R aşırı satım.
  - AXON: en zayıfı (haftalık BOS aşağı 339). Dip 291,5, altında yakın talep yok. RSI 30.
- 13:31'de Enes'e verilen "ben olsam" planı: RKLB 58-60 al (stop 52, hedef 63,5 ve 70-71); VRT 202-205 geri alınırsa (stop 176, hedef 242); DOCN 79-84 küçük (stop 69,8 altı, hedef 97-102); SITM 398-426 (stop 355, hedef 491-494); CBRS 90 civarı bekle (stop 77,8 altı); NBIS alma, 109 altı kapanışta azalt; AXON girme, 291,5 tutar ve 1 saatlikte 323 üstü gelirse dönüş ara.
  - Bu plan 13:32 dip-avcısı kuralından ÖNCE yazıldı. Sonraki notlar dip bölgesi + kademeli alım mantığıyla yazılmalı.

## 14b. GÜNDE 2 SABİT TEKNİK KONTROL (16.11 13:55, Enes)
- Her ABD işlem günü İKİ kez: açılıştan 30 dk sonra (18:00 TSİ) ve kapanıştan 30 dk önce (23:30 TSİ). (ABD yaz saatinde 17:00 ve 23:00; yarım günlerde kapanış 21:00 TSİ ise 20:30.)
- Kapsam: portföyün tamamı (DOCN RKLB SITM AXON CBRS VRT AVGO; 16.11 23:44, eski: NBIS RKLB DOCN SITM AXON CBRS VRT) + benim yatırıma uygun bulduğum EN İYİ 3-4 hisse (portföy dışı, herhangi bir ABD hissesi; temel + teknik gerekçeyle).
- Yöntem: `python3 ta2.py <tickerlar> > /tmp/ta.txt` (21 gösterge, 1s/4s/günlük/haftalık) + bilgisayar açıksa TradingView (UN09ZFN8, SMC + Supertrend). Gün içi fiyatı mutlaka kullan.
- Çıktı: Enes'e tek SendUserMessage, her hisse için "ben olsam ..." kararı (bölüm 14 dili): dip bölgesi, kademeli alım seviyeleri, tezin bozulduğu seviye, hedef. Değişiklik olmasa da bu iki kontrolde mesaj HER ZAMAN atılır.
- (16.11 21:43, KURAL 5f, GEÇERLİ OLAN) Ekran görüntüsünü ENES alır; Claude her hisse için "TradingView'da $TICKER → dilim → açık olacak 2 gösterge → neye bakılacak" talimatı + tweet taslağı + düşüncelerini tek mesajda, sırayla gönderir. Aşağıdaki SendUserFile maddeleri eski kuraldır.
- GRAFİK EKRAN GÖRÜNTÜSÜ (16.11 14:00, Enes): "ben olsam" kararının dayandığı göstergeleri gösteren grafik görüntüsü Enes'e SendUserFile ile atılır (önemli karar/değişiklik olan hisseler için, her kontrolde en çok 3-4 görsel; kullanım limiti).
  - Bilgisayar açıksa: TradingView (UN09ZFN8, ilgili zaman dilimi), mcp__claude-in-chrome__computer screenshot save_to_disk=true. Basic plan 2 gösterge sınırı: gerekirse göstergeyi değiştir, görüntüyü al, ctrl+s. X'e girme.
  - (İPTAL 16.11 18:05: kendi çizimi grafik gönderilmez, yalnız TradingView ekran görüntüsü. Bilgisayar kapalıysa görsel yok, Enes'e söylenir.) Eski: Yahoo verisinden matplotlib ile koyu temalı grafik çiz (fiyat + EMA 200 + VWAP + dip bölgesi/FVG/OB kutuları + Fib OTE + alt panelde RSI/MACD/OBV), kararı destekleyen seviyeler işaretli. invest/g/ta/ altına kaydet.
  - Görsele kısa açıklama: hangi gösterge neyi gösteriyor, karar neden bu.
- Tweet değildir; al/sat tweette yok kuralı aynen geçerli. Portföy güncellemesi tweetini Enes atar.
- Zincir: her kontrol sonunda bir sonraki kontrol için send_later kurulur (18:00 -> 23:30 aynı gün; 23:30 -> sonraki işlem günü 18:00). Hafta sonu ve ABD tatilleri atlanır (26.11.2026 Şükran Günü kapalı; 27.11 yarım gün).

## 14c. HİSSE SEÇİMİ = PROFESYONEL YÖNTEM (16.11 13:58, Enes, KESİN KURAL)
Hisse araştırırken, beğenirken ve portföyle karşılaştırırken profesyonel bir yatırımcı / portföy yöneticisi / aracı kurum analisti neye bakıyorsa ona bakılır. HEM TEMEL HEM TEKNİK. Teknik taraf Enes'in verdiği set (bölüm 13: 21 gösterge + SMC kombinasyonu, 4 zaman dilimi). Temel taraf aşağıdaki kontrol listesi. Her rakam 2 kaynak, yıl kontrolü; bulunamayan "bilinmiyor" diye yazılır, uydurulmaz.

A) TEMEL KONTROL LİSTESİ (her aday ve her portföy hissesi için aynı liste)
1. İş ve hendek: ne satıyor, pazar büyüklüğü, rakipler, rekabet avantajı (teknoloji, ölçek, geçiş maliyeti, ağ etkisi), müşteri yoğunlaşması (tek müşteri %20+ ise risk).
2. Büyüme: gelir büyümesi (YoY ve çeyrekten çeyreğe), hızlanıyor mu yavaşlıyor mu, organik mi satın almalı mı (organik payı hesaplanır), sipariş birikimi / RPO / backlog.
3. Kârlılık: brüt marj ve trendi, faaliyet marjı, net kâr; zarardaysa kâra geçiş yolu. GAAP ile düzeltilmiş arası fark ve hisse bazlı ödeme (SBC) büyüklüğü.
4. Nakit: serbest nakit akışı (FCF) ve marjı, capex yükü, nakit yakma hızı ve kaç çeyrek yeteceği.
5. Bilanço: net nakit / net borç, borç vadesi, faiz karşılama, likidite. Hisse seyrelmesi (hisse sayısı artışı, konvertibl, ATM satışları).
6. Değerleme: ileri F/K, EV/Satış, EV/FAVÖK, PEG, FCF getirisi; rakiplere ve kendi 3-5 yıllık geçmişine göre ucuz mu pahalı mı. Büyümeye göre fiyat (Rule of 40 yazılım/bulut için).
7. Beklenti momentumu: son 30-90 günde EPS ve gelir tahmin revizyonları (yukarı/aşağı), son bilançoda beklenti aşımı/kaçırma, şirketin kendi tahmininin (guidance) yükseltilmesi/düşürülmesi.
8. Analist ve kurum: not/hedef değişiklikleri (kurum + eski/yeni hedef), 13F'de kurum giriş/çıkışları, içeriden alım-satım (Form 4; kod P alım anlamlı, 10b5-1 ve vergi satışları ayrılır).
9. Pozisyonlanma: açığa satış oranı ve kapanma günleri, opsiyon ima edilen hareket, hacim ve likidite (günlük işlem hacmi), piyasa değeri.
10. Katalizör ve takvim: sonraki bilanço tarihi, ürün/sözleşme duyuruları, lock-up bitişi, endeks girişi, düzenleme kararları.
11. Riskler: dava, düzenleme, ihracat kontrolleri, yönetim değişikliği, muhasebe uyarıları, short raporları (tek kaynaksa doğrulanmamış diye belirtilir), müşteri kaybı, makro duyarlılık (faiz, dolar, emtia).
12. Yönetim ve sermaye dağıtımı: geri alım/temettü, satın alma geçmişi, yöneticinin hisse sahipliği.
13. Makro ve sektör rejimi: faiz beklentisi, sektör rotasyonu, sektörün göreceli gücü (S&P 500 ve sektör ETF'ine göre), risk iştahı.

B) TEKNİK (bölüm 13 aynen): EMA 200 trend, SMC yapısı (BOS/CHoCH, order block, FVG, likidite süpürmesi), VWAP, RSI 14, MACD, ATR (stop/hedef mesafesi), Volume Profile (POC, değer alanı), ADX, Fibonacci OTE 0.618-0.786, OBV uyumsuzluğu + kalan göstergeler; 1s/4s/günlük/haftalık. Enes dip avcısı: dip bölgesi ve kademeli alım seviyesi öncelikli.

C) ADAY BULMA SÜRECİ
1. Tarama: güncel haberler, tahmin revizyonu yukarı olanlar, güçlü bilanço + düşük değerleme, sektör gücü, aşırı satılmış kaliteli hisseler (dip bölgesine gelen). Evren: tüm ABD borsası, izleme listesiyle sınırlı değil.
2. Kısa liste (6-10) -> A listesi + B tekniğiyle eleme -> en iyi 3-4.
3. Her aday için PUAN KARTI: Temel (iş/hendek, büyüme, kârlılık, nakit/bilanço, değerleme, beklenti momentumu, risk) ve Teknik (trend, dip bölgesine uzaklık, momentum/uyumsuzluk, risk/ödül = hedef mesafesi / stop mesafesi). Her başlık 1-5. Toplam ve kısa gerekçe.

D) PORTFÖYLE KARŞILAŞTIRMA (zorunlu)
- Portföydeki 7 hisse AYNI puan kartıyla puanlanır.
- Aday, portföydeki en zayıf hisseden AÇIKÇA daha iyiyse (toplamda belirgin üstün ve risk/ödülü daha iyi) önerilir: "Ben olsam X'i azaltıp/çıkarıp Y'ye geçerdim, çünkü ..." + seviyeler.
- Daha iyi seçenek YOKSA önerilmez; "portföyündekilerden daha iyisini bulamadım" denir ve neden kısaca söylenir. Zorla öneri yapılmaz.
- Portföy hissesi için de: tez bozulduysa (temel ya da yapı) açıkça söylenir.

E) DİL VE SINIRLAR
- Enes'e özel mesaj, "ben olsam" dili (bölüm 14). Karar Enes'in. Tweette al/sat yok.
- Kaynak belirtilir; tek kaynaklı bilgi "doğrulanmadı" diye işaretlenir ya da kullanılmaz.
- Bu yöntem 18:00 ve 23:30 teknik kontrollerinde (bölüm 14b) ve her fırsat önerisinde uygulanır. Temel taraf invest/temel_karne.md'den okunur (bölüm 14g, 16.11 18:14). (eski: "Kullanım limitine dikkat: temel analiz günde bir kez derinlemesine (18:00), 23:30'da yalnız değişenler güncellenir." -> bu yüzden 16.11 18:00'de temel kart yapılamadı; artık turlarda önceden hazırlanır.)

## 14d. TEKNİK ANALİZ TWEETLERİ VE GÖRSELLERİ — ENES PAYLAŞIR (16.11 14:15, Enes, KESİN KURAL)
- (16.11 21:43, KURAL 5f) Görsel yerine Enes'e ekran görüntüsü TALİMATI verilir (hisse, dilim, açık 2 gösterge, neye bakılacak); tweet + düşünceler aynı mesajda. Aşağıdaki 1. madde (Claude'un görüntü alması) eski kuraldır.
- 18:00 ve 23:30 kontrollerinde bakılan HER hisse için (portföydeki 7 hisse + aday/fırsat hisseleri + test amaçlı bakılanlar) AYRI AYRI hazırlanır:
  1. TradingView ekran görüntüsü (kural 5e: kararı belirleyen 2 gösterge açık; düzen QdeLE4v4; eski UN09ZFN8, ilgili dilim; gerekiyorsa göstergeler 2'şerli değiştirilerek birkaç görüntü). Kendi çizimimiz gönderilmez (kural 5b).
  2. O hisseye özel teknik analiz tweet taslağı (bölüm 6 "TEKNİK ANALİZ TWEETİ DİLİ").
  - Enes'e her hisse ayrı mesaj + ayrı SendUserFile olarak gönderilir (tweet metni + görsel birlikte).
- TEKNİK ANALİZ TWEETLERİNİ CLAUDE PAYLAŞMAZ. Buffer'a gönderilmez. Enes kendisi teyit edip paylaşır (Buffer aylık 1000 gönderi hakkı korunur). Otomatik turlar teknik analiz tweeti atmaz.
- KANIT ZORUNLU (16.11 14:15): "şuradan kademe eklerim / orayı kırarsa şuradan eklerim / şunun altında tez biter / hedef şu" denen HER seviyenin NEDENİ yazılır: hangi göstergeler ve hangi zaman dilimleri o bölgede çakışıyor.
  - Tweette sade dille kısa gerekçe: ör. "79-84'ü seçmemin sebebi: günlükte doldurulmamış bir boşluk var, 1 saatlikte trend göstergesi orada destek veriyor ve fiyat daha önce burada alıcı buldu."
  - Enes'e özel notta tam gerekçe: "79,2-84,3 = günlük bull FVG + 1s Supertrend AL 83,5 + 1s Ichimoku bulutu 78,9-81,8 + 4s bull FVG 79,2". En az 2 bağımsız gösterge/dilim çakışmayan seviye kademe olarak verilmez.
  - Görselde her seviyenin yanında gerekçe etiketi olur.
- Bu kurallar devir notu yeniden yazılırsa aynen korunur.

## 14g. TEMEL KARNE SİSTEMİ (16.11 18:14, Enes: "neden temelleri yapmadın, turlarda vaktin vardı, problemin çözümünü bul", KESİN KURAL)
SORUN: 16.11 18:00 kontrolünde temel puan kartı "kısmi" kaldı. Neden: temel analiz (13 madde x 10 hisse) kontrolün içine bırakılmıştı; aynı anda 21 gösterge x 4 dilim teknik + 10 ekran görüntüsü + 10 tweet yapılınca kullanım limiti yüzünden temel kısım atlandı. Ayrıca kabuktan (curl) Yahoo quoteSummary (crumb 429), SEC, stockanalysis, finviz erişilemiyor; Alpha Vantage COMPANY_OVERVIEW premium (kullanılamaz).
ÇÖZÜM:
1. Dosya: invest/temel_karne.md. Üstte özet tablo (hisse, tarih, 7 başlık 1-5, toplam /35, kısa not), altta her hisse için ayrıntılı kart (14c-A 13 madde 7 başlık altında toplanır, her rakamın kaynağı yazılır).
2. Ne zaman: HER OTOMATİK TURDA, tweet paylaşıldıktan ve DONGU yazıldıktan sonra, send_later kurulmadan önce 1-2 hissenin kartı yazılır/yenilenir (rotasyon: tablodaki "eksik" olanlar, sonra en eski tarihli). 09:00-01:00 arası ~25 dk'da bir tur -> 10 hisse ~3 saatte biter. Gece ve hafta sonu turları da (paylaşım olmasa bile) kart yazabilir.
3. Veri yolu (bu sırayla, en iyi sonucu veren): (a) WebFetch https://stockanalysis.com/stocks/<ticker küçük>/statistics/ (piyasa değeri, EV, ileri F/K, PEG, EV/Satış, EV/FAVÖK, marjlar, FCF, nakit/borç, hisse sayısı değişimi, açığa satış, analist sayısı; sayfanın veri tarihini yaz) (b) WebSearch "<şirket> third quarter 2026 results revenue guidance" (bilanço, rehber, büyüme hızlanması, ikinci kaynak) (c) gerekirse Chrome'da yeni sekmede IR sayfası / finviz, iş bitince sekmeyi kapat (d) analist not değişiklikleri: Benzinga/MarketBeat/TipRanks/TheFly. Her rakam 2 kaynak; tek kaynaksa "(tek kaynak)" yazılır; tutarsız görünen rakam (ör. fiyatla uyuşmayan analist hedefi) "DOĞRULANMADI, kullanma" diye işaretlenir.
4. Tazelik: kart 7 günden eskiyse ya da arada bilanço, rehber değişikliği, büyük haber, analist not dalgası olduysa yenilenir. Bilanço açıklayan portföy hissesinin kartı aynı gün yenilenir.
5. Kullanım: 18:00/23:30 kontrolleri temel puanı karttan okur, teknik puanla birleştirir (14c-C3 puan kartı), portföyle karşılaştırmayı (14c-D) bu toplamlarla yapar. Kontrol mesajında her hisse için "temel X/35 (kart tarihi)" yazılır. Kart eksikse açıkça söylenir; "kısmi" denip geçilmez.
6. Yeni aday: aday listesine giren hisse önce kartla puanlanır, kartı olmayan hisse "değişim önerisi"ne konu olamaz.
7. DONGU'ya "KARNE: <hisse> <toplam>" satırı yazılır, dosya commit + push edilir.
8. Bu bölüm devir notu yeniden yazılırsa aynen korunur.

## 14h. GENİŞLETİLMİŞ METRİK LİSTESİ — PROFESYONEL KARNE (16.11 18:19, Enes: "daha da geliştir, daha çok metrikle, profesyonel bir borsacı gibi çok fazla detaya bak", KESİN KURAL)
14c-A'daki 13 madde ve 14g aynen geçerli; bu bölüm onları AYRINTILANDIRIR. Her karnede aşağıdaki metrikler tek tek aranır. Bulunamayan "bilinmiyor" yazılır (uydurulmaz), her rakam 2 kaynak, tek kaynaksa "(tek kaynak)", veri tarihi yazılır. Son 4-8 çeyrek TREND gösterilir (tek rakam değil, yön).

1) BÜYÜME (puan 1-5)
- Gelir: son çeyrek YoY ve QoQ, son 4 çeyrek YoY dizisi (hızlanıyor mu = ikinci türev), TTM, 3 yıllık CAGR.
- Segment ve coğrafya büyümesi; organik / satın alma payı (satın alınan gelir çıkarılarak organik % hesaplanır).
- Sipariş göstergeleri: backlog, RPO, cRPO (12 ay), book-to-bill, sözleşmeli kapasite.
- Abonelik/SaaS: ARR ve net yeni ARR, NRR/NDR, brüt elde tutma, müşteri sayısı, 100 bin $+ müşteri sayısı, ARPU.
- Rehber: şirket rehberi vs analist konsensüsü (çeyrek + yıl), rehber yükseltme/düşürme geçmişi.
- Konsensüs: gelecek yıl gelir ve HBK büyüme beklentisi, 2-3 yıllık beklenti.
2) KÂRLILIK
- Brüt marj (4-8 çeyrek trend), GAAP ve düzeltilmiş faaliyet marjı, FAVÖK marjı, net marj, artımlı (incremental) marj.
- Gider yapısı: Ar-Ge / satış-pazarlama / genel yönetim, gelire oranı ve trendi; faaliyet kaldıracı.
- SBC (hisse bazlı ödeme) / gelir; GAAP-düzeltilmiş kâr farkı ve nedeni.
- Getiri oranları: ROE, ROA, ROIC; ROIC > sermaye maliyeti (WACC ~%8-10) mı.
- Rule of 40 (büyüme % + FCF marjı %), yazılımda magic number / CAC geri dönüş süresi (bulunursa).
3) NAKİT AKIŞI
- Faaliyet nakit akışı, FCF, FCF marjı, FCF dönüşümü (FCF / net kâr), SBC düşülmüş FCF.
- Capex / gelir, bakım vs büyüme capex; finansal kiralama ve ekipman finansmanı ile "gizli capex" (FCF'ye dahil edilmeyen).
- İşletme sermayesi: alacak gün (DSO), stok gün (DIO), borç gün (DPO), nakit dönüşüm süresi; stok ve alacak gelirden hızlı artıyor mu (kırmızı bayrak).
- Zarardaysa: çeyreklik nakit yakma ve kaç çeyrek yeteceği (runway).
4) BİLANÇO VE SEYRELME
- Nakit + yatırımlar, toplam borç, net nakit/borç, net borç / FAVÖK, faiz karşılama (FAVÖK / faiz gideri).
- Cari oran, asit-test oranı; borç vade takvimi (yakın vadede büyük ödeme var mı), konvertibl tahviller ve dönüşüm fiyatı, kiralama yükümlülükleri.
- Şerefiye / toplam varlık (satın alma riski), Altman Z, Piotroski F (bulunursa).
- Hisse sayısı değişimi (yıllık %), seyrelme kaynağı (SBC, ATM satışı, konvertibl, satın alma), geri alım ile net etki.
5) DEĞERLEME
- F/K (TTM + ileri), PEG, EV/Satış (TTM + gelecek 12 ay), EV/FAVÖK, EV/FCF, F/FCF, PD/DD, FCF getirisi, kâr getirisi (E/P) vs 10 yıllık ABD tahvil faizi.
- AKRAN KARŞILAŞTIRMASI: en az 3-5 rakiple aynı çarpanlar (medyan), büyümeye göre düzeltilmiş (EV/Satış / büyüme).
- KENDİ GEÇMİŞİ: 3-5 yıllık çarpan aralığında şu an nerede (ucuz/orta/pahalı).
- TERS DCF: bugünkü fiyat hangi büyüme/marjı fiyatlıyor, gerçekçi mi.
- SENARYO: ayı / baz / boğa (gelir büyümesi + marj + hedef çarpan) -> 12 aylık fiyat aralığı ve olasılık tahmini; risk/ödül oranı.
- Analist hedefleri: ortalama, en yüksek, en düşük, dağılım; fiyatla tutarsız hedef DOĞRULANMADI işaretlenir.
6) BEKLENTİ MOMENTUMU
- HBK ve gelir tahmin revizyonları 7 / 30 / 90 gün (yukarı/aşağı sayısı ve %).
- Son 4-8 bilançoda beklenti aşımı/kaçırma ve büyüklüğü (%), bilanço sonrası hisse tepkisi ve sonraki günlerde devam (drift).
- Not değişiklikleri (yükseltme/düşürme, kurum, eski/yeni hedef) son 90 gün.
- Kâr kalitesi: tahakkuk oranı, tek seferlik kalemler, gelir tanıma değişikliği.
7) SAHİPLİK VE AKIŞ
- İçeriden işlemler (Form 4, son 3-6 ay): P kodlu alımlar ayrı, 10b5-1 planlı satışlar ve vergi satışları ayrı.
- Kurum sahipliği ve son 13F değişimi (büyük fonlar giriş/çıkış), ETF sahipliği, halka açıklık (float).
- Açığa satış: float %'si, kapanma günü, ödünç maliyeti (bulunursa), son 2 raporda değişim.
- Opsiyon: ima edilen volatilite ve IV seviyesi (rank), bilanço için ima edilen hareket, put/call oranı, olağandışı opsiyon akışı.
- Likidite: ortalama günlük işlem hacmi ($), piyasa değeri sınıfı.
8) GÖRECELİ GÜÇ VE FİYAT DAVRANIŞI (temel karnede kısa; ayrıntı bölüm 13 teknikte)
- Getiri 1 hafta / 1 ay / 3 ay / yılbaşından beri / 1 yıl; S&P 500'e ve sektör ETF'ine (ör. XLK, SMH, IGV, ITA, XLI, XLB) göre fark.
- 52 hafta zirve ve dibe uzaklık, beta, yıllık volatilite, son büyük düşüşün (drawdown) büyüklüğü.
9) KALİTE, HENDEK VE YÖNETİM
- Hendek türü (ağ etkisi, geçiş maliyeti, ölçek, patent/teknoloji, marka, düzenleme lisansı) ve kanıtı (fiyatlama gücü, brüt marj istikrarı, müşteri kaybı oranı).
- Müşteri yoğunlaşması (en büyük müşteri %, ilk 10), tedarikçi yoğunlaşması (tek tedarikçi riski, ör. NVIDIA/TSMC).
- Tekrarlayan gelir payı, sözleşme süreleri.
- Yönetim: CEO/CFO geçmişi ve görev süresi, rehberi tutturma geçmişi, sermaye dağıtımı (satın almalar başarılı mı, geri alım/temettü), yönetimin hisse sahipliği.
- Muhasebe kırmızı bayrakları: denetçi değişikliği, yeniden düzenleme (restatement), ilişkili taraf işlemleri, geç 10-Q/10-K, SEC soruşturması, short raporu (tek kaynaksa doğrulanmadı).
10) RİSK, KATALİZÖR, MAKRO
- Risk: dava, düzenleme, ihracat kontrolü, Çin/Tayvan gelir payı ve jeopolitik, kur, faiz duyarlılığı, emtia girdi maliyeti, kilit kişi riski, lock-up bitişi.
- Katalizör takvimi: sonraki bilanço tarihi, yatırımcı günü, ürün lansmanı, büyük sözleşme, endeks girişi (S&P 500 uygunluğu), FDA/düzenleme tarihleri.
- Makro/sektör rejimi: faiz beklentisi, sektör rotasyonu, risk iştahı, sektörün son 1-3 ay göreceli gücü.

SEKTÖRE ÖZEL KPI (ilgili olan mutlaka bakılır):
- AI bulut / neo-bulut (NBIS, DOCN, CRWV vb.): sözleşmeli güç (MW/GW), GPU kapasitesi ve kullanım oranı, backlog/RPO, en büyük müşteri payı, capex/gelir, finansman maliyeti, GPU amortisman süresi.
- Yarı iletken (SITM, AVGO, TSM, VRT tedarik): book-to-bill, stok günleri (şirket + kanal), brüt marj, tasarım kazanımları, son pazar dağılımı (veri merkezi/oto/endüstri/tüketici), kapasite kullanımı, düğüm (node) karışımı (TSM).
- Uzay/savunma (RKLB): backlog ve 12 ay içinde gelire dönecek kısmı, fırlatma sıklığı ve başarı, Neutron takvimi, devlet sözleşmesi payı, uzay sistemleri vs fırlatma marjı.
- Kamu güvenliği / SaaS (AXON): ARR, NRR, toplam rezervasyon, yazılım payı, TASER/kamera birim büyümesi, ABD dışı büyüme.
- Elektrik/soğutma altyapısı (VRT): sipariş büyümesi, book-to-bill, backlog, veri merkezi payı, fiyatlama, kapasite artışı.
- Çip/AI donanım yeni halka arz (CBRS): müşteri yoğunlaşması (G42 vb.), çekirdek gelir, RPO, lock-up takvimi, IPO fiyatına göre konum.
- Kimya/hijyen (ECL): organik satış, fiyat/hacim ayrımı, brüt marj genişlemesi, hammadde maliyeti.
- Perakende/tüketici: aynı mağaza satışı, işlem sayısı ve ortalama sepet, stok/satış.
- Banka/finans: net faiz marjı, CET1, kredi kalitesi (takipteki krediler), mevduat değişimi.
- Biyoteknoloji: nakit runway, faz takvimi, onay tarihleri (PDUFA), pazar büyüklüğü, ortaklık.

PUANLAMA (14g'nin üstüne): 10 başlık x 1-5 = /50 (BÜYÜME, KÂRLILIK, NAKİT, BİLANÇO, DEĞERLEME, MOMENTUM, SAHİPLİK/AKIŞ, GÖRECELİ GÜÇ, KALİTE/YÖNETİM, RİSK/KATALİZÖR; RİSK'te 5 = düşük risk). Her başlığın yanına 1 cümle gerekçe. Sonra TEKNİK puan (bölüm 13) ayrı yazılır, karşılaştırma (14c-D) temel /50 + teknik birlikte yapılır. Eski /35 kartlar yenilenirken /50'ye çevrilir.
KAYNAKLAR (karne için, sırayla): WebFetch stockanalysis.com/stocks/<t>/statistics/, /financials/?p=quarterly, /financials/cash-flow-statement/?p=quarterly, /financials/balance-sheet/?p=quarterly, /forecast/; şirket IR bülteni ve sunumu (Chrome gerekirse); WebSearch: bilanço haberleri (Reuters, CNBC, Barchart/StockStory, Earnings Whispers, Investing), analist notları (Benzinga, MarketBeat, TipRanks, TheFly), içeriden işlemler (secform4, OpenInsider, MarketBeat insider), açığa satış (Nasdaq short interest, MarketBeat), opsiyon IV (Barchart, Market Chameleon), 13F (WhaleWisdom, HoldingsChannel). Kabuktan curl bu sitelere ULAŞAMIYOR (proxy) -> WebFetch/WebSearch/Chrome kullan.
SÜRE: tek kart çok uzarsa (kullanım limiti) o turda 1 hisse yapılır; kart en az 10 başlığın hepsini puanlamadan "tamam" sayılmaz, eksik metrik "bilinmiyor" diye geçilebilir ama başlık boş geçilemez.
Bu bölüm devir notu yeniden yazılırsa aynen korunur.


## 14i. TEMEL KARNE ÖZ-DENETİMİ — YANLIŞ VE ADALETSİZ SONUÇ ÖNLEME (16.11 21:16, Enes: "yanlış veya adaletsiz sonuç nasıl çıkar düşün, ne eklenebilir düşün ve gittikçe geliştir", KESİN KURAL)
Amaç: karne puanı gerçeği yansıtsın, hisseler arasında adil karşılaştırılabilsin. 14c, 14g, 14h aynen geçerli; 14i onların üstüne eklenir. Bu bölüm silinmez, sadece büyür.

A) HATA / ADALETSİZLİK KONTROL LİSTESİ (her karneden sonra tek tek, karnenin sonuna "DENETİM: A1 ✓, A2 düzeltildi (...) ..." satırı yazılır)
VERİ DOĞRULUĞU
A1. ESKİ FİYAT / ESKİ VERİ: kaynağın veri tarihi yazıldı mı? Değerleme çarpanları (F/K, EV/Satış, FCF getirisi, piyasa değeri) BUGÜNKÜ fiyatla yeniden hesaplandı mı? (16.11 örnek: ECL stockanalysis verisi 27.10 tarihli, fiyat 26.10 -> ileri F/K eski fiyatla.) 7 günden eski çarpan doğrudan puana giremez.
A2. BİRİM / BÜYÜKLÜK: milyon-milyar, çeyrek-yıl, TTM-çeyrek karışmış mı? Rakamın büyüklüğü şirketin gelirine göre makul mü? (16.11 örnek: KuCoin CBRS yıllık rehberini 9,4-9,6 Mr$ yazdı, doğrusu 940-960 Mn$.)
A3. YIL / DÖNEM: 2025-2026 karışması; şirketin mali yılı takvim yılından farklı mı (TSN, NVDA)? Çeyrek adı doğru mu?
A4. TEK KAYNAK AĞIRLIĞI: bir başlığın puanı ağırlıkla tek kaynaklı rakamlara mı dayanıyor? Öyleyse o başlığa "(güven düşük)" yazılır ve puan uç değer (1 veya 5) olamaz, en fazla 2-4.
A5. DÜZELTİLMİŞ vs GAAP TUTARLILIĞI: bütün hisselerde aynı tanım mı kullanıldı? Bir hissede düzeltilmiş marj, diğerinde GAAP marj ile puan vermek adaletsiz. Kural: KÂRLILIK puanı iki ayağa bakar (düzeltilmiş + GAAP farkı/SBC); fark gelirin %10'undan büyükse 1 puan kırılır.
A6. HİSSE BÖLÜNMESİ / SEYRELME: hisse başı rakamlar (HBK, hedef fiyat) bölünme öncesi/sonrası karışmış mı? Hisse sayısı değişimi halka arz veya satın alma kaynaklıysa açıklandı mı?
A7. ANALİST HEDEFİ: ortalama hedef bugünkü fiyatla tutarsızsa (çok üstte/altta ve tarihi eski) puana girmez, "DOĞRULANMADI" yazılır.
ADALET (aynı ölçüyle ölçme)
A8. SEKTÖRE GÖRE ADALET: mutlak eşik yerine AKRAN eşiği. Ör. erken aşama büyüme şirketinde negatif FCF tek başına 1 puan değildir; nakit yakma süresi (runway) ve yatırımın gelir dönüşü de bakılır. Olgun şirkette %7 büyüme "orta" değil sektör içinde iyi olabilir. Her başlıkta gerekçeye "akrana göre" bir cümle eklenir.
A9. ÇİFT SAYIM: aynı olgu iki başlıkta cezalandırıldı/ödüllendirildi mi? Ör. fiyat düşüşü hem MOMENTUM hem GÖRECELİ GÜÇ'te; düşük FCF hem NAKİT hem BİLANÇO'da; müşteri yoğunlaşması hem KALİTE hem RİSK'te. Kural: bir olgu tek başlıkta puanı belirler, diğerinde sadece not edilir. ÖNEMLİ: GÖRECELİ GÜÇ fiyat trendidir ve teknik puanla (bölüm 13) çakışır -> 14c-D karşılaştırmasında "temel" toplam, GÖRECELİ GÜÇ HARİÇ /45 olarak da yazılır; teknik ayrı puanlanır. Böylece teknik zayıflık iki kez sayılmaz.
A10. İNORGANİK BÜYÜME: satın almalı büyüme organik gibi puanlandı mı? BÜYÜME puanı organik büyümeyle verilir; satın alma katkısı ayrıca yazılır. (16.11: SITM TPD, ECL Ovivo/CoolIT, VRT +6 puan.)
A11. BİLİNMEYEN = CEZA DEĞİL: "bilinmiyor" metrik puanı otomatik düşürmez de yükseltmez de; ama bir başlıktaki metriklerin yarısından fazlası bilinmiyorsa o başlık "(güven düşük)" ve puan 2-4 arası.
A12. YENİ HALKA ARZ / KISA GEÇMİŞ: 52 hafta, 5 yıllık çarpan geçmişi yoksa bu eksiklik ceza değildir; yerine halka arz fiyatı ve akranlar kullanılır.
A13. PORTFÖY YANLILIĞI: portföydeki hisseye "sahip olduğumuz için" kolay puan, adaya zor puan verilmedi mi? Kontrol: puanı yazmadan önce rakamlara bakıp "bu rakamlar tanımadığım bir şirketin olsaydı kaç verirdim?" sorusu.
A14. GÜNCEL HABER YANLILIĞI: o günün haberi (Fed konuşması, sektör satışı, analist notu) uzun vadeli başlıkları (KALİTE, BİLANÇO) etkiledi mi? Günlük haber sadece MOMENTUM ve RİSK/KATALİZÖR'e girer.
A15. ANLATI YANLILIĞI: "yapay zeka hikayesi" gibi bir tema rakamla desteklenmeden puan yükseltti mi? Her puan en az 1 rakama dayanmalı.
A16. SENARYO ÇARPANLARI KEYFİ Mİ: ayı/baz/boğa çarpanları şirketin kendi geçmiş aralığına veya akran medyanına bağlandı mı? Bağlanamıyorsa "kaba" etiketi zorunlu.
A17. EŞİT AĞIRLIK ADALETSİZLİĞİ: 10 başlık eşit ağırlıklı; büyüme şirketi ile savunmacı şirketi aynı toplamla kıyaslamak yanıltabilir. Kontrol: karşılaştırmada toplamın yanında "en zayıf 2 başlık" ve "kırmızı bayrak var/yok" da yazılır; toplam tek başına karar değildir.

B) KIRMIZI BAYRAK (toplam ne olursa olsun karar notunda ayrıca yazılır)
- Tek müşteri gelirin %25'inden fazla (ör. CBRS 2025: MBZUAI %62, G42 %24).
- Nakit 4 çeyrekten az yetiyor ve finansman garantisi yok.
- Net borç / FAVÖK > 4 ya da yakın vadede karşılanamayan borç.
- Rehber üst üste 2 çeyrek düşürüldü.
- Muhasebe uyarısı, yeniden düzenleme, denetçi değişikliği, SEC soruşturması.
- Yıllık hisse seyrelmesi %10'dan fazla (halka arz yılı hariç, o da not edilir).
- Açığa satış float'ın %15'inden fazla.

C) KALİBRASYON (her 5 karnede bir + her gün ilk turda)
1. Tablodaki bütün karneler yan yana okunur: sıralama mantıklı mı? Ör. "X, Y'den 3 puan yüksek; rakamlar bunu destekliyor mu?" Her başlık için en yüksek ve en düşük puanlı hisse kontrol edilir; ölçek kaymışsa (bugün 4 verilen şey dün 3 verildiyse) düzeltilir.
2. Puan çapaları (sektör içi): 5 = akranların en iyi %20'si, 4 = üst-orta, 3 = medyan civarı, 2 = alt-orta, 1 = en kötü %20 ya da kırmızı bayrak. Çapa için akran rakamı yoksa "(çapa yok)" yazılır.
3. Tarihi 7 günden eski karneler ve arada bilanço/büyük haber olanlar yenileme sırasına öne alınır.
4. Kalibrasyon sonucu DONGU'ya "KALİBRASYON: değişen puanlar ..." diye yazılır.

D) HATA GÜNLÜĞÜ (bulunan her hata buraya; tekrar eden hata türü A'ya yeni madde olarak eklenir)
- 16.11 21:20 | ECL | A1 eski veri: stockanalysis 27.10 fiyatıyla ileri F/K 33,6 -> bugünkü ~309$ ile 2026 F/K ~38 olarak düzeltildi, DEĞERLEME 2 korundu.
- 16.11 21:20 | CBRS | A2 birim: KuCoin "9,4-9,6 Mr$" rehberi yanlış -> 940-960 Mn$ (Investing, Leafy) kullanıldı.
- 16.11 21:20 | NBIS RKLB SITM AXON CBRS VRT ECL | A9 çift sayım: GÖRECELİ GÜÇ fiyat trendi teknik puanla çakışıyor -> 14c-D karşılaştırmasında GÖRECELİ GÜÇ hariç /45 de yazılacak (temel_karne.md tablosuna "/45" sütunu eklendi).
- 16.11 21:20 | CBRS VRT ECL | A4 tek kaynak: NAKİT ve BİLANÇO başlıkları büyük ölçüde tek kaynağa (stockanalysis) dayanıyor -> "(güven düşük)" işareti; sonraki yenilemede 10-Q ile ikinci kaynak.
- 16.11 21:20 | SITM ECL VRT | A10 inorganik büyüme: SITM puanı (5) rapor edilen +%257'ye dayanıyordu; organik +%156 (tek kaynak) ile de 5 kalıyor ama gerekçe organik rakama çevrilecek. VRT organik +%55 ile 5 doğru. ECL organik %7 ile 3 doğru.
- 16.11 21:20 | DOCN | eski /35 formatı -> /50 yenilemesi sırada.
- 16.11 21:40 | TSM | A3 eski yıl: Stocktwits sonucu (marj %59,5, Q4 32-33 Mr$) 2024 verisiydi -> kullanılmadı.
- 16.11 22:05 | KALİBRASYON | büyüme puanı için sektör içi çapa yok (yarı iletken akran medyan büyümesi) -> sonraki karnelerde akran medyanı yazılacak (A8'in uygulaması).
- 16.11 22:00 | haber taraması | Diamondback/Double Eagle (2025 anlaşması 2026 diye görünüyor) ve Telus teklifi yıl/rakam karışıklığı -> A3 tweet taramasında da geçerli, atılmadı.

E) GELİŞTİRME DÖNGÜSÜ
- Her turda karneden sonra "bu karnede hangi varsayım en çok sonucu değiştirdi?" sorusu sorulur, cevap karnenin DENETİM satırına yazılır.
- Haftada bir (Pazar) 14i-A listesi gözden geçirilir: hiç tetiklenmeyen madde de kalır; yeni hata türleri eklenir; Enes'e "karne sisteminde bu hafta düzelttiklerim" diye kısa özet gönderilir.
- Enes bir puana itiraz ederse itiraz 14i-D'ye yazılır ve aynı türden hata diğer karnelerde de aranır.
Bu bölüm devir notu yeniden yazılırsa aynen korunur.

## 14e. 16.11 YAPILAN ÇALIŞMALAR (referans/örnek)
- 13:52 kripto düşüş tweeti (COIN/MSTR, sondakika), 14:08 NVO CagriSema tweeti (editoryal) — otomatik turlar, Buffer.
- 14:15 RKLB TEKNİK DENEME: ta2 -v 21x4. 1s 5/6/12, 4s 8/3/12, G 7/7/9, H 4/8/11 (yukarı/aşağı/nötr). Gerekçe: günlük CHoCH yukarı 61,13; G+4s Supertrend AL (50,6 / 55,6); MACD +; OBV uyumlu; fiyat Fib OTE 43,9-66,8 içinde; haftalık bull FVG 55,3-59,8 + 4s bull FVG 59,4-59,6 çakışması. Ben olsam: 1. kademe ~59,5, 2. kademe 53-55 (günlük bull FVG 53,1-55,0 + VWAP 20g ~55,3), azalt <50,6 günlük kapanış, tez biter <43,9; hedef 63,5 (POC) ve 68-71 (son tepe + EMA 200). Görseller g/ta/20261116_1405_rklb_tradingview.jpg, 1415_rklb_teknik.jpg.
- 14:25 DOCN TEKNİK DENEME: ta2 -v + TradingView (Supertrend+SMC 1s/4s/G/H, RSI+MACD G; ctrl+z ile geri, ctrl+s). 1s 9/4/10, 4s 5/9/9, G 3/13/7, H 3/12/8. TV 4s Supertrend AL 73,3 (ta2 92,3 SAT; TV esas). Gerekçe: G/4s/1s OBV pozitif uyumsuzluk, TV RSI 41,7 ortalamasını yukarı kesti, MACD sıfır altı yukarı kesişim, fiyat OTE içinde. Ben olsam: 1. kademe 79-84 (G bull FVG 79,2-84,3 + 1s Supertrend 83,5 + 1s bulut 78,9-81,8), 2. kademe 70-73 (son dip 69,8 + haftalık EMA 200 70,0 + TV 4s Supertrend 73,3), tez biter haftalık kapanış <69,8; direnç 93,8-97,3 (G bear FVG), 102,2 (G Supertrend). Görseller g/ta/20261116_1420_docn_*.jpg, 1425_docn_teknik.jpg.
- Grafik çizim kodu: bu iki görselin matplotlib kodu (koyu tema, sağda gerekçeli seviye etiketleri, altta RSI/MACD/OBV) yeni görseller için şablondur -> invest/ta_grafik.py.
- TradingView rotasyon yöntemi: legend'e tıkla + Delete ile göstergeyi kaldır; Indicators (üst menü) -> ara -> yerleşik göstergeyi tıkla; ekran görüntüsü; ctrl+z ile tüm değişiklikleri geri al (özel ayarlar korunur); ctrl+s. URL'de interval=60/240/D/W ile dilim değişir; yüklenmesi için 8-10 sn bekle.

## 14f. DEVİR NOTU YENİDEN YAZILIRKEN (16.11 14:15, Enes: "farklı sohbete geçerken hiçbir eksik olmaması lazım")
- Enes "devir notu yaz" deyince: bu dosya (DEVIR_TAM.md) TEMEL alınır, hiçbir bölüm silinmez/kısaltılmaz. Yeni oturumda gelen her Enes mesajı ilgili bölüme işlenir, eski hâli "(eski: ...)" diye korunur, bölüm 18 kontrol listesine saat + özet + bölüm olarak eklenir.
- Baştaki KESİN KURALLAR bloğu (1-5 ve sonradan eklenenler) aynen taşınır.
- Güncellenecekler: tarih/sürüm satırı, portföy (bölüm 1), son 3 düzen + ticker saatleri (B ve 7), bekleyen görevler ve ID'leri (16), takvim (15), son tarama referansı (14), yapılan çalışmalar (14e'ye yeni gün).
- Yazınca: commit + push, sonra temiz klasöre `git clone --depth 1` ile çekip anahtar başlıklar grep ile doğrulanır (A6/A7, KESİN KURALLAR, 13, 14b, 14c, 14d, 14e, 14f, 14g, temel_karne.md). Eski oturum kendi bekleyen görevlerini (otomatik tur + teknik kontroller) siler, DURDUR yazmaz.
- Bilgi: Buffer planında aylık ~1000 gönderi hakkı var (Enes 16.11); teknik analiz tweetlerini Enes elle attığı için bu hak harcanmaz. 18:00/23:30 teknik kontrol görevleri Enes'in bilgisayarına bağlı kurulabiliyor (DESKTOP-Q39CPIE); bilgisayar/uygulama kapalıysa çalışmayabilir, Enes'e söylenir.

## 15. TAKVİM (16-19 Kasım 2026, TSİ)
- Pzt 16.11:
  - Tyson (TSN) Q4 açılış öncesi. Konsensus EPS kaynağa göre 0,53-0,61$, gelir ~14,1 Mr$. Çağrı 17:00 TSİ. Tyson IR (Chrome ile, 15:30): 24.09 duyurusu -> sonuçlar 16.11 açılış öncesi, çağrı 9:00 ET (17:00 TSİ). 15:30'da IR listesinde Q4 bülteni henüz yoktu. Rakamlar 14:08'de de henüz yoktu (bulunanlar 2025 ve Q3 2026); 2026 Q4 olduğunu doğrula. Konsensus Zacks 0,65$ / Talk Business 0,59$ (kaynaklar farklı).
  - Baidu Q3 açıklandı ve 13:33'te tweetlendi.
  - Warsh konuşması 20:00 TSİ. ABD açılışı 17:30 TSİ.
- Sal 17.11: HD açılış öncesi; NVDA kapanış sonrası (rakamlar ~00:20 TSİ Çarşamba). Gece istisnası turu için Enes onayı bekleniyor.
- Çar 18.11: TGT; FOMC toplantı notları 22:00 TSİ; PANW kapanış sonrası.
- Per 19.11: WMT.
- Q3 13F son günü 16 Kasım 2026.

## 16. DİĞER GÖREVLER / BEKLEYENLER
- "EnesInvestUS günlük portföy sorusu" (trig_019TTCnsx74Nsi9DjkY7M5MF): 16.11 13:54 Enes isteğiyle DURDURULDU (portföy tweetini Enes atar).
- Saatlik hazırlık ve Buffer taslak görevleri KAPALI.
- AKTİF ZİNCİRLER (bu oturum session_01EmZ47ojykRADiBmC9CvV5D, 16.11 14:25): "Otomatik paylaşım turu" (20-40 dk, her tur yeni ID), "Teknik kontrol (açılış +30 dk)" 18:00 TSİ ve "Teknik kontrol (kapanış -30 dk)" 23:30 TSİ (her gün yeni ID; ikisi Enes'in bilgisayarına bağlı). Yeni oturum list_triggers ile bu ADLARLA bulur, eski oturumunkileri siler (delete_trigger), kendisi yeniden kurar.
- Enes'ten cevap beklenenler:
  - Anthropic adı yasağı gevşesin mi?
  - Portföy ağırlıkları (eşit ağırlık dedi).
  - Resmi CBRS logosu (opsiyonel).
  - NVDA gece turu istisnası.
  - Twelve Data bağlantısı.


### 16-G. KURULU GÖREVLER (17.11 13:05, oturum session_01JKiyuk5Mhinmn4mL9usBPz; kural 15)
SABİT (HESAP=A önekli, 17.11 13:22; tekrarlayan, create_trigger, her çalışmada YENİ oturum açar, oturumdan bağımsız; devirde SİLİNMEZ, list_triggers ile kontrol edilir):
- trig_01LCT69YkpVZvjjW6ueTGftC Teknik kontrol 18:00 (hafta içi) — CRON_TZ=Europe/Istanbul 0 18 * * 1-5
- trig_01Me3Zwdnufk6rkLKNmZ2YF5 Teknik kontrol 23:30 (hafta içi) — 30 23 * * 1-5
- trig_01BGRz55RsS87Nko3XpCmXRE Günlük key levels + başlıklar 10:30 (hafta içi) — 30 10 * * 1-5
- trig_01XKuwGwLJwQbLzfPfbdjAX8 Haftalık bilanço takvimi (Pazar 20:00)
- trig_017HiX433Vy7u15V1a6wfbec Haftalık performans raporu (Pazar 21:30)
- trig_01C56vPfmWMnsPMFTV6wU6CM Günlük sabah kontrolü 09:00 (her gün)
- trig_01X4fnNMsC1i6wo8kXaMLqmf 13F serisi başlangıcı 15 Şub/Ağu/Kas 09:05; trig_014UMzEahLeqQdKb27x5skDU 16 Mayıs 09:05
- ABD YAZ SAATİ (8 Mart 2027): 18:00 → 17:00, 23:30 → 23:00 update_trigger ile alınmalı; 1 Kasım 2027'de geri. Takvime not.
TEK SEFERLİK (send_later, bu oturuma bağlı; 17.11 13:22 hepsinin mesajı HESAP=A ile başlar): otomatik tur zinciri "Otomatik paylaşım turu"; 17.11 HD/DIS hazırlık trig_01YW1dvnhPHaepQNX1m7iDAb (13:06), HD yayın trig_01MK5kMeJds7kxMU1nWi3K2Z (13:58), DIS yayın trig_01C94A6fGMsZta4dKyugisDi (14:38), perakende hazırlık trig_01Be651ivjjZLkrvQL9B7SBF (15:40), perakende yayın trig_01FZ1JNJM1vSHxSTQ3hJkGR3 (16:28), NVDA hazırlık trig_01XxN54vuUHFc1Yrwv19Nw43 (23:25), NVDA yayın trig_01ABe9pTdGzwtJSxY5w6F3QS (00:18 18.11); key levels bugünkü tek çalışma trig_01W2NqTt7qy5d2A2JYR22oew (13:15).
DEVRE DIŞI (silme yetkisi verilmedi, enabled=false): eski send_later teknik kontroller trig_01E6RSbqVeQrZ6mLmDK23LTy (18:00) ve trig_01J57K2S12HQAYCp9LmtaLK6 (23:30) — sabit görevlerle çift olmasın diye.
NOT: Sabit görevler yeni oturumda add_repo(push) ister; o oturumda izin istenirse Enes onaylamalı.

- 17.11 13:40 (kural 19-21, eski oturumdan kuruldu): Haftalık özet Cumartesi 10:55 trig_01LRGPzzrcF327Pqe67n55Qa; Ayın özeti her ayın 1-7'si 10:55 (yalnız ilk ABD işlem günü çalışır) trig_01X3YVaH2z1Yv7RyptTiUKok; Pazar 20:00 takvim görevi (trig_01XKuwGwLJwQbLzfPfbdjAX8) güncellendi: + 'gelecek hafta' tweeti (kural 20) + DONGU arşivi (kural 18).

- 17.11 14:45 (kural 22): yeni sabit görevler ve ID'ler DURUM.md 'Sabit görevler' bölümünde.

## 17. KAYIT
- DONGU.md satır biçimi: `- HH:MM AUTO (TÜR): dosya.jpg - özet (kaynaklar; tek kaynak olup kullanılmayanlar) | Buffer id | düzen:...` ve gerekirse "SIRADAKİ: ...".
- Commit sonuna sistemin verdiği attribution satırları eklenir.
- Repo: enesuludg6-debug/kontra-gorsel → /home/claude/kontra-gorsel (invest/). Yeni oturumda: add_repo (push) → git clone --depth 1 → register_repo_root.
- 16.11 Buffer gönderileri (23, 14:08 itibarıyla): vadeli, sabah notu, PANW, INTC, ROK, Form 4, PLTR, ASTS, HOOD, ON, geri alım, NVDA Bessent, CBRS, MS küresel, Japonya GDP, GOOGL TPU Kuo, ulusal şampiyon (WSJ), SITM bilanço, NBIS açılış öncesi, BIDU bilanço, Enes'in elle attığı ekran tweeti (13:40), kripto düşüş COIN/MSTR (13:52), NVO CagriSema (14:08). Ticker saatleri: SITM 13:05, NBIS 13:20, BIDU 13:33, COIN/MSTR 13:52, NVO 14:08, NVDA 11:40.

## 18. KONTROL LİSTESİ — HER ENES MESAJI → BU DOSYADAKİ YERİ
(15.11 mesajları DEVIR.md ve DEVIR_OZET.md'de kayıtlı, burada özetlendi. 16.11 mesajlarının tamamı tek tek:)
| Saat (16.11) | Enes'in mesajı (özet) | Bölüm |
|---|---|---|
| 01:49 | Haberi X üreticilerinden önce bul, hız kaynakları | 4 |
| 01:52 | Turlar 5-20 dk rastgele | 2 |
| 01:53 | Gece sınırı yalnız bilinen açıklamada gevşer | 2 |
| 02:05 | Vadeli işlemler her gün atılır | 4 |
| 10:30-10:38 | Logolar daha da belirgin (1,8x) | 7 |
| 10:34 | İnce/keskin yazı (sonra iptal) | 7 |
| 11:12 | Turlar durmasın, otomatik devam | 2 |
| 11:21 | Öncelik son dakika/en yeni gelişme | 4 |
| 11:53 | İnce keskin yazıya gerek yok | 7 |
| 12:22 | Beğendiğim tweetlerin tarzı + yapıştırdığım konuyu hemen araştırıp at (Kuo/TPU) | 6, 8 |
| 12:47 | Portföyü yönet, ekle/çıkar fikri, son 2 gün grafikler, arada bir, beğenmediğini söyle | 11 |
| 12:48 | Ben yatırımcıyım | 0 |
| 12:49 | Portföy NBIS RKLB DOCN SITM AXON CBRS VRT, açılışta eşit ağırlık | 1 |
| 12:51 | Turlarda ara ara bakarsın | 11 |
| 13:07 | "Organik değil" gibi kusuru araştır, iyi mi kötü mü, rakamlar yanlış/çakma mı cevapla | 6 |
| 13:09 | TradingView bağlayacağım; her turda portföy + fırsat hisseleri, indikatörler, birlikte karar | 11, 12 |
| 13:11 | Alpha Vantage'a ne yazayım (API anahtarı) | 12 |
| 13:13 | Bağladım ama farklı sohbette açılıyor | 12 |
| 13:13 | Twelve Data sayfası açılmadı | 12 |
| 13:15 | Türkçe kullanıyorum, nereye ekleyeceğim (alan adı izni) | 12 |
| 13:16 | Yaptım (Yahoo izni) | 12 |
| 13:17 | Al-sat ve SMC indikatörlerine de ulaş; TradingView başka sohbete bağlandı | 12, 13 |
| 13:19 | Ekle (SMC) | 12 |
| 13:22 | Önceki göstergeleri kaldır, SMC ekle, araştır; gerekirse çıkar-ekle-tekrar | 12 |
| 13:25 | Hepsini kurallara ekle; her turda tweet + portföy + grafik; beğendiğin/beğenmediğin/ekleme/satma; TradingView yoksa diğer kaynaklar | 3, 11, 12 |
| 13:25 | Fırsat hissesi izleme listesinde olmak zorunda değil | 1 |
| 13:27 | 9 göstergeli zorunlu set (EMA200, VWAP, RSI14, MACD, ATR, VP, ADX, Fib, OBV) | 13 |
| 13:28 | 21 göstergenin hepsi + farklı zaman dilimleri + SMC kombinasyonu | 13 |
| 13:31 | "Ben olsam" diye konuş, kurala ekle | 14 |
| 13:32 | Amacım en dipleri bulmak, yatırımcıyım | 0, 14 |
| 13:47 (yeni sohbet) | Devir notunu yeni sohbete yükledi, A bölümünü uygula | A |
| 13:49 | Eski portföy görevini güncelle (başka oturuma bağlı olduğu için güncellenemedi, 13:54'te durduruldu) | 16 |
| 13:50 | Repoyu PUSH yetkisiyle ekle, Buffer otomatik paylaşım ve send_later zinciri onayı (A7 metni buradan) | A6, A7 |
| 13:54 | Portföy güncellemesi tweetlerini kaldır, onları ben atarım | 1, başlık |
| 13:55 | Günde 2 kez (açılış +30, kapanış -30) portföy + en iyi 3-4 hisse teknik kontrol, 'ben olsam' kararları | 14b, başlık |
| 15:15 | WebFetch onayı (ir.tyson.com) | 3 |
| 15:29 | Haberleri istersen Chrome'dan araştır (açık) | 10 |
| 18:05 | Teknik analiz görsellerini kendin oluşturma, TradingView ekran görüntüsü at | başlık 5b, 14b, 14d |
| 18:09 | Sırayla at: ekran görüntüsü, tweet, ekran görüntüsü, tweet (tek tek toplu değil) | başlık 5d |
| 18:14 | Neden temelleri yapmadın, turlarda vaktin vardı; çözüm bul, devir notuna ekle, hiçbir şey çıkarma, sürekli kontrol et | başlık 3b, 14c-E, 14g, B, temel_karne.md |
| 02:31 (17.11) | 13F'ler açıklandı: her kişi için ayrı, değişiklikler + görüş tweeti; sonraki çeyreklerde sormadan kendin paylaş; devir + kurallara ekle | başlık 10, takvim |
| 11:10 (17.11) | Teknik analizde Nasdaq'a da bak → Nasdaq 100 endeksi her teknik kontrolde ilk mesaj + hisselerde endeks kıyası | kesin kural 12 |
| 13:28 (17.11) | Kullanım tasarrufu (DURUM.md, kısa okuma, kısa şablon, arşiv, ölçüm), haftalık özet, Pazar gelecek hafta tweeti, düzeltme kuralı, ayın özeti | kesin kural 18-21, DURUM.md, HATA_GUNLUGU.md |
| 13:11 (17.11) | Hakkım bitince arkadaşımın hesabından devam; tek seferde kopyalanacak eksiksiz kurulum, olası sorunlar | kesin kural 17, AKTIF_HESAP.md, HESAP_DEVRI.md, skills/ |
| 12:58 (17.11) | Bilanço rakam tweetinde şirket bülteni tek başına yeterli; ikinci kaynak teyidi yayından sonra 10 dk içinde | kesin kural 16 kaynak istisnası |
| 12:54 (17.11) | Performans raporu (hangi tweet işe yarıyor), sabit saatli görevler, haftalık bilanço takvimi + geç kalmama (hız protokolü) | kesin kural 14-16, performans.md, takvim.md |
| 12:39 (17.11) | Devir: yeni sohbete geçiş; skill'ler kaydedildi (enes-tweet-turu, enes-bilanco-13f, enes-portfoy-analiz) | v8 özeti, A7 |
| 12:12-12:22 (17.11) | Düşüş sebepleri tek uzun tweet; NVDA bilanço önizlemesi (profesyonel tahminci gibi) atıldı | enes-bilanco-13f |
| 10:40 (17.11) | "Benim okumam:" gibi etiketli görüş girişlerini kaldır, kurala ekle (yapay zekâ gibi duruyor) | kesin kural 11, yasak kalıplar |
| 23:48 | NBIS YOK | 1 |
| 23:44 | Portföy güncellemesi tweetini bu kez benden istedi: başlık 'PORTFÖY GÜNCELLEMESİ', altında 'YTD %53.36 / Günlük değişim -%5.19', hisseler alt alta; tutar ve ağırlık YOK. Atıldı. Portföy: DOCN RKLB SITM AXON CBRS VRT AVGO | 1 |
| 22:48 | Tweet sınırını kaldır; TradingView'a bağlanıp analiz yapabiliyor musun kontrol et (yapıldı: RKLB 4s Supertrend 55,90 okundu) | başlık 9, 2, A6, B |
| 22:44 | Başkasının NVDA/CEO tweetini yapıştırdı: 'olaya hakim, bağ kurmuş, bunun gibi at, bu tarz tweetleri çok sevdiğimi not al' | 6, ORNEKLER 18 |
| 21:59 | Warsh 'AI boom başarısız olursa' haberi: tweet + çok detaylı araştırma, her olasılık, ilgili olaylar | 4, 8 (thread + rapor) |
| 21:43 | Ekran görüntüsünü ben alırım; sen hangi hisse, hangi dilim, hangi göstergeler açık olacak onu söyle, tweeti ve düşüncelerini yaz (kıyas, ekleme/azaltma bölgeleri) | başlık 5f, 14b, 14d |
| 21:41 | Ekran görüntüsü sadece Supertrend+SMC açıkken değil, karar için en etkili göstergeler açıkken alınsın | başlık 5e, 14b, 14d |
| 21:34 | TradingView hesabı fark etmez; Adsız düzene Supertrend + SMC kur | 12 |
| 21:16 | Temel analizde yanlış/adaletsiz sonuç nasıl çıkar düşün, ne eklenebilir düşün, sürekli geliştir; devir notuna ekle | başlık 3d, 14i, B-EK2 |
| 20:09 | Otomatik çalışmaya başla (bu akşam günlük sayım yalnız Buffer kaynaklı) | 2 |
| 20:00 | Yeni oturuma devir, A7 onayı (push, Buffer, send_later) | A, A7 |
| 18:19 | Daha da geliştir, çok daha fazla metrik, profesyonel borsacı gibi detay; devir notuna ekle, hiçbir şey çıkarma, kanıt ver | başlık 3c, 14h, B-EK |
| 16:46 | Artık 20-40 dk'da bir at; benim attıklarımı hemen at ama senin zamanlamanı etkilemesin; devir notuna ekle, hiçbir kuralı atlama, tekrar tekrar kontrol et | 2, B, başlık 8 |
| 16:36 | Tweet aralıklarını 7'şer dk arttır (5-20 -> 12-27 dk) | 2, B |
| 16:33 | $CRWV bilanço formatı: bilançolar bu sayfa düzeninde yazılacak; sayfa stiline uyan hissede 15 dk sonra kapsamlı analiz; devir notuna ekle ve bana tekrar at | 4, başlık 7 |
| 15:45 | Raymond James/SPCX yapıştırdı (hemen atıldı) | 4, 8 |
| 15:39 | Uber/Zoox tweeti yapıştırdı (hemen araştırılıp atıldı) | 4, 8 |
| 15:42 | Citi/NBIS hedef indirimi yapıştırdı; attığım tweetlerden hangi sitelere bakacağını ve ne kadar tweet atacağını öğren | 4, başlık 6 |
| 15:31 | Her haber için en iyi ve kapsamlı hangi araçsa onu kullan | 10 |
| 14:19 | Farklı sohbete geçiş için eksiksiz devir notu yaz (v4); şimdilik bu sohbetten otomatik devam | 14f, 16, 19 |
| 14:15 | Hepsini eklediğini kontrol et, yeni devir notunda bu kurallar eksiksiz olsun | 14f, A6, A7 |
| 14:15 | Tüm çalışmaları ve kuralları ekle; kademelerin nedenini yaz; 18:00/23:30'da bakılan her hisse için ayrı görsel + tweet bana gönder, teknik analizi ben paylaşırım (Buffer 1000/ay) | 14d, 14e, başlık |
| 14:07 | Teknik analiz tweetinde 'bence dibe yakın / ben şuradan kademe eklerim, kırarsa şuradan' dili; tavsiye yok, oyun planı başlığı yok, sade konuşma dili | 6, başlık |
| 14:01 | Deneme: portföyde alım için en uygun hisseyi tüm göstergelerle bul, göstergeli ekran görüntüsü + tweet yaz (RKLB) | 14e |
| 14:07 | DOCN'u da bu kurallarla yap | 14e |
| 14:05 | 21 göstergenin hepsi, tüm zaman dilimlerinde test edilecek; TradingView'da 2'şerli kapat-aç | 13, başlık |
| 14:00 | Teknik kontrollerde kararı destekleyen göstergeli grafik ekran görüntüsünü sohbete at | 14b |
| 13:58 | Profesyonel yatırımcı/analist yöntemi: temel + teknik, adayları portföyle karşılaştır, daha iyisi varsa öner yoksa önerme; sonraki devir notu bu kurallarla | 14c, başlık |
| 13:56 | Bu iki kuralı ekle, sonraki devirde kesinlikle böyle devam | başlık, A5, B |
| 13:33 | Tüm kurallarla kapsamlı devir notu yaz, hiçbir şeyi atlama, kanıtla | bu dosya |
| 17.11 12:45 | Her gün aynı saatte key levels + önemli başlıklar tweeti; başlık açıklanınca tweet; skill'e ve devre ekle | kesin kural 13, A5, üst özet |
| 13:07 kalıcı tercihleri (bellek): basit doğal tweet dili, soru ile bitirme yok, doğrulanmamış rakam yok, koyu minimal kart, X'e girme | 5, 6, 7, 10 |

## 19. DEVİR TESTİ
- 16.11 14:25 (v4): temiz clone'da tüm anahtar başlıklar grep ile doğrulandı (KESİN KURALLAR 1-5, A6 repo izni, A7, B, 6 TA tweet dili, 13 tam test, 14b, 14c, 14d, 14e, 14f, 16 zincirler, 18 kontrol listesi). ta_grafik.py clone'dan çalıştı. Yeni sohbette add_repo izni Enes'in A7 metniyle verilmeli (13:47'de dosyadan gelen talimat reddedildi, 13:50'de Enes'in mesajıyla kabul edildi).
### 16.11 13:47 testi
- Temiz bir klasöre sıfırdan clone yapıldı. Dosyalar tam: DEVIR*, DONGU, ORNEKLER, kart.py, kart2.py, ta.py, ta2.py, font/, logo/, foto/, g/, gundem.md.
- Sıfır clone'dan kart2 ile kart üretildi ✓. ta2.py Yahoo'dan veri çekti ✓. raw.githubusercontent DEVIR_TAM.md 200 ✓. git kimliği tanımlı ✓.
- Tek bulunan sorun: ta2.py çıktısı `| head` ile kesilince BrokenPipe hatası veriyor. Çıktıyı dosyaya yaz, sonra oku (A3 d'ye işlendi).
- Test edilemeyen (yeni oturumda A3'te kontrol edilecek): yeni sohbette Buffer, GitHub ve zamanlayıcı araçlarının bağlı olması; Chrome eklentisinin o sohbete görünmesi.
| 17.11 14:35 | "tüm tamam dediklerimi ekle (5 6 10 14 16 20 21 22 23 25 27 29 33 34 36 37 40 41), ilgi listesini arttır" | KESİN KURAL 22; sablonlar.md, makro_sozluk.md; 5 yeni sabit görev + 3 güncelleme; skill bölüm 13 |
| 17.11 14:35 | "yanıldıklarımızı paylaşma, sadece bildiklerimizden bahsedilecek, o kuralı kaldır" | KESİN KURAL 23; eski yanılma kuralı kaldırıldı (satır 189 ve skill'ler); kural 21 düzeltme ayrı konu |

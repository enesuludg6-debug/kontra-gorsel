# KURAL DİZİNİ — her turun okuduğu TEK kural listesi (Enes 23.11 20:47: kredi tasarrufu, "hiçbir yeteneği de atlamanı istemiyorum")

Bu dosya kural 1-63'ün GÜNCEL hâlinin kısa listesidir; hiçbir kural silinmedi. Tam metinler: `KURALLAR_TAM.md` (DURUM'dan taşınan bütün kural blokları, kelimesi kelimesine), `skills/*.md`, `DEVIR_TAM.md`. Bir konuda ayrıntı gerekirse YALNIZ o kuralı grep ile aç (`grep -n "KURAL 58" KURALLAR_TAM.md`); dosyaları baştan okuma. Çelişkide numarası BÜYÜK (yeni) kural geçerli; bugünlük kural (DURUM.md başı) hepsinin önünde.

## A. Kilit, sayaç, zamanlama
- 17 Hesap kilidi: görev mesajındaki HESAP=X, AKTIF_HESAP.md'deki `AKTIF:` ile aynı değilse hiçbir şey yapma, görevi kapat. `bash invest/tur_basi.sh <etiket>` çıkış 2/3 → dur. DONGU'da tek başına `DURDUR` → dur.
- 29 Her şey bu sohbete (SendUserMessage/SendUserFile); sabit görevler send_later zinciri (`sonraki.py`), her çalışma İLK İŞ sonrakini kurar, aynı adlı bekleyen varsa kurmaz.
- 42/48/48-B/53 Tweet penceresi 11:00-02:00 TSİ. Pzt-Cuma en az 30 en çok 50, Cumartesi en çok 20, Pazar en çok 10 (hafta sonu alt sınır yok). Saat dilimi sınırı YOK. Turlar 15-25 dk arayla, turda 1-2 tweet. BUGÜNLÜK KURAL varsa o geçerli.
- 43 İş defteri `isler.py` tek kaynak (ekle/durum/devir); iptal yalnız Enes'in aynen sözüyle, en dar kapsam.
- 44 18:00 (temel1800) ve 23:30 (teknik2330) analiz görevleri YOK.
- 24 Periyotlu işler `periyot.py durum/kontrol/yap` ile; hafızadan tahmin yok.
- 18/28 Tasarruf: tur başı `tur_basi.sh`, kart `yayinla_gorsel.sh`, kayıt `kayit.py`. Sabah 09:00 kontrolü zincirleri doğrular, gece biten tur zincirini kurar.
- 14-16 Sabit görevler: sabah 09:00, perfogren 10:15, key levels 11:00, radar 14:20, haftalık özet Cmt 10:55, sektör Cmt 13:25, ilgi sıralama Cmt 16:25, analist Paz 12:25, sezon karnesi Paz 14:25, takvim Paz 20:00, performans Paz 21:30, ayın özeti ayın 1-7'si 10:55, 13F Şub/May/Ağu/Kas 15. İçerik `gorevler/<anahtar>.md`.

## B. Konu seçimi
- 46 KONU FİLTRESİ: yalnız yapay zekâ (çip, bellek, ağ, bulut/neocloud, veri merkezi enerjisi, YZ yazılımı/siber güvenlik), uzay, Nasdaq/büyük teknoloji + bunları etkileyen makro. Perakende, banka, sanayi, ilaç, enerji/emtia YOK.
- 55 YZ ile ilgili her hisse konu olabilir; hafta içi tur "haber yok" diye boş geçmez (YZ evreninde tara). 3 saat ticker kuralı yalnız aynı bilginin tekrarını engeller.
- 57 İÇERİK AYARI (DURUM.md): portföy hissesinde gelişme varsa turun ilk tweeti o; son dakika öncelikli; ayrı detay/çağrı tweeti az; görüşlü analiz 21:00-01:00.
- 48 Her turda ilk iş son dakika taraması (newsquawk + WebSearch, portföy ve listeler).
- 58 Fikir taraması: 10:15 görevi + 21:00-23:00 arası ilk tur; Chrome yoksa Chrome adımı atlanır; Reddit Chrome'da engelli, dolanılmaz; fikir tweeti hafta içi günde 3-10 (hafta sonu alt sınır yok), DONGU "FIKIR-TWEET n/10"; YZ'yi toptan kötüleyen fikir elenir.
- 22/22a-r İçerik türleri: içeriden alım (Form 4, kod P anlamlı), analist notu, sektör, ilgi listesi, sezon karnesi, ayın özeti, mevsimsellik, takvim, lansmanlar. 19-20 haftalık özet ve "gelecek hafta" tweeti.
- 10/13F: çeyreklik seri, yalnız teknoloji hamleleri, "30 Eylül itibarıyla" uyarısı, 13F günde en çok 1 (21-24).
- 13 Key levels = seviyesiz "günün başlıkları" (kural 37 sonrası).
- 37/38 Claude TEKNİK ANALİZ YAPMAZ ve teknik tweet atmaz; Enes teknik analiz atarsa yalnız sade, mecazsız taslak yazılıp Enes'e yollanır (30-31, 33-35 teknik kuralları bu yüzden yalnız Enes'in taslakları için).
- 39-41/45/49 Bilanço: önce konsensüs beklenti tweeti (49, açıklamadan 30-60 dk önce); opsiyon beklenen hareketi en az bir tweette (39); RAKAM tweeti yorumsuz ve hızlı (10 dk), 15 dk sonra yorumlu ANALIZ (45: detaylı, çok kaynaklı); görüşme ve detay tweetleri 40-41; KURAL 67 (Enes 24.11 09:47): bilanço başına EN FAZLA 6 tweet (beklenti, opsiyon, rakam, analiz, detay, çağrı, beklenen hareket HEPSİ dahil; 6 tavan, hedef değil — zayıf detay/çağrı tweeti sayı doldurmak için atılmaz); 51 dönem = takvim + mali yıl birlikte.
- Anthropic adı/konusu ASLA. x.com'a girilmez. Enes'in kendi attığı konu tekrar edilmez (Buffer son gönderiler).

## C. Doğrulama
- 3/16 Her rakam ve yan iddia 2 BAĞIMSIZ kaynak (aynı haberin kopyası sayılmaz). Tek istisna: bilanço rakam tweetinde şirket bülteni (10 dk içinde ikinci kaynak teyidi).
- 23/56-B Yalnız doğrulananlar ve TUTAN beklentiler yazılır; tutmayan tahmin hiç anılmaz.
- 66 SONUÇ TAKİBİ (Enes 24.11 09:44): olaydan önce ölçülebilir yorum (belirleyici kalem, eşik, "şu olursa şu demektir") içeren her tweet atıldığı an `isler.py ekle TEST-<T>-<GGAA> ... --tur sonuctakip` ile kaydedilir; olay açıklanınca o yorumu gerçek rakamla sınayan analiz tweeti atılır (hangi dal gerçekleşti + kendi hesabımız + sonuç cümlesi). Bilançoda bu ANALİZ tweetinin kendisidir (kural 57 sayısı artmaz); veri ve diğer olaylarda ayrı görev. Koşullu yorumda önceki nota tek cümle atıf serbest; tutmayan yön tahmini 56-B ile anılmaz. Ayrıntı `skills/enes-sonuc-takibi.md`.
- 21 Yanlış rakamda düzeltme tweeti.
- 56 Beklenti/seviye tweeti atılınca her madde için TAKIP işi açılır (yalnız tutanlar yazılır).
- Yıl/çeyrek karışmasına dikkat (2025/2026). Canlı fiyat Yahoo chart uç noktası.

## D. Yazım (her tweet)
- 11/11-B/52/54/54-B/54-C `yasak.py` her tweetten önce (çıkış 1 = atma): etiketli giriş ("Görüşüm:", "Not:", satır başı "X:"), "okuyorum/okumam", iki tarafı dengeleyen kalıplar, ruh hâli klişeleri, mecaz ve dramatik sahne, sunucu açılışları yasak.
- 54-D (Enes 23.11 22:06): veriye/manşete konuşma yükleyen kurgulu karşıtlık yasak ("Manşet X diyor; veri başka bir şey söylüyor", "rakamlar başka bir hikâye anlatıyor", "fısıldıyor"); yasak.py yakalar. Olgu düz cümleyle. Piyasanın ruh hâlini soyut kelimeyle özetlemek de yasak ("stres geçmiş değil", "panik bitti", "nefes aldı"); rakamın gösterdiğini düz söyle ("kısa vadeli oynaklık hâlâ uzun vadelinin üzerinde").
- 54-E (Enes 24.11 09:10): rakamsız "X tarafı da güçlü" hüküm cümleleri yasak ("Nakit tarafı da güçlü.", "Bilanço tarafı sağlam.", "Talep de güçlü görünüyor."); "X tarafı/cephesi/ayağı" kalıbı hiç yok, kalem doğrudan özne olur, hüküm rakamla verilir; yasak.py yakalar.
- 25/50 Her haber tweeti haber + YORUM; birinci tekil net görüş zorunlu (bilanço rakam tweeti hariç).
- 50-B `gorus.py kontrol/kaydet`: görüş açılışı ve kalıbı son tweetlerde tekrar etmez.
- 59 Görüş Enes'in profiliyle (ENES_GORUS_PROFILI.md): YZ altyapısına inanan, dip toplayan uzun vadeli yatırımcı; şirkete özgü sorunu YZ talebinden ayır; YZ'yi toptan kötüleme; kötü veriyi gizleme.
- 60 Profesyonel, kendinden emin ama uydurmasız üslup (örnekler taslak/uslup_60_ornekler.md).
- 61 ANALİZ KALİTESİ (skill enes-analiz-kalitesi): konuya özgü mercek, mekanizma, veri kartı (tarih, kapsam, gerçekleşen/beklenti ayrımı), tarihsel karşılaştırma yalnız 4 testten geçerse ve farkıyla (tweet başına en çok 1), boğa/ayı/baz her tweete konmaz, zorla bağlantı yok, gelecek için kesinlik yok. UZUNLUK TAVANI: SONDAKIKA/HABER 600, BAGLAM-GORUS/PORTFOY 800, EGITICI 900, DERIN-ANALIZ/BILANCO-ANALIZ/ÖZET 1200 (`kalite.py sinirlar`). Derinlik Enes mesajına taşınır.
- 62 Piyasa jargonu (fiyatlandı, iskonto, prim, denklem, çarpan, katalizör, pozisyonlanma, konsensüs, iştah, kâr satışı, belirsizlik, ayrışma): tweet başına en çok 1, son 6 tweette geçen kullanılmaz.
- 63 Derinlik, sade anlatım: konuya uygun BİR kalıp (A zincir, B o zaman/şimdi, C koşullu eşik, D piyasa değeri - net nakit [hedef fiyat DEĞİL], E tek kavram dersi, F hareketi normalleştirme); ham İngilizce opsiyon/fon jargonu yazılmaz; DERIN-ANALIZ günde en çok 2.
- 63-B (Enes 23.11 21:11 "etkisini göremiyorum"): HER tweet `kalite.py kontrol --tur <TÜR> --kalip <A-N>` ile; kalıbın izi metinde yoksa HATA; aynı kalıp üst üste 3 kez olmaz; en az 2 doğrulanmış rakam. Görünür farkın 5 işareti ve önce/sonra örneği: taslak/derinlik_63_ornekler.md (tweet yazmadan ÖNCE bak). Kendi hesabımız (kârın kaç katı, piyasa değeri - nakit, zirveden uzaklık, korunan pay) her tweette tercih edilir; iki noktalı etiket yine yasak (kural 11).
- 63-C (Enes 23.11 21:14) ek profesyonel kalıplar: G beklenti farkı, H birim ekonomisi (X başına), I nakit/sermaye izi, J değer zinciri (kimin harcaması kimin geliri), K tersine hesap (fiyatın haklı çıkması için ne gerekir; hedef fiyat değil), L akran kıyası (aynı ölçüyle), M tetikleyici takvimi (tarih + tek rakam), N kırılma noktası (tezi bozan şey ve mesafesi). Konu eşleştirmesi skill bölüm 8.
- 63-D (Enes 23.11 21:19 "14 kalıp = 14 tweette bir tekrar mı?"): kalıp cümle şablonu DEĞİL, analiz açısıdır. Birincil kalıp son 4 tweette tekrar etmez; iki kalıp birleştirilebilir (`--kalip D+J`, ikili son 12 tweette tekrar etmez); YAPI İMZASI (paragraf sayısı, kısa satır/düz yazı, uzunluk bandı, açılış türü) son 3 tweetten biriyle aynı olamaz. Biçimleri döndür: tek güçlü paragraf, kısa satırlı zincir, rakam satırları + tek hüküm, iki paragraf, uzun derin analiz.
- 64 KONUŞMA DİLİ (Enes 23.11 21:31: "bilançoda ilk bakacağım satır bu yazmaktan ziyade ben bilançolarda ilk bunu kontrol edeceğim mesela bu tarz şeyler daha konuşma diliyle oluyor"): Analiz derin olur ama cümleler Enes konuşuyormuş gibi kurulur. Kalıplaşmış analist/rapor cümleleri yasak (yasak.py): "bakacağım tek ...", "ilk bakacağım satır", "izlenecek (tek) kalem", "bakılacak tek kalem/rakam". Yerine öznesi "ben" olan doğal fiil: "Ben bilançoda ilk bunu kontrol edeceğim.", "Ben en çok ön ödemelerin ne olacağını merak ediyorum.", "Aralık'ta ilk bu rakama bakarım.", "Bu fark kapanırsa içim rahatlar." Her tweette aynı kapanış fiili kullanılmaz (kalite.py kapanış tekrarı). 63-B'deki "bakılacak tek kalem" işareti bu dille yazılır.
- 64-B (Enes 23.11 22:03 "ben en çok şunu takip edeceğim, benim için önemlisi, en yakından izleyeceğim bunları çok sık kullanıyorsun"): "takip edeceğim / izleyeceğim / merak ediyorum / benim için önemlisi / en yakından / ilk bakarım" ailesi tweet başına en çok 1 ve son 5 tweette geçtiyse kullanılmaz (kalite.py HATA). Tweet "ben şunu izleyeceğim" ile BİTMEZ; verinin vardığı SONUÇLA biter (ör. "Bu yapı düzelmeden yükselişe güvenmek erken."). 63-B'deki "bakılacak tek kalem" işareti ZORUNLU DEĞİL, 5 tweette en çok 1.
- 65 PROFESYONELLİK ÇITASI (Enes 23.11 22:03 "sana attığım tweet örnekleri senin yaptıklarından çok daha profesyonel, ben o derecede profesyonel şeyler istiyorum"): Fiyat yüzdesi + manşet + yorum = YETERSİZ. Her analiz tweetinde en az bir İKİNCİ KATMAN veri (kalite.py HATA): oynaklık yapısı (VIX 9 gün/1 ay/3 ay vade eğrisi, VVIX, SKEW, VXN — Yahoo ^VIX ^VIX9D ^VIX3M ^VVIX ^SKEW ^VXN), örtük korelasyon (^COR1M/^COR3M), piyasa genişliği, açığa satış oranı, marj borcu (FINRA), ETF/fon akışı, CFTC pozisyonları, analist tahmin revizyonları, şirket tablosundan derin kalem (ertelenmiş gelir, RPO, serbest nakit, yatırım harcaması/gelir, hisse sayısı, sipariş/satış), birleşme farkı, kâr/satış katı. Referans tweetlerde olan şey bu: manşeti değil, manşetin altındaki yapıyı anlatıyor. Yazım: kendinden emin, yoğun, dolgu cümlesi yok ("Bu da ... açıklıyor" gibi), sonuç cümlesiyle biter. Opsiyon pozisyonu (hangi seviyede kaç kontrat) yalnız 2 kaynakla yazılır; kaynak yoksa yazılmaz, onun yerine kamuya açık oynaklık ve akış verisi kullanılır. Örnek: taslak/derinlik_63_ornekler.md "KURAL 65 ÖRNEĞİ".
- `kalite.py kontrol --tur <TÜR>` (1 = atma, 2 = DONGU'ya gerekçe) ve atınca `kalite.py kaydet`. En çok 2 yeniden yazım, sonra konu değiştir.
- YASAK: al/sat tavsiyesi ve emir kipi, hedef fiyat, emoji, hashtag, @mention, link, soruyla bitirme, portföy tutarı/ağırlığı, "aldım/sattım" (Enes açıkça istemedikçe). "Bence" en fazla bir kez. Şirketi ilk geçtiği yerde ne iş yaptığıyla tanıt.

## E. Kart ve paylaşım
- `kart2.py`; son 3 turdaki düzen tekrar edilmez (DURUM "Son 3 düzen"). LOGO_BUYUT 1.8, küçültme YOK; logo `$TICKER` ile çıkar; dortlu/isi kartında logolu ticker rakama biniyor → logosuz isim; spotlight alt metni kısa; kaynak satırı kısa; "AI" değil "Yapay zekâ"; her kart Read ile kontrol edilir, kötü çıkarsa yeni dosya adıyla yeniden çizilir.
- Dosya `g/YYYYMMDD_HHMM_konu.jpg` → commit + push → raw URL 200 olmalı; main 404 ise commit SHA'lı raw URL. 200 yoksa görselsiz tweet atma.
- Paylaşmadan önce Buffer son gönderiler + DONGU son satır (son 20 dk aynı konu varsa atma). Buffer create_post: org 6af5719777bce44fa736607b, kanal 6af99a1aece6dfde5fd109c7, automatic, shareNow, görsel + Türkçe altText.
- ARALIK (Enes 23.11 21:29): bir turda 2 tweet varsa ikisi arka arkaya atılmaz. İlki shareNow, ikincisi Buffer `customScheduled` ile ~12 dk sonraya (dueAt +03:00); tweetler akışa eşit aralıkla düşer. Sonraki tur, zamanlanmış tweetin saatinden en az 10 dk sonra kurulur.
- 47 Her tweetten sonra Enes'e "Paylaşıldı (SS:DD): TÜR" + metin + öğretici "Ne anlama geliyor?" (3-6 madde; tweete girmeyen tek kaynaklı bilgiler dahil).
- 26 Kayıt: `kayit.py` (DONGU + performans) + `gorus.py kaydet` + `kalite.py kaydet`; dersler `ders_analiz.py` ile, DERSLER.md aktif dersler uygulanır.
- Portföy (DURUM.md) hissesinde teze dokunan gelişme varsa Enes'e kısa "ben olsam" notu (enes-portfoy-analiz).

## F. Ayrıntı nerede
- Tur akışı ayrıntısı: `skills/enes-tweet-turu.md` bölüm 1-7 (yalnız gereken bölüm).
- Bilanço/13F: `skills/enes-bilanco-13f.md`. Portföy/karne: `skills/enes-portfoy-analiz.md`.
- Kalite (61-63): `skills/enes-analiz-kalitesi.md`. Sonuç takibi (66): `skills/enes-sonuc-takibi.md`.
- Kuralların tam metni: `KURALLAR_TAM.md`; eski geçmiş: `DEVIR_TAM.md`.

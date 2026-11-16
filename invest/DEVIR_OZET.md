# ENESINVESTUS — GÜNCEL DEVİR NOTU (15.11.2026 21:05 TSİ)

> **16.11.2026 13:40: EN GÜNCEL VE TAM NOT invest/DEVIR_TAM.md. ÖNCE ONU OKU (çelişkide o geçerli).**

Bu dosya, 15.11.2026 boyunca Enes Uludağ'ın canlı sohbette verdiği tüm kararların temiz özetidir. invest/DEVIR.md'deki eski bölümlerle çelişirse BU DOSYA geçerlidir. Ayrıntılar için DEVIR.md'ye bak.

## 1. Hesap ve amaç
- X hesabı: @enes1050392, görünen ad "Enes Uludağ". Türkçe, ABD borsası odaklı.
- AMAÇ: en iyi getiri değil; GÜVEN sağlamak ve İYİ İÇERİK üretmek. Hedef okur borsayı az bilen biri: kısa, sade, anlaşılır.
- Portföy (15.11 16:55): $AXON $NBIS $RKLB $CBRS $DOCN $VRT $SPCX. Ağırlık/tutar ASLA yazılmaz. Enes'in ağzından "aldım/sattım/portföyüm" cümlesi kurulmaz.
- İlgi listesi: $ON $AAOI $HOOD $TEM $CRDO $PLTR $ISRG $ASTS $MU + büyük AI/yarı iletken/bulut/uzay şirketleri.

## 2. Paylaşım modu (son karar)
- OTOMATİK: Buffer `create_post`, channelId `6af99a1aece6dfde5fd109c7`, organizationId `6af5719777bce44fa736607b`, schedulingType `automatic`, mode `shareNow`, görselli.
- Aralık (Enes 16.11 01:52): her tur sonunda 5-20 dk arası RASTGELE (python random.randint(5,20)) `send_later` (zincir); son paylaşım 5 dk'dan yeniyse paylaşma. Gece 01:00-09:00 TSİ paylaşım yok (09:05'e kur); İSTİSNA (Enes 16.11 01:53): gece sınırı yalnız ÖNCEDEN BİLİNEN bir açıklama varsa gevşer (takvimdeki bilanço rakamı, veri, konuşma); o saat için ayrıca tur kurulur. Beklenmedik haber için gece tur kurulmaz, haber 09:05 turuna kalır. Günde en fazla 45 tweet (Enes 15.11 21:46; önceki 40) (Enes'in elle attıkları dahil, Buffer list_posts ile say).
- Durdurma: Enes "durdur" derse DONGU.md'ye satır başında tek başına `DURDUR` yaz, zinciri kurma.
- Her paylaşımdan sonra Enes'e SendUserMessage: paylaşılan metin + "Ne anlama geliyor?" öğretici bölüm.
- Enes'ten SADECE fotoğraf istenir (kişi haberi için). Başka soru sorulmaz.
- Not: X Original Content Rewards otomatik içeriği ödeme dışı tutabilir; Enes'e söylendi, Enes yine de otomatik istedi.

## 3. Enes tweet/görsel atarsa
- Başkasının tweetini/grafiğini atarsa: araştır, her rakamı doğrula, KENDİ cümlenle benzerini yaz, kendi kartını çiz (başkasının görselini kullanma). Tutmayan rakamı Enes'e söyle.
- "yorum yaz" derse: yanıt metni hazırla (Enes atar; otomatik yanıt YOK). İngilizce gönderiye istenirse İngilizcesini de ver.
- Gönderdiği her tweetin konsept/şeklini invest/ORNEKLER.md'ye şablon olarak ekle.
- Grafik ekran görüntüsü atarsa teknik analiz tweeti (DEVIR 5h). TradingView: sadece Claude in Chrome/masaüstü bağlıyken, sadece tradingview.com, X'e ASLA girme (DEVIR 5j).

## 4. İçerik kuralları
- TEKRAR YOK: daha önce atılan konu tekrar atılmaz (DONGU.md tamamı + Buffer son 50). Yeni gelişme varsa yeni açıyla olur.
- Aynı ticker 3 saatte bir. Her rakam 2 kaynakla; çelişirse kullanma ya da şirket rakamını kullan.
- ÖNCELİK SIRASI (Enes 16.11 11:21, EN ÖNEMLİ): HER TURDA ÖNCE SON DAKİKA/EN YENİ GELİŞME TARA (son 1-3 saat: WebSearch 'breaking', Reuters/Bloomberg/CNBC, şirket IR/8-K, Fed/veri, portföy+ilgi listesi haberleri, analist not değişikliği, yönetici alım/satım). Taze ve doğrulanmış bir gelişme varsa ONU at (aynı turda, hızlı). Yalnızca taze gelişme yoksa terim/analiz/eski bilanço içeriği at. Eski konulara (geçen haftanın bilançoları, terimler) dayanma alışkanlığı bırakılacak. Tur özetinde taranan taze kaynakları ve bulunan/bulunamayan gelişmeleri DONGU'ya yaz.
- ÖNCELİKLİ TÜRLER (artırılacak): son dakika · bu hafta ne var / yarın ne var · bilanço rakamları (YORUMSUZ) · bilanço analizi (YORUMLU, ayrı tur, 30-90 dk sonra) · İÇERİDEN ALIM-SATIM (günde 1-2; Form 4; alım > satım; 10b5-1/vergi satışını açıkça yaz).
- Diğer menü (DEVIR "İÇERİK MENÜSÜ"): sabah notu, premarket, açılış, kapanış, haftanın karnesi, makro beklenti→sonuç→etki, analist notları, geri alım/temettü, anlaşmalar, endeks girişleri, halka arz, kilometre taşı, CEO/Fed sözü, 13F, fon akışları, açığa satış, 1 yıl önce vs bugün, rakip karşılaştırma, sektör sıralaması, uzun dönem grafik, AI capex, emtia/tahvil/dolar, haftanın rakamı, terim sözlüğü, "bu şirket ne iş yapar", strateji, teknik analiz.
- Anthropic konusu otomatik atılmaz (çıkar çatışması).
- YASAK: al/sat/hedef fiyatım tavsiyesi, mention, link, hashtag kalabalığı, yanıt/beğeni/takip otomasyonu, emoji, soruyla bitirme, doğrulanmamış rakam, Chrome ile X'e girmek.

## 4b. HABER HIZI KAYNAKLARI (Enes 16.11 01:49; kural, haberi X içerik üreticilerinden önce bulmak için)
A) Takip/alarm kuralı: takip edilen şirketlerin resmi X hesapları + IR (yatırımcı ilişkileri) sayfaları (basın bülteni, 8-K, bilanço tarihi); Bloomberg / Reuters / FT takibi veya alarmı; ekonomik takvim kullanımı. (X hesaplarına Claude girmez; yalnız Enes'in takibi. IR sayfaları ve haber siteleri WebSearch/WebFetch ile taranır.)
B) Hızlı kaynak listesi (her turda önce bunlara bak, sırayla):
- Birincil/en hızlı: SEC EDGAR (8-K, Form 4, 13F, 6-K; sec.gov/cgi-bin/browse-edgar RSS "latest filings"), şirket IR basın bültenleri, PR Newswire / Business Wire / GlobeNewswire / Accesswire (bülten dakikalar içinde burada).
- Resmi veri: Fed (federalreserve.gov), BLS (TÜFE/PPI/istihbarat), BEA, Treasury, Census; ekonomik takvim: Investing.com, TradingEconomics, Forex Factory, MarketWatch, Econoday.
- Bilanço takvimi/rakam: Earnings Whispers, Nasdaq earnings calendar, Yahoo Finance calendar, Zacks, StockAnalysis, TheStreet.
- Haber ajansları: Reuters, Bloomberg, AP, CNBC, Dow Jones/WSJ, FT, Barron's, MarketWatch, Benzinga, Investing.com, Seeking Alpha news, Yahoo Finance, TipRanks, Stocktwits news, Finviz news, TradingView news.
- İçeriden/kurum: OpenInsider, SEC Form 4 canlı, Quiver Quantitative, Capitol Trades, WhaleWisdom/HedgeFollow/Dataroma (13F), Unusual Whales.
- Piyasa hareketi/premarket: Finviz, Chartmill premarket movers, TradingView screener, Stocktwits trending, Benzinga premarket.
- Sektör/derin: Semianalysis, The Information, Nikkei/DigiTimes/TrendForce (Asya çip haberi), Axios, Techmeme, The Verge, SpaceNews (uzay), Fierce (telekom), analist notları (Barron's, Investing.com analist).
- Sosyal sinyal (doğrulamadan KULLANMA): X'te şirket/CEO hesapları, Walter Bloomberg, DeItaone, Unusual Whales, FirstSquawk gibi hızlı haber hesapları; her haber 2 güvenilir kaynakla doğrulanmadan atılmaz.
C) Uygulama: her turda önce (1) SEC/IR/bülten, (2) Reuters/CNBC/Bloomberg/Benzinga son dakika, (3) takvim, sonra (4) menü. Kaynak çelişirse atma. Hız için: son dakika ve bilanço rakamı en önce, analiz 30-90 dk sonra.

## 4c. VADELİ İŞLEMLER (FUTURES) HEP ATILIR (Enes 16.11 02:05)
- Her işlem günü vadeli endeks tweeti atılır: sabah 09:05 turunda (Dow, S&P 500, Nasdaq 100, Russell 2000 vadelileri, önceki kapanışa göre %) ve ABD açılışından önce (~15:00-15:25 TSİ) güncel durumla tekrar. Önemli sürprizde (örn. %1+ hareket) ek tweet.
- Pazar akşamı vadeliler açılınca (~02:00 TSİ Pzt) Enes ekran görüntüsü atarsa o rakamlarla at; yoksa 2 kaynakla doğrula.
- Düzen: kart2.isi(kolon=2, hane=2, etiket="VADELİ İŞLEMLER"); yüzde 2 basamak. Kapanışa göre değişim yazılır; vadeli = "açılışı gösteren işaret", garanti değil.

## 5. Yazım stili
- Arkadaşına anlatır gibi, kısa cümle, 2-4 cümle, en fazla 2-3 rakam. Şirketi ilk geçtiği yerde ne iş yaptığıyla tanıt. Terimleri sadeleştir.
- Her tweette tek cümle görüş (bilanço rakam tweeti hariç) ama "bence", "gösteriyor bana", "düşünüyorum" TEKRAR ETMESİN; kapanışları çeşitlendir (düz tespit, kısa yargı, karşıtlık, takip, yorumu başa koyma).
- Yasak kalıplar: "Benim görüşüm:", "Sonuç olarak", "dikkat çekiyor", "kritik", "nabız", "mercek altında" vb.

## 6. Görseller
- Kod: invest/kart2.py (yeni), kart.py (eski/yedek). Fontlar invest/font (Inter Display + Instrument Serif + JetBrains Mono).
- Enes'in seçtiği/beğendiği düzenler (K-Z, ÖNCE BUNLAR): bento, halka, isi, takvim, cizgi, panel, uclu, soz, editoryal, skor, zaman, ilerleme, dilim, dortlu, manset. Yedek A-J: spotlight, split, terminal, sondakika, once_sonra, kapak, cam, poster, siralama, grafik2.
- KALDIRILDI (Enes 15.11 21:23 "kaba, beğenmedim"): versus (çapraz renkli iki taraf). Yerine kart2.panel (koyu, serif başlık, mono etiket, ince çizgili tablo, altın çubuk). Benzer kaba/renkli blok tarzından kaçın; sade ve profesyonel.
- Tür → düzen: bilanço rakam = skor/terminal; analiz = bento/uclu/panel; iki hisse karşılaştırma = panel; takvim = takvim; kapanış = isi/dortlu; son dakika = sondakika/manset; içeriden = uclu/skor; kişi = manset/soz (Enes fotosu).
- Logolar büyük ve belirgin (küçültme). Enes 16.11 10:30: "logolar daha da belirgin olmalı" -> kart2.LOGO_BUYUT=1.8 (10:32 "daha da belirgin": önce 1,4 sonra 1,8; tüm düzenlerde logo 1,8 kat); yeni düzen/render'da logoyu bundan küçük yapma, gerekirse daha da büyüt. Son 3 turda kullanılan düzen tekrar edilmez. Read ile kontrol; taşma varsa YENİ dosya adıyla düzelt (raw URL önbelleği). Örnekler: invest/g/ornek/.
- YAZI TİPİ (Enes 16.11 10:34): kaba/kalın yazı değil, daha İNCE ve KESKİN yazı sever. kart2.sans() artık Black/ExtraBold/Bold/SemiBold isteklerini Inter Display Medium'a çevirir (INCE sözlüğü; eldeki en ince ağırlık Medium). Başlıkta ince serif (Instrument Serif) tercih edilir; yeni düzende de kalın ağırlık kullanma. Render'da taşma/satır kırılması değişebilir, Read ile kontrol et. Örnek: g/ornek/ince_*.jpg (henüz çizilmedi, ilk fırsatta çiz).
- Kart dosyası: invest/g/YYYYMMDD_HHMM_konu.jpg → commit + push → raw URL 200 kontrol → Buffer.

## 7. Diğer görevler
- "EnesInvestUS günlük portföy sorusu" (trig_019TTCnsx74Nsi9DjkY7M5MF): Pzt gece 00:05 TSİ; talimatı eski (sohbet modu, eski portföy listesi) — çalıştığında bu dosyayı esas al.
- Saatlik hazırlık ve Buffer taslak görevleri KAPALI.

## 8. Kayıt
- Her işlem invest/DONGU.md'ye: `- HH:MM AUTO: dosya.jpg - özet (kaynaklar) | TÜR | düzen:...`. Commit sonuna sistemin verdiği attribution satırları.

- YAZI TİPİ KURALI İPTAL (Enes 16.11 11:53): ince/keskin yazı gerekmiyor, normal ağırlıklar kullanılır; tur mesajındaki "ince yazı" ifadesini yok say. Logo büyüklüğü (1,8x) geçerli.

ENES'IN PAYLASTIGI TWEETLER (Enes 16.11 12:22): Enes begendigi tweetleri yapistirir. (1) Bu tweetlerin tarzini ogren: kisa, haber odakli, kaynak/analist adi + rakam + net sonuc; tahmini 'tahmin' olarak belirt. Otomatik turlarda bu tarzda tweetler at. (2) Yapistirdigi KONU hakkinda hemen arastir (2 kaynak) ve hemen tweet at, tur beklemeden. Anthropic gecen kisimda Anthropic adi yazilmaz (yasak kural), 'bir baska buyuk yapay zeka sirketi' denir. KART NOTU: logo icin ticker '$' ile verilmeli ($GOOGL), yoksa logo cizilmez; cizgi'de buyuk rakam logoyla cakisabilir, baslik ve rakam kisa tutulur.

PORTFOY YONETIMI (Enes 16.11 12:47, EN ONEMLI YENI KURAL): Arastirma turlarinda ayni zamanda Enes'in PORTFOYUNU de yonet: portfoye su hisse eklenebilir / su hisse cikarilabilir gibi FIKIRLER ver (yalniz Enes'e SendUserMessage ile, TWEETTE ASLA al/sat tavsiyesi yok, 'aldim/sattim' yok). Grafikleri/teknik gorunumu de incele ama yalnizca SON IKI GUNDE yayinlanmis grafik/teknik analiz kaynaklari (tarih kontrolu zorunlu). Bunu her turda yapma; arada bir firsat bulunca ya da portfoydeki bir hisseyi begenmezsen (zayif temel/teknik, kotu haber) bunu Enes'e soyle. Portfoy (Enes 16.11 12:49 GUNCEL, SPCX cikti, SITM girdi): NBIS RKLB DOCN SITM AXON CBRS VRT; Enes yatirimci, piyasa acilisinda hepsine ESIT AGIRLIK alacak. Ilgi listesi: ON AAOI HOOD TEM CRDO PLTR ISRG ASTS MU. Fikirler gerekceli (haber/bilanço/grafik kaynagi + tarih), 'bu bir finansal tavsiye degildir, karar senin' notuyla, kisa. Enes'in X'ine erisilmez; grafikler web aramasindaki son 2 gun tarihli teknik analiz yazilarindan alinir.

## OKUYUCUNUN AKLINDAKI SORUYU CEVAPLA (Enes 16.11 13:07, YENI KURAL)
- Tweette "organik degil", "tek seferlik", "satin almadan", "bilanco disi" gibi bir kusur/sart yazacaksan bunu havada birakma: arastir, ne kadari oldugunu 2 kaynakla bul (ornek: satin almanin payi, organik buyume orani) ve tweete yaz. Okuyucunun aklina gelecek soruyu once sen sor, sonra cevapla: "Bu iyi mi kotu mu? Rakamlar sisirilmis mi, yanlis mi? Duzeltince ne kaliyor?"
- Rakam bulunamiyorsa ya da tek kaynaktaysa tahmin yurutme; "ne kadari belli degil" de ya da o kusur cumlesini yazma. Tahmin yazarsan acikca "tahminen" de ve dayanagini (hangi rakamdan hesapladigini) belirt.
- Her iki yonu de ver: neden iyi isaret, neden dikkat edilmeli (iyi/kotu cevabi net olsun, tek cumle yorum kurali korunur).
- Ayni kural bilanco, satin alma, kar/zarar, hisse bolunmesi, geri alim gibi okuyucuyu "bu gercek mi?" diye dusunduren her konu icin gecerli. Tweet uzunsa kisa tut, en onemli cevabi sec.

## TEKNIK ANALIZ HER TURDA (Enes 16.11 13:09)
- Enes grafik/indikator kaynagi baglayacak (TradingView istedi; TradingView connector'i yok -> tarayici veya Twelve Data / Alpha Vantage connector onerildi). Baglaninca HER TURDA: portfoy (NBIS RKLB DOCN SITM AXON CBRS VRT) + firsat gorulen hisseler icin grafik ve indikatorlere bak (trend, 50/200 gunluk ortalama, RSI, MACD, hacim, destek/direnc, Bollinger vb.), Enes'e kisa karar notu ver (tut / ekle / azalt / izle + gerekce + seviye). Kararlar Enes'in; notlar sadece SendUserMessage ile, tweette al/sat yok.
- Kaynak bagli degilse eski kural: sadece son 2 gun tarihli grafik analizleri.
- X hesabina asla girilmez.
- (13:16) VERI KAYNAGI BAGLANDI: Yahoo Finance (query1.finance.yahoo.com izinli). `python3 ta.py NBIS RKLB ...` -> son kapanis, 5g/20g degisim, SMA20/50/200, RSI14, MACD, Bollinger, 20g dip/tepe, 52h, hacim orani. Alpha Vantage bagli ama ucretsiz anahtar ABD verisi vermiyor (kullanma). Her turda portfoy + firsat hisseleri icin calistir, Enes'e kisa not (tut/ekle/azalt/izle + seviye). Ilk analiz 16.11 13:17: hepsi 50/200 gunluk ortalamanin altinda; en zayif NBIS ve AXON, en guclu RKLB.
- (13:18) TRADINGVIEW: Enes'in Windows Chrome'u (Claude in Chrome, deviceId 2c13b0fb...) bagli; tradingview.com/chart/?symbol=NASDAQ%3ATICKER ile acilir. Enes'in duzeni: Vol20, EMA 20/50/100/200, Supertrend (Buy/Sell etiketleri), yatay destek/direncler. Sadece TradingView, X'e ASLA girme. Bilgisayar kapaliysa ta.py (Yahoo) ile devam. SMC indikatoru eklemek icin Enes'in onayini bekle (duzenini degistirir).
- (13:25) TradingView duzeni degisti (Enes onayi): EMA cikarildi, LuxAlgo Smart Money Concepts eklendi, kaydedildi. Grafikte: Vol20 + Supertrend + SMC (BOS/CHoCH, order block/talep-arz bolgeleri). EMA'lar ta.py'den. Sembol degistirmek icin URL: tradingview.com/chart/UN09ZFN8/?symbol=NASDAQ%3ATICKER (DOCN/VRT NYSE). Gerekirse baska gosterge icin birini cikarip tekrar bak (Enes izni var).

## HER TURDA PORTFOY + GRAFIK (Enes 16.11 13:25, KALICI KURAL, ozet)
Her turda tweet isinin YANINDA sunlari da yap:
1. GRAFIK: Bilgisayar/Chrome bagliysa TradingView (duzen UN09ZFN8: Vol20 + Supertrend + LuxAlgo SMC). Portfoy (NBIS RKLB DOCN SITM AXON CBRS VRT) + firsat gordugun hisseler. FIRSAT HISSESI ILGI LISTESIYLE SINIRLI DEGIL (Enes 13:25): ABD borsasinda yatirima uygun buldugun HERHANGI bir hisse olabilir (haber/bilanco/analist notu/grafik kurulumu ile one cikan). Oner: neden (temel + teknik), seviye, risk. Bak: Supertrend Buy/Sell ve cizgi seviyesi, SMC BOS/CHoCH yonu, talep/arz (order block) bolgeleri, fiyatin bunlara uzakligi. Gerekirse bir gostergeyi cikarip baskasini ekle, bak, kaydet (Enes izni var; plan Basic = grafik basina 2 gosterge). ASLA X'e girme.
2. TradingView YOKSA: `python3 ta.py <tickerlar>` (Yahoo: SMA20/50/200, RSI, MACD, Bollinger, hacim, 52h, 20g dip/tepe). Alpha Vantage ucretsiz anahtar ABD verisi vermiyor.
3. ENES'E NOT (SendUserMessage, tweetten AYRI, tweette asla al/sat yok): portfoyde begenmedigin/begendigin degisiklik, EKLEME firsati (Supertrend Buy, talep bolgesine gelis, yukari BOS/CHoCH), AZALTMA/SATMA isareti (Supertrend Sell, destek/talep kirilimi, asagi BOS), portfoy disi firsat hisse. Kisa: hisse + ne oldu + seviye + fikir (tut/ekle/azalt/izle). Degisiklik yoksa her tur yazmak zorunlu degil ama grafiklere her tur bak. Notlar fikir, karar Enes'in.
4. Ilk tam inceleme 16.11 13:25: RKLB tek Supertrend Buy (destek 57,2); VRT esikte (202,2 alti -> Sell'e donebilir; talep 160-170); SITM/DOCN/CBRS/NBIS/AXON Supertrend Sell ve dusus yapisi; AXON ve NBIS en zayif. Onceki durumla karsilastirarak degisimleri bildir.
- ZORUNLU GOSTERGE SETI (Enes 16.11 13:27, HER TURDA HEPSINE BAK): EMA 200 (ana trend), VWAP (SMC bolgelerinde adil deger; 20g + son ana dip/tepeden anchored), RSI 14 (likidite supurmesi sonrasi momentum), MACD (trend donusu/momentum), ATR 14 (stop/hedef mesafesi), Volume Profile (POC + deger alani, hacim/likidite bolgeleri), ADX 14 (trend gucu, +DI/-DI), Fibonacci Retracement (OTE 0.618-0.786), OBV (hacim akisi, uyumsuzluk). Hepsi `python3 ta.py <tickerlar>` ile tek komutta hesaplanir (TradingView Basic 2 gosterge siniri yuzunden). TradingView'da Supertrend + SMC ile birlestir. Enes'e notta gerekli olanlari kullan (ozellikle ATR ile stop, Fib OTE ile giris, VP POC ile hedef).
- TAM GOSTERGE LISTESI + COKLU ZAMAN DILIMI (Enes 16.11 13:28, ZORUNLU): RSI, MACD, EMA, SMA, Bollinger, VWAP, Stochastic RSI, ADX, Ichimoku, ATR, OBV, CCI, Williams %R, Parabolic SAR, Supertrend, MFI, Fibonacci, Keltner, Aroon, Volume Profile, SMC. Her analizde HEPSI ve 1 saat / 4 saat / gunluk / haftalik dilimlerde. Komut: `python3 ta2.py <tickerlar>` (gunlukte hepsini, diger dilimlerde ozet basar; `-v` tum dilimlerde hepsi). SMC icin ana kombinasyon: SMC + EMA200 + VWAP + RSI14 + ATR + Volume Profile + Fibonacci (teyit). ta2.py'deki SMC/Supertrend yaklasik hesap; TradingView aciksa SMC ve Supertrend icin TradingView esas (gunluk + 4s + 1s grafiklere bak). Ilk tam tarama 13:30: coklu dilimde tek dengeli gorunen RKLB (gunluk Supertrend Buy, SMC gunlukte 61,13 yukari CHoCH); AXON tum dilimlerde asagi (19/23 asagi); NBIS 4s/gunluk 20/23 asagi; CBRS ve DOCN 1 saatlikte toparlanma, ust dilimler asagi.
- KONUSMA DILI (Enes 16.11 13:31): Portfoy notlarinda "tavsiye/oneri" dili YOK; "BEN OLSAM" diye konus. Ornek: "Ben olsam bugun RKLB'den biraz eklerdim", "Ben olsam bugun AXON'a girmezdim, 291 kirilmadan dipte donus gorursem 295-300 civarinda eklerdim", "Ben olsam elimde NBIS varsa 109 altinda kapanirsa azaltirdim". Her notta somut seviye (giris, stop = ATR'ye gore, hedef = VP POC/FVG/direnc) ver. Bu dil SADECE Enes'e ozel mesajlarda; tweetlerde al/sat yok kurali aynen gecerli.
- YATIRIM TARZI (Enes 16.11 13:32): Enes YATIRIMCI, amaci yukselis basladiginda almak DEGIL, EN DIPLERI bulmak. Notlari buna gore yaz: dip bolgesi (talep/order block, Fibonacci OTE 0.618-0.786, Volume Profile deger alani alti/HVN, haftalik destek), dip isaretleri (RSI/StochRSI/Williams %R/MFI asiri satim, OBV ve RSI pozitif uyumsuzluk, likidite supurmesi sonrasi geri donus, kapitulasyon hacmi), kademeli alim seviyeleri ("ben olsam su 2-3 seviyeden parca parca alirdim") ve tezin bozuldugu seviye. Trend teyidi beklemek yerine dip bolgesine yaklasmayi bildir.

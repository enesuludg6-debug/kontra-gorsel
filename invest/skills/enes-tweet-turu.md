---
name: "enes-tweet-turu"
description: "Enes Uludağ'ın X hesabı için otomatik paylaşım turu, Enes'in istediği tweet veya 13F tweeti hazırlanıp Buffer'dan atılırken kullanılır: kontrol listesi, kaynak, yazım, kart ve kayıt kuralları."
---

# Enes tweet turu

Repo: `/home/claude/kontra-gorsel/invest` (GitHub enesuludg6-debug/kontra-gorsel). Ayrıntı ve geçmiş için başvuru dosyaları: `DEVIR_TAM.md` (tüm kurallar, portföy, adaylar), `DEVIR_OZET.md`, `ORNEKLER.md` (beğenilen tweet kalıpları), `DONGU.md` (her paylaşımın kaydı), `temel_karne.md`. Bu skill ile DEVIR_TAM çelişirse EN YENİ tarihli kural geçerlidir; yeni kural gelince ikisi de güncellenir.

Her zaman Türkçe yaz. Enes'e giden mesajlar da Türkçe.

Hesabın amacı (her şeyin üstünde): en iyi getiriyi yakalamak ya da en bilgili görünmek değil, GÜVEN ve İYİ İÇERİK. Doğru olmayan rakam yerine eksik tweet; tutmayan tahminden bahsedilmez, yalnız doğru çıkanlar (kural 23); abartı ve heyecan yok. Hedef okur ABD borsasını az bilen biri: kısa, sade, anlaşılır. X hesabı @enes1050392 (Enes Uludağ, EnesInvestUS).

Bilanço önizleme/rakam/analiz ve 13F serisi için `enes-bilanco-13f`, 18:00 temel analiz (kural 37: teknik analiz yok), portföy notları ve temel karne için `enes-portfoy-analiz` skill'ini de yükle.

## 1. Tur başı kontrol (sırayla)

1. `ReadNotifications` (bildirim varsa), sonra `cd /home/claude/kontra-gorsel/invest && git pull -q`.
2. `invest/DURUM.md` ve `tail -n 30 DONGU.md` oku (DEVIR_TAM'ı baştan okuma, kural 18): satır başında tek başına `DURDUR` varsa HİÇBİR ŞEY yapma, yeni tur kurma.
3. Son OTOMATİK paylaşım saati: 20 dakikadan yeniyse paylaşma; kalan süreye göre 20-40 dk sonrasına aynı mesajla tur kur. Enes'in istediği tweet hemen atılır (o 20 dk kuralına girmez ama sonraki otomatik turu en az 20 dk sonraya kaydır).
4. Saat 01:00-09:00 TSİ arasıysa paylaşma (önceden bilinen açıklama hariç), 09:05'e tur kur.

## 2. Konu seçimi (öncelik sırası)

1. Takvimdeki bilanço/veri açıklandıysa (günün başlıkları listesi dahil, bölüm 9): önce yorumsuz RAKAM tweeti (format aşağıda), 15 dk sonra yorumlu analiz turu.
2. Son dakika (son 1-3 saat): SEC 8-K/Form 4, IR bültenleri, Reuters/CNBC/Bloomberg/Benzinga, analist notları (TheFly, StreetInsider, MarketBeat, TipRanks).
3. Sezona bağlı seri: 13F serisi (Şubat/Mayıs/Ağustos/Kasım ortası; her turda 1 yatırımcı; DONGU'daki "13F SERİSİ: ... / sıradaki" satırını izle).
4. Sabit seriler: 09:05 ve ~15:00-15:25 vadeli işlemler (kart `isi`, kolon=2, hane=2), kapanış 00:05-00:45, haftalık takvim.
5. Menü: analiz, karşılaştırma, eğitici.
- Tekrar yok: DONGU'nun tamamı + Buffer son 50 gönderide olan konu yeni açı olmadan atılmaz (yeni açıyla atılırsa DONGU'ya "devam: önceki dosya"); aynı ticker 3 saatte bir; aynı haber 24 saatte tekrar yok.
- "Taze haber yok" diye boş tur geçilmez: sırasıyla (1) son 24 saatin analist notları, (2) bugünkü lansman/ortaklık/anlaşmalar, (3) bu haftanın takvimi, (4) menü.
- Zamana bağlı menü: sabah notu 09:30-11:00, premarket 16:15-17:15, açılış 17:30-18:30, kapanış 00:05-00:45, hafta içi 22:00 "yarın ne var", Cuma/Cumartesi haftanın karnesi, Pazar/Pazartesi "bu hafta ne var". Makro veri günü: beklenti → sonuç + yorum (kural 25: ne demek, büyük resim, Fed ne düşünür, piyasaya etkisi, net görüş; tek tweet bile olsa).
- Öncelikli türler: son dakika; bu hafta/yarın ne var; bilanço rakamı (yorumsuz); bilanço analizi (yorumlu); içeriden alım-satım (günde 1-2, SEC Form 4; kod P piyasadan alım anlamlı, 1 Mn $ üstü, küme alımı; 10b5-1 planlı satış ve kod F vergi satışı açıkça yazılır); büyük olayda düz haber yerine "bağlam + görüş" tweeti (günde en az 1-2).
- Eğitici içerik haftada 3-5 (terim, "bu şirket ne iş yapar", strateji/psikoloji). Karşılaştırma/veri: 1 yıl önce vs bugün, iki rakip, sektör sıralaması, uzun dönem tek metrik, yapay zekâ yatırım harcaması, emtia/dolar/tahvil/kripto.
- `invest/gundem.md`'de Enes'in elle eklediği konular önceliklidir; kullanınca DONGU'ya "(gündem)" yaz.

Haber hızı kaynakları (her turda bu sırayla): (1) SEC EDGAR (8-K, 6-K, Form 4, 13F), şirket IR, PR Newswire / Business Wire / GlobeNewswire / Accesswire; (2) Reuters, CNBC, Bloomberg, AP, Benzinga son dakika; (3) takvim: Investing, TradingEconomics, Earnings Whispers, Nasdaq, Yahoo, Zacks, StockAnalysis; resmi veri: Fed, BLS, BEA, Treasury, Census; (4) analist not akışları: TheFly, StreetInsider, Investing "analyst ratings", MarketBeat, TipRanks, Benzinga ratings, Futu/Moomoo, aktiencheck/finanzen; içeriden/kurum: OpenInsider, Quiver, WhaleWisdom, Dataroma; derin: Semianalysis, The Information, Nikkei, DigiTimes, TrendForce, Axios, Techmeme, SpaceNews. Sosyal hızlı haber hesapları (Walter Bloomberg, FirstSquawk vb.) 2 güvenilir kaynak olmadan kullanılmaz.

Analist notu tweeti kalıbı: kurum + analist (biliniyorsa) + eski → yeni hedef + tavsiye + notun gerekçesi + bağlam (son 2-4 haftadaki önceki değişiklik, bilanço) + mevcut fiyata göre fark (Yahoo fiyatıyla hesapla) + tek cümle görüş. Hedef ve tavsiye 2 kaynakla.

Vadeli işlemler (her işlem günü 09:05 ve ~15:00-15:25): Yahoo `ES=F NQ=F YM=F RTY=F` önceki kapanışa göre % + 1 haber kaynağı; kart `isi(..., etiket="VADELİ İŞLEMLER", kolon=2, hane=2)`; %1 üstü sürprizde ek tweet; "vadeli = açılışın işareti, garanti değil".

Enes bir şey atarsa:
- Başkasının tweeti/grafiği: tur beklemeden hemen araştır, her rakamı 2 kaynakla doğrula, KENDİ cümlenle yaz, kendi kartını çiz; tutmayan rakamı Enes'e söyle; tarzını `ORNEKLER.md`'ye şablon olarak ekle. Başkasının tweeti kopyalanmaz/çevrilmez.
- "Yorum yaz" derse yanıt metni hazırla (Enes kendisi atar, otomatik yanıt yok); istenirse İngilizcesi.
- (Kural 37-38) Claude teknik analiz yapmaz; Enes teknik analizini atarsa kural 38'e göre sade dilde tweet taslağı yazılır ve Enes'e gönderilir (Claude paylaşmaz).
- Kişi haberinde fotoğraf gerekiyorsa internetten indirme; Enes'e "X'in fotosunu at" de, bekleme, o tur başka konu at. Enes'in fotoları `invest/foto/`.
- Enes'in istediği tweetler otomatik zincirin zamanlamasını değiştirmez; ama sonraki otomatik paylaşım en az 20 dk sonra olur.
- Anthropic adı/konusu (halka arzı dahil) ASLA tweete girmez.
- Portföy güncellemesi tweeti yalnız Enes açıkça isterse. Teknik analiz tweetini Claude ATMAZ (Enes atar).

## 3. Doğrulama

- Her rakam ve her yan iddia en az 2 bağımsız kaynakla. Tek kaynaktaysa tweete girmez (rakamsız yön verilebilir). Aynı haberin yeniden yayını (Yahoo'daki 24/7 kopyası gibi) ikinci kaynak sayılmaz.
- YIL ve ÇEYREK kontrolü: arama sonuçları 2025 ile 2026'yı karıştırır; tarihi mutlaka kontrol et.
- Canlı fiyat: Yahoo chart uç noktası (urllib, User-Agent) `query1.finance.yahoo.com/v8/finance/chart/<T>`.
- sec.gov WebFetch izin isteyebilir; cevapsız kalırsa tekrar deneme, 13f.info gibi EDGAR aynası + haber kullan.
- X sitesine girme. Sosyal medya iddiası 2 güvenilir kaynak olmadan kullanılmaz.
- Kişisel/özel hayat detayı yazılmaz (ör. Huang istifasında yalnız şirket ve piyasa yönü).

## 4. Yazım

- Arkadaşına anlatır gibi, sade ve doğal cümleler. Terimleri sadeleştir: EPS = hisse başı kâr, guidance = şirketin verdiği tahmin/yönlendirme, capex = yatırım harcaması.
- Şirketi ilk geçtiği yerde ne iş yaptığıyla tanıt. Ticker'lar gerektiğinde $TICKER.
- İlk satır durdurmalı: rakam, tezat ya da net tespit.
- KESİN KURAL 25 (Enes 17.11 16:51, "insanlar bizi haberlere ulaşmak için takip ediyor ama asıl takip ettiği şey bizim fikirlerimiz, olaylara dair düşüncelerimiz"): Haberi vermek yetmez; her haber ve veri tweetinin ağırlığı YORUMDUR (yaklaşık üçte biri haber, üçte ikisi düşünce). Okur tweeti bitirdiğinde şu sorulara cevap almış olmalı: (1) Bu ne demek, sade dille? (2) Neden şimdi önemli, büyük resimde neye işaret ediyor (büyüme, enflasyon, tüketici, şirket kârları, yapay zekâ döngüsü)? (3) Fed ne düşünür, faiz beklentisi nasıl değişir (FedWatch/vadeli fiyatlama, 2 kaynak)? (4) Piyasaya, sektörlere ve takip edilen hisselere etkisi ne? (5) Bizim net düşüncemiz ne? Makro veri tweeti TEK tweet olsa bile bu beşini içerir; ayrı 'sonuç' ve 'etki' tweeti yerine tek, yorumlu tweet. Bilanço rakam tweeti yorumsuz kalır ama 15 dk sonraki analiz tweeti bu beş soruyu cevaplar. Görüş etiketsiz, düz cümleyle (kural 11), al/sat yok, tahmin dili ölçülü.
- Görüş zorunlu (bilanço rakam tweeti hariç). Enes'in en sevdiği tarz: haberi tekrar etmek yerine arkasındaki yapıyı anlatan, olayları birbirine bağlayan "bağlam + görüş" (ORNEKLER 18).
- ETİKETLİ GÖRÜŞ GİRİŞİ YASAK: "Benim okumam:", "Benim görüşüm:", "Görüşüm:", "Yorumum:", "Not:", "Asıl ilginci", "Bence önemli nokta şu:", "Burada kritik olan", "İşin özü", "Önemli nokta:", "Sonuç olarak", "Özetle", "Kısaca", "Bir de şu var:", "X neden önemli?" ve iki noktalı her benzeri. Görüş rakamlardan sonra düz cümleyle gelir.
- "Bence" en fazla bir kez; kapanışları çeşitlendir.
- YASAK: al/sat tavsiyesi, emir kipi ("alın, kaçırmayın"), hedef fiyatım, emoji, hashtag, @mention, link, soruyla bitirme, portföy tutarı/ağırlığı, "aldım/sattım".
- 13F uyarısı gerekiyorsa etiketsiz: "Tablo 30 Eylül itibarıyla, sonrasındaki işlemler dosyada yok."
- Gönder öncesi tara: satır başında "kelime + iki nokta" var mı, yasak kalıp var mı, tek kaynaklı rakam var mı.

Bilanço rakam tweeti (yorumsuz):
```
$TICKER 3. ÇEYREK BİLANÇOSU
• Gelir: X / Beklenti: Y
• Hisse başı kâr: X / Beklenti: Y
• (şirkete özgü 2-3 metrik: çipte brüt marj ve veri merkezi geliri, bulutta backlog, yazılımda ARR, perakendede aynı mağaza satışı)

4. ÇEYREK TAHMİNİ
• Gelir: X / Beklenti: Y
```

## 5. Kart

- `invest/kart2.py`. Düzenler: bento, halka, isi, takvim, cizgi, panel, uclu, soz, editoryal, skor, zaman, ilerleme, dilim, dortlu, manset, siralama. `versus` kaldırıldı.
- Son 3 turda kullanılan düzen tekrar edilmez (DONGU'daki "Son 3 düzen" notuna bak).
- Tür → düzen: bilanço rakam = skor/terminal; analiz = bento/uclu/panel; vadeli = isi; kapanış = isi/dortlu; son dakika = sondakika/manset; sıralama = siralama.
- Logo yalnız `"$TICKER"` verilince çizilir. Enes kuralı (16.11): logolar ÇOK belirgin, `kart2.LOGO_BUYUT = 1.8`, KÜÇÜLTME YOK. Logo bir düzende taşıyorsa logoyu küçültme; başlığı kısalt ya da logoyu düzgün taşıyan başka düzen seç (dortlu/bento/uclu/editoryal/siralama). Koyu logolar beyaz plakada. Logo dosyası yoksa `logo/XXX.png` ticker yazı logosu oluştur. `halka` logo çizmez, logo gereken konuda kullanma. BRK logosu yok.
- Kicker'da şirket adı bozulabilir ("SİTİME"); ticker kullan ("SITM • 3. ÇEYREK"). "OpenAI" kart fontunda "OpenAl" görünür, kullanma.
- Kartı kötü çıkarsa YENİ dosya adıyla yeniden çiz (raw URL önbelleği), kötüsünü sil.
- Font tuzakları: "AI" yerine "Yapay zekâ"; Türkçe büyük harfleri hazır yaz ("GELİRİ"); "Kaynak:" öneki verme; kaynak satırını kısa tut (taşar).
- Her kartı Read ile kontrol et (taşma, boş logo kutusu, üst üste binme). Sorun varsa düzelt ve yeniden çiz.
- Dosya: `g/YYYYMMDD_HHMM_konu.jpg` → git add, commit (attribution satırlarıyla) → `git -c push.negotiate=true push -q origin main` → `sleep 4` → raw URL `https://raw.githubusercontent.com/enesuludg6-debug/kontra-gorsel/main/invest/g/<dosya>` curl ile 200 olmalı. 200 değilse görselsiz tweet atma.

## 6. Paylaşım

- Buffer `create_post`: channelId `6af99a1aece6dfde5fd109c7`, schedulingType `automatic`, mode `shareNow`, image asset + altText (Türkçe, yazım hatasız).
- Uzun tek tweet serbest; Enes "flood değil tek tweet" derse tek tweet.
- Ardından Enes'e `SendUserMessage`: başlık "Paylaşıldı (SS:DD): TÜR", tweet metninin aynısı, sonra "Ne anlama geliyor?" (terimler, tweete konmayan tek kaynaklı bilgiler, Enes'in hisseleri etkileniyor mu).
- "Ne anlama geliyor?" 3-6 kısa madde: terim/bilgi sade anlatım, piyasada neden önemli, iyi/kötü sinyal nasıl okunur, varsa tarihten örnek, doğrulanamayıp tweete girmeyen rakamlar. Bu bölüm tweete girmez.
- Enes'in portföyündeki hisseleri (DEVIR_TAM bölüm 1; şu an DOCN RKLB SITM AXON CBRS VRT AVGO, NBIS YOK) etkileyen büyük hareket varsa ayrıca kısa "ben olsam" notu.
- Her turda tweetten sonra portföy taraması (kural 37): 7 portföy hissesinde son haber/8-K/Form 4/analist revizyonu; teze dokunan bir gelişme varsa Enes'e kısa "ben olsam" notu (değerleme bölgesi + tez durumu). Değişiklik yoksa mesaj zorunlu değil.

Tarayıcı: Enes'in X hesabına ve x.com'a HİÇBİR ŞEKİLDE girilmez. Chrome yalnız tradingview.com ve haber/birincil kaynak okumak için (yeni sekme, get_page_text, iş bitince sekmeyi kapat, TradingView sekmesine dokunma). Form, giriş, abonelik, yorum, paylaşım yok; çerez bannerında en gizli seçenek.

Hata durumları: Bash "classifier no verdict" → 1 kez tekrar, olmazsa o tur paylaşma, 5-10 dk sonrasına kur. WebFetch PROVENANCE_REQUIRED → tekrar deneme, WebSearch. Buffer hata → 1 kez tekrar, olmazsa DONGU'ya yaz ve atla. Push reddi → görselsiz tweet atma. Buffer aylık ~1000 gönderi; 900'ü geçerse Enes'e söyle.

## 7. Kayıt ve sonraki tur

1. `DONGU.md`'ye satır: `- SS:DD (GG.AA) AUTO (TÜR): dosya.jpg (düzen) - rakamlar (kaynaklar). Tek kaynak (atılmadı): ... Buffer <id>. Son 3 düzen: a, b, c.` 13F'de ayrıca `- 13F SERİSİ: <isim> atıldı / sıradaki: <isim>`.
2. commit + push.
3. `python3 -c "import random;print(random.randint(20,40))"` ile gecikme; `send_later` adı "Otomatik paylaşım turu", mesaj = önceki tur mesajı, yalnız bu turun konusu, sıradaki konu/isim, son 3 düzen ve saatler güncellenir. 01:00 sonrasına düşerse 09:05.
4. Zaman kalırsa (13F/bilanço günü değilse) `temel_karne.md`'de en eski 1-2 hissenin karnesini yenile (DEVIR_TAM 14g-14i).

## 9. Günlük key levels + günün önemli başlıkları (kesin kural 13, Enes 17.11 12:45)

- Her ABD işlem günü 10:30 TSİ (hafta sonu/tatil yok; 26.11 Şükran Günü yok). Zincir: send_later adı "Günlük key levels + başlıklar"; her çalışma sonunda sıradaki işlem gününün 10:30'una kendini kurar. Her otomatik turda list_triggers ile kontrol et, yoksa kur.
- Tek tweet + kart (isi/takvim/dortlu/zaman; son 3 düzen kuralı), Buffer shareNow:
  - KEY LEVELS: S&P 500 ve Nasdaq 100 için önceki kapanış, vadeli yönü, 2 destek + 2 direnç. Seviyeler `python3 ta2.py -v ^GSPC ^NDX > /tmp/kl.txt` çıktısının tamamından; yalnız en az 2 gösterge/dilim çakışan seviye yazılır, her birine sade gerekçe ("önceki dip", "200 günlük ortalama", "doldurulmamış boşluk"). Gözlem dili ("kırılırsa satış hızlanabilir"); al/sat ve emir kipi yok.
  - GÜNÜN BAŞLIKLARI: o gün açıklanacak makro veri (saat TSİ + beklenti), önemli bilançolar (açılış öncesi/kapanış sonrası, HBK + gelir beklentisi), Fed konuşması/tutanak, büyük olaylar. En fazla 5-6, saat sırasıyla; her saat ve beklenti 2 kaynak.
- BAŞLIK AÇIKLANINCA: saati belli her başlık için açıklanma saati +3 dk'ya tek seferlik send_later ("Başlık açıklandı: <başlık>"). O tur sonucu 2 kaynakla doğrular, yorumsuz rakam tweeti atar (veri: beklenti → sonuç; bilanço: CRWV formatı, enes-bilanco-13f; bilançoda 15 dk sonra analiz turu). Sonuç yayınlanmadıysa 5-10 dk sonrasına kendini yeniden kurar (en çok 3 kez). 01:00 öncesi kapanış sonrası açıklamalar bilinen açıklama istisnasıdır. Saati belirsiz başlıklar otomatik turlarda öncelikle kontrol edilir.
- Bu tweetler otomatik zincirin zamanlamasını değiştirmez; normal turlar aynı konuyu tekrar atmaz.
- DONGU: `- SS:DD (GG.AA) AUTO (KEY LEVELS+BAŞLIKLAR): dosya (düzen) - seviyeler | başlıklar ve saatleri | kurulan başlık turları | Son 3 düzen: ...`.
- DEVİR: Enes "devir" yazınca yeni devir notunda kesin kural 13 ve A5 maddesi aynen korunur; yeni oturum A5'te bu zinciri mutlaka kurar (bugün 10:30 geçmiş ve başlıklar henüz açıklanmamışsa hemen bir kez çalıştırır).

## 10. Performans, sabit görevler, takvim ve hız (kesin kural 14-16, Enes 17.11 12:54)

- PERFORMANS (kural 14): DONGU satırında TÜR şu listeden yazılır: VADELI, 13F, BILANCO-RAKAM, BILANCO-ANALIZ, BILANCO-ONIZLEME, ANALIST, SONDAKIKA, BAGLAM-GORUS, KAPANIS, TAKVIM, KEY-LEVELS, EGITICI, ENES-ISTEGI. Her tweet `invest/performans.md` tablosuna da eklenir (tarih, saat, tür, konu, düzen, Buffer id). Günün ilk turunda önceki günün tweetleri için Buffer `get_post` (includeMetrics: true) ile görüntülenme, beğeni, yanıt, repost çekilir. Pazar 21:30 haftalık rapor: türe/saate/düzene göre ortalama, en iyi/en kötü 5, önerilen içerik karışımı Enes'e; tek haftayla karar yok, 3 haftalık trend.
- SABİT GÖREVLER (kural 15): tekrarlayan görev (create_trigger, cron, CRON_TZ=Europe/Istanbul): teknik kontrol 18:00 ve 23:30 hafta içi, key levels + başlıklar 10:30 hafta içi, Pazar 20:00 takvim, Pazar 21:30 performans, çeyreklik 13F başlangıcı (15 Şubat, 16 Mayıs, 15 Ağustos, 15 Kasım 09:05), her gün 09:00 sabah kontrolü. Görev mesajları bağımsız ve tam yazılır (yeni oturumda ateşlenebilir). Rastgele aralıklı paylaşım turu zincir kalır; sabah kontrolü zincir koptuysa (son otomatik tur 60 dk'dan eski, 09:00-01:00) yeniden kurar ve Enes'e söyler.
- TAKVİM VE HIZ (kural 16): her tur başında `invest/takvim.md`'ye bak; önümüzdeki 60 dk içinde bilanço/veri varsa hazırlık (T-45/60 dk) ve yayın (T-2 dk) görevleri kurulu mu kontrol et, yoksa kur (ayrıntı `enes-bilanco-13f`). Bilanço ve saati belli veri başlıklarında bölüm 9'daki "+3 dk tek seferlik tur" yerine bu protokol uygulanır. Kurulacak otomatik tur bir yayın saatine ±15 dk denk geliyorsa yayından 20+ dk sonraya kur.
- KART: `skor` düzeni 1.8 kat logoyu taşımıyor; bilanço rakam kartı `uclu` (logo küçültme yasak).

## 11. Hesap kilidi (kesin kural 17, 17.11 13:11)

- Her tur, her görev, her bilanço yayını EN BAŞTA `invest/AKTIF_HESAP.md`'yi okur. Görev mesajındaki `HESAP=<etiket>` ile dosyadaki `AKTIF:` etiketi farklıysa HİÇBİR ŞEY yapma (tweet yok, push yok), kendi tekrarlayan görevlerini devre dışı bırak (update_trigger enabled=false), yeni görev kurma. Böylece eski hesabın görevleri yeni hesaba geçince kendiliğinden susar, çift tweet olmaz.
- Görev mesajları ve send_later mesajları her zaman `HESAP=<etiket>` içerir. Etiketi bilmiyorsan `AKTIF_HESAP.md`'deki aktif etiketi kullan.
- Hesap değişimi `invest/HESAP_DEVRI.md` ile yapılır.

## 12. Tasarruf, haftalık/aylık özet, gelecek hafta, düzeltme (kesin kural 18-21, Enes 17.11 13:28)

- OKUMA (kural 18): turda DEVIR_TAM ve DEVIR_OZET BAŞTAN OKUNMAZ. Okunan: bu skill + `invest/DURUM.md` + `tail -n 30 DONGU.md` (+ takvim.md). DEVIR_TAM'dan yalnız gereken bölüm grep ile. Tur sonunda DURUM.md güncellenir (son 10 tweet, ticker saatleri, son 3 düzen, 13F sırası, bekleyenler).
- Otomatik tur send_later mesajı KISA ŞABLON (DEVIR_TAM kural 18'deki metin); uzun kural metni mesaja kopyalanmaz.
- Buffer tekrar kontrolü first 5. WebSearch varsayılan standard. Turda portföy taraması kısa ta2 çıktısıyla; tam (-v) yalnız teknik kontrol ve key levels.
- HAFTALIK ÖZET (kural 19): Cumartesi 11:00 sabit görev; endeksler haftalık %, en çok konuşulan 3 olay + kısa görüş, haftanın en iyi/en kötü büyük hissesi; tür HAFTALIK-OZET.
- GELECEK HAFTA (kural 20): Pazar 20:00 takvim görevi takvimden tek tweet + takvim kartı (en önemli 8-10 olay, gün + TSİ saat, beklenti 2 kaynak); tür TAKVIM.
- AYIN ÖZETİ (kural 21): ayın ilk ABD işlem günü 11:00; endeksler + takip edilen hisseler aylık % (portföy/ağırlık yazılmaz), en önemli 3 olay; tür AYLIK-OZET.
- DÜZELTME (kural 21): atılmış tweette hata çıkarsa Enes'e HEMEN mesaj, aynı gün sade düzeltme tweeti ("Az önceki $X tweetinde Y'yi Z yazdım, doğrusu W."), DONGU'ya "DUZELTME:" ve `invest/HATA_GUNLUGU.md` kaydı; tekrar eden hata türü için skill'e önlem maddesi.

## 13. Yeni içerikler ve tek doğrular kuralı (kesin kural 22-23, Enes 17.11 14:35)

- YALNIZ DOĞRU ÇIKANLAR (kural 23): tutmayan tahmin/beklenti/"ben olsam" tweette anılmaz; tutan tahmin bağlama uyuyorsa söylenebilir. Atılmış tweetteki yanlış RAKAM için kural 21 düzeltme aynen geçerli.
- ŞABLONLAR: sık türlerde `invest/sablonlar.md`'deki iskeleti doldur (cümleleri her seferinde değiştir). Makro veri tweetine `invest/makro_sozluk.md`'den tek cümle (A/B sırayla, DONGU'ya "sözlük: X-A").
- KARIŞIM: DURUM.md "İçerik karışımı" bölümü varsa konu seçimi ona uyar (Enes onaylı).
- HER TURDA EK KONTROL: Yahoo ^TNX ve DX-Y.NYB + CME FedWatch; 10 yıllık ±8 baz puan, DXY ±%0,6 ya da toplantı olasılığında 15 puan üstü değişim varsa FED-TAHVIL tweeti (günde en fazla 1, şablon 8).
- TAKVİMDEN: kurumsal olaylar (halka arz, bölünme, büyük temettü, endeks giriş/çıkış) ve lansmanlar (GTC, Apple, re:Invent, CES, I/O, Build, Computex) günü gelince tweet (KURUMSAL / LANSMAN).
- BİLANÇO SONRASI: önizlemede opsiyon beklenen hareketi; ertesi gün açılıştan sonraki ilk turda portföy ve büyük şirketler için "beklenen ±%X, gerçekleşen %Y" (BEKLENEN-HAREKET); portföy/ilgi listesi bilançosunda rakip karşılaştırma kartı (RAKIP, panel/dortlu).
- 13F: seri bitince sonraki turda 13F-OZET (ortak alınan/satılan, en az 3 yatırımcı).
- MENÜ: ayda 2-3 kez "1 yıl önce bugün" (BIR-YIL, yalnız doğru çıkanlar).
- İLGİ LİSTESİ (genişledi): ON AAOI HOOD TEM CRDO PLTR ISRG ASTS MU + ANET ALAB MRVL COHR LITE ETN GEV CRWD NET DDOG APP RBRK PL LUNR. Zaman kalan turlarda günde 1-2 yeni adayın temel karnesini çıkar (`temel_karne.md`, /50); 30 altını DURUM.md'de "çıkarıldı" yap.
- Sabit görevler (kendileri yapar, turlar tekrar atmaz): içeriden alım + geri alım radarı hafta içi 14:20, sektör ısı haritası Cmt 13:25, ilgi listesi sıralama Cmt 16:25, bilanço sezonu karnesi Pazar 14:25, analist hedef özeti (ayın ilk Pazarı) ve değerleme bandı (ikinci Pazar) 12:25, mevsimsellik ayın ikinci işlem günü 11:00 (ayın özeti görevi).

## 8. Yeni kural gelince

Enes yeni bir kural verirse: `DEVIR_TAM.md`'ye kesin kural olarak (tarih + Enes'in sözü), `DEVIR_OZET.md`'ye bir satır, bölüm 18 kayıt tablosuna satır, `DONGU.md`'ye ENES satırı ekle, push et; bu skill'in güncellenmesini `propose_skills` (improvement) ile öner ve AYNI DEĞİŞİKLİĞİ `invest/skills/<skill>.md` kopyasına da yaz (başka hesaba geçişte kaynak burası).
## 13. Periyot defteri (kesin kural 24, Enes 17.11 16:33)
Sohbet her gün değişebilir; yeni sohbet "en son ne zaman yapıldı, bu hafta kaç kez yapıldı" bilgisini HAFIZADAN bilemez. Bu yüzden haftada/ayda/N günde bir ya da "en çok/en az N kez" kuralı olan her iş `invest/periyot.json` defterine göre yapılır, tahminle değil.
- Tur ve görev başında: `python3 periyot.py durum` (UYGUN/BEKLE ve "YAPILMALI" olanlar). Tek iş için `python3 periyot.py kontrol <anahtar>` (çıkış 0 = uygun).
- İş yapılınca HEMEN: `python3 periyot.py yap <anahtar> "<kısa not>"`, sonra commit + push (DONGU satırıyla aynı commit).
- Makro sözlük cümlesi: `python3 periyot.py sozluk "<Veri adı>"` hangi varyasyonun (A/B) kullanılacağını söyler (14 gün tekrar yok); kullanınca `yap sozluk:<Veri>-<A|B>`.
- Karne yazınca `yap karne <hisse>`; kalibrasyon "UYGUN" olunca yapılır ve `yap kalibrasyon`.
- Yeni periyodik kural gelirse (ör. "üç haftada bir"): `python3 periyot.py ekle <anahtar> min_gun 21 "<açıklama>"`. Türler: min_gun, gunluk_max, haftalik_min/max, aylik_min/max, ayin_pazari, baslangic_gun, her_n.
- Sabit görevler (cron) her çalışmada yeni oturumda açılır; saatleri cron'dan gelir, "bu ay/bu hafta zaten yapıldı mı" kontrolünü periyot.py ile yapar. Sabit görevler sohbet değişince silinmez; devirde yalnız send_later zinciri (oturuma bağlı) yeniden kurulur.
- ETİKETLİ TEKRAR KONTROLÜ (17.11 21:35, Enes: "farklı sohbete geçince tarihleri bilemez, kalıcı çözüm"): "son N günde/son N kayıtta aynısı olmasın" kuralları da hafızadan değil periyot.json'dan: `python3 invest/periyot.py etiket kontrol <grup> <değer> <gün> [son_n]` (çıkış 0 = uygun), kullanınca `etiket yap <grup> <değer>`. Gruplar: aday (teknik analiz adayı, 5 gün), cerceve (uzun yazı çerçevesi, son 3 kayıt: `etiket kontrol cerceve B 0 3`), uzun_ticker (uzun yazı hissesi, 30 gün). Yeni benzer kural gelirse yeni grup açılır. Haftalık alt sınırı olan işler `periyot.py durum`da "YAPILMALI" ya da geride kalınca "ACIL BUGUN YAP" yazar; tur_basi.sh bunu her turda gösterir, tur o işi o gün planlar.
- DONGU.md 7 günde arşive taşındığı için "son 2 hafta / bu ay" sorusunun cevabı DONGU'dan değil defterden alınır.

## 14. Ders sistemi (kesin kural 26, Enes 17.11 17:18 + 17:24)
Tam protokol `invest/DERSLER.md` başında (veri, ölçü, eşik, çakışma, yaşam döngüsü, takvim). Özet:
- Tur başında DERSLER.md "AKTİF DERSLER" + "OPERASYON DERSLERİ" okunur ve uygulanır.
- Tweet atınca `invest/performans_veri.csv`'ye satır (metrik boş; kaynak=sistem, kesin tür, görüş evet/hayır, düzen, Buffer id). Sabah 09:00 metrikleri doldurur.
- Ders yalnız `python3 ders_analiz.py` ile çıkar: göreli skor (görüntülenme / önceki 7 gün medyanı), grup medyanı. Eşik: ≥8 tweet, ≥2 hafta, ≥%25 fark, haftalar aynı yön → ADAY; 3. hafta da tutarsa AKTİF (adet/karışım değişikliği Enes onayıyla). Tek viral tweet ders değildir; 12 saatten taze tweet ölçülmez.
- Çakışma: Enes talimatı > kesin kurallar > Enes onaylı ders > otomatik ders > aday > gözlem. Yeni bulgu eski dersle çelişirse eski hemen silinmez: ÇELİŞKİ + 1-2 haftalık A/B deney, kazanan kalır, kaybeden "Silinen dersler"e gerekçeyle. Farklı kapsam (sezon, gün tipi) çatışma değildir, kapsamlı iki ders olur; dar kapsam genel dersi o kapsamda geçer. Eşit kanıtta yeni veri öncelikli.
- Her aktif ders 4 haftada bir yeniden test; 2 kez tutmazsa silinir. En çok 15 aktif ders. Tweetlerin %10-15'i keşif (yeni tür/saat/biçim), DONGU'da "(keşif)".
- Pazar 21:30: `ders_analiz.py` + Enes'e "bu hafta öğrendiklerim" (rakamlı, eklenen/silinen/çatışan). Operasyon dersleri (hatalardan, O-xxx) metrikle değil hata günlüğüyle eklenir.

## 15. Kredi tasarrufu (kesin kural 28, Enes 17.11 17:41: "tüm talimatlar harfiyen çalışmaya devam edecek; hiçbir şey değiştirmeden, ekleyerek tasarruf sağla")
Bu bölüm HİÇBİR kuralı kaldırmaz ya da gevşetmez; aynı işi daha az araç çağrısı ve daha az okuma ile yapma yollarıdır. Bir tasarruf yolu bir kuralla çelişirse KURAL kazanır.
1. Tur başı tek çağrı: `bash invest/tur_basi.sh A` (git pull, hesap kilidi, DURDUR, saat, DURUM ilk 60 satır, DONGU son 30, son paylaşım saatleri, aktif + operasyon dersleri, periyot uyarıları, bugün/yarın takvimi, gündem, vadeli/faiz/dolar). Çıkış 2 = kilit, 3 = DURDUR → dur. Ayrı ayrı cat/grep/tail yapma.
2. Kart yayını tek çağrı: `bash invest/yayinla_gorsel.sh g/<dosya>.jpg` (commit + pull --rebase + push + raw URL 200 kontrolü, 3 deneme). "OK" yazmazsa görselsiz tweet atılmaz (kural aynı).
3. Tweet sonrası kayıt tek çağrı: `CS=<oturum linki> python3 invest/kayit.py --saat .. --tur .. --konu .. --duzen .. --buffer .. --dosya .. --gorus evet --dongu "<kaynaklar ve rakamlar>" [--hak serbest|ayrilan|yok] [--periyot sozluk:X-A]` → DURUM sayacı + KULLANILAN + Son 3 düzen + DONGU + performans.md + performans_veri.csv + periyot + commit/push. DONGU içeriği (kaynaklar, tek kaynaklılar, hatalar) aynı ayrıntıda yazılır.
4. Paralel çağrı: birbirine bağlı olmayan aramalar (WebSearch x2-3), Yahoo + git + periyot gibi işler aynı mesajda paralel. Gereken bütün ertelenmiş araçlar TEK ToolSearch'te yüklenir (Chrome çekirdek seti + Buffer create_post birlikte).
5. Okuma ekonomisi: DEVIR_TAM ve skill kopyaları baştan okunmaz (kural 18); gerekirse `grep -n` ile ilgili satır. Düzenlenen dosya tekrar okunmaz. Büyük araç çıktıları (Buffer metrikleri, uzun sayfalar) dosyaya yazılıp python/jq ile süzülür; sohbete dökülmez. ta2 çıktısı dosyaya, yalnız gereken satırlar grep'lenir (tam test zorunlu olan teknik kontrollerde dosyanın tamamı yine okunur; kural aynı).
6. Arama ekonomisi: WebSearch önce "standard"; "extended" yalnız sonuç zayıf/eski/çok yeni olayda (kural aynı: 2 kaynak). Bir aramada iki kaynak çıktıysa ek arama yok. Hazırlık turunda bulunan beklentiler `/tmp/hazir_*.py` ve DONGU'dan okunur, yayın turunda yeniden aranmaz.
7. Chrome ekonomisi: önce `get_page_text` (metin), olmazsa ekran görüntüsü; okumak için `scale: 0.5`, Enes'e gidecek görüntüde tam çözünürlük + `zoom` grafik alanı. Birden çok tıklama/gezinme `browser_batch` ile tek çağrıda. PDF'de doğrudan sayfa küçük resmine tıkla.
8. Buffer ekonomisi: tekrar kontrolü `list_posts first 5` metriksiz; metrikler yalnız sabah görevinde, `includeMetrics` sonucu dosyaya yazılıp `ders_analiz.py`/python ile işlenir.
9. Kart kontrolü: kart bir kez Read ile bakılır; değişmediyse tekrar okunmaz. Bilinen sorunlu düzenler (skor/bento + logo) baştan seçilmez (O-007).
10. Enes'e mesajlar: istenen bölümler aynen (tweet metni + "Ne anlama geliyor?" 3-6 madde); tekrar ve uzun önsöz yok.
11. Zincir mesajı kısa şablonla (kural 18); her tur mesajında yalnız değişen bilgiler (konu, saatler, son 3 düzen) güncellenir.

## 16. Uzun görüş yazısı (kesin kural 32)
UZUN GÖRÜŞ YAZISI (kesin kural 32, Enes 17.11 21:13, örnek: "GÜNCELLENMİŞ $NBIS DÜŞÜNCELERİM" metni, invest/ORNEKLER.md bölüm 21): arada sırada (haftada 2-3, periyot.py uzun_gorus) tek uzun tweet. Konu: portföy, ilgi listesi ya da büyük yapay zekâ/yarı iletken/bulut şirketi; tercihen duyarlılığın sert değiştiği, çok konuşulan ama yanlış anlaşıldığını düşündüğümüz bir hisse. Yapı TEK DEĞİL: ÇERÇEVE HAVUZU (Enes 17.11 21:30: "farklı yapılardan olabilir, hep aynı yaparsan hepsi aynı olur, çare bul"): her uzun yazı aşağıdaki çerçevelerden BİRİYLE yazılır; son 3 uzun yazıda kullanılan çerçeve tekrar edilmez (DURUM.md "Uzun yazı çerçeveleri" satırı), aynı ticker 30 gün içinde yeni gelişme olmadan tekrar yazılmaz. Başlık, paragraf sayısı (5-10), açılış biçimi ve kapanış cümlesi de her seferinde değişir.
A) GÜNCELLENMİŞ DÜŞÜNCELER (duyarlılık dönüşü; Enes'in NBIS örneği): ne değişti → haklı endişeler → iyi giden taraf → takaslar → zamanlama → yönetimin göstermesi gerekenler → sonuç. Başlık örn. "GÜNCELLENMİŞ $X DÜŞÜNCELERİM".
B) BOĞA VE AYI: en güçlü 3 boğa argümanı ve en güçlü 3 ayı argümanı (her biri rakamla), sonra hangisinin daha ağır bastığına dair kendi tartımız. Başlık örn. "$X: İKİ TARAFIN DA HAKLI OLDUĞU YERLER".
C) TEK RAKAMIN HİKÂYESİ: şirketi tek bir metrik üzerinden anlatmak (brüt marj, backlog, müşteri başına gelir, serbest nakit); metriğin geçmişi, neden önemli, ne olursa ne demek. Başlık örn. "$X'İ ANLAMAK İÇİN TEK BİR RAKAM".
D) İKİ ŞİRKET, AYNI SORU: iki rakip aynı soruya göre karşılaştırılır (büyüme, marj, değerleme, risk); hangisi hangi senaryoda öne çıkar. Başlık örn. "$X MI $Y Mİ: AYNI PAZARDA İKİ FARKLI YOL".
E) TEZ KONTROLÜ: bir şirketin uzun vadeli tezinin 4-5 maddesi tek tek bugünkü verilerle kontrol edilir (güçlenen / zayıflayan / henüz belli değil). Tutmayan eski tahmin anılmaz (kural 23); maddeler bugünkü durum olarak yazılır. Başlık örn. "$X TEZİNİN 5 MADDESİ BUGÜN NEREDE".
F) KALABALIĞIN GÖZDEN KAÇIRDIĞI: piyasanın konuştuğu konu yerine bizce asıl önemli olan tek nokta; neden gözden kaçtığı ve rakamlarla neden önemli olduğu. Başlık örn. "$X'TE KİMSENİN KONUŞMADIĞI KONU".
G) DEĞER ZİNCİRİ: bir olayın (bilanço, ihracat kuralı, büyük sözleşme) zincirdeki etkisi: tedarikçiler, müşteriler, rakipler, enerji/altyapı; kim kazanır kim kaybeder. Başlık örn. "BU GECEKİ RAKAMLAR ZİNCİRDE KİMİ ETKİLER".
H) 12 AYLIK ÜÇ SENARYO: kötü / baz / iyi senaryo, her birinin tetikleyicisi ve izlenecek gösterge (senaryo dili, hedef fiyat yok, al/sat yok). Başlık örn. "$X İÇİN ÖNÜMÜZDEKİ 12 AYDA ÜÇ YOL".
I) YÖNETİM VE SERMAYE: yönetimin son 1-2 yıldaki kararları (geri alım, seyreltme, satın alma, capex), söyledikleriyle yaptıkları. Başlık örn. "$X YÖNETİMİ PARAYI NEREYE HARCIYOR".
J) TARİHTEN BENZER DÖNEM: bugünkü durumun geçmişteki benzer bir dönemle (döngü, aşırı yatırım, teknoloji geçişi) karşılaştırılması; benzerlik ve farklar rakamla. Başlık örn. "$X VE 20XX'TEKİ BENZER DÖNEM".
Seçim: konuya en uygun ve son 3'te olmayan çerçeve. DONGU satırına "çerçeve: B" yazılır; DURUM.md "Uzun yazı çerçeveleri: son 3 = ..." güncellenir. Ders sistemi (kural 26) çerçeveleri ayrıca ölçer (performans_veri.csv konu sütununa "[B]" öneki). Her rakam 2 kaynak (tek kaynaklı rakam yazılmaz). YASAK: al/sat tavsiyesi, "aldım/alım yapıyorum", pozisyon/ağırlık, hedef fiyat, emoji, hashtag, link, soruyla bitirme, etiketli görüş girişi ("Benim okumam:" vb.), deyim/mecaz yerine sade dil (kural 30), tutmayan eski tahmin (kural 23). "Bence" birkaç kez olabilir ama tekrar eden kalıp olmasın. Kart: editoryal ya da panel (son 3 düzen kuralı). Zaman: 21-24 ya da 12-15 dilimi (D-003). Tür UZUN-GORUS; DONGU ve performans_veri.csv'ye yazılır (ders sistemi bu türü ayrıca ölçer).

## Her şey bu sohbete (kesin kural 29, Enes 17.11: "her şeyin bu sohbete gelmesi lazım")
- 14 sabit görev bu sohbette send_later ZİNCİRİDİR (bulut cron'ları kapalı). Zincir mesajı çalışınca İLK İŞ `python3 invest/sonraki.py <anahtar>` → verdiği zamana, verdiği adla ve AYNI mesajla send_later (list_triggers'ta aynı adlı bekleyen varsa kurma); sonra `invest/gorevler/_ORTAK.md` + `invest/gorevler/<anahtar>.md` harfiyen. `python3 invest/sonraki.py hepsi` bütün zincirlerin sıradaki zamanını verir.
- Otomatik tur, hazırlık/yayın/analiz görevleri de bu sohbette send_later; Enes'e giden her şey SendUserMessage / SendUserFile.

## 17. Sistem tutarlılığı (kesin kural 36)
SİSTEM DENETİMİ VE TUTARLILIK (kesin kural 36, Enes 17.11 21:46: "tüm sistemi araştır, çok detaylı düşün, tamamen geliştir"). Denetimde bulunan çelişki ve boşlukların çözümü (hiçbir kural kaldırılmadı; çelişkide en yeni tarihli kural geçerli ilkesi uygulandı):
a) TUR SIKLIĞI ve GÜNLÜK ADET: otomatik tur zinciri 20-40 dk aralıkla çalışmaya devam eder (16.11 kuralı), ama TWEET ATMA kararı DERSLER D-002/D-003'e (Enes onayı 17.11 17:18, daha yeni) bağlıdır: sistem tweeti günde en çok 15 (`periyot.py kontrol tweet_gunluk`), 18-21 arası en çok 2; hedefe ulaşıldıysa ya da değerli konu yoksa tur paylaşmadan geçer ve zamanı karne/aday/uzun yazı hazırlığına kullanır. GÜNE ÖZEL İSTİSNA: Enes'in o güne verdiği adet kuralı (ör. 17.11 15:23 "01:00'e kadar 10 tweet") geçerliyse o gün tweet_gunluk sınırı yerine o kural uygulanır (Enes talimatı > onaylı ders). Enes'in istediği tweetler ve bilanço/veri yayınları her zaman atılır (sayaca yazılır, sınıra takılmaz). tur_basi.sh "BUGUN SISTEM TWEETI" satırı bunu gösterir; kayit.py her tweette `tweet_gunluk` sayacını otomatik artırır.
b) GÜNE ÖZEL KURALLAR ve SÜRESİ: DURUM.md'deki "BUGÜNLÜK KURAL" bloğu yalnız başlığındaki tarih için geçerlidir; kayit.py başka günde sayacı düşürmez; sabah kontrolü (09:00) önceki güne ait blokları DURUM.md'den siler ve DONGU'ya "bugünlük kural süresi doldu" yazar.
c) SKILL ile KOPYA: hesaptaki skill'ler Enes kartları kaydettikçe güncellenir; kaydedilmemiş bir öneri olabilir. Bu yüzden skill ile invest/skills/ kopyası ya da DEVIR_TAM kesin kuralları çelişirse KOPYA ve en yeni kesin kural geçerlidir. Her görev skill'i yükledikten sonra çelişki şüphesinde ilgili kopya bölümünü grep ile okur.
d) GÖREV ÇAKIŞMASI (tek oturum sırayla çalışır): bilanço/veri YAYIN görevi ile ağır görevler (teknik analiz, uzun yazı, karne) çakışırsa yayın önceliklidir. Bir YAYIN görevi 60 dk içinde başlayacaksa ağır görev zaman kutusuna girer: yayından en az 15 dk önce bitecek şekilde kısaltılır (teknik analizde portföy 4s tek görüntü + KARAR satırları, adaylar 2'ye iner, rotasyon kısalır; atlanan kısım bir sonraki çalışmaya not edilir). Kapanış gibi kısa görevler yayından önce sıraya girerse 10 dk içinde biter.
e) KART DÜZENLERİ (O-007 eki): isi ve siralama 17.11 21:55'te düzeltildi (siralama negatif değerleri sıfır ekseniyle çizer; isi logoya çarpan ticker yazısını gizler, rakamı kalan yüksekliğe sığdırır; LOGO_BUYUT 1.8 korunur). Yeni kart düzeni kullanmadan önce Read ile tek bakış zorunlu kalır.
f) ÖLÇÜM FARKI: ta2.py ile TradingView arasında %2'den büyük fark olursa (ör. 17.11 DOCN 4s Supertrend ta2 91,4 SAT / TV 73,30 AL) TradingView esas; fark DONGU'ya "TA-FARK" etiketiyle yazılır, Pazar raporu farkların sık olduğu göstergeyi inceler.
g) DENETİM DÖNGÜSÜ: her Pazar performans raporundan sonra kısa sistem denetimi: (1) bütün zincirler bekliyor mu (sonraki.py hepsi vs list_triggers), (2) DURUM.md 100 satırı aştı mı (eski bölümler arsiv/'e), (3) HATA_GUNLUGU ve TA-FARK satırlarından tekrar eden hata var mı (varsa O-xxx operasyon dersi), (4) skill kopyası ile DEVIR_TAM kesin kurallar listesi aynı numaraya kadar mı. Sonuç Enes'e 3-5 madde.

## 18. Teknik analiz yok (kesin kural 37)
TEKNİK ANALİZ KALDIRILDI, TEMEL ANALİZE YOĞUNLAŞ (kesin kural 37, Enes 17.11 22:17: "teknik analize bakmıyoruz bir daha, onunla alakalı her şeyi kaldır, onun yerine temel analize daha da yoğunlaş").
- Kaldırılan: 18:00 ve 23:30 teknik kontrol zincirleri (devre dışı), TradingView ve ekran görüntüleri (kural 27), teknik tweet taslakları, gösterge rotasyonu, çizimler (kural 31), ta_ek ve seviye karnesi (kural 33), KARAR'ın teknik ayağı (kural 35), key levels tweetindeki destek/direnç seviyeleri, turlardaki ta2 portföy taraması, TA-FARK (36f). ta2.py, ta_ek.py, seviye_takip.csv repoda arşiv olarak durur, KULLANILMAZ. Kural 12, 27, 31, 33 ve 30/35/36'nın teknik kısımları geçersiz.
- Yerine: her ABD işlem günü 18:00 TEMEL ANALİZ görevi (zincir temel1800, gorevler/temel1800.md): haber/8-K/Form 4/analist revizyonu taraması, günde en az 2 karne, tez kartı kontrolü (tez_kartlari.md), değerleme bölgeleri (kendi 3 yıllık bandı + akran + ters DCF; ucuz/adil/pahalı fiyat aralığı), temel KARAR tablosu, her gün 2-3 yeni aday tam karneyle, adayların en zayıf 2 portföy hissesiyle kıyası, özet tablo. Ben olsam notları değerleme bölgesi ve tez durumuna dayanır, grafik seviyesine değil.
- Key levels 10:30 görevi: seviye yok; "günün başlıkları" tweeti (takvim, vadeliler yönü, bilanço/veri beklentileri, kural 25 yorum) + takvim güncelleme + hazırlık/yayın görevleri.
- Turlarda tweetten sonra portföy hisselerinde haber taraması (ta2 yerine).
- Tweetlerde grafik/teknik görüş yok; görüş temel veriye dayanır.

## Enes'in teknik analizinden tweet (kesin kural 38)
ENES'İN TEKNİK ANALİZİNDEN TWEET (kesin kural 38, Enes 17.11 22:30: "artık teknik analizi ben sana atacağım, sen de tweet yazım kurallarına bakıp sade dilde, mecaz kullanmadan yazacaksın ve bana tweeti yollayacaksın").
- Enes teknik analizini (metin, sesli not ya da grafik görüntüsü) atınca: Claude kendi teknik analizini YAPMAZ, gösterge/seviye EKLEMEZ, Enes'in seviye ve görüşlerini değiştirmez; yalnız onları tweet diline çevirir.
- Yazım kuralları aynen: arkadaşına anlatır gibi sade cümle; DEYİM/MECAZ YOK ("hikâye değişir/biter", "resim bozulur", "asıl sınav", "kapı açılır", "nefes alıyor", "ters köşe" vb. yerine düz ve ölçülebilir cümle: "69'un altında günlük kapanış gelirse düşüş devam edebilir"); terimler sade (FVG = boşluk, order block = alıcıların daha önce toplandığı bölge, Supertrend = trend göstergesi); etiketli giriş ve paragraf başında "X şu:" yok; emoji, hashtag, mention, link yok; soruyla bitmez; okura emir kipi ve al/sat tavsiyesi yok ("ben şuradan eklerim" Enes'in kendi dili olarak kalabilir, "alın" yok); "aldım", portföy, tutar, ağırlık yok; Anthropic adı geçmez.
- Grafikte okunamayan değer uydurulmaz; eksik ya da çelişkili bir şey varsa tweet yine yazılır, altına Enes'e tek cümle not.
- Çıktı: Enes'e SendUserMessage ile kopyalanmaya hazır tweet metni (gerekirse 1 kısa alternatif). Claude bu tweeti PAYLAŞMAZ, Buffer'a göndermez; Enes kendisi atar. DONGU'ya "- SS:DD ENES-TA-TASLAK: <ticker>" satırı.

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
- NETLEŞTİRME (Enes 18.11 01:05): detay tweetleri için BEKLEME YOK. Bilanço ne zaman açıklanırsa açıklansın, belgeler (bülten, CFO yorumu, sunum, 10-Q) ulaşılabilir olduğu anda analiz tweetinden sonra başlar; gece bilançolarında da 01:00-09:00 paylaşım yasağı bu tweetler için UYGULANMAZ (kural 16 gece istisnası gibi). Tweetler arası 15-25 dk. Ertesi sabaha bırakılmaz. Tweetler arası 20-30 dk; 18:00-21:00 dilimine düşen 21:00 sonrasına kayar; görüşme tweetleriyle (kural 40) sırayla ve iç içe değil.
- KURULUM: bilançonun YAYIN görevi (ya da 10:30 günün başlıkları görevi) "Detay: <T>" send_later görevini kurar (aynı ad varsa kurma); görev ilk tweeti atar, kalanları "Detay: <T> (2)" ... zinciriyle kurar ve her mesaja taslak + kaynak yazar. DONGU'ya her tweet için "- DETAY: <T> <konu>"; `tur_basi.sh` dün/bugün bilançosu olup DETAY satırı 2'den az olanları "EKSİK DETAY" diye yazar. Bu tweetler Enes isteğidir; günlük tweet sınırına takılmaz.

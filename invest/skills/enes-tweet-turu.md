---
name: "enes-tweet-turu"
description: "Enes Uludağ'ın X hesabı için otomatik paylaşım turu, Enes'in istediği tweet veya 13F tweeti hazırlanıp Buffer'dan atılırken kullanılır: kontrol listesi, kaynak, yazım, kart ve kayıt kuralları."
---

> **KURAL 61 (23.11, ÖNCE BUNU UYGULA):** Bu skill ile yazılan her içerik ayrıca `enes-analiz-kalitesi` skill'ine (yoksa `invest/skills/enes-analiz-kalitesi.md`) uyar: konuya özgü mercek, veri kartı, tarihsel karşılaştırma ve senaryo disiplini, zorla bağlantı ve terim yığını yok, uzunluk tavanı. Yayından önce `python3 invest/kalite.py kontrol --tur <TUR>` (1 = atma), atınca `kalite.py kaydet --tur <TUR>`. Bu dosyadaki daha uzun/esnek uzunluk ifadeleri kural 61 tavanlarıyla sınırlıdır.


> **KURALLAR (23.11 20:50, kredi tasarrufu):** Bu dosyanın başındaki "!!!" kural blokları kelimesi kelimesine `invest/KURALLAR_TAM.md`'ye taşındı (hiçbiri silinmedi). Güncel kısa liste `invest/KURAL_DIZINI.md` (tur_basi.sh basar). Ayrıntı gerekince ilgili kural grep ile açılır.

# Enes tweet turu

Repo: `/home/claude/kontra-gorsel/invest` (GitHub enesuludg6-debug/kontra-gorsel). Ayrıntı ve geçmiş için başvuru dosyaları: `DEVIR_TAM.md` (tüm kurallar, portföy, adaylar), `DEVIR_OZET.md`, `ORNEKLER.md` (beğenilen tweet kalıpları), `DONGU.md` (her paylaşımın kaydı), `temel_karne.md`. Bu skill ile DEVIR_TAM çelişirse EN YENİ tarihli kural geçerlidir; yeni kural gelince ikisi de güncellenir.

Her zaman Türkçe yaz. Enes'e giden mesajlar da Türkçe.

Hesabın amacı (her şeyin üstünde): en iyi getiriyi yakalamak ya da en bilgili görünmek değil, GÜVEN ve İYİ İÇERİK. Doğru olmayan rakam yerine eksik tweet; tutmayan tahminden bahsedilmez, yalnız doğru çıkanlar (kural 23); abartı ve heyecan yok. Hedef okur ABD borsasını az bilen biri: kısa, sade, anlaşılır. X hesabı @enes1050392 (Enes Uludağ, EnesInvestUS).

Bilanço önizleme/rakam/analiz ve 13F serisi için `enes-bilanco-13f`, portföy notları (18:00 ve 23:30 görevleri yok, kural 44) ve temel karne için `enes-portfoy-analiz` skill'ini de yükle.

## 1. Tur başı kontrol (sırayla)

1. `ReadNotifications` (bildirim varsa), sonra `cd /home/claude/kontra-gorsel/invest && git pull -q`.
2. `invest/DURUM.md` ve `tail -n 30 DONGU.md` oku (DEVIR_TAM'ı baştan okuma, kural 18): satır başında tek başına `DURDUR` varsa HİÇBİR ŞEY yapma, yeni tur kurma.
3. Son OTOMATİK paylaşım saati: 20 dakikadan yeniyse paylaşma; kalan süreye göre 20-40 dk sonrasına aynı mesajla tur kur. Enes'in istediği tweet hemen atılır (o 20 dk kuralına girmez ama sonraki otomatik turu en az 20 dk sonraya kaydır).
4. Saat 01:00-09:00 TSİ arasıysa paylaşma (önceden bilinen açıklama hariç), 09:05'e tur kur.

## 2. Konu seçimi (öncelik sırası)

0. KONU FİLTRESİ (kesin kural 46, Enes 18.11 17:12): yalnız YAPAY ZEKÂ (çip, bellek/depolama, ağ, bulut/neocloud, veri merkezi enerjisi, yapay zekâ yazılımı/siber güvenlik), UZAY ve NASDAQ (Nasdaq 100, büyük teknoloji, endeks) + bunlara etkisiyle makro (Fed, faiz, enflasyon). Perakende/tüketim (Target, Walmart, Lowe's, HD, TJX...), banka, sanayi, ilaç, konut, enerji/emtia ALAN DIŞI: tweet yok.
0c. KURAL 74 UZMAN DİLİ (Enes 24.11 17:39): her tweet en az iki uzmanlık izi (U1 sektöre özgü ölçü, U2 belge satırı, U3 görünür hesap, U4 kesin emsal, U5 ikinci derece etki, U6 beklenti yapısı) taşır; skill enes-uzman-dil.
0b. KURAL 73 KONU KAPSAMI (Enes 24.11 16:39: "sadece portföy haberleri koy demedim; yapay zekâ ile alakalı, portföyümü ilgilendirecek ya da portföyümle aynı sektörde, aynı tarafta olan tüm hisseler hakkında haber ve bilanço paylaşabilirsin"): tur yalnız portföy hisselerini taramaz. Evren = (a) yapay zekâ ile ilgili HER hisse, (b) portföyü etkileyen her gelişme (müşteri, tedarikçi, rakip, makro), (c) portföyle aynı sektör ve aynı tedarik zincirindeki tüm hisseler (ör. VRT için güç/soğutma: ETN, GEV, Schneider; AVGO için ağ/özel çip: MRVL, ANET, CRDO, ALAB; DOCN/NBIS için bulut/neocloud: CRWV, ORCL, IREN; SITM/CBRS için çip: NVDA, AMD, TSM, MU; RKLB için uzay: ASTS, LUNR, PL). Bu evrendeki şirketlerin haberleri ve BİLANÇOLARI paylaşılabilir. Son dakika taraması bu geniş evrende yapılır; portföy hissesinde haber varsa yine turun ilk tweeti o olur (kural 57). Kural 46 alan dışı listesi (perakende, banka, ilaç vb.) aynen geçerli.

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

- KURAL 54-H (Enes 27.11 19:30: "'risk masada kalır.' böyle ibareler istemiyorum, çok yapay zekâ yazmış gibi"): süslü mecaz ve vecize kapanış YASAK: "risk masada kalır", "masaya geldi", "denklem", "terazi", "ibre", "oyunun kuralları", "kartlar yeniden dağıtılıyor", "top X'in sahasında", "rüzgar arkasında", "tabloyu bozar", "pusula", "fırtına öncesi", "perde aralandı", "söz artık X'te". Kapanış düz ve ölçülebilir: ne olursa ne düşünürüm/yaparım, rakamla (ör. "Oran 1'in altına inene kadar temkinliyim.", "Faiz %5'i aşarsa bu yükseliş zayıflar."). yasak.py 54-H yakalar.
- Arkadaşına anlatır gibi, sade ve doğal cümleler. Terimleri sadeleştir: EPS = hisse başı kâr, guidance = şirketin verdiği tahmin/yönlendirme, capex = yatırım harcaması.
- Şirketi ilk geçtiği yerde ne iş yaptığıyla tanıt. Ticker'lar gerektiğinde $TICKER.
- İlk satır durdurmalı: rakam, tezat ya da net tespit.
- KESİN KURAL 25 (Enes 17.11 16:51, "insanlar bizi haberlere ulaşmak için takip ediyor ama asıl takip ettiği şey bizim fikirlerimiz, olaylara dair düşüncelerimiz"): Haberi vermek yetmez; her haber ve veri tweetinin ağırlığı YORUMDUR (yaklaşık üçte biri haber, üçte ikisi düşünce). Okur tweeti bitirdiğinde şu sorulara cevap almış olmalı: (1) Bu ne demek, sade dille? (2) Neden şimdi önemli, büyük resimde neye işaret ediyor (büyüme, enflasyon, tüketici, şirket kârları, yapay zekâ döngüsü)? (3) Fed ne düşünür, faiz beklentisi nasıl değişir (FedWatch/vadeli fiyatlama, 2 kaynak)? (4) Piyasaya, sektörlere ve takip edilen hisselere etkisi ne? (5) Bizim net düşüncemiz ne? Makro veri tweeti TEK tweet olsa bile bu beşini içerir; ayrı 'sonuç' ve 'etki' tweeti yerine tek, yorumlu tweet. Bilanço rakam tweeti yorumsuz kalır ama 15 dk sonraki analiz tweeti bu beş soruyu cevaplar. Görüş etiketsiz, düz cümleyle (kural 11), al/sat yok, tahmin dili ölçülü.
- Görüş zorunlu (bilanço rakam tweeti hariç). Enes'in en sevdiği tarz: haberi tekrar etmek yerine arkasındaki yapıyı anlatan, olayları birbirine bağlayan "bağlam + görüş" (ORNEKLER 18).
- CÜMLE ORTASI ETİKET YASAK (Enes 18.11 17:26): "Yine de yön net:", "Mesele şu:", "Fark şu:" gibi iki noktayla açılan ara cümleler yok; düz cümle kur.
- ARAÇ KONTROLÜ ZORUNLU (kural 11-B, Enes 18.11 14:55): her create_post'tan önce `python3 invest/yasak.py`; çıkış 1 = atma.
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
- Enes'in portföyündeki hisseleri (DEVIR_TAM bölüm 1; şu an DOCN RKLB SITM AXON CBRS VRT AVGO NBIS; NBIS 20.11 eklendi) etkileyen büyük hareket varsa ayrıca kısa "ben olsam" notu.
- Her turda tweetten sonra portföy taraması (kural 37): 7 portföy hissesinde son haber/8-K/Form 4/analist revizyonu; teze dokunan bir gelişme varsa Enes'e kısa "ben olsam" notu (değerleme bölgesi + tez durumu). Değişiklik yoksa mesaj zorunlu değil.

Tarayıcı: Enes'in X hesabına ve x.com'a HİÇBİR ŞEKİLDE girilmez. Chrome yalnız tradingview.com ve haber/birincil kaynak okumak için (yeni sekme, get_page_text, iş bitince sekmeyi kapat, TradingView sekmesine dokunma). Form, giriş, abonelik, yorum, paylaşım yok; çerez bannerında en gizli seçenek.

Hata durumları: Bash "classifier no verdict" → 1 kez tekrar, olmazsa o tur paylaşma, 5-10 dk sonrasına kur. WebFetch PROVENANCE_REQUIRED → tekrar deneme, WebSearch. Buffer hata → 1 kez tekrar, olmazsa DONGU'ya yaz ve atla. Push reddi → görselsiz tweet atma. Buffer aylık ~1000 gönderi; 900'ü geçerse Enes'e söyle.

## 7. Kayıt ve sonraki tur

- KURAL 47 (Enes 18.11 18:07): her tweetten sonra Enes'e 'Paylaşıldı (SS:DD): TÜR' + metin + ÖĞRETİCİ 'Ne anlama geliyor?' (terimler sade dille, neden önemli, benzer haber nasıl okunur, Nasdaq/portföy bağlantısı, izlenecek 1-2 şey).

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
1. Tur başı tek çağrı: `bash invest/tur_basi.sh <etiket>` (<etiket> = görev mesajındaki HESAP=, şu an A2) (git pull, hesap kilidi, DURDUR, saat, DURUM ilk 60 satır, DONGU son 30, son paylaşım saatleri, aktif + operasyon dersleri, periyot uyarıları, bugün/yarın takvimi, gündem, vadeli/faiz/dolar). Çıkış 2 = kilit, 3 = DURDUR → dur. Ayrı ayrı cat/grep/tail yapma.
2. Kart yayını tek çağrı: `bash invest/yayinla_gorsel.sh g/<dosya>.jpg` (commit + pull --rebase + push + raw URL 200 kontrolü, 3 deneme). "OK" yazmazsa görselsiz tweet atılmaz (kural aynı).
   KURAL 77 (F-007): kart 'LOGO DOGRULANMADI' uyarısı verirse Read ile kontrol; doğruysa `python3 logo_dogrula.py ekle <T>`, yanlışsa logo sil, logosuz çiz.
   KURAL 78 (F-008): haber yazılmamış gün içi hareket için `python3 fiyat_teyit.py <T> <ikinci_%> "<kaynak>"` (ikinci kaynak WebSearch '<T> stock today'); fark ≤0,5 puan net rakam, değilse 'civarı'.
   KURAL 79 (F-009, Enes 24.11 20:29): günün ÇİFT sıradaki sistem tweetleri 'iddia açılışı' (ilk satır ≤12 kelime, birinci tekil şahıs ya da net hüküm, rakamla başlamaz; rakamlar 2. paragraftan); tek sıradakiler mevcut açılış. kalite.py kaydet açılış tipini yazar; kayit.py --konu başına [A:iddia]/[A:normal]. A/B 08.12'ye kadar.
   KURAL 80 (F-010, Enes 24.11 20:29): günde 2-3 ALINTI tweet: büyük şirket/haber hesabının paylaşımına Buffer create_post metadata.twitter.retweet {id: '<id>'} ile, metinde yalnız bizim ek verimiz + kart. id yalnız WebSearch sonucundaki x.com/.../status/<id> bağlantısından; x.com'a girilmez, id tahmin edilmez. --konu başına [ALINTI].
   KURAL 72 (F-004, Enes 24.11 11:36): betik kartla birlikte invest/ altındaki bekleyen her değişikliği (is_defteri.json, logo/, kalite ve kayıt dosyaları) de commit'ler; commit'lenecek bir şey yoksa hata vermez. "PUSH HATA" görülürse DONGU'ya yazılır.
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
- (18:00 zamanlanmış görev kural 44 ile kaldırıldı; aşağıdaki içerik turlarda/istenince:) haber/8-K/Form 4/analist revizyonu taraması, günde en az 2 karne, tez kartı kontrolü (tez_kartlari.md), değerleme bölgeleri (kendi 3 yıllık bandı + akran + ters DCF; ucuz/adil/pahalı fiyat aralığı), temel KARAR tablosu, her gün 2-3 yeni aday tam karneyle, adayların en zayıf 2 portföy hissesiyle kıyası, özet tablo. Ben olsam notları değerleme bölgesi ve tez durumuna dayanır, grafik seviyesine değil.
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

## Günlük adet ve son dakika (kesin kural 48, Enes 18.11 22:13)
[GÜNCEL: kural 86, Enes 25.11 18:08 — hafta içi en az 18 en çok 26, Cmt ve Paz en çok 10; aşağıdaki eski sayılar GEÇERSİZ] Pzt-Cmt günde en az 30 en çok 50 tweet; Pazar 10 tweet. Her turda ilk iş son dakika taraması: WebFetch https://www.newsquawk.com/headlines (gün içi hisse başlıkları, analist hedefleri, ön piyasa hareketleri) + WebSearch extended (portföy ve ilgi listesi isimleri). 2 kaynaklı yeni hisse haberi varsa önce o atılır (haber + yorum, kural 25). Turlar 15-25 dk arayla, her turda 1-2 tweet; zamanlı görevlerin arası boş bırakılmaz. Kural 42'deki 40 üst sınırı 50 oldu.

## Paylaşım saati ve günlük adet (kesin kural 42)
[GÜNCEL: kural 86, Enes 25.11 18:08 — hafta içi en az 18 en çok 26, Cmt ve Paz en çok 10; aşağıdaki eski sayılar GEÇERSİZ] PAYLAŞIM SAATİ VE GÜNLÜK ADET (kesin kural 42, Enes 18.11 01:13: "sabah 11'de başla artık turlara ve en geç gece 2'de bitir; pazartesi-cumartesi günde en az 30, en fazla 40 tweet atabilirsin; pazar günleri ise en fazla ... tweet").
- SAAT: tweet/tur penceresi 11:00-02:00 TSİ. Paylaşım günü 02:00'de biter (kayit.py ve bugünlük sayaçlar buna göre). 02:00-11:00 arası tweet yok; istisna yalnız saati belli bilanço/veri rakam yayınları (kural 16) ve kural 41 bilanço detayları (Enes 01:05: "beklemeden"). Sabah 09:00 kontrolü tweet atmadan çalışır; 09:05 vadeli tweeti ve 10:30 günün başlıkları 11:00'e kayar (günün başlıkları vadelileri de içerir).
- ADET: Pazartesi-Cumartesi günde EN AZ 30, EN ÇOK 40 tweet (Enes istekleri, bilanço rakam/analiz/detay/görüşme tweetleri dahil sayılır; 40'ı yalnız Enes isteği aşabilir). Pazar: alt sınır yok, üst sınır Enes rakam verene kadar 40. Bu kural D-002 (12-15) ve kural 36a'daki 15 sınırının yerine geçer; 18-21 dilimi sınırı KALDIRILDI (Enes 18.11 01:18).
- TEMPO: 15 saatlik pencerede 30-40 tweet (ortalama ~25 dk'da bir ama aralık SERBEST, aşağıya bak). Otomatik tur zinciri 11:15'te başlar; her tur en az bir tweet atar (2 kaynak ve kural 25 aynen; değerli konu yoksa menü: eğitici, karşılaştırma, bir yıl önce, 13F, uzun görüş, analist notu, içeriden alım, sektör, emtia/kripto/dolar). `tur_basi.sh` "BUGUN SISTEM TWEETI" satırı hedefi ve kalan süreye göre gereken tempoyu gösterir; 01:00'da 30'un altındaysa son saatte aralık 12-15 dk'ya iner.
- Kalite korunur: tekrar yok, aynı ticker 3 saatte bir, 2 kaynak, kural 23/25, kart son 3 düzen.
- ARALIK SERBEST (Enes 18.11 01:15: "tweet aralarında kaç dakika olacağı tamamen sana kalmış, 1 dakika da olabilir 1 saat de; o kuralı kaldır, illa belli bir aralık olmasına gerek yok"): tweetler arasında SABİT BİR ARALIK YOK. Eski "son otomatik paylaşımdan 20 dk geçmediyse paylaşma", "20-40 dk", "18-28 dk", detay/görüşme serilerindeki "15-25 / 20-30 dk" aralıkları kaldırıldı. Aralığı haberin önemi ve tazeliği, günün 30-40 hedefi ve kalan süre belirler: son dakika hemen, birbirine bağlı seri tweetler arka arkaya ya da birkaç dakika arayla, sakin saatlerde daha uzun. Yalnız aynı konu/ticker tekrarı kuralları kalır; 18-21 dilimi sınırı da kaldırıldı (Enes 01:18). Bir sonraki tur zamanını her turda Claude seçer (1-60 dk; gerekirse daha uzun).
- 18-21 SINIRI KALDIRILDI (Enes 18.11 01:18): 18:00-21:00 arasında tweet sınırı YOK; D-003 ve görüşme/detay tweetlerindeki '18-21 dilimine düşen 21:00 sonrasına kayar' kuralları geçersiz.

## İş defteri ve sohbet devri (kesin kural 43)
İŞ DEFTERİ VE SOHBET DEVRİ GÜVENCESİ (kesin kural 43, Enes 18.11 01:29: "başka sohbete geçince bazı şeyler o tarafa geçmedi çünkü o sohbette hiç NVDA bilançosunu konuşmamıştık; sorunu tamamen anla ve çöz, bundan sonraki sohbet değişikliklerinde de hallolsun").
- SORUNUN KÖKÜ (18.11 tespiti): (1) devam eden işlerin durumu (ne yapıldı, ne bekliyor, ne iptal) yalnız sohbet geçmişinde ve görev mesajlarındaydı; yeni sohbet bunları göremez. (2) Elle yazılmış "bekleyen görevler" listesi eksik/yanlış kaldı. (3) Enes'in bir cümlesi fazla geniş yorumlandı ("bu bilanço için atman gereken bir şey kalmadı" = yalnız DETAY tweetleri; görüşme tweetleri de yanlışlıkla iptal edildi) ve bu yanlış karar kayda geçtiği için yeni sohbet de aynen uyguladı.
- ÇÖZÜM 1 — İŞ DEFTERİ: zamanı belli her tek seferlik iş invest/is_defteri.json'da durur (python3 invest/isler.py). Bilanço takvime girer girmez `python3 invest/isler.py bilanco <T> <YYYY-MM-DDTHH:MM> <acilis_oncesi|kapanis_sonrasi> [görüşme HH:MM]` ile 7 adım eklenir: opsiyon (39), hazırlık, yayın, analiz, detay (41), çağrı (40), beklenen hareket (22n). Veri yayınları ve Enes'in istediği zamanlı işler `isler.py ekle <ID> "<ad>" <YYYY-AA-GGTSS:DD> "<ne>" [--ticker T] [--tur tur|test|tek]` ile (KURAL 76: sıra ad → zaman; betik tarihi doğrular, ad/zaman yer değiştirmişse düzeltir, tarih yoksa reddeder). send_later kurulunca `isler.py durum <id> kuruldu --trigger <trig>`, iş bitince `durum <id> yapildi --not "saat, Buffer id"`.
- ÇÖZÜM 2 — İPTAL KURALI: Enes bir şeyi iptal ettiğinde YALNIZ açıkça söylediği kapsam iptal edilir; birden fazla işi kapsayabilecek cümlede EN DAR yorum alınır. İptal `isler.py durum <id> iptal --soz "Enes'in aynen sözü"` ile yazılır (söz olmadan iptal kaydı reddedilir). İptal edilen her iş Enes'e tek satırda adıyla söylenir; emin olunmayan kısım iptal edilmez ve "X devam ediyor" denir.
- ÇÖZÜM 3 — DEVİR: yeni sohbet (HESAP_DEVRI.md "SOHBET DEVRİ") açık işleri hafızadan değil `python3 invest/isler.py devir` çıktısından kurar; list_triggers ile karşılaştırır, eksikleri kurar; sonra Enes'e açık işleri tek tek (saat + ad) listeler. Eski sohbet "dur" denince görevlerini kapatır ama defter aynen kalır.
- ÇÖZÜM 4 — GÜNLÜK KONTROL: tur_basi.sh her turda `isler.py kontrol` çalıştırır; zamanı geçip yapılmamış iş "EKSIK IS" diye çıkar ve o tur önce onu tamamlar ya da Enes'e yazar. Sabah 09:00 kontrolü `isler.py devir` ile list_triggers'ı karşılaştırır.
- ÇÖZÜM 5 — KONUŞMADAKİ KARARLAR: Enes'in sohbette verdiği her karar (tek bilanço, tek hisse, tek gün için olanlar dahil) ilgili defter satırının "not" alanına ve DONGU'ya aynen yazılır; kalıcı kural ise DEVIR_TAM'a. "Bu sohbette konuşuldu, kayda gerek yok" diye bir şey yoktur.

## 19. 18:00 ve 23:30 analiz görevleri yok (kesin kural 44, Enes 18.11 01:51-01:54)
Yalnız iki zamanlanmış görev kaldırıldı: 18:00 temel analiz (temel1800) ve 23:30 (teknik2330). Kurulmaz, ateşlenirse kapanır. Turlarda karne, tez kartı, ben olsam notları ve diğer temel işler aynen sürer.

## 20. Detaylı analiz yazısı (kesin kural 45, Enes 18.11 07:40)
Bilanço sonrası analiz ve bir hisse üzerine her analiz/uzun görüş yazısı ÇOK DETAYLI ve ÇOK KAYNAKLI olur: 10-15 kısa paragraf, en az 6 bağımsız kaynak (en az 4 tür: şirket belgesi, görüşme, 2+ haber kuruluşu, 2+ analist kurumu, konsensüs/veri sitesi), 13 maddelik içerik sırası ve gönderim öncesi kontrol. Tam yöntem: `enes-bilanco-13f` skill'i 'Detaylı analiz yazısı' bölümü (ve DEVIR_TAM kural 45).

## KURAL 66 — Sonuç takibi (Enes 24.11 09:44)
- Olaydan önce ölçülebilir yorum içeren tweet atıldığı an `isler.py ekle TEST-<T>-<GGAA> ... --tur sonuctakip`; olay açıklanınca o yorumu sınayan analiz tweeti. Bilançoda ANALİZ tweeti testin kalemleriyle açılır (ayrı tweet değil). Ayrıntı: `invest/skills/enes-sonuc-takibi.md` (skill enes-sonuc-takibi).

## KURAL 83 GÜNÜN OLAYLARI LİSTESİ (Enes 25.11 11:11)
83 GÜNÜN OLAYLARI LİSTESİ (Enes 25.11 11:11, örnek: 'Today's Key Events (All EST)' listesi): ABD borsasının açık olduğu her gün 11:00 günün başlıkları görevinin İKİNCİ tweeti (Buffer customScheduled ~12 dk sonra). Biçim: başlık 'Bugünün önemli olayları (TSİ) • GG Ay'; altında saat sıralı satırlar 'SS:DD olay' (TSİ = ET+8 kış / ET+7 yaz; satır başında iki nokta YOK, emoji yok): ABD verileri (PCE, TÜFE, GDP, istihdam, başvurular, dayanıklı mallar, konut, ISM/PMI, tüketici güveni), Fed konuşmacıları, Fed tutanak/Bej Kitap, tahvil ihaleleri (önemliyse); ayrı blok 'Açılış öncesi bilanço' ve 'Kapanış sonrası bilanço' — yalnız kural 46/73 evrenindeki şirketler ($TICKER + ne iş yaptığı 2-4 kelime; enerji/perakende/sanayi yazılmaz; evrende yoksa blok yazılmaz). Saatler 2 kaynak (resmi takvim: BEA/BLS/Census/federalreserve.gov ya da şirket bülteni + bir takvim sitesi; Enes'in gönderdiği liste bir kaynak sayılır). Sonda TEK cümle: günün belirleyicisi ve neden (birinci tekil görüş). Tür GUNUN-OLAYLARI (kalite.py: kalıp muaf, tavan 700). Kart terminal ya da takvim (son 3 düzen kuralı). Tatil/kapalı günde atılmaz; yarım günde kapanış saati satırı eklenir.

## KURAL 84 GRAFİK DOĞRULUĞU + KART3 (Enes 25.11 11:38)
84 GRAFİK DOĞRULUĞU + KART3 (Enes 25.11 11:36-11:38: 6 örneğin hepsi beğenildi; 'grafiklerin gerçekten olduğu gibi konması lazım, mum gerekmez, çizgi olabilir ama grafik gerçekten o şekilde olmalı'): VARSAYILAN KART ARTIK `kart3.py` (tek koyu tema, tek vurgu, sonuç bandı; düzenler: cizgi_olay, esleme, siralama, isi, bilanco, goreli). kart2 yalnız kart3'te karşılığı olmayan özel durumda. Grafik kuralları: (1) veri yalnız ham kaynaktan (Yahoo chart uç noktası günlük kapanış, şirket bülteni, resmi kurum); yumuşatma, ara değer uydurma, nokta atlama, elle düzeltme YOK; (2) çizilen seri kaynakla birebir `kart3.dogrula(seri, kaynak_seri)`; (3) son nokta gerçek son kapanış, kartın alt başlığında 'son veri GG.AA.YYYY' (kart3 otomatik yazar); (4) olay işareti gerçek tarihteki noktaya (gece bilançosunda tepki günü); (5) eksen etiketleri gerçek değer, tarih ekseni gerçek tarih; çizgi grafikte y ekseni sıfırdan başlamak zorunda değil ama kırpma ile hareketi abartmak yok (seri aralığının %3-6 payı); (6) tweet metnindeki her rakam grafikteki veriyle aynı; (7) Read ile bakılır: şekil kaynaktaki grafikle (Yahoo/TradingView'daki görüntü) aynı mı. Mum grafik gerekmez, çizgi yeterli.

## KURAL 85 HİSSE-TAHVİL AYRIŞMA ÖLÇÜSÜ (Enes 25.11 18:02)
85 HİSSE-TAHVİL AYRIŞMA ÖLÇÜSÜ (Enes 25.11 18:02 geliştirme fikrini kabul etti): her tur başında `tur_basi.sh` içinden `python3 invest/ayrisma.py --sessiz` çalışır (Nasdaq 100 % değişimi vs 10 yıllık faiz bp değişimi, Yahoo canlı). SİNYAL (NDX <= −%1 ve 10Y <= −3 bp: hisse ve faiz birlikte düşüyor) -> satış faizle açıklanmıyor, o turun 1. tweet adayı büyüme/risk tweeti; TERS SİNYAL (NDX >= +%1 ve 10Y >= +5 bp) -> büyüme iyimserliği tweeti adayı. Aynı gün aynı sinyal için en çok 1 tweet (ilk görüldüğünde), sonrası yalnız belirgin değişimde. Yazım 54-F: soyut 'X'in yansıması/genel kaçış' YOK; somut: hangi hisseler, ne kadar, faiz kaç bp. Rakam tek kaynak -> 'civarı' (kural 78) ya da 2. kaynak (CNBC/Investing). Kart: haber_dosya (Nasdaq 100 + 10Y/2Y vadeli mini grafik, bugün 5 dk).

## KURAL 86 BEĞENİ + PROFESYONELLİK PAKETİ (Enes 25.11 18:05)
86 BEĞENİ + PROFESYONELLİK PAKETİ (Enes 25.11 18:05 'HEPSİ KABUL', F-012..F-019; veri 351 tweet: sistem ort. 2,3 beğeni, Enes 5,8, portföy 12,7, eğitici 5,8): (a) F-012 GÜNLÜK SAYI (Enes 25.11 18:08 düzeltme): HAFTA İÇİ EN AZ 18, EN ÇOK 26 sistem tweeti; HAFTA SONU (Cmt-Paz) EN ÇOK 10 (eski 48-B 30-50 kalktı). En az 18'e yetişmek için tur aralığı 20-35 dk, turda 1 tweet (güçlü konu varsa 2); 18'in altı ancak gün sonunda (02:00) güçlü konu kalmadıysa, DONGU'ya gerekçe. kalite.py hafta içi 26, hafta sonu 10'da durdurur. (b) F-013 ENES SESİ: sistem tweetlerinin ilk satırı Enes'in kişisel/iddialı tonunda ('Bunu 3 haftadır yazıyorum.', 'Kimse konuşmuyor ama…' değil — 54-F'ye takılmayan, birinci tekil, somut iddia); kibir/hakaret yok. (c) F-014 PORTFÖY DOSYASI günde 2: Enes'in hisselerinden (RKLB, NBIS, AVGO, MU, NVDA, HPE, CRWV, AXON…) derin tweet + kart3 dosya, öncelik 13:00 ve 20-23. (d) F-015 AKŞAM EĞİTİCİ günde 1, 20:00-23:00: 'X nedir, neden önemli, bugün nerede' (tür EGITICI, kalıp E), güncel olaya bağlı. (e) F-016 SAAT: en güçlü tweetler 13, 17, 20-23 slotlarına; 10, 15, 19 ve 00-01 slotlarına yalnız zorunlu/son dakika. (f) F-017 KISA VE TEK FİKİR: ilk satır en çok 12 kelime, metinde en çok 3 farklı rakam (5 üstü hata), en çok 3 paragraf; fazla rakam karta (kalite.py denetler; bilanço rakam/olaylar/keylevels muaf). (g) F-018 HAFTALIK KARNE Cumartesi 20:25 sabit görev `karne` (gorevler/karne.md): YALNIZ TUTAN yorumlar paylaşılır (Enes 18:06 'tutmayanları paylaşma sadece tutanlar'); tutmayanlar yalnız DONGU iç notu, isabet oranı yazılmaz; tutan 2'den azsa atılmaz. (h) F-019 GÜNCELLEME ALINTISI: 2 saatte 2.000+ gösterim ya da 15+ beğeni alan tweete 20-60 dk içinde yeni veri gelirse kendi tweetini alıntılayan kısa güncelleme (günde en çok 2; kural 80 alıntı sayısına dahil değil); Buffer'da alıntı mümkün değilse metinde 'Saat SS:DD tweetine güncelleme:' ile başlar. Ölçüm: 2 hafta, performans_veri.csv beğeni/gösterim ortalaması 2,3'ten yukarı.

## KURAL 98 (Enes 27.11 17:39 'hepsini yeteneklere ekle') — hacim, taslak, biçim
Veri 13-26.11: Enes'in elle attıkları medyan 522, sistem 341 (her saat diliminde); sistem hacmi düşünce medyan 420+'ya çıktı. X kodunda zamanlanmış/yapay zekâ yazımı gönderiye ceza yok; fark hacim (yazar çeşitliliği cezası), kalıp görünüm ve yanıt farkından.
- (a) SİSTEM TWEETİ hafta içi günde 15-20, Cumartesi/Pazar en çok 8 (kural 86'nın 18-26'sının yerine). Yalnız GÜÇLÜ konu: konu_puan ≥75, son dakika, bilanço ya da 2 kaynaklı yeni haber. Zayıf konuda tur TWEETSİZ kapanır, DONGU'ya gerekçe. Sabit veri zincirleri bu sayıya dahil; verisi zayıf haftada atlanır. tur_basi.sh hedefi '15-20' gösterir, 20'de 'UST SINIR DOLDU'.
- (b) ENES-TASLAK hafta içi 6 (11-13, 13-15, 15-17, 17-19, 19-21, 21-24 dilimlerinde birer), Cumartesi 3, Pazar 2. Her biri 1-3 kısa cümle, 'ben' dili, tartışma açan net hüküm, en çok 1 rakam, kart yok. Altına 'Atarsan ilk 1 saatte gelen yanıtlara cevap ver.'. Sayaç 'ENES-TASLAK n/6'.
- (c) BİÇİM ROTASYONU her gün: sistem tweetlerinin en az 3'ü KARTSIZ tek-iki cümle (görselsiz, yalnız metin; Buffer'a asset gönderme), en az 2'si TARTIŞMA AÇAN GÖRÜŞ (karşı görüşü davet eden net iddia; Enes kuralı gereği SORU İŞARETİYLE BİTMEZ), kalanı kartlı analiz. Art arda iki tweet aynı biçimde olmaz. DONGU satırına 'biçim: kartsız | görüş | kartlı' yazılır.
- Ölçüm 04.12: sistem medyanı ≥450 hedef; tutmazsa hacim 12-15'e iner (Enes'e bildir).

## KURAL 99 (27.11): tur akışı
Tur talimatı `invest/gorevler/tur.md` (sabit), sayaçlar `python3 invest/gun_ozet.py`, yayın kapısı `bash invest/yayin_kontrol.sh <TUR> <KALIP> < metin` ('GEÇTİ' olmadan Buffer yok). Sonraki tur send_later mesajı tur.md'deki KISA ŞABLON.


## KURAL 100-101 (Enes 27.11 19:37 'hepsini yap, yeteneklere ekle')
- 100: Buffer create_post/edit_post öncesi hook (buffer_kapi.py) yalnız yayin_kontrol.sh GEÇTİ almış metni geçirir; GEÇTİ sonrası metin değişirse kontrol yeniden. Göndermeden önce Enes gözüyle son okuma: (1) Enes bunu böyle der mi, (2) yapay zekâ kokan cümle var mı, (3) her rakamın 2 kaynağı DONGU'da mı.
- 101: yazmadan önce `python3 invest/ses_ornek.py` (Enes'in kendi en çok okunan tweetlerinden 3 örnek + ses özellikleri; kısa, konuşur gibi, süssüz hüküm). Kural dizini sadeleşti: KURAL_DIZINI.md 52 satır, tek geçerli rakamlar; eskisi KURAL_DIZINI_ARSIV_2711.md. Pazar perfogren SES_ORNEKLERI.md'yi yeniler.


## KURAL 102 (Enes 27.11 23:34: "artık her tweet benim sesimle yazılacak"): İSTİSNASIZ HER TWEET (tur, sabit veri görevi, bilanço, sonuç takibi, alıntı, eğitici, tarihsel) Enes'in sesiyle yazılır. Yazmadan önce `python3 invest/ses_ornek.py`; yayından önce yayin_kontrol.sh içindeki `ses_kontrol.py` (28 kelimeyi aşan cümle, ortalama 18 kelime üstü, rapor dili = DUR). Ses: kısa, konuşur gibi, birinci tekil, süssüz hüküm, kendi davranışını anlatır ("ben ... bekliyorum"). Kural 60/89 (profesyonel, fon yöneticisi) İÇERİK derinliği içindir; KELİME seçiminde Enes sesi önce gelir, çelişirse Enes sesi kazanır.


## KURAL 106 — X NABZI (Enes 28.11 11:08 'ücretsiz halini yap')
X'i hesapsız ve ücretsiz izlemek için WebSearch aracını allowed_domains ["x.com","twitter.com"] ile kullan: arama motorunun dizinlediği herkese açık tweetler (metin, yazar, görüntülenme, yanıtlar) gelir. X'e giriş, x.com WebFetch, otomasyon YOK (Enes'in hesabına sıfır risk). Tur başına en çok 2 arama; takip listesi ve kurallar invest/X_NABIZ.md. Tweet içeriği kaynak değildir, rakam yine 2 bağımsız kaynak; başkasının cümlesi kopyalanmaz.

## KURAL 107 — ENES'İN FAVORİ 4 HESABI (Enes 28.11 11:13 "piyasa fikirlerini çok beğeniyorum, bunlara bak")
Her tur X NABZI'nın 2 aramasından EN AZ 1'i bu 4 hesaptan biri olur (sırayla döner: Shay → Serenity → Venu → Akdağ). Arama: `<hesap adı> <gündem hissesi/tema>` ya da yalnız hesap adı, allowed_domains x.com/twitter.com. Son 3 günden eski tweet alınmaz.

| Hesap | Kim | Neye bakılır | Bizim kullanım |
|---|---|---|---|
| Shay Boloor @StockSavvyShay | Futurum Equities baş piyasa stratejisti, ~466 bin takipçi, büyüme portföyü (YZ altyapı, uzay, drone, fiziksel YZ, YZ enerji) | Gözden kaçan metrik ("piyasa ağaca bakıp ormanı kaçırıyor": NBIS MW başına sözleşme fiyatı, ön ödemeli capex), banka tahminini tek cümlede yorumlama (GS HBM 2026 ~60 mlr $ → 2027 200 mlr $), "%70+ düşenler" listeleri, enerji darboğazı isim listeleri | Açı ve liste formatı. Rakam GS/şirket kaynağından teyit edilir |
| Serenity @aleabitoreddit | YZ/yarı iletken tedarik zinciri analisti (eski RISC-V, YZ araştırmacı), ~808 bin takipçi, "bilinmeyen darboğaz" avcısı | Tedarik zinciri eşleme (CPO lazer: SIVE, LITE, COHR, AAOI, Sumitomo), hiperskaler LTA'ları, düşük çarpanlı hızlı büyüyen küçük şirketler, iddia/yalanlama takibi (SoftBank türbin) | Darboğaz teması ve aday hisse fikri → aday hisseler önce enes-portfoy-analiz puanlamasından geçer. Marjlı/yüksek beta oynar (Ekim'de -%49 düşüş paylaştı): getiri iddiaları ve küçük şirket heyecanı TEYİTSİZ alınmaz |
| Venu @Venu_7_ | Pozisyon trader, temel + teknik, yalnız hisse (opsiyon yok), ~51 bin takipçi | Stage 2 trend, kupa/düşen kama/üçgen formasyonu, 50 günlük SMA testi, Power Earnings Gap (bilanço boşluğu) mumu, kâr realizasyonu notları, tema listeleri (10 yarı iletken) | Teknik açı: formasyon adını kendi grafiğimizle (teknik_pro/formasyon.py) doğrularız. PEG fikri bilanço sonrası tweetlerde "boşluk kapanmadıysa güç" açısı olur |
| Duhan Samet Akdağ @DSAkdag | NCM Investment araştırma, SPK Düzey 3 + Türev lisansı, CFA adayı; Türkçe | Opsiyon yapısı (0DTE payı, iron condor'un endeksi dar bantta tutması), M&A sinyal sırası (8-K → fairness opinion → 13D), Sharpe/risk ayarlı getiri | Türkçe pro dil örneği (rakip/benchmark). Opsiyon/akış açıklayıcı tweetleri (kural 86-d eğitici) için konu kaynağı |

Kurallar (106'nın üstüne):
- Fikir alınır, cümle alınmaz. Onların tweetini çeviri gibi yazmak YASAK. Aynı konuyu kendi verimiz + Enes sesiyle (kural 102) yazarız; açı aynıysa farklı bir rakam ya da karşı görüş ekleriz.
- İsim anılmaz (rakip hesabı büyütmeyiz), tek istisna: Enes'in kendisinin alıntı tweet istemesi.
- Onların "aldım/ekledim" pozisyonu bizim için sinyal değil, konu adayıdır. Enes'e "ben olsam" notunda geçerse: "Serenity X'i darboğaz diye anlatıyor, bizim puan: N/50" biçiminde, kaynaklı.
- Yüksek görüntülenmeli tweetleri (ör. 100 bin+) konu_puan'a +10; DONGU'ya `xnabiz: <hesap> <görüntülenme> <konu>`.
- Her Pazar (perfogren) bu 4 hesabın haftanın en çok görüntülenen 1'er tweetine bakılır: hangi FORMAT tuttu (liste, tek metrik, grafik, karşı görüş) → DERSLER.md'ye 1 satır.

## KURAL 108 — GÜNÜN TEKNİK ANALİZ TWEETLERİ → BİZİM ÇİZİM (Enes 28.11 11:20)
Ne: Takip hesaplarının AYNI GÜN attığı teknik analiz tweetlerini bul, kendi teknik analizimizle karşılaştır, en beğendiğin tweetin ÇİZİM TARZINA benzer (birebir aynı DEĞİL) kendi grafiğimizi çiz, o tarzdaki fikirle görselli tweet at (sistem atar, Buffer).
Hesaplar (TA): J_TradezZ, Jake__Wujastyk, TrendSpider, spluscollective (First Fellow), Venu_7_ + kural 107'nin 4 hesabı (Shay, Serenity, Akdağ teknik paylaşırsa).
Ne zaman: günde 1 kez. Hafta içi ilk uygun tur ≥ 23:00 TSİ (ABD seansı içinde atılan grafikler dizinlenmiş olur), Cmt/Paz 19:00 sonrası ilk tur (haftalık grafikler). DONGU'da o gün 'TA-STIL' varsa tekrar yok.
Adımlar:
1. ARA (en çok 4 WebSearch, allowed_domains ["x.com","twitter.com"]): `<hesap> chart` / `<hesap> $<ticker> breakout|trendline|weekly`. YALNIZ BUGÜNÜN tarihli tweeti (ET tarihi = bugün ya da TSİ bugün). Tarihi görünmeyen ya da dünkü tweet ALINMAZ. Bulunamazsa o gün 108 atlanır, DONGU'ya 'TA-STIL yok: aynı gün tweet bulunamadı'.
2. SEÇ: adaylar arasından en beğendiğini seç: net çizim (trend çizgisi, bölge, osilatör kırılımı, formasyon), çok izlenen, bizim kitleye uygun hisse (YZ/çip/büyük teknoloji, Enes portföyü önce). Seçim gerekçesi DONGU'ya: 'TA-STIL: <hesap> $<ticker> <görüntülenme> <çizim öğeleri>'.
3. KENDİ ANALİZİMİZ (zorunlu, enes-teknik-smc): `teknik_pro`, `teknik_ek derin`, `dip_tepe`, gerekirse `formasyon.py`. Tüm zaman dilimleri. Onların tezi ile bizimki karşılaştırılır: AYNI mı, KISMEN mi, TERS mi. Seviyeleri kendi verimizden hesaplarız; onların rakamını kopyalamayız.
4. ÇİZ: `python3 invest/stil_cizim.py <T> --tf <1wk|1d|4h> --trend asagi|yukari --ma .. --bolge a-b --osc cci|rsi --halka --seviye .. --baslik "..."` . Beğenilen tweetteki ÖĞE TÜRLERİNİ seç (ör. düşen trend + 200 HO + mor destek bölgesi + CCI trend kırılımı + halka) ama: kendi pivotlarımız, kendi renk/yazı (kart4 paleti), kendi markamız, en az 1 farklılık (zaman dilimi, ek seviye ya da farklı osilatör). Görsel yayinla_gorsel denetiminden geçer; Read ile bakılır, çakışma/kesik yazı varsa düzeltilir.
5. TWEET (Enes sesi, kural 102 + 54-H): o tarzdaki fikir kendi cümlemizle. Kalıp: ilk satır gördüğümüz şey (ör. 'Tesla haftalıkta 1 yıllık düşen trendi zorluyor.'), sonra 2-3 kısa satır: hangi çizgi, hangi seviye, osilatör ne diyor; bizim analiz farklıysa açıkça 'ama ben X'e bakıyorum' der; kapanış: 'Haftalık kapanış Y üstünde gelirse kırılım onaylanır, Z altı bozar.' Al/sat tavsiyesi, emoji, hashtag, link, soru YOK. Hesap adı anılmaz, onların cümlesi çevrilmez.
6. KAPI + KAYIT: `bash yayin_kontrol.sh TEKNIK <kalip>` GEÇTİ → Buffer (kart = stil çizim), `kayit.py --tur TEKNIK --duzen stil_cizim`, teknik_ek gunluk ekle (seviyeler), ertesi gün kural 66 takibi (yalnız tutan seviye anılır).
Kural ilişkisi: Enes'in kendi 'ben olsam' teknik tweetleri (TradingView ekran görüntüsü, Enes atar) AYNEN devam eder; 108 ayrı bir format: sistem atar, görsel kendi çizimimiz (Enes 28.11 açık talimatı).
Not: Enes'in 28.11'de örnek attığı TSLA haftalık (düşen trend + 40H HO + 275-295 mor bölge + CCI trend kırılımı + turuncu halka) bu formatın referans tarzıdır; örnek: g/stil_tsla.png.

108 HASSASİYET (Enes 28.11 11:38 'milimi milimine, mumlar kayıyor, çizgi yanlış çekilmesin'):
- Veri: stil_cizim.temiz() Yahoo haftalık serideki ÇİFT SON HAFTAYI siler (Yahoo son günü ayrı 'hafta' döndürür -> mum kayması). Çizimden önce son 3 mumu günlük veriyle karşılaştır (açılış/en yüksek/en düşük/kapanış).
- Trend çizgisi: --noktalar <tarih1>,<tarih2> ile İKİ GERÇEK fitil ucundan çizilir; araç 'gövde ihlali' sayar, 0 olmalı. Başkasının çizgisi gövdeleri kesiyorsa onu çizmeyiz, doğru çizgiyi çizip farkı tweette söyleriz (28.11 TSLA: Mayıs çizgisi Kasım başında kırılıp başarısız olmuştu; doğru çizgi Aralık tepesi -> 2 Kasım tepesi, 408,6).
- Osilatör çizgisi de --osc-noktalar ile gerçek tepelerden.
- Görsel Read ile açılır: son mum doğru mu, çizgi fitillere değiyor mu, etiketler mumların üstüne binmiyor mu. Hepsi tamam olmadan yayınlanmaz.
- Aynı gün tweet aramada çıkmazsa ve Enes o gün bir grafik gönderdiyse referans o grafiktir.

108 KARAR KURALI (Enes 28.11 11:43 'farklı çıkarsa onunkilerini kabul et, sen sadece beğenme olarak kontrol et'):
- Beğenilen tweetin TEZİ ve ÇİZGİSİ kabul edilir; bizim analiz farklı çıkarsa tweette karşı görüş YAZILMAZ.
- Bizim analizin işi yalnız BEĞENME süzgeci: çizim net mi, veri doğru mu (mum, kapanış, kırılım gerçekten oldu mu), kitleye uygun mu. Beğenmezsek o tweeti seçmeyiz, sıradakine geçeriz.
- Çizim: onların çizgisini aynı iki noktadan (--noktalar) çizeriz, gövde ihlali olsa bile; veri (mumlar, kapanış) yine birebir doğru olmalı.
- Tweet onların fikrini Enes sesiyle anlatır; seviyeler kendi verimizden hesaplanmış hâliyle yazılır.

54-H EK (Enes 28.11 11:46 'Bu yüzden ben bu kırılımı ciddiye alıyorum' -> 'çok yapay zeka yazmış'): 'X'i ciddiye alıyorum / ciddiye alırım / ciddiye almak gerek' ve 'Bu yüzden ben ...' kanaat kalıbı YASAK (yasak.py yakalar). Kanaat düz söylenir: '390 altına dönmedikçe kırılım geçerli', 'yön yukarı'.

## KURAL 109 — ŞİRKET ADI YERİNE $TICKER (Enes 28.11 11:49 'artık şirket isimlerini tweetlerde $TICKER şeklinde yazacaksın')
- Tweette şirket adı geçmez, $TICKER yazılır: Tesla -> $TSLA, Nvidia -> $NVDA, Marvell -> $MRVL, Micron -> $MU, Google/Alphabet -> $GOOGL.
- Türkçe ek kesme işaretiyle: $NVDA'nın, $TSLA'da, $MU'yu.
- İlk satır dahil her yerde. Endeks, emtia, kripto ve kurum (Fed, Goldman gibi halka açık olmayan bağlam) bu kuralın dışında; halka açık banka şirket olarak geçerse $GS, $JPM.
- yasak.py SIRKET_TICKER sözlüğü adı yakalar ve atmayı durdurur; yeni şirket geçince sözlüğe eklenir.
- Enes taslakları (ENES-TASLAK) ve kart başlıkları da aynı kurala uyar; kartta logo yanında $TICKER.

## KURAL 110 — GÜNLÜK ALT SINIR: TEKNİK ≥2, TEMEL ≥1 (Enes 28.11 12:00 'temelde en az 1, teknikte en az iki olsun, üst sınır yok')
- TA-STİL (kural 108): her gün EN AZ 2 tweet, üst sınır yok. Hafta içi 1. ≥19:00 TSİ (ABD seansı açıldıktan sonra dizinlenen grafikler), 2. ≥23:00; hafta sonu 1. ≥11:00, 2. ≥19:00. İkisi farklı hisse ve farklı hesaptan olur.
- TEMEL-FİKİR (kural 107: Shay Boloor, Serenity, Venu, Akdağ): her gün EN AZ 1 tweet, üst sınır yok. Fikir onların, tweet bizim verimiz + Enes sesi; isim anılmaz; rakam 2 kaynak. kayit.py --konu içine 'K107' yazılır (gun_ozet sayar).
- 22:00 TSİ'de gun_ozet 'KURAL 110 ... EKSİK' diyorsa sonraki turlar önce eksik olanı atar.
- Günlük toplam (hafta içi 15-20, hafta sonu 8) ve 35 dk aralık geçerli; 110 alt sınırları bu toplamın içinde öncelikli yer alır.
- Aynı gün tweet bulunamazsa (dizin gecikmesi) arama 2 kez daha denenir (farklı sorgu: hisse adı + 'chart', 'breakout', 'weekly'); yine yoksa DONGU'ya gerekçe yazılır, alt sınır o gün düşer.

54-H EK-2 (Enes 28.11 12:16 'kalabalık henüz inanmadı' -> 'çok AI gibi'): piyasayı/kalabalığı kişileştiren kanaat kalıpları YASAK: 'kalabalık henüz inanmadı', 'piyasa ikna olmadı', 'yatırımcılar kabullenmedi'. Düz ve ölçülebilir yaz: 'çoğu yatırımcı hâlâ korkuyor', 'korku endeksi hâlâ 25 altında' (yasak.py 54-H yakalar).

## KURAL 111 — PATLAYAN TWEET AVCISI (Enes 28.11 12:17 'takipçi sayısına göre tweeti çok patlamış hesapların o tweetini alıp benzer bir tweet atamaz mısın')
Amaç: takipçisine göre olağandışı yayılan finans tweetini bul, NEDEN yayıldığını çıkar, aynı fikri/biçimi kendi verimiz ve Enes sesiyle yaz.
- Bulma (her gün en az 1 aday, tur başına en çok 2 ek arama): X nabzı WebSearch (allowed_domains x.com/twitter.com) — sorgular: '<gündem hissesi> Görüntülenme', 'ABD borsası $TICKER', '<tema> views'. Sonuçta görünen görüntülenme ÷ hesabın takipçisi (profil sonucundan ya da X_NABIZ akran tablosundan). PATLAMA = görüntülenme ≥ 5 x takipçi VE ≥ 10 bin. Enes'in attığı ekran kayıtları/görüntüleri de kaynak (28.11 @Umitkirmizialan 27B / 3,1B takipçi).
- xcancel/nitter aynaları 28.11'de bot korumasıyla reddetti; deneme tur başına en çok 1, başarısızsa arama motoruyla devam. x.com'a giriş YOK.
- Çözümleme (DONGU'ya 1 satır 'PATLAMA: <hesap> <görüntülenme>/<takipçi> <neden>'): konu (kitlenin acısı mı, haber mi), biçim (uyarı, tartışma, liste, grafik, alıntı), ilk satır kancası, saat.
- Yazma: AYNI KONU ya da AYNI BİÇİM, cümle kopyası YOK, çeviri YOK, hesap adı anılmaz. Rakamlar 2 kaynak. Enes sesi (102), $TICKER (109), 54-H yasakları. Zamanı mümkünse orijinalin patladığı saat dilimine yakın.
- 111-Y (Enes 28.11 12:19): PATLAYAN TWEET kaynağı YALNIZ yabancı (İngilizce) finans içerik üreticileri; Türk hesaplar (Ümit Kırmızıalan vb.) yalnız akran kıyası içindir, onlardan benzer tweet üretilmez. GÜNDE EN AZ 2 K111 tweeti (üst sınır yok, günlük toplamın içinde öncelikli; gun_ozet sayar). Arama İngilizce: '$TICKER views', 'stocks chart views', '<tema> thread'; aday: X_NABIZ takip listesi (Shay Boloor, Serenity, Venu, Jake Wujastyk, TrendSpider, Kobeissi, Wall St Engine, unusual_whales, StockMKTNewz, Gary Black, Jonah Lupton...) + aramada görüntülenmesi takipçisinin ≥5 katı olan herhangi bir yabancı hesap. Uyarlama: birebir çeviri YOK; konu/biçim/kanca alınır, rakamlar 2 kaynaktan doğrulanır, Türk okura bağlam eklenir.
- Sayılır: günlük toplamın içinde, tür PATLAMA-BENZER; kayit.py --konu içine 'K111'. 48 saat sonra görüntülenmesi bizim ortancamızla karşılaştırılır -> DERSLER.md 1 satır (hangi biçim bizde de tuttu).

## KURAL 112 — GÜNLÜK 20-40 (Enes 28.11 12:20 'günlük tweet sayılarını 20-40 arası yap')
Her gün (hafta sonu dahil) sistem tweeti EN AZ 20, EN ÇOK 40 (kural 98'in 15-20 / hafta sonu 8 sayıları geçersiz). Aralık en az 20 dk (35 dk kuralı yerine), tur 20-30 dk arayla, turda 1-2 tweet. Konu eşiği konu_puan ≥60; K107/K108/K111 her zaman yeterli. Alt sınıra yetişmek için tur boş geçmez: haber zayıfsa açıklayıcı, eğitici, tarihsel istatistik ya da veri tweeti. Kalite kapısı (yayin_kontrol.sh) aynen.

54-H EK-3 (Enes 28.11 13:03 'Yönü Pazartesi'nin tam seansı ve Salı gecesi $MRVL bilançosu belirler' -> 'çok AI ibaresi'): 'Yönü X belirler / belirleyecek', 'son sözü X söyleyecek', 'belirleyici olacak şey' gibi kehanet/sunucu kapanışları YASAK. Düz ve kişisel yaz: 'Salı gecesi $MRVL bilançosuna bakacağım', 'Pazartesi 26.000 üstünde kalırsa dip geride'. yasak.py 54-H yakalar.

## KURAL 113 — ENES SESİ + ÇOK ÜST DÜZEY BORSACI (Enes 28.11 19:26: "artık daha çok benim dilimde benim sesimle ama çok daha profesyonel bir borsacı gibi yazılmasını istiyorum, çok çok prof")
Kural 102 (Enes sesi) ile kural 60/89 (profesyonel ton) arasındaki denge DEĞİŞTİ: ikisi birlikte, en üst seviyede. Ses Enes (birinci tekil, kısa, konuşur gibi, süssüz); İÇERİK ve KELİME hazinesi masada işlem yapan kıdemli bir borsacı.
Her tweette:
1. NET HÜKÜM + SEVİYE: "beğendim/beğenmedim", "ben buradan eklerim / burada beklerim" + somut rakam (fiyat, çarpan, eşik). Belirsiz "olabilir, sanırım, galiba, gibi görünüyor" YOK; "bence" en çok 1 kez.
2. BORSACI TERİMLERİ doğal ve doğru: konsensüs, rehber (guidance), çarpan / ileri F/K, marj, nakit akışı, pozisyonlanma, katalizör, risk/ödül, destek/direnç, kapanış teyidi, hacim, revizyon, satış baskısı, kâr realizasyonu, sipariş görünürlüğü. Tweet başına 2-3 terim (kalite.py sınırı 3), her biri yerinde; terimi açıklamak açıklayıcı tweetin işi.
3. EN AZ BİR "MASA" DETAYI: piyasanın neyi fiyatladığı / beklentiden fark / pozisyonlanma / tetikleyici tarih / geçersiz kılan seviye (kural 89 öğelerinden en az biri; uyarı değil hedef).
4. Kısa: ilk satır ≤12 kelime iddia; toplam 3 paragrafı geçmez; cümle ortalaması ≤18 kelime (ses_kontrol).
5. YASAK kalır: vecize/mecaz kapanış, 54-F/G/H kalıpları, "X değil Y" süsü, al/sat tavsiyesi, soru, emoji, hashtag.
Örnek (önce -> sonra):
- "Bence bu düşüş fırsat olabilir." -> "$MU zirveden %48 aşağıda, 12 kat kârla işlem görüyor. Ben 600 altını kademeli alım bölgesi sayıyorum, 560 kapanışı tezi bozar."
- "Hisse güzel yükseldi." -> "$NVDA haftayı güçlü kapattı ama hacim ortalamanın altında. Kapanış teyidi 160 üstü, gelmezse bu bir tepki yükselişi."
Taslaklar (kural 69) ve "Ne anlama geliyor?" açıklamaları da aynı seviyede yazılır; Enes'e mesajlar Türkçe.

## KURAL 113-B — KURUMSAL MASA SEVİYESİ (Enes 28.11 19:29 'daha da prof istiyorum')
113'ün üstüne, kalite.py ZORUNLU denetler (HATA, uyarı değil):
- Her tweette EN AZ 3 borsacı öğesi: konsensüs/beklenti, rehber, çarpan/F/K, marj, nakit akışı, pozisyonlanma, katalizör, risk/ödül-asimetri, destek/direnç, kapanış teyidi, hacim, revizyon, realizasyon, sipariş, fiyatlama, prim/iskonto, baz puan, yıllık/çeyreklik bazda, oynaklık, akış, değerleme, eşik/seviye, trend, genişlik, geri alım, kredi.
- Tereddüt dili YASAK: olabilir, sanırım, galiba, gibi görünüyor, belki, muhtemelen, düşünüyorum. "bence" en çok 1.
- Somut rakam/seviye zorunlu.
Yazım düzeyi: kurumsal araştırma notunun tek paragraflık özeti gibi. Sıra: (1) olgu + rakam, (2) piyasanın fiyatladığı / beklentiden fark, (3) benim pozisyonum ve seviyem, (4) tezi bozan eşik. Ses yine Enes: birinci tekil, kısa cümle, süssüz.
Örnek: "$NVDA 12,5 kat ileri F/K ile S&P 500'e %32 iskontolu. Konsensüs kâr tahminini düşürmedi, yani çarpan daralması tamamen fiyattan geldi. Ben 145 desteğini pozisyon artırma bölgesi görüyorum; tahmin revizyonu aşağı dönerse tez bozulur."

## KURAL 113-C — HEDGE FON MASASI (Enes 28.11 19:30 'daha da prof istiyorum, yetmez')
113-B'nin üstüne kalite.py ZORUNLU (HATA):
- EN AZ 4 borsacı öğesi (3 değil).
- Her tweette İKİ ÇAPA birden: (a) değerleme/beklenti çapası: çarpan, konsensüs, revizyon, iskonto/prim, marj, piyasanın fiyatladığı; (b) risk/eşik çapası: tezi bozan seviye, kapanış teyidi, destek/direnç, asimetri.
Yazım düzeyi: hedge fon portföy yöneticisinin sabah notu. Ne oldu (rakam) → piyasa neyi fiyatlıyor, konsensüsten fark → benim pozisyonum ve asimetri → tezi bozan eşik. Kelimeler: asimetri, risk/ödül, pozisyon artırma/azaltma, kısa pozisyon kapatma, çarpan genişlemesi/daralması, kâr tahmini revizyonu, akış, teyit kapanışı. Ses yine Enes: birinci tekil, kısa cümle, süssüz; terim yığını yok, her terim bir rakama bağlı.
Örnek: "$SMH haftayı %10 yükselişle kapattı, 200 günlük ortalamanın hâlâ %16 altında. Hacim ortalamanın 1,4 katı, bu kısa pozisyon kapatmanın ötesinde gerçek alım. Konsensüs 2027 kâr tahminini düşürmedikçe çarpan daralması aşırı; risk/ödül alım tarafında. 200 günlük ortalamanın üstünde kapanış teyit, haftanın dibi altı tezi bozar."

## KURAL 113-D — KURUMSAL ARAŞTIRMA NOTU DÜZEYİ (Enes 28.11 19:33 'olmaz, daha da prof')
113-C'nin üstüne kalite.py ZORUNLU (HATA):
- KIYAS ÇAPASI: her rakam bir ölçüte bağlanır: endeks, akran, tarihsel ortalama/yüzdelik, 'X'ten beri en düşük', konsensüs. Çıplak rakam yok.
- FARKLI GÖRÜŞ (variant perception): piyasanın/konsensüsün ne fiyatladığı VE benim nerede ayrıştığım aynı tweette. Haber aktarmak yetmez; fark yaratan tez yazılır.
- AMATÖR DİL YASAK: güzel, harika, müthiş, uçtu, çakıldı, patladı, roket, fırsat, kaçırma, bomba, efsane, süper, inanılmaz, resmen, 'alım gerçek'. Kurumsal karşılık: fırsat -> asimetrik risk/ödül; uçtu -> %X prim; alım gerçek -> hacim teyitli.
- Jargon sınırı 5 (terim yığını değil, her biri rakama bağlı).
Yapı (her tweet): 1) olgu + rakam + kıyas, 2) piyasanın fiyatladığı / konsensüs, 3) benim ayrıştığım nokta (tez), 4) asimetri + teyit seviyesi + tezi bozan seviye.
Örnek (biçim örneği; rakamlar her seferinde 2 kaynakla doğrulanır): "$SMH haftayı %10 primle kapattı ama 200 günlük ortalamanın %16 altında. Piyasa çip kârlarında aşağı revizyon fiyatlıyor, konsensüs ise $NVDA'da tahmini indirmedi. Benim ayrıştığım yer bu: değerleme daralması tamamen fiyattan geldi. Hacim teyitli yükseliş, risk/ödül asimetrik. 200 günlük ortalama üstü kapanış teyit, haftanın dibi altı tezi bozar."

## KURAL 113-E — KURUMSAL VERİ DERİNLİĞİ + İKİ YÖNLÜ SENARYO (Enes 28.11 19:35 'daha da prof')
113-D'nin üstüne kalite.py ZORUNLU (HATA):
- FİYAT DIŞI KURUMSAL METRİK: rakamıyla en az biri: çarpan (12,5 kat), marj, konsensüs/beklenti rakamı, revizyon yüzdesi, rehber, EPS/hisse başı kâr, opsiyon ima edilen hareket. Yalnız fiyat yüzdesi yetmez.
- İKİ YÖNLÜ SENARYO: yukarı teyit seviyesi (X üstü kapanış) VE aşağı geçersizlik seviyesi (Y altı tezi bozar) birlikte.
- Veri kaynakları öncelik sırası: şirket belgesi (8-K, sunum, görüşme), konsensüs (FactSet/LSEG haberleri), kendi hesabımız (Yahoo), sonra haber. DONGU satırında her metriğin kaynağı.
Örnek (biçim): "$NVDA 12,5 kat ileri F/K ile S&P 500'ün 18,3 katına %32 iskontolu, 2012'den beri en düşük seviye. Piyasa YZ yatırım harcamasında 2027 yavaşlamasını fiyatlıyor, konsensüs ise kâr tahminini indirmedi. Benim ayrıştığım yer bu: daralma tamamen fiyattan geldi, kazanç tarafında revizyon yok. 160 üstü haftalık kapanış teyit, 145 altı tezi bozar; bu aralıkta risk/ödül alım tarafında."

## KURAL 113-MAX — EN YÜKSEK PROFESYONELLİK STANDARDI (Enes 28.11 19:37 'YETMEZ, EN YÜKSEK PROFESYONELLİK')
Bundan sonra tek standart vardır: EN YÜKSEK. 113, 113-B, C, D, E'nin hepsi zorunlu, ayrıca:
1. KIDEMLİ PM EDİTÖR GEÇİŞİ (her tweet, yayin_kontrol GEÇTİ'den sonra, Buffer'dan önce): metni bir kez büyük bir fonun kıdemli portföy yöneticisi gözüyle oku ve 5 soruyu yanıtla; biri hayırsa yeniden yaz, kapıdan yeniden geçir:
   a) İlk cümle tek başına okunsa masadaki biri "bunu bilmiyordum" der mi (yeni bilgi ya da yeni açı)?
   b) Konsensüsün tam rakamı ya da piyasanın fiyatladığı şey açıkça yazılı mı?
   c) Benim tezim konsensüsten hangi değişkende ayrışıyor (kâr, marj, çarpan, zamanlama) ve bu tek cümlede söylenmiş mi?
   d) Asimetri rakamla var mı (teyit seviyesine uzaklık / geçersizlik seviyesine uzaklık)?
   e) Gereksiz kelime var mı? Varsa sil; her kelime bilgi taşımalı.
2. VERİ STANDARDI: her tweette en az 1 birincil ya da konsensüs verisi (şirket belgesi, FactSet/LSEG konsensüsü, borsa verisi) ve kaynağı DONGU'da. Haber cümlesi tek başına veri sayılmaz.
3. ÖLÇÜLEBİLİR TEZ: her tez ileride doğrulanabilir bir rakama bağlanır (kural 66 sonuç takibine girer).
4. DİL: kurumsal Türkçe, Enes'in birinci tekil sesi; İngilizce terim yalnız Türkçesi yerleşik değilse (capex, EPS), ilk geçişte Türkçesiyle.
5. DONGU satırına 'PM: a✓ b✓ c✓ d✓ e✓' yazılır; eksik işaretli tweet atılmaz.
Not: 113-MAX yazım çıtasıdır; asıl fark veri derinliğinden gelir. Pazar perfogren 113 öncesi/sonrası görüntülenmeyi kıyaslar, sonuç Enes'e rakamla bildirilir.

## KURAL 113-F — PROFESYONEL VE ANLAŞILIR + KALIP ÇEŞİTLİLİĞİ (Enes 28.11 19:40 'sürekli aynısını yapıyorsun, terimler hem prof hem anlaşılır olacak')
- Her tweette EN AĞIR terim aynı cümlede sade Türkçeyle açılır: "ileri F/K, yani fiyatın gelecek yıl beklenen kâra oranı", "tahmin revizyonu, yani analistlerin kâr beklentisini değiştirmesi". Tweet başına 1 açıklama yeter; kolay terimler (destek, hacim) açılmaz. kalite.py ZORUNLU.
- AYNI ŞABLON YOK: "olgu -> fiyatlanan -> ben -> seviye" iskeleti her tweette tekrarlanmaz. Profesyonel biçimler döner: (1) MAKAS: iki göstergenin ters gitmesi (fiyat düşüyor, kâr tahmini yükseliyor), (2) O ZAMAN / ŞİMDİ: aynı ölçünün aylar önceki ve bugünkü değeri, (3) SENARYO: iki ihtimal ve her birinin fiyata etkisi, rakamla, (4) AKRAN: aynı işi yapan şirketlerle tek ölçüde kıyas, (5) TERSİNE HESAP: bugünkü fiyatın haklı çıkması için kârın ne olması gerektiği, (6) TAKVİM: tarihli tetikleyici ve o gün bakılacak rakam. Son 3 tweette kullanılan biçim tekrar edilmez; DONGU'ya 'biçim113: makas|ozaman|senaryo|akran|tersine|takvim'.
- Sesi Enes: kısa, birinci tekil, sade; profesyonellik kelime yığınından değil, doğru rakam + doğru kıyas + net tezden gelir.
Örnek (MAKAS + O ZAMAN/ŞİMDİ): "$NVDA'da fiyat ile kâr tahmini ters yönde gidiyor. Ağustos sonunda ileri F/K, yani fiyatın gelecek yıl beklenen kâra oranı, 24 civarındaydı. Şimdi analistlerin tahmin revizyonu yukarı, hisse aşağı; oran 12,5'e indi, endeks ortalaması 18,3. Piyasa CEO değişikliğini ve YZ harcamasında yavaşlamayı fiyatlıyor, bence bu daralma aşırı tepki. 165 üstü haftalık kapanış teyit, 124,5'teki yılın dibi kırılırsa tez bozulur."

## KURAL 113-G — BEN DİLİ, İNSAN KONUŞMASI (Enes 28.11 19:42 'bu olur ama tamamen ben dilinde, insan konuşmasını analiz ederek yaz')
113'ün profesyonel içeriği aynen kalır; YAZIŞ insan konuşması gibi olur (SES_ORNEKLERI.md'deki Enes tweetleri referans):
- Açılış konuşma cümlesi: "$NVDA'da garip bir durum var." / "Şuna dikkat çekmek istiyorum." Rapor başlığı gibi değil.
- Terim okura çevrilir: "(ileri F/K)" parantezde, anlamı da günlük dille: "yani aynı kâr için neredeyse yarı fiyat ödüyorsun".
- Okura doğrudan hitap serbest ("ödüyorsun", "takipte kalmakta fayda var"), soru yok.
- Kendi davranışını ve duygusunu söyler: "ben acele etmiyorum", "şunu görürsem daha rahat ederim", "kırılırsa yanıldığımı kabul ederim", "alımlarımı parça parça yapıyorum".
- Cümleler kısa, satır satır; "bence" en çok 1 kez; vecize, mecaz, "X değil Y" süsü yok.
- Kontrol: metni sesli okuyunca bir insanın arkadaşına anlatışı gibi duruyor mu? Rapor gibiyse yeniden yaz.
Örnek (Enes onayladı 28.11 19:42 seviyesi): "$NVDA'da garip bir durum var. Hisse düşüyor ama analistler kâr tahminlerini yukarı çekiyor. / Ağustos sonunda hisse, gelecek yıl beklenen kârının 24 katı civarından işlem görüyordu (ileri F/K). Şimdi 12,5. Yani aynı kâr için neredeyse yarı fiyat ödüyorsun. Endeksin ortalaması 18,3. / Bence piyasa YZ harcamalarında yavaşlamayı fazla fiyatlıyor, tahmin revizyonları tersini söylüyor. Ben acele etmiyorum; 165 üstünde haftalık kapanış görürsem daha rahat ederim, 124,5'teki yılın dibi kırılırsa da yanıldığımı kabul ederim."

## KURAL 114 — YAPAY ZEKÂ YAZIM İZLERİ YASAĞI (Enes 28.11 19:45 'tezi bozar, risk masada, ben acele etmiyorum vb. tüm ifadeleri araştır, kullanma')
113 bölümlerindeki örneklerde geçen 'tezi bozar', 'teyit eder', 'ben acele etmiyorum', 'daha rahat ederim', 'yanıldığımı kabul ederim', 'benim ayrıştığım yer', 'risk/ödül alım tarafında', 'garip bir durum var' ARTIK YASAK; 113 içeriği (rakam, kıyas, terim açıklaması, iki yönlü seviye) aynen sürer, yalnız bu kalıplar kullanılmaz.
Tam liste ve gerekçe: invest/YZ_IZLERI.md. yasak.py 'YZ114' bloğu HATA verir (yayin_kontrol.sh içinde).
- Yapısal izler: 'X değil, Y'; 'sadece X değil, Y de'; üçlü yığın ('A, B ve C'); uzun tire (— –); retorik soru-cevap; sohbet botu açılışı; hazır açılış cümlesi; her tweette aynı kapanış şablonu; markdown; ✅🚀→ gibi işaretler.
- Yasak aileler: tez/teyit şablonu, duygu/tavır klişeleri, masa/pusula/fırtına mecazları, şablon fon dili, YZ sözlüğü (kritik, kilit rol, çığır açan, kayda değer, çarpıcı), sunucu dili (gözler X'te, zaman gösterecek, büyük resim, işin özü), özet bağlaçları (sonuç olarak, özetle, günün sonunda), 'işaret ediyor / sinyal veriyor', dengeli temkin ('temkinli iyimserim', 'bir yandan... diğer yandan'), 'şunu belirtmek gerekir'.
- İnsan gibi: olguyla başla; kapanışta kendi hareketin seviyeyle ('165'i geçerse büyütürüm, 124,5 kırılırsa kenara çekilirim'), her tweette farklı fiil; cümle uzunlukları karışık; rakam konuşsun; aynı açılış/kapanış/bağlaç aynı gün iki kez yok.
Geçerli örnek: "$NVDA düşüyor ama analistler kâr tahminlerini yukarı çekiyor. Ağustos sonunda hisse, gelecek yıl beklenen kârının 24 katı civarından işlem görüyordu (ileri F/K). Şimdi 12,5. Yani aynı kâr için neredeyse yarı fiyat ödüyorsun. Endeksin ortalaması 18,3. Bence piyasa YZ harcamalarında yavaşlamayı fazla fiyatlıyor, tahmin revizyonları tersini söylüyor. 165'in üstünde haftalık kapanış gelirse pozisyonu büyütürüm, 124,5'teki yılın dibi kırılırsa kenara çekilirim."

## KURAL 114-B — EK YASAKLAR + AYNI GÜN TEKRAR YASAĞI (Enes 28.11 20:22 'hepsini yasakla, yeteneklere ekle')
yasak.py (YZ114 ek liste) ve kalite.py (aynı gün tekrar) HATA verir.
1. Bizim tekrarladıklarımız: 'tek başına sinyal değil', 'Benim gördüğüm risk / baktığım yer', '... ancak X yapar' vecizesi, 'bu kalem taşınabilir', 'fazla karamsar', 'aşırı tepki', 'kendi ölçeğimde' (kaynak satırında kalır).
2. Borsa gazetesi klişeleri: yön arayışı, soluklanma, nefes alma, yatay seyir, satıcılı/alıcılı seyir, risk iştahı, pozitif/negatif ayrışma, tepki alımı, kâr satışı geldi, 'güne yükselişle başladı'.
3. Boş güçlendiriciler: tamamen, kesinlikle, açıkça, son derece, oldukça, bir hayli, net bir şekilde, ciddi düşüş/alım, güçlü sinyal, önemli gelişme, dikkat çeken. Yerine rakam.
4. Bağlaç: dolayısıyla, bu nedenle, bu yüzden, öte yandan, buna karşın, ayrıca, üstelik, bununla birlikte; tweet başına en çok 1.
5. Sahte samimiyet: dürüst olmak gerekirse, açık konuşayım, açıkçası, itiraf etmeliyim, şunu söyleyeyim. 'yani' tweet başına en çok 1.
6. Belirsiz zaman/miktar: son dönemde, kısa vadede, önümüzdeki süreçte, uzun zamandır, bir süredir, yakın zamanda. Yerine tarih/rakam ('3 haftadır', 'Aralık'ta').
7. AYNI GÜN TEKRAR YASAĞI (kalite.py, kaydedilen metinlerle): aynı ilk 3 kelime, aynı kapanış fiili, aynı hüküm kelimesi (aşırı, gerçek, güçlü, zayıf, net, ciddi, karamsar, iyimser, temkinli, ucuz, pahalı, sağlam, abartılı, fazla) aynı gün ikinci tweette kullanılmaz. kalite.py kaydet artık metni de saklar.

## KURAL 111-T — TAKİPÇİ SAYISI ZORUNLU DOĞRULAMA (Enes 28.11 20:29 'takipçi sayısını neden bulamadın, önüne geçecek düzenleme yap')
Sebep (28.11): adaylar yalnız görüntülenmeye bakılarak seçildi; takipçi aranmadı. Sonradan bakıldı: LeopoldTracker_ 411,5B görüntülenme / 715,8B takipçi = 0,57x; MMMTwealth 40,2B / 64,7B = 0,62x; Kobeissi 422B / 1M+ -> üçü de PATLAMA DEĞİL. Bugünkü 3 'K111' tweeti sayılmadı.
Yöntem (x.com'a giriş YOK):
1. Aday tweet bulunur (WebSearch allowed_domains x.com/twitter.com; snippet'te görüntülenme yazar).
2. Takipçi: önce `python3 invest/takipci.py bak <handle>` (defter, 30 gün geçerli). Yoksa TEK WebSearch: '<handle> followers' (allowed_domains x.com/twitter.com, mode standard). Profil sonucu 'NNN.NK Followers' ya da JSON 'Follows' sayısını verir -> `takipci.py ekle <handle> <sayı>`. socialblade/xcancel aynaları reddediyor, deneme.
3. `python3 invest/takipci.py oran <handle> <görüntülenme>` -> 'ORAN:Nx PATLAMA' değilse aday ELENİR, sıradakine geçilir. Takipçi 1 aramada bulunamazsa aday elenir.
4. Hızlı süzgeç: büyük hesaplar (100B+ takipçi: Kobeissi, unusual_whales, Wall St Engine, takip/haber hesapları) nadiren 5x yapar; öncelik 5-50B takipçili analist hesapları (snippet görüntülenmesi 50B+ olanlar).
5. Kayıt: kayit.py --konu 'K111 ORAN:<n>x ...'; gun_ozet yalnız ORAN>=5 olanları PATLAMA sayar. DONGU: 'PATLAMA: <hesap> <görüntülenme>/<takipçi> = <n>x <neden>'.

## KURAL 111-M İPTAL — ORAN ESAS (Enes 28.11 20:33 'en çok okunan önemli değil, takipçi sayısına kıyasla en çok patlayan önemli')
Mutlak görüntülenme yedeği KALDIRILDI. Yalnız ORAN ≥5x sayılır.
BULMA YÖNTEMİ (28.11'de işe yarayan): günün en sıcak konusunu bul (ör. Leopold mektubu), o konuya TEPKİ veren küçük hesapların tweetlerini ara ('<konu> Views', '<konu> thread', '<ticker> <konu>'); snippet'te 30B+ görüntülenmesi olan ama adı tanınmayan hesapları profil aramasıyla kontrol et. Örnek: EhrmantrautCap_ 3.152 takipçi, 123B görüntülenme = 39x (tek cümlelik karşı çıkış + belge görüntüsü). Büyük hesaplar (100B+ takipçi) atlanır.

## KURAL 111 ÖZET (28.11 akşamı, Enes 20:26-20:33) — PATLAYAN TWEET = TAKİPÇİYE ORAN
- Ölçü YALNIZ oran: görüntülenme ≥ 5 x takipçi VE ≥ 10B. 'En çok okunan' sayılmaz (111-M iptal).
- Takipçi: `takipci.py bak`; yoksa tek WebSearch '<handle> followers' (allowed_domains x.com/twitter.com) -> `takipci.py ekle`; `takipci.py oran` PATLAMA demezse aday elenir. Konu 'K111 ORAN:<n>x'; gun_ozet yalnız ≥5x sayar.
- Bulma: günün en sıcak konusuna TEPKİ veren küçük hesaplar ('<konu> Views', '<konu> thread'); snippet'te 30B+ görüntülenen tanınmamış hesapların profili kontrol edilir. Büyük hesaplar (100B+ takipçi) atlanır.
- 28.11 ölçümü: Leopold takip 0,57x, MMMT 0,62x, Serenity 0,21x, Jukan 0,23x, bert_gilfoyle 4,88x (sayılmaz), EhrmantrautCap_ 39x (PATLAMA: tek cümlelik karşı çıkış + belge görüntüsü).
- Uyarlama: aynı konu + aynı kanca, çeviri yok, hesap adı yok, Enes sesi, kural 113/114/116.

## KURAL 116 — İŞLEM FİİLİ YOK, TEKNİK YALNIZ TA TWEETİNDE (Enes 28.11 20:36 'seviyelerde eklerim, çıkarırım vs deme; teknikten teknik analiz tweetleri dışında bahsetme')
kalite.py ZORUNLU (HATA):
- İşlem fiili YASAK (tüm tweetler, TA dahil): eklerim, çıkarırım, alırım, satarım, alıcı olurum, kenarda kalırım, kenara çekilirim, pozisyonu büyütürüm/küçültürüm, kâr alırım, stop olurum. Görüş ve koşul söylenir, işlem bildirilmez.
- Teknik öğeler YALNIZ TA tweetinde (tur TEKNIK / TA-STİL): 200/50 günlük ortalama, hareketli ortalama, destek, direnç, kırılım/kırılırsa, trend çizgisi, haftalık kapanış, 'X üstü kapanış', RSI, MACD, Fibonacci, 'üstüne çıkarsa / altına inerse'. Diğer tweetlerde fiyat seviyesi senaryosu yerine TEMEL tetikleyici yazılır: 'kâr tahminleri aşağı dönerse görüşümü değiştiririm', 'EUV siparişleri gerilerse', 'rehber düşürülürse', 'brüt marj %X'in altında kalırsa'.
- 113-C/113-E bu nedenle TA dışı tweetlerde temel tetikleyiciyle de sağlanır.
- 28.11 uygulaması: 20:47 ($NVDA/Aschenbrenner) ve 21:08 ($ASML) zamanlanmış tweetleri yayından önce bu kurala göre düzeltildi.

## KURAL 114-C — ART ARDA AYNI KALIP YASAĞI (Enes 28.11 20:39 'ikisi de aynı kalıpta, bu tarz şeyleri engelleyecek yetenekler koy')
Örnek hata: 20:47 'Aschenbrenner'ın fonu ... Bellekte ben de aynı yerdeyim. $NVDA'da ayrılıyorum ... görüşümü değiştiririm.' ve 21:08 'Aschenbrenner'ın mektubunda ... fonla aynı yerdeyim, $ASML'de ayrılıyorum ... görüşümü değiştiririm.' -> aynı iskelet.
kalite.py ZORUNLU, son 3 tweete karşı (kaydedilen metinlerle):
- Yapı benzerliği: ticker ve rakamlar soyutlanınca kelime dizisi benzerliği ≥%45 ise HATA.
- İlk kelime aynıysa HATA (ör. iki tweet de 'Aschenbrenner'ın' ile başlıyor).
- Son 3 kelime (kapanış) aynıysa HATA.
- Kalıp ifade son 3 tweette tekrar ederse HATA: 'görüşümü değiştir', 'fikrim değiş', 'aynı yerdeyim', 'ayrılıyorum', 'en zayıf', 'uzak duruyor'.
- 114-B (aynı gün kapanış fiili, açılış, hüküm kelimesi) aynen.
- Buffer'da düzenlenen tweetin metni kalite_defteri.json'da da güncellenir (yoksa sonraki kontrol eski metne bakar).
- Aynı konuda (ör. aynı mektup) art arda iki tweet atılacaksa ikincisi farklı biçimle (113-F: makas, o zaman/şimdi, senaryo, akran, tersine hesap, takvim) ve farklı açılış özne/fiiliyle kurulur.

## KURAL 117 — "NE DEMİŞTİM, NE OLDU" SERİSİ (Enes 28.11 20:44; eski 'Bu hafta tutan yorumlarım' listesi İPTAL)
- Haftada 2: 1 TEKNİK (Cumartesi 20:25 sabit görevi), 1 TEMEL (aynı görev, 25 dk sonra). Görev dosyası: invest/gorevler/karne.md.
- Yalnız TUTAN ve BİLMESİ EN ZOR tek yorum (piyasa tersini bekliyordu / eşiğe %1'den yakın / kısa sürede tuttu). Tutmayan hiç yazılmaz.
- Anlaşılır biçim: ilk satır neyin tuttuğunu net söyler; sonra 'ne zaman ne demiştim' + 'ne oldu (rakam, tarih)'; son satır 'Ne demiştim, ne oldu serisinin teknik/temel ayağı bu.' Liste, '•', birden çok yorum yok. Kart kart4 kiyas (NE DEMİŞTİM / NE OLDU).
- Örnek (teknik, 28.11): 'Geçen hafta Nasdaq 100 için yazdığım eşik tuttu. 25 Kasım'da endeks gün içinde 24.971'e, 24.980'deki ayı piyasası eşiğinin 9 puan altına indi ve oradan döndü. O akşam eşik kapanış bazında kırılmadıkça ayı piyasası başlamaz demiştim. Kırılmadı, cuma günü 26.726'dan kapattı; eşiğin %7 üstünde. Ne demiştim, ne oldu serisinin teknik ayağı bu.'
- Seriyi beslemek için her gün en az 1 ölçülebilir TEMEL yorum (bilanço/rehber/marj/konsensüs, tarih + eşik) `yorumlar.py ekle` ile deftere yazılır.

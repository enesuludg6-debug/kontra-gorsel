---
name: "enes-tweet-turu"
description: "Enes Uludağ'ın X hesabı için otomatik paylaşım turu, Enes'in istediği tweet veya 13F tweeti hazırlanıp Buffer'dan atılırken kullanılır: kontrol listesi, kaynak, yazım, kart ve kayıt kuralları."
---

# Enes tweet turu

> **23.11.2026 GÜNCELLEMESİ (ÖNCE BUNU UYGULA; bu dosyanın eski bölümleriyle çelişirse bu blok geçerli):**
> - **Tek kural listesi ve tasarruf (Enes 20:47):** Tur başı `bash invest/tur_basi.sh <etiket>`; çıktıdaki `invest/KURAL_DIZINI.md` kural 1-65'in güncel listesidir. Bu dosyayı, diğer skill dosyalarını ve `invest/KURALLAR_TAM.md`'yi baştan okuma; ayrıntı gerekince yalnız ilgili bölümü grep ile aç. Hiçbir kural silinmedi.
> - **Her tweet `enes-analiz-kalitesi` skill'ine uyar** (kural 61-65): uzunluk tavanı, jargon sıklığı (62), 14 analiz kalıbı ve görünürlük (63, 63-B/C/D: `kalite.py kontrol --tur <TÜR> --kalip <X veya X+Y>`, birincil kalıp son 4 tweette tekrar etmez, yapı imzası son 3 tweetle aynı olamaz), konuşma dili (64), "takip edeceğim / merak ediyorum / benim için önemlisi" sınırı ve sonuç cümlesiyle bitiş (64-B), yapay zekâ gibi duran kurgulu cümle yasağı (54-D: "manşet X diyor, veri başka şey söylüyor", "stres geçmiş değil"), ikinci katman veri zorunluluğu (65: oynaklık vade eğrisi, korelasyon, akış, revizyon, tablodan derin kalem, kendi hesabımız).
> - **Mekanik kontrol sırası:** `yasak.py` → `gorus.py kontrol` → `kalite.py kontrol --tur --kalip`; atınca `gorus.py kaydet` + `kalite.py kaydet --tur --kalip` + `kayit.py`.
> - **Aralık (Enes 21:29):** Bir turda 2 tweet varsa arka arkaya atılmaz. İlki Buffer shareNow, ikincisi Buffer `mode: customScheduled`, `dueAt` ilkinden ~12 dk sonra (+03:00). Sonraki tur zamanlanan tweetten en az 10 dk sonra kurulur.
> - **Kart notları:** `versus` düzeni kaldırıldı; dortlu/isi/terminal kartlarında logolu `$TICKER` rakamın üstüne biniyor, logosuz isim kullan; takvim kartında gün adı kısa (ÇAR/PER); raw main URL 404 verirse commit SHA'lı raw URL.
> - **Enes'e mesaj:** kısa; tweet metni + kullanılan kalıp + 3-5 maddelik "Ne anlama geliyor?" (tek kaynakta kalan bilgiler dahil).

Repo: `/home/claude/kontra-gorsel/invest` (GitHub enesuludg6-debug/kontra-gorsel). Ayrıntı ve geçmiş için başvuru dosyaları: `DEVIR_TAM.md` (tüm kurallar, portföy, adaylar), `DEVIR_OZET.md`, `ORNEKLER.md` (beğenilen tweet kalıpları), `DONGU.md` (her paylaşımın kaydı), `temel_karne.md`. Bu skill ile DEVIR_TAM çelişirse EN YENİ tarihli kural geçerlidir; yeni kural gelince ikisi de güncellenir.

Her zaman Türkçe yaz. Enes'e giden mesajlar da Türkçe.

Hesabın amacı (her şeyin üstünde): en iyi getiriyi yakalamak ya da en bilgili görünmek değil, GÜVEN ve İYİ İÇERİK. Doğru olmayan rakam yerine eksik tweet; tutmayan tahminden bahsedilmez, yalnız doğru çıkanlar (kural 23); abartı ve heyecan yok. Hedef okur ABD borsasını az bilen biri: kısa, sade, anlaşılır. X hesabı @enes1050392 (Enes Uludağ, EnesInvestUS).

Bilanço önizleme/rakam/analiz ve 13F serisi için `enes-bilanco-13f`, portföy notları ve temel karne için `enes-portfoy-analiz` (18:00 ve 23:30 analiz görevleri yok, kural 44) skill'ini de yükle.

## 1. Tur başı kontrol (sırayla)

1. `ReadNotifications` (bildirim varsa), sonra `cd /home/claude/kontra-gorsel/invest && git pull -q`.
2. `invest/DURUM.md` ve `tail -n 30 DONGU.md` oku (DEVIR_TAM'ı baştan okuma, kural 18): satır başında tek başına `DURDUR` varsa HİÇBİR ŞEY yapma, yeni tur kurma.
3. Son OTOMATİK paylaşım saati: 20 dakikadan yeniyse paylaşma; kalan süreye göre 20-40 dk sonrasına aynı mesajla tur kur. Enes'in istediği tweet hemen atılır (o 20 dk kuralına girmez ama sonraki otomatik turu en az 20 dk sonraya kaydır).
4. Saat 01:00-09:00 TSİ arasıysa paylaşma (önceden bilinen açıklama hariç), 09:05'e tur kur.

## 2. Konu seçimi (öncelik sırası)

0. KONU FİLTRESİ (kesin kural 46, Enes 18.11 17:12: "sayfamda ben ai space nasdaq la ilgileniyorum, alakasız şirketler paylaşıyorsun"): yalnız YAPAY ZEKÂ (çip/yarı iletken, bellek/depolama, ağ/optik, bulut/neocloud, veri merkezi enerji/soğutma, yapay zekâ yazılımı ve siber güvenlik), UZAY (RKLB, ASTS, LUNR, PL...) ve NASDAQ (Nasdaq 100, büyük teknoloji, endeks hareketi) + bunlara etkisiyle makro (Fed, faiz, enflasyon, istihdam). Perakende/tüketim (Target, Walmart, Lowe's, Home Depot, TJX...), banka, sanayi, ilaç, konut, enerji/emtia ALAN DIŞI: tweet atılmaz. 13F'te yalnız fonun teknoloji/yapay zekâ/uzay hamleleri anlatılır; bu alanda anlamlı hamlesi olmayan fon atlanır.
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
- Grafik ekran görüntüsü atarsa teknik analiz tweet taslağı (Claude paylaşmaz); okunamayan değer uydurulmaz.
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
- KESİN KURAL 25 (Enes 17.11 16:51, "insanlar bizi haberlere ulaşmak için takip ediyor ama asıl takip ettiği şey bizim fikirlerimiz, olaylara dair düşüncelerimiz"): Haberi vermek yetmez; her haber ve veri tweetinin ağırlığı YORUMDUR (yaklaşık üçte biri haber, üçte ikisi düşünce). Okur tweeti bitirdiğinde şu sorulara cevap almış olmalı: (1) Bu ne demek, sade dille? (2) Neden şimdi önemli, büyük resimde neye işaret ediyor (büyüme, enflasyon, tüketici, şirket kârları, yapay zekâ döngüsü)? (3) Fed ne düşünür, faiz beklentisi nasıl değişir (FedWatch/vadeli fiyatlama, 2 kaynak)? (4) Piyasaya, sektörlere ve takip edilen hisselere etkisi ne? (5) Bizim net düşüncemiz ne? Makro veri tweeti TEK tweet olsa bile bu beşini içerir; ayrı 'sonuç' ve 'etki' tweeti yerine tek, yorumlu tweet. Bilanço rakam tweeti yorumsuz kalır ama 15 dk sonraki analiz tweeti bu beş soruyu cevaplar. Görüş etiketsiz, düz cümleyle (kural 11), al/sat yok, tahmin dili ölçülü. Şablon: invest/sablonlar.md bölüm 7.
- DETAYLI ANALİZ (kesin kural 45, Enes 18.11 07:40): bilanço sonrası analiz ve bir hisse üzerine her analiz/uzun görüş yazısı ÇOK DETAYLI ve ÇOK KAYNAKLI: 10-15 kısa paragraf, en az 6 bağımsız kaynak (en az 4 tür: şirket belgesi, görüşme, 2+ haber kuruluşu, 2+ analist kurumu, konsensüs/veri sitesi), 13 maddelik içerik sırası ve gönderim öncesi kontrol. Tam yöntem: `enes-bilanco-13f` skill'i "Detaylı analiz yazısı" bölümü. Enes'e mesajda kaynak listesi (link) verilir.
- Görüş zorunlu (bilanço rakam tweeti hariç). Enes'in en sevdiği tarz: haberi tekrar etmek yerine arkasındaki yapıyı anlatan, olayları birbirine bağlayan "bağlam + görüş" (ORNEKLER 18).
- ARAÇ KONTROLÜ ZORUNLU (kural 11-B, Enes 18.11 14:55: "benim görüşüm: ifadesini kullanmayacaksın, yasaklanmıştı"): HER Buffer create_post'tan önce metin `python3 invest/yasak.py <<'EOF' ... EOF` ile taranır; çıkış 1 (YASAK VAR) ise tweet ATILMAZ, düzeltilip yeniden taranır. Uzun analiz ve düzeltme tweetleri dahil; düzeltme cümlesi "Not:" ile değil düz cümleyle başlar.
- CÜMLE ORTASI ETİKET YASAK (Enes 18.11 17:26: "yine de yön net: vs kullanımları istemiyorum"): paragraf başı gibi cümle başında da iki noktayla açılan ara cümle yok ("Yine de yön net:", "Mesele şu:", "Fark şu:", "Tablo net:"); düz cümle kurulur. `python3 invest/yasak.py` her cümlenin ilk 6 kelimesini tarar.
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
- Her turda tweetten sonra portföy taraması: `python3 ta2.py DOCN RKLB SITM AXON CBRS VRT AVGO > /tmp/ta.txt` (pipe ile head kullanma, BrokenPipe) + Chrome bağlıysa TradingView okuma; önceki duruma göre değişiklik, ekleme fırsatı, azaltma işareti ya da portföy dışı fırsat varsa Enes'e "ben olsam" notu (dil ve yöntem `enes-portfoy-analiz`). Değişiklik yoksa mesaj zorunlu değil.

Tarayıcı: Enes'in X hesabına ve x.com'a HİÇBİR ŞEKİLDE girilmez. Chrome yalnız tradingview.com ve haber/birincil kaynak okumak için (yeni sekme, get_page_text, iş bitince sekmeyi kapat, TradingView sekmesine dokunma). Form, giriş, abonelik, yorum, paylaşım yok; çerez bannerında en gizli seçenek.

Hata durumları: Bash "classifier no verdict" → 1 kez tekrar, olmazsa o tur paylaşma, 5-10 dk sonrasına kur. WebFetch PROVENANCE_REQUIRED → tekrar deneme, WebSearch. Buffer hata → 1 kez tekrar, olmazsa DONGU'ya yaz ve atla. Push reddi → görselsiz tweet atma. Buffer aylık ~1000 gönderi; 900'ü geçerse Enes'e söyle.

## 7. Kayıt ve sonraki tur

- KURAL 47 (Enes 18.11 18:07: "her tweeti attıktan sonra bunu bana, beni piyasada geliştirebilmek için açıklayacaktın, ne anlama geliyor vesaire, bana da öğretecektin"): her tweetten hemen sonra Enes'e "Paylaşıldı (SS:DD): TÜR" + tweet metni + ÖĞRETİCİ "Ne anlama geliyor?" (4-7 madde): (1) tweetteki teknik terimleri sade dille açıkla, (2) neden önemli, (3) benzer haberi kendisi görünce neye bakmalı (hangi satır, hangi kıyas, hangi tuzak), (4) Nasdaq / yapay zekâ teması / portföy bağlantısı, (5) izlenecek 1-2 somut şey. Kaynak ve tek kaynak notu ayrı bir satır.

1. `DONGU.md`'ye satır: `- SS:DD (GG.AA) AUTO (TÜR): dosya.jpg (düzen) - rakamlar (kaynaklar). Tek kaynak (atılmadı): ... Buffer <id>. Son 3 düzen: a, b, c.` 13F'de ayrıca `- 13F SERİSİ: <isim> atıldı / sıradaki: <isim>`.
2. commit + push.
3. `invest/DURUM.md`'yi güncelle (son 10 tweet, ticker saatleri, son 3 düzen, 13F sırası, bekleyenler), push. `python3 -c "import random;print(random.randint(20,40))"` ile gecikme; `send_later` adı "Otomatik paylaşım turu", mesaj = DEVIR_TAM kural 18'deki KISA ŞABLON (HESAP etiketi, bu turun konusu/sıradaki, son 3 düzen, ticker saatleri, bekleyen yayınlar). Uzun kural metni mesaja kopyalanmaz. 01:00 sonrasına düşerse 09:05.
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
- SABİT GÖREVLER (kural 15): tekrarlayan görev (create_trigger, cron, CRON_TZ=Europe/Istanbul): key levels + başlıklar 10:30 hafta içi, Pazar 20:00 takvim, Pazar 21:30 performans, çeyreklik 13F başlangıcı (15 Şubat, 16 Mayıs, 15 Ağustos, 15 Kasım 09:05), her gün 09:00 sabah kontrolü. Görev mesajları bağımsız ve tam yazılır (yeni oturumda ateşlenebilir). Rastgele aralıklı paylaşım turu zincir kalır; sabah kontrolü zincir koptuysa (son otomatik tur 60 dk'dan eski, 09:00-01:00) yeniden kurar ve Enes'e söyler.
- TAKVİM VE HIZ (kural 16): her tur başında `invest/takvim.md`'ye bak; önümüzdeki 60 dk içinde bilanço/veri varsa hazırlık (T-45/60 dk) ve yayın (T-2 dk) görevleri kurulu mu kontrol et, yoksa kur (ayrıntı `enes-bilanco-13f`). Bilanço ve saati belli veri başlıklarında bölüm 9'daki "+3 dk tek seferlik tur" yerine bu protokol uygulanır. Kurulacak otomatik tur bir yayın saatine ±15 dk denk geliyorsa yayından 20+ dk sonraya kur.
- KART: `skor` düzeni 1.8 kat logoyu taşımıyor; bilanço rakam kartı `uclu` (logo küçültme yasak).

## 11. Hesap kilidi (kesin kural 17, 17.11 13:11)

- Her tur, her görev, her bilanço yayını EN BAŞTA `invest/AKTIF_HESAP.md`'yi okur. Görev mesajındaki `HESAP=<etiket>` ile dosyadaki `AKTIF:` etiketi farklıysa HİÇBİR ŞEY yapma (tweet yok, push yok), kendi tekrarlayan görevlerini devre dışı bırak (update_trigger enabled=false), yeni görev kurma. Böylece eski hesabın görevleri yeni hesaba geçince kendiliğinden susar, çift tweet olmaz.
- Görev mesajları ve send_later mesajları her zaman `HESAP=<etiket>` içerir. Etiketi bilmiyorsan `AKTIF_HESAP.md`'deki aktif etiketi kullan.
- Hesap değişimi `invest/HESAP_DEVRI.md` ile yapılır.

## 12. Tasarruf, haftalık/aylık özet, gelecek hafta, düzeltme (kesin kural 18-21, Enes 17.11 13:28)

- OKUMA (kural 18): turda DEVIR_TAM ve DEVIR_OZET BAŞTAN OKUNMAZ. Okunan: bu skill + `invest/DURUM.md` + `tail -n 30 DONGU.md` (+ takvim.md). DEVIR_TAM'dan yalnız gereken bölüm grep ile.
- Buffer tekrar kontrolü first 5. WebSearch varsayılan standard (extended yalnız son dakika ilk araması boşsa). Turda portföy taraması kısa ta2 çıktısıyla; tam (-v) yalnız teknik kontrol ve key levels. Kart Read kontrolü bir kez.
- HAFTALIK ÖZET (kural 19): Cumartesi 11:00 sabit görev; endeksler haftalık %, en çok konuşulan 3 olay + kısa görüş, haftanın en iyi/en kötü büyük hissesi; tür HAFTALIK-OZET.
- GELECEK HAFTA (kural 20): Pazar 20:00 takvim görevi takvimden tek tweet + takvim kartı (en önemli 8-10 olay, gün + TSİ saat, beklenti 2 kaynak); tür TAKVIM. Aynı görev DONGU'da 7 günden eski satırları `invest/arsiv/`'e taşır.
- AYIN ÖZETİ (kural 21): ayın ilk ABD işlem günü 11:00; endeksler + takip edilen hisseler aylık % (portföy/ağırlık yazılmaz), en önemli 3 olay; tür AYLIK-OZET.
- DÜZELTME (kural 21): atılmış tweette hata çıkarsa Enes'e HEMEN mesaj, aynı gün sade düzeltme tweeti ("Az önceki $X tweetinde Y'yi Z yazdım, doğrusu W."), DONGU'ya "DUZELTME:" ve `invest/HATA_GUNLUGU.md` kaydı; tekrar eden hata türü için skill'e önlem maddesi.

## 13. Yeni içerikler ve yalnız doğrular kuralı (kesin kural 22-23, Enes 17.11 14:35)

- YALNIZ DOĞRU ÇIKANLAR (kural 23): tutmayan tahmin/beklenti/"ben olsam" tweette anılmaz; tutan tahmin bağlama uyuyorsa söylenebilir. Atılmış tweetteki yanlış RAKAM için kural 21 düzeltme aynen geçerli.
- ŞABLONLAR: sık türlerde `invest/sablonlar.md`'deki iskeleti doldur (cümleleri her seferinde değiştir). Makro veri tweetine `invest/makro_sozluk.md`'den tek cümle (A/B sırayla, DONGU'ya "sözlük: X-A").
- KARIŞIM: DURUM.md "İçerik karışımı" bölümü varsa konu seçimi ona uyar (Enes onaylı; Enes "karışım onay" yazınca rapordaki öneri oraya ve buraya işlenir).
- HER TURDA EK KONTROL: Yahoo ^TNX ve DX-Y.NYB + CME FedWatch; 10 yıllık ±8 baz puan, DXY ±%0,6 ya da toplantı olasılığında 15 puan üstü değişim varsa FED-TAHVIL tweeti (günde en fazla 1, şablon 8).
- TAKVİMDEN: kurumsal olaylar (halka arz, bölünme, büyük temettü, endeks giriş/çıkış) ve lansmanlar (GTC, Apple, re:Invent, CES, I/O, Build, Computex) günü gelince tweet (KURUMSAL / LANSMAN).
- BİLANÇO SONRASI: önizlemede opsiyon beklenen hareketi; ertesi gün açılıştan sonraki ilk turda portföy ve büyük şirketler için "beklenen ±%X, gerçekleşen %Y" (BEKLENEN-HAREKET); portföy/ilgi listesi bilançosunda rakip karşılaştırma kartı (RAKIP, panel/dortlu).
- 13F: seri bitince sonraki turda 13F-OZET (ortak alınan/satılan, en az 3 yatırımcı).
- MENÜ: ayda 2-3 kez "1 yıl önce bugün" (BIR-YIL, yalnız doğru çıkanlar).
- İLGİ LİSTESİ (genişledi): ON AAOI HOOD TEM CRDO PLTR ISRG ASTS MU + ANET ALAB MRVL COHR LITE ETN GEV CRWD NET DDOG APP RBRK PL LUNR. Zaman kalan turlarda günde 1-2 yeni adayın temel karnesini çıkar (`temel_karne.md`, /50); 30 altını DURUM.md'de "çıkarıldı" yap.
- Sabit görevler (kendileri yapar, turlar tekrar atmaz): içeriden alım + geri alım radarı hafta içi 14:20, sektör ısı haritası Cmt 13:25, ilgi listesi sıralama Cmt 16:25, bilanço sezonu karnesi Pazar 14:25, analist hedef özeti (ayın ilk Pazarı) ve değerleme bandı (ikinci Pazar) 12:25, mevsimsellik ayın ikinci işlem günü 11:00 (ayın özeti görevi).

## 8. Yeni kural gelince

Enes yeni bir kural verirse: `DEVIR_TAM.md`'ye kesin kural olarak (tarih + Enes'in sözü), `DEVIR_OZET.md`'ye bir satır, bölüm 18 kayıt tablosuna satır, `DONGU.md`'ye ENES satırı ekle, push et; bu skill'in güncellenmesini `propose_skills` (improvement) ile öner ve aynı değişikliği `invest/skills/` kopyasına da yaz.

## Ders sistemi (kesin kural 26, Enes 17.11 17:18 + 17:24)
Tam protokol `invest/DERSLER.md` başında (veri, ölçü, eşik, çakışma, yaşam döngüsü, takvim). Özet:
- Tur başında DERSLER.md "AKTİF DERSLER" + "OPERASYON DERSLERİ" okunur ve uygulanır.
- Tweet atınca `invest/performans_veri.csv`'ye satır (metrik boş; kaynak=sistem, kesin tür, görüş evet/hayır, düzen, Buffer id). Sabah 09:00 görevi metrikleri Buffer'dan doldurur.
- Ders yalnız `python3 invest/ders_analiz.py` ile çıkar: göreli skor (görüntülenme / önceki 7 gün medyanı), grup medyanı. Eşik: ≥8 tweet, ≥2 hafta, ≥%25 fark, haftalar aynı yön → ADAY; 3. hafta da tutarsa AKTİF (adet/karışım değişikliği Enes onayıyla, saat/kart/uzunluk gibi küçükler otomatik ve Pazar raporunda bildirilir). Tek viral tweet ders değildir; 12 saatten taze tweet ölçülmez.
- Çakışma: Enes talimatı > kesin kurallar > Enes onaylı ders > otomatik ders > aday > gözlem. Yeni bulgu eski dersle çelişirse eski hemen silinmez: ÇELİŞKİ işaretlenir, 1-2 haftalık A/B deney kurulur, kazanan kalır, kaybeden "Silinen dersler"e tarih ve gerekçeyle taşınır (Enes onaylı dersin yerine geçecekse Enes'e sorulur). Farklı kapsam (sezon, gün tipi) çatışma değildir, kapsamlı iki ders olur; dar kapsam genel dersi o kapsamda geçer. Eşit kanıtta yeni veri öncelikli.
- Her aktif ders 4 haftada bir yeniden test edilir; 2 kez tutmazsa silinir. En çok 15 aktif ders. Tweetlerin %10-15'i keşif (yeni tür/saat/biçim), DONGU'da "(keşif)".
- Pazar 21:30: `ders_analiz.py` + Enes'e "bu hafta öğrendiklerim" (rakamlı; eklenen, silinen, çatışan ders). Operasyon dersleri (hatalardan, O-xxx) metrikle değil hata günlüğüyle eklenir.
- Dersler kesin kuralları değiştirmez (al/sat yok, 2 kaynak, kural 23, 25); yalnız konu, saat, biçim, adet, kart tercihlerini değiştirir.

## 9. Periyot defteri (kesin kural 24, Enes 17.11 16:33)
Sohbet her gün değişebilir; yeni sohbet "en son ne zaman yapıldı, bu hafta kaç kez yapıldı" bilgisini hafızadan bilemez. Haftada/ayda/N günde bir ya da "en çok/en az N kez" kuralı olan her iş `invest/periyot.json` defterine göre yapılır, tahminle değil.
- Tur ve görev başında `python3 periyot.py durum` (UYGUN/BEKLE ve "YAPILMALI" olanlar). Tek iş: `python3 periyot.py kontrol <anahtar>` (çıkış 0 = uygun).
- İş yapılınca hemen `python3 periyot.py yap <anahtar> "<kısa not>"`, sonra commit + push (DONGU satırıyla aynı commit).
- Makro sözlük cümlesi: `python3 periyot.py sozluk "<Veri adı>"` hangi varyasyonu (A/B) kullanacağını söyler (14 gün tekrar yok); kullanınca `yap sozluk:<Veri>-<A|B>`.
- Karne yazınca `yap karne <hisse>`; kalibrasyon UYGUN olunca yapılır ve `yap kalibrasyon`.
- Yeni periyodik kural gelirse (ör. "üç haftada bir"): `python3 periyot.py ekle <anahtar> min_gun 21 "<açıklama>"`. Türler: min_gun, gunluk_max, haftalik_min/max, aylik_min/max, ayin_pazari, baslangic_gun, her_n.
- Sabit görevler (cron) hesaba bağlıdır, sohbet değişince silinmez; saatleri cron'dan gelir, "bu hafta/bu ay zaten yapıldı mı" kontrolünü periyot.py ile yapar. Devirde yalnız oturuma bağlı send_later zinciri yeniden kurulur.
- ETİKETLİ TEKRAR KONTROLÜ (17.11 21:35, Enes: "farklı sohbete geçince tarihleri bilemez, kalıcı çözüm"): "son N günde / son N kayıtta aynısı olmasın" kuralları da hafızadan değil periyot.json'dan: `python3 invest/periyot.py etiket kontrol <grup> <değer> <gün> [son_n]` (çıkış 0 = uygun), kullanınca `etiket yap <grup> <değer>`. Gruplar: aday (teknik analiz adayı, 5 gün), cerceve (uzun yazı çerçevesi, son 3 kayıt: `etiket kontrol cerceve B 0 3`), uzun_ticker (uzun yazı hissesi, 30 gün). Yeni benzer kural gelirse yeni grup açılır. Haftalık alt sınırı olan işler (uzun_gorus, egitici) `periyot.py durum`da "YAPILMALI" ya da geride kalınınca "ACIL BUGUN YAP" yazar; tur_basi.sh bunu her turda gösterir, tur o işi o gün planlar.
- DONGU.md 7 günde arşive taşındığı için "son 2 hafta / bu ay" sorusunun cevabı DONGU'dan değil defterden alınır.

## Uzun görüş yazısı (kesin kural 32, Enes 17.11 21:13)
- Arada sırada (haftada 2-3, aralarında en az 2 gün; `python3 invest/periyot.py kontrol uzun_gorus`) tek uzun tweet. Örnek: Enes'in "GÜNCELLENMİŞ $NBIS DÜŞÜNCELERİM" metni (invest/ORNEK_UZUN_NBIS_Enes.txt), kalıp ORNEKLER.md bölüm 21, şablon sablonlar.md 20. Metin kopyalanmaz, yapısı alınır.
- Konu: portföy, ilgi listesi ya da büyük yapay zekâ/yarı iletken/bulut şirketi; tercihen duyarlılığın sert değiştiği, çok konuşulan bir hisse.
- Yapı TEK DEĞİL (Enes 17.11 21:30: "farklı yapılardan olabilir, hep aynı yaparsan hepsi aynı olur"): her yazı invest/sablonlar.md bölüm 20'deki 10 çerçeveden biriyle yazılır ve son 3 uzun yazıda kullanılan çerçeve tekrar edilmez (DURUM.md "Uzun yazı çerçeveleri"); aynı ticker 30 gün içinde yeni gelişme olmadan tekrar yazılmaz; başlık, paragraf sayısı (5-10), açılış ve kapanış her seferinde değişir. Çerçeveler: A) güncellenmiş düşünceler (duyarlılık dönüşü, NBIS örneği); B) boğa ve ayı (3'er argüman, rakamla, sonra tartımız); C) tek rakamın hikâyesi (şirketi tek metrikle anlatmak); D) iki şirket aynı soru (rakip kıyası); E) tez kontrolü (4-5 madde bugünkü verilerle; tutmayan eski tahmin anılmaz); F) kalabalığın gözden kaçırdığı tek nokta; G) değer zinciri (bir olayın tedarikçi, müşteri, rakip, enerji/altyapı üzerindeki etkisi); H) 12 aylık üç senaryo (kötü/baz/iyi, tetikleyiciler; hedef fiyat yok); I) yönetim ve sermaye dağıtımı (söyledikleri ve yaptıkları); J) tarihten benzer dönem (benzerlik ve farklar rakamla). DONGU satırına "çerçeve: X", performans_veri.csv konusuna "[X]" öneki (ders sistemi çerçeveleri ayrıca ölçer).
- Her rakam 2 kaynak. YASAK: al/sat tavsiyesi, "aldım / alım yapıyorum", pozisyon ve ağırlık, hedef fiyat, emoji, hashtag, link, soruyla bitirme, etiketli görüş girişi, deyim/mecaz (sade dil), tutmayan eski tahmin.
- Kart editoryal ya da panel; zaman 21-24 ya da 12-15; tür UZUN-GORUS (DONGU + performans_veri.csv; ders sistemi ayrıca ölçer). Yayından sonra `python3 invest/periyot.py yap uzun_gorus`.

## Kredi tasarrufu (kesin kural 28, Enes 17.11 17:41: "tüm talimatlar harfiyen çalışmaya devam edecek; hiçbir şey değiştirmeden, ekleyerek tasarruf sağla")
Bu bölüm HİÇBİR kuralı kaldırmaz ya da gevşetmez; aynı işi daha az araç çağrısı ve daha az okuma ile yapma yollarıdır. Çelişkide KURAL kazanır.
1. Tur başı tek çağrı: `bash invest/tur_basi.sh A` (git pull, hesap kilidi, DURDUR, saat, DURUM ilk 60 satır, DONGU son 30, son paylaşım saatleri, aktif + operasyon dersleri, periyot uyarıları, bugün/yarın takvimi, gündem, vadeli/faiz/dolar). Çıkış 2 = kilit, 3 = DURDUR → dur.
2. Kart yayını tek çağrı: `bash invest/yayinla_gorsel.sh g/<dosya>.jpg` (commit + pull --rebase + push + raw URL 200, 3 deneme). "OK" yazmazsa görselsiz tweet atılmaz.
   KURAL 77 (F-007, Enes 24.11 20:24): kart 'LOGO DOGRULANMADI' uyarısı verirse kart Read ile kontrol edilir; logo doğruysa `python3 invest/logo_dogrula.py ekle <T>`, yanlışsa logo/<T>.png silinir ve kart logosuz çizilir. Doğrulanmış liste logo/DOGRULANDI.txt.
   KURAL 78 (F-008, Enes 24.11 20:24): haber yazılmamış gün içi hareket tweete girmeden `python3 invest/fiyat_teyit.py <T> <ikinci_kaynak_%> "<kaynak>"` (ikinci kaynak WebSearch '<T> stock today' sonucu ya da haber); fark ≤0,5 puan net rakam, değilse 'civarı' + DONGU notu.
   KURAL 79 (F-009, Enes 24.11 20:29): günün ÇİFT sıradaki sistem tweetleri 'iddia açılışı' ile yazılır: ilk satır ≤12 kelime, birinci tekil şahıs ya da net hüküm, rakamla başlamaz; rakamlar ikinci paragraftan. Tek sıradakiler mevcut açılışla. kalite.py kaydet açılış tipini yazar; kayit.py --konu başına [A:iddia]/[A:normal]. A/B 08.12'ye kadar; iddia ≥%20 öndeyse tüm tweetlere geçer.
   KURAL 80 (F-010, Enes 24.11 20:29): günde 2-3 ALINTI tweet: büyük şirket/haber hesabının (RocketLab, nvidia, CNBC, Reuters vb.) önemli paylaşımına Buffer create_post metadata.twitter.retweet {id: '<id>'} ile; metinde haber tekrar edilmez, yalnız bizim ek verimiz (2 kaynak, kural 74) + kart. id yalnız WebSearch sonucundaki x.com/.../status/<id> bağlantısından; x.com'a girilmez, id tahmin edilmez, bulunamazsa normal tweet. Anthropic ya da siyasi hesap alıntılanmaz. --konu başına [ALINTI].
   KURAL 72 (F-004, Enes 24.11 11:36): betik kartla birlikte invest/ altındaki bekleyen her değişikliği (is_defteri.json, logo/, kalite ve kayıt dosyaları) de commit'ler; commit'lenecek bir şey yoksa hata vermez. "PUSH HATA" görülürse DONGU'ya yazılır.
   KURAL 66-71 (24.11): sonuç takibi (skill enes-sonuc-takibi), geliştirme fikirleri (skill enes-gelistirme-fikirleri), Enes taslak 12-15 ve 21-24 (skill enes-taslak), bilanço başına en fazla 6 tweet ve veriyle dağılım, belirleyici kalem (skill enes-bilanco-13f). Ayrıntı KURAL_DIZINI.md.
   KURAL 75 (F-005, Enes 24.11 18:33): resmi kurum bültenindeki alt kalemler tek başına bültenden yazılabilir (manşet rakam ve beklenti yine 2 kaynak; skill enes-analiz-kalitesi).
   KURAL 76 (F-006, Enes 24.11 18:33): iş defteri kaydı `isler.py ekle <ID> "<ad>" <YYYY-AA-GGTSS:DD> "<ne>" [--ticker T] [--tur tur|test|tek]`; sıra ad → zaman. Betik tarihi doğrular, ad/zaman yer değiştirmişse düzeltir, tarih yoksa reddeder.
3. Tweet sonrası kayıt tek çağrı: `CS=<oturum linki> python3 invest/kayit.py --saat .. --tur .. --konu .. --duzen .. --buffer .. --dosya .. --gorus evet --dongu "<kaynaklar ve rakamlar>" [--hak serbest|ayrilan|yok] [--periyot sozluk:X-A]` → DURUM sayacı + KULLANILAN + Son 3 düzen + DONGU + performans.md + performans_veri.csv + periyot + commit/push. DONGU içeriği aynı ayrıntıda yazılır.
4. Bağımsız çağrılar paralel (WebSearch x2-3, Yahoo + git + periyot); gereken tüm ertelenmiş araçlar TEK ToolSearch'te.
5. Okuma ekonomisi: DEVIR_TAM ve skill kopyaları baştan okunmaz, `grep -n` ile ilgili satır; düzenlenen dosya tekrar okunmaz; büyük çıktılar dosyaya yazılıp python/jq ile süzülür (teknik kontrolde ta2 tam çıktısının tamamı yine okunur).
6. Arama ekonomisi: WebSearch önce "standard", "extended" yalnız zayıf/eski sonuçta; bir aramada iki kaynak çıktıysa ek arama yok; hazırlık turunda bulunan beklentiler yayın turunda yeniden aranmaz.
7. Chrome ekonomisi: önce `get_page_text`, olmazsa ekran görüntüsü; okumak için `scale: 0.5`, Enes'e gidecek görüntü tam çözünürlük + zoom; çoklu tıklama/gezinme `browser_batch` ile.
8. Buffer: tekrar kontrolü `list_posts first 5` metriksiz; metrikler yalnız sabah görevinde, sonuç dosyaya yazılıp işlenir.
9. Kart bir kez Read ile kontrol; bilinen sorunlu düzenler (skor/bento + logo) baştan seçilmez.
10. Enes'e mesajlar istenen bölümlerle (tweet + "Ne anlama geliyor?" 3-6 madde), tekrarsız.
11. Zincir mesajı kısa şablonla; her turda yalnız değişen bilgiler güncellenir.

## Paylaşım saati, günlük adet ve aralık (kesin kural 42, Enes 18.11 01:13 + 01:15 + 01:18) — eski saat/adet/aralık kurallarının yerine
- Tweet penceresi 11:00-02:00 TSİ; paylaşım günü 02:00'de biter. 02:00-11:00 tweet yok (istisna: saati belli bilanço/veri rakam yayınları ve bilanço detay tweetleri). 09:00 sabah kontrolü tweet atmaz; vadeliler 11:00 günün başlıkları tweetinde.
- Pazartesi-Cumartesi günde EN AZ 30, EN ÇOK 40 tweet (Enes istekleri ve bilanço tweetleri dahil; 40'ı yalnız Enes isteği aşabilir). Pazar: alt sınır yok, üst sınır Enes rakam verene kadar 40. Eski 12-15 ve 15 sınırları geçersiz.
- ARALIK SERBEST: tweetler arasında sabit aralık yok (1 dk da olabilir 1 saat de); eski 20 dk / 20-40 dk / seri aralıkları kaldırıldı. Aralığı haberin önemi/tazeliği, 30-40 hedefi ve kalan süre belirler; bir sonraki tur zamanını her turda Claude seçer.
- 18:00-21:00 arası tweet sınırı YOK (D-003 iptal, Enes 18.11 01:18).
- Otomatik tur 11:15'te başlar; her tur en az bir tweet atar. `tur_basi.sh` günün sayısını ve kalan süreyi rehber olarak gösterir. Kalite kuralları (2 kaynak, kural 23/25, tekrar yok, aynı ticker 3 saatte bir) aynen.

## Paylaşım saati, günlük adet ve aralık (kesin kural 42, Enes 18.11 01:13 + 01:15) — eski saat/adet/aralık kurallarının yerine
- Tweet penceresi 11:00-02:00 TSİ; paylaşım günü 02:00'de biter. 02:00-11:00 tweet yok (istisna: saati belli bilanço/veri rakam yayınları ve bilanço detay tweetleri). 09:00 sabah kontrolü tweet atmaz; vadeliler 11:00 günün başlıkları tweetinde.
- Pazartesi-Cumartesi günde EN AZ 30, EN ÇOK 40 tweet (Enes istekleri ve bilanço tweetleri dahil; 40'ı yalnız Enes isteği aşabilir). Pazar: alt sınır yok, üst sınır Enes rakam verene kadar 40. Eski 12-15 ve 15 sınırları geçersiz.
- ARALIK SERBEST: tweetler arasında sabit aralık yok (1 dk da olabilir 1 saat de). "Son paylaşımdan 20 dk geçmediyse paylaşma", "20-40 dk" gibi bütün eski aralık kuralları kaldırıldı. Aralığı haberin önemi/tazeliği, 30-40 hedefi ve kalan süre belirler; bir sonraki tur zamanını her turda Claude seçer. Birbirine bağlı konular aynı turda arka arkaya atılabilir.
- Otomatik tur 11:15'te başlar; her tur en az bir tweet atar. `tur_basi.sh` günün sayısını, kalan süreyi ve ortalama gereken aralığı rehber olarak gösterir. Kalite kuralları (2 kaynak, kural 23/25, tekrar yok, aynı ticker 3 saatte bir) aynen.

## Paylaşım saati ve günlük adet (kesin kural 42, Enes 18.11 01:13) — eski saat/adet kurallarının yerine
- Tweet/tur penceresi 11:00-02:00 TSİ; paylaşım günü 02:00'de biter. 02:00-11:00 tweet yok (istisna: saati belli bilanço/veri rakam yayınları ve bilanço detay tweetleri). 09:00 sabah kontrolü tweet atmaz; 09:05 vadeli tweeti kaldırıldı, vadeliler 11:00 günün başlıkları tweetinde.
- Pazartesi-Cumartesi günde EN AZ 30, EN ÇOK 40 tweet (Enes istekleri ve bilanço tweetleri dahil; 40'ı yalnız Enes isteği aşabilir). Pazar: alt sınır yok, üst sınır Enes rakam verene kadar 40. Eski 12-15 (D-002) ve 15 sınırı geçersiz; 18-21 arası en çok 2 korunur, 30'un altında kalma riski varsa 4'e kadar.
- Otomatik tur 11:15'te başlar, turlar arası rastgele 18-28 dk, her tur bir tweet atar (değerli haber yoksa menü: eğitici, karşılaştırma, bir yıl önce, 13F, uzun görüş, analist notu, içeriden alım, sektör, emtia/dolar/kripto). `tur_basi.sh` günün sayısını, kalan süreyi ve gereken tempoyu gösterir; gerekirse aralık 12-15 dk'ya iner. Kalite kuralları (2 kaynak, kural 23/25, tekrar yok, aynı ticker 3 saatte bir) aynen.

## Teknik analiz yok (kesin kural 37, Enes 17.11 22:17)
- Claude kendi teknik analizini yapmaz: 18:00/23:30 teknik kontroller, TradingView, ekran görüntüleri, göstergeler, çizimler, key levels seviyeleri ve turlardaki ta2 taraması kaldırıldı. Bu skill'de teknikle ilgili eski satırlar geçersizdir.
- 18:00 ve 23:30 analiz görevleri YOK (kesin kural 44, 18.11); 10:30 seviyesiz "günün başlıkları"; turlarda portföy haber taraması.

## Enes'in teknik analizinden tweet (kesin kural 38, Enes 17.11 22:30: "artık teknik analizi ben sana atacağım, sen de tweet yazım kurallarına bakıp sade dilde, mecaz kullanmadan yazacaksın ve bana tweeti yollayacaksın")
- Enes teknik analizini (metin, sesli not ya da grafik) atınca Claude kendi analizini yapmaz, gösterge/seviye eklemez, Enes'in seviye ve görüşlerini değiştirmez; yalnız tweet diline çevirir.
- Yazım kuralları aynen: sade cümle; deyim/mecaz yok ("hikâye değişir", "resim bozulur", "asıl sınav", "kapı açılır" yerine "69'un altında günlük kapanış gelirse düşüş devam edebilir"); terimler sade (FVG = boşluk, order block = alıcıların daha önce toplandığı bölge); etiketli giriş ve "X şu:" yok; emoji, hashtag, mention, link yok; soruyla bitmez; okura emir kipi ve al/sat tavsiyesi yok; portföy/tutar/ağırlık yok.
- Okunamayan değer uydurulmaz; eksik ya da çelişkili bir şey varsa Enes'e tek cümle not.
- Çıktı: Enes'e SendUserMessage ile kopyalanmaya hazır tweet (gerekirse 1 kısa alternatif). Claude PAYLAŞMAZ, Buffer'a göndermez. DONGU'ya "- SS:DD ENES-TA-TASLAK: <ticker>".

## Teknik analiz yok (kesin kural 37, Enes 17.11 22:17: "teknik analize bakmıyoruz bir daha, onunla alakalı her şeyi kaldır, onun yerine temel analize daha da yoğunlaş")
- Kaldırıldı: 18:00/23:30 teknik kontroller, TradingView ve ekran görüntüleri, teknik tweet taslakları, gösterge rotasyonu, çizimler, ta_ek ve seviye karnesi, key levels tweetindeki destek/direnç, turlardaki ta2 portföy taraması. ta2.py/ta_ek.py kullanılmaz. Bu skill'de teknikle ilgili eski satırlar geçersizdir.
- 18:00 ve 23:30 analiz görevleri YOK (kesin kural 44, 18.11; karne, tez kartı, ben olsam notları turlarda aynen sürer). 10:30 görevi seviyesiz "günün başlıkları" tweeti + takvim + hazırlık/yayın görevleri.
- Turlarda tweetten sonra 7 portföy hissesinde haber/8-K/Form 4/analist taraması; teze dokunan gelişme varsa Enes'e kısa "ben olsam" notu (değerleme bölgesi + tez durumu).
- Tweetlerde grafik/teknik görüş yok; görüş temel veriye dayanır.

## Her şey bu sohbete (kesin kural 29) ve sistem tutarlılığı (kesin kural 36)
- Sabit görevler bu sohbette send_later zinciri: çalışınca İLK İŞ `python3 invest/sonraki.py <anahtar>` → aynı mesajla send_later (aynı adlı bekleyen varsa kurma), sonra `invest/gorevler/_ORTAK.md` + `invest/gorevler/<anahtar>.md`.
- Günlük adet: sistem tweeti günde en çok 15 (`periyot.py kontrol tweet_gunluk`), 18-21 en çok 2; Enes'in o güne verdiği adet kuralı varsa o geçerli. Bugünlük blok yalnız kendi tarihinde (gün 01:00'de biter).
- Skill ile `invest/skills/` kopyası çelişirse kopya geçerli.
- 60 dk içinde YAYIN görevi varsa ağır görevler yayından 15 dk önce biter.

## Her şey bu sohbete (kesin kural 29, Enes 17.11: "her şeyin bu sohbete gelmesi lazım")
- 14 sabit görev bu sohbette send_later ZİNCİRİDİR (bulut cron'ları kapalı). Zincir mesajı çalışınca İLK İŞ `python3 invest/sonraki.py <anahtar>` → verdiği zamana, verdiği adla ve AYNI mesajla send_later (list_triggers'ta aynı adlı bekleyen varsa kurma); sonra `invest/gorevler/_ORTAK.md` + `invest/gorevler/<anahtar>.md` harfiyen. `python3 invest/sonraki.py hepsi` bütün zincirlerin sıradaki zamanını verir.
- Otomatik tur, hazırlık/yayın/analiz görevleri de bu sohbette send_later; Enes'e giden her şey SendUserMessage / SendUserFile.

## Sistem tutarlılığı (kesin kural 36, Enes 17.11 21:46)
- TUR ve ADET: otomatik tur 20-40 dk aralıkla döner ama tweet atma kararı D-002/D-003'e bağlıdır: sistem tweeti günde en çok 15 (`python3 invest/periyot.py kontrol tweet_gunluk`), 18-21 arası en çok 2. Hedef dolduysa ya da değerli konu yoksa tur paylaşmadan geçer, zamanı karne/aday/uzun yazı hazırlığına kullanır. Enes'in o güne verdiği adet kuralı varsa o gün o geçerli. Enes'in istediği tweetler ve bilanço/veri yayınları her zaman atılır. `tur_basi.sh` "BUGUN SISTEM TWEETI" satırı sayıyı gösterir; `kayit.py` sayacı otomatik artırır.
- GÜNE ÖZEL BLOK: DURUM.md "BUGÜNLÜK KURAL" bloğu yalnız başlığındaki tarihte geçerli (paylaşım günü 01:00'de biter); kayit.py başka günde sayacı düşürmez; 09:00 sabah kontrolü eski bloğu siler.
- SKILL ile KOPYA: bu skill ile `invest/skills/` kopyası ya da DEVIR_TAM kesin kuralları çelişirse kopya ve en yeni kesin kural geçerli; şüphede ilgili bölüm grep ile okunur.
- GÖREV ÇAKIŞMASI: tek oturum sırayla çalışır; 60 dk içinde bilanço/veri YAYIN görevi varsa ağır görev (teknik analiz, karne, uzun yazı) yayından en az 15 dk önce bitecek şekilde kısaltılır; kapanış gibi kısa görevler 10 dk içinde biter.
- KART: isi ve siralama 17.11'de düzeltildi (siralama negatif değer çizer, isi logoya çarpan ticker yazısını gizler; LOGO_BUYUT 1.8 korunur). Her kart Read ile kontrol.
- ÖLÇÜM FARKI: ta2.py ile TradingView arasında %2'den büyük fark varsa TradingView esas; DONGU'ya "TA-FARK".
- PAZAR DENETİMİ: performans raporundan sonra zincirler (sonraki.py hepsi vs list_triggers), DURUM.md boyu (100 satır üstü arşive), HATA_GUNLUGU

## KURAL 85 — Hisse-tahvil ayrışma ölçüsü (Enes 25.11.2026 18:02)
- Her tur başında `tur_basi.sh` içinden `python3 invest/ayrisma.py --sessiz` çalışır (Nasdaq 100 % vs 10Y faiz bp, Yahoo canlı).
- SİNYAL: NDX <= −%1 ve 10Y <= −3 bp -> satış faizle açıklanmıyor; turun 1. tweet adayı risk tweeti. TERS SİNYAL: NDX >= +%1 ve 10Y >= +5 bp -> büyüme iyimserliği tweeti adayı.
- Aynı gün aynı sinyal için en çok 1 tweet. Yazım somut (hangi hisse, ne kadar, kaç bp). Kart haber_dosya.

## KURAL 86 — Beğeni + profesyonellik paketi (Enes 25.11.2026 18:05 'HEPİSİ KABUL', 18:08 sayı düzeltmesi)
Veri (351 tweet): sistem ort. 2,3 beğeni, Enes 5,8, portföy 12,7, eğitici 5,8.
- (a) GÜNLÜK SAYI: HAFTA İÇİ EN AZ 18, EN ÇOK 26 sistem tweeti; HAFTA SONU (Cmt-Paz) EN ÇOK 10, alt sınır yok. Eski 30-50 / 30-40 / Pazar 10 sayıları GEÇERSİZ. Tur aralığı 20-35 dk, turda 1 tweet (güçlü konu varsa 2). 18'in altı ancak 02:00'de güçlü konu kalmadıysa, DONGU'ya gerekçe. kalite.py hafta içi 26, hafta sonu 10'da durdurur.
- (b) ENES SESİ: ilk satır Enes'in birinci tekil, iddialı, somut tonunda (54-F'ye takılmadan); kibir/hakaret yok.
- (c) PORTFÖY DOSYASI günde 2: Enes'in hisselerinden derin tweet + kart3 dosya; öncelik 13:00 ve 20-23.
- (d) AKŞAM EĞİTİCİ günde 1 (20-23): 'X nedir, neden önemli, bugün nerede', güncel olaya bağlı.
- (e) SAAT: en güçlü tweetler 13, 17, 20-23; 10, 15, 19 ve 00-01 yalnız zorunlu/son dakika.
- (f) KISA VE TEK FİKİR: ilk satır en çok 12 kelime, en çok 3 farklı rakam (5 üstü hata), en çok 3 paragraf; fazla rakam karta (kalite.py denetler; bilanço rakam/olaylar/keylevels muaf).
- (g) HAFTALIK KARNE Cumartesi 20:25 sabit görev `karne` (gorevler/karne.md): YALNIZ TUTAN yorumlar paylaşılır (Enes 18:06); tutmayanlar yalnız DONGU iç notu, isabet oranı yazılmaz; tutan 2'den azsa atılmaz.
- (h) GÜNCELLEME: 2 saatte 2.000+ gösterim ya da 15+ beğeni alan tweete yeni veri gelirse 20-60 dk içinde kısa güncelleme ('Saat SS:DD tweetine güncelleme:'), günde en çok 2.
- Ölçüm: 2 hafta, performans_veri.csv sistem beğeni ortalaması 2,3'ten yukarı.

## KURAL 85 — Hisse-tahvil ayrışma ölçüsü (Enes 25.11.2026 18:02)
- Her tur başında `tur_basi.sh` içinden `python3 invest/ayrisma.py --sessiz` çalışır (Nasdaq 100 % vs 10Y faiz bp, Yahoo canlı).
- SİNYAL: NDX <= −%1 ve 10Y <= −3 bp -> satış faizle açıklanmıyor; turun 1. tweet adayı risk tweeti. TERS SİNYAL: NDX >= +%1 ve 10Y >= +5 bp -> büyüme iyimserliği tweeti adayı.
- Aynı gün aynı sinyal için en çok 1 tweet. Yazım somut (hangi hisse, ne kadar, kaç bp). Kart haber_dosya.

## KURAL 86 — Beğeni + profesyonellik paketi (Enes 25.11.2026 18:05 'HEPİSİ KABUL')
Veri (351 tweet): sistem ort. 2,3 beğeni, Enes 5,8, portföy 12,7, eğitici 5,8.
- (a) GÜNLÜK TAVAN 20 sistem tweeti (eski 30-50 hedefi kalktı). Hedef 15-20 güçlü tweet; zayıf konu varsa tur tweetsiz biter. kalite.py 20'de durdurur.
- (b) ENES SESİ: ilk satır Enes'in birinci tekil, iddialı, somut tonunda (54-F'ye takılmadan); kibir/hakaret yok.
- (c) PORTFÖY DOSYASI günde 2: Enes'in hisselerinden derin tweet + kart3 dosya; öncelik 13:00 ve 20-23.
- (d) AKŞAM EĞİTİCİ günde 1 (20-23): 'X nedir, neden önemli, bugün nerede', güncel olaya bağlı.
- (e) SAAT: en güçlü tweetler 13, 17, 20-23; 10, 15, 19 ve 00-01 yalnız zorunlu/son dakika.
- (f) KISA VE TEK FİKİR: ilk satır en çok 12 kelime, en çok 3 farklı rakam (5 üstü hata), en çok 3 paragraf; fazla rakam karta (kalite.py denetler; bilanço rakam/olaylar/keylevels muaf).
- (g) HAFTALIK KARNE Cumartesi 20:25 sabit görev `karne` (gorevler/karne.md): YALNIZ TUTAN yorumlar paylaşılır (Enes 18:06 'tutmayanları paylaşma sadece tutanlar'); tutmayanlar yalnız DONGU iç notu, isabet oranı yazılmaz; tutan 2'den azsa atılmaz.
- (h) GÜNCELLEME: 2 saatte 2.000+ gösterim ya da 15+ beğeni alan tweete yeni veri gelirse 20-60 dk içinde kısa güncelleme ('Saat SS:DD tweetine güncelleme:'), günde en çok 2.
- Ölçüm: 2 hafta, performans_veri.csv sistem beğeni ortalaması 2,3'ten yukarı.

## KURAL 85 — Hisse-tahvil ayrışma ölçüsü (Enes 25.11.2026 18:02 kabul)
- Her tur başında `tur_basi.sh` içinden `python3 invest/ayrisma.py --sessiz` çalışır: Nasdaq 100 % değişimi ile 10 yıllık faizin (^TNX) bp değişimi, Yahoo canlı.
- SİNYAL: NDX <= −%1 ve 10Y <= −3 bp (hisse ve faiz birlikte düşüyor) -> satış faizle açıklanmıyor; o turun 1. tweet adayı büyüme/risk tweeti.
- TERS SİNYAL: NDX >= +%1 ve 10Y >= +5 bp -> büyüme iyimserliği tweeti adayı.
- Aynı gün aynı sinyal için en çok 1 tweet (ilk görüldüğünde); sonrası yalnız belirgin değişimde.
- Yazım 54-F: soyut 'X'in yansıması / genel kaçış' YOK; somut yaz: hangi hisseler, ne kadar, faiz kaç bp.
- Rakam tek kaynaksa 'civarı' (kural 78) ya da 2. kaynak (CNBC/Investing).
- Kart: haber_dosya (Nasdaq 100 + 10Y/2Y vadeli mini grafik, bugün 5 dk). ve TA-FARK tekrarları (O-xxx dersi), skill kopyası ile DEVIR_TAM kural numarası uyumu; Enes'e 3-5 madde.
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

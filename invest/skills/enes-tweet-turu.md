---
name: "enes-tweet-turu"
description: "Enes Uludağ'ın X hesabı için otomatik paylaşım turu, Enes'in istediği tweet veya 13F tweeti hazırlanıp Buffer'dan atılırken kullanılır: kontrol listesi, kaynak, yazım, kart ve kayıt kuralları."
---

# Enes tweet turu

Repo: `/home/claude/kontra-gorsel/invest` (GitHub enesuludg6-debug/kontra-gorsel). Ayrıntı ve geçmiş için başvuru dosyaları: `DEVIR_TAM.md` (tüm kurallar, portföy, adaylar), `DEVIR_OZET.md`, `ORNEKLER.md` (beğenilen tweet kalıpları), `DONGU.md` (her paylaşımın kaydı), `temel_karne.md`. Bu skill ile DEVIR_TAM çelişirse EN YENİ tarihli kural geçerlidir; yeni kural gelince ikisi de güncellenir.

Her zaman Türkçe yaz. Enes'e giden mesajlar da Türkçe.

Hesabın amacı (her şeyin üstünde): en iyi getiriyi yakalamak ya da en bilgili görünmek değil, GÜVEN ve İYİ İÇERİK. Doğru olmayan rakam yerine eksik tweet; yanılınca açıkça söyle ("şunu demiştim, olmadı"); abartı ve heyecan yok. Hedef okur ABD borsasını az bilen biri: kısa, sade, anlaşılır. X hesabı @enes1050392 (Enes Uludağ, EnesInvestUS).

Bilanço önizleme/rakam/analiz ve 13F serisi için `enes-bilanco-13f`, 18:00/23:30 teknik kontrol, portföy notları ve temel karne için `enes-portfoy-analiz` skill'ini de yükle.

## 1. Tur başı kontrol (sırayla)

1. `ReadNotifications` (bildirim varsa), sonra `cd /home/claude/kontra-gorsel/invest && git pull -q`.
2. `DONGU.md` son 40 satırını oku: satır başında tek başına `DURDUR` varsa HİÇBİR ŞEY yapma, yeni tur kurma.
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
- Zamana bağlı menü: sabah notu 09:30-11:00, premarket 16:15-17:15, açılış 17:30-18:30, kapanış 00:05-00:45, hafta içi 22:00 "yarın ne var", Cuma/Cumartesi haftanın karnesi, Pazar/Pazartesi "bu hafta ne var". Makro veri günü: beklenti → sonuç (yorumsuz) → etki (yorumlu).
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

- Arkadaşına anlatır gibi, sade ve doğal cümleler. Terimleri sadeleştir: EPS = hisse başı kâr, guidance = şirketin verdiği tahmin/yönlendirme, capex = yatırım harcaması.
- Şirketi ilk geçtiği yerde ne iş yaptığıyla tanıt. Ticker'lar gerektiğinde $TICKER.
- İlk satır durdurmalı: rakam, tezat ya da net tespit.
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
- Her turda tweetten sonra portföy taraması: `python3 ta2.py DOCN RKLB SITM AXON CBRS VRT AVGO > /tmp/ta.txt` (pipe ile head kullanma, BrokenPipe) + Chrome bağlıysa TradingView okuma; önceki duruma göre değişiklik, ekleme fırsatı, azaltma işareti ya da portföy dışı fırsat varsa Enes'e "ben olsam" notu (dil ve yöntem `enes-portfoy-analiz`). Değişiklik yoksa mesaj zorunlu değil.

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

## 8. Yeni kural gelince

Enes yeni bir kural verirse: `DEVIR_TAM.md`'ye kesin kural olarak (tarih + Enes'in sözü), `DEVIR_OZET.md`'ye bir satır, bölüm 18 kayıt tablosuna satır, `DONGU.md`'ye ENES satırı ekle, push et; bu skill'in güncellenmesini `propose_skills` (improvement) ile öner ve AYNI DEĞİŞİKLİĞİ `invest/skills/<skill>.md` kopyasına da yaz (başka hesaba geçişte kaynak burası).
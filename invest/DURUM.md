# DURUM — tek sayfa güncel durum (kesin kural 18)
Son güncelleme: 19.11.2026 15:48 TSİ (B). Her tur ve görev sonunda güncellenir (en çok 80 satır). Turlar DEVIR_TAM'ı baştan okumaz: skill + bu dosya + DONGU.md son 30 satır. DEVIR_TAM'dan yalnız gereken bölüm grep ile açılır.

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



## !!! Kural 49 (Enes 18.11 22:16: 'bizim yatırımcılık tarzımıza uyan tüm hisseler için bilanço açıklanmadan önce konsensüs beklentilerini tweet at bu şekilde kısaca'): kural 46 alanındaki (yapay zekâ / uzay / Nasdaq teknoloji + portföy, ilgi listesi, büyük takip; WMT 19.11 istisnası dahil) HER bilançodan önce AYRI, KISA bir konsensüs tweeti. Zaman: HAZIRLIK görevi içinde, açıklamadan 30-60 dk önce (önizleme tweeti olsa da ayrıca atılır; 3 saat ticker kuralına takılmaz, Enes'in açık isteği). Kart: kart2.beklenti(ticker, şirket adı, 'Mali YYYY • N. çeyrek', 'GG Ay, açılış öncesi/kapanış sonrası (TSİ ~SS:DD)', [(metrik, konsensüs, alt not)], kaynak, out) — büyük logo + Metrik/Konsensüs tablosu; satırlar gelir + hisse başı kâr (+ şirkete özgü 1-2 KPI ya da şirket rehberi). Metin 2-4 kısa satır, yorumsuz: '$T bu gece/yarın sabah ... bilançosunu açıklıyor. Piyasa beklentisi gelirde X, hisse başı kârda Y.' + varsa şirket rehberi ve opsiyon hareketi tek cümle. Her rakam 2 kaynak. DONGU '- BEKLENTI: T'.

## !!! Kural 48 (Enes 18.11 22:11-22:13: 'hiç son dk haberi atmıyosun hisselerle ilgili' / 'günde en az 30-50 tweet sadece pazar günleri 10 tweet ve son dakika haberi de istiyorum arada sırada'): Pzt-Cmt günde EN AZ 30 EN ÇOK 50 tweet; PAZAR 10 tweet. Her turda İLK İŞ son dakika taraması (WebFetch https://www.newsquawk.com/headlines + WebSearch 'stock news today' / portföy-ilgi listesi isimleri; extended mod), 2 kaynaklı yeni hisse haberi varsa ÖNCE o atılır. Zamanlı görevler arasında boşluk bırakma: turlar 15-25 dk arayla, her turda 1-2 tweet. Kural 42'deki 40 sınırı 50 oldu.

## !!! Kural 43 (Enes 18.11 01:29): İŞ DEFTERİ `python3 invest/isler.py` — zamanlı her iş ve bilanço adımları burada; devirde tek kaynak; iptal yalnız en dar kapsam ve Enes'in aynen sözüyle.

## !!! HESAP DEVRİ TAMAM (18.11 20:31): B aktif; tur_basi.sh B; bütün görevler bu sohbette (session_01EmZ47ompNeGsaQSXfJ8wHS).

## !!! Kural 47 (Enes 18.11 18:07): her tweetten sonra Enes'e ÖĞRETİCİ 'Ne anlama geliyor?': terimler, neden önemli, nasıl okunur, Nasdaq/portföy bağlantısı, izlenecek.

## !!! Kural 46 (Enes 18.11 17:12): KONU FİLTRESİ: yalnız YAPAY ZEKÂ, UZAY, NASDAQ (+ bunları etkileyen makro). Perakende/tüketim/banka/sanayi/ilaç vb. tweet YOK. 13F'te yalnız teknoloji hamleleri; Pabrai, Icahn atlandı. İSTİSNA: WMT 19.11 görevleri kalır (Enes 17:16), analiz/detayda MAKRO bölüm zorunlu (tüketici, enflasyon/tarife, Fed ve Nasdaq'a etkisi).

## BUGÜNLÜK 18.11 (Enes 15:39): Target (TGT) hakkında bugün başka tweet YOK; TGT beklenen ve çağrı iptal. Haklar diğer konulara. Yalnız 18.11 için.

## !!! Kural 11-B (Enes 18.11 14:55): HER tweetten önce `python3 invest/yasak.py` taraması; çıkış 1 = ATMA. 'Benim görüşüm:', 'Not:' ve paragraf başı 'X:' yasak.

## !!! Kural 45 (Enes 18.11 07:40): bilanço sonrası analiz ve hisse analizi yazıları ÇOK DETAYLI ve ÇOK KAYNAKLI: 10-15 paragraf, en az 6 kaynak / 4 tür, 13 maddelik sıra (skill enes-bilanco-13f 'Detaylı analiz yazısı').

## !!! Kural 44 (Enes 18.11 01:51-01:54): YALNIZ 18:00 (temel1800) ve 23:30 (teknik2330) analiz görevleri kaldırıldı, bir daha kurulmaz. Karne, tez kartı, ben olsam ve diğer temel işler AYNEN sürer.

## !!! Kural 42 (Enes 18.11 01:13; 01:18: 18-21 sınırı da kaldırıldı): tweet penceresi 11:00-02:00; Pzt-Cmt günde EN AZ 30 EN ÇOK 40 tweet; Pazar üst sınır (Enes rakam verene kadar 40), alt yok; tweet aralığı SERBEST (sabit aralık yok, Enes 01:15); 10:30 görevi 11:00'e kaydı; 09:05 vadeli tweeti yok.

## !!! Kural 41 (Enes 18.11 00:57; 01:05 netleştirme: detaylar BEKLEMEDEN, gece dahil, belge çıkar çıkmaz; görüşme tweetleri gece bilançosunda aynı sabah): her bilançodan sonra 2-7 AYRI detay tweeti (belgeden: taahhütler, serbest nakit, müşteri kırılımı, koşullu anlaşmalar, marj köprüsü, stok/alacak, KPI...), kendi kartımız + yorum; 'Detay: <T>' görevi; DONGU '- DETAY: <T> <konu>'.

## !!! Kural 40 (Enes 18.11 00:31): bilanço görüşmesi (kazanç çağrısı) önemli yerleri AYRI AYRI tweet; açılış öncesi bilançoda aynı gün, kapanış sonrasında ertesi gün; transkript + haber, 2 kaynak; 'Çağrı: <T>' görevi; DONGU '- CAGRI: <T> <konu>'.

## !!! Kural 39 (Enes 17.11 23:47): her bilançodan önce opsiyon beklenen hareketi en az bir tweette (önizleme/günün başlıkları/bağlam); DONGU '- OPSIYON: <T>'; tur_basi 'EKSİK OPSİYON' uyarır; ertesi gün kıyas görevi hazırlıkta kurulur.

## !!! Kural 38 (Enes 17.11 22:30): Enes teknik analizini atar → Claude yalnız sade, mecazsız tweet taslağı yazar ve Enes'e yollar; kendi analizini eklemez, PAYLAŞMAZ.

## !!! Kural 37 (Enes 17.11 22:17): TEKNİK ANALİZ YOK. 18:00/23:30 teknik zincirleri kapalı; yerine her işlem günü 18:00 TEMEL ANALİZ (temel1800). Key levels 10:30 = seviyesiz 'günün başlıkları'. Turlarda ta2 yerine portföy haber taraması.

## Kural 36 (21:46-22:00): tur 20-40 dk ama tweet günde en çok 15 + 18-21 en çok 2 (`kontrol tweet_gunluk`); bugünlük blok yalnız kendi tarihinde; skill-kopya çelişkisinde kopya; yayın 60 dk içindeyse ağır görev yayından 15 dk önce biter; Pazar sistem denetimi.

## Kural 34-35 (21:43): karneye 9 ek (trend, revizyon, kazanç kalitesi, artımlı marj, KPI ivmesi, stres, değerleme bandı, tepki geçmişi, tez kartı); 18:00/23:30'da her hisse için tek satır KARAR = temel sınıf (karneden okunur) + teknik durum A-E tablosu. Portföy karne eksikleri önce: RKLB SITM AXON CBRS VRT.

## Kural 33 (21:37): teknik analizde ayrıca `ta_ek.py` (MTF hizalama, göreli güç, hacim teyidi, sıkışma, pivot, uyumsuzluk, mum, boşluk, kanal/üçgen ipucu, AVWAP, ölçümlü hedef, risk/ödül, piyasa rejimi) + seviye_takip.csv.

## Kural 32 (21:13-21:30): haftada 2-3 uzun görüş yazısı (UZUN-GORUS, periyot uzun_gorus); 21-24 ya da 12-15 diliminde. 10 çerçeveli havuzdan (sablonlar.md 20, A-J) son 3'te olmayan seçilir; başlık, uzunluk, açılış ve kapanış her seferinde değişir.
- Uzun yazı: `periyot.py etiket kontrol cerceve <X> 0 3` + `etiket kontrol uzun_ticker <T> 30`; yazınca `etiket yap cerceve X`, `etiket yap uzun_ticker T`, `yap uzun_gorus`.

## Kural 31 (21:01-21:03): gerekli olduğunda çizim mutlaka (her grafikte zorla değil) (kanal/üçgen/takoz/yatay bant + kademe ışınları/kutular, gerekirse Fibonacci); caption ve taslakta formasyon sade dille.

## Kural 30 (20:19): teknik analiz tweet taslağı ve notlarında deyim/mecaz yok, sade ve ölçülebilir dil.

## Kural 28 (tasarruf, kurallar aynen): tur başı `bash tur_basi.sh A2`, kart `bash yayinla_gorsel.sh g/x.jpg`, kayıt `CS=<oturum> python3 kayit.py ...` (skills/enes-tweet-turu.md 15).

## Kural 25 (Enes 17.11 16:51): her haber/veri tweeti = haber + YORUM (ne demek, büyük resim, Fed ne düşünür, piyasaya/hisselere etkisi, net düşüncemiz). Şablon 7 güncellendi.

## Kural 26-27 (17.11 17:18)
- 26: tweet atınca performans_veri.csv'ye satır; dersler yalnız ders_analiz.py ile (protokol DERSLER.md başı); tur başında invest/DERSLER.md 'AKTİF DERSLER' okunur ve uygulanır (günde 12-15 tweet, 18-21 en çok 2, görüşlü analiz 12-15 / 21-24, 13F en çok 2). Sabah 09:00 gözlem ekler, Pazar 21:30 dersleri günceller.
- 27: teknik analizde TradingView ekran görüntüsünü CLAUDE alır (Chrome zoom save_to_disk → SendUserFile), sıra: görüntü → taslak + ben olsam. Chrome yoksa talimat satırı.

## Periyot defteri (kural 24)
- Karışım önerisi 3 haftada bir (Pazar 21:30 raporu `periyot.py kontrol karisim_onerisi` UYGUN ise üretir, sonra `yap`). #1 17.11'de verildi (performans.md), Enes ONAYLADI (17.11 17:18) → DERSLER.md AKTİF DERSLER.
- Haftalık/aylık/N günlük ya da adet sınırlı HER iş: önce `python3 periyot.py durum` / `kontrol <anahtar>`, yapınca `python3 periyot.py yap <anahtar> "<not>"` + push. Sözlük cümlesi: `python3 periyot.py sozluk "<Veri>"`. Hafızadan tahmin yok.

## Hesap
- AKTIF: B (invest/AKTIF_HESAP.md; 18.11 20:26 hesap devri). Görev mesajları HESAP=B ile başlar. Oturum: session_01EmZ47ompNeGsaQSXfJ8wHS. Chrome B hesabında bağlı değil.
- Chrome: 17.11 15:31 bagli (TradingView ve bulten sayfalari icin). Oturum: session_01JKiyuk5Mhinmn4mL9usBPz (zincir + tek seferlik yayınlar). Sabit görevler bulut (persist_session false).

## Portföy ve listeler
- Portföy: DOCN RKLB SITM AXON CBRS VRT AVGO. NBIS YOK.
- Kartlı adaylar: TSM (/50 39), ECL (36). Karne: temel_karne.md.
- İlgi listesi (kural 22r): ON AAOI HOOD TEM CRDO PLTR ISRG ASTS MU | yeni, karnesi bekleniyor (günde 1-2, 30/50 altı çıkar): ANET ALAB MRVL COHR LITE ETN GEV CRWD NET DDOG APP RBRK PL LUNR | çıkarılanlar: -
- Büyük takip: NVDA AMD TSM MSFT GOOGL AMZN META ORCL CRWV SNOW.
- Kural 23: tutmayan tahmin tweette anılmaz, yalnız doğru çıkanlar. Yanlış rakamda kural 21 düzeltme.

## Aday rotasyonu (teknik analizlerde her gün farklı 3-4 aday): `periyot.py etiket kontrol aday <T> 5`, kullanınca `etiket yap aday <T>`
- 17.11: TSM (39/50), DDOG (karne yok), ANET (karne yok; ekran görüntüsü alındı, mesaj 23:30'a) — tekrar etme: 18-20.11.
- TradingView düzeni şu an DMI + Aroon ile kayıtlı: sonraki teknik çalışmada rotasyona devam et, sonunda Supertrend + SMC geri koy.

## Son teknik seviyeler (17.11 18:25 TradingView + ta2 tam)
NDX 26.990 (4s ST AL) / 26.600 kritik | DOCN k1 72-74 k2 69-70 tez hf<69,8 | RKLB k1 55-57 k2 50-52 tez G<43,9 | SITM k1 395-405 k2 345-365 tez G<335 | AXON k1 291-298 k2 255-270 tez hf<255 | CBRS k1 96-99 k2 88-91 tez G<77,8 | VRT k1 178-183 k2 169-174 tez hf<150 | AVGO k1 323-330 k2 300-311 tez G<289,8 | TSM k1 351-360 | ECL 294-301

## Kart
- Son 3 düzen: spotlight (WMT detay: düzeltilm), zaman (WMT detay: üyelik +%), uclu (PANW ön piyasa +%9; ). k). ceyrek o). ceyrek onizl). Electron +). ceyrek). ceyrek). ceyrek analiz). ceyrek rakam).). ceyrek anali). ceyrek tam f). ceyrek). LOGO_BUYUT 1.8, küçültme YOK; bento ve skor kare logoyu taşımıyor → bilanço rakamı uclu.

## 13F serisi (Q3 2026)
Atılanlar: Berkshire, Ackman, Druckenmiller, Tepper, Soros, Third Point/Loeb. Atıldı: Greenlight, Coatue (18.11 11:17), Tiger Global (18.11 12:07), Baupost (18.11 13:57), Himalaya (18.11 16:58). Atıldı: Lone Pine (18.11 20:51). Viking 19.11 14:30 zamanlandı, Bridgewater 19.11 13:01 atıldı. Sıradaki: teknoloji hamleli yeni fon (Point72, ARK, Baillie Gifford) (yalnız teknoloji hamleleri); Pabrai, Icahn atlandı. Bitince Enes'e özet. Burry yok (SEC kaydı silindi).

## Bugün / yarın (takvim.md ayrıntılı)
- 17.11: HD yayın 13:58, DIS yayın 14:38, vadeli ~15:00-15:25, perakende satış hazırlık 15:40 yayın 16:28, teknik 18:00, teknik 23:30, NVDA hazırlık 23:25 yayın 00:18 (+15 dk analiz; 12:22 önizleme tahminleriyle kıyas: gelir 111-113, DC 103-105, GM %74,2-74,5, HBK 2,53-2,58; Q4 rehber 122-126, marj ~%72).
- 18.11: TGT, FOMC notları, PANW, P (bitti). 19.11: WMT (15:00), INTU (00:00 TSİ 20.11, 7 görev kuruldu).
- Cumartesi 21.11 11:00 haftalık özet (kural 19). Pazar 22.11 20:00 takvim + "gelecek hafta" tweeti (kural 20), 21:30 performans raporu.

## Son 10 tweet (17.11)
09:06 vadeli | 09:38 13F Berkshire | 10:13 13F Ackman | 10:48 13F Druckenmiller | 11:13 13F Tepper | 11:41 13F Soros | 12:14 düşüş analizi (Enes) | 12:22 NVDA önizleme (Enes) | 12:48 13F Loeb | 13:16 key levels + başlıklar | 14:07 HD bilanço rakamı | 14:25 HD analiz | 14:44 DIS bilanço rakamı | 15:01 DIS analiz | 15:21 vadeli | 14:16 NVDA ihracat komitesi (Enes)
Ticker 3 saat: DIS 15:01; HD 14:25; NVDA 14:16 (Enes); META/NVDA/MSFT/GOOGL 12:48; NVDA 12:22.

## Sabit görevler A2 (18.11 01:24 sohbet devri, session_01JKiyukU5wB8Xm26NDD6m99)
sabah trig_01Y2HE9jpJ1HxtCgDLPw9wsY | keylevels trig_01MtFa8vPDj98fPsEHEFkXQ7 | radar trig_011hBn9NzYUqsLA9H3sxjTaU | haftalikozet trig_01WdCCVcVUdUH4PTvapMAiUk | sektor trig_01CLY9FkshP5VsSR7HfGTd7r | ilgisira trig_01HmdehZpTUqTMS7ib2xQmJW | analist trig_01ToiAEZR2azSBwmNTB2aRim | sezon trig_01AsGEUyWLG78gu9jczvP2DG | takvim trig_01GSk4e6zDur9Qe5KPWtDiyF | performans trig_01VuGwf6NEdZjnviXGhyqou3 | ayinozeti trig_012hEULzCuEmJGki2qJDVPZj | 13f trig_018WMPgmsvBXmwsrWRTSFFqc
Tek seferlik A2: tur 01:29 trig_01Qbj8KoEDhmYphZpPAMEmei | tur 11:15 trig_01B1n1AKy7aRNppmDzU9K7cz | Beklenen hareket NVDA 17:45 trig_01R5Jz9iMFsJ7oio6nsdfeNp | Çağrı TGT 19:20 trig_013ixAYQMgEVvehVA1xg7xqb
Eski sohbet (A) görevleri 01:22'de eski sohbette devre dışı bırakıldı; kilit AKTIF: A2 (tur_basi tam eşleşme).
## (A, eski) Sabit görevler (kural 29: BU SOHBETTE send_later zinciri; `python3 sonraki.py hepsi`)
17.11 18:12 kuruldu: sabah trig_012ce3N7txgyPgMe7NExSdXk | keylevels trig_015KcRGTBLUf5FgoyTgM4aPx | radar trig_01JPKB6q6hoSbr7aUvc1tZdT | teknik1800 trig_01YGd9XSQVBPaEvPzUxn58KR | teknik2330 trig_01FrJLYoFpaVNWBML1X51T6Q (bugün 23:30) | haftalikozet trig_01N9oJUV6yDkcy1dHi2UedGi | sektor trig_01H9bcdWG66a46bi8y9XRWGr | ilgisira trig_01VUaoQm8x7ekUc2N4ihwqeF | analist trig_01YPoX9xAnKJ2GkrM1KCvFFj | sezon trig_016jw1UgF9rXmU77P7S3AuBB | takvim trig_01NgZxB2262tvbJv5eirvc9L | performans trig_01TtCSqsEgbDoVwJtAdzyanC | ayinozeti trig_017GsHAih4s9BHpfQCssPh5S | 13f trig_019tLt3qvMWqMLPcNqTQ3kj8. (Her çalışmada yeni ID; güncel liste list_triggers.)
ESKİ bulut cron (kapalı): aşağıdakiler; 18:00 ve 23:30 bulut cron da 20:19'da kapatıldı. 23:42 TV teyidi kapatıldı (23:30 zinciri ekran görüntülü).
## (eski) Sabit görevler (kimlikler)
Kural 22 (17.11 14:40): radar hf 14:20 trig_016SbofaS65yjLJA3vxEJFJn | sektör Cmt 13:25 trig_01UJ5gbaa8MpWRkeNfCZfdcb | ilgi sıralama Cmt 16:25 trig_01R8djvwKF63qvV4cwdsivEK | sezon karnesi Pz 14:25 trig_01DgnmwSnDP8dT1HdLPGKch3 | analist hedef / değerleme Pz 12:25 trig_01LGJqeSfkqAMg3YAbsecQvA | ayın özeti + mevsimsellik trig_01X3YVaH2z1Yv7RyptTiUKok | haftalık özet trig_01LRGPzzrcF327Pqe67n55Qa | performans Pz 21:30 trig_017HiX433Vy7u15V1a6wfbec | sabah 09:00 trig_01C56vPfmWMnsPMFTV6wU6CM
18:00 trig_01LCT69YkpVZvjjW6ueTGftC | 23:30 trig_01Me3Zwdnufk6rkLKNmZ2YF5 | key levels 10:30 trig_01BGRz55RsS87Nko3XpCmXRE | takvim Pazar 20:00 trig_01XKuwGwLJwQbLzfPfbdjAX8 | performans Pazar 21:30 trig_017HiX433Vy7u15V1a6wfbec | sabah 09:00 trig_01C56vPfmWMnsPMFTV6wU6CM | 13F Şub/Ağu/Kas trig_01X4fnNMsC1i6wo8kXaMLqmf | 13F May trig_014UMzEahLeqQdKb27x5skDU | haftalık özet Cmt 11:00 trig_01LRGPzzrcF327Pqe67n55Qa | ayın özeti (ayın 1-7'si 10:55, ilk işlem günü kontrolü) trig_01X3YVaH2z1Yv7RyptTiUKok | Pazar 20:00 görevine 'gelecek hafta' tweeti + DONGU arşivi eklendi.

## Zincir
- Otomatik tur zinciri: sıradaki trig_013emWjdzCRS8wjiYjy7yuNJ 19.11 15:47 (B); 13F: Viking 14:30, Bridgewater 13:01, Baillie Gifford 14:38 atıldı; sıradaki Point72/ARK
- Bu oturumdaki tek seferlikler (HESAP=A): HD yayın 13:58, DIS yayın 14:38, perakende 15:40/16:28, NVDA 23:25/00:18.

## Bekleyen kararlar
- Yok (kaynak istisnası 12:58'de onaylandı).

## Radar (içeriden alım / geri alım, son 5)
- 19.11 14:20: kayda değer yok (TSM yönetim kurulu üyesi Burns 500 bin $ alım, eşik altı)
- 18.11 14:20: kayda değer yok (süre dışı izlenenler: ROK CEO 1,55 Mn$ 09.11; CVS Shah 2 Mn$ 06.11)

## İçerik karışımı (Enes onaylı, kural 22a)
- Henüz yok (3 haftalık veri bekleniyor).

## NVDA hazır (17.11 23:27): /tmp/hazir_NVDA.py (uclu; JSON: gelir, gelir_b, hbk, hbk_b, q4, q4_b, kaynak, out, baslik). Beklenti tweet: gelir 109,3 Mr $, HBK 2,47 $, veri merkezi 101-102 Mr $, brüt marj %74,0 (şirket rehberi). Q4 rehber konsensüsü bulunamadı → tweette Q4 satırı 'Beklenti' yazmadan ya da yayın anında 2 kaynakla. NOT: Q1 FY27'den beri düzeltilmiş rakamlar hisse bazlı ödemeyi DÜŞMÜYOR (FourWeekMBA) → 'düzeltilmiş' etiketi bültenden. Opsiyon beklenen hareket: ±%8,5 (Analytics Insight + Reuters, 17.11), Saxo 11.11 kapanışta ±%7,8.

## BEKLEYEN DÜZELTME (kural 21)
- Yok (TGT 160,32 -> 159,53 düzeltmesi 18.11 14:47 analiz tweetinde yapıldı).

## Bekleyen tek seferlik görevler → ARTIK `python3 invest/isler.py liste` (kural 43; is_defteri.json tek kaynak)

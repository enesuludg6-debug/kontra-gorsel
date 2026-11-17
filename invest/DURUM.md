# DURUM — tek sayfa güncel durum (kesin kural 18)
Son güncelleme: 18.11.2026 01:08 TSİ. Her tur ve görev sonunda güncellenir (en çok 80 satır). Turlar DEVIR_TAM'ı baştan okumaz: skill + bu dosya + DONGU.md son 30 satır. DEVIR_TAM'dan yalnız gereken bölüm grep ile açılır.

## !!! BUGÜNLÜK KURAL (Enes 17.11 15:23; YALNIZ 17.11 için, 18.11 sabah kontrolü siler): KALAN TWEET HAKKI = 0 (paylaşım günü sonu 01:00 TSİ'ye kadar) — ENES 21:53: 21:53-01:00 arası EN AZ 7 tweet (alt sınır; 3'ü kapanış + NVDA rakam + NVDA analiz, 4'ü serbest: 22:15, 22:40, 23:05, 23:18 turları MUTLAKA atar) !!!
- Her tweet atan tur/görev ÖNCE bu sayıya bakar; 0 ise ATMAZ. Atınca sayıyı 1 düşürür, DONGU satırına "hak: kalan N" yazar, push.
- Ayrılan: perakende satış 16:30 (1), NVDA rakam 00:20 (1), NVDA analiz (1), kapanış 00:05 (1; "Kapanış tweeti" görevi kuruldu). Serbest: 6 → 13F (en çok 2), büyük son dakika, Enes isteği. Vadeli, FED-TAHVIL, analist notu, ikinci bilanço analizi gibi ikincil tweetler bugün YOK. Otomatik tur paylaşım için en az 60 dk arayla; değerli konu yoksa paylaşmadan geçer.
- KULLANILAN (15:23'ten sonra): 16:31 perakende, 17:36 perakende yorum (serbest), 19:32 13F Greenlight Einhorn (serbest), 21:07 NVDA bilanco oncesi satis (serbest), 22:16 TGT, FOMC tutanaklari, PANW (serbest), 22:41 Ileri F/K nasil okunur (serbest), 23:06 TSM iki gunde yuzde 10 (serbest), 23:19 VIX nasil okunur (serbest), 00:06 17.11 kapanis (ayrilan), 00:23 NVDA 3. ceyrek (ayrilan), 00:41 NVDA 3. ceyrek analiz (ayrilan)

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

## Kural 28 (tasarruf, kurallar aynen): tur başı `bash tur_basi.sh A`, kart `bash yayinla_gorsel.sh g/x.jpg`, kayıt `CS=<oturum> python3 kayit.py ...` (skills/enes-tweet-turu.md 15).

## Kural 25 (Enes 17.11 16:51): her haber/veri tweeti = haber + YORUM (ne demek, büyük resim, Fed ne düşünür, piyasaya/hisselere etkisi, net düşüncemiz). Şablon 7 güncellendi.

## Kural 26-27 (17.11 17:18)
- 26: tweet atınca performans_veri.csv'ye satır; dersler yalnız ders_analiz.py ile (protokol DERSLER.md başı); tur başında invest/DERSLER.md 'AKTİF DERSLER' okunur ve uygulanır (günde 12-15 tweet, 18-21 en çok 2, görüşlü analiz 12-15 / 21-24, 13F en çok 2). Sabah 09:00 gözlem ekler, Pazar 21:30 dersleri günceller.
- 27: teknik analizde TradingView ekran görüntüsünü CLAUDE alır (Chrome zoom save_to_disk → SendUserFile), sıra: görüntü → taslak + ben olsam. Chrome yoksa talimat satırı.

## Periyot defteri (kural 24)
- Karışım önerisi 3 haftada bir (Pazar 21:30 raporu `periyot.py kontrol karisim_onerisi` UYGUN ise üretir, sonra `yap`). #1 17.11'de verildi (performans.md), Enes ONAYLADI (17.11 17:18) → DERSLER.md AKTİF DERSLER.
- Haftalık/aylık/N günlük ya da adet sınırlı HER iş: önce `python3 periyot.py durum` / `kontrol <anahtar>`, yapınca `python3 periyot.py yap <anahtar> "<not>"` + push. Sözlük cümlesi: `python3 periyot.py sozluk "<Veri>"`. Hafızadan tahmin yok.

## Hesap
- AKTIF: A (invest/AKTIF_HESAP.md). Görev mesajları HESAP=A ile başlar.
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
- Son 3 düzen: uclu (NVDA 3, ilerleme (NVDA 3, grafik2 (NVDA taahhutler). ceyrek anali). ceyrek tam f). ceyrek). LOGO_BUYUT 1.8, küçültme YOK; bento ve skor kare logoyu taşımıyor → bilanço rakamı uclu.

## 13F serisi (Q3 2026)
Atılanlar: Berkshire, Ackman, Druckenmiller, Tepper, Soros, Third Point/Loeb. Atıldı: Greenlight. Sıradaki: Coatue → Tiger Global → Baupost → Himalaya → Pabrai → Icahn → Bridgewater → Lone Pine/Viking. Bitince Enes'e özet. Burry yok (SEC kaydı silindi).

## Bugün / yarın (takvim.md ayrıntılı)
- 17.11: HD yayın 13:58, DIS yayın 14:38, vadeli ~15:00-15:25, perakende satış hazırlık 15:40 yayın 16:28, teknik 18:00, teknik 23:30, NVDA hazırlık 23:25 yayın 00:18 (+15 dk analiz; 12:22 önizleme tahminleriyle kıyas: gelir 111-113, DC 103-105, GM %74,2-74,5, HBK 2,53-2,58; Q4 rehber 122-126, marj ~%72).
- 18.11: TGT (açılış öncesi), FOMC notları 22:00, PANW. 19.11: WMT.
- Cumartesi 21.11 11:00 haftalık özet (kural 19). Pazar 22.11 20:00 takvim + "gelecek hafta" tweeti (kural 20), 21:30 performans raporu.

## Son 10 tweet (17.11)
09:06 vadeli | 09:38 13F Berkshire | 10:13 13F Ackman | 10:48 13F Druckenmiller | 11:13 13F Tepper | 11:41 13F Soros | 12:14 düşüş analizi (Enes) | 12:22 NVDA önizleme (Enes) | 12:48 13F Loeb | 13:16 key levels + başlıklar | 14:07 HD bilanço rakamı | 14:25 HD analiz | 14:44 DIS bilanço rakamı | 15:01 DIS analiz | 15:21 vadeli | 14:16 NVDA ihracat komitesi (Enes)
Ticker 3 saat: DIS 15:01; HD 14:25; NVDA 14:16 (Enes); META/NVDA/MSFT/GOOGL 12:48; NVDA 12:22.

## Sabit görevler (kural 29: BU SOHBETTE send_later zinciri; `python3 sonraki.py hepsi`)
17.11 18:12 kuruldu: sabah trig_012ce3N7txgyPgMe7NExSdXk | keylevels trig_015KcRGTBLUf5FgoyTgM4aPx | radar trig_01JPKB6q6hoSbr7aUvc1tZdT | teknik1800 trig_01YGd9XSQVBPaEvPzUxn58KR | teknik2330 trig_01FrJLYoFpaVNWBML1X51T6Q (bugün 23:30) | haftalikozet trig_01N9oJUV6yDkcy1dHi2UedGi | sektor trig_01H9bcdWG66a46bi8y9XRWGr | ilgisira trig_01VUaoQm8x7ekUc2N4ihwqeF | analist trig_01YPoX9xAnKJ2GkrM1KCvFFj | sezon trig_016jw1UgF9rXmU77P7S3AuBB | takvim trig_01NgZxB2262tvbJv5eirvc9L | performans trig_01TtCSqsEgbDoVwJtAdzyanC | ayinozeti trig_017GsHAih4s9BHpfQCssPh5S | 13f trig_019tLt3qvMWqMLPcNqTQ3kj8. (Her çalışmada yeni ID; güncel liste list_triggers.)
ESKİ bulut cron (kapalı): aşağıdakiler; 18:00 ve 23:30 bulut cron da 20:19'da kapatıldı. 23:42 TV teyidi kapatıldı (23:30 zinciri ekran görüntülü).
## (eski) Sabit görevler (kimlikler)
Kural 22 (17.11 14:40): radar hf 14:20 trig_016SbofaS65yjLJA3vxEJFJn | sektör Cmt 13:25 trig_01UJ5gbaa8MpWRkeNfCZfdcb | ilgi sıralama Cmt 16:25 trig_01R8djvwKF63qvV4cwdsivEK | sezon karnesi Pz 14:25 trig_01DgnmwSnDP8dT1HdLPGKch3 | analist hedef / değerleme Pz 12:25 trig_01LGJqeSfkqAMg3YAbsecQvA | ayın özeti + mevsimsellik trig_01X3YVaH2z1Yv7RyptTiUKok | haftalık özet trig_01LRGPzzrcF327Pqe67n55Qa | performans Pz 21:30 trig_017HiX433Vy7u15V1a6wfbec | sabah 09:00 trig_01C56vPfmWMnsPMFTV6wU6CM
18:00 trig_01LCT69YkpVZvjjW6ueTGftC | 23:30 trig_01Me3Zwdnufk6rkLKNmZ2YF5 | key levels 10:30 trig_01BGRz55RsS87Nko3XpCmXRE | takvim Pazar 20:00 trig_01XKuwGwLJwQbLzfPfbdjAX8 | performans Pazar 21:30 trig_017HiX433Vy7u15V1a6wfbec | sabah 09:00 trig_01C56vPfmWMnsPMFTV6wU6CM | 13F Şub/Ağu/Kas trig_01X4fnNMsC1i6wo8kXaMLqmf | 13F May trig_014UMzEahLeqQdKb27x5skDU | haftalık özet Cmt 11:00 trig_01LRGPzzrcF327Pqe67n55Qa | ayın özeti (ayın 1-7'si 10:55, ilk işlem günü kontrolü) trig_01X3YVaH2z1Yv7RyptTiUKok | Pazar 20:00 görevine 'gelecek hafta' tweeti + DONGU arşivi eklendi.

## Zincir
- Otomatik tur zinciri: sıradaki trig_01UGcYwU5DDm3PHkXyZBLBiN 22:15 (son tur; 21:07 NVDA öncesi bağlam atıldı)
- Bu oturumdaki tek seferlikler (HESAP=A): HD yayın 13:58, DIS yayın 14:38, perakende 15:40/16:28, NVDA 23:25/00:18.

## Bekleyen kararlar
- Yok (kaynak istisnası 12:58'de onaylandı).

## Radar (içeriden alım / geri alım, son 5)
- (henüz yok; ilk tarama 18.11 14:20)

## İçerik karışımı (Enes onaylı, kural 22a)
- Henüz yok (3 haftalık veri bekleniyor).

## NVDA hazır (17.11 23:27): /tmp/hazir_NVDA.py (uclu; JSON: gelir, gelir_b, hbk, hbk_b, q4, q4_b, kaynak, out, baslik). Beklenti tweet: gelir 109,3 Mr $, HBK 2,47 $, veri merkezi 101-102 Mr $, brüt marj %74,0 (şirket rehberi). Q4 rehber konsensüsü bulunamadı → tweette Q4 satırı 'Beklenti' yazmadan ya da yayın anında 2 kaynakla. NOT: Q1 FY27'den beri düzeltilmiş rakamlar hisse bazlı ödemeyi DÜŞMÜYOR (FourWeekMBA) → 'düzeltilmiş' etiketi bültenden. Opsiyon beklenen hareket: ±%8,5 (Analytics Insight + Reuters, 17.11), Saxo 11.11 kapanışta ±%7,8.

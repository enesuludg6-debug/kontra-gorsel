---
name: enes-teknik-smc
description: Enes bir endeks ya da hisse için SMC/ICT veya teknik analiz istediğinde (grafik ekran görüntüsü, seviye, "trade et", 1G/4S) Yahoo verisi + smartmoneyconcepts + pandas_ta ile analiz yaparken kullanılır.
---
# SMC / ICT teknik analiz (Enes 25.11.2026 22:11 onayı)

## Onay (her hesapta, her sohbette geçerli)
Enes 25.11.2026 22:11: "kurulumu onaylıyorum ayrıca yeteneklere ekle başka hesapta da onayladığımı bilsin".
- `pip install --break-system-packages -q smartmoneyconcepts pandas_ta` kurulumu ÖNCEDEN ONAYLIDIR; kurulu değilse sormadan kur.
- TEXT TO QUANT bağlayıcısı bağlı ama plan yalnız kripto (Binance spot); hisse/endeks için kullanma (Power planı gerekir). Financial Datasets bağlanırsa Yahoo'ya yedek fiyat kaynağı.

## Akış
1. `python3 invest/smc_analiz.py <TICKER> <1d|4h|1h|1wk> [--png g/<ad>.png]` (repo `kontra-gorsel`). Endeks: ^NDX, ^GSPC; vadeli: NQ=F, ES=F.
   - Çıktı: EMA20/50/200, RSI14, ATR14, Supertrend, MACD histogram, Bollinger; son swingler; BOS/CHoCH; açık (doldurulmamış) FVG'ler; açık emir blokları; alınmamış likidite (BSL/SSL); 4h/1h'de önceki gün tepe/dip; dealing range ve premium/discount.
   - 4h Yahoo'da yok: 60m'den üretilir (ABD seansı 16:30 TSİ hizalı); IG/TradingView ile birkaç puan fark olabilir — bunu söyle.
1-B. TEKNİK PRO (Enes 25.11 22:14 "daha da geliştir"): `python3 invest/teknik_pro.py <TICKER> [--seviyeler a,b,c] [--png g/<ad>.png]`
   - Çoklu zaman dilimi yön tablosu (1wk/1d/4h/1h; yapı + EMA20 + Supertrend + RSI, toplam puan −20..+20 -> GÜÇLÜ AŞAĞI … GÜÇLÜ YUKARI). Analize HER ZAMAN bu tabloyla başla (top-down).
   - ICT: dealing range + premium/discount, OTE (Fibonacci 0,62/0,705/0,79) hem günlük büyük dalga hem 4h son dalga, NWOG/NDOG açılış boşlukları, killzone saatleri (TSİ).
   - Hacim profili (POC, değer alanı VAL–VAH, 1h ~20 seans) ve anchored VWAP (son büyük tepe ve dipten).
   - ATR tabanlı otomatik senaryo (giriş/stop/3 hedef/R:R) — başlangıç noktasıdır, Enes'in seviyeleri ve FVG/OB ile düzelt.
   - --seviyeler ile Enes'in ekran görüntüsündeki çizgileri ver: fiyata yüzde uzaklıklarıyla listelenir ve grafikte çizilir.
   - Çakışma (confluence) kuralı: bir seviye ancak en az 2 araçla örtüşüyorsa "güçlü" denir (ör. Enes seviyesi + açık FVG + AVWAP); tek araçlı seviye "zayıf".
2. Enes ekran görüntüsü yolladıysa: onun çizgilerini (yatay seviyeler, trend çizgisi) okuyup yazılım çıktısıyla birleştir; hangi grafik hangi zaman dilimi, başlıktan oku (1G = günlük, 4s/4Sa = 4 saat). Zaman dilimlerini AYRI başlıklarla ver.
3. "Çıplak göz" bölümü: mum yapısı (fitil, gövde, kapanış yeri), ikili dip/tepe, sıkışma, hacim.
4. Plan: en az 2 senaryo (trend yönünde + karşı trend), her birinde giriş bölgesi, tetik (alt zaman diliminde CHoCH/MSS), stop, 2-3 hedef, kabaca R:R; geçersizlik seviyeleri (günlük kapanış bazında). "Tavsiye değil, senaryo" notu tek satır; pozisyon küçüklüğü/ince piyasa uyarısı gerekiyorsa.
5. Mobil: 2 ekranı geçme; başlıklar + kısa maddeler.

## DİP / TEPE / TREND DEĞİŞİMİ RADARI (Enes 25.11 22:22: "dip tahmini, trend değişimi, tepeye yakınken çok iyi analiz et, bana çok basit anlat")
- Enes "dip mi?", "tepe mi?", "dönüyor mu?", "trend değişti mi?" derse ya da herhangi bir teknik analizde İLK `python3 invest/dip_tepe.py <T>` çalıştır.
- Ne ölçer: 10 dip işareti (RSI ≤32, 200 günlükten 4 ATR uzak, zirveden −%15, Bollinger altı, VIX/VXN ≥30, teslimiyet mumu, 5+ gün düşüş, RSI boğa uyumsuzluğu, gün içi güçlü dönüş, önceki gün tepesi üstü kapanış) ve 10 tepe işareti (aynalanmış); son 5 günde yanan işaret sayılır. Trend değişimi 4 şartla: 20 günlük üstü kapanış, yükselen dip, son tepenin kırılması, 20/50 kesişimi -> YOK / ERKEN / GELİŞİYOR / GÜÇLÜ / ONAYLI.
- Kalibrasyon: aynı skorun 20 yılda 10/20/60 gün sonraki sonucu + ONAYLI GİRİŞ TESTİ (skor sonrası ilk 20 günlük ortalama üstü kapanışta giriş). NDX 25.11: dip skoru 7/10 tek başına 20 günde %46 yukarı; onaylı girişte %82 (11 olay). Ana ders: DİP SKORU "nerede bakmalı"yı, TREND ONAYI "ne zaman girmeli"yi söyler.
- ANLATIM (Enes'e, çok basit, 5-6 satır, jargon yok ya da parantezde): 1) Dip mi tepe mi: skor + tek cümle. 2) Trend: hangi aşamada + onay için sıradaki şart ve seviyesi. 3) Geçmiş ne diyor: tek cümle, olay sayısıyla. 4) Ne yapmalı (senaryo, tavsiye değil): "beklenecek seviye", "geçersiz olduğu seviye". 5) Bir benzetme serbest (ör. "satıcılar yoruldu ama alıcılar daha kapıyı açmadı").

## ÇİZİMLİ ANALİZ — VARSAYILAN (Enes 25.11 23:01: "artık gerektiğinde analizleri çizimle beraber yap")
- Her teknik analizde (teknik X, dip/tepe, seviye, trade planı, ekran görüntüsü) metinle birlikte ÇİZİMLİ GRAFİK gönder: `python3 invest/cizim.py <T> [--tf 4h|1d] [--seviyeler a,b] [--fib] [--onay X] [--bozulma Y] --out /tmp/cizim_<T>.png` -> SendUserFile.
- Otomatik çizilenler: mumlar, düşen/yükselen trend çizgisi, en güçlü direnç/destek kutuları (çakışma puanı ≥3, hangi araçlardan geldiği yazılı), Enes seviyeleri (mavi), belirgin dip/tepe okları, istenirse Fibonacci, A (onay) ve B (bozulma) senaryo okları; etiketler üst üste binmez.
- Planın onay/bozulma seviyelerini --onay/--bozulma ile metindekiyle AYNI ver; metin ile çizim çelişmez.
- Enes kendi ekran görüntüsüne çizim isterse: sağdaki fiyat etiketlerinden ölçeği çıkar (iki etiketin piksel y'si ile fiyat arasında doğrusal eşleme), PIL ile aynı öğeleri görüntünün üstüne çiz; ölçek belirsizse Yahoo verisiyle cizim.py kullan ve bunu söyle.
- Tweet için de bu çizim kullanılabilir (Enes atacaksa); yazılar Türkçe, kart3 renkleri.
- GÖRSEL İMZA KURALI (Enes 25.11 23:04): grafik/kart İÇİNDE hiçbir yerde "Enes" yazmaz (seviye etiketi "Seviye 26.980", çakışma kaynağı "yatay seviye"); isim yalnız sağ altta "ENES ULUDAĞ" imzası olarak, grafik alanının dışında durur.

## ÜST KATMAN (Enes 25.11 23:58 "teknik analizi daha da geliştir")
- Her hisse analizinde dip_tepe.py'den sonra `python3 invest/teknik_ust.py <T>` çalıştır; endeks yorumu için `teknik_ust.py genislik`.
- HİSSEYE ÖZEL SİNYAL KARNESİ: 10 dip işaretinin her birinin BU hissede 20 gün sonra kazandırma oranı; şu an yanan sinyallerin geçmiş başarısını söyle ("AVGO'da VIX 30 üstü sinyali 42 olayda %74 tuttu"). Genel kural yerine hisseye özel kanıt.
- PİYASA GENİŞLİĞİ (Nasdaq 100 bileşenleri): 20/50/200 günlük üstü oranı, 52 hafta dibine yakın oranı. 50G üstü <%15 = genişlik yıkanmış (dip için olumlu); >%85 = aşırı alım (tepe riski). Endeks düşerken genişlik nötrse "düşüş dar tabanlı, birkaç dev hisseden" de.
- HACİM: OBV ve birikim/dağıtım uyumsuzluğu (fiyat dipte, para akışı dipte değil = sessiz birikim), göreli hacim.
- GÜVEN SKORU 0-100 (dip işaretleri + hisseye özel sinyal başarısı + trend onay adımı + genişlik + hacim + 1d/4h yapı): ≥70 YÜKSEK, 45-69 ORTA, <45 DÜŞÜK. Enes'e tek cümle hükümle ver.
- Opsiyon verisi (put/call, gamma) Yahoo'da 401 verdiği için yok; Enes bağlarsa başka kaynak (Financial Datasets vb.) değerlendirilir.

## AMAÇ: ENES'İN ANALİZ KALİTESİ — OTOMATİK TWEET YOK (Enes 25.11 22:20)
- Bu yeteneğin hiçbir çıktısı (kart, seviye, plan, tarama, alarm) otomatik tweete/Buffer'a GİTMEZ; paylaşım turlarında konu adayı da yapılmaz. Yalnız Enes'e SendUserMessage/SendUserFile. Enes açıkça "bunu tweet at" derse ayrı iş olarak kural 84/86/89 ile ele alınır.
- Kaliteyi artıran döngü:
  1. SEVİYE TESTİ: Enes seviye verdiğinde `teknik_ek.py seviye_test <T> --seviyeler …` çalıştır — her seviyenin son 2 yılda kaç kez temas aldığı, kaçında ≥1 ATR tepki verdiği, kaçında kırıldığı. Tepki oranı ≥%50 ve ≥3 temas = "işe yarayan seviye"; düşük oranlı seviyeleri Enes'e açıkça söyle ("25.446 son 2 yılda 14 temasta yalnız 5 tepki verdi, zayıf").
  2. ANALİZ GÜNLÜĞÜ: her planı kaydet `teknik_ek.py gunluk ekle <T> <yukari|asagi> <giriş> <stop> <hedef> <gün> "<gerekçe>"`; sabah kontrolünde `gunluk kontrol` -> HEDEF/STOP/SÜRE DOLDU ve isabet karnesi. Enes'e haftalık (Pazar) karnesini ver: hangi gerekçe türü (FVG, OB, likidite süpürmesi, Enes seviyesi) daha çok tuttu.
  3. ÖN KONTROL LİSTESİ (her plandan önce, metinde ✓/✗ yazmadan kısa): üst zaman dilimi yönüyle uyumlu mu (MTF), seviye çakışma puanı ≥3 mü, seviye testi tepki oranı ≥%50 mi, R:R ≥2 mi, stop ≥0,5 x 4h ATR mi, beklenen hareket (VIX/VXN) hedefe izin veriyor mu, takvim riski (veri/Fed/bilanço/tatil) var mı. Eksik olanı tek satırda uyar.
  4. SENARYO OLASILIĞI: iki senaryoya kabaca olasılık ver (ör. %60/%40) ve dayanağını yaz (MTF puanı, istatistik modülü, seviye testi). Olasılık uydurma değil, bu verilerden türetilir; belirsizse "eşit" de.

## Kurallar
- Rakamlar yalnız veriden; uydurma seviye yok. ICT kavramları Türkçe açıklamalı (FVG = dengesiz boşluk, OB = emir bloğu, SSL/BSL = dip/tepe likiditesi, NWOG = haftalık açılış boşluğu).
- Tweet'e dönüşecekse kural 84 (grafik ham veriyle birebir), 86, 89 ve 54-F; hedef fiyat ve al/sat emri tweete yazılmaz (Enes'e özel analizde senaryo seviyeleri serbest).

## TELEFON KOMUTLARI (Enes 25.11 22:16 "çok daha geliştir, sadece telefondan yapabileyim")
Enes telefondan kısa mesaj yazar ya da grafik ekran görüntüsü atar; sen aşağıdakini çalıştırıp sonucu mobil biçimde (kart + en çok 2 ekran metin) verirsin. Soru sorma.
| Enes yazarsa | Çalıştır |
|---|---|
| "teknik NVDA" / "analiz et NVDA" / grafik ekran görüntüsü | `teknik_pro.py <T> --seviyeler <görüntüden okunan çizgiler> --png` + `teknik_ek.py derin <T> --seviyeler …` + `teknik_ek.py kart <T> --seviyeler … --out g/teknik_<T>.jpg` -> kartı ve 4h grafiği SendUserFile, özet metin |
| "derin NVDA" | `teknik_ek.py derin` (çakışma haritası, RSI uyumsuzluğu 1d/4h, pivot + Camarilla, Ichimoku, Bollinger sıkışması, oynaklık rejimi, VIX/VXN'den 1 gün/1 hafta beklenen hareket, Nasdaq 100'e göre göreli güç, mevsimsellik) |
| "tara" / "portföyü tara" / "tara NVDA,AMD,MU" | `teknik_ek.py tara [liste]` — varsayılan Enes portföyü (DOCN RKLB SITM AXON CBRS VRT AVGO NBIS); MTF puanına göre sıralı tablo |
| "istatistik NDX zirveden<-20" / "rsi<30 olunca ne oluyor" | `teknik_ek.py istatistik <T> "<koşul>"` (rsi<30, zirveden<-20, ema200_alti, gun_dustu>3): 20 yıl, koşula ilk giriş, 5/10/20/60 gün sonrası dağılım; <15 olay = güvenilmez de |
| "alarm NDX 24915 aşağı" | `teknik_ek.py alarm ekle <T> <seviye> <yukari|asagi> "<not>"`; her paylaşım turu başında `alarm kontrol` çalışır (tur_basi.sh), tetiklenince SendUserMessage: "ALARM: …" |
| "alarmlar" / "alarm sil 2" | `teknik_ek.py alarm liste` / `alarm sil <id>` |
- Ekran görüntüsünden seviye okuma: sağdaki fiyat etiketlerini (mavi kutular) aynen al, Türk biçimini (28.319,8) 28319.8'e çevir; trend çizgisini iki noktasıyla tarif et.
- Kart başlığında yön (MTF), en güçlü direnç ve destek (çakışma puanı en yüksek), günlük + 4h mini grafik olur.
- Çakışma puanı 3+ = GÜÇLÜ seviye. Planı bu seviyelere göre kur (giriş güçlü dirençte/destekte, stop bir sonraki seviyenin ötesinde, en az 0,5 x 4h ATR).

## ARTI KATMAN (Enes 26.11 00:00 "daha da geliştir") — `python3 invest/teknik_plus.py <T>`
- BENZER GÜNLER: bugünün parmak izine (20g/5g getiri, RSI, 200G'den ATR uzaklığı, zirveden düşüş, oynaklık yüzdeliği) en yakın 12 geçmiş gün (aralarında ≥30 gün) ve 5/20/60 gün sonrası: medyan, yukarıda biten oran, en kötü. Enes'e "geçmişte buna benzeyen 12 günün 9'unda 1 ay sonra yukarıdaydı" diye anlat.
- BEKLENEN HAREKET: 20 günlük oynaklıktan 1 hafta / 1 ay ±1σ bandı (~%68) ve oynaklık yüzdeliği; band dışı = haber/kırılım.
- MEVSİMSELLİK: içinde bulunulan ay ve bugünkü takvim gününden sonraki 20 işlem günü, yıllara göre.
- GÖRELİ GÜÇ: QQQ ve sektör ETF'i (SOXX/IGV/ITA/XLI); endeks için S&P 500 ve eşit ağırlık RSP. Göreli güç çizgisi 3 ay dibi = liderlik kaybı.
- TEPE RİSKİ SKORU 0-100 (tepe işaretleri, RSI>60, 200G'den >3 ATR, yüksek oynaklıkta yükseliş, göreli zayıflıkta yükseliş). Dip güven skoru (teknik_ust.py) ile birlikte ver.
- Benzer günler istatistiktir, garanti değildir; örneklem 12 olduğunu her zaman söyle.

## VERİ KALİTESİ VE KANIT KURALI (Enes 26.11 00:04 "kaliteli veri, daha iyi analiz")
- Tüm araçlar artık `veri_kalite.temiz()` üzerinden veri çeker (dip_tepe.yahoo): temettü/bölünme düzeltmeli OHLC, çift/boş mum atma, tepe/dip tutarsızlığı düzeltme, ertesi gün geri dönen bozuk sıçramaları ayıklama.
- Her analizin başında `python3 invest/veri_kalite.py <T>`: VERİ ESKİ / canlı mum / eksik gün / kısa geçmiş / sıfır hacim uyarısı varsa Enes'e ilk satırda söyle. Son kapanışı WebFetch ile ikinci kaynaktan doğrula (shell yalnız Yahoo'ya çıkıyor); fark >%0,5 ise belirt.
- KANIT KURALI: "%X tuttu" asla tek başına yazılmaz; yanına TABAN ORAN (rastgele bir günden aynı süre sonra yukarıda olma oranı) ve %95 güven aralığı (Wilson) gelir. Hüküm: alt sınır > taban = GÜÇLÜ; fark ≥8 = zayıf; ±8 içinde = farksız; ≤−8 = TERS. <10 olay = kanıt yok.
- YÖNTEM DOĞRULAMASI: `veri_kalite.py <T> --dogrula` benzer-gün yöntemini ve dip sinyallerini ileriye dönük (o günün verisiyle) test eder. 26.11 sonucu: AVGO ve NDX'te benzer-gün tahmini taban orandan FARKSIZ; AVGO'da yalnız VIX≥30 ve RSI≤32 zayıf üstünlük (+10/+11). Bu yüzden benzer günleri "bağlam" diye ver, tahmin diye değil; doğrulamada farksız çıkan aracı hükmün dayanağı yapma.

## SMC/ICT YARDIMCI ARAÇLAR (Enes 26.11 00:08) — `python3 invest/smc_ek.py <T> --tf 4h|1h|1d [--ortak X]`
- LİKİDİTE SÜPÜRMESİ: fitil eski onaylı dibin/tepenin ötesine geçip kapanış geri içeride; ardından MSS (karşı salınımın kapanışla kırılması). MSS yoksa iki tetik seviyesi ver: ana yapı ve erken iç yapı (önceki 2 mumun tepesi/dibi).
- FVG KALİTESİ 0-5: itki ≥1,5 ATR, itki mumu hacmi ≥1,5x, doğru bölge (boğa FVG indirimde, ayı FVG primde), henüz test edilmemiş, üst zaman dilimi yönüyle uyumlu. Fiyatın üstündeki ve altındaki en yakın 3 FVG listelenir.
- SMT: ortak enstrümanla (NDX↔S&P 500, NQ↔ES, hisse↔sektör ETF) biri yeni dip/tepe yaparken diğeri yapmıyorsa.
- GEÇMİŞ TESTİ (kanıt kuralı, bu enstrüman ve bu zaman dilimi): süpürme, süpürme+MSS, FVG'ye ilk dönüş (itkili/hacimli/doğru bölge) sonrası 10 mum; taban oran + Wilson. Sonuçlar `invest/smc_karne.json`'a yazılır; analizde yalnız GÜÇLÜ/zayıf kanıtlı araçları dayanak yap, TERS çıkanı (ör. NDX 4h tepe süpürmesi+MSS %9) Enes'e açıkça söyle.
- A+ KONTROL LİSTESİ 7 madde (üst TF uyumu, lehte süpürme, MSS, yakın kaliteli FVG, doğru bölge, SMT, geçmişte işe yarama): ≥6 A+, 4-5 B (onay bekle/küçük), ≤3 kurulum yok.
- 26.11 bulguları: AVGO günlükte dip süpürmesi tabanı geçiyor (%69 vs %60, 144 olay, GÜÇLÜ) ve 25.11'de 279,31 dibi süpürüldü; 4h'de süpürme+MSS TERS. NDX 4h'de süpürmeler farksız; hacimli FVG'ye dönüş zayıf üstünlük.

## İSVİÇRE ÇAKISI KATMANI (Enes 26.11 07:55-07:56 "TrendSpider'ın tüm özelliklerine bak, eksikleri bul, daha iyisini yap")
TrendSpider karşılıkları ve fazlası; hepsi Enes'e özel analiz için, otomatik tweet yok. Ortak motor `invest/gosterge.py` (70+ gösterge adı; `python3 invest/gosterge.py` listeler), Türkçe kural dili: "rsi<35 ve kapanis>ema200 ve h_trend=1" (ve / veya / değil). h_ önekli adlar HAFTALIK (son tamamlanan hafta) = çoklu zaman dilimi.
| Enes yazarsa | Çalıştır |
|---|---|
| "tara dip" / "tara rsi<30 ve h_trend=1" | `tarama.py <hazır|ifade> [--evren portfoy|ndx|hepsi|A,B] [--sirala rs20]` — 122 hisse; kalite puanı, 1 hafta bandı, kaç gündür, GEÇMİŞ KANIT satırı |
| "hazır taramalar" | `tarama.py hazir` (13 hazır: dip_avcisi, derin_dip, supurme_donus, kirilim, zirve_kirilim, sikisma, lider, trend_donus, altin_kesisim, geri_cekilme, birikim, asiri_alim, kirilim_asagi; yanında ÜSTÜN/FARKSIZ/TERS) |
| "izleme listesi" | `tarama.py liste` (dinamik liste; her sabah `tarama.py izle` günceller, 30 günde kapanır -> tarama karnesi = ileriye dönük test) |
| "backtest …" / "bu strateji çalışır mı" | `backtest.py <T|portfoy|ndx|hepsi> --giris "<ifade>" [--cikis] [--stop 2] [--hedef 4] [--sure 20] [--yon kisa] [--png]` |
| "formasyon AVGO" / "trend çizgisi" | `formasyon.py <T> [--tf 1d|4h|1wk] [--mtf]` |
| "ısı haritası" | `tarama.py isi --evren ndx --olcu getiri1|getiri5|rs20|rsi --out g/isi.png` -> SendUserFile |
| "raindrop AVGO" | `raindrop.py <T> --gun 30 --out g/rd.png` -> SendUserFile |
| "alarm: portföyde dip süpürmesi olursa" | `tarama.py alarm ekle <T|evren> "<ifade>" "<not>"`; her tur başında `alarm kontrol` (yanlıştan doğruya geçişte bir kez) |
| "ML AVGO" | `ml.py <T|evren> [--ufuk 10] [--model orman|lojistik]` |
- BACKTEST kuralları: sinyal kapanışta, giriş ertesi gün açılışta (ileriye bakma yok); stop ve hedef aynı gün = stop (kötümser); maliyet %0,1 gidiş-dönüş. Rapor: TABAN = rastgele girişler AYNI stop/hedef/süreyle (giriş üstünlüğünü adil ölçer), Wilson aralığı, örnek dışı (ilk %70 / son %30), eşik duyarlılığı (±%10/±%20), Monte Carlo (2000), çok hisselide her işlem sermayenin 1/5'i; HÜKÜM SAĞLAM / UMUT VERİCİ / ZAYIF. Tabanı geçmeyen strateji en fazla ZAYIF.
- Evren uyarısı: NDX listesi BUGÜNKÜ bileşenler (hayatta kalanlar) — geçmiş testler iyimser; bunu söyle. Tek hisse yerine evren testi tercih et.
- 26.11 KANIT (122 hisse, 10 yıl, 2 ATR stop / 4 ATR hedef / 15 gün): ÜSTÜN yalnız dip_avcisi (ort +1,29 vs rastgele +0,70) ve derin_dip (+2,13 vs +0,70); kirilim, lider, sikisma, trend_donus, geri_cekilme, altin_kesisim FARKSIZ; birikim TERS. ML (portföy, orman, 10 gün) AUC 0,46 -> İŞE YARAMIYOR. Bu sonuçları Enes'e açıkça söyle; FARKSIZ taramayı "fırsat" diye sunma, "izleme" diye sun.
- FORMASYON: ikili dip/tepe, OBO ve ters OBO, yükselen/alçalan/simetrik üçgen, yükselen/düşen kama, bayrak; boyun/kırılım, ölçülen hedef, geçersizlik, ONAY durumu ve BU hissede geçmiş başarısı (taban oranlı). Trend çizgileri pivot dokunma sayısıyla (≥3), ihlalsiz, fiyatın doğru tarafında ve ≤6 ATR uzaklıkta; --mtf ile haftalık çizgiler. Doldurulmamış boşluklar, otomatik Fibonacci.
- TrendSpider'da olup bizde OLMAYAN: gerçek zamanlı veri (Yahoo gecikmeli/gün sonu), opsiyon zinciri ve karanlık havuz verisi, aracı kurum emri/bot. Bizde olup onda olmayan: her sinyal için taban oranlı kanıt, örnek dışı + duyarlılık + Monte Carlo zorunlu, dürüst ML hükmü, SMC/ICT geçmiş testi.

## TRENDSPIDER EKSİKLERİNİN ÇÖZÜMÜ (Enes 26.11 08:21 "çözüm bul, yeteneklere ekle")
Shell yalnız Yahoo'ya çıkar (diğer siteler 403); bu yüzden: Yahoo'dan alınabilen her şey betikte, geri kalan WebFetch + kaydedici betik, işlem/anlık kurum verisi bağlayıcıyla.
1. ANLIK VERİ — `python3 invest/canli.py <T> [T2…]`: Yahoo 1 dk veri (seans öncesi/sonrası dahil; Nasdaq hisseleri ve NQ/ES vadelileri pratikte anlık, 'son veri' saatini her zaman yaz). Gün içi VWAP üstü/altı, ilk 30 dk açılış aralığı kırılımı, aynı saate kadar göreli hacim (RVOL), seans öncesi/sonrası aralık. Seviye takibi: `canli.py izle <T> <seviye> yukari|asagi --dk 5 --sure 120`; Enes isterse send_later ile 10-15 dk'lık kontrol zinciri (yalnız seans saatleri, iş bitince zinciri kır).
2. OPSİYON — WebFetch `https://chartexchange.com/symbol/nasdaq-<t>/optionchain/summary/` (NYSE: nyse-<t>), istem "CSV: expiration,call_open_interest,put_open_interest,call_volume,put_volume,put_call_ratio,max_pain; yorum yok" -> `alt_veri.py opsiyon <T> <fiyat> < csv`. Analiz: toplam put/call açık pozisyon, en yakın ve aylık vade max pain (fiyata uzaklık), en büyük açık pozisyon vadesi, önceki kayda göre korunma değişimi. Vadeye yakın max pain = mıknatıs olabilir, yön sinyali değil.
3. KARANLIK HAVUZ / BORSA DIŞI — WebFetch `chartexchange.com/symbol/nasdaq-<t>/stats/` (bugünkü borsa dışı hacim % ve 30 gün ort %), `/short-volume/` (FINRA günlük kısa satış payı), `https://tapeboard.com/dark-pool/<T>` (FINRA haftalık ATS hacmi, 4 hafta değişim, en büyük havuzlar), `/borrow-fee/` (ödünç ücreti) -> `alt_veri.py karanlik <T> --offex --offex30 --kisa --ats_degisim --odunc`. Resmi dosya: `cdn.finra.org/equity/regsho/daily/CNMSshvol<YYYYMMDD>.txt` (büyük, offset ile). Analiz `alt_veri.py analiz <T>`; borsa dışı pay 30 gün ortalamasından +5 puan = kurumsal blok ilgisi; DIX mantığı: borsa dışı kısa hacim payı yüksek = piyasa yapıcı alımı. Kayıtlar `invest/alt_veri/` altında birikir; 30+ kayıt olunca taban oranlı kanıt ölç, o güne kadar "kanıt birikiyor" de.
4. BOT — `python3 invest/kagit_bot.py calis|durum`: SANAL işlem botu (gerçek emir yok), backtest ile aynı kurallar (ertesi açılış girişi, 2 ATR stop, 4 ATR hedef, 15 gün, en çok 5 pozisyon %20'şer, 100.000 sanal $), stratejiler = tarama_kanit.json'da ÜSTÜN olanlar. Her sabah 09:00 çalışır; canlı sonuç backtest ve rastgele girişle kıyaslanır (30 işlemden önce hüküm yok).
5. GERÇEK ARACI KURUM — yalnız Enes kendi hesabını bağlarsa (Interactive Brokers bağlayıcısı: anlık fiyat, pozisyon, emir talimatı). Kural: hiçbir gerçek emir Enes'in o emir için ayrı ve açık "onaylıyorum" yazısı olmadan gönderilmez; otomatik/bot emri YOK; emirler tweete ya da başka yere yazılmaz.
6. EK VERİ BAĞLAYICILARI (bağlanırsa öncelik): Financial Datasets (kurulumu yarım kaldı; fiyat yedek kaynağı + içeriden alım/satım + kurumsal sahiplik), Alpha Vantage (opsiyon zinciri ve Yunan harfleri, gün içi veri, haber duygu skoru). Bağlıysa WebFetch yolunun yerine bunları kullan.

## ALPHA VANTAGE (Enes 26.11 08:26 bağladı) — ücretsiz anahtar
- Sınır: günde 25 istek, saniyede 1 → çağrıları SIRAYLA yap (paralel çağrı hata verir), her çağrıdan sonra `python3 invest/alt_veri.py av 1` (sayaç). Sabah görevi ~18 istek kullanır, ~7 Enes'in gün içi isteklerine kalır.
- ÇALIŞAN (ücretsiz): REALTIME_PUT_CALL_RATIO (tüm zincir + vade bazlı, işlem hacmine göre), HISTORICAL_PUT_CALL_RATIO (2008'den, tarih bazlı → geçmiş doldurma ve kanıt), INSIDER_TRANSACTIONS (yönetici alım/satımı), şirket temel verileri ve teknik gösterge uçları.
- ÜCRETLİ (bu anahtarla ÇALIŞMIYOR, örnek/sahte veri döner — ASLA kullanma): REALTIME_OPTIONS, HISTORICAL_OPTIONS (Yunan harfleri, IV), NEWS_SENTIMENT. REALTIME_OPTIONS "ARTIFICIAL" uyarılı örnek döndürür: bunu veri sanma.
- Akış: put/call JSON → `alt_veri.py pc <T>` (stdin; JSON'da "date" yoksa bugünün tarihi yazılır, gerçek tarihi ekle) ; içeriden işlem JSON → `alt_veri.py iceriden <T>` ; `alt_veri.py analiz <T>` = opsiyon OI/max pain (chartexchange) + karanlık havuz + put/call geçmişi (z skoru, 30+ kayıtta 10 gün sonrası kanıtı). Geçmiş doldurma planı: `alt_veri.py plan 10`.
- Put/call iki türü karıştırma: chartexchange = AÇIK POZİSYON (OI) oranı; Alpha Vantage = İŞLEM HACMİ oranı. Raporda hangisi olduğunu yaz.
- Anlık fiyat için Yahoo 1 dk (canli.py) yeterli; Alpha Vantage GLOBAL_QUOTE'u bütçe yemesin diye yalnız Yahoo'nun boş kaldığı durumda kullan.

## BIGDATA.COM (Enes 26.11 08:33 bağladı) — kredili (1000 kredi = 10 $)
- Maliyet: `bigdata_search` ~7 kredi, tablo araçları (portfolio/history tearsheet) ~3, `find_securities` ~0. Günlük üst sınır ~30 kredi; bakiyeyi `bigdata_help` ile gör. Gereksiz arama yapma, `max_chunks` 6-8 yeter.
- Portföy ID'leri `invest/alt_veri/bigdata_id.json` (AVGO 09DE1F, DOCN 5B1011, RKLB 8BBCDA, SITM 96A2D3, AXON D2AC74, CBRS BD0A16, VRT 96D34D, NBIS B45FD2). Yeni hisse için `find_securities` (ücretsiz) ve dosyaya ekle.
- Ne için kullan:
  1. `bigdata_portfolio_tearsheet` (tek çağrı, 8 hisse): seans öncesi/sonrası fiyat ve alış-satış, haber duygu skoru (−1..+1, yön oku), analist hedefi (düşük/medyan/yüksek), son EPS sürprizi. Hedefler eski kalmış olabilir; fiyata göre %100+ uzak hedefi "güncellenmemiş" say.
  2. `bigdata_history_tearsheet`: ORTEX günlük açığa satış tahmini (serbest dolaşıma oran, kapatma günü, ödünç ücreti), en çok 5 hisse/çağrı → CSV'yi `python3 invest/alt_veri.py si` ile kaydet; `alt_veri.py analiz <T>` "açığa satış 4 haftada ve fiyat" okumasını verir (düşüşe ekleme = baskı + sıkışma yakıtı; düşüşte azalma = satıcı yorgunluğu). Bu, karanlık havuz verisinden daha doğrudan bir konumlanma ölçüsüdür.
  3. `bigdata_search` (smart): "neden hareket etti" haberleri, bilanço görüşmesi metinleri, SEC belgeleri, analist notları; kaynak + tarih + bağlantıyla alıntıla. Teknik analizde "haber/katalizör" satırı için.
  4. `bigdata_events_calendar`: bilanço ve makro takvim (teknik plandaki takvim riski kontrolü).
- Bilgi Enes'e gidiyorsa kaynak adını "Bigdata.com" yaz. Tweet'e girecekse kural 23 (iki kaynak) geçerli.

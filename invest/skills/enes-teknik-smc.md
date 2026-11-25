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

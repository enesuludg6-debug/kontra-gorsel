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

## Kurallar
- Rakamlar yalnız veriden; uydurma seviye yok. ICT kavramları Türkçe açıklamalı (FVG = dengesiz boşluk, OB = emir bloğu, SSL/BSL = dip/tepe likiditesi, NWOG = haftalık açılış boşluğu).
- Tweet'e dönüşecekse kural 84 (grafik ham veriyle birebir), 86, 89 ve 54-F; hedef fiyat ve al/sat emri tweete yazılmaz (Enes'e özel analizde senaryo seviyeleri serbest).

# TAKVİM (kesin kural 16) — bilanço ve veri saatleri, hız protokolü

Her Pazar 20:00 gelecek 7 gün yazılır, her gün 09:05 güncellenir. Her satır için HAZIRLIK (T-45/60 dk) ve YAYIN (T-2 dk) görevleri kurulur.
TSİ = ET + 8 saat (ABD kış saati, 2 Kasım 2026 - 8 Mart 2027).

| Tarih | Saat TSİ | Şirket/Olay | Tür | Beklenti (2 kaynak) | Bülten kaynağı | Hazırlık görevi | Yayın görevi | Durum |
|---|---|---|---|---|---|---|---|---|
| 17.11 Sal | ~14:00 (06:00 ET) | Home Depot (HD) | bilanço açılış öncesi | HBK 3,84 $, gelir 42,81 Mr $ (MarketBeat, Investing, TipRanks) | ir.homedepot.com, Business Wire | 13:06 (HD+DIS) | 13:58 | kuruldu |
| 17.11 Sal | ~14:40 (6:40 ET, Earnings Whispers); konferans 16:30 | Disney (DIS) | bilanço açılış öncesi (mali 2026 Q4) | HBK 1,67-1,69 $, gelir 25,2-25,3 Mr $ (Investing, TipRanks, Zacks, EW) | disney.com/investors, Business Wire | 13:06 (HD+DIS) | 14:38 | kuruldu |
| 17.11 Sal | 16:30 | Ekim perakende satışları | veri | manşet +%0,2 (Continuum, ActionForex, TokenPost); araç+benzin hariç +%0,3 (Continuum, RBC); kontrol +%0,3 (RBC, tek); Eylül +%0,8 | census.gov/retail | 15:40 | 16:28 | kuruldu |
| 18.11 Çar | ~00:20 | Nvidia (NVDA) | bilanço kapanış sonrası (16:20 ET) | gelir 108,8-109,3 Mr $ (Visible Alpha/S&P 109,3; Seeking Alpha 108,81; OANDA ~109; Chartmill 111,36 aykırı), HBK 2,47-2,49 $ (takvim 2,47; FourWeekMBA 2,49; Chartmill 2,53), veri merkezi 101,2-102 Mr $ (Zacks 101,24; Coinpedia ~102), brüt marj rehberi %74,0 ±0,5 (FourWeekMBA + Zacks), şirket gelir rehberi 108,0 ±%2 (FourWeekMBA + OANDA + AskTraders); bülten 16:20 ET = 00:20 TSİ, görüşme 01:00 (ecorpit) | nvidianews.nvidia.com, GlobeNewswire | 23:25 | 00:18 | kuruldu; tahminlerim 12:22 önizlemede |
| 18.11 Çar | 14:30 (6:30 ET; hazırlıkta O-001 ile doğrulanacak) | Target (TGT) | bilanço açılış öncesi (mali 2026 Q3) | HBK 2,04 $ (Zacks) / 2,07 $ (Investing), gelir 26,4-26,47 Mr $; opsiyon ±%8 | corporate.target.com | 13:30 | 14:28 | kuruldu (isler.py) |
| 18.11 Çar | 22:00 | FOMC toplantı notları | veri | - | federalreserve.gov | | | |
| 19.11 Per | ~00:05 TSİ (18.11 kapanış sonrası ET) | Palo Alto (PANW) | bilanço (mali 2027 Q1; şirket rehberi gelir 3,30-3,31 Mr $, HBK 0,96-0,98 $ — Nasdaq, Zacks) | doğrulanacak | investors.paloaltonetworks.com | | | (tarih doğrulanacak) |
| 19.11 Per | 15:00 (7:00 ET; Earnings Whispers + Walmart IR 6:00 CT düzeni); görüşme 16:00 (days.to) | Walmart (WMT) | bilanço açılış öncesi (mali 2027 Q3) | HBK 0,64 $ (Zacks, Earnings Whispers), gelir 186,5-187,3 Mr $ (Zacks, Investing) | stock.walmart.com | 14:00 | 14:58 | kuruldu (isler.py) |
| 19.11 Per | açılış öncesi (EW 5:30 ET = 13:30 TSİ); görüşme 15:00 (7:00 ET) | Alibaba (BABA) | bilanço (mali 2027 Q2) | gelir 40,2-40,5 Mr $, HBK 1,62-1,63 $ (MarketBeat, TipRanks, EW) | businesswire / alibabagroup.com | 12:02 | 13:15 | kuruldu (Enes 12:01) |
| 19.11 Per | ~00:05 TSİ (4:05 PM ET, 18.11 kapanış sonrası); görüşme 01:00 TSİ (2:00 PM PT) | Everpure (P, eski Pure Storage) | bilanço (mali 2027 Q3) | HBK 0,77-0,78 $ (FXEmpire, Arincen), gelir 1,33-1,36 Mr $; Earnings Whisper 0,81 | investor.everpuredata.com | 23:15 | 00:05 | kuruldu (isler.py; Enes 13:16 bol tweet) |
| 20.11 Cum | ~00:00 TSİ (19.11 4:00 PM ET kapanış sonrası) | Intuit (INTU) | bilanço (mali 2027 Q1) | gelir ~4,30-4,31 Mr $ (Earnings Whispers, Tiger), şirket rehberi 4,29-4,31 Mr $ / düz. HBK 2,44-2,48 $; whisper 2,59 | BusinessWire | 23:00 | 23:58 | kuruldu (isler.py, sabah 19.11) |

## Şükran Günü haftası (23-27.11.2026, kaynak: Gotrade + Leafy/Substack + RoboForex + UnifyBrowse + Coingabbar)
- Çar 25.11 16:30 TSİ: Ekim PCE + 3. çeyrek GDP ikinci tahmin + haftalık işsizlik başvuruları (perşembeden alındı). 22:00 Bej Kitap.
- Per 26.11: Şükran Günü, NYSE/Nasdaq KAPALI.
- Cum 27.11: hisse 21:00 TSİ erken kapanış (opsiyon 21:15).
- Bu hafta bilanço: Dell, HPE, Analog Devices, Deere, Best Buy (tarihler takvimde ayrıca doğrulanacak; yalnız YZ ile ilgili olanlar tweet).
- Fed toplantısı 8-9 Aralık.

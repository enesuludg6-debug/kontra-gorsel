# PERFORMANS (kesin kural 14) — hangi tweet işe yarıyor

Her gün 09:05'te önceki günün tweetleri eklenir (Buffer get_post includeMetrics). Her Pazar 21:30 haftalık rapor.
Türler: VADELI, 13F, BILANCO-RAKAM, BILANCO-ANALIZ, BILANCO-ONIZLEME, ANALIST, SONDAKIKA, BAGLAM-GORUS, KAPANIS, TAKVIM, EGITICI, ENES-ISTEGI.

| Tarih | Saat | Tür | Konu | Düzen | Buffer id | Görüntülenme | Beğeni | Yanıt | Repost | Etkileşim % |
|---|---|---|---|---|---|---|---|---|---|---|
| 17.11 | 09:06 | VADELI | vadeli | isi | 6afbeed43e42cd001e578f96 | | | | | |
| 17.11 | 09:38 | 13F | Berkshire | bento | 6afbf65c3e42cd001e5a104c | | | | | |
| 17.11 | 10:13 | 13F | Ackman | uclu | 6afbfe90c6d951405b4cb992 | | | | | |
| 17.11 | 10:48 | 13F | Druckenmiller | dortlu | 6afc06ae81189bfde7f5c68c | | | | | |
| 17.11 | 11:13 | 13F | Tepper | ilerleme | 6afc0c91e445e0ec2b8b98f2 | | | | | |
| 17.11 | 11:41 | 13F | Soros | editoryal | 6afc132e99aa510fba465599 | | | | | |
| 17.11 | 12:14 | BAGLAM-GORUS (ENES-ISTEGI) | Nasdaq düşüş analizi | siralama | 6afc1ae2f94854b5e25e0f96 | | | | | |
| 17.11 | 12:22 | BILANCO-ONIZLEME (ENES-ISTEGI) | NVDA önizleme | bento | 6afc1c6d64f1073d81d26e1d | | | | | |
| 17.11 | 12:48 | 13F | Third Point | dortlu | 6afc22f305a7e8ecf8518a48 | | | | | |
| 17.11 | 13:16 | TAKVIM | key levels + başlıklar | takvim | 6afc2993ec24b44737d789b8 | | | | | |
| 17.11 | 14:07 | BILANCO-RAKAM | HD 3. çeyrek | uclu | 6afc3572681dcb15ba481a1e | | | | | |
| 17.11 | 14:16 | BAGLAM-GORUS (ENES-ISTEGI) | NVDA ihracat komitesi | editoryal | 6afc377e7e5c00d2a8e2106f | | | | | |
| 17.11 | 14:25 | BILANCO-ANALIZ | HD analiz | ilerleme | 6afc398a7eae93f519187b15 | | | | | |
| 17.11 | 14:44 | BILANCO-RAKAM | DIS 4. çeyrek | uclu | 6afc3e059d7d4c6b78587178 | | | | | |
| 17.11 | 15:01 | BILANCO-ANALIZ | DIS analiz | dortlu | 6afc4216b9fb95e12d03db93 | | | | | |
| 17.11 | 15:21 | VADELI | öğlen vadeli | isi | 6afc46d2bea63ad8bdd00a08 | | | | | |

## Haftalık raporlar
(Pazar 21:30'da eklenir: türe göre ortalama, en iyi/en kötü 5, saat dilimi, düzen, önerilen karışım.)
| 17.11 | 16:31 | MAKRO-SONUC | Ekim perakende satislari | editoryal | 6afc5731686bdd2a3c12d718 |

### KARIŞIM ÖNERİSİ #1 (17.11 17:20, Enes isteğiyle erken; veri 15.11-17.11 09:00, ölçülen 124 tweet; Buffer metrikleri ~24 saat gecikmeli; GÜVEN DÜŞÜK)
Bulgular: ortalama görüntülenme ~480, tweet türleri arasında fark küçük; en yüksekler görüş/duruş içerenler (YTD paylaşımı 3290, RKLB grafik görüşü 1475, NBIS 1466, "tepeden almanızı" 1225, portföy güncellemesi 1223). Düz haber/bilanço medyanı ~340-370. 13F (ER %1,4) ve eğitici (ER %1,2) en düşük etkileşim. 16.11'de 78 tweet atıldı: adet arttıkça tweet başı görüntülenme artmadı. Saat (TSİ, ort. görüntülenme): 09-12 350, 12-15 633, 15-18 470, 18-21 385 (en kalabalık 36 tweet, en düşük), 21-24 602, 00-03 530.
Önerilen günlük karışım (toplam 12-15):
| Tür | Günlük | En iyi dilim |
|---|---|---|
| Görüşlü hisse/tema analizi (bağlam + görüş, kural 25) | 4-5 | 12-15, 21-24 |
| Bilanço (büyük isimlerde rakam + 15 dk sonra yorumlu analiz) | 2-4 (bilanço günü) | açıklama anı |
| Son dakika (2 kaynak + yorum) | 1-2 | anında |
| Piyasa: sabah vadeli + key levels + kapanış | 3 | 09, 10:30, 00:05 |
| Makro veri (tek yorumlu tweet) | veri günü 1 | açıklama anı |
| Analist notu (yorumlu) | 0-1 | 12-15 |
| 13F (sezonda) | en çok 2 | 12-15 / 21-24 |
| Eğitici | haftada 3 (alt sınır), ölçülecek | 21-24 |
- 18-21 dilimini seyrelt (en çok 2). Durum: ÖNERİ, Enes "onay" yazınca DURUM.md "İçerik karışımı" ve skill'e işlenir.
- Sonraki öneri: 3 hafta sonra (periyot.py; ~08.12, ilk Pazar raporu 13.12).
| 17.11 | 17:36 | MAKRO-YORUM | Perakende yorum (kural 25) | uclu | 6afc666ed41d8612acc8a60e |
| 17.11 | 19:32 | 13F | 13F Greenlight Einhorn | dortlu | 6afc8184104bf3e624906e5f |
| 17.11 | 21:07 | BAGLAM-GORUS | NVDA bilanco oncesi satis | ilerleme | 6afc97e032ea84693c3376ba |
| 17.11 | 22:16 | YARIN-NE-VAR | TGT, FOMC tutanaklari, PANW | takvim | 6afca8229c73f3089bb12fe8 |
| 17.11 | 22:41 | EGITICI | Ileri F/K nasil okunur | editoryal | 6afcadf6ad43efddcc54c27a |
| 17.11 | 23:06 | BAGLAM-GORUS | TSM iki gunde yuzde 10 | cizgi | 6afcb3cf7847359f57adbac4 |
| 17.11 | 23:19 | EGITICI | VIX nasil okunur | uclu | 6afcb6d57338fb226f833d32 |
| 18.11 | 00:06 | KAPANIS | 17.11 kapanis | isi | 6afcc1cf9b0477630c937e20 |
| 18.11 | 00:23 | BILANCO-RAKAM | NVDA 3. ceyrek | uclu | 6afcc5b9fa88ce86dcb0cb94 |
| 18.11 | 00:25 | BILANCO-RAKAM | NVDA 3. ceyrek tam format (Enes) | uclu | 6afcc632bbe886f1b5140175 |
| 18.11 | 00:41 | BILANCO-ANALIZ | NVDA 3. ceyrek analiz | ilerleme | 6afcca0949939c25efa18bb2 |
| 18.11 | 01:08 | DETAY | NVDA taahhutler | grafik2 | 6afcd043536cf08383ca8135 |
| 18.11 | 01:31 | OPSIYON | TGT ve PANW bilanco oncesi opsiyon beklenen hareket | editoryal | 6afcd5d48e2194ed032b0fb1 |
| 18.11 | 11:02 | KEY-LEVELS | Gunun basliklari 18.11: NVDA sonrasi vadeliler, TGT, FOMC, PANW, WMT | takvim | 6afd5b93739d5342ff13f3ef |
| 18.11 | 11:17 | 13F | 13F Coatue Q3 2026: MSFT +%120, CRM yeni, META +1,99 Mn, SHOP/V/ICE yeni | dortlu | 6afd5f0e45783105f4378a2f |
| 18.11 | 11:42 | BILANCO-ANALIZ | Cagri NVDA 1/2: GPU kira fiyatlari (Hopper 2x, B300 +%60, token -%60) | uclu | 6afd64f0805b2f3bff40e508 |
| 18.11 | 11:43 | BILANCO-ANALIZ | Cagri NVDA 2/2: yonetim kurulu Jensen geri donmuyor, CEO takvimi yok, %75 rehber | editoryal | 6afd652c45783105f439a82c |
| 18.11 | 12:07 | 13F | 13F Tiger Global Q3 2026: CBRS +%48, INTC +%30, NVDA +%7, DHR +%178; TSM -%36, META -%20 | siralama | 6afd6ad3d015b337f13f0f87 |
| 18.11 | 12:41 | EGITICI | 13F nasil okunur: 45 gun gecikme, kapsam, baglam | zaman | 6afd72da085e629e46f362eb |
| 18.11 | 13:12 | BAGLAM-GORUS | Nvidia sonrasi acilis oncesi: neocloud NBIS IREN CRWV +%6-8, AMD +%3 | isi | 6afd79f3e4de71c5c6d9b5c8 |
| 18.11 | 13:57 | 13F | 13F Baupost Q3 2026: HONA ve SITE yeni, AXTA 2 kat, CME ekleme, GOOG azaltma, 4 cikis | dortlu | 6afd8483f4526871ade0df85 |
| 18.11 | 14:37 | BILANCO-RAKAM | TGT 3. ceyrek rakam | uclu | 6afd8de467b44b742a4f425d |
| 18.11 | 14:47 | BILANCO-ANALIZ | TGT 3. ceyrek analiz (kural 45) + kural 21 duzeltme | editoryal | 6afd904667b44b742a50348c |
| 18.11 | 15:01 | BILANCO-DETAY | TGT kategoriler | ilerleme | 6afd93b567b44b742a51bb38 |
| 18.11 | 15:02 | BILANCO-DETAY | TGT guzellik / Beauty Studio | zaman | 6afd93f103c6b6e75e05a645 |
| 18.11 | 15:41 | BILANCO-GORUS | LOW 3. ceyrek | uclu | 6afd9d1467b44b742a562442 |
| 18.11 | 15:42 | ANALIST | NVDA bilanco sonrasi analist hedefleri | editoryal | 6afd9d4767b44b742a563ffd |
| 18.11 | 16:42 | BILANCO-GORUS | TJX 3. ceyrek | ilerleme | 6afdab3ab1824861ddb9bc98 |
| 18.11 | 16:58 | 13F | 13F Himalaya Li Lu Q3 | dortlu | 6afdaf05b24db460bb0445cc |
| 18.11 | 18:08 | UZUN-GORUS | Yapay zeka stres testi: deger dar alanlara kayiyor (Enes metninden) | uclu | 6afdbf70b3f8322ac7454d4d |
| 18.11 | 18:26 | PIYASA | Nasdaq acilis: cipler yukari, yazilim/perakende asagi | editoryal | 6afdc3b06a70d040da0077e4 |
| 18.11 | 18:27 | PORTFOY | RKLB 100. Electron + siparis defteri | zaman | 6afdc3db0a7aa6dca2c72948 |
| 18.11 | 18:46 | BEKLENEN-HAREKET | NVDA opsiyon 8,5 vs gercek ~-1 | ilerleme | 6afdc85cb3f8322ac7492dc0 |
| 18.11 | 19:23 | ENES | Bellek geri alim + sermaye rekabeti (Enes metni) | uclu | 6afdd0f9b35a3030f043de24 |
| 18.11 | 19:36 | PORTFOY | AXON RBC konferansi + Q3 yazilim | editoryal | 6afdd415b35a3030f0453b15 |
| 18.11 | 21:28 | ENES-TEKNIK | RKLB SMC teknik analiz (Enes gorselleri, zamanli 21:28) | enes-grafik | 6afdd9107f787ce2b19347c4 |
| 18.11 | 20:08 | ENES-TEKNIK | VRT SMC teknik analiz (Enes gorselleri) | enes-grafik | 6afddb974a03ad131e7dd5ee |
| 18.11 | 20:15 | ENES-TEKNIK | CBRS SMC/ICT teknik analiz (Enes gorselleri) | enes-grafik | 6afddd3e4b233b0b898aab73 |
| 18.11 | 20:33 | BILANCO-ONIZLEME | PANW 1. ceyrek onizleme | uclu | 6afde163ba7cb28cce133902 |
| 18.11 | 20:51 | 13F | Lone Pine Q3 teknoloji hamleleri | dortlu | 6afde59ea11f24337a0f73c8 |
| 18.11 | 21:16 | BILANCO-ONIZLEME | Everpure 3. ceyrek onizleme + opsiyon | editoryal | 6afdeb88144d89f0a5b5ff42 |
| 18.11 | 22:10 | MAKRO | FOMC ekim tutanaklari | zaman | 6afdf820badbce99d00612fa |
| 18.11 | 22:13 | SON-DAKIKA | AAOI 550 Mn ATM hisse satisi | uclu | 6afdf8d37d64a85c92a34bf9 |
| 18.11 | 22:27 | SON-DAKIKA | SpaceX 40 Mr bilanco disi cip finansmani | spotlight | 6afdfc1df83633dc1bab10a6 |
| 18.11 | 22:51 | SON-DAKIKA | Cip rotasyonu AVGO AMD vs NVDA | editoryal | 6afe01c950f5b9552ad175a3 |
| 18.11 | 23:07 | BEKLENTI | PANW konsensus beklentisi | beklenti | 6afe057a750db4a2bff35f26 |
| 18.11 | 23:16 | BEKLENTI | Everpure konsensus beklentisi | beklenti | 6afe07951173b0b5f0e15539 |
| 18.11 | 23:38 | PORTFOY | CBRS analist hedef kesintileri ve dusus | uclu | 6afe0cb8f5888642f69cd6b3 |
| 19.11 | 00:11 | BILANCO-RAKAM | PANW Q1 FY27 rakam | uclu | 6afe14876fadb4be7117d535 |
| 19.11 | 00:12 | BILANCO-RAKAM | Everpure Q3 FY27 rakam | uclu | 6afe14c7a8bd8e4ffd19e8e7 |
| 19.11 | 00:23 | BILANCO-ANALIZ | PANW Q1 FY27 analiz | editoryal | 6afe17300d8c064ce4d8c374 |
| 19.11 | 00:38 | BILANCO-DETAY | PANW hisse sayisi 709->838 Mn (+%18), FY27 844-847 Mn | spotlight | 6afe1ac149e7044385b1ee05 |
| 19.11 | 00:38 | BILANCO-DETAY | PANW gelir kirilimi urun 595 Mn +%37, abonelik 2,85 Mr +%40, %83 | cam | 6afe1ac461993df3280862d4 |
| 19.11 | 00:38 | BILANCO-DETAY | PANW nakit OCF 1,93 vs 1,77 Mr, FCF 1,94 Mr %56,2, yil hedef %38 | terminal | 6afe1ac661993df328086411 |
| 19.11 | 00:38 | BILANCO-DETAY | PANW GAAP 96 Mn vs duz 1,06 Mr faaliyet, HBK 0,57 vs 1,05 | split | 6afe1ac94cec3cf024f1225d |
| 19.11 | 00:38 | BILANCO-DETAY | PANW NGS ARR 9,10->9,73, Q2 10,20-10,22, FY 11,475-11,525 (onceki 11,075-11,175) | zaman | 6afe1acbaff6b481b2ae1947 |
| 19.11 | 00:42 | BILANCO-ANALIZ | Everpure Q3 FY27 analiz | uclu | 6afe1bc70801c920897af721 |
| 19.11 | 01:18 | detay | P: RPO ve ertelenmiş gelir | uclu | 6afe2420c462756e9e21fa0d |
| 19.11 | 01:22 | detay | P: Serbest nakit ve geri alım | zaman | 6afe2423a588bd66879e5ee6 |
| 19.11 | 01:26 | detay | P: Ürün marjı düşüşü | spotlight | 6afe2424c69bd1cb888755fc |
| 19.11 | 01:30 | detay | P: Rehber ve büyüme | grafik2 | 6afe242401ba7c5e7917c41b |
| 19.11 | 01:34 | detay | P: Yapay zekâ kazanımları | editoryal | 6afe2425ebd4409dc9fcb37e |
| 19.11 | 01:52 | son-dakika | NVDA: Huang dönmüyor, çalışan toplantısı | zaman | 6afe29b101ba7c5e7919d7b0 |
| 19.11 | 11:01 | baslik | Günün başlıkları: vadeli; WMT; INTU; PANW | takvim | 6afeacef7dcd23a28ea92fa2 |
| 19.11 | 11:26 | yapay-zeka | GOOGL: Gemini 4 Neon | uclu | 6afeb2b7fba2406b99ae654d |
| 19.11 | 11:42 | cagri | PANW çağrı: acil durum bütçeleri | split | 6afeb6746d068c1c9d6701b6 |
| 19.11 | 11:50 | cagri | PANW çağrı: ajan trafiği ücretlendirme 6-9 ay | spotlight | 6afeb6776d068c1c9d6703b1 |
| 19.11 | 11:56 | cagri | PANW çağrı: Applied Compute 1 Mr ARR hedefi | editoryal | 6afeb6786d068c1c9d670415 |
| 19.11 | 12:02 | cagri | PANW çağrı: segment büyümesi ve 170 platform geçişi | terminal | 6afeb6792276cdcb15da1482 |
| 19.11 | 14:30 | 13f | 13F Viking Global: TSLA TSM GOOGL META | dortlu | 6afeb8c44a35072d027c8425 |
| 19.11 | 12:02 | beklenti | BABA bilanço beklentisi | beklenti | 6afebb054ad8a97b3a2d1698 |
| 19.11 | 12:12 | cagri | P çağrı: hyperscaler marjı %75-85 | spotlight | 6afebd8073dee41859366c49 |
| 19.11 | 12:20 | cagri | P çağrı: NAND maliyeti yüksek kalacak | split | 6afebd834ad8a97b3a2e5ccd |
| 19.11 | 12:26 | cagri | P çağrı: rehber 3. kez yükseldi; 2. hyperscaler gelecek yıl; FY28 | zaman | 6afebd8373dee41859366cf1 |
| 19.11 | 12:36 | haber | AMD: Taalas alımı tamamlandı | uclu | 6afec330bad67efd5adc1ba8 |
| 19.11 | 13:01 | 13f | 13F Bridgewater: NVDA QCOM MU SNDK | terminal | 6afec8eea51c94c1af71f097 |
| 19.11 | 13:16 | bilanco-rakam | BABA mali 2027 Q2 rakamları | uclu | 6afecc95ec3834f154504283 |
| 19.11 | 13:38 | portfoy | RKLB: Neutron fiyat 70 Mn; 16 görev | editoryal | 6afed1b6ffd0192517a92bde |
| 19.11 | 13:47 | bilanco-analiz | BABA Eylül 2026 çeyreği analiz | spotlight | 6afed3a8528b203593ecc2bc |
| 19.11 | 14:01 | beklenti | WMT bilanço beklentisi | beklenti | 6afed6f67c25de751c34e374 |
| 19.11 | 14:11 | detay | BABA detay: bulut kalitesi (dış +%64; tekrarlayan +%67) | uclu | 6afed95e7fc65314b9ec2d45 |
| 19.11 | 14:19 | detay | BABA detay: e-ticaret ve hızlı teslimat | split | 6afed961ec3834f154558ede |
| 19.11 | 14:25 | detay | BABA detay: kasa geri alım temettü | zaman | 6afed9627fc65314b9ec2f41 |
| 19.11 | 14:38 | 13f | 13F Baillie Gifford: LRCX KLAC ARM SPCX | terminal | 6afedfb4f365ba93c5823ad7 |
| 19.11 | 15:07 | bilanco-rakam | WMT Ekim 2026 çeyreği rakamları | uclu | 6afee66f2938086e1d4d8e9a |
| 19.11 | 15:17 | bilanco-analiz | WMT Ekim 2026 çeyreği analiz (makro) | editoryal | 6afee8d0fcd8732ff211a6d0 |
| 19.11 | 15:32 | detay | WMT detay: ilaç fiyat düzenlemesi ve GLP-1 | split | 6afeec462b33bbf880bb151f |
| 19.11 | 15:38 | detay | WMT detay: düzeltilmiş faaliyet kârı temposu 17;4 -> 5;5 | spotlight | 6afeec482d4643e56c937866 |
| 19.11 | 15:44 | detay | WMT detay: üyelik +%17 ve 120 $ paket | zaman | 6afeec495eafbd656fdd9b20 |
| 19.11 | 15:48 | son-dakika | PANW ön piyasa +%9; siber güvenlik rallisi | uclu | 6afef012d541877eb93a6454 |
| 19.11 | 17:40 | 13f | 13F ARK: NVDA SPCX TSLA | editoryal | 6afef7cb03dff68ab45a60ae |
| 19.11 | 16:41 | cagri | BABA çağrı: yerli çip ana motor | split | 6afefca3b3b455c2f570013f |
| 19.11 | 16:52 | cagri | BABA çağrı: nakit takvimi 2028 2. yarı | zaman | 6afefca503dff68ab45c3e12 |
| 19.11 | 17:07 | vadeli | Açılış öncesi vadeliler; 10 yıllık %5; Fed tutanakları | isi | 6aff02b2abf4ba608b78c9d5 |
| 19.11 | 17:46 | beklenen | PANW P BABA WMT opsiyon vs gercek tek tweet | dortlu | 6aff0bd8b3b455c2f5783672 |
| 19.11 | 18:12 | makro | İşsizlik 203 bin; Philly Fed 6;3 | uclu | 6aff11e15187bf7d546ee6ae |
| 19.11 | 18:36 | haber | Çip toparlanması MU AVGO AMD | editoryal | 6aff178ccfb6abb6944d8e38 |
| 19.11 | 19:01 | cagri | WMT Sparky sepet +40% | spotlight | 6aff1d60f996b44ffbc4e7b1 |
| 19.11 | 19:12 | cagri | WMT tüketici istikrarlı ve dayanıklı | zaman | 6aff1d6270751782c0cfa052 |
| 19.11 | 20:31 | son-dakika | Gün ortası sert dönüş; Nasdaq -1;5 Dow -2 | isi | 6aff328195650eb4b8b88df2 |
| 19.11 | 21:06 | 13f | Point72 MSFT NVDA artırdı AMD TSMC azalttı | uclu | 6aff3ab7ed6071e709915556 |
| 19.11 | 21:46 | son-dakika | AMD Hunterbrook açığa satış -9 | spotlight | 6aff440fd9396e656819f13a |
| 19.11 | 21:58 | son-dakika | Anthropic halka arz + 2;5 Tr silinen değer (ENES İSTEĞİ) | editoryal | 6aff46e0182c0ff41176a9c5 |
| 19.11 | 22:16 | son-dakika | AMD Hunterbrook yanıtı (takip) | zaman | 6aff4af8ff0f4be226851b65 |
| 19.11 | 23:06 | 13f | Renaissance NVDA -99;7 MU en büyük | uclu | 6aff56b7afe79203125be4a2 |
| 19.11 | 23:29 | teknik | NDX günlük teknik analiz (ENES İSTEĞİ; Enes'in TradingView görüntüleri) | ekran | 6aff5c31c233673006c1a233 |
| 20.11 | 00:06 | beklenti | KEYS bilanço beklentisi | beklenti | 6aff64ecd606779a4df98c43 |
| 20.11 | 00:12 | kapanis | Kapanış: Nasdaq -2;25 S&P -1;97 Dow -2;19 | isi | 6aff6634373c7db3cb537ce2 |
| 20.11 | 00:19 | bilanco-rakam | KEYS Ekim 2026 çeyreği rakam | dortlu | 6aff67ef8ba5b0cdc4ae936a |
| 20.11 | 00:26 | egitici | Açığa satış raporu nasıl işler (AMD örneği) | zaman | 6aff69838ec824f4cec13bb3 |
| 20.11 | 00:51 | 13f | Whale Rock ALAB çıkış SITM artış | uclu | 6aff6f678ec824f4cec357fe |
| 20.11 | 01:26 | gorus | Cuma için dört not | editoryal | 6aff778986abad2170218d8a |
| 20.11 | 12:30 | gorus | ENES İSTEĞİ: iyi bilançolar ve token düşüşüne rağmen düşüş gerçekçi değil (12:30 zamanlandı) | dortlu | 6affdc97738ce4635f8ce777 |
| 20.11 | 11:04 | baslik | Günün başlıkları 20.11; vadeliler ekside; Michigan 18:00; AMD ve Keysight takibi | terminal | 6afffef10f5eda1a57d1e806 |
| 20.11 | 11:19 | portfoy | NBIS Eylül 2026 çeyreği; gelir +%571; gecikme zamanlama sorunu | uclu | 6b0002857b0a126cebbce091 |
| 20.11 | 11:41 | portfoy | AVGO YZ çip geliri 16;7 Mr +%221; Ekim rehberi 21;7 Mr +%236; 115 Mr tedarik | ilerleme | 6b0007c97b0a126cebbec84e |
| 20.11 | 12:06 | haber | ABD uzaktan erişim çip kuralı 19.11 yürürlükte; Çin; lisans | zaman | 6b000da4738ce4635f9fb12d |
| 20.11 | 12:12 | enes-teknik | NBIS teknik; kademeler 88-93 / 82-85 / 74-78; dönüş 110 üstü | enes-grafik | 6b000f177b0a126cebc1ffdf |
| 20.11 | 12:46 | haber | ORCL S&P BBB-; borçla finansman; YZ talebiyle karıştırma | spotlight | 6b0017073409fcd68aa03586 |
| 20.11 | 13:11 | haber | vadeliler; YZ satışı Asya ve Avrupa'ya yayıldı | terminal | 6b001ce6e0dc26301cccee1f |
| 20.11 | 13:33 | fikir | VIX 28.44; korku endeksi | uclu | 6b0021e439116a845dcbedd3 |
| 20.11 | 13:56 | haber | Asya çip satışı; Tayvan 1991'den beri en kötü hafta | ilerleme | 6b00276539116a845dcdfe6d |
| 20.11 | 14:18 | makro | Michigan tüketici güveni 18:00 beklentisi | spotlight | 6b002c870c6d6b9052805c0a |
| 20.11 | 14:42 | haber | ASML %6 düşüş; zirvenin %30 altı | once_sonra | 6b00320e0c6d6b9052827be3 |
| 20.11 | 15:12 | SONDAKIKA | On piyasa cip satisi AMD MU MRVL | terminal | 6b00392644831c50e4c0c8d7 |
| 20.11 | 15:37 | BAGLAM-GORUS | RKLB siparis defteri Neutron gecikmesi | uclu | 6b003ef6fc5b97f0f8056789 |
| 20.11 | 16:00 | BAGLAM-GORUS | LITE MRVL birlesme farki | spotlight | 6b00447144831c50e4c5dde2 |
| 20.11 | 16:25 | VADELI | Vadeli ayrisma Nasdaq Dow opsiyon vade gunu | isi | 6b004a37234b6bb6ee9a983a |
| 20.11 | 16:51 | BAGLAM-GORUS | VRT temettu artisi yuzde 60 | grafik2 | 6b00504cfc5b97f0f80d6ee4 |
| 20.11 | 17:15 | TAKIP | KEYS takip prim yok | uclu | 6b0055ef5d9549971cb061f6 |
| 20.11 | 17:38 | SONDAKIKA | ABD acilis cip satisi DOCN NBIS DELL AXON | terminal | 6b005b61fc5b97f0f8135743 |
| 20.11 | 18:04 | ENES-ISTEGI | Michigan kasim nihai enflasyon beklentisi 3.7 | dortlu | 6b0061865d9549971cb5d47b |
| 20.11 | 18:26 | BAGLAM-GORUS | Faiz dustu cip satisi hizlandi SOX | isi | 6b0066a7234b6bb6eea902c0 |
| 20.11 | 18:49 | BAGLAM-GORUS | CBRS satista artida | spotlight | 6b006c112473d9c25a98c4c2 |
| 20.11 | 19:14 | BAGLAM-GORUS | SOX 5 Kasim kapanisinin altinda | grafik2 | 6b0071cdfcc25b8656450926 |
| 20.11 | 19:36 | BAGLAM-GORUS | GOOGL harcama serbest nakit akisi | uclu | 6b0076fc825e970fbdfa8276 |
| 20.11 | 19:59 | EGITICI | Neocloud nedir NBIS IREN CRWV satisi | dortlu | 6b007c6f8323fb252aa64612 |
| 20.11 | 20:21 | BAGLAM-GORUS | Uzay hisseleri satisi ASTS yillik dip | isi | 6b0081a96f199ec35b6961be |
| 20.11 | 20:47 | ICERIDEN-ALIM | TSMC yonetici alimlari | spotlight | 6b00879444c36191134c4278 |
| 20.11 | 21:10 | BAGLAM-GORUS | BofA anketi cipler en kalabalik islem | grafik2 | 6b008d1d63ab5fef6744ed10 |
| 20.11 | 21:26 | ENES-HABER | Trump yurt disi veri merkezi vergi tehdidi | sondakika | 6b0090cd44c3619113508860 |
| 20.11 | 21:34 | BAGLAM-GORUS | DOCN haber yok rakamlar guclu | uclu | 6b0092a4d425f1473a04a15a |
| 20.11 | 21:59 | EGITICI | ARR nedir | poster | 6b0098a444c3619113537103 |
| 20.11 | 22:24 | SONDAKIKA | S&P 500 ve Dow duzeltme bolgesinde | dortlu | 6b009e50861298c9b1483458 |
| 20.11 | 22:47 | BAGLAM-GORUS | Sektor rotasyonu defansif | isi | 6b00a3c6d425f1473a0c2779 |
| 20.11 | 23:10 | BAGLAM-GORUS | Altin Eylul 2025 dibi | spotlight | 6b00a9296f199ec35b7b8b50 |
| 20.11 | 23:33 | EGITICI | Fed Aralik artirimi ve buyume hisseleri | uclu | 6b00ae6dd425f1473a10b634 |
| 21.11 | 00:12 | TAKIP | Cuma kapanisi ve dort not takibi | dortlu | 6b00b7da5e993799d82c10ff |
| 21.11 | 00:37 | BAGLAM-GORUS | NVDA dusus ve temel | grafik2 | 6b00bd7dd9cbb430a1fac617 |
| 21.11 | 01:01 | BAGLAM-GORUS | Bitcoin 60 bin alti ETF cikisi | spotlight | 6b00c3225102766245d70fd9 |
| 21.11 | 10:56 | HAFTALIK-OZET | 16-20 Kasim haftalik ozet | isi | 6b014ec29ffbc8503c09f1ed |
| 21.11 | 11:16 | SONDAKIKA | NVDA SEC muhasebe sorusturmasi | sondakika | 6b015363d9cbb430a12e35c6 |
| 21.11 | 12:21 | PORTFOY | NBIS Israil 134 MW Mega DC | uclu | 6b0162a8d9cbb430a13488dd |
| 21.11 | 13:27 | SEKTOR | Haftalik sektor isi haritasi | dortlu | 6b0171f751027662451562d1 |
| 21.11 | 14:16 | EGITICI | Ayi piyasasi nedir | editoryal | 6b017da48bd84d5966e10749 |
| 21.11 | 15:21 | PORTFOY | VRT ATLAS Lab Nvidia | spotlight | 6b018ce4d5eabfb8cc2c016d |
| 21.11 | 17:16 | EGITICI | Neocloud nedir | uclu | 6b01a7be8bd84d5966f3eed3 |
| 23.11 | 20:18 | PORTFOY | NBIS neocloud korunan kazanc | grafik2 | 6b04754b827feee79c10a65f |
| 23.11 | 20:37 | PORTFOY | AVGO Kuo TPU kesintisi | dortlu | 6b0479bcff0a846b7faca7a9 |
| 23.11 | 20:38 | BAGLAM-GORUS | NVDA skandal oncesinin %11 alti | cizgi | 6b047a1c4129dae94380575d |
| 23.11 | 21:01 | BAGLAM-GORUS | MU Citi bellek talebi | spotlight | 6b047f690191a6ffcb813076 |
| 23.11 | 21:02 | EGITICI | Bellek DRAM ve NAND ayrimi | uclu | 6b047fc00720ccb673fd4e36 |
| 23.11 | 21:27 | BAGLAM-GORUS | CRWD ZS birlesme farki | editoryal | 6b04858376f8581f138ec5a1 |
| 23.11 | 21:28 | FIKIR | VRT siparis verisi gizli | terminal | 6b0485c783d02a1633847b27 |
| 23.11 | 21:52 | DERIN-ANALIZ | Dort endiseden biri kalkti | dortlu | 6b048b686dffe25404d712e6 |
| 23.11 | 22:05 | MAKRO | Sukran haftasi takvimi PCE | takvim | 6b048ba676f8581f13912df8 |
| 23.11 | 22:17 | BAGLAM-GORUS | VIX vade yapisi | grafik2 | 6b04915b0720ccb673056450 |
| 23.11 | 22:30 | BAGLAM-GORUS | DELL bilanco oncesi | editoryal | 6b0491940191a6ffcb8993ad |
| 23.11 | 22:43 | BAGLAM-GORUS | HPE bilanco oncesi | uclu | 6b04976f768ab8d8e40cc694 |
| 23.11 | 22:57 | BAGLAM-GORUS | ortuk korelasyon COR1M | once_sonra | 6b0497a90720ccb67308310a |
| 23.11 | 23:10 | BAGLAM-GORUS | SKEW cokus korumasi | cizgi | 6b049da1d73c10ed4ca51708 |
| 23.11 | 23:22 | BAGLAM-GORUS | esit agirlik genislik | siralama | 6b049df1c890e50e66ac0c41 |
| 23.11 | 23:35 | PORTFOY | SITM satin alinan buyume | spotlight | 6b04a3745678330d31d88a1f |
| 23.11 | 23:47 | PORTFOY | DOCN YZ payi ve nakit | halka | 6b04a3b6f80929239f3f3bea |
| 24.11 | 00:09 | BAGLAM-GORUS | kapanis rekora uzaklik | terminal | 6b04ab7407fee37ee600eee5 |
| 24.11 | 11:04 | KEYLEVELS | gunun basliklari DELL PCE | takvim | 6b05450eb34a1444db97adfd |
| 24.11 | 11:17 | BILANCO-ANALIZ | HPE Q4 sonuc takibi marj gider | uclu | 6b05480df1f0435123304e80 |
| 24.11 | 11:39 | PORTFOY | RKLB Electron fiyat gucu Neutron | once_sonra | 6b054d47e7f2021e56805e1a |
| 24.11 | 12:02 | BAGLAM-GORUS | Asya cip zincir TSMC Foxconn | siralama | 6b0552a42acbde8befbc8dc1 |
| 24.11 | 12:23 | PORTFOY | CBRS beta iki kat satis carpani | spotlight | 6b055794428d2546b7f950a7 |
| 24.11 | 12:46 | PORTFOY | AXON rehber revizyonu Dedrone zamanlama | editoryal | 6b055d03387f16878f837677 |
| 24.11 | 13:10 | EGITICI | PCE TUFE farki Fed hedefi | uclu | 6b0562768feb7d2bb85ea89f |
| 24.11 | 13:31 | BAGLAM-GORUS | NVDA not degisikligi F/K tersine hesap | siralama | 6b056796b2a80eb8e45d2744 |
| 24.11 | 14:22 | GERI-ALIM | HPE geri alim 5 Mr FCF %75 | halka | 6b05738c81eea170c9176e00 |
| 24.11 | 14:36 | SONDAKIKA | vadeliler geri cekilme NQ -2 | once_sonra | 6b0576b498255767f867683d |
| 24.11 | 15:00 | BILANCO-ANALIZ | HPE islem oncesi -10 marj | terminal | 6b057c3fbc0aa0829453a3b5 |
| 24.11 | 16:42 | BAGLAM-GORUS | DELL bilanco oncesi HPE kiyasi | dortlu | 6b05944ba9e62b5051a850e6 |
| 24.11 | 17:37 | BAGLAM-GORUS | ABD acilis sunucu bellek satis | siralama | 6b05a1086bb1e3ab6a388fc4 |
| 24.11 | 17:42 | BILANCO-ANALIZ | HPE nakit akis tedarikci borcu | uclu | 6b05a25bc592f5a905e46428 |
| 24.11 | 18:15 | MAKRO-YORUM | Tüketici güveni Kasım 103,3 | once_sonra | 6b05a9f1e86dabb983d85d4a |
| 24.11 | 18:32 | BAGLAM-GORUS | Çip rallisi geri verme oranı | dortlu | 6b05adf387ca84f8fe769833 |
| 24.11 | 18:54 | BILANCO-ANALIZ | ADI rehber: gelir +0,6 HBK -5,9 | editoryal | 6b05b334dac0a74131de0d38 |
| 24.11 | 19:17 | EGITICI | Neocloud neden sert oynar | siralama | 6b05b88684a6c936472b8ada |
| 24.11 | 19:38 | BAGLAM-GORUS | SOX-IGV korelasyon koptu, güvenlik artıda | terminal | 6b05bd9e78f91355c97a0071 |
| 24.11 | 19:59 | BAGLAM-GORUS | Güç zinciri: ekipman vs elektrik satıcısı (VRT portföy) | halka | 6b05c2882aa1a78e43941fc2 |
| 24.11 | 20:21 | PORTFOY | RKLB Neutron fiyat 55->70 | once_sonra | 6b05c7919694e6b567041954 |
| 24.11 | 20:44 | PORTFOY | [A:iddia] SITM 3'e 1 bölünme | spotlight | 6b05ccdabd6e90a3281cf52d |
| 24.11 | 21:07 | MAKRO-YORUM | [A:normal] Fed kararı Kasım TÜFE'den 1 gün önce, PCE eşiği | takvim | 6b05d2749694e6b567097272 |
| 24.11 | 21:29 | ANALIST | [A:iddia] PLTR analist hedefleri 80-265, 3,3 kat | siralama | 6b05d79220f9e770f0855c16 |
| 24.11 | 21:53 | BILANCO-BEKLENTI | [A:normal] SNOW 2 Aralık önizleme: RPO kırılma noktası | uclu | 6b05dd3720f9e770f087da78 |
| 24.11 | 22:16 | TAKVIM | [A:iddia] Yarın ne var: hafta tek seansa sıkıştı | dortlu | 6b05e2912db23f32428c5d3a |
| 24.11 | 23:01 | BILANCO-BEKLENTI | [A:normal] DELL bilanço beklentisi + brüt marj %20 eşiği | terminal | 6b05ecfe53ba61949d6178ac |
| 25.11 | 00:15 | BILANCO-RAKAM | [A:muaf] DELL 3Ç rakam: 54,9 / 9,45 / defter 132,3 | uclu | 6b05fe72bbd94e83696f6f13 |
| 25.11 | 00:17 | BILANCO-ANALIZ | [A:normal] DELL analiz: defter kâra dönüyor, marj sabit, 4Ç HBK -%11 | once_sonra | 6b05fec99dd8377af120a802 |
| 25.11 | 00:31 | KAPANIS | [A:iddia] [ALINTI-kendi] NDX sonuç takibi: rallinin %31'i geri verildi, %50 eşiği aşılmadı | halka | 6b060233bbd94e83697121fe |
| 25.11 | 11:02 | KEYLEVELS | [A:normal] Günün başlıkları: NQ -2 vadeli, DELL primi geri verdi, PCE 0,3=yıllık 3,7 | takvim | 6b069620c68d7845a492dc71 |
| 25.11 | 11:07 | HABER | [A:iddia] BIS kara liste 7 şirket MY/SG/TH, Megaspeed; ABD merkezli muafiyet -> kanal temizliği | editoryal | 6b069756d8874a038c0514ea |
| 25.11 | 11:20 | GUNUN-OLAYLARI | [A:normal] Bugünün önemli olayları (TSİ) listesi 25.11 — kural 83 ilk | terminal | 6b069874b6204bca46dbff6c |
| 25.11 | 11:43 | BILANCO-CAGRI | [A:iddia] DELL görüşme: her sipariş 4 kontrol (sermaye, müşteri kalitesi, ihracat, arazi/elektrik), açık 2027'de büyüyor | sutun | 6b069fa2b6204bca46deda4e |
| 25.11 | 12:07 | BAGLAM-GORUS | [A:iddia] NVDA dosya: zirveden −35 vs NDX −16, 1 yıl −14 vs +4, DELL defter 51->132 | dosya | 6b06a53222dfb7833a979788 |
| 25.11 | 12:54 | BAGLAM-GORUS | [A:normal] YZ çipleri 52 hafta: MU +180/−48, AMD ×2/−36, ANET −22 TSM −28, NBIS/CRWV −69/70; CRWV tahvil %14-16 | aralik | 6b06b03f6212ba833cb06fb0 |
| 25.11 | 13:17 | MAKRO | [A:iddia] Yeni gümrük vergileri: Çin, AB + 14 ekonomi, USTR aşırı kapasite; PCE 0,3 ile zincir | haber_dosya | 6b06b5a6f7449faeec45287e |
| 25.11 | 14:04 | HABER | [A:normal] Gümrük listesi 16 ekonomi: Tayvan, Kore, Japonya, Malezya, Singapur; tavan %15/%19, Tayvan tavansız -> TSM riski | haber_dosya | 6b06c0a64f2f059ad9a4f8a6 |
| 25.11 | 14:36 | BILANCO-RAKAM | [A:muaf] GDS 3Ç26 rakam: gelir 3,18 Mr yuan +10,1, net marj 0,9, alan +25,5, capex 8,5 | bilanco_dosya | 6b06c849e3ac2fcff79fbc05 |
| 25.11 | 15:22 | BILANCO-ANALIZ | [A:normal] GDS analiz: FAVÖK +2,8, doluluk 74,4->81,2, marj 46,5->43,4, capex 8,5, net borç/FAVÖK ~5,3 | sutun | 6b06d2fca98b4d223dac3eba |
| 25.11 | 16:47 | MAKRO | [A:iddia] [TEST-SONUC] PCE: çekirdek 3,3 yıllık / 0,3 aylık, GDP 4,3; eşik tuttu, 50 bp sorusu | haber_dosya | 6b06e6ec3b100906e7587db1 |
| 25.11 | 17:37 | BAGLAM-GORUS | [A:normal] Açılış: NDX ~−4, SPX ~−2,7; MU −11, CRWV/NBIS −10, NVDA −8,5; en az HPE/AXON/CRWD | isi | 6b06f2c1232e485be0cd5b9a |
| 25.11 | 18:00 | MAKRO | [A:iddia] Hisse düşerken tahvil yükseldi: 10Y 4,90->4,82, ZT/ZQ yukarı, NDX −3 (açılış −4); 17:37 açıklaması düzeltildi | haber_dosya | 6b06f80ecabcf2e3e37bd992 |
| 25.11 | 18:22 | PORTFOY | [A:normal] CRWV/NBIS tahvil baskısı: kredi primi rekor, 2031 tahvil %16 üstü; eşik %16 | dosya | 6b06fd325fe597980b65b3cf |
| 25.11 | 18:52 | HABER | [A:iddia] Tayvan USTR resmi öneri en çok %15 (anlaşma tavanı); TSM −%7 gümrükten değil çip satışından | haber_dosya | 6b070424304332fdc8e12c9b |
| 25.11 | 20:02 | EGITICI | [A:normal] Kredi temerrüt swabı (CDS) nedir; CRWV 1.155 / ORCL 298 / NVDA 139 bp (6.11) | siralama | 6b07125a95a0fa08d474a277 |
| 25.11 | 20:14 | ENES-HABER | [A:iddia] FCC SpaceX Starmind 1 milyon uydu izni; Starlink Gen2 15.000; ilk etki fırlatma talebi/Starship | haber_dosya | 6b0713abdb153417ca0fe4e1 |
| 25.11 | 20:57 | BAGLAM-GORUS | [A:normal] Nasdaq 100 ayı çizgisine (24.980) dokunup döndü; VIX gün içi zirveden ~5 puan geri; çizgi %3 yukarıda | cizgi_pro | 6b07218d52de4830633e1512 |
| 25.11 | 22:10 | MAKRO | [A:iddia] Fed Bej Kitap: 8/12 bölge büyüme, girdi maliyeti > satış fiyatı, ücret hızlandı; Aralık artırımı değişmez, baskı marjlarda; 13 Ocak sonraki Bej Kitap | haber_dosya | 6b07329c636c52154b99315f |
| 26.11 | 00:16 | SONUC | [A:iddia] TEST-AYRISMA-2511 sonuç takibi: NVDA 149,30>125,53, AMD 406,03<424,39, AVGO 300,86<304,41 tuttu | haber_dosya | 6b075026b96dd8d35161b98e |
| 26.11 | 10:40 | KORKU | [A:normal] Korku-Açgözlülük 17,4 aşırı korku (kural 90 ilk) | cizgi_pro | 6b07c6f4b96dd8d351914536 |
| 26.11 | 11:19 | HABER | [A:iddia] Kioxia +%12,6 yalnız Nvidia değil; 2,21 trilyon yen iç temettü + 144 SSD deneme; ikinci etki SanDisk/Micron | cizgi_olay | 6b07eb84aca8612480906cfc |
| 26.11 | 11:46 | HABER | [A:normal] SK Hynix Kore toparlanması akşama taşınmadı | dosya | 6b07f1fb63939e1d00875fa7 |
| 26.11 | 12:23 | HABER | [A:iddia] SpaceX yörünge veri merkezi FCC onayı 10 ayda | siralama | 6b07fa6c17fc84b971bcaa01 |
| 26.11 | 12:52 | HABER | [A:normal] Nvidia kredi notu S&P izleme / Moody's teyit | cizgi_pro | 6b08013510c0f7816e972e48 |
| 26.11 | 13:28 | HABER | [A:iddia] Asya veri merkezi kredileri ABD çip lisansına takıldı | bilanco | 6b0809d2a35d913b496dbd04 |
| 26.11 | 13:54 | HABER | [A:normal] Nikkei yükselişinin yarısı Advantest'ten, Topix +%0,1 | cizgi_olay | 6b080ff5b56cc066e5beaa97 |
| 26.11 | 14:27 | HABER | [A:iddia] OpenAI Private Inference / gizli hesaplama tedarikçileri | kucuk_coklu | 6b08178c3d35a6c490d28670 |
| 26.11 | 14:56 | PORTFOY | [A:normal] RKLB fiyatlama gücü / SpaceX yörünge veri merkezi ikinci derece etkisi | dosya | 6b081e6096d200044e41cfe6 |
| 26.11 | 15:40 | DERIN-ANALIZ | [A:iddia] AÇIKLAYICI 1/5: Neocloud iş modeli ve Nebius peşin ödeme | bilanco | 6b0824615b429f9be00a73ae |
| 26.11 | 16:20 | VERI-KUYRUK | [A:normal] Kuyruk riski: VVIX 115 (%87), SKEW ortalama | cizgi_pro | 6b08306eb56b3bb7f9fd0f73 |
| 26.11 | 16:57 | DERIN-ANALIZ | [A:iddia] AÇIKLAYICI 2/5: XPU / özel yapay zekâ çipi, AVGO | sutun | 6b083ac080ee2e8b6680cb1f |
| 26.11 | 17:50 | PORTFOY | [A:normal] AÇIKLAYICI 3/5: sıvı soğutma neden zorunlu, VRT ön ödemeler | dosya | 6b084713a9607f755582e90f |
| 26.11 | 19:21 | TARIHSEL | [A:iddia] TARİHSEL (kural 96) ilk: VIX 25 üstü -> Nasdaq 100 6 ay | egim | 6b085ca54e32cfdd23069e88 |
| 26.11 | 20:12 | PORTFOY | [A:normal] AÇIKLAYICI 4/5: zamanlama çipi, SITM | bilanco | 6b08688c3accdac92ce4d4f2 |
| 26.11 | 21:03 | HABER | SNOW tüketim bazlı gelir 2 Aralık öncesi | sutun | 6b087486ce64081689def217 |
| 26.11 | 21:47 | EGITICI | Ay sonu yeniden dengeleme (emeklilik fonu) | siralama | 6b087ed3ce64081689e3c950 |
| 26.11 | 22:24 | HABER | [A:iddia] MDB 1 Aralık bilançosu öncesi Atlas eşiği | cizgi_olay | 6b08876b3accdac92cf3b9ab |
| 26.11 | 23:13 | HABER | Kara Cuma çevrim içi harcama beklentisi (Adobe) | bilanco | 6b0892ecc81617797dddc881 |
| 27.11 | 00:04 | HABER | [A:iddia] Tokyo enflasyonu bu gece, yen taşıma işlemi riski | cizgi_pro | 6b089ed5ce64081689f2aad0 |
| 27.11 | 11:01 | VADELI | [A:normal] GÜNÜN BAŞLIKLARI: vadeliler +, Tokyo TÜFE beklenti altı, yarım gün | siralama | 6b0938e71fd46e62e7253a5e |
| 27.11 | 11:42 | AAII | [A:iddia] AAII ayı %45, nötr %18'e indi | aaii | 6b094271049983dcfba1ed3d |
| 27.11 | 12:22 | HABER | [A:normal] AÇIKLAYICI 1/5: jeopolitik risk primi  Brent 92 / ekim 117 | cizgi_olay | 6b094bd9062ed764a8ffd7b7 |
| 27.11 | 13:05 | HABER | [A:iddia] AÇIKLAYICI 2/5: ihracat kısıtlaması / Çin payı  ASML | dosya | 6b0955d1776ce21276079a57 |
| 27.11 | 13:55 | HABER | [A:normal] Gelecek hafta bilanço takvimi: MRVL CRWD MDB OKTA CRDO / CRM SNOW ZS | bilanco | 6b0961b9658222306c05eefc |
| 27.11 | 14:40 | ICERIDEN | [A:normal] COHR yönetim kurulu üyesi Pagliuca ~50 Mn $ açık piyasa alımı | cizgi_pro | 6b096c36049983dcfbb542df |
| 27.11 | 15:25 | HABER | [A:normal] AÇIKLAYICI 3/5: özel çip (ASIC)  MRVL 1 Aralık önizleme | sutun | 6b09769f062ed764a813b168 |
| 27.11 | 16:15 | VERI-FAKTOR | [A:iddia] Faktör panosu: momentum −11 puan, eşit ağırlık +6 | siralama | 6b09825a062ed764a8197aaf |
| 27.11 | 16:51 | HABER | [A:normal] AÇIKLAYICI 4/5: kontrol düzlemi  Air Force Cloud One ihlali | bilanco | 6b098af732c212878fd46ded |
| 27.11 | 18:14 | VERI-VIX | VIX vade eğrisi 8 gündür ters, oran 1,05 (biçim: görüş) | cizgi_pro | 6b099e5b32c212878fdeac6b |
| 27.11 | 18:52 | HABER | Faiz +7 bp iken Nasdaq +%1,7: para tahvilden hisseye (biçim: kartsız) | kartsiz | 6b09a722bb117e5ba75c43de |
| 27.11 | 19:32 | HABER | AÇIKLAYICI 5/5: dikey entegrasyon  Tesla EMAG başvurusu (biçim: kartlı) | dosya | 6b09b0a832c212878fe786d8 |
| 27.11 | 20:09 | EGITICI | EĞİTİCİ: yarım gün ve ince hacim, QQQ hacim 0,5x (biçim: kartsız) | kartsiz | 6b09b932d5bf252ef53a399a |
| 27.11 | 21:14 | HABER | Nasdaq 100 haftalık +%7, dip görüşü, 26.000 teyit eşiği (biçim: görüş) | cizgi_olay | 6b09c8720dc186ddf75d6d5e |
| 27.11 | 22:05 | HABER | Çipler +%5, Nvidia geride: Çin veri merkezinde Blackwell haberi (biçim: kartsız) | kartsiz | 6b09d46802e606c3af771a00 |
| 28.11 | 10:57 | HAFTALIK-OZET | Haftalık özet: 1,5 yılın en iyi haftası, Nvidia ~%20, genişlik (biçim: kartlı, kart4 siralama) | k4_siralama | 6b0a8949fe7140cdac9d63c2 |
| 28.11 | 11:35 | KORKU | Korku endeksi 24,9, aşırı korku, 25 eşiği (biçim: kartlı, kart4 olcer) | k4_olcer | 6b0a89f4fe7140cdac9d93e7 |
| 28.11 | 12:12 | SONUC | TEST-NDX-AYI tuttu: 24.980 savunuldu, kapanış 26.726 (biçim: kartsız) | kartsiz | 6b0a8caefe7140cdac9f0d29 |
| 28.11 | 12:50 | TEKNIK | TA-STİL TSLA haftalık: düşen trend 409, kırılım henüz yok, eşik 345 (biçim: stil çizim) | stil_cizim | 6b0a9386ced9496800aa44f9 |
| 28.11 | 13:01 | VERI-GENISLIK | Nasdaq 100 genişlik %46->%52, korku hâlâ aşırı (biçim: kart4 cizgi) | k4_cizgi | 6b0a9b189caa4fb9ca97756a |
| 28.11 | 13:22 | TEMEL-FIKIR | K107 HBM 2027 200 mlr $ fiyat 2 kat, MU SKHY marj (biçim: kartsız görüş) | kartsiz | 6b0aab62d2df6f06d3a2f889 |
| 28.11 | 15:11 | SEKTOR | Sektör haftalık: malzeme 7,9 teknoloji 7,5 önde, savunma 2,5 geride (biçim: kart4 isi) | k4_isi | 6b0ac50b0f9559e0ce0dac83 |
| 28.11 | 15:35 | K111-LISTE | K111 YZ hisseleri 52H zirveden düşüş listesi Kara Cuma (biçim: kart4 siralama, tartışma görüşü) | k4_siralama | 6b0aca77b8ec87c6cec48b55 |

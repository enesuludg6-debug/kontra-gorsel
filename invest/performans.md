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

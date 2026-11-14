# KONTRA OTOMATİK HABER DÖNGÜSÜ (Enes, 12.11.2026 — son güncelleme 11:44)

## Akış (her tweet için ayrı, TOPLU HAZIRLIK YOK)
1. Uyanış gelince: O ANDA araştır. Son dakika futbol haberleri (Türk kulüpleri, milli takım, Türk izleyiciyi ilgilendiren büyük Avrupa haberleri). En yeni + en önemli haberi seç.
   - O an yeni son dakika yoksa: son birkaç saatte çıkmış ama henüz paylaşmadığımız en önemli son dakikayı seç (LOG'a bak, tekrar etme).
2. Enes'e SendUserMessage + PushNotification: kısa haber özeti + "📸 Fotoğraf at: <ideal kare>".
3. BEKLEYEN'e yaz. Fotoğraf gelince HEMEN: görseli kontra_stil diliyle habere özel çiz → /home/claude/kontra-gorsel/g/ → git push → raw URL ile Buffer create_post mode=shareNow (kanal 6af5723862b70b94b0047aa5) → LOG'a taşı. Paylaşmadan hemen önce haberde yeni gelişme var mı kısa kontrol et.
4. Bir sonraki uyanışı send_later ile RASTGELE kur: python random ile 5-30 dk arası farklı değer; ~%15 ihtimalle 1-2 dk (art arda iki tweet hissi). Sabit aralık YOK.

## ZİNCİR NOTU
- 12:02'deki uyanış (trig_01Vk2qf43hsXdMUjndYTtpbq) silinemedi. 12:17'de trig_01JVMhYtRaqrTAKpVGNMtFmJ kurulu. 12:02 uyanışı İŞLENDİ (Lukaku istendi, yeni send_later kurulmadı) (zincir 12:17'den devam eder). Tek zincir kuralı: her uyanış sadece kendi sonrakini kurar.

## Kurallar
- Fotoğraf yoksa paylaşma. Bekleyen istek 2'yi geçerse yeni istek atma; bekleyenleri hatırlat (eski istek bayatladıysa iptal et, yenisini iste).
- Tek kaynaklı / iddia → İDDİA etiketi. Doğrulanamayan haber paylaşılmaz.
- Hedef: 12.11 19:30'a kadar 30 tweet. Limitler: Buffer API 1000 istek/30 gün, X 100/24 saat.
- Zamana bağlı haber (maç günü vb.) kendi saatinde.
- Enes "dur" derse döngüyü durdur.

## HESAP GÜVENLİĞİ / ÇEŞİTLİLİK (Enes 11:45 — çok önemli)
- EMOJİ YOK (Enes 11:46): tweet metinlerinde hiç emoji kullanma.
- Kalıp cümle YOK. Her tweetin açılışı farklı: bazen direkt alıntı, bazen soru, bazen rakamla, bazen tek kelime başlık, bazen düz cümle. "🚨" ile başlamayı alışkanlık yapma; emoji sayısı/yeri değişsin, bazen hiç emoji yok.
- Uzunluk değişsin: bazen 1-2 satır, bazen 4-6 satır. Madde işareti yapısı her seferinde aynı olmasın.
- Kapanış değişsin: kaynak bazen "📰 X", bazen "(X)", bazen cümle içinde "X'in haberine göre". Hashtag nadiren ve her seferinde farklı (çoğu tweette hiç yok).
- Son 5 tweetin açılış/kapanışını LOG'a kısaca not et, aynısını tekrarlama.
- Linkli tweet atma (X link içerenleri spam sayabiliyor + API ücreti). Mention / etiket (@) yok, toplu yanıt yok, beğeni/takip otomasyonu yok.
- Aynı haberi iki kez atma; aynı oyuncuyu art arda tweetlerde kullanma.
- Görsel düzeni de her seferinde değiştir (art arda aynı şablon yok).
- Günlük toplam makul: hedef 30, asla 50'yi geçme. Gece 01:00-08:00 arası paylaşım yok.
- Telif: sadece Enes'in fotoğrafı; alıntılar kısa, haber metni kopyalanmaz, kendi cümlelerimizle.
- Buffer hata verirse (rate limit / X uyarısı) DUR ve Enes'e bildir, tekrar deneme döngüsüne girme.

## Ayarlar
- Buffer org: 6af5719777bce44fa736607b · kanal KONTRA_11: 6af5723862b70b94b0047aa5
- Görsel repo: /home/claude/kontra-gorsel (enesuludg6-debug/kontra-gorsel, main) · raw: https://raw.githubusercontent.com/enesuludg6-debug/kontra-gorsel/main/g/<dosya>
- Stil: /home/claude/font/kontra_stil.py · eski düzen örnekleri: /home/claude/work/*.py

## FOTO KURALI (19:24, kalıcı)
- Enes'in gönderdiği HER oyuncu/kişi fotoğrafı hemen /home/claude/kontra-foto/foto/<kisi_kulup>.jpg olarak kaydedilir, index.json güncellenir.
- Haberin kişisiyle birebir eşleşen foto varsa MUTLAKA fotolu görsel; yoksa yazılı kart ve Enes'e 'arşivde X fotoğrafı yok' notu.
- Ekran görüntüleri arşive girmez.

## ENES TALİMATI 2 (17:53) — GEÇERLİ
- 19:30'a kadar SORMADAN haber bul ve OTOMATİK at. Aralık 3-17 dk rastgele (python random.randint(3,17)).
- Foto: önce foto/ arşivi (/home/claude/kontra-foto/foto/) — sadece haberin oyuncusu/kişisiyle birebir eşleşiyorsa. Eşleşme yoksa FOTOĞRAFSIZ tipografik kart (work/yazikart.py). Gerçek kişilerin yapay zeka görseli ÜRETME (Canva generate-image dahil).
- Aynı kuralllar: emoji yok, kalıp cümle yok, İDDİA etiketi, kaynak, aynı haber/oyuncu art arda yok.
- 19:30 sonrası yeni send_later kurma. Maç tweetleri Enes'te.
- (19:09) Enes: tur ATLAMA. Taze doğrulanmış haber yoksa bile en yeni ve en mantıklı olanı (gerekirse İDDİA etiketiyle) at.
- (17:59) Enes: önce telifsiz kaynak (Wikimedia Commons) dene → yoksa arşiv → yoksa kendin üret (tipografik kart). Commons/upload.wikimedia.org proxy tarafından ENGELLİ; Enes Settings > Capabilities'ten izin verirse kullan (CC lisans + fotoğrafçı adı görselde ve tweette). İzin yokken etrafından dolanma.

## ENES TALİMATI (16:21, günceller 16:18) — ESKİ
- 18:00'e kadar AYNI DÜZEN: araştır, foto iste, gelince çiz ve otomatik paylaş.
- 17:45 sonrası uyanışta yeni istek atma; 18:00 sonrası yeni send_later KURMA. Döngü 18:00'de biter.
- Maç başlayınca tweetleri Enes kendisi elle atacak; maç için hiçbir şey hazırlama/atma. 19:58 kontrol uyanışı silindi.
- 30 tweet hedefi iptal; 18:30 maç günü tweeti iptal.

## BEKLEYEN (fotoğraf istendi)
- [İPTAL - ara] [11:38] Türkiye–Belçika maç günü (20:00, Sergen Yalçın ilk maç, grupta 4 maç 0 puan). Foto: Sergen Yalçın / Arda / Barış Alper. 18:30 civarı.

## YEDEK (bugün çıkmış, henüz istenmedi — yeni son dakika yoksa buradan)
- GS Noa Lang'a Genoa rakip (Sporx 10:13) İDDİA

## LOG (paylaşılan) — format: saat | haber | açılış tipi | kapanış tipi | görsel düzeni
- 11.11 Zubimendi, Yarmolyuk, Kislyak, Cibara zemin (elle)
- 12.11 11:47 | #1 Osimhen 'kronik' (Cibara) | açılış: doğrudan alıntı | kapanış: 'Fanatik, Karar' düz | görsel: soyledi_duzeltti (tam foto + dev KRONİK? + 2 sütun) | Buffer id 6af57d1d15999d2da120a9b1
- 12.11 12:05 | #2 Lukaku Türkiye maçında yok | açılış: düz kısa hüküm cümlesi | kapanış: parantez '(Sabah, Takvim)' | görsel: duoton_uclu (Belçika duoton + dev düz başlık + 3 hücre) | Buffer id 6af5814097798e85b9f52f43
- 12.11 12:21 | #3 Rashica BJK ayrılık (Takvim) İDDİA | açılış: isim+hüküm cümlesi | kapanış: kaynak cümle içinde, ayrı kaynak satırı yok | görsel: cizgili_kesik (BJK pinstripe + rembg kesik + sol bilgi satırları) | Buffer id 6af58500ae66bc26867c58eb
- 12.11 12:35 | #4 Altay Celta ilk maç (Faro de Vigo) | açılış: haber cümlesi (isim+tarih) | kapanış: 'İlginç detay:' cümlesi, kaynak ortada cümle içinde | görsel: editoryal (foto üst + ortalı 2 satır) | Buffer id 6af5885cae66bc26867d9b18
- 12.11 12:41 | #5 Carrick ManU'dan gitti (Romano; Tribuna) — Enes'in seçtiği konu | açılış: rakamla tek satır | kapanış: 'Yerine en güçlü aday ...' | görsel: dev_rakam (7. HOCA) | Buffer id 6af589adbe2095778d9d273b
- 12.11 12:50 | #6 Nene FB ayrılık (Takvim) İDDİA | açılış: soru | kapanış: 'Kulüpten henüz resmi açıklama yok.' | görsel: istatistik (2 sütun) | Buffer id 6af58bd9041a9377d7ddae21
- 12.11 13:21 | #7 TS iç sahada 5/5, 26 yıl sonra (Nefes/Akşam) | açılış: kısa slogan '5'te 5' | kapanış: tarihsel kıyas cümlesi, kaynak yok | görsel: seri_serit (dev 5/5 + skor şeridi) | Buffer id 6af59321e11ce7b6b8e21dcc
- NOT: Enes kendisi haber+foto gönderirse onu öncelikle işle (araştır, doğrula, at).
- 8 | 13:39 | Pochettino ManU 8. hoca | isim listesi | "Planlanan ilk maç..." | sira_listesi (work/poch.py) | 6af5977b100f73160cc7af8a
- 9 | 14:03 | GS Ugochukwu+Bitshiabu fesih planı (TRT Spor/Fotomaç) | zıtlık cümlesi 'Yazın geldiler, ocakta...' | 'Teknik ekibin memnun olmadığı belirtiliyor.' | dakika_cubugu (work/gs_veda.py) | 6af59cfef662733b84ac2928
- 10 | 14:30 | BJK Vlahovic milli arada İstanbul'da (Posta/A Spor) | düz haber cümlesi 'X değil Y' | 'Haber Posta'nın.' | rota_iptal (work/vlahovic.py) | 6af5a33f0219d925487fffb3
- 11 | 14:57 | FB Hakan Çalhanoğlu hedefi (Fanatik) İDDİA | 'listede sürpriz isim: X' | 'Şimdilik bir iddia...' | kutu_seridi (work/hakan.py) | 6af5a9a1c6319c29c493eaf7
- 12 | 14:59 | TS Richarlison ikinci deneme (Sporx) İDDİA | olay cümlesi 'Yazın olmayan transfer ocakta masada' | 'Resmi teklif ya da anlaşma bilgisi yok.' | ikinci_deneme duoton (work/richarlison.py) | 6af5aa134926d8280f0cc560
- 13 | 15:26 | Milli: Enes Ünal santrfor + Sergen sözü (basın toplantısı) | saat-yer başlığı 'Bu akşam 20.00, İzmir.' | kadro eksikleri bilgisi | iki_ses (work/enes.py) | 6af5b062d9468bac7106266d
- NOT: 18:30 maç günü tweetinde Enes Ünal sözünü TEKRARLAMA; Sergen ilk maç / 0 puan / Gürsel Aksel'de 2de 2 açısı kullan.
- 14 | 15:55 | FB Hogsberg stoper hedefi (Fotomaç) İDDİA | rakam dizisi '20 yaş, 1.87 boy, 18M' | 'Listede Sylla'nın önüne geçtiği yazılıyor.' | profil_karti yatay foto (work/hogsberg.py) | 6af5b73e6f4d84d775f6ffd0
- NOT: Enes yanlış oyuncu fotosu gönderebiliyor; forma/kulüp haberle uyuşmazsa sormadan atma.
- [16:16] Uyanış: taze ve doğrulanabilir haber yok (Sane/Osimhen/Noa Lang/Alanyaspor eski; Oğuz Aydın FB arka arkaya olur). Bu tur istek atlandı. Enes'e tempo sorusu soruldu (30 hedefi mi, az ama hızlı mı, akşam maç odak mı), cevap bekleniyor. Aday: Oğuz Aydın'a İngiliz-İspanyol ilgisi (Türkiye Gzt 12.11) bir sonraki turda.
- 15 | 16:33 | Fatih Tekke Gaziantep FK (61saat/yerel) İDDİA | geçmiş başarı cümlesi 'Mayısta kupa kaldıran X' | 'Açıklama yapılmadı.' | egik_bant (work/tekke.py) | 6af5c03de223e10d29ce04cd
- 16 | 17:12 | CIES altyapı raporu, Süper Lig 50/50 (Fotomaç) | soru-cevap 'Hangi lig? Cevap Süper Lig.' | yorum cümlesi | sira_raporu (work/cies.py) | 6af5c94ae7d7941c3fa57883
- 17 | 17:30 | GS Kazımcan 27 dk, ayrılık planı (Sporx) İDDİA | 'X için ocak yol ayrımı olabilir' | 'Açıklama yok.' | halka_dakika (work/kazimcan.py) | 6af5cd7f1529ce0ee2510eaa
- DÖNGÜ 12.11 17:30'da tamamlandı (Enes talimatı: 18:00'e kadar). Bekleyen istek yok, zincir yok.
- 18 | 17:55 | Muslera 28 Kasım Libertadores finali sonrası emeklilik (Espectador Deportes via GZT) İDDİA | 'X için geri sayım başladı.' | 'kendisinden açıklama yok' | yazi_kart stil=orta FOTOSUZ (work/yazikart.py) | 6af5d36ddf65abceb03b7cda
- 19 | 18:02 | Crystal Palace Sage resmen gönderildi (cpfc.co.uk) RESMİ | 'Premier Ligde bugün ikinci hoca gitti.' | Thomas Frank adı | yazi_kart stil=sol mavi FOTOSUZ
- 20 | 18:20 | Uluslar Ligi akşam programı + hakem Schärer (TFF/haber siteleri) PROGRAM | 'Uzun bir futbol gecesi bizi bekliyor.' | '5. hafta bu akşam açılıyor' | yazi_kart stil=ust kırmızı FOTOSUZ
- 21 | 18:29 | Pochettino önce ABD-Haiti 2 maç, sonra United (Yahoo/Sky) ANLAŞMA | 'X, Y ye geçmeden önce Z ile işini bitirecek.' | Anfield 22 Kasım | arşiv foto pochettino, editoryal varyant
- [18:44] tur atlandı: Emery yeni sözleşme henüz resmi değil (sadece 'yakın'); taze doğrulanmış haber yok.
- 22 | 18:58 | Ümit Milli - Çekya yarın Rize, U21 EURO play-off ilk maç (Sporx) MİLLİ | 'A Milli bu akşam, Ümitler yarın' | 'bilet iki maç sonunda' | yazi_kart stil=sol koyu kırmızı FOTOSUZ
- [19:09] tur atlandı: Kane uzatması 5 Kasım (eski).
- 23 | 19:11 | Emery Villa ile yeni sözleşmeye yakın (Ben Jacobs, Romano) İDDİA | 'United listesindeki diğer isim kalıyor' | 'Resmi imza yok' | yazi_kart stil=orta bordo FOTOSUZ
- 24 | 19:14 | GS Batrakov 55M madde, menajer İstanbul a gelecek (Match TV/Milli Gazete) İDDİA | 'X teki madde Y nin gündeminde' | sözleşme 2031 | yazi_kart stil=ust sarı FOTOSUZ
- 25 | 19:20 | Sage Lens e dönebilir, Lens Cahuzac ı göndermişti (Inside Croydon) İDDİA | 'X için yeni kapı eski evinde' | Fransa Kupası notu | yazi_kart stil=sol sarı-bordo FOTOSUZ
- 26 | 19:24 | ENES HABERİ: Sergen Yalçın 'ilk maç çok değerli, kazanmak istiyoruz' AÇIKLAMA | direkt alıntı | maç bilgisi | yazi_kart stil=orta kırmızı FOTOSUZ
- OTOMATİK MOD 12.11 19:30'da kapandı. Toplam 26 tweet (otomatik modda 9: #18-#26). Zincir yok.
- 27 | 21:05 | ENES HABERİ: Gaziantep FK Volkan Demirel ile büyük ölçüde anlaştı, Tekke ihtimali düştü (Ajansspor/Sporx) İDDİA | 'X te son dakika değişikliği' | puan durumu | rota_iptal (Vlahovic düzeni) + Enes fotosu volkan_demirel.jpg | NOT: #15 Tekke tweetini düzeltir
- 28 | 21:58 | ENES HABERİ: Sergen ilk maçını kaybeden Lucescu sonrası ilk hoca, TR 1-2 BEL (Fanatik/CNN Türk/T24) İSTATİSTİK | istatistik cümlesi | 'Sağlık olsun' | ilk_mac_karti (work/sergen_ilk.py), Enes posteri KIRPILDI (yazı+filigran dışarıda), duoton

## 13.11.2026 (yeni sohbet, otomatik mod 2-15 dk)
| # | Saat | Haber | Etiket | Düzen | Açılış/Kapanış | Buffer id |
|---|---|---|---|---|---|---|
| 1 | 10:52 | Osimhen iki aşamalı dönüş planı (Villa 24.11 → BJK derbisi 90 dk) | İDDİA | iki_asama (yeni) + gs_45_maske | düz haber / "Fanatik'in haberine göre. Resmi açıklama yok." | 6af6c1bfba218f3263880c4f |

> 13.11 10:59 Enes talimatı: aralık random.randint(7,14) dk, 20:00'de otomatik dur (20:00 sonrası yeni uyanış kurma). Günlük 50 sınırı Enes tarafından kaldırıldı (11:00); sınır 20:00 bitişi ve X 100/24s limiti. Foto eşleşmezse tweeti beklet, Enes'ten foto iste.

> 13.11 11:01 Enes: aralık random.randint(10,15) dk (7-14 iptal). Bitiş 20:00.
| 2 | 11:08 | Mbappé Türkiye maçı belirsiz (arka adale), Thuram/Tchouameni/Kalulu kamptan ayrıldı | AÇIKLAMA | durum_listesi (yeni) + fransa_sirt | durum cümlesi / kaynak cümle içinde (TF1) | 6af6c5915ec1c9d5be6c10f0 |
| 5 | 12:07 | Sergen: Belçika maçına 2 günlük antrenmanla çıktık | AÇIKLAMA | portre_sag (yeni) + sergen_yalcin_milli | isimle düz cümle / kaynaksız, açıklama aktarımı | 6af6d3466d858908964f0e87 |
| 4 | 11:54 | FB Marlon Gomes 20M, Emre-Arda Turan görüşmesi 25.11 | İDDİA | cerceveli_kare (yeni) + marlon_gomes_shakhtar | kaynakla açılış / "Kulüpten resmi açıklama yok." | 6af6d03df66277c9ba434c46 |
| 3 | 11:40 | A1 Grubu puan durumu: 5 maç 0 puan, son sıra kesin | İSTATİSTİK | puan_tablosu (yeni) + milli_8_uzgun (filigran blur) | rakam başlık / kaynaksız, hedef cümlesiyle kapanış | 6af6ccebac315c828ef68933 |

> 13.11 11:52 Enes: gönderdiği HER fotoğraf arşive (kontra-foto/foto + kontra-gorsel/foto + index.json) kaydedilir. Devirde güncel zip verilir.
| 6 | 12:21 | TS'de 13 farklı futbolcu skora katkı, Salah 11+5, Muçi 7 asist, 6 galibiyet 25 puan | İSTATİSTİK | dev_rakam + ts_grup_sevinc | rakam başlık / "(DHA)" | 6af6d69f562501e68e94f398 |
| 7 | 12:51 | GS radarında Mert Müldür (Takvim) | İDDİA | editoryal_pill + mert_muldur_fb | "radarında" açılış / "İddia aşamasında, taraflardan açıklama yok." | 6af6dd87b185663f9f992bdd |
| 8 | 13:05 | GS-Bruno Fernandes ayrılığı kafasına koydu (Fotomaç; maaş rakamı tek zayıf kaynak, çıkarıldı) | İDDİA | polaroid (yeni) + bruno_fernandes_manu | isimle düz haber / "Resmi bir adım yok." | 6af6e0c8df68225fc1b13d4d |
| 9 | 13:23 | Tugay: Hakan vücut dili iyi değil (Yeniçağ) | AÇIKLAMA | alinti_tam (yeni) + hakan_calhanoglu_inter_sirt | hedef cümlesi + birebir alıntı / "Yeniçağın aktardığı sözler." | 6af6e52b69e5ecee127cb8ed |
> DİKKAT: trig_01RCHRywWrWs2ACWGgg4ybNf gecikti, Tugay elle 13:23te atıldı. O uyanış gelirse Tugayı TEKRAR ATMA, normal yeni haber turu yap.

> 13.11 13:42 Enes: foto isterken KISA yaz, sadece 'X fotosunu at' (gerekirse forma notu). Uzun açıklama yok.
| 10 | 13:51 | BJK hedefi Oumar Solet (Nefes) | İDDİA | yarim_cizgili (yeni) + oumar_solet_udinese | "listede yeni isim" / "Kulüpten resmi açıklama yok." | 6af6ebc19a21933ffacbf55d |
| 11 | 14:05 | Arda frikiği Avrupa basınında (AS Beckham, Foot Mercato) + 65. dk 'Kimse yok' tepkisi | MİLLİ | manset_seridi (yeni) + milli_8_sut_euro2024 | olay cümlesi / kamera anı ile kapanış | 6af6eee766ff9797d87940ff |

> 13.11 14:18 Enes: OTOMATİK DÖNGÜ KAPANDI. Artık sadece Enes haber gönderince: tweet metni + görsel hazırla, Enes'e ver; PAYLAŞMA (Buffer'a gönderme). Enes kendisi atıyor.

> 13.11 14:19 Enes: tweetler emojisiz ama İLGİ ÇEKİCİ olacak; ilk satır kaydırmayı durdurmalı (çarpıcı rakam, zıtlık, beklenmedik detay, kısa vurucu cümle). Düz ajans dili yok.

> 13.11 15:05 Enes: OTOMATİK MOD TEKRAR AÇIK. Aralık random.randint(5,10) dk, 20:00'de dur. Arşivde ilgili foto yoksa SORMA, kendin fotoğrafsız görsel yap (yazi_kart vb.). Enes'e hazırlanan 13.11 14:17-15:03 kartları (poch_manu_2029, jackson_ekim, supercopa_istanbul, fabian_betis, van_dijk_talipler, raphinha_sakatlik, ronaldo_7_saygi, issman_real, camp_nou_300m, shomurodov_batrakov, batrakov_real, poch_tek_isim) Enes'in elinde; ATMA (tekrar riski).
| 12 | 15:06 | BJK-GS Kim Min-jae (BILD/Falk) | İDDİA | yazi_kart ust (fotoğrafsız) | zıtlık açılış / kaynakla gövde | 6af6fd53d414da1f7da2e7b1 |
| 13 | 15:20 | FB Breno Bidon gözlemci (Fotomaç) | İDDİA | yazi_kart sol (fotoğrafsız) | geçiş/zıtlık açılış / 'Resmi bir adım yok.' | 6af7006fbd1182b0d3f17042 |
| 14 | 15:32 | TS Wagner Pina Yeşil Burun kampından muaf (federasyon) | RESMİ | yazi_kart orta (fotoğrafsız) | kısa kötü haber açılışı / belirsizlik kapanışı | 6af7035a66ff9797d88162de |

> 13.11 15:35 Enes: döngü 16:15'te bitecek (20:00 iptal).

> 13.11 15:36 Enes: OTOMATİK DÖNGÜ DURDU. Mod: Enes haber gönderir → Claude metin + görsel hazırlar, gönderir; Enes kendisi atar. Buffer'a GÖNDERME.

> 13.11 15:55 YENİ DÜZEN SETİ: arac/font/pro2.py (Inter/Lora/Poppins + Anton). Fonksiyonlar: gazete (krem gazete manşeti, serif), swiss (beyaz minimal grid + 6 bilgi hücresi), sinema (letterbox + Lora italik altyazı alıntı), ticker (SON DAKİKA şeritleri), transfer_rota (nereden → nereye kulüp kartları), dergi (dergi kapağı, dev Anton + kapak satırları), capraz (çapraz bölünmüş foto/renk), veri_panel (yuvarlak avatar + 4 istatistik kutusu). Katalog: arac/pro2_katalog.jpg. Eski düzenlerle karışık kullan, art arda aynı yok.
> pro2.saha_sut eklendi: fotoğrafsız yarım saha + şut yayı + dev mesafe (uzak gol, frikik, şut haberleri).

## 16:28 MOD DEGISTI: OTOMATIK (5-14 dk)
- Enes: "otomatiğe geri dön 5-14 dk da bir". Buffer ile otomatik paylaşım yeniden aktif.
- Duran ve Doku-Oguz kartlarını Enes kendisi atmış olabilir, otomatik döngüde TEKRAR ATMA.
- Gece 01:00-08:00 arası tweet yok.
- 17:58 (manuel, Buffer 502): umit_cekya.jpg hazırlandı, Enes e gönderildi

## 13.11 18:00 DEVİR v2 — Mod: Hazırla, Enes atsın
- 18:50 (manuel): oh_hyeongyu_suudi.jpg — Oh Hyeon-gyu 46' gol, Suudi Arabistan 1-1 Güney Kore (hazırlık, maç sürüyor) | BUGÜN | saha_sut (fotoğrafsız) | açılış: Türkiye bağı (Beşiktaş)
- 18:55 (manuel): necip_uysal_uefab.jpg — Necip Uysal UEFA B kursu | RESMİ | polaroid (BJK siyah-beyaz) | yeni foto: necip_uysal_kurs.jpg
- 19:10 (manuel): ts_zenit_hazirlik.jpg — TS Zenit hazırlığı başladı (15.11 Pazar 17.00 Rusya) | RESMİ | program_karti (bordo-mavi) | foto: ts_teknik_ekip_antrenman.jpg (kişi belirsiz)
- 19:15 (manuel): bursaspor_ikili.jpg — Iheanacho 17G 3A + Lincoln 3G 6A = 29 skor katkısı | İSTATİSTİK | veri_panel (yeşil) | foto: iheanacho_bursaspor.jpg (teyit bekliyor)
- 19:15 kubo_bjk (İDDİA) Buffer
- 19:28 (manuel): exxen_uefa.jpg — UEFA kupaları 2027-28'den 4 yıl Exxen'de (Acun açıklaması, bedel iddia) | AÇIKLAMA | transfer_rota (TRT/tabii → EXXEN) | foto: acun_ilicali_exxen.jpg
- 19:45 sane_ocak (İDDİA, yazi_kart sol) Buffer

> 13.11 19:45 Enes: otomatik atan diğer sohbeti durdurdu. Bu sohbet devam ediyor, mod: Hazırla, Enes atsın (Buffer'a gönderme).

## 20:02 MOD DEGISTI: OTOMATIK (5-14 dk) — Enes: "sen otomatik at, arşivde alakalı foto varsa kullan yoksa foto iste"
- Foto zip'i geldi: 53 foto, repodakiyle aynı (yeni foto yok).
- 20:02 AUTO: exxen_uefa.jpg Buffer shareNow (6af742ab4d5a2b44be9e69ef)
- 20:04 Enes kuralı: alakalı foto yoksa fotosuz ATMA, Enes'ten foto iste; Enes'in attığı her fotoyu arşive kaydet. Bekleyenler: arac/bekleyen.md
- NOT: Eski send_later (trig_01BsCus..., 20:11) silinemedi (izin reddi). 20:11 firingi yeni kuralla çalıştırılır; 20:12 firingi (trig_01YAaP7...) MÜKERRER: son 5 dk içinde tweet atıldıysa atma ve yeni send_later KURMA (tek döngü kalsın).
- 20:10 AUTO: ake_soleus.jpg — FB resmi: Ake rehab sırasında soleus yaralanması | RESMİ | ticker (lacivert, SAKATLIK) | foto: nathan_ake_fb.jpg (Enes)
- 20:20 tur: fotolu taze haber bulunamadı (Kenan dönüş 12:59'da, Bruno/Batrakov/Osimhen bugün atıldı). Ümit-Çekya sonucu beklemeye alındı, Enes'ten Ümit Milli fotosu istendi. Sonraki tur 20:55.
- 20:23 AUTO: fransa_turkiye_hakem.jpg — Fransa-Türkiye hakemi Chris Kavanagh (UEFA/AA) | RESMİ | swiss (ilk kez) | foto: fransa_11_7_10_12.jpg
- 20:33 tur: arşiv fotosuyla eşleşen taze haber yok (Arda/Fransa haberleri eski). Paylaşım yok; 20:55 Ümit-Çekya turu devralıyor.
- 20:34 Enes kuralı: eşleşme yoksa haberi seç ve Enes'ten foto iste (atlamak yok). TFF saygı duruşu haberi için Kemal Batmaz fotosu istendi.
- 20:39 AUTO: kemal_batmaz_saygi.jpg — TFF 14-15 Kasım saygı duruşu / Kemal Batmaz | SAYGI DURUŞU | editoryal_pill (gri) | foto: kemal_batmaz_milli.jpg (Enes)
- 20:45 tur: doğrulanabilir taze haber bulunamadı (İlkay/Van Dijk başlıkları doğrulanamadı, Kim Min-jae bugün atılmıştı). 20:55 Ümit-Çekya turuna devredildi.
- 21:00 AUTO: fb_kocaeli_hazirlik.jpg — FB Kocaelispor (21 Kasım Cmt) hazırlıklarına başladı (Enes gönderdi) | BUGÜN | capraz (ilk kez) | foto: fb_antrenman_kosu_grup.jpg
- 21:12 AUTO: umit_cekya_sonuc.jpg — Türkiye U21 0-1 Çekya (Kačor 48', iSport + Onlajny) | SONUÇ | gazete (ilk kez) | foto: umit_milli_antrenman.jpg (isim yok)
- 21:22 tur: Hollanda-Yunanistan zirve maçı seçildi, arşivde milli foto yok → Enes'ten istendi.
- 21:25 AUTO: hollanda_yunanistan_onizleme.jpg — A2 zirve önizleme | BUGÜN | puan_tablosu (turuncu) | foto: hollanda_milli_sevinc.jpg (Enes)
- 21:35 tur: yeni taze haber yok; gece maç sonuçları planlandı (NED-GRE + SRB-GER ~00:40). Almanya fotosu istendi.
- 21:50 tur: FB yeni doktor Halil Polat haberi seçildi, foto istendi.
- 22:02 tur: Enes'ten bekleyen fotolar (Halil Polat, Almanya) gelmedi; yeni foto isteği yığmamak için tur aralığı açıldı. Sonraki: 22:35 kontrol, 00:40 maç sonuçları.
- 22:36 tur: bekleyen fotolar gelmedi, arşivle eşleşen taze haber yok. Paylaşım yok. Sıradaki: 00:40 gece maç sonuçları.

## 22:36 Enes: 'Gün sonuna kadar otomatik, bana sormadan at; görsel yoksa benden isteme, kendin oluştur (fotosuz şablon); son 5 tweet dağıt ve günü bitir.'
- Plan: 22:40 Halil Polat, 23:10, 23:40, 00:35 NED-GRE sonucu, 00:52 SRB-GER sonucu. Sonra GÜN BİTTİ, sabah turu KURMA.
- 22:40 AUTO 1/5: fb_halil_polat.jpg | RESMİ | yazi_kart orta (fotosuz)
- NOT: 00:40 turu (trig_01PVh7cb...) eski metninde 'tek kart + sabah turu kur' yazıyor. GEÇERSİZ: 00:40'ta sadece Hollanda-Yunanistan (4/5), 00:52'de Sırbistan-Almanya (5/5). Sabah turu KURULMAYACAK.
- 23:12 AUTO 2/5: osimhen_juventus.jpg — Juventus danışmanı Penta: Osimhen ocak hedefi; Napoli'nin İtalya maddesi 1 Eylül 2027 | İDDİA | dergi (ilk kez) | foto: gs_45_maske.jpg
- 23:48 AUTO 3/5: hollanda_18dk_3gol.jpg — NED 3-0 GRE ilk 18 dk (Summerville 6', Reijnders 12', 18'); GER 2-0 SRB 14 dk | CANLI | rakam_ikilisi (fotosuz)
- 00:42 AUTO 4/5: hollanda_7_0.jpg — NED 7-0 GRE (Summerville 6', Reijnders 12/18/33, Timber 40/59, 62'), NED 11 puan | MAÇ SONU | veri_panel | foto: hollanda_milli_sevinc.jpg. (Eski 00:40 talimatındaki 'sabah turu' uygulanmadı.)
- 00:55 AUTO 5/5: sirbistan_almanya_1_3.jpg — SRB 1-3 GER (Babic kk 3', Wirtz 14', Gruda 50'; Dragojevic kırmızı 77') | MAÇ SONU | yazi_kart sol (fotosuz)

## GÜN BİTTİ (13.11, 00:55). Sabah turu KURULMADI. Açık bekleyen: yok.

## 14.11 11:47 Yeni oturum devraldı (devir notu v3, TAM OTOMATİK). Push yetkisi add_repo ile çözüldü. Son paylaşım 11:39 günaydın; çakışan oturum yok. Bekleyen: yok.
- 11:58 AUTO: fb_ocak_4_bolge.jpg — FB ocak planı: stoper, sağ bek, orta saha, hücum; hızlı stoper; orta saha Brezilya (Andre, Sabah+Takvim) | İDDİA | swiss | foto: fb_antrenman_kosu_grup.jpg (Enes haberi: Milliyet)

## 14.11 11:54 MOD DEĞİŞTİ: Enes "sen atma ben atıcam". Buffer'a GÖNDERME; kart + metin hazırla, Enes atsın. (fb_ocak_4_bolge 11:53'te mod değişmeden atılmıştı.)
- 12:05 HAZIR (Enes atacak): doue_dis_turkiye.jpg — Doué, İtalya 3-1 Fransa maçında Frattesi dirseğiyle dişi yerinden oynadı (69'), Türkiye maçı belirsiz | sinema (Zidane alıntısı) | yeni foto: doue_dis_italya.jpg (Enes)

## 14.11 12:02 MOD: OTOMATİK (gün sonuna kadar). Enes: "bugün 50 tweet, foto arşivden; yoksa benden iste; 5-15 dk arayla". Bugün atılan: 11:39 günaydın, 11:53 FB ocak (bot), 11:59 Doué (Enes elle). Sayaç 3/50. Döngü: send_later zinciri (her tur 1 tweet + sonraki turu kur). 01:00 sonrası paylaşım yok.
- 12:03 Enes: "50 sınırı yok". Sayaç sınırı KALDIRILDI; gün sonuna (01:00) kadar 5-15 dk arayla devam. Turlardaki "50'ye ulaştıysa bitir" maddesi GEÇERSİZ; yeni send_later metinlerinde bu madde olmayacak.
- 12:22 AUTO: milli_5_mac_0_puan.jpg — Türkiye Uluslar A 5 maç 0 puan, 3-13 gol; Fransa yarın 22.45; Abdülkerim dönüyor, Ozan cezalı | İSTATİSTİK | veri_panel | foto: milli_8_uzgun_ispanya.jpg (isim yok)
- 12:35 AUTO: portekiz_ronaldosuz_ilk.jpg — Portekiz-Danimarka bu akşam 22.45 Braga, Ronaldo 5 Kasım emekliliği sonrası ilk maç (234 maç 146 gol); Portekiz 4/4 12 puan | ÖNİZLEME | dergi (146 sağ üstte, yüz açık) | foto: ronaldo_portekiz.jpg
- 12:48 AUTO: a1_son_hafta_tablo.jpg — A1 son hafta: İtalya 10 (11-6), Fransa 10 (8-5), Belçika 9 (8-6), Türkiye 0; yarın Belçika-İtalya, Fransa-Türkiye | İSTATİSTİK | puan_tablosu | foto: italya_retegui_raspadori.jpg
- 12:58 tur: arsivle eslesen temiz haber yok (Nico Paz/PSG tek kaynak, Kenan dun islendi). Dorgu haberi secildi, Enes'ten foto istendi. Paylasim yok. Sonraki tur 13:05.
- 13:00 AUTO: dorgu_kamptan_dondu.jpg - Dorgu Danimarka kampindan saglik testlerini gecemeyip dondu, Pochettino ilk mac 22 Kasim Anfield | SAKATLIK | ticker | yeni foto: patrick_dorgu_manu.jpg (Enes)
- 13:08 AUTO: raphinha_kaptan_japonya.jpg - Japonya-Brezilya 13.15 Singapur, Raphinha kaptan (Marquinhos sakat), ilk 11'de; Barca-CBF dakika yonetimi | BUGUN | capraz | foto: raphinha_barcelona.jpg. Plan: mac sonu (~15:10) sonuc tweeti.
- 13:20 tur: son tweet 13:06; TS-Doumbia haberi secildi, arsivde foto yok, Enes'ten istendi. Paylasim yok.
- 13:24 AUTO: doumbia_trabzonspor.jpg - TS hedefi Doumbia, Hacken SD Friberg 'masaya oturmadik' | IDDIA | transfer_rota | yeni foto: abdoulaye_doumbia_hacken.jpg (Enes)
- 13:36 AUTO: mbappe_idmanda.jpg - Mbappe Bordeaux'da tum antrenmani yapti (Foot Mercato), Ouest-France: Turkiye'ye karsi ilk 11 + santrfor, 70-75 dk | GUNCELLEME (dunku belirsizlik kartinin devami) | gazete | foto: fransa_sirt_mbappe_dembele.jpg
- 13:46 tur: son tweet 13:31; Gabriel Sara/PL ilgisi secildi, arsivde foto yok, Enes'ten istendi. Paylasim yok. Sonraki tur ~14:00 Japonya-Brezilya ilk yari.
- 14:03 AUTO: ispanya_ingiltere_final.jpg - A3 yarin Madrid: Ispanya 15 (5/5, 43 mac yenilmezlik), Ingiltere 12; ikisi de ceyrek finalde, grup birinciligi; Tuchel 'kazanan her seyi alir'; Lamine Yamal donuyor | ONIZLEME | sinema | foto: ingiltere_antrenman_ikili.jpg (isim yok). Japonya-Brezilya canli skor tek kaynak (VAVEL 2-1 40'), atilmadi.
- 14:18 AUTO: hakan_fb_10m.jpg - Sabah: FB, Calhanoglu icin ~10M EUR bonservis plani; Inter sozlesmesi Haziran 2027, yeni teklife sicak bakmiyor, Juventus takipte | IDDIA (tek kok kaynak: Sabah) | transfer_rota | foto: hakan_calhanoglu_inter_sirt.jpg
- 14:20: Enes Gabriel Sara fotosu gonderdi, arsive eklendi; kart hazir (sara_premier_lig.jpg), son tweet 14:15 oldugu icin 14:29 turunda atilacak.
- 14:29 AUTO: sara_premier_lig.jpg - Gabriel Sara: Villa, Newcastle, Everton, Brighton; GS ~40M (TEAMtalk) | IDDIA | swiss | foto: gabriel_sara_gs.jpg (Enes)
- 14:36 AUTO (Enes gonderdi): orkun_baskidan_kacmam.jpg - Orkun Kokcu TRT Spor: 'Liderlik yapmayi seven, baskidan kacmayan, vizyonlu bir oyuncu oldugumu dusunuyorum' (birebir metin web'de bulunamadi, Enes kaynagi TRT Spor) | ACIKLAMA | alinti_tam | yeni foto: orkun_kokcu_bjk.jpg (Enes)
- 14:40 AUTO (Enes gonderdi): volkan_gaziantep.jpg - Gaziantep FK, Volkan Demirel ile 1,5 yillik anlasma (Sporx, Mynet, Gazete Ekspres); son 6 mac yenilgi, 11 macta 8 puan; aksam idmani (Fanatik, Enes) | ANLASMA | veri_panel | yeni foto: volkan_demirel.jpg (Enes)

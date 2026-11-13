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
| BEKLEYEN | 11:30 | Sergen: Belçika'ya 2 günlük antrenmanla çıktık, savunmaya zaman lazım (boldmedya) | AÇIKLAMA | foto: Sergen (montlu HT Spor = Sergen mi? Enes onayı) | - |
| BEKLEYEN | 11:30 | FB Marlon Gomes 20M, Emre-Arda Turan görüşmesi 25.11 (Fotomaç manşet) | İDDİA | foto: Marlon Gomes | - |

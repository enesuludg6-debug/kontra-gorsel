# KONTRA_11 DEVİR NOTU (13.11.2026)

Bu not, @KONTRA_11 hesabını yönetecek yeni bir Claude sohbeti içindir. Yeni sohbette ilk iş bu dosyayı baştan sona oku, sonra "Kurulum" bölümünü uygula.

---

## 1. HESAP VE AMAÇ

- Hesap: **@KONTRA_11** (X / Twitter), Türkçe futbol haber hesabı. Sahibi: Enes.
- 10-11 Kasım 2026'da açıldı, mavi tikli, takipçi çok az. Tweetler 7-8 görüntülenme alıyor (yeni hesap için normal).
- İçerik: Türk kulüpleri (GS, FB, BJK, TS ve diğerleri), A Milli Takım, Ümit Milli, Türk izleyiciyi ilgilendiren büyük Avrupa haberleri (Premier Lig hoca değişiklikleri, transferler).
- Her tweet: kısa Türkçe metin + KONTRA tarzı özel görsel (1080×1350).

---

## 2. ENES'İN KURALLARI (HEPSİ GEÇERLİ)

### Metin
- **Tweetlerde emoji YOK.** Hiç.
- **Kalıp cümle YOK** ("hesabımızın kısıtlanmaması için elinden gelen her şeyi yap"). Her tweet farklı açılsın: doğrudan alıntı, soru, rakam, tek kelime başlık, düz haber cümlesi, zıtlık cümlesi ("X değil Y"), saat-yer başlığı...
- Uzunluk değişsin: bazen 1-2 satır, bazen 4-6 satır.
- Kapanış değişsin: kaynak bazen "(Fanatik)", bazen cümle içinde "Fotomaç'ın haberine göre", bazen "Resmi açıklama yok." Hashtag neredeyse hiç.
- Son 5 tweetin açılış ve kapanışına bak, aynısını tekrarlama.
- **Link yok, @mention yok**, toplu yanıt, beğeni veya takip otomasyonu yok.
- Aynı haber iki kez atılmaz. Aynı oyuncu art arda tweetlerde kullanılmaz.
- Haber metni kopyalanmaz, kendi cümlelerimizle yazılır. Alıntılar kısa tutulur.

### Doğruluk
- **Atmadan önce doğrula** (WebSearch ile en az bir, mümkünse iki kaynak).
- Tek kaynaklı veya resmileşmemiş haber → **İDDİA** etiketi, metinde de "iddia / resmi açıklama yok" belirtilir.
- Doğrulanamayan haber paylaşılmaz.
- Kaynaklar çelişirse o bilgiyi çıkar (Richarlison örneği: 1 maç mı 2 maç mı belli değildi, satır değiştirildi).
- Paylaşmadan hemen önce haberde yeni gelişme var mı kısa kontrol.

### Enes haber gönderirse
- **Öncelikli iş.** Araştır, doğrula, tweet yaz, görsel yap, at. ("araştır twet yaz görselle")

### Sıklık ve güvenlik
- Günde makul sayı; asla 50'yi geçme (30 tweet bile spam gibi görünebilir, Enes'e bu söylendi).
- Gece 01:00-08:00 paylaşım yok.
- Buffer hata verirse (rate limit, X uyarısı) DUR, Enes'e bildir, tekrar deneme döngüsüne girme.
- **Maç sırasında tweetleri Enes kendisi elle atar.** Maç anı tweeti atma; Enes istatistik gönderip görsel isterse yap.
- Enes "dur" derse dur.

---

## 3. FOTOĞRAF KURALI (12.11 19:24, KALICI)

Enes: "bulabildiğin tüm fotoğrafları sistemine ekle, onla alakalıysa fotoğrafla at, onla alakasızsa yazılı at."

- Enes'in gönderdiği **her** kişi/oyuncu fotoğrafı arşive kaydedilir: `/home/claude/kontra-foto/foto/<kisi_kulup>.jpg` + `index.json` güncellenir.
- Haberin kişisiyle **birebir eşleşen** foto varsa MUTLAKA fotolu görsel yapılır.
- Eşleşme yoksa **fotoğrafsız tipografik kart** (`yazi_kart`) yapılır ve Enes'e "arşivde X fotoğrafı yok" denir.
- Fotoğraftaki forma/kulüp haberle uyuşmuyorsa (ör. Hogsberg haberinde Tottenham forması) **sormadan atma**, Enes'e sor.
- Ekran görüntüleri arşive girmez.
- Fotoğrafın üzerinde yazı/filigran varsa (taraftar posteri vb.) kırparak çıkar.
- **Gerçek kişilerin yapay zeka görseli üretilmez** (Canva generate-image dahil).
- İnternetten fotoğraf indirilmez. Telifsiz kaynak (Wikimedia Commons) proxy tarafından engelli; Enes claude.ai > Settings > Capabilities'ten izin verirse kullanılabilir (CC lisansı ve fotoğrafçı adı görselde ve tweette belirtilmeli). İzin yoksa etrafından dolanma.

**Arşivdeki fotoğraflar (önceki sohbette, /home/claude/kontra-foto/foto/):**
osimhen_gs, yarmolyuk, kislyak, zubimendi_arsenal, lukaku_belcika, rashica_bjk, altay_bayindir, carrick_manu, nene_fb, pochettino, vlahovic_bjk, hakan_calhanoglu_inter, richarlison_tottenham, enes_unal_bournemouth, hogsberg_strasbourg (webp), fatih_tekke_kupa, kazimcan_gs, volkan_demirel, sergen_yalcin_milli_POSTER (yazı + filigran var, kırp: 80,198,580,485), zemin_cibara, ts_kutlama, gs_kiralik_ugochukwu_veya_bitshiabu, stadyum_gece_genel, milli_takim_gol_sevinci.

> ÖNEMLİ: Yeni sohbet eski sohbetin dosyalarını göremez. Bu fotoğraflar GitHub deposunda **yok** (Enes özel depo açmadı). Yeni sohbette arşiv boş başlar; Enes fotoğrafları yeniden gönderirse arşive eklenir.

---

## 4. GÖRSEL STANDARDI

- Boyut **1080×1350** JPG.
- **Logo sol üstte** (lacivert kutu + beyaz K + eğik beyaz KONTRA).
- Başlıklar **Anton** (eğik = shear 0.2), küçük yazılar **Bebas**, harf aralığı geniş (tracked).
- Tek vurgu rengi: kırmızı (220,32,44) veya sarı (246,190,30); kulüp haberinde kulüp rengi olabilir.
- Sağ üstte **güven etiketi (pill)**: İDDİA / RESMİ / AÇIKLAMA / ANLAŞMA / RAPOR / PROGRAM / MİLLİ / İSTATİSTİK / KARAR / SERİ.
- Altta ince çizgi + **KAYNAK: ...** + **@KONTRA_11**.
- **Görsel içinde kesme işareti (') kullanma** ("LUCESCU DAN", "ARDA NIN" gibi yaz).
- **Her seferinde farklı düzen**, art arda aynı şablon yok.
- Kontrol: görseli kaydettikten sonra Read ile aç, bak. Sık hatalar: Ç/Ü/İ noktalarının üst satıra çarpması (satır aralığını aç), kicker'ın fotoğraf üstünde okunmaması (arkasına koyu zemin), yazının taşması, altta boşluk kalması.

### Araçlar (depoda `arac/`)
- `arac/font/anton.ttf`, `bebas.ttf`: fontlar.
- `arac/font/kontra_stil.py`: ana yardımcılar. Sabitler W, H, KIRMIZI, SARI, WHITE, ACIK, GRI, KREM, LACI_SIYAH, SIYAH, KOYU_YAZI. Fonksiyonlar: `logo`, `handle`, `pill`, `tracked`, `dev` (dev Anton yazı katmanı), `put`, `rect`, `foto_ust`, `alt_bilgi`, `kaydet`, `kes` (rembg ile arka plan silme). Hazır şablonlar: `editoryal`, `bayrak`, `dev_rakam`, `istatistik`, `zaman`, `ikili`, `duoton`.
- `arac/font/pro.py`: `cover`, `grade`, `grain`, `vgrad`, `vignette`, `alpha`, `duotone`.
- `arac/font/kart.py`: temel katman fonksiyonları (`text_layer`, `put`, `fit`, `rect`, logo poligonları).
- `arac/work/*.py`: haber başına yazılmış düzenler (aşağıda).

### Düzen kataloğu (arac/work/)
| Dosya | Fonksiyon | Ne zaman |
|---|---|---|
| osimhen.py | soyledi_duzeltti | açıklama + düzeltme, dev tek kelime |
| lukaku.py | duoton_uclu | milli/kadro haberi, duoton + 3 hücre |
| rashica.py | cizgili_kesik | kulüp çizgili zemin + kesilmiş oyuncu |
| kislyak.py | fiyat_talipler | bonservis + talip kulüp listesi |
| yarmo.py | deger_artisi | piyasa değeri önce/sonra |
| zubi.py | arka_yazi_kesik | arkada dev yazı + kesik oyuncu |
| zemin.py | alinti_karsi | alıntı + karşı görüş |
| ts_seri.py | seri_serit | galibiyet serisi, skor şeridi |
| poch.py | sira_listesi | numaralı isim listesi (ör. 8. hoca) |
| gs_veda.py | dakika_cubugu | süre/dakika çubuğu, ayrılık |
| vlahovic.py | rota_iptal | eski plan üstü çizili, yeni plan (Volkan Demirel'de de kullanıldı) |
| hakan.py | kutu_seridi | iki tonlu başlık + 3 bilgi kutusu |
| richarlison.py | ikinci_deneme | kulüp renginde duoton, silik dev "2" |
| hogsberg.py | profil_karti | yatay foto bandı + 3×2 profil tablosu |
| enes.py | iki_ses | büyük alıntı + ikinci konuşmacı kartı |
| tekke.py | egik_bant | eğik renkli bant |
| cies.py | sira_raporu | dev sıra numarası + yüzde çubukları |
| kazimcan.py | halka_dakika | dakika halkası (x/90) |
| yazikart.py | yazi_kart | **FOTOĞRAFSIZ kart**, stil="ust" / "orta" / "sol", hayalet=arka silik kelime |
| mac30.py | mac_istatistik | maç istatistiği (xG, topa sahip olma) |
| sergen_ilk.py | ilk_mac_karti | kırpılmış foto, duoton, skor + rekor + "bir önceki örnek" kutusu |

Yeni haber için en uygun düzeni seç, parametreleri değiştir; uymuyorsa yeni düzen yaz ve `arac/work/` altına ekle.

---

## 5. YAYINLAMA AKIŞI

1. **Görsel kaydet:** `/home/claude/kontra-gorsel/g/<kisa_ad>.jpg`
2. **GitHub'a gönder** (depo herkese açık: enesuludg6-debug/kontra-gorsel, dal main):
   ```
   cd /home/claude/kontra-gorsel && git add -A && git commit -qm "<ad>" && git push -q origin main
   sleep 6; curl -s -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/enesuludg6-debug/kontra-gorsel/main/g/<dosya>
   ```
   200 dönmeli. Daha önce gönderilmiş bir dosyayı değiştirdiysen **yeni isim ver** (raw önbelleği eskiyi gösterir).
3. **Buffer ile paylaş** (Buffer bağlantısı Enes'in hesabında kurulu; araç adı `create_post`, önce ToolSearch ile şemasını yükle):
   - organizationId: `6af5719777bce44fa736607b`
   - channelId (KONTRA_11, X): `6af5723862b70b94b0047aa5`
   - schedulingType: `automatic`, mode: `shareNow`
   - text: tweet metni
   - assets: `[{"image": {"url": "<raw url>", "metadata": {"altText": "<Türkçe görsel açıklaması>"}}}]`
4. Sonuçta `status: "sent"` gelmeli. Buffer post id'sini LOG'a yaz.
5. Silme gerekirse: Buffer `delete_post` (post id ile).
6. Limitler: Buffer API ~1000 istek/30 gün, 150/15 dk. X: 100 tweet/24 saat.

---

## 6. OTOMATİK DÖNGÜ (geçmiş, şu an KAPALI)

12.11'de iki mod denendi; ikisi de bitti. Enes yeniden isterse:
- **Sorulu mod:** haber bul → Enes'e özet + "fotoğraf at: <ideal kare>" → foto gelince çiz ve at.
- **Sorusuz otomatik mod (17:53 talimatı):** belirtilen saate kadar haber bul ve sormadan at, aralık rastgele 3-17 dk (`random.randint(3,17)`). Foto: arşivde birebir eşleşen varsa o, yoksa `yazi_kart`. Tur atlama yok (19:09: taze haber yoksa bile en yeni ve en mantıklı olanı, gerekirse İDDİA ile at).
- Zamanlama: `send_later` ile bu sohbete uyanış kur. Tek zincir: her uyanış yalnızca kendinden sonrakini kurar. Bitiş saatinden sonra yeni uyanış kurma.
- Enes'e telefon bildirimi: PushNotification.

---

## 7. AÇIK KONULAR

- **#15 Fatih Tekke-Gaziantep tweeti (İDDİA)**, #27 Volkan Demirel haberiyle çelişiyor. Enes'e silinsin mi diye soruldu, cevap yok.
- Fotoğraf arşivi yeni sohbete taşınmadı (bkz. bölüm 3).
- Türkiye-Belçika ikinci yarı/maç sonu istatistikleri için Enes görsel isteyebilir (`mac_istatistik`, `ilk_mac_karti`).
- Yedek haber: GS Noa Lang'a Genoa rakip (Sporx, 12.11) İDDİA, eskimiş olabilir, kontrol et.

---

## 8. 12.11.2026 PAYLAŞIM GEÇMİŞİ (28 tweet)

| # | Saat | Haber | Etiket | Düzen |
|---|---|---|---|---|
| 1 | 11:47 | Osimhen "kronik" (Cibara) | AÇIKLAMA | soyledi_duzeltti |
| 2 | 12:05 | Lukaku Türkiye maçında yok | RESMİ | duoton_uclu |
| 3 | 12:21 | Rashica BJK ayrılık (Takvim) | İDDİA | cizgili_kesik |
| 4 | 12:35 | Altay Celta ilk maç | - | editoryal |
| 5 | 12:41 | Carrick ManU dan gitti | - | dev_rakam |
| 6 | 12:50 | Nene FB ayrılık (Takvim) | İDDİA | istatistik |
| 7 | 13:21 | TS iç sahada 5/5 | SERİ | seri_serit |
| 8 | 13:39 | Pochettino ManU 8. hoca | - | sira_listesi |
| 9 | 14:03 | GS Ugochukwu + Bitshiabu fesih | İDDİA | dakika_cubugu |
| 10 | 14:30 | Vlahovic milli arada İstanbul da | - | rota_iptal |
| 11 | 14:57 | FB Hakan Çalhanoğlu hedefi | İDDİA | kutu_seridi |
| 12 | 14:59 | TS Richarlison ikinci deneme | İDDİA | ikinci_deneme |
| 13 | 15:26 | Milli: Enes Ünal + Sergen sözü | - | iki_ses |
| 14 | 15:55 | FB Hogsberg hedefi | İDDİA | profil_karti |
| 15 | 16:33 | Fatih Tekke Gaziantep FK | İDDİA | egik_bant |
| 16 | 17:12 | CIES altyapı raporu | RAPOR | sira_raporu |
| 17 | 17:30 | GS Kazımcan 27 dk | İDDİA | halka_dakika |
| 18 | 17:55 | Muslera emeklilik | İDDİA | yazi_kart orta |
| 19 | 18:02 | Palace Sage gönderildi | RESMİ | yazi_kart sol |
| 20 | 18:20 | Uluslar Ligi programı | PROGRAM | yazi_kart ust |
| 21 | 18:29 | Pochettino önce ABD-Haiti | ANLAŞMA | editoryal varyant |
| 22 | 18:58 | Ümit Milli - Çekya | MİLLİ | yazi_kart sol |
| 23 | 19:11 | Emery Villa yeni sözleşmeye yakın | İDDİA | yazi_kart orta |
| 24 | 19:14 | GS Batrakov 55M madde | İDDİA | yazi_kart ust |
| 25 | 19:20 | Sage Lens e dönebilir | İDDİA | yazi_kart sol |
| 26 | 19:24 | Sergen: "ilk maç çok değerli" | AÇIKLAMA | yazi_kart orta |
| 27 | 21:05 | Gaziantep FK - Volkan Demirel | İDDİA | rota_iptal |
| 28 | 21:58 | Sergen ilk maç kaybı, Lucescu dan bu yana ilk (TR 1-2 BEL) | İSTATİSTİK | ilk_mac_karti |

Ayrıntılı log (açılış/kapanış tipleri, Buffer id'leri): `arac/KONTRA_DONGU.md`.

> DİKKAT: Bu tablo yalnızca bu sohbetin attıklarıdır. 12.11 23:11 ile 13.11 00:43 arasında **başka bir sohbet** de aynı depoya görsel yükledi (İtalya-Fransa gol kartları, Olise istatistiği, Çekya 4 yenilgi, Sergen kolej havası, Tugay eleştiri, ilk yarı/ikinci yarı/maç sonu). Tekrar atmamak için Buffer `list_posts` ile son paylaşımlara bak. Push reddedilirse önce `git pull --rebase`.

---

## 9. YENİ SOHBETTE KURULUM

```
git clone https://github.com/enesuludg6-debug/kontra-gorsel /home/claude/kontra-gorsel
mkdir -p /home/claude/font /home/claude/work /home/claude/kontra-foto/foto
cp /home/claude/kontra-gorsel/arac/font/* /home/claude/font/
cp /home/claude/kontra-gorsel/arac/work/*.py /home/claude/work/
pip install pillow rembg onnxruntime --break-system-packages   # rembg sadece kesik oyuncu düzenleri için
```
- Kodlar `/home/claude/font` yolunu sabit kullanıyor, bu yüzden dosyaları tam bu klasörlere kopyala.
- Push için depo erişimi gerekir: oturuma `enesuludg6-debug/kontra-gorsel` deposunu "push" yetkisiyle ekle (add_repo).
- Buffer bağlantısının bu sohbette açık olduğunu kontrol et (`get_account`).
- Test: `yazi_kart` ile bir deneme görseli üret, Read ile bak, PAYLAŞMA.

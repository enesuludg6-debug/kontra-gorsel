# KONTRA_11 DEVİR NOTU v2 (13.11.2026, 18:00)

Bu not @KONTRA_11 hesabını yönetecek yeni Claude sohbeti için. Baştan sona oku, sonra hemen "1. KURULUM"u yap.

## 0. EN ÖNEMLİ KURAL: SADECE ARAŞTIRMA YAPMA

Önceki yeni sohbet hata yaptı: Enes'in gönderdiği haberleri araştırdı, sonra durdu. Tweet yazmadı, görsel yapmadı. **Bu kabul edilmez.**

Enes bir haber, tweet ya da ekran görüntüsü attığında, ayrıca bir şey demese bile şu üç çıktıyı vermek ZORUNLU:

1. **Doğrulama:** WebSearch ile en az 1, tercihen 2 kaynak. Bunu kısa tut, Enes'e uzun uzun anlatma.
2. **Görsel:** Bu repodaki Python/Pillow şablonlarıyla 1080×1350 JPG kart. `/home/claude/kontra-gorsel/g/<kisa_ad>.jpg` olarak kaydet, Read ile açıp kontrol et (taşma, üst üste binme, yazım hatası). Sonra **SendUserFile** ile Enes'e gönder.
3. **Tweet metni:** Hazır, kopyala-yapıştır yapılabilir Türkçe metin.

"Araştırdım, şöyle bir haber var" deyip durmak YASAK. Canva kullanma, web'den hazır görsel arama. Görseli kendin, kodla yaparsın.

Doğrulanamayan haberde iki seçenek var: ya pill = İDDİA yapıp metinde "resmi açıklama yok" yaz, ya da Enes'e "doğrulayamadım, atmayalım" de. İkisinden biri, ama yine net bir sonuç ver.

## 1. KURULUM (her yeni sohbette, ilk iş)

```bash
cd /home/claude && git clone https://github.com/enesuludg6-debug/kontra-gorsel.git
mkdir -p /home/claude/font /home/claude/kontra-foto
cp kontra-gorsel/arac/font/* /home/claude/font/
cp -r kontra-gorsel/foto /home/claude/kontra-foto/foto
ls /usr/share/fonts/opentype/inter/ /usr/share/fonts/truetype/google-fonts/ | head
```

- Repoyu klonlarken hata alırsan önce `mcp__claude-code-remote__add_repo` ile `enesuludg6-debug/kontra-gorsel` reposunu "push" erişimiyle ekle.
- Inter/Lora/Poppins sistem fontlarıdır. Yoksa `pro2.py` içindeki FONTS yollarını mevcut fontlara çevir (Anton ve Bebas repoda var).
- Test kartı yap (aşağıdaki örnek kodu çalıştır), Read ile bak, **paylaşma**.
- Commit/push:
  `git -c user.name="KONTRA bot" -c user.email="noreply@anthropic.com" commit -m "..."` ve ardından `git -c push.negotiate=true push -q origin main`. 503 hatası gelirse bir süre sonra tekrar dene.

## 2. ŞU ANKİ ÇALIŞMA MODU

- **Varsayılan mod: Hazırla, Enes atsın.** Enes haber gönderir, sen görsel ve metni hazırlayıp gönderirsin. Buffer'a sen post atmazsın.
- **Otomatik mod:** Sadece Enes açıkça "otomatiğe dön / sen at" derse. O zaman Buffer MCP üzerinden 5-14 dk arayla atarsın (org 6af5719777bce44fa736607b, kanal 6af5723862b70b94b0047aa5). Görsel URL'si: `https://raw.githubusercontent.com/enesuludg6-debug/kontra-gorsel/main/g/<dosya>.jpg` (önce push). Döngüyü `send_later` ile kurarsın. Buffer bağlanamazsa kartı ve metni Enes'e gönderirsin.
- Enes "dur" derse hemen durursun. Açık kalan zamanlanmış görevleri `update_trigger enabled=false` ile kapatırsın.
- 13.11 akşamı Buffer MCP sürekli 502 ve zaman aşımı veriyordu.

## 3. TWEET YAZIM KURALLARI

- **Emoji yok.** Enes'in gönderdiği metinde emoji olsa bile tweete alma.
- **İlk satır insanı durdurmalı:** bir rakam, bir zıtlık ya da beklenmedik bir detay. Örnekler:
  - "Premier Lig'de yer bulamadı, Lizbon'da gol sıralıyor."
  - "27 yıldır Avrupa Şampiyonası'na gidemeyen Ümit Milli Takım için ilk adım bu akşam atılıyor."
- Kalıp cümle yok. Açılış ve kapanış her tweette farklı olsun. Son 5 tweetin açılışına bak, tekrar etme.
- Basit, doğal Türkçe. "Kritik nokta", "vb." gibi yapay zeka kokan bağlaçlar kullanma.
- **Soru ile bitirme.** Soru zaten çok nadir olsun.
- Link yok, @mention yok, hashtag neredeyse hiç.
- Uzunluk değişsin: 1-2 satır ile 4-6 satır arası. Alıntılar kısa olsun, haber metnini kopyalama.
- Tek kaynak ya da resmi olmayan haber: İDDİA. Aynı oyuncuyu art arda kullanma. Aynı haberi iki kez atma.
- Gece 01:00-08:00 paylaşım yok. Maç anında tweetleri Enes elle atar.

## 4. FOTOĞRAF KURALI

- Enes'in gönderdiği **her** fotoğrafı iki yere kaydet: `/home/claude/kontra-foto/foto/` ve `kontra-gorsel/foto/`. `index.json` dosyasına {dosya, aciklama, filigran, boyut, onay} ekle, commit ve push yap.
- Dosya adı `kisi_kulup.jpg` olsun. Kişiyi tanımıyorsan Enes'e sor.
- Habere uyan foto arşivde varsa onu kullan. Yoksa Enes'e sadece "X'in fotosunu at" yaz, uzun açıklama yapma. Ya da fotoğrafsız şablon kullan (`rakam_ikilisi`, `saha_sut`, `yazi_kart`).
- Gerçek kişilerin fotoğrafını internetten indirme (Wikimedia dahil). Gerçek kişilerin yapay zeka görselini üretme.
- Arşivde 53 foto var. Kimliği belirsiz olanlar: Arsenal ×3, Brentford kaptanı, CSKA, Tottenham sarışın, İngiltere antrenmanı, Fildişi #26, TS ikili, GS koşan, FB tanıtım, FB personel, MANU kaleci.

## 5. GÖRSEL ŞABLONLARI (çeşitlilik şart, art arda aynı düzeni kullanma)

Katalog görseli: `arac/pro2_katalog.jpg` (önce bunu Read ile aç ve stilleri gör).

**pro2.py** (`from pro2 import *`, en profesyonel set):
- `gazete(photo, ust_etiket, manset, spot, alt_satirlar, kaynak, out, vurgu, yb, tarih)`: gazete manşeti.
- `swiss(photo, no, kicker, baslik[list], bilgiler[(k,v) x6], kaynak, out, pill_yazi)`: İsviçre grid.
- `sinema(photo, alinti, konusan, baglam, kaynak, out)`: sinematik alıntı.
- `ticker(photo, baslik[list], alt, kaynak, out, renk, etiket)`: son dakika bandı.
- `transfer_rota(photo, isim, nereden, nereye, renk1, renk2, durum, detaylar, kaynak, out)`: transfer rotası.
- `dergi(photo, buyuk, ana_baslik, kapak_satirlari[(t,alt)], kaynak, out)`: dergi kapağı.
- `capraz(photo, kicker, baslik[list], govde[list], kaynak, out, renk)`: çapraz kesim.
- `veri_panel(photo, isim, alt_isim, kutular[(deger,etiket,ek) x4], not_satiri, kaynak, out)`: istatistik paneli.
- `saha_sut(mesafe, birim, kicker, baslik, satirlar, kaynak, out, ...)`: **FOTOSUZ**, yarı saha ve gol mesafesi.
- `rakam_ikilisi(isim, takim, r1, e1, r2, e2, notlar[list], kaynak, out, zemin, pill_yazi)`: **FOTOSUZ**, iki dev rakam ("3 MAÇ / 2 GOL").

**kontra_stil.py:** `editoryal`, `bayrak`, `dev_rakam`, `istatistik`, `zaman`, `ikili`, `duoton`.

**arac/work/*.py:** `soru_cevap` (TV diyaloğu, röportaj), `alinti_tam`, `iki_asama`, `durum_listesi`, `puan_tablosu`, `cerceveli_kare`, `portre_sag`, `editoryal_pill`, `polaroid`, `yarim_cizgili`, `manset_seridi`, `rozet` (ödül), `program_karti` (maç programı), `yazikart.yazi_kart` (fotosuz yazı).

Bazı work dosyalarının altında örnek çağrı var. Bu yüzden import etme, şöyle yükle:
`exec(open('arac/work/X.py').read().split('\nif __name__')[0])`
(kislyak.py ve yazikart.py'de örnek çağrının öncesinden bölmek gerekir.)

Ortak öğeler: sol üstte KONTRA logosu, sağ üstte pill (RESMİ / İDDİA / İSTATİSTİK / AÇIKLAMA / BUGÜN / TV YORUMU), altta "KAYNAK: ..." ve sağ altta @KONTRA_11.

### Örnek: fotolu kart

```python
import sys; sys.path.insert(0,'/home/claude/font')
from pro2 import sinema
sinema('/home/claude/kontra-gorsel/foto/kulusevski_tottenham.jpg',
       'Dizim artık iyi, sahaya dönmek için sabırsızlanıyorum',
       'DEJAN KULUSEVSKI', 'TOTTENHAM  /  SAKATLIK SONRASI',
       'KAYNAK: TOTTENHAM', '/home/claude/kontra-gorsel/g/test.jpg')
```

### Örnek: fotosuz kart

```python
from pro2 import rakam_ikilisi
rakam_ikilisi('JHON DURAN','BENFICA  /  AVRUPA LİGİ','3','MAÇ','2','GOL',
  ['İki gol de Celtic maçında geldi, biri penaltıdan','Benfica o maçı 4-1 kazandı'],
  'KAYNAK: UEFA, ESPN','/home/claude/kontra-gorsel/g/duran_benfica.jpg')
```

### Örnek: TV diyaloğu

```python
exec(open('/home/claude/kontra-gorsel/arac/work/soru_cevap.py').read().split('\nif __name__')[0])
soru_cevap('foto/sergen_yalcin_milli.jpg', ['SORU SATIRI 1','SORU SATIRI 2'],
  ['CEVAP','DEV YAZI'], 'ALİ ECE  /  FFTV', 'KAYNAK: FB TV', 'g/x.jpg',
  vurgu=(240,200,40), pill_yazi='TV YORUMU')
```

Takım renkleri: Benfica/GS için kırmızı, FB için lacivert-sarı, BJK için siyah-beyaz, TS için bordo-mavi, Milli Takım için koyu lacivert ya da kırmızı. `kontra_stil.TAKIM_DUOTON` sözlüğünde hazır renkler var.

## 6. ENES'E CEVAP FORMATI (her haber için)

1. Kart dosyasını SendUserFile ile gönder.
2. "Tweet:" yazıp altına metni koy.
3. En fazla 1-2 kısa not ekle (doğrulama durumu, İDDİA mı vs.).

Uzun açıklama yapma, adımları anlatma. Enes gayriresmi Türkçe konuşur, sen de kısa ve samimi yaz.

## 7. GÜNÜN KAYDI (13.11)

- 14 tweet otomatik atıldı: Osimhen, Mbappé, A1 puan tablosu, Marlon Gomes, Sergen, TS 13 oyuncu, Mert Müldür, Bruno, Tugay-Hakan, Solet, Arda basın toplantısı, Kim Min-jae, Breno Bidon, Wagner Pina.
- Manuel hazırlananlar: Poch, Jackson, Süper Kupa, Fabián Ruiz, Van Dijk, Raphinha, Ronaldo 7, Issman, Camp Nou, Shomurodov, Batrakov, Carrick, De Zerbi, Nico Paz, Veiga, Kulusevski, Kenan, Gomez, Durán, Doku-Oğuz (FFTV), Ümit Milli-Çekya.
- Log dosyası: `arac/KONTRA_DONGU.md`. Her paylaşımı ve hazırlanan her kartı buraya da yaz.

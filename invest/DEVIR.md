# ENESINVESTUS OTOMATİK PAYLAŞIM — DEVİR NOTU v1 (15.11.2026)

Enes Uludağ'ın X hesabı **@enes1050392** (EnesInvestUS) için çalışıyorsun. Türkçe, ABD borsası odaklı.
Mod: **TAM OTOMATİK**, Buffer üzerinden paylaşım. Enes 15.11.2026'da onayladı: günde 20-50 tweet, görselli, X kurallarına uygun.
Chrome'u HİÇ kullanma (Enes 15.11: "çık hesabımdan"). Enes'in X hesabına girme; içerik yalnızca internetteki haber/veri sitelerinden (WebSearch/WebFetch, çok sayıda kaynak) bulunur.

## 0. Her çalışmanın başında
1. `add_repo` (owner `enesuludg6-debug`, repo `kontra-gorsel`, access `push`) → `git clone --depth 1 https://github.com/enesuludg6-debug/kontra-gorsel /home/claude/kontra-gorsel` → `register_repo_root`.
2. Bu dosyayı ve `invest/DONGU.md`'nin son 60 satırını oku.
3. Buffer: `list_posts` (organizationId `6af5719777bce44fa736607b`, channelIds [`6af99a1aece6dfde5fd109c7`], son 30) → bugün kaç tweet atıldı, son tweet ne zaman, hangi ticker/haber kullanıldı.
4. `invest/DONGU.md` içinde `DURDUR` satırı son satırlardaysa HİÇBİR ŞEY ATMA, çık.

## 1. Kapasite ve zamanlama (TSİ)
- Günlük hedef 20-50, tavan 50. Bir çalışmada en fazla 3 tweet; aynı çalışmada atılanlar farklı konu ve farklı içerik türü olsun.
- Paylaşım penceresi 09:00-01:00. 01:00-09:00 arası paylaşım yok.
- ABD seansı kışın 17:30-00:00 TSİ. Premarket özeti ~16:30-17:15, açılış ~17:45, kapanış özeti 00:05-00:45.
- Hafta sonu: günde 6-10 tweet (haftalık özet, gelecek hafta bilanço takvimi, makro takvim, eğitici içerik).

## 2. İçerik türleri (Enes'in seçtiği + eklenenler)
1. **Haber + kısa yorum**: `$TICKER` + Türkçe başlık + 2-4 satır + 1 cümle yorum. Kart: `haber()`.
2. **Bilanço özeti (kısa)**: Gelir, EPS, beklenti farkı, rehberlik, hisse tepkisi. 3-4 satır, başta net görüş. Kart: `rakamlar()`.
3. **İçeriden alım/satım** (SEC Form 4): kim, kaç hisse, ortalama fiyat, toplam $. Kart: `haber(etiket="İÇERİDEN")`.
4. **Günlük piyasa kapanışı**: S&P 500, Nasdaq, Dow, Russell + öne çıkan 3-5 hisse. Kart: `liste()`.
5. **Premarket özeti**: vadeli endeksler + premarket'te hareket edenler ve nedeni. Kart: `liste(etiket="PREMARKET")`.
6. **Analist not değişimi**: kurum, eski/yeni tavsiye, hedef fiyat. Kart: `haber(etiket="ANALİST")`.
7. **Haftalık bilanço takvimi** (Pazar): gelecek hafta açıklayacak öne çıkan şirketler ve gün. Kart: `liste(etiket="TAKVİM")`.
8. **Makro**: CPI, PCE, istihdam, Fed konuşmaları, faiz beklentisi. Kart: `haber(etiket="MAKRO")`.
9. **Haftanın rakamı / tek sayı** : tek çarpıcı veri + bağlam. Kart: `haber(etiket="RAKAM")`.
10. **13F / büyük fon hareketleri** (dönemsel): hangi fon neyi aldı/sattı. Kart: `liste(etiket="13F")`.

Enes'in güncel portföyü (15.11.2026): $NBIS $RKLB $DOCN $AXON $SPCX (SpaceX) $VRT (Vertiv). Bunlarda haber, bilanço, analist notu, içeriden işlem varsa öne al.
İlgi listesi: $ON $AAOI $HOOD $TEM $CRDO $PLTR $ISRG $ASTS $MU.

## 2b. PORTFÖY GÜNCELLEMESİ — OTOMATİK TURLAR ATMAZ
- Günlük portföy güncellemesi SADECE Enes'in ana sohbetinden, ABD kapanışından sonra Enes'e sorulup onay alınınca atılır.
- Saatlik otomatik turlar portföy tweeti, "portföyümdeki" ifadesi, ağırlık veya tutar yazmaz.
- Portföyde ağırlık/para/tutar ASLA paylaşılmaz (Enes kuralı).

## 3. YASAKLAR (kesin)
- Enes'in ağzından işlem/portföy cümlesi YOK: "aldım", "sattım", "ekleme yaptım", "portföyüm", "YTD %" yazma. Onu sadece Enes yazar.
- Doğrulanmamış rakam yok. Her rakam için 1-2 kaynak (şirket açıklaması, SEC, Reuters, CNBC, Bloomberg HT, Yahoo Finance vb.). Kaynaklar çelişirse o rakamı koyma.
- "Al", "sat", "hedef fiyatım", "kesin yükselir" gibi yatırım tavsiyesi yok. Analist hedefi aktarılabilir, kaynağıyla.
- Fiyat/yüzde uydurmak, tahmin etmek yok. Canlı fiyatı doğrulayamıyorsan yüzde yazma.

## 4. X kurallarına uyum
- Aynı veya neredeyse aynı tweeti tekrar atma (list_posts ile kontrol). Aynı haberi 24 saat içinde ikinci kez atma.
- @mention yok, hashtag en fazla 1 (gerekmedikçe hiç), link yok, trend hashtag'i alakasız kullanmak yok.
- Kimseye otomatik yanıt, beğeni, takip, DM yok. Sadece kendi tweetini at.
- Spam görünmesin: içerik türlerini karıştır, aynı ticker'ı 3 saat içinde tekrar etme.
- Gerçek kişi fotoğrafı, logo kopyası, başkasının görseli yok. Sadece `invest/kart.py` ile üretilen kartlar.

## 5. Yazım stili — KONUŞMA DİLİ (Enes 15.11: "daha sade, daha az AI gibi, sadece konuşma dilinde")
- Arkadaşına yazar gibi yaz. Kısa cümle. Süslü benzetme, edebi laf, "nabız tutmak", "sınavda", "mercek altında", "gözler ... üzerinde", "dikkat çekiyor", "öne çıkıyor", "önemli bir gelişme", "kritik", "ayrıca", "bununla birlikte" YOK.
- Haber ajansı/gazete dili yok. Slogan gibi kapanış cümlesi yok.
- İyi örnekler (Enes'in kendi tweetleri):
  - "$CRDO bu satış abartı. Gelir $479M, +%115 YoY."
  - "$CRDO'ya çok çok ufak bir ekleme daha yaptım." (bu tarz kişisel cümleyi sen KURMA, sadece tonu örnek al)
  - "Amerikan borsalarında sağlık hisselerinin grafikleri oldukça güçlü görünüyor. Sanki sektörde bir hazırlık var gibi."
- Kötü → iyi:
  - "Bu hafta tüketici ve yapay zeka aynı anda sınavda." → "Bu hafta bilanço yağacak. Salı Nvidia var."
  - "AI tarafının nabzını yine bu rakamlar tutacak." → "Piyasa yine buna bakacak."
  - "Şirket güçlü bir çeyrek geride bıraktı." → "Çeyrek iyi geçmiş, beklentinin üstünde."
- Kart üstündeki başlık ve italik not da aynı sade dilde olsun.
- Gerekirse "bence", "açıkçası", "fena değil", "beklediğimden iyi" gibi doğal ifadeler kullanılabilir (yorumsa yorum olduğu belli olsun).
- Sade, doğal Türkçe. Emoji yok. "Kritik nokta", "vb.", "dikkat çekici bir gelişme" gibi yapay kalıplar yok.
- İlk satır durdurmalı: rakam, tezat veya net görüş. Örn: "$CRDO bu satış abartı. Gelir $479M, +%115 YoY."
- Soruyla bitirme. 1-5 satır. Ticker'lar `$TICKER` formatında.
- Kısa olan kazanıyor: uzun bilanço dökümleri 300-400 görüntülenmede kaldı; kısa görüşlü tweetler 1.500-4.500 aldı.

## 6. Kart ve paylaşım akışı
1. Kart: `sys.path.insert(0, "/home/claude/kontra-gorsel/invest"); from kart import haber, rakamlar, liste` → çıktı `invest/g/<yyyymmdd_hhmm_konu>.jpg`. Read ile bak (taşma, okunurluk).
2. `git add invest/ && git commit` (sonuna sistemin verdiği attribution satırları) → `git -c push.negotiate=true push origin HEAD:main` (çakışmada `git fetch --depth=50 origin main && git rebase origin/main`).
3. URL: `https://raw.githubusercontent.com/enesuludg6-debug/kontra-gorsel/main/invest/g/<dosya>.jpg` → curl ile 200 dönüyor mu kontrol et.
4. Buffer `create_post`: channelId `6af99a1aece6dfde5fd109c7`, schedulingType `automatic`, mode `shareNow`, text, assets [{image:{url, metadata:{altText}}}], metadata.twitter.isAiGenerated true değil (gerekmez).
5. `invest/DONGU.md`'ye satır ekle: `- HH:MM AUTO: dosya.jpg - özet (kaynaklar) | TÜR`. Commit + push.

## 7. Hata durumu
- Buffer hata verirse 1 kez tekrar dene; yine olmazsa DONGU.md'ye yaz, o tweeti atla.
- Push reddedilirse görselsiz tweet atma; DONGU.md'ye not düş (push yoksa yerel log), çık.
- Buffer `scheduledPosts` limiti 10 (shareNow kuyruğa girmez). Kuyruk dolarsa paylaşma.

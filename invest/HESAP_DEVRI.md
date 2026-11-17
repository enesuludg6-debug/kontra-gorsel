# HESAP DEVRİ — BAŞKA BİR CLAUDE HESABINDA SIFIRDAN KURULUM (kesin kural 17)

Bu dosyayı okuyan oturum, Enes Uludağ'ın X hesabı (@enes1050392, EnesInvestUS) için çalışan otomatik içerik sistemini, Enes'in kendi hesabındaki (A) skill'ler ve tercihler OLMADAN, başka bir Claude hesabında (B) eksiksiz kurar. Her şey bu repoda: kurallar, skill'ler, kart kodu, analiz aracı, kayıtlar.
Her zaman Türkçe yaz. Enes'e soru sorma; eksik bir şey varsa ne yapması gerektiğini TEK CÜMLEYLE söyle ve kalan adımlara devam et.

## 0. Bu hesapta OLMAYANLAR ve yerlerine geçenler
| A hesabında vardı | B hesabında | Ne yapılır |
|---|---|---|
| 3 skill (enes-tweet-turu, enes-bilanco-13f, enes-portfoy-analiz) | yok | `invest/skills/*.md` dosyalarından okunur; Adım 4'te propose_skills ile bu hesaba kaydettirilir. Kaydedilmese de her tur bu dosyaları okuyarak çalışır. |
| Enes'in kalıcı tercihleri (bellek) | yok | Hepsi `invest/DEVIR_TAM.md` ve skill dosyalarında. |
| İzinli alan adları (query1.finance.yahoo.com) | muhtemelen yok | Adım 3 testi; yoksa Enes'e tek cümle. |
| Chrome eklentisi (TradingView) A hesabına giriş yapmış | B'de yok | TradingView opsiyonel; yoksa Yahoo (ta2.py) ile devam. |
| A hesabındaki görevler (sabit 10 görev + zincir) | A'da çalışmaya devam edebilir | ÇİFT TWEET RİSKİ: Adım 2 hesap kilidi çözer. |

## 1. Repo
- `mcp__claude-code-remote__add_repo(owner="enesuludg6-debug", repo="kontra-gorsel", access="push")` (Enes'in ilk mesajındaki açık onayla).
- `git clone --depth 1 https://github.com/enesuludg6-debug/kontra-gorsel /home/claude/kontra-gorsel` (varsa `git pull`), `register_repo_root`.
- `git config user.email "noreply@anthropic.com"; git config user.name "Claude"`; `pip install pillow --break-system-packages` (PIL yoksa).
- SORUN: add_repo "yetki yok / repo erişilemiyor" derse sebep, B hesabına bağlı GitHub kullanıcısının Enes'in reposuna yazma izni olmaması. Enes'e: "GitHub'da kontra-gorsel reposu > Settings > Collaborators'tan arkadaşının GitHub kullanıcısını ekle (ya da bu Claude hesabının Ayarlar > Connectors'ında GitHub'ı kendi GitHub hesabınla bağla), sonra 'tamam' yaz." Push olmadan görsel yayınlanamaz; bu çözülene kadar tweet atma.

## 2. HESAP KİLİDİ (çift tweet engeli) — GÖREV KURMADAN ÖNCE
- `invest/AKTIF_HESAP.md` içindeki `AKTIF: A` satırını `AKTIF: B` yap, Geçmiş'e "GG.AA SS:DD B devraldı" ekle, DONGU.md'ye "HESAP DEVRİ: B aktif" satırı yaz, commit + push.
- Bundan sonra A hesabının görevleri ateşlenirse kilidi görüp hiçbir şey yapmaz ve kendini kapatır (kesin kural 17; A'daki görevlere 17.11'de HESAP=A eklendi). A görevlerinin kilit kontrolü yoksa (eski mesaj) yine de "son otomatik paylaşım 20 dk'dan yeniyse paylaşma" ve DONGU tekrar kontrolü çifti büyük ölçüde engeller; Enes A hesabına tekrar girebilirse oradaki sohbete "durdur" yazsın.
- Bu hesaptaki TÜM görev ve send_later mesajlarına `HESAP=B` yaz.
- Enes A hesabına geri dönerse: A'daki oturum dosyayı `AKTIF: A` yapar, B'nin görevleri kendini kapatır.

## 3. Sistem kontrolü (sonuçları Enes'e tek mesajda bildir)
a) Buffer: araçlar var mı (ToolSearch "buffer list_posts create_post"). `get_account` → organizasyon adı EnesInvestUS / id `6af5719777bce44fa736607b` olmalı; `list_channels` → X kanalı `6af99a1aece6dfde5fd109c7` (@enes1050392) olmalı. BAŞKA bir Buffer hesabıysa (arkadaşının) ASLA paylaşma; Enes'e: "Bu Claude hesabındaki Buffer bağlantısı senin EnesInvestUS hesabın değil; Ayarlar > Connectors'tan Buffer'ı çıkarıp kendi Buffer hesabınla bağla."
b) Kart: `cd /home/claude/kontra-gorsel/invest && python3 -c "import kart2"`; test kartı çiz, Read ile bak.
c) Push + raw: DONGU.md'ye "B oturum kontrol" satırı, push, `curl -s -o /dev/null -w "%{http_code}" https://raw.githubusercontent.com/enesuludg6-debug/kontra-gorsel/main/invest/DONGU.md` → 200.
d) Yahoo: `python3 ta2.py RKLB > /tmp/ta.txt; head -5 /tmp/ta.txt` ("[1H] son ..." gelmeli). Hata/connect_rejected ise Enes'e: "claude.ai > Ayarlar > Yetenekler (Capabilities) > izin verilen alan adlarına query1.finance.yahoo.com ekle." raw.githubusercontent.com 200 vermezse aynı yere raw.githubusercontent.com ve github.com.
e) Zamanlayıcı: `mcp__claude-code-remote__send_later`, `create_trigger`, `list_triggers`, `update_trigger`, `delete_trigger` var mı. Yoksa: "Bu sohbet zamanlayıcıyı desteklemiyor; aynı mesajı claude.ai/code (Claude Code web) oturumunda aç."
f) Web: WebSearch "stock market news today" sonuç vermeli.
g) Chrome: `list_connected_browsers`. Yoksa TradingView atlanır, sorun sayılmaz (Enes isterse: "Chrome'daki Claude eklentisinde bu hesapla oturum aç").
h) Saat: `mcp__claude_ai__current_time` ya da `date`; Türkiye saatiyle (TSİ, UTC+3) çalış; cron'larda MUTLAKA `CRON_TZ=Europe/Istanbul`.

## 4. Skill'leri bu hesaba kaydettir
- `invest/skills/enes-tweet-turu.md`, `enes-bilanco-13f.md`, `enes-portfoy-analiz.md` dosyalarını TAMAMEN oku.
- `propose_skills` ile üçünü TEK çağrıda `kind: new`, `skillMd` = dosya içeriğinin aynısı olarak öner (ad ve açıklama dosyanın başındaki frontmatter'dan). Enes'e: "Çıkan 3 kartı kaydet." Kaydedilmese de her tur bu dosyaları okur; görev mesajlarına "skill yoksa invest/skills/<ad>.md oku" yaz.
- Kural değişirse hem skill (improvement) hem `invest/skills/` kopyası güncellenir.

## 5. Okuma
Devir anında BİR KEZ: `invest/DEVIR_TAM.md` (en üst v8 özeti + KESİN KURALLAR 1-21 + bölümler), `DEVIR_OZET.md`, `ORNEKLER.md`, `DONGU.md` (son 60 satır: son 3 düzen, 13F sırası, bekleyenler, son TEKNIK seviyeleri), `takvim.md`, `performans.md`, `temel_karne.md`, `AKTIF_HESAP.md`, `gundem.md`, `DURUM.md`, `HATA_GUNLUGU.md`.
Sonraki her tur ve görevde (kural 18, tasarruf): yalnız skill + `DURUM.md` + `tail -n 30 DONGU.md` (+ takvim.md). Zincir mesajı DEVIR_TAM kural 18'deki KISA ŞABLON.

## 6. Görevleri kur (HESAP=B, CRON_TZ=Europe/Istanbul, mesajlar bağımsız ve tam)
Önce `list_triggers`: bu hesapta aynı adlı eski görev varsa sil/kapat.
Tekrarlayan (create_trigger, cron):
1. "Sabah kontrolü" her gün 08:55: kilit, DURDUR, zincir canlı mı (değilse kur), takvim.md güncelle, performans.md'ye önceki günün metrikleri.
2. "Key levels + başlıklar" hafta içi 10:25 (kesin kural 13, enes-tweet-turu bölüm 9).
3. "Teknik kontrol (açılış +30 dk)" hafta içi 17:55 ve 4. "Teknik kontrol (kapanış -30 dk)" hafta içi 23:25 (enes-portfoy-analiz; Nasdaq 100 ilk mesaj; tatil/yarım gün kuralı).
5. "Haftalık bilanço takvimi" Pazar 19:55 (kural 16 + 20 + 18: takvim.md + "gelecek hafta" TWEETİ + DONGU'da 7 günden eski satırları invest/arsiv/'e taşıma).
6. "Haftalık performans raporu" Pazar 21:25 (kural 14).
7. "13F serisi başlangıcı" 15 Şubat, 16 Mayıs, 15 Ağustos, 15 Kasım 09:05 (kural 10).
8. "Haftalık özet" Cumartesi 10:55 (kural 19).
9. "Ayın özeti" her ayın 1-7'si 10:55; yalnız ayın ilk ABD işlem günü ve bu ay atılmadıysa çalışır (kural 21).
Görev metinleri için A hesabındaki karşılıkları örnek alınır: DEVIR_TAM bölüm 16-G'deki ID'ler; metinleri DURUM.md + tail 30 DONGU okur ve sonunda DURUM.md'yi günceller. Düzeltme kuralı (kural 21) her turda geçerli.
(Saatler 5 dk erken: sistem yoğunluğundan gecikme payı. İçerikte asıl saatler geçerli.)
Zincir (send_later): "Otomatik paylaşım turu" 20-40 dk rastgele, 09:00-01:00; ilk tur HEMEN (son otomatik paylaşım 20 dk'dan eskiyse).
Tek seferlik: `takvim.md`'de bugün/yarın kalan her olay için hazırlık ve yayın görevleri.
Her görev mesajının başına: "HESAP=B. Önce invest/AKTIF_HESAP.md (AKTIF: B değilse hiçbir şey yapma, bu görevi kapat), git pull, DURDUR kontrolü. Skill: <ad> (yoksa invest/skills/<ad>.md oku)."
Kurulan görev ID'lerini DEVIR_TAM bölüm 16'ya ve DONGU'ya yaz.
SORUN: görev "bilgisayar gerekiyor / onay bekliyor" derse Enes'e: "Telefonda/uygulamada çıkan görev onayını kabul et." Görev oturumu repo yazma izni isterse: "Çıkan repo izni sorusunu onayla."

## 7. Enes'e başlangıç mesajı (tek mesaj)
"Devraldım (B hesabı). Kontroller: Buffer ✓/✗ (EnesInvestUS doğrulandı), repo/push ✓/✗, kart ✓/✗, Yahoo ✓/✗, zamanlayıcı ✓/✗, TradingView ✓/✗ (yoksa Yahoo). Hesap kilidi B'ye çevrildi, eski hesabın görevleri kendini kapatacak. Kurulan görevler: ... İlk tur başladı. Senden beklenen: [varsa tek cümle] + çıkan 3 skill kartını kaydet."

## 8. Olası sorunlar ve önlemler (hepsini düşün)
| Sorun | Belirti | Önlem / çözüm |
|---|---|---|
| Çift tweet (A ve B aynı anda) | DONGU'da aynı konuda iki satır, Buffer'da iki gönderi | Kural 17 kilidi; ayrıca her tur paylaşmadan hemen önce Buffer list_posts son 3 gönderi + DONGU son satır kontrolü; son 20 dk içinde aynı konu varsa atma. |
| Push çakışması (iki oturum aynı anda yazıyor) | push reddi / merge hatası | Her commit'ten önce `git pull --rebase -q`; çakışmada DONGU.md için iki tarafın satırlarını birlikte tut; asla `--force` yok. |
| Yanlış Buffer hesabı | org/kanal id'si farklı | Adım 3a: id'ler eşleşmeden paylaşım YOK. |
| GitHub yazma izni yok | add_repo hatası, push 403 | Adım 1 SORUN satırı. |
| Yahoo kapalı | ta2 connect_rejected | İzinli alan adı; o arada teknik kontrolde "veri yok" de, seviye uydurma. |
| raw URL 404/önbellek | Buffer görseli yükleyemiyor | Push sonrası `sleep 4`, 200 değilse 10 sn daha; hâlâ değilse yeni dosya adıyla tekrar; görselsiz tweet atma. |
| Kullanım limiti (B hesabının planı) | araç çağrıları reddediliyor, oturum duruyor | Gereksiz tekrar araması yapma, ta2 çıktısını özetle; limit dolarsa DONGU'ya "LİMİT" yaz, Enes'e "limit doldu, şu saatte yeniden başlar" de; sabit görevler limit açılınca devam eder. |
| Saat dilimi | görevler 3 saat kayık | Her cron'da CRON_TZ=Europe/Istanbul; send_later'da `[Europe/Istanbul]` biçimi. ABD saat değişimi: 8 Mart 2027'de TSİ = ET + 7 olur, teknik kontroller 17:00/23:00'e, bilanço saatleri 1 saat öne kayar (takvim.md başlığını güncelle). |
| Skill'ler kaydedilmedi | Skill aracında yok | invest/skills/*.md okunarak çalışılır. |
| sec.gov izin sorusu | WebFetch PROVENANCE_REQUIRED | Tekrar deneme; 13f.info / haber kaynakları. Enes'e bir kez "sec.gov iznini onayla" denir. |
| X'e giriş | — | x.com'a ve Enes'in X hesabına HİÇBİR ŞEKİLDE girilmez. |
| Anthropic konusu | — | Adı ve konusu (halka arz dahil) tweete girmez. |
| Kişisel bilgi | — | Enes'in e-postası ve kişisel bilgisi hiçbir dış servise gönderilmez. |
| Logo taşması | Read'de logo kutudan taşıyor | LOGO_BUYUT 1.8, küçültme YOK; başlığı kısalt ya da başka düzen (bilanço rakamı = uclu). |
| Tek kaynak | — | Her rakam 2 kaynak; TEK istisna bilanço RAKAM tweetinde şirket bülteni (kural 16, 10 dk içinde ikinci kaynak teyidi). |
| A hesabına dönüş | Enes "eski hesaba döndüm" der | Bu hesap AKTIF_HESAP'ı A'ya çevirmez; A'daki oturum çevirir. B görevleri kilidi görünce kendini kapatır. B'deki zinciri de durdur. |

## 9. Bitince
DEVIR_TAM.md en üstüne "B AKTİF (GG.AA SS:DD)" satırı, bölüm 16'ya görev ID'leri, bölüm 18'e kayıt; commit + push; temiz klasöre clone ile doğrula.

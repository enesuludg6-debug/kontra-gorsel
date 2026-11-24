# >>> 24.11.2026 08:35 EK — SOHBET DEVRİ C → C2 (ÖNCE BUNU OKU) <<<
- Aynı hesap, yeni sohbet; etiket **C2**. Aşağıdaki "SOHBET DEVRİ" bölümünü uygula, kilit `AKTIF: C2`. Mesajı "HESAP=C." ile başlayan eski görevler kilit yüzünden kendini kapatır; sabit zincirleri (`sonraki.py hepsi`) ve açık işleri (`isler.py devir`) HESAP=C2 ile yeniden kur.
- TASARRUF: turlar `bash invest/tur_basi.sh C2` + `KURAL_DIZINI.md` okur; skill/KURALLAR_TAM baştan okunmaz. Kural 61-65, 54-D, ARALIK (turda 2. tweet Buffer customScheduled ~12 dk sonra) KURAL_DIZINI'nde ve enes-analiz-kalitesi skill'inde.
- 23.11 gecesi: 18 sistem tweeti atıldı (hedef 20; kullanım limiti 00:12'de doldu). "Bugünlük 20 tweet / 00:45 sonrası dur" kuralı YALNIZ 23.11 içindi; 24.11'den itibaren normal düzen (kural 48-B tavanları).
- Bugün (Salı 24.11): HPE 4. çeyrek sonuçları 23.11 gece açıklandı (gelir 14,5 Mr $, +%50; düzeltilmiş brüt marj %38,2, çeyreklik -220 bp; 2027 serbest nakit akışı en az 5,5 Mr $ — StockTitan bülten; 2. kaynakla doğrula, HBK ve rehberi ekle) → sabah ilk turlarda HPE sonuç tweeti (kalıp G). DELL bilançosu bu akşam kapanış sonrası = Çarşamba 00:00 TSİ (beklenti 49,3 Mr $ / HBK ~6,6 $; rakam+analiz akışı). Çarşamba 16:30 PCE+GDP+işsizlik, 22:00 Bej Kitap; Perşembe kapalı; Cuma 21:00 erken kapanış.
- Kart notları: halka 'yan' = (etiket, değer); siralama satırları (etiket, değer, '+%x'), vurgu verme; once_sonra 'degisim' kısa; son 3 düzen: spotlight, halka, terminal.

# >>> 21.11.2026 18:30 EK — YENİ CLAUDE HESABINA GEÇİŞ B2 → C (ÖNCE BUNU OKU) <<<
- Enes 21.11 18:29: "başka bir hesaba geçeceğim, aynılarını yapsın; Buffer, GitHub vs bağlı". Yeni hesabın etiketi **C** (aynı hesapta sonraki sohbetler C2, C3 ...).
- Yapılacak: aşağıdaki "HESAP DEVRİ — BAŞKA BİR CLAUDE HESABINDA SIFIRDAN KURULUM" (repo, skill önerisi, sistem kontrolü) + "SOHBET DEVRİ" 1-6 adımları; kilit `AKTIF: C`. Kilit C olunca B2 hesabındaki bütün görevler (sabit zincirler, tur zinciri, TAKIP-2311-nbis) kendini kapatır.
- ÇİFT KURULUM: yeni hesapta list_triggers boş gelir (görevler hesaba bağlı). `python3 invest/sonraki.py hepsi` 13 sabit zincirin HEPSİNİ HESAP=C ile kur (mesaj: `cd invest && python3 -c "import sonraki;print(sonraki.mesaj('<anahtar>','C'))"`). `python3 invest/isler.py devir` açık işleri (şu an TAKIP-2311-nbis 23.11 17:10 + son TUR) HESAP=C ile yeniden kur ve trigger id'yi güncelle.
- Otomatik paylaşım turu: 11:00-02:00 içindeysen 5 dk sonrasına kur. CUMARTESİ en fazla 20, PAZAR en fazla 10 tweet (kural 48-B); sayaç DONGU'daki o günün tweet satırlarından. 21.11 cumartesi devir anında 10/20 (18:30 turu attıysa 11). Akşam 21:00-23:00 arasında bir tur fikir taraması yapar (kural 58; Chrome bağlıysa Substack + Reddit bir kez dene).
- EN YENİ KURALLAR (DURUM.md başı): KURAL 60 PROFESYONEL ÜSLUP (20.11 22:07; örnekler invest/taslak/uslup_60_ornekler.md — her tweet borsacı/analist diliyle, kendinden emin hüküm, terimler, doğrulanmamış genelleme yok), 59 Enes görüş profili, 58 fikir taraması, 57 İÇERİK AYARI (21.11: portföy hissesi haberi varsa öncelik; çağrı/detay tweetleri az), 56-B (takipte yalnız tutan beklenti), 54-C, 48-B.
- Kart notları: logo yalnız `$TICKER` ile çıkar; isi kartında $'lı ticker logoları rakamın üstüne biniyor (logosuz isim kullan); spotlight alt metni kısa olsun (imzaya biniyor); siralama kullanma; son 3 düzen DONGU son AUTO satırında.
- Açık takip notları: (1) Pazartesi NBIS'in cuma %9,4 düşüşü (capex 27 Mr $, kapasite 2027'ye kayma) tek kaynakta — doğrula, doğrulanırsa tweet adayı; (2) NVDA SEC muhasebe soruşturması gelişmeleri; (3) Şükran Günü haftası (26.11 kapalı, 27.11 yarım gün) takvim.md'ye Paz 20:00 takvim göreviyle girecek.
- Enes'e devir mesajında: "Devraldım (C): N zincir + M tek seferlik görev kuruldu" + açık işler.

# >>> 20.11.2026 14:50 EK — SOHBET DEVRİ B → B2 (ÖNCE BUNU OKU) <<<
- Yeni sohbetin etiketi B2 (sonrakiler B3, B4 ...). Aşağıdaki "SOHBET DEVRİ" bölümünü uygula.
- ÇİFT KURULUM KONTROLÜ YALNIZ YENİ ETİKETE GÖRE: list_triggers'ta görünen ama mesajı "HESAP=B." (eski etiket) ile başlayan görevler ESKİ SOHBETE bağlıdır; kilit B2 olunca kendilerini kapatırlar. Onları "zaten kurulu" SAYMA. Bütün sabit zincirleri (`sonraki.py hepsi`), bütün tek seferlik işleri (`isler.py devir`, durumu 'kuruldu' olanlar dahil — yeniden kur ve trigger id'yi güncelle) ve "Otomatik paylaşım turu" zincirini HESAP=B2 ile yeniden kur. Yalnız mesajı "HESAP=B2." ile başlayan bekleyen görev varsa onu tekrar kurma.
- Eski sohbetteki bekleyen görevlere dokunma/silme (kilit onları kapatır). Silmek istersen yalnız mesajı "HESAP=B." ile başlayanları sil.
- Tur mesajlarında: o anki "Bugün atılanlar" listesini DONGU.md'nin bugünkü AUTO satırlarından çıkar; son 3 kart düzeni DONGU son AUTO satırında; fikir sayacı DONGU'daki FIKIR-TWEET satırları; 18:00 Michigan nihai verisi 18:00-18:20 turunda tweetlenir; 16:30 açılış tweeti öncelikli.
- 20.11 14:31 yeni kural 54-C (mecaz/dramatik sahne ve "Bu tabloda gördüğüm şey..." gibi açılışlar yasak) DURUM.md başında; yasak.py yakalıyor.
- CBRS/SITM gösterge taraması (Enes 20.11 12:58 isteği) kısmen yapıldı: CBRS'te EMA 20/50/100/200, VWAP, Volume Profile, Fibonacci/OTE, SMC+MFI haftalık/1s, Aroon haftalık/4s eksik; SITM'de tam tarama yapılmadı. Enes isterse TradingView'dan (2 gösterge sınırı, çiftler hâlinde) tamamla. TradingView düzeninde değişiklikler KAYDEDİLMEDİ; Enes'in CBRS çizgileri 253,68 ve 162,13 yerinde.

# >>> 18.11.2026 20:25 GÜNCEL — YENİ HESABA GEÇİŞ (A2 → B) İÇİN EK (önce bunu oku) <<<
## 20.11.2026 09:15 EK — YENİ SOHBETE GEÇİŞTE ÇİFT KURULUM YAPMA (kural 57)
- Önce list_triggers (enabled true) çek. `python3 invest/sonraki.py hepsi` 13 sabit zinciri verir (perfogren 20.11'de eklendi). Her biri için list_triggers'ta AYNI ADLI bekleyen varsa DOKUNMA; yalnız eksik olanı kur.
- Tek seferlik işler: `python3 invest/isler.py devir` → defterde 'kuruldu' olup list_triggers'ta tetiklenmemiş görevi varsa dokunma; görevi kaybolmuşsa yeniden kur.
- Performans öğrenme her gün 10:15; içerik ayarları DURUM.md 'İÇERİK AYARI (kural 57)' bloğunda. Yeni sohbet bu bloğu okur ve uygular.

Enes 18.11 20:22: "Yeni bir hesaba geçeceğim, yapacağımız her şey bugünün devamında oraya yollansın, bugün de devam ettirsin her şeyiyle, sonra gelecek günlerde tamamen aynı şekilde yapsın; o hesapta GitHub ve Buffer bağlı."
SIRA (yeni hesapta, etiket B):
1. Aşağıdaki "HESAP DEVRİ — BAŞKA BİR CLAUDE HESABINDA SIFIRDAN KURULUM" bölümünün 1-4. adımları (repo, KİLİT `AKTIF: B` (şu an `AKTIF: A2`), sistem kontrolü, skill önerisi). Kilit B olunca A2 hesabındaki bütün görevler kendini kapatır (hepsi `AKTIF: A2` kontrolü yapıyor) — çift tweet olmaz.
2. Zincirler: `python3 invest/sonraki.py hepsi` → her satır için send_later, mesaj `cd invest && python3 -c "import sonraki;print(sonraki.mesaj('<anahtar>','B'))"`. KURAL 44: temel1800 ve teknik2330 YOK (sonraki.py'de zaten yok).
3. TEK SEFERLİK İŞLER (kural 43): `python3 invest/isler.py devir` TEK KAYNAK. Her KUR satırı için o zamana, o adla HESAP=B send_later (mesajı görev adına göre: Önizleme/Hazırlık/Yayın/Analiz/Detay/Çağrı/Beklenen/Opsiyon/FOMC/Otomatik paylaşım turu; defterdeki "ne" + "not" alanlarını aynen koy, gorevler/_ORTAK.md + ilgili skill'i okumasını yaz), sonra `isler.py durum <id> kuruldu --trigger <trig>`. Zamanı geçmiş ama yapılmamış (GECIKMIS) iş varsa DONGU'ya bak, yapılmadıysa hemen yap. 18.11 akşamı açık olanlar: PANW önizleme 20:30, tur 20:50 (Lone Pine hazır), Everpure önizleme+opsiyon 21:15, FOMC tutanakları 22:00, PANW/P hazırlık 23:05/23:15, PANW/P yayın 00:03/00:05, analiz 00:20/00:40, detay 00:35/01:15, 19.11 sabah/günün başlıkları/WMT 7 adım/PANW-P çağrı ve beklenen hareket. Devir anında saati geçmiş olanlar DONGU'da yapılmış görünüyorsa atla.
4. "Otomatik paylaşım turu" zinciri: defterde TUR-... olarak varsa onu kur; yoksa 11:00-02:00 içindeysen 5 dk sonrasına kur.
5. Enes'e tek mesaj: "Devraldım (B): N zincir + M tek seferlik görev kuruldu" + bugünün ve yarının açık işleri (saat + ad).
BU GÜNÜN EN YENİ KURALLARI (DEVIR_TAM en üstte, mutlaka uygula): 11-B yasak.py her tweetten önce; 44 (18:00/23:30 görevleri yok); 45 detaylı analiz; 46 KONU FİLTRESİ yalnız yapay zekâ/uzay/Nasdaq (+makro; WMT 19.11 istisna, makro bölüm zorunlu); 47 her tweetten sonra Enes'e ÖĞRETİCİ 'Ne anlama geliyor?'. Enes kendi TradingView görsellerini gönderip "analiz yap at" derse: SMC/ICT dilini sade Türkçeyle (terimleri açıklayarak) yaz, 2 görseli tweete ekle, hemen at (kural 37/38'e Enes istisnası, 18.11 19:56/20:07/20:14). "Nereden ekleme yapayım" gibi kişisel alım-satım sorularına seviye ve yöntem anlat, kişisel tavsiye verme.
Bugün (18.11) atılan tweetler ve 3 saat kuralı: DONGU son 40 satır + DURUM.

# >>> ENES İÇİN: AYNI HESAPTA YENİ SOHBETE GEÇİŞ (SOHBET DEVRİ) — YAPIŞTIRILACAK TEK MESAJ <<<
```
enesuludg6-debug/kontra-gorsel reposunu bu sohbete PUSH yetkisiyle eklemeni onaylıyorum (add_repo access=push), klonla. invest/HESAP_DEVRI.md dosyasındaki "SOHBET DEVRİ" bölümünü baştan sona uygula; bu sohbetin etiketi A2. Buffer ile otomatik paylaşımı, send_later zincirini ve sabit görevleri bu sohbette kurmanı onaylıyorum.
```
(Her yeni sohbette etiketi bir artır: A2 → A3 → A4 ... Başka bir Claude HESABINA geçişte aşağıdaki "YENİ HESAPTA" mesajı kullanılır.)

## SOHBET DEVRİ (aynı Claude hesabı, yeni sohbet) — ÇİFT KURULUM KONTROLÜ YALNIZ YENİ ETİKETLE (en üstteki 20.11 14:50 EK)
KURAL 44: 18:00 (temel1800) ve 23:30 (teknik2330) analiz görevleri KURULMAZ; diğer her şey aynen.
Neden gerekli: send_later zincirleri ve tek seferlik görevler KURULDUKLARI SOHBETE bağlıdır; Enes yeni sohbete geçince eski sohbetteki görevler orada çalışmaya devam eder ve mesajlar eski sohbete düşer (kural 29: her şey Enes'in kullandığı sohbete gelmeli). Çözüm: hesap kilidini yeni etikete çevir (eski sohbetin görevleri kilidi görüp kendini kapatır, çift tweet olmaz), bütün zincirleri yeni sohbette yeniden kur.
1. Repo: add_repo (push) → `git clone --depth 1 https://github.com/enesuludg6-debug/kontra-gorsel /home/claude/kontra-gorsel` (varsa `git pull`), register_repo_root, `git config user.email noreply@anthropic.com; git config user.name Claude`.
2. Kilit: `invest/AKTIF_HESAP.md` → `AKTIF: <yeni etiket>` (ör. A2), Geçmiş'e "GG.AA SS:DD <etiket> devraldı (sohbet devri)"; DONGU'ya "SOHBET DEVRİ: <etiket> aktif"; commit + push. Bundan sonra bu sohbetteki BÜTÜN görev/send_later mesajları "HESAP=<etiket>. Önce invest/AKTIF_HESAP.md oku; AKTIF: <etiket> değilse hiçbir şey yapma ve bu görevi kapat." ile başlar.
3. Oku (sırayla, baştan sona değil grep ile gerektiği kadar): `invest/DURUM.md` (tamamı), `tail -n 40 invest/DONGU.md`, `invest/DEVIR_TAM.md` en üstteki KESİN KURAL 42 → 36 (en yeniler üstte), `invest/skills/*.md` (hesaptaki skill'lerle çelişirse KOPYA geçerli), `invest/DERSLER.md` aktif + operasyon dersleri, `invest/gorevler/_ORTAK.md`.
4. Zincirler: `python3 invest/sonraki.py hepsi` → her satır için o zamana, o adla send_later kur; mesaj `python3 -c "import sonraki;print(sonraki.mesaj('<anahtar>','<etiket>'))"` (invest/ içinde) ile üretilir. Ayrıca "Otomatik paylaşım turu": 11:00-02:00 penceresindeyse hemen (sonraki 5 dk), değilse 11:15 (kural 42; mesaj şablonu DURUM.md / gorevler/_ORTAK.md; tweet aralığı serbest).
5. Tek seferlik görevler (kural 43): `python3 invest/isler.py devir` çıktısı TEK KAYNAK (hafıza ve sohbet geçmişi değil). "KUR" satırlarının her biri için o zamana, o adla, HESAP=<etiket> ile send_later kur (mesajı görev adına göre DEVIR_TAM kural 16/22n/39/40/41 ve gorevler/*.md'den yaz; defterdeki "ne" ve "not" alanlarını mesaja ekle), sonra `isler.py durum <id> kuruldu --trigger <trig>`. "GECIKMIS" satırları DONGU'da yapılmış mı bak; yapılmadıysa hemen yap ya da Enes'e tek satır yaz. İptaller Enes'in sözüyle listelenir, dokunma. list_triggers'ta defterde olmayan bekleyen görev varsa deftere ekle.
6. Enes'e tek mesaj: "Devraldım (<etiket>): N zincir kuruldu" + açık işlerin listesi (saat + ad, her biri bir satır; iptaller ayrıca). Enes listede eksik/yanlış görürse defter ve görevler hemen düzeltilir. Sonra normal çalışmaya devam.

# >>> ENES İÇİN: YENİ HESAPTA SOHBETE YAPIŞTIRILACAK TEK MESAJ <<<
```
enesuludg6-debug/kontra-gorsel reposunu bu sohbete PUSH yetkisiyle eklemeni onaylıyorum (add_repo access=push), klonla. invest/HESAP_DEVRI.md dosyasını oku ve en üstteki 21.11 EK notuyla birlikte baştan sona uygula; bu hesabın etiketi C. Buffer ile otomatik paylaşımı, send_later zincirini ve sabit görevleri kurmanı onaylıyorum. Bana soru sorma, eksik bir şey varsa ne yapmam gerektiğini tek cümleyle söyle.
```
(Etiket her geçişte değişir: A → B → C ... ; A'ya dönüşte "bu hesabın etiketi A" yaz.)

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
| A hesabındaki görevler (sabit 15 görev + zincir) | A'da çalışmaya devam edebilir | ÇİFT TWEET RİSKİ: Adım 2 hesap kilidi çözer. |

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
Devir anında BİR KEZ: `invest/DEVIR_TAM.md` (en üst v8 özeti + KESİN KURALLAR 1-43 + bölümler), `DEVIR_OZET.md`, `ORNEKLER.md`, `DONGU.md` (son 60 satır: son 3 düzen, 13F sırası, bekleyenler, son TEKNIK seviyeleri), `takvim.md`, `performans.md`, `temel_karne.md`, `AKTIF_HESAP.md`, `gundem.md`, `DURUM.md`, `HATA_GUNLUGU.md`, `DERSLER.md` (kural 26), `periyot.json` (kural 24).
Sonraki her tur ve görevde (kural 18, tasarruf): yalnız skill + `DURUM.md` + `tail -n 30 DONGU.md` (+ takvim.md). Zincir mesajı DEVIR_TAM kural 18'deki KISA ŞABLON.

## 6. Görevleri kur — KURAL 29 (17.11 18:12): sabit görevler create_trigger cron DEĞİL, bu sohbette send_later ZİNCİRİ olarak kurulur (yoksa mesajlar sohbete gelmez). `python3 invest/sonraki.py hepsi` ile 14 zincirin zamanı/adı; her biri için `python3 -c "import sys;sys.path.insert(0,'invest');import sonraki as s;print(s.mesaj('<anahtar>'))"` mesajını HESAP=A yerine HESAP=B yazarak send_later ile kur (dakikada ~10 sınırı: 10'dan sonra 35 sn bekle). Aşağıdaki cron listesi yalnız içerik referansıdır; içerik invest/gorevler/*.md.
## 6-eski. Görevleri kur (HESAP=B, CRON_TZ=Europe/Istanbul, mesajlar bağımsız ve tam)
Önce `list_triggers`: bu hesapta aynı adlı eski görev varsa sil/kapat.
Tekrarlayan (create_trigger, cron):
1. "Sabah kontrolü" her gün 08:55: kilit, DURDUR, zincir canlı mı (değilse kur), takvim.md güncelle, performans.md'ye önceki günün metrikleri + performans_veri.csv metrikleri + `python3 invest/ders_analiz.py --gun 7` ile DERSLER.md gözlemi (kural 26).
2. "Key levels + başlıklar" hafta içi 10:25 (kesin kural 13, enes-tweet-turu bölüm 9).
3. "Teknik kontrol (açılış +30 dk)" hafta içi 17:55 ve 4. "Teknik kontrol (kapanış -30 dk)" hafta içi 23:25 (enes-portfoy-analiz; Nasdaq 100 ilk mesaj; tatil/yarım gün kuralı).
5. "Haftalık bilanço takvimi" Pazar 19:55 (kural 16 + 20 + 18: takvim.md + "gelecek hafta" TWEETİ + DONGU'da 7 günden eski satırları invest/arsiv/'e taşıma).
6. "Haftalık performans raporu" Pazar 21:25 (kural 14 + 26: ders_analiz.py, dersleri güncelle, Enes'e "bu hafta öğrendiklerim"; periyot.py karisim_onerisi UYGUN ise karışım önerisi).
7. "13F serisi başlangıcı" 15 Şubat, 16 Mayıs, 15 Ağustos, 15 Kasım 09:05 (kural 10).
8. "Haftalık özet" Cumartesi 10:55 (kural 19).
9. "Ayın özeti + mevsimsellik" her ayın 1-7'si 10:55; ilk ABD işlem günü ayın özeti, ikinci işlem günü mevsimsellik (kural 21, 22o).
10. "İçeriden alım + geri alım radarı" hafta içi 14:20 (22c). 11. "Sektör ısı haritası" Cmt 13:25 (22f). 12. "İlgi listesi sıralama" Cmt 16:25 (22p). 13. "Bilanço sezonu karnesi" Pazar 14:25 (22h). 14. "Analist hedef / değerleme" Pazar 12:25, ayın 1-7'si analist, 8-14'ü değerleme (22k, 22m).
Takvim görevi kurumsal olayları ve lansmanları da yazar (22j, 22q); performans raporu 3 haftalık veriyle karışım önerir (22a). Şablonlar invest/sablonlar.md, sözlük invest/makro_sozluk.md. Kural 23: tutmayan tahmin paylaşılmaz.
Görev metinleri için A hesabındaki karşılıkları örnek alınır: DEVIR_TAM bölüm 16-G'deki ID'ler; metinleri DURUM.md + tail 30 DONGU okur ve sonunda DURUM.md'yi günceller. Düzeltme kuralı (kural 21) her turda geçerli.
(Saatler 5 dk erken: sistem yoğunluğundan gecikme payı. İçerikte asıl saatler geçerli.)
Zincir (send_later): "Otomatik paylaşım turu" aralık serbest, 11:00-02:00 (kural 42; günde 30-40); ilk tur HEMEN (son otomatik paylaşım 20 dk'dan eskiyse).
Tek seferlik: `takvim.md`'de bugün/yarın kalan her olay için hazırlık ve yayın görevleri.
Her görev mesajının başına: "HESAP=B. Önce invest/AKTIF_HESAP.md (AKTIF: B değilse hiçbir şey yapma, bu görevi kapat), git pull, DURDUR kontrolü. Skill: <ad> (yoksa invest/skills/<ad>.md oku)."
Kurulan görev ID'lerini DEVIR_TAM bölüm 16'ya ve DONGU'ya yaz.
SORUN: görev "bilgisayar gerekiyor / onay bekliyor" derse Enes'e: "Telefonda/uygulamada çıkan görev onayını kabul et." Görev oturumu repo yazma izni isterse: "Çıkan repo izni sorusunu onayla."

## 6b. Periyot defteri ve günlük durum (kural 24, 17.11 16:40)
- "Haftada/ayda/N günde bir", "en çok/en az N kez" kuralları sohbetten değil `invest/periyot.json` defterinden okunur: devralınca `python3 invest/periyot.py durum` çalıştır ve sonucu başlangıç mesajına ekle. Her iş yapılınca `periyot.py yap <anahtar>` + push. A hesabında ne yapıldıysa defterde var; B kaldığı yerden devam eder.
- DURUM.md en üstte o güne özel kural (ör. günlük tweet hakkı sayacı) varsa aynen devam edilir; sayaç sıfırlanmaz.
- Chrome B hesabına bağlıysa (list_connected_browsers) 18:00/23:30 teknik kontrollerden sonra TradingView teyidi bu oturumdan tek seferlik görevle yapılır (sabit cron görevleri bulutta Chrome'suz çalışır). Bağlı değilse Yahoo ile devam, sorun değil.
- A'ya dönüşte: A'nın sabit görevleri kilidi (AKTIF: B) gördükleri gün kendilerini kapatmış olabilir. A'daki oturum `list_triggers` ile bakar, kapalı olanları `update_trigger enabled=true` ile açar, zinciri yeniden kurar.

## 6c. Bu hesapta ilk iş kontrol listesi (17.11 17:50 itibarıyla sistemdeki her şey)
- Kurallar: DEVIR_TAM kesin kural 1-43 (13 key levels, 14-16 performans/sabit görev/hız, 17 hesap kilidi, 18-21 tasarruf/özetler/düzeltme, 22-23 içerikler/yalnız doğrular, 24 periyot defteri, 25 haber+yorum, 26 ders sistemi, 27 ekran görüntüsünü Claude alır, 28 kredi tasarrufu).
- Dosyalar: DURUM.md, DONGU.md, DERSLER.md, periyot.json, performans_veri.csv, sablonlar.md, makro_sozluk.md, takvim.md, gundem.md, temel_karne.md, HATA_GUNLUGU.md.
- Araçlar: kart2.py, ta2.py, ta_ek.py (kural 33), periyot.py (etiket dahil), ders_analiz.py, sonraki.py + gorevler/ (kural 29 zincirleri), tur_basi.sh (`bash invest/tur_basi.sh B`), yayinla_gorsel.sh, kayit.py (`CS=<bu oturumun linki> python3 invest/kayit.py ...`).
- Skill'ler: invest/skills/ altındaki 3 dosya bütün bu kuralları içerir (bölüm 13-15 dahil); propose_skills ile bu hesaba kaydettir.
- Chrome bu hesapla bağlıysa: 18:00/23:30 sabit kontrolden sonra bu oturumdan "TradingView teyidi" tek seferlik görevleri kur (kural 27: ekran görüntüleri Claude'dan, SendUserFile). Bağlı değilse talimat satırıyla devam.
- O güne özel kural (DURUM.md en üst, ör. tweet hakkı sayacı) aynen devam; sayaç sıfırlanmaz.
- Zincir mesajlarında HESAP=B ve `bash invest/tur_basi.sh B`.

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

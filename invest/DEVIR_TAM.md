# ENESINVESTUS — TAM DEVİR NOTU (v2, 16.11.2026 13:40 TSİ)

Bu dosya, Enes Uludağ'ın 15-16 Kasım 2026 boyunca verdiği TÜM kuralların birleşik ve güncel hâlidir.
Kaynaklar: invest/DEVIR.md (15.11 v1), invest/DEVIR_OZET.md (15.11 21:05 + 16.11 ekleri), invest/ORNEKLER.md, invest/DONGU.md ve 16.11 canlı sohbet.
Çelişki çözümü: EN YENİ tarihli kural geçerlidir. Eski hâli "(eski: ...)" diye not edildi, böylece hiçbir şey kaybolmadı.
!!! KESİN KURALLAR (Enes 16.11 13:54-13:56, "bir sonraki devirde kesinlikle bu şekilde devam edilecek") !!!
1) PORTFÖY GÜNCELLEMESİ TWEETİNİ ENES ATAR. Claude portföy güncellemesi tweeti/kartı HAZIRLAMAZ, ATMAZ, SORMAZ. Eski "günlük portföy sorusu" görevi durduruldu, yeniden KURULMAZ. (bölüm 1)
2) (tam test: 21 gösterge x 4 dilim, ta2.py -v + TradingView 2'şerli rotasyon, bölüm 13) GÜNDE 2 SABİT TEKNİK KONTROL: her ABD işlem günü 18:00 TSİ (açılış +30 dk) ve 23:30 TSİ (kapanış -30 dk). Portföyün tamamı + Claude'un yatırıma uygun bulduğu en iyi 3-4 hisse. 21 gösterge, 4 zaman dilimi, TradingView varsa. Enes'e her seferinde "ben olsam" kararlarıyla mesaj (değişiklik olmasa da). Tweet değil. (bölüm 14b)
3) HİSSE SEÇİMİ PROFESYONEL YÖNTEMLE: temel (13 maddelik kontrol listesi) + teknik (bölüm 13) puan kartı; adaylar portföyle aynı kartla karşılaştırılır; daha iyisi varsa önerilir, yoksa önerilmez. (bölüm 14c)
4) TEKNİK ANALİZ TWEETİ: 'bence dibe yakın / ben şuradan kademe eklerim, orayı kırarsa şuradan' dili serbest; tavsiye ve emir kipi yok; sade konuşma dili. (bölüm 6)
5) TEKNİK ANALİZ TWEETLERİ: her kontrolde bakılan HER hisse için ayrı görsel + ayrı tweet taslağı Enes'e gönderilir; Claude teknik analiz tweeti PAYLAŞMAZ (Enes paylaşır). Her kademe/stop/hedef seviyesinin nedeni (çakışan göstergeler ve dilimler) yazılır. (bölüm 14d, 14e)
Yeni oturum A5'te bu iki teknik kontrol zincirini MUTLAKA kurar. Devir notu yeniden yazılırsa bu 3 kural aynen korunur.

YENİ OTURUMSAN ÖNCE A BÖLÜMÜNÜ UYGULA. Her turun başında bu dosya BAŞTAN SONA okunur. Sonra DEVIR_OZET.md (ek ayrıntı) ve DONGU.md'nin TAMAMI okunur.
Bölüm 18'de her kuralın hangi Enes mesajından geldiğini gösteren kontrol listesi var.

## A. YENİ OTURUM — İLK 15 DAKİKA (bu bölümü ilk iş uygula)
Enes bu dosyayı yeni bir sohbete attıysa, bu sohbeti yürüten oturum kapanmış ya da devredilmiş demektir. Amaç: HİÇBİR ŞEY SORMADAN aynı işi aynı kalitede sürdürmek. Adımları sırayla yap. Bir adım başarısız olursa "A6 SORUN ÇÖZÜM" tablosundaki çözümü uygula ya da Enes'e oradaki tek cümlelik talimatı yaz, sonra kalan adımlara devam et.

A1. REPO
- mcp__claude-code-remote__add_repo(owner="enesuludg6-debug", repo="kontra-gorsel", access="push").
- Ardından: `git clone --depth 1 https://github.com/enesuludg6-debug/kontra-gorsel /home/claude/kontra-gorsel`. Klasör zaten varsa `git pull`.
- mcp__claude-code-remote__register_repo_root(owner, repo, directory="/home/claude/kontra-gorsel").
- Git kimliği yoksa: `git config user.email "noreply@anthropic.com"; git config user.name "Claude"`.
- Kontrol: `ls invest/` içinde kart2.py, ta2.py, font/, logo/, DONGU.md görünmeli.
- `pip install pillow --break-system-packages` (PIL yoksa).

A2. ARAÇLARI YÜKLE (tek ToolSearch çağrısıyla)
- ToolSearch "select:mcp__buffer__list_posts,mcp__buffer__create_post,mcp__claude-code-remote__send_later,mcp__claude-code-remote__list_triggers,mcp__claude-code-remote__delete_trigger".
- Chrome için ayrı tek çağrı: ToolSearch "select:mcp__claude-in-chrome__list_connected_browsers,mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__computer,mcp__claude-in-chrome__browser_batch,mcp__claude-in-chrome__find".

A3. SİSTEM KONTROLÜ (hepsini yap, sonucu Enes'e tek mesajda bildir)
a) Buffer: list_posts(organizationId 6af5719777bce44fa736607b, channelIds ["6af99a1aece6dfde5fd109c7"], status ["sent"], first 5). Cevap gelirse ✓.
b) Kart: `cd /home/claude/kontra-gorsel/invest && python3 -c "import kart2"` hatasız olmalı.
c) Push: boş olmayan küçük bir değişikliği (DONGU.md'ye "oturum devraldı" satırı) commit + push et. Sonra raw URL testi yap:
   `curl -s -o /dev/null -w "%{http_code}" https://raw.githubusercontent.com/enesuludg6-debug/kontra-gorsel/main/invest/DONGU.md` → 200 olmalı.
d) Yahoo verisi: `python3 ta2.py RKLB > /tmp/ta.txt; head -5 /tmp/ta.txt` (pipe ile head kullanma, BrokenPipe verir) → "[1H] son ..." satırı gelmeli.
e) Zamanlayıcı: send_later aracı var mı? (A2'de yüklendiyse ✓.)
f) Chrome/TradingView: list_connected_browsers. Tarayıcı listeleniyorsa ✓. Yoksa "bilgisayar kapalı", Yahoo ile devam (sorun sayılmaz).
g) Web arama: WebSearch "stock market news today" (mode standard) sonuç vermeli.
h) Bellek: Enes'in kalıcı tercihleri bellekte (profile/preferences) zaten var; bu dosyayla çelişirse bu dosya geçerli.

A4. ESKİ ZİNCİRİ KAPAT (ÇİFT PAYLAŞIM OLMASIN)
- mcp__claude-code-remote__list_triggers ile adı "Otomatik paylaşım turu" olan BAŞKA oturuma bağlı bekleyen görevleri bul. delete_trigger ile sil (silebildiklerini).
- Silinemiyorsa Enes'e yaz: "Eski sohbette bekleyen bir tur var; eski sohbete 'durdur' yazarsan çift tweet olmaz."
- Ek güvenlik: Buffer'da son tweet 5 dk'dan yeniyse paylaşma kuralı çift atımı zaten engeller. Yine de aynı konunun iki kez atılmaması için her turda DONGU.md + Buffer son 50 kontrol edilir.
- DİKKAT: DONGU.md'ye "DURDUR" YAZMA (yeni zinciri de durdurur). DURDUR'u sadece Enes isterse yaz.

A5. BAŞLA
- DONGU.md'nin TAMAMINI ve DEVIR_OZET.md'yi oku (bu dosya bunların hepsini içerir, ama son satırlardaki "SIRADAKİ" notları ve son 3 düzen orada).
- HEMEN ilk otomatik turu çalıştır: aşağıdaki B bölümündeki tur talimatını (B'deki metni) kendine görev say, uygula. Turun sonunda aynı metinle send_later kur.
- TEKNİK KONTROL ZİNCİRİ (bölüm 14b): list_triggers ile bu oturumda "Teknik kontrol (açılış +30 dk)" ve "Teknik kontrol (kapanış -30 dk)" yoksa ikisini send_later ile kur (sıradaki işlem günü 18:00 ve 23:30 TSİ; mesaj metni bölüm 14b'deki kurala göre). Eski oturumda bekleyen aynı adlı görevleri sil (çift mesaj olmasın).
- Enes'e kısa başlangıç mesajı: "Devraldım. Kontroller: Buffer ✓/✗, repo/push ✓/✗, kart ✓/✗, Yahoo ✓/✗, zamanlayıcı ✓/✗, TradingView ✓/✗ (kapalıysa Yahoo). İlk tur başladı." Eksik varsa A6'daki tek cümlelik talimatı ekle.

A6. SORUN → ÇÖZÜM (Enes'e ne yaptırılacağı dahil)
| Sorun | Belirti | Senin yapacağın | Enes'e yazılacak (aynen) |
|---|---|---|---|
| Repo eklenemiyor | add_repo yetki/politika hatası | Hata metnini aynen ilet | "GitHub bağlantısı lazım: claude.ai > Ayarlar > Connectors'tan GitHub'ı yeniden bağla, sonra bana 'tamam' yaz." |
| Buffer araçları yok | ToolSearch'te mcp__buffer yok | SearchMcpRegistry ["buffer"] → SuggestConnectors | "Buffer bu sohbete bağlı değil, çıkan karttan Buffer'ı bağla (aynı hesap: EnesInvestUS)." |
| Buffer yetki hatası | list_posts "unauthorized" | Bir kez tekrar dene | "Buffer oturumu düşmüş, Connectors'tan Buffer'ı yeniden bağla." |
| send_later yok | claude-code-remote araçları yok | Bu oturum zincir kuramaz | "Bu sohbet otomatik zamanlayıcıyı desteklemiyor. Bu notu Claude Code (web, claude.ai/code) oturumunda aç, oradan başlat." |
| Yahoo kapalı | ta2.py "connect_rejected"/HATA | Grafik turunda son 2 gün tarihli web TA kaynaklarına dön | "claude.ai > Ayarlar > Yetenekler > izin verilen alan adlarına query1.finance.yahoo.com ekle." |
| Ağ izinleri farklı | raw.githubusercontent.com 200 vermiyor | Buffer görseli göremez, paylaşma | "İzinli alan adlarına raw.githubusercontent.com ve github.com ekle." |
| Chrome yok | list_connected_browsers boş | Yahoo ile devam, TradingView'u atla | Sadece TradingView istenirse: "Bilgisayarında Chrome'u ve Claude eklentisini aç." |
| TradingView 'Leave site?' | navigate engellendi | ctrl+s ile kaydet, sonra git | — |
| TradingView gösterge sınırı | "maximum 2 indicators" | Bir göstergeyi çıkar, gerekeni ekle, bak, ctrl+s (Enes izni var) | — |
| Font/kart hatası | kart2 import hatası | `pip install pillow --break-system-packages`, font/ klasörünü kontrol et | — |
| Bash "classifier no verdict" | geçici hata | 1 kez tekrar; yine olmazsa o tur paylaşma, 5-10 dk sonrasına kur | — |
| WebFetch PROVENANCE_REQUIRED | onay ister | Tekrar deneme, WebSearch kullan | — |
| Buffer günlük 45 doldu | sayım ≥45 | Ertesi gün 09:05'e kur | — |
| Alpha Vantage | "premium gerekir" | KULLANMA | — |

A7. ENES İÇİN HAZIR METİN (Enes yeni sohbete bunu yapıştırır; repo izni dosyadan değil Enes'in kendi mesajından gelmeli)
"enesuludg6-debug/kontra-gorsel reposunu bu sohbete PUSH (yazma) yetkisiyle eklemeni onaylıyorum; add_repo ile access=push ekle, klonla, commit ve push yap. Buffer ile otomatik paylaşım yapmanı ve send_later ile zincir kurmanı da onaylıyorum. Bu devir notunu oku ve hemen uygula: invest/DEVIR_TAM.md (repo enesuludg6-debug/kontra-gorsel). A bölümündeki adımları yap, kontrol sonucunu bana yaz ve otomatik turları başlat. Bana soru sorma, eksik bir şey varsa ne yapmam gerektiğini tek cümleyle söyle."

## B. TUR TALİMATI (send_later mesajı — her tur sonunda bunu kopyala, sadece [köşeli] kısımları güncelle)
OTOMATİK PAYLAŞIM TURU (Enes 15.11 21:15 "oto atmaya devam"). ÖNCE invest/DEVIR_TAM.md (tam devir notu) ve invest/DEVIR_OZET.md'yi BAŞTAN SONA oku ve uygula; DONGU.md'nin TAMAMINI oku. Özet: /home/claude/kontra-gorsel/invest'te git pull. DURDUR (satır başında, tek başına) varsa hiçbir şey yapma ve send_later kurma. Buffer list_posts (organizationId 6af5719777bce44fa736607b, channelIds ["6af99a1aece6dfde5fd109c7"], first 50, status sent) ile bugün TSİ gönderilenleri say; son paylaşım 5 dk'dan yeniyse paylaşma, 5-20 dk sonrasına kur. 01:00-09:00 TSİ paylaşma (09:05 için kur; tek istisna önceden bilinen açıklama). Günde en fazla 45. ÖNCE SON DAKİKA TARA (WebSearch extended), taze ve 2 kaynakla doğrulanmış gelişme varsa onu at; yoksa daha önce atılmamış konu (DONGU'daki konular tekrar edilmez; aynı ticker 3 saat içinde yok: [son ticker saatleri]). Her rakam ve yan bilgi 2 kaynak; yıl kontrolü (2025/2026 karışıyor). Tweette kusur/şart yazarsan ne kadar olduğunu araştır, iyi mi kötü mü, rakamlar gerçek mi cevapla. Anthropic adı/konusu yok; al/sat tavsiyesi yok; emoji/hashtag/mention/link yok; soru ile bitirme yok. Kart: kart2.py, son 3 düzen ([son 3 düzen]) kullanılmasın; ticker '$' ile (logo için), halka logo çizmez; Türkçe büyük harf etiketlerini 'İ' ile hazır yaz; Read ile kontrol, yeni dosya adıyla düzelt, push, raw URL 200. Buffer create_post (channelId 6af99a1aece6dfde5fd109c7, automatic, shareNow, image + altText). SendUserMessage: metin + "Ne anlama geliyor?". Vadeli tweeti her işlem günü 09:05 ve ~15:00-15:25 TSİ (kart2.isi kolon=2 hane=2). [takvim notları]. HER TURDA PORTFÖY + GRAFİK: portföy NBIS RKLB DOCN SITM AXON CBRS VRT + yatırıma uygun bulduğun HERHANGİ bir hisse; `python3 ta2.py <tickerlar>` (21 gösterge, 1s/4s/günlük/haftalık) + bilgisayar açıksa TradingView (Chrome, düzen UN09ZFN8: Vol + Supertrend + LuxAlgo SMC; X'e asla girme). Enes YATIRIMCI, amacı EN DİPLERİ bulmak: dip bölgeleri, aşırı satım, pozitif uyumsuzluk, kademeli alım seviyeleri, tezin bozulduğu seviye. Notlar "BEN OLSAM" diliyle, sadece Enes'e mesajla, değişiklik/fırsat olunca. Portföy güncellemesi tweeti ATMA (Enes atar). 18:00 ve 23:30 TSİ teknik kontroller ayrı zincirdir (bölüm 14b), bu turda yoksa kur. DONGU.md'ye "AUTO" + tür + konu işle, push et. Son olarak bu mesajın aynısıyla (son 3 düzen ve ticker saatlerini güncelle) 5-20 dk rastgele gecikmeyle yeni send_later kur.

## C. DEVRİN SINIRLARI (yeni oturum bunları bilsin, Enes'e de söylesin)
- Bu sohbetin konuşma geçmişi yeni oturuma geçmez; geçen her şey bu dosyada, DEVIR_OZET.md, ORNEKLER.md, DONGU.md ve Enes'in kalıcı belleğinde.
- send_later görevleri oturuma bağlıdır: eski oturumun kurduğu tur, eski oturumda çalışır (A4).
- TradingView yalnız Enes'in bilgisayarı ve Chrome açıkken çalışır; değilse Yahoo hesapları kullanılır (sonuç aynı göstergeler, sadece SMC/Supertrend yaklaşık).
- Enes'in Claude planı en düşük ücretli plan: uzun oturumlar kullanım limitine takılabilir. Limit dolarsa zincir durur; Enes'e "limit doldu, şu saatte yeniden başlat" diye söylenir ve DONGU'ya not düşülür. Kullanımı azaltmak için gereksiz tekrar araması yapma, grafik taramasında ta2.py çıktısını özetle.

---------------------------------------------------------------------------------------------------

## 0. KİM, NE, NEDEN
- Kişi: Enes Uludağ. X hesabı @enes1050392, görünen ad "Enes Uludağ", hesap adı EnesInvestUS. Türkçe, ABD borsası odaklı.
- Enes bir YATIRIMCI (16.11 12:48). Portföy yönetiminde amacı yükselişin başını yakalamak değil, EN DİPLERİ bulmak (16.11 13:32).
- HESABIN AMACI (15.11 18:10, her şeyin üstünde): en iyi getiriyi yakalamak ya da borsayı en iyi bilen görünmek DEĞİL. Amaç GÜVEN sağlamak ve İYİ İÇERİK üretmek.
  - Doğru olmayan rakam yerine eksik tweet. Her kartta kaynak.
  - Yanılınca açıkça söyle ("şunu demiştim, olmadı").
  - Abartı, heyecan, "kaçırmayın" yok. Sade, dürüst, anlaşılır.
  - Okuru eğit: neden önemli, kime etkisi var.
- Hedef okur (15.11 16:25, EN ÖNEMLİ YAZIM KURALI): ABD borsasını az bilen biri. Olabildiğince KISA ve BASİT.
- Enes'i geliştirmek de amaç: her tweetle birlikte "Ne anlama geliyor?" öğretici bölümü gönderilir (bölüm 9).

## 1. PORTFÖY VE LİSTELER
- GÜNCEL PORTFÖY (16.11 12:49): NBIS RKLB DOCN SITM AXON CBRS VRT.
  - SPCX çıktı, SITM girdi.
  - Enes piyasa açılışında hepsini EŞİT AĞIRLIKLA alacağını söyledi. Benim "ben olsam" görüşüm kademeli girmekti; karar onun.
  - (eski 15.11 16:55: AXON NBIS RKLB CBRS DOCN VRT SPCX)
- İLGİ LİSTESİ: ON AAOI HOOD TEM CRDO PLTR ISRG ASTS MU + büyük yapay zeka/yarı iletken/bulut/uzay şirketleri (NVDA AMD AVGO TSM MSFT GOOGL AMZN META ORCL CRWV SNOW vb.).
- FIRSAT HİSSESİ SINIRSIZ (16.11 13:25): fırsat önerisi ilgi listesiyle sınırlı değil. ABD borsasında yatırıma uygun bulduğum HERHANGİ bir hisse önerilebilir; gerekçesi (temel + teknik), seviyesi ve riskiyle.
- Portföyde ağırlık/tutar/para ASLA tweete yazılmaz. Enes'in ağzından "aldım / sattım / ekledim / portföyüm / YTD %" cümlesi kurulmaz.
- PORTFÖY GÜNCELLEMESİ TWEETİ YOK (16.11 13:54): Portföy güncellemesi tweetini Enes kendisi atar. Claude portföy güncellemesi tweeti/kartı hazırlamaz, atmaz, sormaz. (eski: ana sohbetten Enes onayıyla atılırdı)
- Eski 'EnesInvestUS günlük portföy sorusu' görevi (trig_019TTCnsx74Nsi9DjkY7M5MF) 16.11 13:54'te DURDURULDU. Kapanış tweeti normal turların içerik menüsünden (00:05-00:45) atılır.

## 2. PAYLAŞIM MODU (güncel: TAM OTOMATİK)
- Buffer create_post:
  - organizationId 6af5719777bce44fa736607b, channelId 6af99a1aece6dfde5fd109c7 (X)
  - schedulingType automatic, mode shareNow
  - text + assets [{image:{url, metadata:{altText}}}]
  - altText'te yazım hatası yapma.
- Zincir:
  - Her tur sonunda mcp__claude-code-remote__send_later ile yeni tur kurulur.
  - Gecikme 5-20 dk arası RASTGELE (python random). "Tam 10 dk olmasın" (15.11 20:43).
  - Mesaj = sabit tur talimatı; son 3 düzen ve ticker saatleri her seferinde güncellenir.
  - Turlar DURMAYACAK (16.11 11:12 "turlar durmasın otomatik devam et").
- Son paylaşım 5 dk'dan yeniyse o tur paylaşma, 5-20 dk sonraya kur.
- GECE: 01:00-09:00 TSİ paylaşım yok, 09:05 için tur kurulur.
  - Tek istisna (16.11 01:53): önceden BİLİNEN bir açıklama varsa (takvimdeki bilanço rakamı, veri, konuşma) o saat için ayrıca tur kurulur.
  - Beklenmedik haber 09:05'e kalır.
- GÜNLÜK TAVAN 45 tweet (15.11 21:46; eski 40). Enes'in elle attıkları dahil, Buffer list_posts ile sayılır (00:00 TSİ = önceki gün 21:00Z).
- DURDUR: Enes "durdur" derse DONGU.md'ye satır başında tek başına "DURDUR" yaz ve zinciri kurma. Her tur başında DURDUR kontrol edilir.
- Mod geçmişi (bilgi için):
  - 15.11 16:10 sohbet modu (Buffer yok)
  - 17:30 istek modu
  - 18:30 10 dk modu
  - 19:30 OTOMATİK (shareNow)
  - 20:40 "10 dakikada 1, otomatik at, benden sadece foto iste"
  - 15.11 21:15 "oto atmaya devam"
  - Taslak (saveToDraft) modu İPTAL; şu an shareNow geçerli.
- X Original Content Rewards otomatik içeriği ödeme dışı tutabilir. Enes'e söylendi, Enes yine otomatik istedi.

## 3. TUR AKIŞI (her turda sırayla)
1. ReadNotifications (bildirim varsa). Ardından `cd /home/claude/kontra-gorsel/invest && git pull`.
2. Oku: DEVIR_TAM.md (bu dosya), DEVIR_OZET.md, DONGU.md TAMAMI (özellikle son satırlardaki "SIRADAKİ" notları).
3. DURDUR kontrolü.
4. Buffer list_posts: bugün kaç tweet atıldı, son tweet ne zaman, hangi konu/ticker.
5. ÖNCE SON DAKİKA TARAMASI (bölüm 4). Taze ve 2 kaynakla doğrulanmış gelişme varsa onu at. Yoksa içerik menüsünden daha önce ATILMAMIŞ bir konu seç.
6. Rakamları 2 kaynakla doğrula (bölüm 5).
7. Kart yap → Read ile kontrol et → push → raw URL 200 → Buffer (bölüm 7).
8. Enes'e SendUserMessage: paylaşılan metin + "Ne anlama geliyor?" (bölüm 9).
9. PORTFÖY + GRAFİK TARAMASI (bölüm 11-14): her turda grafiklere bakılır. Değişiklik ya da fırsat varsa Enes'e "ben olsam" notu atılır.
10. DONGU.md'ye `- HH:MM AUTO (TÜR): dosya.jpg - özet (kaynaklar) | düzen:...` yaz. Commit ve push.
11. Yeni send_later kur (5-20 dk).
- Bash "classifier no verdict" verirse bir kez tekrar dene. Olmazsa o tur paylaşma, 5-10 dk sonrasına aynı mesajla kur.
- WebFetch PROVENANCE_REQUIRED derse tekrar deneme, WebSearch ile devam et.
- Buffer hata verirse 1 kez tekrar dene; olmazsa DONGU'ya yaz, atla.
- Push reddedilirse görselsiz tweet atma.

## 4. İÇERİK ÖNCELİĞİ VE KONU SEÇİMİ
- ÖNCELİK SIRASI (16.11 11:21, EN ÖNEMLİ):
  - Her turda ÖNCE son dakika ve en yeni gelişmeyi tara (son 1-3 saat, WebSearch extended).
  - Taranacaklar: Reuters, AP, Bloomberg, CNBC; Asya/Avrupa/ABD; vadeliler; şirket IR, 8-K, 6-K, Form 4; Fed ve veriler; analist notları; portföy + ilgi listesi; son 1 haftada açıklanmış ama paylaşılmamış bilançolar.
  - Taze yoksa terim/analiz/eski içerik. Eski konulara yaslanma alışkanlığı bırakılacak.
- HABER HIZI KAYNAKLARI (16.11 01:49):
  - Sıra: (1) SEC EDGAR, IR ve bülten siteleri (PR Newswire, Business Wire, GlobeNewswire, Accesswire); (2) Reuters, CNBC, Bloomberg, Benzinga son dakika; (3) ekonomik ve bilanço takvimi; (4) menü.
  - Diğer kaynaklar:
    - Resmi veri: Fed, BLS, BEA, Treasury, Census.
    - Takvimler: Investing.com, TradingEconomics, Forex Factory, MarketWatch, Econoday, Earnings Whispers, Nasdaq, Yahoo, Zacks, StockAnalysis.
    - İçeriden/kurum: OpenInsider, Quiver, Capitol Trades, WhaleWisdom, Dataroma, Unusual Whales.
    - Hareket: Finviz, Chartmill, Stocktwits.
    - Derin: Semianalysis, The Information, Nikkei, DigiTimes, TrendForce, Axios, Techmeme, SpaceNews.
  - Sosyal sinyal (Walter Bloomberg, DeItaone, FirstSquawk vb.) 2 güvenilir kaynakla doğrulanmadan KULLANILMAZ.
  - X hesaplarına Claude girmez.
- VADELİ İŞLEMLER HER İŞLEM GÜNÜ (16.11 02:05):
  - 09:05 turunda ve ABD açılışından önce (~15:00-15:25 TSİ) tekrar. Dow, S&P 500, Nasdaq 100, Russell 2000 vadelilerinin önceki kapanışa göre %'si.
  - %1+ sürprizde ek tweet.
  - Düzen: kart2.isi(kolon=2, hane=2, etiket="VADELİ İŞLEMLER"). Yüzde 2 basamak.
  - "Vadeli = açılışı gösteren işaret, garanti değil."
- TEKRAR YOK:
  - DONGU.md tamamı + Buffer son 50'de olan konu tekrar atılmaz. Yeni gelişme varsa yeni açıyla atılabilir (DONGU'ya "devam: önceki dosya").
  - Aynı ticker 3 saatte bir. Aynı haber 24 saatte tekrar yok.
- ÖNCELİKLİ TÜRLER:
  - Son dakika.
  - Bu hafta ne var / yarın ne var.
  - Bilanço rakamları (YORUMSUZ, ilk tweet).
  - Bilanço analizi (YORUMLU, 30-90 dk sonra ayrı tur).
  - İçeriden alım-satım: günde 1-2. SEC Form 4; piyasadan alım (kod P) daha anlamlı; 1 Mn$ üstü; küme alımı; 10b5-1 planlı satış ya da vergi için bırakma (kod F) açıkça yazılır.
- İÇERİK MENÜSÜ (DEVIR.md bölüm 3 tam liste):
  - Zamana bağlı: sabah notu 09:30-11:00, premarket 16:15-17:15, açılış 17:30-18:30, kapanış 00:05-00:45, Cuma/Cumartesi haftanın karnesi, Pazar/Pazartesi bu hafta ne var, hafta içi 22:00 yarın ne var. Makro veri günü: beklenti → sonuç (yorumsuz) → etki (yorumlu).
  - Şirket: bilanço öncesi/rakam/analiz, opsiyonların beklediği hareket, analist notu (kurum + eski/yeni hedef), içeriden işlem, geri alım/temettü, anlaşma/satın alma, endeks girişi, halka arz, kilometre taşı, CEO/Fed sözü (foto Enes'ten).
  - Fon: 13F, haftalık fon akışları, açığa satış oranı.
  - Karşılaştırma ve veri: 1 yıl önce vs bugün, iki rakip, sektör sıralaması, uzun dönem tek metrik, yapay zeka capex, emtia/dolar/tahvil/kripto, haftanın rakamı.
  - Eğitici (haftada 3-5): terim sözlüğü, "bu şirket ne iş yapar", strateji/psikoloji, teknik analiz.
- Bilanço öncesi ve sonrası, kısa + uzun (DEVIR 5g):
  - Portföy ve ilgi listesi şirketlerinde öncesi ve sonrası KESİN atılır.
  - Uzun format 5-7 tweetlik flood. Zamanlama: öncesi 1 gün önce akşam ya da sabah; sonrası ilk tur.
- Sabit seriler (DEVIR 5f): sabah notu, kapanış, haftanın karnesi, gelecek hafta takvimi.
- Uzun seri ve çoklu hisse grafikleri (DEVIR 5k):
  - Fiscal.ai tarzı 5-10 yıllık tek metrik.
  - Forward F/K sıralaması, NTM büyüme sıralaması.
  - Hepsi aynı kaynak ve tarih. Başkasının grafiği kopyalanmaz.
- Gündem dosyası (DEVIR 5c): invest/gundem.md'de Enes'in elle eklediği konular öncelikli. Doğrula, kullanınca DONGU'ya "(gündem)" yaz.
- ANTHROPIC (çıkar çatışması):
  - Konu otomatik atılmaz (halka arz dahil).
  - Adı tweete YAZILMAZ; gerekirse "bir başka büyük yapay zeka şirketi" denir.
  - Enes'e soruldu: bu yasak gevşetilsin mi? Cevap bekleniyor.

## 5. DOĞRULAMA KURALLARI
- Her rakam en az 2 bağımsız kaynakla doğrulanır.
  - Kaynaklar çelişirse rakam kullanılmaz (ya da şirketin kendi rakamı kullanılıp not düşülür).
  - Tek kaynaktaki iddia KULLANILMAZ.
- YIL KONTROLÜ: arama sonuçları 2025 ile 2026'yı karıştırıyor; tarih mutlaka kontrol edilir.
- "Şu an / bugün" iddiaları güncel fiyatla doğrulanır.
- Tweetteki YAN BİLGİLER de 2 kaynakla doğrulanır ("borsa sert düştü", çeyreklik/yıllık ayrımı, "Huawei gibi" vb.). Doğrulanmayan yan cümle yazılmaz.
- Fiyat ve yüzde uydurulmaz, tahmin edilmez.
- Doğrulanamayanı Enes'e dürüstçe söyle. Enes'in tercihi: birincil kaynak, doğrulanamıyorsa belirt.
- Yanlış atılmış bir şey çıkarsa Enes'e açıkça söyle. Örnekler: INTC tweetindeki doğrulanmamış "şu an zararda" iddiası; Japonya GDP tweetindeki zayıf doğrulanmış yan cümleler.

## 6. YAZIM STİLİ
- Arkadaşına anlatır gibi, konuşma dili. Kısa cümle. 2-4 cümle. En fazla 2-3 rakam. Bir tweette tek fikir.
- Basit ve doğal cümleler (Enes tercihi). Yapay zeka gibi duran ifadeler yok.
- Şirketi ilk geçtiği yerde ne iş yaptığıyla tanıt: "$NBIS (yapay zeka şirketlerine GPU bulut gücü kiralayan Nebius)".
- Terimleri sadeleştir: EPS → hisse başı kâr; guidance → şirketin önümüzdeki dönem için verdiği tahmin; capex → yatırım harcaması; YoY → geçen yıla göre; tutanak → toplantı notları.
- Saatler gündelik dille: "akşam 8'de", "gece yarısı".
- Ticker'lar $TICKER biçiminde.
- İlk satır durdurmalı: rakam, tezat ya da net görüş.
- Her tweette 1 cümle net görüş. Bilanço rakam tweeti hariç.
  - "Bence" tekrarı yok (15.11 16:58).
  - Kapanışlar çeşitli olsun: "gösteriyor bana / düşünüyorum / sanmıyorum" tekrar etmez. Son 5 tweetin kapanışına bak.
  - Seçenekler: düz tespit, kısa yargı, sonuca bağlama, karşıtlık, takip, farklı fiilli kişisel cümle, yorumu başa koyma.
- ENES'İN BEĞENDİĞİ TARZ (16.11 12:22): kısa, haber odaklı, analist/kaynak adı + rakam + net sonuç. Tahmin "tahmin" diye belirtilir.
  - Örnek: Ming-Chi Kuo'nun "GOOGL 2029'da 16-18 milyon TPU" tahmini.
  - Enes bir tweet yapıştırırsa: tarzını öğren + konuyu hemen araştır (2 kaynak) + tur beklemeden hemen tweet at.
- OKUYUCUNUN AKLINDAKİ SORUYU CEVAPLA (16.11 13:07):
  - Tweette bir kusur/şart yazarsan ("organik değil", "tek seferlik", "satın almadan", "bilanço dışı") havada bırakma.
  - Ne kadar olduğunu 2 kaynakla bul. Okuyucunun soracağı soruları önceden cevapla: Bu iyi mi kötü mü? Rakamlar şişirilmiş mi, yanlış mı, çakma mı? Düzeltince ne kalıyor?
  - Rakam bulunamazsa ya da tek kaynaktaysa o cümleyi yazma ya da "ne kadarı belli değil" de. Tahmin yürütürsen "tahminen" de ve dayanağını yaz.
  - Örnek: SITM'de satın alma hariç gelir +%154 (212,4 Mn$), satın alınan birimin katkısı 86,3 Mn$ (~%29). Doğrusu "satın alınan birim hariç bile +%154" demekti.
  - Örnek: NBIS'te "düşüşün sebebi talep değil zamanlama" (13:20 tweetinde uygulandı).
- YASAK KALIPLAR: "Benim görüşüm:", "Görüşüm:", "Sonuç olarak", "Özetle", "Kısaca", "Risk tarafı da var", "Bir de şu var:", "X neden önemli?", "Kısa bir flood açayım", "Bu bence çok şey anlatıyor", "mesaj net", "dikkat çekiyor", "öne çıkıyor", "önemli bir gelişme", "kritik / kritik nokta", "vb.", "nabız tutmak", "sınavda", "mercek altında", "gözler ... üzerinde", "ayrıca", "bununla birlikte". Haber ajansı dili ve slogan kapanış yok.
- YASAKLAR (kesin):
  - Al/sat/hedef fiyatım/kesin yükselir tavsiyesi (analist hedefi kaynağıyla aktarılabilir).
  - @mention, link, hashtag kalabalığı (gerekmedikçe hiç).
  - Yanıt/beğeni/takip/DM otomasyonu.
  - Emoji.
  - Soruyla bitirmek (soru çok nadir).
  - Doğrulanmamış rakam.
  - Kişisel/özel hayat detayı (Huang olayında yalnız şirket/piyasa yönü).
  - Başkasının tweetini kopyalamak/çevirmek.
  - Gerçek kişi fotoğrafını internetten indirmek.
- TEKNİK ANALİZ TWEETİ DİLİ (16.11 14:07, Enes, KESİN KURAL): teknik analiz tweetlerinde Enes'in kendi bakışı ve planı anlatılır, ama tavsiye verilmez ve "oyun planı" diye başlık atılmaz. Arkadaşa anlatır gibi, konuşma dili, sade.
  - Örnek dil: "Bence bu hisse dibe yakın." / "Bence daha dip arıyor." / "Ben 80-82 arasından bir kademe eklerim, orayı da aşağı kırarsa 70-72'den bir kademe daha eklerim." / "69'un altında kapanırsa benim için hikaye değişir."
  - Seviyeler bölüm 13 tam testinden gelir (21 gösterge x 4 dilim). Teknik terimleri sadeleştir: FVG -> "boşluk", order block -> "alıcıların daha önce toplandığı bölge", OTE -> "geri çekilmenin ideal bölgesi", Supertrend -> "trend göstergesi".
  - YASAK kalır: "alın / satın / siz de ekleyin / kaçırmayın / hedef fiyatım kesin", miktar/ağırlık/para, "portföyümün %X'i". Okura yönelik emir kipi yok; sadece "ben" dili.
  - (eski: "Enes'in ağzından aldım/ekledim cümlesi kurulmaz" -> teknik analiz tweetlerinde "ben şuradan kademe eklerim" planı ARTIK SERBEST; gerçekleşmiş alım ("aldım") ve portföy güncellemesi yine yazılmaz, onu Enes atar.)
  - Teknik analiz tweeti görseli: göstergeli grafik (g/ta/ matplotlib koyu tema veya TradingView ekran görüntüsü), seviyeler işaretli.
- Şablonlar: invest/ORNEKLER.md (13 şablon). O zaman/şimdi, iki çarpıcı istatistik, bilanço skor kartı, haber + sektör etkisi, teknik analiz, uzun dönem sütun, çoklu hisse sıralama, uzun tez, eğitici strateji, yanıt kalıbı, araştırma raporu, çeyrek sonu vs bugün, kurum araştırma grafiği. Enes'in attığı her yeni tweet buraya şablon olarak eklenir.

## 7. GÖRSELLER (KART)
- Kod: invest/kart2.py (ana), kart.py (yedek). Fontlar invest/font: Inter Display, Instrument Serif, JetBrains Mono. Enes koyu tema + minimal sever.
- Düzenler (önce bunlar): bento, halka, isi, takvim, cizgi, panel, uclu, soz, editoryal, skor, zaman, ilerleme, dilim, dortlu, manset. Yedek: spotlight, split, terminal, sondakika, once_sonra, kapak, cam, poster, siralama, grafik2.
- KALDIRILDI: versus (15.11 21:23 "kaba"). Yerine panel.
- Son 3 turda kullanılan düzen tekrar edilmez. Şu an son 3: editoryal (13:05), uclu (13:20), bento (13:33). Bunu tur mesajında güncelle.
- Tür → düzen:
  - Bilanço rakam: skor/terminal. Analiz: bento/uclu/panel.
  - İki hisse: panel. Takvim: takvim. Kapanış: isi/dortlu.
  - Son dakika: sondakika/manset. İçeriden işlem: uclu/skor. Kişi: manset/soz (Enes fotosuyla). Vadeli: isi.
- LOGO ÇOK BELİRGİN (16.11 10:30-10:38): kart2.LOGO_BUYUT = 1.8. Küçültme yok, gerekirse daha da büyüt.
  - Koyu logolar beyaz plakada.
  - Logo yoksa logo/XXX.png ticker yazı logosu oluştur (örnek: 16.11'de logo/BIDU.png).
  - Ticker MUTLAKA "$" ile verilir ("$GOOGL"), yoksa logo çizilmez.
  - halka düzeni logo ÇİZMEZ, logo gereken konuda kullanma.
  - cizgi'de büyük rakam logoyla çakışabilir; başlık ve rakam kısa tutulur.
- YAZI TİPİ: ince/keskin yazı kuralı İPTAL (16.11 11:53). Normal ağırlıklar. (eski 10:34: ince istenmişti)
- Font tuzakları:
  - "OpenAI" kart fontunda "OpenAl" gibi görünür; kartta kullanma.
  - "AI" → "Al" gibi görünür; "Yapay zeka" yaz.
  - Türkçe büyük harf: Python .upper() "i" harfini "I" yapar ("GELIRI"). Etiketleri "İ" ile hazır büyük yaz ("GELİRİ").
  - Kicker'da şirket adı bozulabilir ("SİTİME"); ticker kullan ("SITM • 3. ÇEYREK").
- "Kaynak:" önekini verme (kart kendisi ekliyor). Kaynak ve alt başlığı kısa tut. Açıklamalar 3 satıra sığsın.
- HER KART Read ile kontrol edilir. Hata varsa YENİ dosya adıyla yeniden çiz (raw URL önbelleği) ve kötüsünü sil.
- Akış: invest/g/YYYYMMDD_HHMM_konu.jpg → git add/commit (attribution satırlarıyla) → push → curl ile raw URL 200 kontrolü → Buffer.
  - URL: https://raw.githubusercontent.com/enesuludg6-debug/kontra-gorsel/main/invest/g/<dosya>
- Haber ve kişi fotoğrafı internetten indirilmez. Kişi haberinde foto gerekiyorsa Enes'e sadece "X'in fotosunu at" yazılır. Beklenmez, o tur başka konu atılır; Enes'in fotoları invest/foto/.
- Signature'lar:
  - uclu(ticker, etiket, baslik, [(rakam, açıklama)]x3, kaynak, out)
  - cizgi(ticker, etiket, baslik, etiketler, degerler, buyuk, buyuk_lbl, kaynak, out, renk=None)
  - sondakika(ticker, baslik, alt, kaynak, out, bant=)
  - dortlu(etiket, baslik, [(ticker, değer, not)]x4, kaynak, out)
  - editoryal(ticker, kicker, baslik, spot, rakamlar3, kaynak, out, tarih="")
  - skor(ticker, etiket, baslik, [(metrik, beklenti, gerçek, ok)], sonuc, kaynak, out)
  - zaman(ticker, etiket, baslik, [(tarih, başlık, açıklama)], kaynak, out)
  - isi(baslik, alt, kutular, kaynak, out, etiket, kolon, hane)
  - panel(sol, sag, kicker, baslik, satirlar, cubuk, kaynak, out, notu="")
  - bento(ticker, etiket, baslik, buyuk, buyuk_lbl(str), [(ETİKET, değer, alt)]x3, seri, seri_lbl, kaynak, out)
  - halka(ticker, yuzde, baslik, orta_alt, [(etiket, değer)]x3, kaynak, out, etiket, renk)

## 8. ENES BİR ŞEY ATARSA
- Başkasının tweeti/grafiği: araştır, her rakamı doğrula, KENDİ cümlenle benzerini yaz, kendi kartını çiz. Tutmayan rakamı Enes'e söyle. Hemen at (tur bekleme).
- "Yorum yaz" derse yanıt metni hazırla (Enes kendisi atar; otomatik yanıt yok). İstenirse İngilizcesi de.
- Grafik ekran görüntüsü atarsa teknik analiz tweeti hazırla (DEVIR 5h 2. yol). Okunamayan değer uydurulmaz.
- Gönderdiği her tweet ORNEKLER.md'ye şablon olarak eklenir.

## 9. "NE ANLAMA GELİYOR?" (ÖĞRETME, 15.11 19:15)
- Her paylaşımdan sonra Enes'e SendUserMessage atılır. İçinde paylaşılan metin + "Ne anlama geliyor?" bölümü olur. 3-6 kısa madde:
  1. Bu bilgi/terim nedir, sade anlatım.
  2. Piyasada neden önemli, genelde neye yol açar.
  3. Nasıl yorumlanır, iyi/kötü sinyal ne olur.
  4. Varsa tarihten kısa bir örnek.
- Doğrulanamayıp tweete girmeyen rakamları da kısaca söyle. Bu bölüm tweete girmez.

## 10. TARAYICI / BİLGİSAYAR ERİŞİMİ
- Enes'in X hesabına HİÇBİR ŞEKİLDE girilmez. Tarayıcı otomasyonu ve scraping X kurallarına aykırı.
- Tarayıcı ve bilgisayar SADECE tradingview.com için (Enes'in X hesabına zararı olmayacak şekilde).
  - TradingView'da paylaşım, yorum, fikir yayınlama, hesap/abonelik ayarı YOK. Kayıtlı çizim şablonları silinmez.
- Enes'in bilgisayarı: Windows, Claude in Chrome eklentisi, deviceId 2c13b0fb-418e-4a79-aee9-34fd79d23bef. Bilgisayar ve Chrome açıksa çalışır, kapalıysa Yahoo hesaplarına geçilir.
- TradingView planı Basic: grafik başına en fazla 2 gösterge.

## 11. PORTFÖY YÖNETİMİ — HER TURDA (16.11 12:47 → 13:25 kalıcı)
- 12:47 kuralı (EN ÖNEMLİ YENİ KURAL o an): araştırma yaparken portföyü de yönet. Ekle/çıkar fikirleri ver, grafikleri incele. Ancak 12:51'de "arada bir" denmişti.
- 13:09 / 13:25 GÜNCELLEME: grafik kaynağı bağlandığı için HER TURDA tweet işinin YANINDA:
  1. Portföydeki 7 hisse + fırsat gördüğüm hisselerin grafiklerine bakılır (bölüm 12-13).
  2. Beğendiğim/beğenmediğim bir şey, EKLEME fırsatı, AZALTMA/SATMA işareti, portföy dışı fırsat varsa Enes'e özel mesaj (SendUserMessage) atılır.
  3. Değişiklik yoksa her tur mesaj atmak zorunlu değil, ama grafiklere her tur bakılır. Önceki durumla karşılaştır, değişeni bildir.
- TWEETLERDE al/sat ASLA yok. Portföy notları yalnız Enes'e özel.
- Grafik kaynağı bağlı değilse eski kural geçerli: sadece SON 2 GÜN tarihli grafik/teknik analiz kaynakları (tarih kontrolü zorunlu).

## 12. GRAFİK KAYNAKLARI (öncelik sırası)
1. TRADINGVIEW (bilgisayar/Chrome açıksa):
   - Düzen adı "Adsız", id UN09ZFN8. URL: https://www.tradingview.com/chart/UN09ZFN8/?symbol=NASDAQ%3ATICKER (DOCN, VRT: NYSE%3A; CBRS: sadece CBRS).
   - Mevcut göstergeler (16.11 13:22'de Enes onayıyla): Vol 20 + Supertrend (10, hl2, 3) + LuxAlgo Smart Money Concepts. EMA 20/50/100/200 çıkarıldı, kaydedildi (ctrl+s).
   - Enes izni (13:22): ihtiyaç olursa bir göstergeyi çıkar, başkasını ekle, tekrar bak. Değişiklikten sonra ctrl+s ile kaydet; kaydedilmezse sembol değiştirirken "Leave site?" uyarısı çıkar.
   - SMC ve Supertrend için TradingView ESAS (benim hesabım yaklaşık).
   - Bakılacak dilimler: 1 saat, 4 saat, günlük, haftalık.
2. YAHOO FINANCE (Enes 13:16'da query1.finance.yahoo.com alan adını izinli listeye ekledi):
   - `python3 ta2.py <tickerlar>`: 21 gösterge, 4 zaman dilimi.
   - `python3 ta.py <tickerlar>`: eski kısa set.
3. ALPHA VANTAGE: bağlı ama ücretsiz anahtar ABD hisse verisi vermiyor ("premium gerekir"). KULLANMA.
4. TWELVE DATA: bağlantı sayfası telefonda açılmadı. Bilgisayardan bağlanması önerildi, henüz bağlı değil.

## 13. GÖSTERGE SETİ — HEPSİ ZORUNLU (16.11 13:27 + 13:28)
- Her analizde AŞAĞIDAKİLERİN HEPSİNE, FARKLI ZAMAN DİLİMLERİNDE (1s / 4s / günlük / haftalık) bakılır:
  RSI, MACD, EMA, SMA, Bollinger Bands, VWAP, Stochastic RSI, ADX, Ichimoku Cloud, ATR, OBV, CCI, Williams %R, Parabolic SAR, Supertrend, MFI, Fibonacci Retracement, Keltner Channels, Aroon, Volume Profile, SMC (Smart Money Concepts).
- Her birinin amacı (Enes 13:27):
  - EMA 200: ana trend yönü.
  - VWAP: SMC bölgelerinde fiyatın adil değeri (20 günlük + son ana dip/tepeden anchored).
  - RSI 14: likidite süpürmesi sonrası momentum kontrolü.
  - MACD: trend dönüşü ve momentum değişimini doğrulamak.
  - ATR: stop-loss ve hedef mesafeleri.
  - Volume Profile: önemli hacim bölgeleri ve likidite alanları (POC, değer alanı).
  - ADX: trendin gücü (+DI / -DI).
  - Fibonacci Retracement: OTE (Optimal Trade Entry) bölgeleri, 0.618-0.786.
  - OBV: hacim akışı ve olası uyumsuzluklar.
- SMC İÇİN ANA KOMBİNASYON (teyit): SMC + EMA 200 + VWAP + RSI 14 + ATR + Volume Profile + Fibonacci.
  - SMC zaten fiyat yapısını, order block, FVG, BOS, CHoCH ve likidite süpürmelerini analiz eder. Diğerleri teyit içindir.
- TAM TEST ZORUNLU (16.11 14:05, Enes, KESİN KURAL): kararı vermeden önce 21 göstergenin HEPSİ, 4 zaman diliminin HEPSİNDE (1s / 4s / günlük / haftalık) tek tek kontrol edilir. "Birkaç göstergeye bakıp karar" YASAK.
  1. `python3 ta2.py -v <tickerlar> > /tmp/ta.txt` (-v ŞART: tüm dilimlerde 21 göstergenin hepsini basar). Çıktının tamamı okunur.
  2. Bilgisayar açıksa TradingView'da da test edilir: Basic plan aynı anda 2 gösterge -> göstergeleri 2'şerli kapat-aç: (Supertrend + SMC), (RSI + MACD), (EMA 200 + VWAP), (Bollinger + Stoch RSI), (ADX + Ichimoku), (ATR + OBV), (CCI + Williams %R), (Parabolic SAR + MFI), (Fibonacci + Keltner), (Aroon + Volume Profile), (SMA). Her çift 1s/4s/G/H dillimlerinde bakılır, kararı destekleyenlerin ekran görüntüsü alınır. Sonunda varsayılan düzen geri kurulur (Supertrend + LuxAlgo SMC) ve ctrl+s.
  3. Karar mesajında her zaman dilimi için özet: "yukarı / aşağı / nötr" sayısı + kararı belirleyen göstergeler + dilimler arası çelişki (örn. 1s aşağı, 4s yukarı) açıkça yazılır.
  4. Kullanım limiti: TradingView rotasyonu her hisse için uzun sürer. Tam rotasyon karar verilen / değişen hisseler için yapılır; diğerleri ta2.py -v ile 21x4 tam test edilir (o da tam testtir, atlanmaz).
- Araç: invest/ta2.py. Günlükte 23 sinyalin hepsini, diğer dilimlerde özet basar; `-v` ile tüm dilimlerde hepsini. Her dilim için "yukarı / aşağı / nötr" sayısı verir.

## 14. ENES'E PORTFÖY NOTU — DİL VE İÇERİK
- "BEN OLSAM" DİLİ (16.11 13:31): tavsiye/öneri dili yok. Örnekler:
  - "Ben olsam bugün RKLB'den biraz eklerdim."
  - "Ben olsam bugün AXON'a girmezdim, 291 kırılmadan dipte dönüş görürsem 295-300 civarında eklerdim."
  - "Ben olsam elimde NBIS varsa 109 altında kapanırsa azaltırdım."
  - Bu dil SADECE Enes'e özel mesajlarda. Tweette al/sat yok kuralı aynen geçerli.
- DİP AVCISI (16.11 13:32): Enes yükselişin başında almak istemiyor, EN DİPLERİ bulmak istiyor. Not içeriği:
  - Dip bölgesi: SMC talep/order block, bull FVG, Fibonacci OTE 0.618-0.786, Volume Profile değer alanı altı/yüksek hacim düğümleri, haftalık destek.
  - Dip işaretleri: RSI / StochRSI / Williams %R / MFI aşırı satım; OBV ve RSI pozitif uyumsuzluk; likidite süpürmesi sonrası geri dönüş; kapitülasyon hacmi; CHoCH yukarı.
  - Kademeli alım seviyeleri: "ben olsam şu 2-3 seviyeden parça parça alırdım".
  - Tezin bozulduğu seviye (stop = ATR'ye göre ya da yapı altı). Hedef = VP POC / bear FVG / direnç.
  - Trend teyidi beklemek yerine fiyatın dip bölgesine yaklaştığını bildir.
- Kısa format: hisse + ne oldu + seviye(ler) + "ben olsam ...". Karar Enes'in.
- SON TARAMA REFERANSI (16.11 13:30, Cuma kapanışı + açılış öncesi; açılış öncesi hepsi -%3 ile -%5,5):
  - RKLB: tek "Buy" (TradingView Supertrend desteği 57,2; günlük SMC 61,13'te yukarı CHoCH). Talep 44-50, bull FVG 53-55. ATR 4,9.
  - VRT: eşikte. Supertrend 202,2 altında kalırsa "Sell"e döner. Talep 160-170, 4s bull FVG 184-197. Haftalıkta 220,9 aşağı kırılmış.
  - SITM: Supertrend Sell 494. Bull FVG 398-426, talep 310-335. 4 saatlikte OBV pozitif uyumsuzluk.
  - DOCN: Supertrend Sell 102,3. Dip 69,8. Günlük ve 4 saatlikte OBV pozitif uyumsuzluk. Fiyat OTE içinde. Talep 51-56.
  - CBRS: Supertrend Sell 116. Dip 77,8. 4s bull FVG 85-92,5. 1 saatlikte toparlanma.
  - NBIS: Supertrend Sell 173,8. Günlük ve 4 saatlikte 23 sinyalin 20'si aşağı. Talep 100,7 ve 86,6. Williams %R aşırı satım.
  - AXON: en zayıfı (haftalık BOS aşağı 339). Dip 291,5, altında yakın talep yok. RSI 30.
- 13:31'de Enes'e verilen "ben olsam" planı: RKLB 58-60 al (stop 52, hedef 63,5 ve 70-71); VRT 202-205 geri alınırsa (stop 176, hedef 242); DOCN 79-84 küçük (stop 69,8 altı, hedef 97-102); SITM 398-426 (stop 355, hedef 491-494); CBRS 90 civarı bekle (stop 77,8 altı); NBIS alma, 109 altı kapanışta azalt; AXON girme, 291,5 tutar ve 1 saatlikte 323 üstü gelirse dönüş ara.
  - Bu plan 13:32 dip-avcısı kuralından ÖNCE yazıldı. Sonraki notlar dip bölgesi + kademeli alım mantığıyla yazılmalı.

## 14b. GÜNDE 2 SABİT TEKNİK KONTROL (16.11 13:55, Enes)
- Her ABD işlem günü İKİ kez: açılıştan 30 dk sonra (18:00 TSİ) ve kapanıştan 30 dk önce (23:30 TSİ). (ABD yaz saatinde 17:00 ve 23:00; yarım günlerde kapanış 21:00 TSİ ise 20:30.)
- Kapsam: portföyün tamamı (NBIS RKLB DOCN SITM AXON CBRS VRT) + benim yatırıma uygun bulduğum EN İYİ 3-4 hisse (portföy dışı, herhangi bir ABD hissesi; temel + teknik gerekçeyle).
- Yöntem: `python3 ta2.py <tickerlar> > /tmp/ta.txt` (21 gösterge, 1s/4s/günlük/haftalık) + bilgisayar açıksa TradingView (UN09ZFN8, SMC + Supertrend). Gün içi fiyatı mutlaka kullan.
- Çıktı: Enes'e tek SendUserMessage, her hisse için "ben olsam ..." kararı (bölüm 14 dili): dip bölgesi, kademeli alım seviyeleri, tezin bozulduğu seviye, hedef. Değişiklik olmasa da bu iki kontrolde mesaj HER ZAMAN atılır.
- GRAFİK EKRAN GÖRÜNTÜSÜ (16.11 14:00, Enes): "ben olsam" kararının dayandığı göstergeleri gösteren grafik görüntüsü Enes'e SendUserFile ile atılır (önemli karar/değişiklik olan hisseler için, her kontrolde en çok 3-4 görsel; kullanım limiti).
  - Bilgisayar açıksa: TradingView (UN09ZFN8, ilgili zaman dilimi), mcp__claude-in-chrome__computer screenshot save_to_disk=true. Basic plan 2 gösterge sınırı: gerekirse göstergeyi değiştir, görüntüyü al, ctrl+s. X'e girme.
  - Ek olarak ya da bilgisayar kapalıysa: Yahoo verisinden matplotlib ile koyu temalı grafik çiz (fiyat + EMA 200 + VWAP + dip bölgesi/FVG/OB kutuları + Fib OTE + alt panelde RSI/MACD/OBV), kararı destekleyen seviyeler işaretli. invest/g/ta/ altına kaydet.
  - Görsele kısa açıklama: hangi gösterge neyi gösteriyor, karar neden bu.
- Tweet değildir; al/sat tweette yok kuralı aynen geçerli. Portföy güncellemesi tweetini Enes atar.
- Zincir: her kontrol sonunda bir sonraki kontrol için send_later kurulur (18:00 -> 23:30 aynı gün; 23:30 -> sonraki işlem günü 18:00). Hafta sonu ve ABD tatilleri atlanır (26.11.2026 Şükran Günü kapalı; 27.11 yarım gün).

## 14c. HİSSE SEÇİMİ = PROFESYONEL YÖNTEM (16.11 13:58, Enes, KESİN KURAL)
Hisse araştırırken, beğenirken ve portföyle karşılaştırırken profesyonel bir yatırımcı / portföy yöneticisi / aracı kurum analisti neye bakıyorsa ona bakılır. HEM TEMEL HEM TEKNİK. Teknik taraf Enes'in verdiği set (bölüm 13: 21 gösterge + SMC kombinasyonu, 4 zaman dilimi). Temel taraf aşağıdaki kontrol listesi. Her rakam 2 kaynak, yıl kontrolü; bulunamayan "bilinmiyor" diye yazılır, uydurulmaz.

A) TEMEL KONTROL LİSTESİ (her aday ve her portföy hissesi için aynı liste)
1. İş ve hendek: ne satıyor, pazar büyüklüğü, rakipler, rekabet avantajı (teknoloji, ölçek, geçiş maliyeti, ağ etkisi), müşteri yoğunlaşması (tek müşteri %20+ ise risk).
2. Büyüme: gelir büyümesi (YoY ve çeyrekten çeyreğe), hızlanıyor mu yavaşlıyor mu, organik mi satın almalı mı (organik payı hesaplanır), sipariş birikimi / RPO / backlog.
3. Kârlılık: brüt marj ve trendi, faaliyet marjı, net kâr; zarardaysa kâra geçiş yolu. GAAP ile düzeltilmiş arası fark ve hisse bazlı ödeme (SBC) büyüklüğü.
4. Nakit: serbest nakit akışı (FCF) ve marjı, capex yükü, nakit yakma hızı ve kaç çeyrek yeteceği.
5. Bilanço: net nakit / net borç, borç vadesi, faiz karşılama, likidite. Hisse seyrelmesi (hisse sayısı artışı, konvertibl, ATM satışları).
6. Değerleme: ileri F/K, EV/Satış, EV/FAVÖK, PEG, FCF getirisi; rakiplere ve kendi 3-5 yıllık geçmişine göre ucuz mu pahalı mı. Büyümeye göre fiyat (Rule of 40 yazılım/bulut için).
7. Beklenti momentumu: son 30-90 günde EPS ve gelir tahmin revizyonları (yukarı/aşağı), son bilançoda beklenti aşımı/kaçırma, şirketin kendi tahmininin (guidance) yükseltilmesi/düşürülmesi.
8. Analist ve kurum: not/hedef değişiklikleri (kurum + eski/yeni hedef), 13F'de kurum giriş/çıkışları, içeriden alım-satım (Form 4; kod P alım anlamlı, 10b5-1 ve vergi satışları ayrılır).
9. Pozisyonlanma: açığa satış oranı ve kapanma günleri, opsiyon ima edilen hareket, hacim ve likidite (günlük işlem hacmi), piyasa değeri.
10. Katalizör ve takvim: sonraki bilanço tarihi, ürün/sözleşme duyuruları, lock-up bitişi, endeks girişi, düzenleme kararları.
11. Riskler: dava, düzenleme, ihracat kontrolleri, yönetim değişikliği, muhasebe uyarıları, short raporları (tek kaynaksa doğrulanmamış diye belirtilir), müşteri kaybı, makro duyarlılık (faiz, dolar, emtia).
12. Yönetim ve sermaye dağıtımı: geri alım/temettü, satın alma geçmişi, yöneticinin hisse sahipliği.
13. Makro ve sektör rejimi: faiz beklentisi, sektör rotasyonu, sektörün göreceli gücü (S&P 500 ve sektör ETF'ine göre), risk iştahı.

B) TEKNİK (bölüm 13 aynen): EMA 200 trend, SMC yapısı (BOS/CHoCH, order block, FVG, likidite süpürmesi), VWAP, RSI 14, MACD, ATR (stop/hedef mesafesi), Volume Profile (POC, değer alanı), ADX, Fibonacci OTE 0.618-0.786, OBV uyumsuzluğu + kalan göstergeler; 1s/4s/günlük/haftalık. Enes dip avcısı: dip bölgesi ve kademeli alım seviyesi öncelikli.

C) ADAY BULMA SÜRECİ
1. Tarama: güncel haberler, tahmin revizyonu yukarı olanlar, güçlü bilanço + düşük değerleme, sektör gücü, aşırı satılmış kaliteli hisseler (dip bölgesine gelen). Evren: tüm ABD borsası, izleme listesiyle sınırlı değil.
2. Kısa liste (6-10) -> A listesi + B tekniğiyle eleme -> en iyi 3-4.
3. Her aday için PUAN KARTI: Temel (iş/hendek, büyüme, kârlılık, nakit/bilanço, değerleme, beklenti momentumu, risk) ve Teknik (trend, dip bölgesine uzaklık, momentum/uyumsuzluk, risk/ödül = hedef mesafesi / stop mesafesi). Her başlık 1-5. Toplam ve kısa gerekçe.

D) PORTFÖYLE KARŞILAŞTIRMA (zorunlu)
- Portföydeki 7 hisse AYNI puan kartıyla puanlanır.
- Aday, portföydeki en zayıf hisseden AÇIKÇA daha iyiyse (toplamda belirgin üstün ve risk/ödülü daha iyi) önerilir: "Ben olsam X'i azaltıp/çıkarıp Y'ye geçerdim, çünkü ..." + seviyeler.
- Daha iyi seçenek YOKSA önerilmez; "portföyündekilerden daha iyisini bulamadım" denir ve neden kısaca söylenir. Zorla öneri yapılmaz.
- Portföy hissesi için de: tez bozulduysa (temel ya da yapı) açıkça söylenir.

E) DİL VE SINIRLAR
- Enes'e özel mesaj, "ben olsam" dili (bölüm 14). Karar Enes'in. Tweette al/sat yok.
- Kaynak belirtilir; tek kaynaklı bilgi "doğrulanmadı" diye işaretlenir ya da kullanılmaz.
- Bu yöntem 18:00 ve 23:30 teknik kontrollerinde (bölüm 14b) ve her fırsat önerisinde uygulanır. Kullanım limitine dikkat: temel analiz günde bir kez derinlemesine (18:00), 23:30'da yalnız değişenler güncellenir.

## 14d. TEKNİK ANALİZ TWEETLERİ VE GÖRSELLERİ — ENES PAYLAŞIR (16.11 14:15, Enes, KESİN KURAL)
- 18:00 ve 23:30 kontrollerinde bakılan HER hisse için (portföydeki 7 hisse + aday/fırsat hisseleri + test amaçlı bakılanlar) AYRI AYRI hazırlanır:
  1. Göstergeli grafik görseli (g/ta/YYYYMMDD_HHMM_<ticker>_teknik.jpg, koyu tema, seviyeler ve gerekçeler işaretli) + varsa TradingView ekran görüntüleri.
  2. O hisseye özel teknik analiz tweet taslağı (bölüm 6 "TEKNİK ANALİZ TWEETİ DİLİ").
  - Enes'e her hisse ayrı mesaj + ayrı SendUserFile olarak gönderilir (tweet metni + görsel birlikte).
- TEKNİK ANALİZ TWEETLERİNİ CLAUDE PAYLAŞMAZ. Buffer'a gönderilmez. Enes kendisi teyit edip paylaşır (Buffer aylık 1000 gönderi hakkı korunur). Otomatik turlar teknik analiz tweeti atmaz.
- KANIT ZORUNLU (16.11 14:15): "şuradan kademe eklerim / orayı kırarsa şuradan eklerim / şunun altında tez biter / hedef şu" denen HER seviyenin NEDENİ yazılır: hangi göstergeler ve hangi zaman dilimleri o bölgede çakışıyor.
  - Tweette sade dille kısa gerekçe: ör. "79-84'ü seçmemin sebebi: günlükte doldurulmamış bir boşluk var, 1 saatlikte trend göstergesi orada destek veriyor ve fiyat daha önce burada alıcı buldu."
  - Enes'e özel notta tam gerekçe: "79,2-84,3 = günlük bull FVG + 1s Supertrend AL 83,5 + 1s Ichimoku bulutu 78,9-81,8 + 4s bull FVG 79,2". En az 2 bağımsız gösterge/dilim çakışmayan seviye kademe olarak verilmez.
  - Görselde her seviyenin yanında gerekçe etiketi olur.
- Bu kurallar devir notu yeniden yazılırsa aynen korunur.

## 14e. 16.11 YAPILAN ÇALIŞMALAR (referans/örnek)
- 13:52 kripto düşüş tweeti (COIN/MSTR, sondakika), 14:08 NVO CagriSema tweeti (editoryal) — otomatik turlar, Buffer.
- 14:15 RKLB TEKNİK DENEME: ta2 -v 21x4. 1s 5/6/12, 4s 8/3/12, G 7/7/9, H 4/8/11 (yukarı/aşağı/nötr). Gerekçe: günlük CHoCH yukarı 61,13; G+4s Supertrend AL (50,6 / 55,6); MACD +; OBV uyumlu; fiyat Fib OTE 43,9-66,8 içinde; haftalık bull FVG 55,3-59,8 + 4s bull FVG 59,4-59,6 çakışması. Ben olsam: 1. kademe ~59,5, 2. kademe 53-55 (günlük bull FVG 53,1-55,0 + VWAP 20g ~55,3), azalt <50,6 günlük kapanış, tez biter <43,9; hedef 63,5 (POC) ve 68-71 (son tepe + EMA 200). Görseller g/ta/20261116_1405_rklb_tradingview.jpg, 1415_rklb_teknik.jpg.
- 14:25 DOCN TEKNİK DENEME: ta2 -v + TradingView (Supertrend+SMC 1s/4s/G/H, RSI+MACD G; ctrl+z ile geri, ctrl+s). 1s 9/4/10, 4s 5/9/9, G 3/13/7, H 3/12/8. TV 4s Supertrend AL 73,3 (ta2 92,3 SAT; TV esas). Gerekçe: G/4s/1s OBV pozitif uyumsuzluk, TV RSI 41,7 ortalamasını yukarı kesti, MACD sıfır altı yukarı kesişim, fiyat OTE içinde. Ben olsam: 1. kademe 79-84 (G bull FVG 79,2-84,3 + 1s Supertrend 83,5 + 1s bulut 78,9-81,8), 2. kademe 70-73 (son dip 69,8 + haftalık EMA 200 70,0 + TV 4s Supertrend 73,3), tez biter haftalık kapanış <69,8; direnç 93,8-97,3 (G bear FVG), 102,2 (G Supertrend). Görseller g/ta/20261116_1420_docn_*.jpg, 1425_docn_teknik.jpg.
- Grafik çizim kodu: bu iki görselin matplotlib kodu (koyu tema, sağda gerekçeli seviye etiketleri, altta RSI/MACD/OBV) yeni görseller için şablondur -> invest/ta_grafik.py.
- TradingView rotasyon yöntemi: legend'e tıkla + Delete ile göstergeyi kaldır; Indicators (üst menü) -> ara -> yerleşik göstergeyi tıkla; ekran görüntüsü; ctrl+z ile tüm değişiklikleri geri al (özel ayarlar korunur); ctrl+s. URL'de interval=60/240/D/W ile dilim değişir; yüklenmesi için 8-10 sn bekle.

## 15. TAKVİM (16-19 Kasım 2026, TSİ)
- Pzt 16.11:
  - Tyson (TSN) Q4 açılış öncesi. Konsensus EPS kaynağa göre 0,53-0,61$, gelir ~14,1 Mr$. Çağrı 17:00 TSİ. Rakamlar 13:33'te henüz yoktu; 2026 tarihli olduğunu doğrula.
  - Baidu Q3 açıklandı ve 13:33'te tweetlendi.
  - Warsh konuşması 20:00 TSİ. ABD açılışı 17:30 TSİ.
- Sal 17.11: HD açılış öncesi; NVDA kapanış sonrası (rakamlar ~00:20 TSİ Çarşamba). Gece istisnası turu için Enes onayı bekleniyor.
- Çar 18.11: TGT; FOMC toplantı notları 22:00 TSİ; PANW kapanış sonrası.
- Per 19.11: WMT.
- Q3 13F son günü 16 Kasım 2026.

## 16. DİĞER GÖREVLER / BEKLEYENLER
- "EnesInvestUS günlük portföy sorusu" (trig_019TTCnsx74Nsi9DjkY7M5MF): 16.11 13:54 Enes isteğiyle DURDURULDU (portföy tweetini Enes atar).
- Saatlik hazırlık ve Buffer taslak görevleri KAPALI.
- Enes'ten cevap beklenenler:
  - Anthropic adı yasağı gevşesin mi?
  - Portföy ağırlıkları (eşit ağırlık dedi).
  - Resmi CBRS logosu (opsiyonel).
  - NVDA gece turu istisnası.
  - Twelve Data bağlantısı.

## 17. KAYIT
- DONGU.md satır biçimi: `- HH:MM AUTO (TÜR): dosya.jpg - özet (kaynaklar; tek kaynak olup kullanılmayanlar) | Buffer id | düzen:...` ve gerekirse "SIRADAKİ: ...".
- Commit sonuna sistemin verdiği attribution satırları eklenir.
- Repo: enesuludg6-debug/kontra-gorsel → /home/claude/kontra-gorsel (invest/). Yeni oturumda: add_repo (push) → git clone --depth 1 → register_repo_root.
- 16.11 Buffer gönderileri (20 tweet): vadeli, sabah notu, PANW, INTC, ROK, Form 4, PLTR, ASTS, HOOD, ON, geri alım, NVDA Bessent, CBRS, MS küresel, Japonya GDP, GOOGL TPU Kuo, ulusal şampiyon (WSJ), SITM bilanço, NBIS açılış öncesi, BIDU bilanço.

## 18. KONTROL LİSTESİ — HER ENES MESAJI → BU DOSYADAKİ YERİ
(15.11 mesajları DEVIR.md ve DEVIR_OZET.md'de kayıtlı, burada özetlendi. 16.11 mesajlarının tamamı tek tek:)
| Saat (16.11) | Enes'in mesajı (özet) | Bölüm |
|---|---|---|
| 01:49 | Haberi X üreticilerinden önce bul, hız kaynakları | 4 |
| 01:52 | Turlar 5-20 dk rastgele | 2 |
| 01:53 | Gece sınırı yalnız bilinen açıklamada gevşer | 2 |
| 02:05 | Vadeli işlemler her gün atılır | 4 |
| 10:30-10:38 | Logolar daha da belirgin (1,8x) | 7 |
| 10:34 | İnce/keskin yazı (sonra iptal) | 7 |
| 11:12 | Turlar durmasın, otomatik devam | 2 |
| 11:21 | Öncelik son dakika/en yeni gelişme | 4 |
| 11:53 | İnce keskin yazıya gerek yok | 7 |
| 12:22 | Beğendiğim tweetlerin tarzı + yapıştırdığım konuyu hemen araştırıp at (Kuo/TPU) | 6, 8 |
| 12:47 | Portföyü yönet, ekle/çıkar fikri, son 2 gün grafikler, arada bir, beğenmediğini söyle | 11 |
| 12:48 | Ben yatırımcıyım | 0 |
| 12:49 | Portföy NBIS RKLB DOCN SITM AXON CBRS VRT, açılışta eşit ağırlık | 1 |
| 12:51 | Turlarda ara ara bakarsın | 11 |
| 13:07 | "Organik değil" gibi kusuru araştır, iyi mi kötü mü, rakamlar yanlış/çakma mı cevapla | 6 |
| 13:09 | TradingView bağlayacağım; her turda portföy + fırsat hisseleri, indikatörler, birlikte karar | 11, 12 |
| 13:11 | Alpha Vantage'a ne yazayım (API anahtarı) | 12 |
| 13:13 | Bağladım ama farklı sohbette açılıyor | 12 |
| 13:13 | Twelve Data sayfası açılmadı | 12 |
| 13:15 | Türkçe kullanıyorum, nereye ekleyeceğim (alan adı izni) | 12 |
| 13:16 | Yaptım (Yahoo izni) | 12 |
| 13:17 | Al-sat ve SMC indikatörlerine de ulaş; TradingView başka sohbete bağlandı | 12, 13 |
| 13:19 | Ekle (SMC) | 12 |
| 13:22 | Önceki göstergeleri kaldır, SMC ekle, araştır; gerekirse çıkar-ekle-tekrar | 12 |
| 13:25 | Hepsini kurallara ekle; her turda tweet + portföy + grafik; beğendiğin/beğenmediğin/ekleme/satma; TradingView yoksa diğer kaynaklar | 3, 11, 12 |
| 13:25 | Fırsat hissesi izleme listesinde olmak zorunda değil | 1 |
| 13:27 | 9 göstergeli zorunlu set (EMA200, VWAP, RSI14, MACD, ATR, VP, ADX, Fib, OBV) | 13 |
| 13:28 | 21 göstergenin hepsi + farklı zaman dilimleri + SMC kombinasyonu | 13 |
| 13:31 | "Ben olsam" diye konuş, kurala ekle | 14 |
| 13:32 | Amacım en dipleri bulmak, yatırımcıyım | 0, 14 |
| 13:54 | Portföy güncellemesi tweetlerini kaldır, onları ben atarım | 1, başlık |
| 13:55 | Günde 2 kez (açılış +30, kapanış -30) portföy + en iyi 3-4 hisse teknik kontrol, 'ben olsam' kararları | 14b, başlık |
| 14:15 | Tüm çalışmaları ve kuralları ekle; kademelerin nedenini yaz; 18:00/23:30'da bakılan her hisse için ayrı görsel + tweet bana gönder, teknik analizi ben paylaşırım (Buffer 1000/ay) | 14d, 14e, başlık |
| 14:07 | Teknik analiz tweetinde 'bence dibe yakın / ben şuradan kademe eklerim, kırarsa şuradan' dili; tavsiye yok, oyun planı başlığı yok, sade konuşma dili | 6, başlık |
| 14:05 | 21 göstergenin hepsi, tüm zaman dilimlerinde test edilecek; TradingView'da 2'şerli kapat-aç | 13, başlık |
| 14:00 | Teknik kontrollerde kararı destekleyen göstergeli grafik ekran görüntüsünü sohbete at | 14b |
| 13:58 | Profesyonel yatırımcı/analist yöntemi: temel + teknik, adayları portföyle karşılaştır, daha iyisi varsa öner yoksa önerme; sonraki devir notu bu kurallarla | 14c, başlık |
| 13:56 | Bu iki kuralı ekle, sonraki devirde kesinlikle böyle devam | başlık, A5, B |
| 13:33 | Tüm kurallarla kapsamlı devir notu yaz, hiçbir şeyi atlama, kanıtla | bu dosya |
| 13:07 kalıcı tercihleri (bellek): basit doğal tweet dili, soru ile bitirme yok, doğrulanmamış rakam yok, koyu minimal kart, X'e girme | 5, 6, 7, 10 |

## 19. DEVİR TESTİ (16.11 13:47)
- Temiz bir klasöre sıfırdan clone yapıldı. Dosyalar tam: DEVIR*, DONGU, ORNEKLER, kart.py, kart2.py, ta.py, ta2.py, font/, logo/, foto/, g/, gundem.md.
- Sıfır clone'dan kart2 ile kart üretildi ✓. ta2.py Yahoo'dan veri çekti ✓. raw.githubusercontent DEVIR_TAM.md 200 ✓. git kimliği tanımlı ✓.
- Tek bulunan sorun: ta2.py çıktısı `| head` ile kesilince BrokenPipe hatası veriyor. Çıktıyı dosyaya yaz, sonra oku (A3 d'ye işlendi).
- Test edilemeyen (yeni oturumda A3'te kontrol edilecek): yeni sohbette Buffer, GitHub ve zamanlayıcı araçlarının bağlı olması; Chrome eklentisinin o sohbete görünmesi.

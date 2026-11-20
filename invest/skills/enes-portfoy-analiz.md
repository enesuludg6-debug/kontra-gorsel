---
name: "enes-portfoy-analiz"
description: "Enes'in portföyü için ben olsam notları, aday hisse seçimi ve kıyas, temel karne (/50) yazılırken kullanılır."
---

# Portföy analizi: temel analiz, ben olsam notu, temel karne

Repo `/home/claude/kontra-gorsel/invest`. Ayrıntı ve geçmiş: `DEVIR_TAM.md` bölüm 11-14i ve kesin kural 37, `temel_karne.md`, `tez_kartlari.md`, `DONGU.md`. Her zaman Türkçe.

Güncel portföy: DOCN RKLB SITM AXON CBRS VRT AVGO NBIS (Enes 20.11 09:53: "NBİSTE EKLEDİM PORTFÖYE"; eski "NBIS YOK" kuralı GEÇERSİZ). Enes YATIRIMCI ve DİP AVCISI: iyi şirketi ucuzken toplamak ister.

## TEKNİK ANALİZ YOK (kesin kural 37, Enes 17.11 22:17: "teknik analize bakmıyoruz bir daha, onunla alakalı her şeyi kaldır, onun yerine temel analize daha da yoğunlaş")
- Gösterge, grafik, TradingView, ekran görüntüsü, destek/direnç, kademe seviyesi, teknik taslak YOK. ta2.py / ta_ek.py / seviye_takip.csv arşivde, kullanılmaz. 18:00/23:30 teknik kontrol zincirleri kapatıldı; 18:00 temel analiz görevi de kaldırıldı (kesin kural 44, 18.11).
- Eski kurallardan teknikle ilgili olanlar (12, 27, 30'un teknik kısmı, 31, 33, 35'in teknik ayağı, 36d/f'nin teknik kısmı, aday rotasyonundaki ekran görüntüsü) geçersizdir. Fiyat yalnız değerleme hesabı için kullanılır.

## Sınırlar (kesin)
- Bu notlar yalnız Enes'e özel (SendUserMessage). Tweette al/sat ASLA yok.
- Portföy güncellemesi tweetini Claude hazırlamaz/atmaz/sormaz; yalnız Enes açıkça isterse, formatı: ilk satır "PORTFÖY GÜNCELLEMESİ", altında Enes'in verdiği "YTD %X" ve "Günlük değişim %Y" aynen, boş satır, ABD hisseleri alt alta $TICKER. Tutar, para, ağırlık asla.

## 1. Temel analiz yöntemi (18:00 ZAMANLANMIŞ GÖREVİ KALDIRILDI, kesin kural 44, 18.11; 23:30 görevi de yok. Aşağıdaki yöntem turlarda, bilanço sonrasında ve Enes isteyince kullanılır.)
Sıra ve içerik (Enes'e mesajlar sade dille, deyim yok):
1. HABER VE BELGE TARAMASI (7 portföy hissesi + ilgi listesi kısa tarama): son 24 saatte 8-K, Form 4 (P kodlu alım ayrı), 13D/G, analist not/hedef ve tahmin revizyonu, rehber değişikliği, sözleşme/müşteri haberi, sektör verisi. Tez kartını etkileyen her şey hisse başına 1-2 cümle; etkisi yoksa "değişiklik yok".
2. KARNE: günde en az 2 karne yenilenir/yazılır (önce eksikler: RKLB SITM AXON CBRS VRT; sonra 7 günden eski olanlar; bilanço açıklayan aynı gün). Bölüm 4 tam yöntemi, kural 34 ekleri ve öz-denetim dahil. "Kısmi" yok.
3. TEZ KARTI KONTROLÜ (`tez_kartlari.md`): her portföy hissesi için tez (2-3 madde), tezi doğrulayan KPI'lar ve eşikleri, tezi bozan durumlar. Bugün bir KPI ya da haber eşiği geçtiyse açıkça "tez güçlendi / zayıfladı / bozuldu".
4. DEĞERLEME BÖLGELERİ (fiyatı yalnız buradan): ileri F/K, EV/Satış ya da FCF getirisi (şirkete uygun olan) ile kendi 3 yıllık bandı ve 3-5 akran medyanı. Bandın alt çeyreğine denk gelen fiyat aralığı = "ucuz bölge", ortası = "adil", üst çeyreği = "pahalı bölge". Ters DCF ile "bugünkü fiyat yılda %X büyüme varsayıyor". Rakamlar 2 kaynaklı, tek kaynaksa "(tek kaynak)".
5. KARAR (her portföy hissesi ve aday için tek satır): temel sınıf (GÜÇLÜ 34+/45, ORTA 26-33, ZAYIF 25 altı ya da kırmızı bayrak) × değerleme bölgesi (ucuz/adil/pahalı) × tez durumu. Tablo: GÜÇLÜ+ucuz → ekleme bölgesi | GÜÇLÜ+adil → tut, ucuz bölgeye gelirse ekle | GÜÇLÜ+pahalı → tut, eklemeyi bekle | ORTA+ucuz → küçük ekleme ancak tez güçleniyorsa | ORTA+adil/pahalı → tut ya da daha iyi adaya geçişi düşün | ZAYIF ya da tez bozuldu → azaltmayı düşün. Biçim: "KARAR (temel): GÜÇLÜ 37/45 + ucuz bölge (ileri F/K 24, 3 yıllık bant 22-38) + tez sağlam → ben olsam 310-325 aralığında eklemeyi düşünürdüm."
6. ADAYLAR: her gün farklı 2-3 aday (`python3 periyot.py etiket kontrol aday <T> 5`, kullanınca `etiket yap aday <T>`); her biri TAM karne + tez kartı + değerleme bölgesi + KARAR. Karnesi olmayan aday yalnız "izle".
7. KIYAS: adaylar portföyün en zayıf 2 hissesiyle (/45, büyüme kalitesi, değerleme bölgesi, risk) yan yana; aday AÇIKÇA iyiyse "Ben olsam Y'yi azaltıp X'e geçmeyi düşünürdüm, çünkü ..."; değilse "portföydekilerden daha iyisini bulamadım" ve neden. Zorla öneri yok.
8. ÖZET TABLO: hisse | /45 | değerleme bölgesi | tez | KARAR. DONGU'ya `- SS:DD TEMEL: ...`, temel_karne.md ve tez_kartlari.md güncellenir, push.
- ZAMAN KUTUSU (kural 36d): 60 dk içinde bilanço/veri YAYIN görevi varsa görev yayından 15 dk önce biter (haber taraması + KARAR satırları + 1 karne; kalan sonraki güne not).
- ABD tatilinde (26.11, 25.12, 1.1) piyasa kapalı olsa da temel görev yapılır (karne ve aday günüdür); yarım günde aynı.

## 2. Ben olsam dili
- Yalnız Enes'e: "Ben olsam bugün RKLB'den biraz eklerdim, çünkü fiyat değerleme bandının alt çeyreğinde ve backlog büyümesi hızlanıyor." / "Ben olsam AXON'a eklemeyi beklerdim, ileri satış çarpanı kendi bandının üst kısmında." / "Ben olsam X'te tez bozulduğu için azaltmayı düşünürdüm." Karar Enes'in. Tavsiye/öneri dili yok.
- Kısa format: hisse + ne oldu (haber/rakam) + değerleme bölgesi + tez durumu + "ben olsam ...".
- Otomatik turlarda tweetten sonra portföy hisselerinde haber/8-K/analist taraması yapılır; teze dokunan bir gelişme ya da değerleme bölgesi değişikliği varsa not atılır.

## 3. Hisse seçimi (profesyonel yöntem, 14c)
A) Temel kontrol listesi (13 madde): iş ve hendek (müşteri yoğunlaşması %20+ risk); büyüme (YoY, QoQ, hızlanma, organik pay, backlog/RPO); kârlılık (brüt/faaliyet marjı, GAAP-düzeltilmiş farkı, SBC); nakit (FCF, capex, runway); bilanço (net nakit/borç, vade, seyrelme); değerleme (ileri F/K, EV/Satış, EV/FAVÖK, PEG, FCF getirisi; akran ve kendi geçmişi; Rule of 40); beklenti momentumu (30-90 gün revizyonlar, aşım/kaçırma, rehber); analist ve kurum (not/hedef, 13F, Form 4); pozisyonlanma (açığa satış, opsiyon ima edilen hareket); katalizör takvimi; riskler; yönetim ve sermaye dağıtımı; makro ve sektör rejimi.
B) (Teknik bölümü kural 37 ile kaldırıldı.)
C) Aday bulma: tüm ABD borsası (izleme listesiyle sınırlı değil): haberler, revizyonu yukarı olanlar, güçlü bilanço + düşük değerleme, sektör gücü, değerleme bandının altına inmiş kaliteli şirketler, içeriden P kodlu alım kümeleri → kısa liste 6-10 → eleme → en iyi 2-3. Kartı olmayan aday değişim önerisine konu olamaz.
D) Portföyle karşılaştırma: bölüm 1 madde 7. Toplamın yanında "en zayıf 2 başlık" ve "kırmızı bayrak var/yok". Tez bozulan portföy hissesi açıkça söylenir.

## 4. Temel karne (`temel_karne.md`, /50)
- TEMEL ANALİZ EKLERİ (kesin kural 34, Enes 17.11 21:43: "temelini de geliştir"; mevcut 10 başlık /50, /45, metrik listesi, öz-denetim ve kırmızı bayraklar AYNEN, yalnız ekleme): her karnede ayrıca (a) KARNE TRENDİ: önceki karneye göre her başlıkta ve toplamda değişim (↑/↓/=) ve sebebi; (b) BEKLENTİ REVİZYON GENİŞLİĞİ: son 30/90 günde HBK ve gelir tahminindeki % değişim + yukarı/aşağı revize eden analist sayısı (2 kaynak); (c) KAZANÇ KALİTESİ: serbest nakit / net kâr, tahakkuk oranı, SBC/gelir eğilimi, tek seferlik kalemlerin payı; (d) ARTIMLI MARJ ve faaliyet kaldıracı: son 4 çeyrekte gelir artışının ne kadarı faaliyet kârına dönüştü; (e) KPI İVMESİ: sektöre özel ana KPI'ın son 3-4 çeyrekte hızlanıyor mu yavaşlıyor mu; (f) BİLANÇO STRESİ: küçük ve borçlu şirketlerde Altman Z, nakit pisti (ay), yakın vade borç; (g) DEĞERLEME BANDI: ileri F/K ya da EV/Satış'ın kendi 3/5 yıllık ortalamasına göre konumu (aylık bant görevinden ya da 2 kaynakla); (h) BİLANÇO TEPKİ GEÇMİŞİ: son 4 çeyrek aşım/kaçırma ve ertesi gün hisse tepkisi; (i) TEZ KARTI: her portföy hissesi için 3-5 maddelik yatırım tezi + "tezi bozan 3 sinyal"; her karnede maddeler tek tek güçlendi/zayıfladı/aynı diye işaretlenir. Eksik portföy karneleri (temel_karne.md'de "eksik" olanlar) bitene kadar her otomatik turun "zaman kalırsa karne" adımı ÖNCE portföy eksiklerini doldurur.
- Ne zaman: her otomatik turda tweetten ve DONGU'dan sonra 1-2 hissenin kartı (eksik/en eski önce; rotasyon tablodaki sıra + yeni adaylar). Kontrolün içine sıkıştırılmaz; kontrol karneyi buradan okur. "Kısmi" deyip geçmek yasak. 7 günden eski ya da arada bilanço/rehber/büyük haber varsa yenilenir; bilanço açıklayan portföy hissesi aynı gün. 13F/bilanço günü zaman darsa atlanabilir.
- 10 başlık x 1-5: BÜYÜME, KÂRLILIK, NAKİT, BİLANÇO, DEĞERLEME, MOMENTUM, SAHİPLİK/AKIŞ, GÖRECELİ GÜÇ, KALİTE/YÖNETİM, RİSK/KATALİZÖR (RİSK'te 5 = düşük risk). Her başlığa 1 cümle gerekçe ("akrana göre" dahil). GÖRECELİ GÜÇ hariç /45 de yazılır (teknikle çift sayılmasın).
- Metrikler (DEVIR_TAM 14h tam listesi): gelir YoY/QoQ ve 4-8 çeyrek trendi, segment/coğrafya, organik pay, backlog/RPO/book-to-bill, ARR/NRR; marj trendleri, gider yapısı, SBC/gelir, ROIC vs WACC, Rule of 40; FCF, FCF dönüşümü, SBC düşülmüş FCF, capex ve gizli capex, DSO/DIO/DPO; net borç/FAVÖK, faiz karşılama, vade takvimi, konvertibl, seyrelme; F/K, PEG, EV/Satış, EV/FAVÖK, FCF getirisi vs 10 yıllık tahvil, 3-5 akran medyanı, kendi geçmiş aralığı, ters DCF, ayı/baz/boğa 12 ay senaryosu; revizyonlar 7/30/90 gün, aşım geçmişi ve tepki; Form 4 (P ayrı), 13F, açığa satış, opsiyon IV ve ima edilen hareket; 1h/1a/3a/YTD/1y getiri vs S&P ve sektör ETF'i, 52 hafta, beta; hendek, müşteri/tedarikçi yoğunlaşması, yönetim ve muhasebe kırmızı bayrakları; risk ve katalizör takvimi. Sektöre özel KPI zorunlu (neo-bulut: sözleşmeli güç, GPU kullanımı, finansman; yarı iletken: book-to-bill, stok günleri, son pazar dağılımı; uzay: backlog, fırlatma sıklığı, Neutron; SaaS: ARR, NRR; altyapı: sipariş, backlog; yeni halka arz: müşteri yoğunlaşması, lock-up).
- Kaynaklar: WebFetch `stockanalysis.com/stocks/<t>/statistics/`, `/financials/?p=quarterly`, `/financials/cash-flow-statement/?p=quarterly`, `/financials/balance-sheet/?p=quarterly`, `/forecast/` (veri tarihini yaz); şirket IR; WebSearch bilanço haberleri (Reuters, CNBC, Barchart, Earnings Whispers), analist notları (Benzinga, MarketBeat, TipRanks, TheFly), içeriden (OpenInsider, secform4), açığa satış (Nasdaq, MarketBeat), opsiyon (Barchart, Market Chameleon), 13F (WhaleWisdom). Her rakam 2 kaynak, tek kaynaksa "(tek kaynak)", bulunamayan "bilinmiyor" (uydurma yok). Başlık boş geçilmez.
- Öz-denetim (14i-A, her karneden sonra, karnenin sonuna "DENETİM: A1 ✓, A2 düzeltildi (...)"): A1 eski fiyat/veri (çarpanları bugünkü fiyatla yeniden hesapla); A2 birim (milyon-milyar, çeyrek-yıl); A3 yıl/dönem ve mali yıl; A4 tek kaynak ağırlığı ("güven düşük", puan 2-4); A5 GAAP-düzeltilmiş tutarlılığı (fark gelirin %10'undan büyükse KÂRLILIK -1); A6 bölünme/seyrelme; A7 tutarsız analist hedefi puana girmez; A8 sektöre göre adalet (akran eşiği); A9 çift sayım; A10 inorganik büyüme (organikle puanla); A11 bilinmeyen ceza değil; A12 yeni halka arz; A13 portföy yanlılığı ("tanımadığım şirket olsaydı kaç verirdim?"); A14 günün haberi yalnız MOMENTUM ve RİSK'e; A15 anlatı yanlılığı (her puan en az 1 rakama dayanır); A16 senaryo çarpanları geçmişe/akrana bağlı mı; A17 eşit ağırlık (toplam tek başına karar değil).
- Kırmızı bayraklar (toplamdan bağımsız yazılır): tek müşteri gelirin %25'inden fazla; nakit 4 çeyrekten az ve finansman yok; net borç/FAVÖK > 4; rehber üst üste 2 çeyrek düşürüldü; muhasebe uyarısı/restatement/denetçi değişikliği/SEC soruşturması; yıllık seyrelme %10'dan fazla; açığa satış float'ın %15'inden fazla.
- Kalibrasyon (her 5 karnede bir + her gün ilk turda): karneleri yan yana oku, sıralama mantıklı mı; çapalar: 5 = akranların en iyi %20'si, 3 = medyan, 1 = en kötü %20 ya da kırmızı bayrak; DONGU'ya "KALİBRASYON: ...".
- Hata günlüğü: bulunan her hata `DEVIR_TAM.md` 14i-D'ye; yeni hata türü 14i-A'ya madde olarak. Her karnede "sonucu en çok değiştiren varsayım" DENETİM satırına. Pazar günü Enes'e "karne sisteminde bu hafta düzelttiklerim" özeti. Enes bir puana itiraz ederse 14i-D'ye yaz ve aynı hatayı diğer karnelerde ara.
- Tablo güncellenir (/50 ve /45 sütunları), DONGU'ya `KARNE: <hisse> <toplam>`, commit + push.
## Kural 22 eklemeleri (17.11 14:35)

- İlgi listesi genişledi: ON AAOI HOOD TEM CRDO PLTR ISRG ASTS MU + ANET ALAB MRVL COHR LITE ETN GEV CRWD NET DDOG APP RBRK PL LUNR. Yeni adayların karnesi turlarda günde 1-2; 30/50 altı listeden çıkar (DURUM.md "İlgi listesi").
- Analist hedef özeti (ayın ilk Pazarı 12:25) ve değerleme bandı (ayın ikinci Pazarı 12:25) sabit görevi: portföy + ilgi listesi + adaylar; Enes'e not, en çarpıcısı tweet. Değerlemede "ucuz/pahalı" değil "kendi geçmişine göre yüksek/düşük".
- "Ben olsam" notlarında eski tahminin tutmadığı tweete taşınmaz (kural 23); Enes'e özel notta durum dürüstçe yazılır.

- PERİYOT DEFTERİ (kural 24): karne, kalibrasyon (her 5 karnede bir), analist özeti (ayın 1. Pazarı) ve değerleme bandı (2. Pazar), Pazar karne sistemi özeti `python3 periyot.py kontrol <anahtar>` ile kontrol edilir, yapılınca `python3 periyot.py yap <anahtar>`. Hafızadan "bu ay yapılmış mıydı" tahmini yapılmaz.

- PERFORMANS DERSLERİ (kural 26): sabah görevi ve Pazar 21:30 raporu DERSLER.md'yi günceller; Pazar raporunda "bu hafta öğrendiklerim" Enes'e gider.
- TASARRUF (kural 28): karne verisi stockanalysis sayfalarından tek seferde dosyaya; haber taraması tek WebSearch turunda hisseler birlikte; değerleme bandı hesabı python ile.


## Kural 29 ve 36 eklemeleri (17.11)
- 18:00 temel analiz bu sohbette send_later zinciridir (`python3 invest/sonraki.py temel1800`, sonra `gorevler/_ORTAK.md` + `gorevler/temel1800.md`). Adaylar yalnız bu görevin içinde.
- Bu skill ile `invest/skills/` kopyası çelişirse kopya geçerli.

## Enes'in teknik analizinden tweet (kesin kural 38)
ENES'İN TEKNİK ANALİZİNDEN TWEET (kesin kural 38, Enes 17.11 22:30: "artık teknik analizi ben sana atacağım, sen de tweet yazım kurallarına bakıp sade dilde, mecaz kullanmadan yazacaksın ve bana tweeti yollayacaksın").
- Enes teknik analizini (metin, sesli not ya da grafik görüntüsü) atınca: Claude kendi teknik analizini YAPMAZ, gösterge/seviye EKLEMEZ, Enes'in seviye ve görüşlerini değiştirmez; yalnız onları tweet diline çevirir.
- Yazım kuralları aynen: arkadaşına anlatır gibi sade cümle; DEYİM/MECAZ YOK ("hikâye değişir/biter", "resim bozulur", "asıl sınav", "kapı açılır", "nefes alıyor", "ters köşe" vb. yerine düz ve ölçülebilir cümle: "69'un altında günlük kapanış gelirse düşüş devam edebilir"); terimler sade (FVG = boşluk, order block = alıcıların daha önce toplandığı bölge, Supertrend = trend göstergesi); etiketli giriş ve paragraf başında "X şu:" yok; emoji, hashtag, mention, link yok; soruyla bitmez; okura emir kipi ve al/sat tavsiyesi yok ("ben şuradan eklerim" Enes'in kendi dili olarak kalabilir, "alın" yok); "aldım", portföy, tutar, ağırlık yok; Anthropic adı geçmez.
- Grafikte okunamayan değer uydurulmaz; eksik ya da çelişkili bir şey varsa tweet yine yazılır, altına Enes'e tek cümle not.
- Çıktı: Enes'e SendUserMessage ile kopyalanmaya hazır tweet metni (gerekirse 1 kısa alternatif). Claude bu tweeti PAYLAŞMAZ, Buffer'a göndermez; Enes kendisi atar. DONGU'ya "- SS:DD ENES-TA-TASLAK: <ticker>" satırı.

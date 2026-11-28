# KURAL DİZİNİ — GÜNCEL, ÇELİŞKİSİZ (sadeleştirme 27.11 19:40, Enes "hepsini yap", kural 101)
Eski 106 satırlık dizin hiçbir şey silinmeden `KURAL_DIZINI_ARSIV_2711.md`'de; tam metinler `KURALLAR_TAM.md` ve `skills/*.md`. Burada her kuralın YALNIZ GÜNCEL hâli var. Ayrıntı gerekirse arşivde ya da skill'de o kuralı grep'le aç. Yeni kural gelince: buraya tek satır, eski hâli varsa burada GÜNCELLE (yan yana iki rakam bırakma), eskisini arşive ekle.

## A. Kilit ve akış
- 17 Kilit: görev mesajındaki HESAP=X ≠ AKTIF_HESAP.md → hiçbir şey yapma. tur_basi.sh çıkış 2/3 ya da DONGU'da `DURDUR` → dur.
- 29 Her mesaj bu sohbete (SendUserMessage/SendUserFile). Sabit görevler send_later zinciri (`sonraki.py <anahtar>`), İLK İŞ sonrakini kur; aynı adlı bekleyen varsa kurma.
- 99 Tur talimatı `gorevler/tur.md` (KISA ŞABLON ile zincir); sayaçlar `gun_ozet.py`; yayın kapısı `yayin_kontrol.sh <TUR> <KALIP> < metin` → GEÇTİ.
- 100 Buffer hook'u (`buffer_kapi.py`) GEÇTİ almamış/değişmiş metni durdurur. Gönderim öncesi Enes gözüyle son okuma (tur.md 7-C).
- 43/76 Zamanlı her iş `isler.py` (ekle/durum/devir); iptal yalnız Enes'in sözüyle.
- 24 Periyotlu işler `periyot.py`. 44 18:00 ve 23:30 analiz görevleri YOK.
- EKSİK BULUNCA Enes'e sorma; tek cümleyle ne yapacağını söyle, yap.

## B. Hacim, zaman, biçim (TEK geçerli rakamlar)
- 112 (Enes 28.11 12:20, 98'in sayılarını değiştirir) Pencere 11:00-02:00 TSİ. Sistem tweeti HER GÜN (hafta sonu dahil) EN AZ 20, EN ÇOK 40. Sistem tweetleri arası EN AZ 20 dk, tur aralığı 20-30 dk, turda 1-2 tweet. Konu eşiği konu_puan ≥60 (son dakika, bilanço, 2 kaynaklı haber, K107/K108/K111 her zaman yeterli); alt sınıra yetişmek için tur boş geçmez, zayıf konu yerine açıklayıcı/eğitici/tarihsel/veri tweeti atılır. Aynı tema günde en çok 2.
- 98 Biçim her gün: ≥3 kartsız (1-2 cümle, görselsiz), ≥2 tartışma açan görüş (soru işaretsiz), kalanı kartlı; art arda iki tweet aynı biçimde olmaz.
- 98/69 ENES-TASLAK hafta içi 6 (11-13, 13-15, 15-17, 17-19, 19-21, 21-24), Cmt 3, Paz 2; Buffer'a gitmez; altına "Atarsan ilk 1 saatte gelen yanıtlara cevap ver."
- AÇIKLAYICI (haberi tek kavramla) hafta içi ≥5, hafta sonu ≥2. EGITICI 20-23 günde 1 (86-d). TARIHSEL günde 1-2, yalnız tabandan belirgin iyiyse (96).
- 79 Açılış: günün çift sıradaki tweeti iddia açılışı (≤12 kelime, rakamla başlamaz), tek sıradaki normal (A/B 08.12'ye kadar).
- 87 Konu `konu_puan.py`; 7 gün tekrar yok (DONGU + performans_veri). 85 Hisse-faiz ayrışma sinyali tur adayı.

## C. Konu alanı
- 46/55/73 Yalnız yapay zekâ (çip, bellek, ağ, bulut, veri merkezi enerjisi, YZ yazılımı, siber güvenlik), uzay, Nasdaq/büyük teknoloji + bunları etkileyen makro; portföy ve tedarik zinciri dahil. Perakende, banka, sanayi, ilaç, emtia yok.
- 59 Görüş Enes profiliyle (ENES_GORUS_PROFILI.md): YZ altyapısına inanan, dip toplayan uzun vadeli yatırımcı; YZ'yi toptan kötüleme, kötü veriyi gizleme.
- Bilanço: 49 konsensüs tweeti (30-60 dk önce, 71 belirleyici kalem) → rakam (yorumsuz) → 15 dk sonra analiz (45). Bilanço başına en çok 6 tweet (67). 51 dönem = takvim çeyreği + mali çeyrek.
- 37/38 TEKNİK ANALİZ TWEETİ YOK. Enes'e özel teknik analiz serbest ve yetenek enes-teknik-smc'nin TÜM adımlarıyla yapılır (çizim, seviye testi, kanıt kuralı); otomatik tweet olmaz.
- Sabit veri zincirleri (90-93, 97): korku Sal-Cmt 10:40, AAII Per 18:40 + Sal 12:40, vix Cum 18:10, kredi Çar 12:10, genişlik Cmt 12:10, putcall Cmt 15:10, açığa Pzt 12:10, fed Cum 12:10, içeriden Per 12:10, faiz Pzt 16:10 (çift), fedwatch Sal 18:10, kuyruk Per 16:10, korelasyon Çar 16:10 (tek), rotasyon Paz 16:10, faktör Cum 16:10, bakır/altın Sal 16:10 (tek), revizyon Pzt 18:10, kalabalık Cmt 18:10. Ayrıntı `gorevler/<anahtar>.md`. Veri değişmediyse tweet yok.
- 66 Ölçülebilir yorum içeren tweet → `isler.py ekle TEST-...`; olay açıklanınca sınanır. 23/56-B Yalnız TUTAN beklenti yazılır, tutmayan hiç anılmaz.
- 88 Numaralı seri yok. Anthropic adı/konusu yok. x.com'a girilmez. Enes'in kendi attığı konu tekrar edilmez.

## D. Doğrulama
- 3/16 Her rakam 2 bağımsız kaynak; tek kaynak = "civarı" (78, `fiyat_teyit.py`). 75 Resmi bültenin alt kalemleri birincil kaynakla yazılabilir. 21 Yanlış rakamda düzeltme tweeti.
- Kartta grafik ham veriyle birebir (84); başlık güncel fiyatla çelişmez; kanıt satırında taban oran (vix kartı dersi 27.11).

## E. Yazım (yasak.py + kalite.py + gorus.py otomatik yakalar)
- 102 SES (her tweet, istisnasız): Enes'in kendi tweetleri gibi; `ses_kontrol.py` yayin_kontrol içinde DUR verir; kural 60/89 içerik içindir, kelimede Enes sesi kazanır; her tur yazmadan önce `python3 invest/ses_ornek.py` (3 gerçek Enes örneği + ses özellikleri, kural 101). Kural listesi değil örnek önce.
- Uzunluk: HABER 600, görüş/portföy 800, EGITICI 900, derin analiz 1200. İlk satır ≤12 kelime. En çok 3 farklı rakam (TARIHSEL muaf), en az 2 doğrulanmış.
- Her tweet: haber + yorum, birinci tekil net görüş (25/50), görüş ifadesi tekrar etmez (50-B gorus.py), "bence" en çok 1.
- Analiz açısı kalıbı A-N (63-B/C/D): birincil kalıp son 4'te yok, yapı imzası son 3'te yok, kapanış türü son 2'de yok (89-B).
- 65 İkinci katman veri, 74 iki uzmanlık izi (U1-U6), 89 fon yöneticisi düşünme sırası (en az 3'ü) — süssüz.
- 62 Jargon tweet başına en çok 1. 64/64-B "izleyeceğim/merak ediyorum" ailesi en çok 1, tweet onunla bitmez.
- YASAK KALIPLAR (54-54-H): etiketli giriş ("Not:", satır başı "X:"), "okuyorum/okumam", iki tarafı dengeleme, ruh hâli klişesi, mecaz/dramatik sahne, sunucu açılışı, veriye konuşma yükleme ("rakamlar başka hikâye anlatıyor"), rakamsız "X tarafı güçlü", "asıl X", "masadaki soru", "saymam / olarak görüyorum / aynı gözle", süslü vecize kapanış ("risk masada kalır", denklem, terazi, ibre, tabloyu bozar, pusula, perde aralandı). Kapanış düz ve rakamlı koşul.
- YASAK: al/sat, hedef fiyat, emoji, hashtag, @, link, soruyla bitirme, portföy tutarı/ağırlığı.

## F. Kart, yayın, kayıt
- 104 GÖRSEL STANDARDI (Enes 27.11 23:53 'görseller bunlar olacak artık'): VARSAYILAN kart4 ailesi (14 tür, g/tur/ katalog, skill enes-gorsel tablosu); kart3 yalnız kart4'te karşılığı olmayan özel düzen için. Son 3 tweette kullanılan tür tekrar yok, logo büyük, Read ile bak, denetim temiz, `yayinla_gorsel.sh` OK + raw URL 200.
- Buffer: org 6af5719777bce44fa736607b, kanal 6af99a1aece6dfde5fd109c7, automatic; 35 dk dolmadıysa customScheduled.
- 47 Her tweetten sonra Enes'e "Paylaşıldı + Ne anlama geliyor?" (3-6 madde).
- 26 Kayıt: `kayit.py` (--kaynak YALNIZ sistem|enes), `kalite.py kaydet`, `gorus.py kaydet`; DERSLER.md aktif dersler.
- 68 Geliştirme fikri: tur başına en çok 1, günde en çok 6, 02-09 arası yok.

## G. Enes'e özel (tweet değil)
- Portföy "ben olsam" notları ve aday karşılaştırma: skill enes-portfoy-analiz. 94 Unusual Whales ekranı → akis_puan.py. IB gerçek emir Enes'in ayrı açık onayı olmadan YOK.
- 103 (27.11 23:39) Kart denetimi: kart3.denetle taşma/çakışma bulursa .denetim dosyası yazar, yayinla_gorsel.sh yayınlamaz. Olay etiketi doğru güne, kanıt satırında taban oran.
- 105 (27.11 23:57) Takipçi psikolojisi: skill enes-takipci-psikolojisi; her tweet en az 1 kaldıraç (K1-K17), DONGU'ya 'psiko: Kx'; günde ≥2 kişisel kendini açma, mesleki övünme haftada ≤1, her ölçülebilir yorum açık döngü (TEST), seri tema bağı, haftada 1 kaydetmelik içerik; sahte aciliyet/FOMO/uydurma sosyal kanıt YASAK.
- 106 (28.11) X NABZI ücretsiz: WebSearch allowed_domains [x.com, twitter.com] ile herkese açık tweetler (X'e giriş/WebFetch/otomasyon YOK); tur başına en çok 2 arama; tweet içeriği kaynak değil, rakam yine 2 kaynak; ayrıntı X_NABIZ.md.
- 107 (28.11) Enes'in favori 4 hesabı (StockSavvyShay, aleabitoreddit, Venu_7_, DSAkdag): her tur X nabzı aramalarından en az 1'i bunlardan, sırayla; fikir alınır cümle alınmaz, isim anılmaz, rakam yine 2 kaynak, Pazar format dersi; ayrıntı X_NABIZ.md.
- 108 (28.11) TA-STİL günde 1: takip hesaplarının AYNI GÜN teknik tweetleri (dünkü yok) → kendi analizimizle karşılaştır → en beğenilenin çizim tarzında benzer ama birebir olmayan kendi grafiğimiz (stil_cizim.py) → Enes sesinde görselli tweet, sistem atar. Hafta içi ≥23:00, hafta sonu ≥19:00 ilk tur. Enes'in kendi TradingView'lı teknik tweetleri ayrı, o kural aynen.
- 108-K (28.11 11:43) TA-STİL'de onların tezi/çizgisi kabul; bizim analiz yalnız beğenme süzgeci (çizim net mi, veri doğru mu), farklı görüş tweete yazılmaz.
- 54-H ek (28.11): 'ciddiye alıyorum' / 'Bu yüzden ben ...' kanaat kalıbı yasak.
- 109 (28.11) Tweetlerde şirket adı yerine $TICKER ($TSLA, $NVDA'nın); yasak.py SIRKET_TICKER yakalar. Taslak ve kart başlığı dahil.
- 110 (28.11) Günlük alt sınır: TA-STİL ≥2 (hafta içi ≥19:00 ve ≥23:00, hafta sonu ≥11:00 ve ≥19:00), TEMEL-FİKİR (K107 hesapları) ≥1; üst sınır yok, günlük toplam içinde öncelikli; gun_ozet sayar.
- 54-H ek-2 (28.11): 'kalabalık henüz inanmadı / piyasa ikna olmadı' kişileştirme kalıbı yasak.
- 111 (28.11) PATLAYAN TWEET AVCISI: kaynak YALNIZ yabancı/İngilizce finans hesapları (Türk hesaplar sadece kıyas); günde EN AZ 2 K111 tweeti; görüntülenme ≥5x takipçi ve ≥10B olan finans tweetinin nedenini çıkar, aynı konu/biçimde kendi verimiz + Enes sesiyle yaz (kopya/çeviri yok, isim anılmaz); konu 'K111'; 48 saat sonra kıyas.
- 54-H ek-3 (28.11): 'Yönü X belirler / son sözü X söyler' kehanet kapanışı yasak.
- 113 (28.11 19:26) Enes sesi + ÇOK ÜST DÜZEY BORSACI: net hüküm + seviye, 2-3 doğru borsacı terimi (kalite sınırı 1->3), en az 1 masa detayı (fiyatlanan / beklenti farkı / pozisyonlanma / tetikleyici / geçersiz kılan seviye), tereddüt kelimesi yok; taslak ve açıklamalar dahil. Ses Enes, içerik kıdemli borsacı.
- 113-B (28.11 19:29 'daha da prof') kalite.py ZORUNLU: en az 3 borsacı öğesi, tereddüt kelimesi yok (olabilir/sanırım/galiba/belki/muhtemelen/düşünüyorum), 'bence' ≤1, somut rakam; sıra olgu -> fiyatlanan/beklenti farkı -> benim seviyem -> tezi bozan eşik.
- 113-C (28.11 19:30 'yetmez') kalite.py ZORUNLU: en az 4 borsacı öğesi + iki çapa (değerleme/beklenti VE risk/eşik); hedge fon sabah notu düzeyi, her terim bir rakama bağlı.
- 113-D (28.11 19:33 'olmaz daha da prof') kalite.py ZORUNLU: kıyas çapası (endeks/akran/tarihsel/konsensüs), farklı görüş (piyasa ne fiyatlıyor + ben nerede ayrışıyorum), amatör dil yasağı (güzel, uçtu, fırsat, alım gerçek...), jargon sınırı 5; yapı olgu+kıyas -> fiyatlanan -> benim tezim -> asimetri+teyit+bozan seviye.
- 113-E (28.11 19:35) kalite.py ZORUNLU: fiyat dışı rakamlı kurumsal metrik (çarpan, marj, konsensüs, revizyon, rehber, EPS, ima edilen hareket) + iki yönlü senaryo (üstü teyit VE altı bozar); veri önceliği şirket belgesi > konsensüs > kendi hesap > haber.
- 113-MAX (28.11 19:37 'EN YÜKSEK PROFESYONELLİK') tek standart en yüksek: 113-B/C/D/E + her tweette kıdemli PM editör geçişi (5 soru: yeni açı, konsensüs rakamı, ayrışılan değişken, rakamlı asimetri, gereksiz kelime yok), en az 1 birincil/konsensüs verisi, ölçülebilir tez (kural 66), DONGU 'PM: a✓..e✓'.
- 113-F (28.11 19:40) Profesyonel VE anlaşılır: en ağır terim aynı cümlede 'yani ...' ile açılır (kalite.py zorunlu); aynı iskelet tekrarlanmaz, 6 biçim döner (makas, o zaman/şimdi, senaryo, akran, tersine hesap, takvim), son 3'te kullanılan biçim yok.
- 113-G (28.11 19:42) Ben dili, insan konuşması: profesyonel içerik aynı, yazış arkadaşına anlatır gibi; terim parantezde + günlük dille anlamı ('yani aynı kâr için yarı fiyat ödüyorsun'), kendi davranışı/duygusu ('acele etmiyorum', 'daha rahat ederim', 'yanıldığımı kabul ederim'), kısa satırlar.
- 114 (28.11 19:45) YZ yazım izleri yasağı: yasak.py YZ114 (X değil Y, sadece X değil Y de, üçlü yığın, uzun tire, retorik soru, hazır açılış, tezi bozar/teyit eder, acele etmiyorum/daha rahat ederim/yanıldığımı kabul ederim, masa/pusula mecazı, kritik/kilit rol/çığır açan, gözler X'te/zaman gösterecek, sonuç olarak/özetle, işaret ediyor, temkinli iyimser...). 113 örneklerindeki bu kalıplar geçersiz. Liste: YZ_IZLERI.md.
- 114-B (28.11 20:22) ek yasaklar: tekrar ettiğimiz kalıplar (tek başına sinyal değil, benim gördüğüm risk, aşırı tepki, kendi ölçeğimde), borsa gazetesi klişeleri, boş güçlendiriciler, bağlaç ≤1, sahte samimiyet, 'yani' ≤1, belirsiz zaman; + aynı gün tekrar yasağı (açılış, kapanış fiili, hüküm kelimesi; kalite.py).
- 115 (28.11 20:24) KREDİ TASARRUFU: skills/enes-kredi-tasarruf.md. Grep ile oku, komutları birleştir, çıktıyı kırp, arama standard ve tur başına ≤3, veri turda 1 kez, propose_skills günde ≤2 toplu (repo anında geçerli), mesaj kısa, taslak havuzu; doğrulama/kapı/kilit/kayıt/zincir/alt sınırlar ASLA kısılmaz.

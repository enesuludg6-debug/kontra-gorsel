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
- 98+95 Pencere 11:00-02:00 TSİ. Sistem tweeti hafta içi 15-20, Cmt/Paz en çok 8. Yalnız GÜÇLÜ konu (konu_puan ≥75, son dakika, bilanço, 2 kaynaklı yeni haber); zayıfsa tur tweetsiz kapanır. Sistem tweetleri arası EN AZ 35 dk, tur aralığı 35-50 dk, turda 1 tweet. Aynı tema günde en çok 2.
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
- kart3 varsayılan, son 3 düzen tekrar yok, logo büyük, Read ile bak, `yayinla_gorsel.sh` OK + raw URL 200.
- Buffer: org 6af5719777bce44fa736607b, kanal 6af99a1aece6dfde5fd109c7, automatic; 35 dk dolmadıysa customScheduled.
- 47 Her tweetten sonra Enes'e "Paylaşıldı + Ne anlama geliyor?" (3-6 madde).
- 26 Kayıt: `kayit.py` (--kaynak YALNIZ sistem|enes), `kalite.py kaydet`, `gorus.py kaydet`; DERSLER.md aktif dersler.
- 68 Geliştirme fikri: tur başına en çok 1, günde en çok 6, 02-09 arası yok.

## G. Enes'e özel (tweet değil)
- Portföy "ben olsam" notları ve aday karşılaştırma: skill enes-portfoy-analiz. 94 Unusual Whales ekranı → akis_puan.py. IB gerçek emir Enes'in ayrı açık onayı olmadan YOK.

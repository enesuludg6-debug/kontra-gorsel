# X NABZI — ücretsiz, hesapsız X takibi (kural 106, Enes 28.11 11:08 "ücretsiz halini yap")
Yöntem: WebSearch aracı `allowed_domains: ["x.com", "twitter.com"]` ile. Arama motorunun dizinindeki herkese açık tweetleri (metin, yazar, tarih, çoğu zaman görüntülenme ve yanıtlar) getirir. X'e GİRİLMEZ, x.com WebFetch EDİLMEZ, hesap/çerez/otomasyon YOK -> Enes'in X hesabına sıfır risk (X kuralları tarama/otomasyonu yasaklar; bu yol X'e bağlanmaz, arama motorunu kullanır). 28.11 testi: Nvidia/Huang araması NYT, Reuters, White House, Balaji, Peter Schiff tweetlerini görüntülenme sayılarıyla getirdi.
Sınır: her tweeti değil, arama motorunun dizinlediklerini görür; en yeni dakikalar eksik olabilir; gizli hesap/DM yok.

## Ne zaman
- Her tur, KONU adımında (tur.md 3) 1-2 arama: (a) portföy/gündem hissesi "<şirket> <olay>" , (b) takip listesinden bir hesap ya da tema. Toplam en çok 2 arama/tur (kullanım limiti).
- Sabah performans görevinde (perfogren) 1 arama: dünün en çok konuşulan YZ/çip konusu.
- Enes bir konu sorduğunda serbest.

## Takip listesi (Enes düzeltir)
Haber/kurum: Reuters, Bloomberg, CNBC, WSJ, FT, nytimes, business, markets, zerohedge (yalnız başlık, teyitsiz rakam alınmaz), unusual_whales, DeItaone (Walter Bloomberg), FirstSquawk.
Şirket: nvidia, AMD, Marvell, Broadcom, Tesla, elonmusk, sama, OpenAI, AnthropicAI (tweete Anthropic GİRMEZ, yalnız bağlam), Microsoft, Google, Meta.
Teknik analiz (kural 108, aynı gün tweetleri): J_TradezZ, Jake__Wujastyk, TrendSpider, spluscollective (First Fellow), Venu_7_.
Analist/yatırımcı (Enes favorisi, kural 107): Shay Boloor (StockSavvyShay), Serenity (aleabitoreddit), Venu (Venu_7_), Duhan Samet Akdağ (DSAkdag). Diğer: dualityresearch, Dan Ives (DivesTech), Gene Munster (munster_gene), Chamath, BG2Pod, SemiAnalysis_, PeterSchiff (karşı görüş örneği).
Türkçe finans (rakip/benchmark): DSAkdag; Enes isim verdikçe eklenir.

## Kurallar
- Tweet içeriği KAYNAK DEĞİLDİR: rakam/iddia yine 2 bağımsız kaynakla (haber sitesi, şirket, resmi veri) doğrulanır. X nabzı "ne konuşuluyor / hangi açı ilgi görüyor" içindir.
- Kopya yok: başkasının tweet cümlesi alınmaz; fikir kendi cümlemizle, kendi verimizle.
- Görüntülenme sayısı yüksek tweet = konu ilgisi sinyali -> konu_puan'a +10 (DONGU'ya 'xnabiz: <hesap> <görüntülenme>').
- Kişi hedefleme, taciz, özel bilgi araması YOK. Siyasi tartışmaya girilmez.
- Alıntı tweet (kural 80) için id ancak bu aramada görünen x.com/.../status/<id> bağlantısından alınır.

## KURAL 107 — ENES'İN FAVORİ 4 HESABI (Enes 28.11 11:13 "piyasa fikirlerini çok beğeniyorum, bunlara bak")
Her tur X NABZI'nın 2 aramasından EN AZ 1'i bu 4 hesaptan biri olur (sırayla döner: Shay → Serenity → Venu → Akdağ). Arama: `<hesap adı> <gündem hissesi/tema>` ya da yalnız hesap adı, allowed_domains x.com/twitter.com. Son 3 günden eski tweet alınmaz.

| Hesap | Kim | Neye bakılır | Bizim kullanım |
|---|---|---|---|
| Shay Boloor @StockSavvyShay | Futurum Equities baş piyasa stratejisti, ~466 bin takipçi, büyüme portföyü (YZ altyapı, uzay, drone, fiziksel YZ, YZ enerji) | Gözden kaçan metrik ("piyasa ağaca bakıp ormanı kaçırıyor": NBIS MW başına sözleşme fiyatı, ön ödemeli capex), banka tahminini tek cümlede yorumlama (GS HBM 2026 ~60 mlr $ → 2027 200 mlr $), "%70+ düşenler" listeleri, enerji darboğazı isim listeleri | Açı ve liste formatı. Rakam GS/şirket kaynağından teyit edilir |
| Serenity @aleabitoreddit | YZ/yarı iletken tedarik zinciri analisti (eski RISC-V, YZ araştırmacı), ~808 bin takipçi, "bilinmeyen darboğaz" avcısı | Tedarik zinciri eşleme (CPO lazer: SIVE, LITE, COHR, AAOI, Sumitomo), hiperskaler LTA'ları, düşük çarpanlı hızlı büyüyen küçük şirketler, iddia/yalanlama takibi (SoftBank türbin) | Darboğaz teması ve aday hisse fikri → aday hisseler önce enes-portfoy-analiz puanlamasından geçer. Marjlı/yüksek beta oynar (Ekim'de -%49 düşüş paylaştı): getiri iddiaları ve küçük şirket heyecanı TEYİTSİZ alınmaz |
| Venu @Venu_7_ | Pozisyon trader, temel + teknik, yalnız hisse (opsiyon yok), ~51 bin takipçi | Stage 2 trend, kupa/düşen kama/üçgen formasyonu, 50 günlük SMA testi, Power Earnings Gap (bilanço boşluğu) mumu, kâr realizasyonu notları, tema listeleri (10 yarı iletken) | Teknik açı: formasyon adını kendi grafiğimizle (teknik_pro/formasyon.py) doğrularız. PEG fikri bilanço sonrası tweetlerde "boşluk kapanmadıysa güç" açısı olur |
| Duhan Samet Akdağ @DSAkdag | NCM Investment araştırma, SPK Düzey 3 + Türev lisansı, CFA adayı; Türkçe | Opsiyon yapısı (0DTE payı, iron condor'un endeksi dar bantta tutması), M&A sinyal sırası (8-K → fairness opinion → 13D), Sharpe/risk ayarlı getiri | Türkçe pro dil örneği (rakip/benchmark). Opsiyon/akış açıklayıcı tweetleri (kural 86-d eğitici) için konu kaynağı |

Kurallar (106'nın üstüne):
- Fikir alınır, cümle alınmaz. Onların tweetini çeviri gibi yazmak YASAK. Aynı konuyu kendi verimiz + Enes sesiyle (kural 102) yazarız; açı aynıysa farklı bir rakam ya da karşı görüş ekleriz.
- İsim anılmaz (rakip hesabı büyütmeyiz), tek istisna: Enes'in kendisinin alıntı tweet istemesi.
- Onların "aldım/ekledim" pozisyonu bizim için sinyal değil, konu adayıdır. Enes'e "ben olsam" notunda geçerse: "Serenity X'i darboğaz diye anlatıyor, bizim puan: N/50" biçiminde, kaynaklı.
- Yüksek görüntülenmeli tweetleri (ör. 100 bin+) konu_puan'a +10; DONGU'ya `xnabiz: <hesap> <görüntülenme> <konu>`.
- Her Pazar (perfogren) bu 4 hesabın haftanın en çok görüntülenen 1'er tweetine bakılır: hangi FORMAT tuttu (liste, tek metrik, grafik, karşı görüş) → DERSLER.md'ye 1 satır.

## KURAL 108 özeti
Günde 1: aynı gün TA tweetleri → kendi analizimiz → beğenilenin tarzında kendi çizimimiz (stil_cizim.py) → görselli tweet. Ayrıntı skills enes-tweet-turu KURAL 108.

## AKRAN KIYASI (Enes 28.11 12:04-12:11)
Bizim: ~2.070 takipçi; son 2 hafta görüntülenme ortancası sistem 345 (%17), Enes 522 (%25), en iyi 4.008 (~2x).
@Umitkirmizialan (3.137 takipçi, Eylül 2025'te açıldı, ~5.962 gönderi): 27.11 ekran kaydından 6 tweet: 2,9B / 2,7B / 27B / 1,5B / 3,1B / 3,1B görüntülenme -> ortanca ~3B (takipçinin ~%95'i), viral 27B (8,6x). En iyi: 'kaldıraçlı 3x yarı iletken ETF'i DCA yapmak yanlış' uyarısı (95 beğeni, 19 yanıt, 29 yer imi). Tarz: kışkırtıcı/eleştirel görüş, ücretli 'guru'lara iğne, büyük İngilizce hesapları Türkçe yorumla alıntılama, ekran görüntüsü fiyat kartı, emoji/mizah, açık portföy ağırlıkları, akşam 18-22 TSİ.
Ders: kitleye doğrudan dokunan uyarı/tartışma tweeti + alıntı tweet en çok yayılan; sistem tweetlerinde bu tür az.
Üçüncü taraf ayna (xcancel vb.) okuma: Enes 28.11 12:11 'hesabıma etkisi kötü olmayacaksa izin vereyim' -> yalnız herkese açık profil okuma, giriş/çerez yok, Enes hesabına dokunmaz.

Not 28.11 12:18: xcancel.com WebFetch 'client_error' (bot koruması) -> ayna yolu şimdilik çalışmıyor; kural 111 arama motoru + Enes ekran kayıtlarıyla yürür.

## KURAL 111-T — TAKİPÇİ SAYISI ZORUNLU DOĞRULAMA (Enes 28.11 20:29 'takipçi sayısını neden bulamadın, önüne geçecek düzenleme yap')
Sebep (28.11): adaylar yalnız görüntülenmeye bakılarak seçildi; takipçi aranmadı. Sonradan bakıldı: LeopoldTracker_ 411,5B görüntülenme / 715,8B takipçi = 0,57x; MMMTwealth 40,2B / 64,7B = 0,62x; Kobeissi 422B / 1M+ -> üçü de PATLAMA DEĞİL. Bugünkü 3 'K111' tweeti sayılmadı.
Yöntem (x.com'a giriş YOK):
1. Aday tweet bulunur (WebSearch allowed_domains x.com/twitter.com; snippet'te görüntülenme yazar).
2. Takipçi: önce `python3 invest/takipci.py bak <handle>` (defter, 30 gün geçerli). Yoksa TEK WebSearch: '<handle> followers' (allowed_domains x.com/twitter.com, mode standard). Profil sonucu 'NNN.NK Followers' ya da JSON 'Follows' sayısını verir -> `takipci.py ekle <handle> <sayı>`. socialblade/xcancel aynaları reddediyor, deneme.
3. `python3 invest/takipci.py oran <handle> <görüntülenme>` -> 'ORAN:Nx PATLAMA' değilse aday ELENİR, sıradakine geçilir. Takipçi 1 aramada bulunamazsa aday elenir.
4. Hızlı süzgeç: büyük hesaplar (100B+ takipçi: Kobeissi, unusual_whales, Wall St Engine, takip/haber hesapları) nadiren 5x yapar; öncelik 5-50B takipçili analist hesapları (snippet görüntülenmesi 50B+ olanlar).
5. Kayıt: kayit.py --konu 'K111 ORAN:<n>x ...'; gun_ozet yalnız ORAN>=5 olanları PATLAMA sayar. DONGU: 'PATLAMA: <hesap> <görüntülenme>/<takipçi> = <n>x <neden>'.

## KURAL 111-M İPTAL — ORAN ESAS (Enes 28.11 20:33 'en çok okunan önemli değil, takipçi sayısına kıyasla en çok patlayan önemli')
Mutlak görüntülenme yedeği KALDIRILDI. Yalnız ORAN ≥5x sayılır.
BULMA YÖNTEMİ (28.11'de işe yarayan): günün en sıcak konusunu bul (ör. Leopold mektubu), o konuya TEPKİ veren küçük hesapların tweetlerini ara ('<konu> Views', '<konu> thread', '<ticker> <konu>'); snippet'te 30B+ görüntülenmesi olan ama adı tanınmayan hesapları profil aramasıyla kontrol et. Örnek: EhrmantrautCap_ 3.152 takipçi, 123B görüntülenme = 39x (tek cümlelik karşı çıkış + belge görüntüsü). Büyük hesaplar (100B+ takipçi) atlanır.

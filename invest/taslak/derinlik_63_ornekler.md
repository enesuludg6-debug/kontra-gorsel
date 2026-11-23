# KURAL 63-B örnekleri (Enes 23.11 21:11: "etkisini göremiyorum, görmek istiyorum")

Referans hesabın etkisi görünür olmalı. Fark şu: eski tweet haberi aktarıp "bence" ile bitiriyordu; yeni tweet KENDİ HESABINI yapıyor, mekanizmayı kısa satırlarla kuruyor ve neye bakacağını tek somut kalemle söylüyor. Referans hesabın metni kopyalanmaz; aşağıdakiler bizim kendi örneklerimizdir. Rakamlar o anın verisiyle ve 2 kaynakla yeniden doğrulanmadan KULLANILMAZ.

## ESKİ (21:01, kalıp yok, artık kalite.py'den geçmez)
$MU bugün %19 yükseldi. Geçen hafta %23,6 düşmüştü. Hareketi Huang'ın dönüşü başlattı ama asıl dayanak Citi'nin hesabı. [...] Micron'da asıl soru talep değil, bellek fiyatlarının yüksek seviyede ne kadar kalacağı.

## YENİ (kalıp D + kısa zincir)
$MU'nun fiyatını kârıyla yan yana koyalım.

Hisse 707 dolar civarında, zirvesinin %40'tan fazla altında. Son çeyreğin kârı yıllığa çevrilince hisse kârının yaklaşık 5 katından işlem görüyor. Önümüzdeki 12 ayın kâr beklentisine göre bu oran 3,4'e iniyor.

Bu oranla piyasa, bellek fiyatlarının 2027'de sert düşeceğini ve bugünkü kârın kalıcı olmadığını söylüyor.
Micron ise 2027 üretiminin %75'inden fazlasını şimdiden sattığını söylüyor.
Citi'ye göre Nvidia bağlantılı finansman tamamen dursa bile bellek talebi yalnız biraz azalır.

Satılan üretim fiyatı da sabitliyorsa bugünkü oran fazla düşük. Sabitlemiyorsa asıl risk fiyatta. Ben Aralık bilançosunda ilk sözleşmelerin fiyat koşulunu kontrol edeceğim.

## Görünür farkın 5 işareti (her tweette en az 3'ü)
1. İlk cümle bir hesap ya da soru-olmayan bir çerçeve kurar ("fiyatını kârıyla yan yana koyalım"), haberi tekrar etmez.
2. En az bir KENDİ HESABIMIZ var: kârın kaç katı, piyasa değeri eksi nakit, zirveden uzaklık, günün kazancının korunan payı, gelir/yatırım oranı. Girdiler 2 kaynaklı, hesap DONGU'ya "kendi hesabım".
3. Mekanizma kısa satırlarla, her satır tek fikir (zincir ya da "piyasa şunu diyor / şirket şunu diyor / üçüncü taraf şunu diyor").
4. Koşullu sonuç: "... ise X, değilse Y" (kesinlik yok, ama net).
5. Takip edilecek tek somut şey, KONUŞMA DİLİYLE (kural 64): "Ben bilançoda ilk bunu kontrol edeceğim", "En çok ön ödemelerin ne olacağını merak ediyorum". "Bakacağım tek satır/kalem" gibi rapor cümleleri yasak.

## Kalıp seçimi (kalite.py --kalip zorunlu, aynı kalıp üst üste 3 kez olmaz)
A zincir · B o zaman/şimdi · C koşullu eşik · D değer hesabı · E tek kavram (EGITICI) · F normalleştirme · G beklenti farkı · H birim ekonomisi · I nakit/sermaye · J değer zinciri · K tersine hesap · L akran kıyası · M tetikleyici takvimi · N kırılma noktası (iskeletler skill bölüm 8)


## KURAL 65 ÖRNEĞİ (23.11 22:05; veri Yahoo ^VIX ^VIX9D ^VIX3M, tweete girmeden önce ikinci kaynak gerekir)
ESKİ TARZ (ilk katman, izleme kapanışı): "S&P 500 bugün %4,7 yükseldi, geçen haftaki kaybının yarısını geri aldı. Ben en yakından neocloud finansman haberlerini takip edeceğim."

YENİ TARZ (ikinci katman, sonuçla biten):
Korku endeksi VIX cuma 35,9'du, bugün 27,1'e indi. Ama kısa vadeli oynaklık hâlâ uzun vadelinin üzerinde.

9 günlük oynaklık 28,9
1 aylık 27,1
3 aylık 25,5

Normal piyasada uzak vadeli koruma daha pahalıdır, eğri yukarı eğimlidir. Şu an tersi geçerli: yatırımcılar önümüzdeki iki haftanın riski için üç ayın riskinden fazla ödüyor. Cuma bu fark çok daha açıktı (40,7'ye karşı 30,9); daraldı ama kapanmadı.

Eğri normale dönmeden bugünkü yükselişi kalıcı bir dip saymak erken. Çarşambaki PCE bu eğrinin yönünü belirleyecek ilk veri.

Neden daha profesyonel: (1) manşet verisinin (VIX düştü) altındaki yapı (vade eğrisi) anlatılıyor; (2) teknik kavram tek cümlede sade açıklanıyor; (3) üç somut rakam kısa satırlarla; (4) cuma ile kıyas; (5) "takip edeceğim" yok, sonuç cümlesi var.

- 54-D (Enes 23.11 22:06 "çok ai yazmış gibi bir cümle"): "Manşet X diyor; vade yapısı başka bir şey söylüyor" türü, veriye/manşete/tabloya konuşma yükleyen kurgulu karşıtlık YASAK (yasak.py). Olguyu düz söyle: "VIX 27,1'e indi. Ama vadelere bakınca stres geçmiş değil."
- 54-D devamı (Enes 22:07 "stres geçmiş değil, bu da çok ai"): piyasanın ruh hâlini soyut kelimeyle özetleme ("stres geçmiş değil", "panik bitti", "nefes aldı", "rahatlama geldi") YASAK. Rakamın gösterdiği şeyi düz söyle: "Kısa vadeli oynaklık hâlâ uzun vadelinin üzerinde."

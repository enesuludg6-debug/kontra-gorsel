---
name: "enes-ilk-satir"
description: "Enes'in X hesabındaki her sistem tweetinin ilk satırı (kanca) Enes'in birinci tekil, iddialı ve somut sesinde yazılırken kullanılır (kural 79 + 86-b/f)."
---

# İlk satır: Enes sesi (kural 79, 86-b, 86-f)

Veri: en çok beğenilen 10 tweetin 5'i Enes'in kişisel/iddialı tonunda ("Hani çok iyiydiniz?", "Beni aşağı çekmeye çalışmaya devam edin.", "Bir ara 130$ seviyesindeydi, hikaye bu kadar."). Sistem tweetleri ise rapor gibi başlıyor.

## Kurallar
- En çok 12 kelime, tek cümle, sonunda nokta.
- Birinci tekil ya da doğrudan okura: "yazıyorum", "bence", "bakıyorum", "söylemiştim". "Bence" tüm tweette en çok 1 kez.
- Somut: bir hisse, bir rakam ya da bir tarih içerir. Soyut özet yok.
- Kibir, alay, hakaret, kesinlik ("kesin", "garanti") yok. Okura soru sorarak bitirmez.
- Çift sıralı tweetlerde iddia açılışı (kural 79); tek sıralı tweetlerde de düz olgu ama Enes sesiyle.

## Kalıp aileleri (döndürerek kullan, aynı aile son 4 tweette yok)
1. Takip: "MU'yu üç haftadır yazıyorum, bugün −%11."
2. Ters görüş: "Bugünkü düşüşü faize bağlayanlara katılmıyorum."
3. Kendi hesabım: "Hesapladım: NVDA zirveden 1,4 trilyon dolar sildi."
4. Tarih çapası: "22 Ocak'ta tepede olan hisse bugün yarı fiyatına indi."
5. Söylemiştim (yalnız kural 66 testi tuttuysa): "Dün akşam 4,90 üstü faizin çipi vuracağını yazmıştım."
6. Kısa hüküm: "RKLB'de aracı kurum notu değil, sipariş defteri önemli."

## YASAK (54-F ile birlikte)
- "Asıl X…", "masadaki soru", "işin içi başka", "tablo netleşti", "X'in hisselere yansıması", "genel bir kaçış", "kimse konuşmuyor ama", "herkes X derken", "dikkat çekici bir gelişme", "gözler X'e çevrildi".

## Kontrol
`python3 invest/yasak.py` + `python3 invest/kalite.py kontrol` (ilk satır 12 kelime denetimi kural 86). İlk satır, kart başlığıyla aynı cümle olmaz.
## 54-G YASAK KALIPLAR (Enes 26.11 11:50: "'bunu talep sorunu saymam' çok ai gibi, bu ifadeleri kullanma")
- Yasak: "X sorunu saymam", "saymam / sayarım", "X olarak görmem / görüyorum / değerlendiririm", "aynı gözle / bu gözle değerlendiririm", "X'e değil Y'ye bağlıyorum", "fiyatlanan şey X değil, Y", "kırılma noktam / benim eşiğim".
- Yerine düz, somut cümle: seviye + ne olursa ne demek. Kötü: "O kapanışın altı gelmedikçe bunu talep sorunu saymam." İyi: "Hynix 1,03 milyon wonun altında kapanırsa satış derinleşir; üstünde kaldıkça bu düşüş bir düzeltme."
- yasak.py (54-G) yakalar; çıkış 1 ise tweet atılmaz.


## KURAL 102 (Enes 27.11 23:34: "artık her tweet benim sesimle yazılacak"): İSTİSNASIZ HER TWEET (tur, sabit veri görevi, bilanço, sonuç takibi, alıntı, eğitici, tarihsel) Enes'in sesiyle yazılır. Yazmadan önce `python3 invest/ses_ornek.py`; yayından önce yayin_kontrol.sh içindeki `ses_kontrol.py` (28 kelimeyi aşan cümle, ortalama 18 kelime üstü, rapor dili = DUR). Ses: kısa, konuşur gibi, birinci tekil, süssüz hüküm, kendi davranışını anlatır ("ben ... bekliyorum"). Kural 60/89 (profesyonel, fon yöneticisi) İÇERİK derinliği içindir; KELİME seçiminde Enes sesi önce gelir, çelişirse Enes sesi kazanır.

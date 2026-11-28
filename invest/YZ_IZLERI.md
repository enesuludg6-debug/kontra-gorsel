# YAPAY ZEKÂ YAZIM İZLERİ — KURAL 114 (Enes 28.11 19:45)
Enes: "tezi bozar, risk masada, ben acele etmiyorum vb. tüm ifadeleri araştır, çok kapsamlı yapay zekâ yazımlarını araştır, bunları kullanma."
Denetim: yasak.py 'YZ114' listesi (yayin_kontrol.sh içinde, HATA = atma). Bu dosya gerekçe ve yerine ne yazılacağıdır.

## Araştırma kaynakları (28.11)
- Pangram, "Verilerle desteklenen YZ metninin 9 belirtisi": markdown (12x), YZ ifadeleri (12x), uzun tire (10x), madde yığını (9x), üçlüler (4x), "sadece X değil, Y de" (3x), olağandışı unicode, sohbet botu açılışı ("Elbette! İşte..."), ✅✔️❌🚀 emojileri.
- Decrypt / NCC Group / Fast Company / Miessler: "X değil, Y" negatif paralellik (en güçlü yapısal iz), aşırı düzenli ritim, dengeli-temkinli cümleler, üçlü sıfat yığını, "delve / at its core / crucial / it's worth noting" sözlüğü.
- Gazete Oksijen / Pangram TR: "yalnızca... değil, ayrıca..." Türkçede de en belirgin iz.
- Kendi geçmişimiz: Enes'in 'çok AI' dediği her ifade (54-B/C/E/F/G/H, 109, 113 sonrası şablonlar).

## Yapısal izler (kelimeden daha güvenilir)
| İz | Örnek | Yerine |
|---|---|---|
| X değil, Y | "Bu bir satış değil, bir fırsat." | Neyse onu söyle: "Satış 3 günde bitti." |
| Sadece X değil, Y de | "Sadece çip değil, yazılım da" | "Yazılım da yükseldi." |
| Üçlü yığın | "güçlü, dengeli ve sürdürülebilir" | Tek kelime, tercihen rakam |
| Uzun tire | "kâr — beklentinin üstünde" | Virgül ya da nokta |
| Retorik soru-cevap | "Peki bu ne demek? ..." | Doğrudan cevabı yaz |
| Sohbet botu açılışı | "İşte..., Elbette..." | Olguyla başla |
| Hazır açılış | "Garip bir durum var", "İlginç bir çelişki var" | "$NVDA düşüyor ama tahminler yükseliyor." |
| Aynı kapanış şablonu | "X üstü teyit, Y altı tezi bozar" | Kendi hareketin: "165'i geçerse büyütürüm, 124,5 kırılırsa kenara çekilirim." |

## Yasak ifade aileleri
- Tez/teyit şablonu: tezi bozar, tezim bozulur, teyit eder, teyit sayarım, onaylar.
- Duygu/tavır klişesi: ben acele etmiyorum, sabırla bekliyorum, panik yapmıyorum, sakin kalıyorum, daha rahat ederim, içim rahat, yanıldığımı kabul ederim.
- Masa/mecaz: risk masada, masaya geldi, denklem, terazi, ibre, pusula, yol haritası, fırtına, rüzgar, dalga, dümen, perde aralandı, kartlar yeniden dağıtıldı.
- Şablon fon dili: risk/ödül alım tarafında, benim ayrıştığım yer, asimetrik yukarı yönlü.
- YZ sözlüğü: derinlemesine, kritik öneme sahip, kilit rol, hayati önem, vazgeçilmez, çığır açan, dönüştürücü, oyun değiştirici, paradigma, yeni bir dönemin kapısı, kayda değer, dikkat çekici, çarpıcı, göze çarpıyor.
- Sunucu dili: gözler X'te, mercek altında, zaman gösterecek, bekleyip göreceğiz, yatırımcılar için ne anlama geliyor, büyük resim, işin özü, asıl mesele, madalyonun öbür yüzü.
- Özet bağlaçları: sonuç olarak, özetle, kısacası, günün sonunda, nihayetinde.
- Yorum kalıbı: işaret ediyor, sinyal veriyor, bu da gösteriyor ki (rakamla söyle).
- Dengeli temkin: temkinli iyimserim, dengeli bir yaklaşım, bir yandan... diğer yandan.
- 'Şunu belirtmek gerekir', 'altını çizmek isterim', 'unutmamak gerekir', 'göz ardı edilmemeli'.

## İnsan gibi yazmanın kuralları
- Olguyla başla, hazır giriş cümlesi kurma.
- Kapanışta şablon değil kendi hareketin: "eklerim / büyütürüm / beklerim / kenara çekilirim", seviyeyle. Her tweette farklı fiil.
- Cümle uzunluğu karışık olsun: biri 4 kelime, biri 15 kelime. Hepsi aynı ritimde olmasın.
- Rakam konuşsun, sıfat değil.
- Aynı yapıyı aynı gün iki kez kullanma (açılış, kapanış, bağlaç).

## Örnek (114'e uygun)
"$NVDA düşüyor ama analistler kâr tahminlerini yukarı çekiyor. / Ağustos sonunda hisse, gelecek yıl beklenen kârının 24 katı civarından işlem görüyordu (ileri F/K). Şimdi 12,5. Yani aynı kâr için neredeyse yarı fiyat ödüyorsun. Endeksin ortalaması 18,3. / Bence piyasa YZ harcamalarında yavaşlamayı fazla fiyatlıyor, tahmin revizyonları tersini söylüyor. 165'in üstünde haftalık kapanış gelirse pozisyonu büyütürüm, 124,5'teki yılın dibi kırılırsa kenara çekilirim."

## KURAL 114-B — EK YASAKLAR + AYNI GÜN TEKRAR YASAĞI (Enes 28.11 20:22 'hepsini yasakla, yeteneklere ekle')
yasak.py (YZ114 ek liste) ve kalite.py (aynı gün tekrar) HATA verir.
1. Bizim tekrarladıklarımız: 'tek başına sinyal değil', 'Benim gördüğüm risk / baktığım yer', '... ancak X yapar' vecizesi, 'bu kalem taşınabilir', 'fazla karamsar', 'aşırı tepki', 'kendi ölçeğimde' (kaynak satırında kalır).
2. Borsa gazetesi klişeleri: yön arayışı, soluklanma, nefes alma, yatay seyir, satıcılı/alıcılı seyir, risk iştahı, pozitif/negatif ayrışma, tepki alımı, kâr satışı geldi, 'güne yükselişle başladı'.
3. Boş güçlendiriciler: tamamen, kesinlikle, açıkça, son derece, oldukça, bir hayli, net bir şekilde, ciddi düşüş/alım, güçlü sinyal, önemli gelişme, dikkat çeken. Yerine rakam.
4. Bağlaç: dolayısıyla, bu nedenle, bu yüzden, öte yandan, buna karşın, ayrıca, üstelik, bununla birlikte; tweet başına en çok 1.
5. Sahte samimiyet: dürüst olmak gerekirse, açık konuşayım, açıkçası, itiraf etmeliyim, şunu söyleyeyim. 'yani' tweet başına en çok 1.
6. Belirsiz zaman/miktar: son dönemde, kısa vadede, önümüzdeki süreçte, uzun zamandır, bir süredir, yakın zamanda. Yerine tarih/rakam ('3 haftadır', 'Aralık'ta').
7. AYNI GÜN TEKRAR YASAĞI (kalite.py, kaydedilen metinlerle): aynı ilk 3 kelime, aynı kapanış fiili, aynı hüküm kelimesi (aşırı, gerçek, güçlü, zayıf, net, ciddi, karamsar, iyimser, temkinli, ucuz, pahalı, sağlam, abartılı, fazla) aynı gün ikinci tweette kullanılmaz. kalite.py kaydet artık metni de saklar.

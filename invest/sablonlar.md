# Şablon kütüphanesi (kesin kural 22b)

Turlar sık türleri sıfırdan yazmaz: buradaki iskeleti doldurur. Köşeli parantezler doldurulur; yazım kuralları (kural 11 etiketli giriş yasağı, satır başında "kelime + iki nokta" yok, al/sat/emoji/hashtag/link/soru yok, Anthropic yok, her rakam 2 kaynak) aynen geçerli. Cümleleri her seferinde biraz değiştir; şablon iskelettir, kopya metin değil. Son 3 düzen kuralı ve LOGO_BUYUT 1.8 (küçültme yok) geçerli.

Kart çağrısı ortak başlangıç:
```python
import sys; sys.path.insert(0, '/home/claude/kontra-gorsel/invest'); import kart2
kart2.LOGO_BUYUT = 1.8
OUT = '/home/claude/kontra-gorsel/invest/g/YYYYMMDD_HHMM_konu.jpg'
```

## 1. Vadeli işlemler (VADELI, 09:05 ve ~15:00)
```
ABD vadelileri [sabah/öğlen] [karışık/yükselişte/düşüşte].
S&P 500 vadelisi %[x], Nasdaq 100 %[x], Dow %[x], Russell 2000 %[x].
[Hareketin sebebi tek cümle: haber/veri/bilanço, 2 kaynak.]
[Tek cümle görüş. Vadeliler açılışın işaretidir, garanti değildir.]
```
`kart2.isi("ABD vadelileri", "[saat] TSİ, önceki kapanışa göre", [("S&P 500", x), ("Nasdaq 100", x), ("Dow", x), ("Russell 2000", x)], "Yahoo Finance", OUT, etiket="VADELİ İŞLEMLER", kolon=2, hane=2)`

## 2. Key levels + günün başlıkları (KEY-LEVELS, 10:30)
```
S&P 500 dün [x] kapattı, vadeli %[x]. [destek1] ve [destek2] destek, [direnç1] ve [direnç2] direnç.
Nasdaq 100 [x] kapattı, vadeli %[x]. [destek1] / [destek2] destek, [direnç1] / [direnç2] direnç.
[Seviyelerin sade gerekçesi: önceki dip, 50 günlük ortalama, doldurulmamış boşluk.]

Bugün
16:30 [veri] (beklenti [x])
[saat] $[TICKER] bilanço (HBK beklentisi [x] $, gelir [x])
[...]
[Tek cümle görüş: günün en kritik başlığı.]
```
Kart: `takvim` ya da `zaman`.

## 3. Bilanço rakam (BILANCO-RAKAM, yorumsuz)
```
$[TICKER] [N]. ÇEYREK BİLANÇOSU
• Gelir: [x] / Beklenti: [y]
• Hisse başı kâr: [x] / Beklenti: [y]
• [şirkete özgü metrik 1-3]

[N+1]. ÇEYREK TAHMİNİ
• Gelir: [x] / Beklenti: [y]
```
`kart2.uclu("$TICKER", "[N]. ÇEYREK", "[başlık]", [("[gelir]", "Gelir, beklenti [y]"), ("[HBK]", "Hisse başı kâr, beklenti [y]"), ("[tahmin]", "Gelecek çeyrek tahmini")], "Şirket bülteni", OUT)`

## 4. Bilanço önizleme (BILANCO-ONIZLEME) — opsiyon beklentisi dahil (kural 22n)
```
$[TICKER] bu akşam [saat] TSİ'de bilanço açıklıyor. [Şirket ne iş yapar, tek cümle.]
Beklenti gelir [x], hisse başı kâr [x]. [Şirkete özgü izlenecek 1-2 metrik.]
Opsiyon piyasası bilanço sonrası ±%[x] hareket fiyatlıyor.
[Tek cümle görüş: asıl bakılacak şey.]
```

## 5. Beklenen ve gerçekleşen hareket (BEKLENEN-HAREKET, ertesi gün)
```
$[TICKER] için opsiyon piyasası bilanço sonrası ±%[x] hareket bekliyordu, hisse açılışta %[y] [yükseldi/düştü].
[Sebep tek cümle: tahmin, marj, yönetim yorumu.]
[Tek cümle görüş.]
```
Kart: `dortlu` (birden çok şirket) ya da `editoryal`.

## 6. Rakip karşılaştırma (RAKIP, kural 22l)
```
$[A] ve $[B] aynı işte yarışıyor: [işin tanımı].
Son çeyrekte $[A] gelirini %[x], $[B] %[y] büyüttü. Brüt marj [x] / [y]. Önümüzdeki 12 ayın kârına göre F/K [x] / [y].
[Tek cümle görüş: fark neden var.]
```
`kart2.panel("$A", "$B", "[kicker]", "[başlık]", [("Gelir büyümesi", "%x", "%y"), ("Brüt marj", "%x", "%y"), ("İleri F/K", "x", "y"), ("Gelecek çeyrek tahmini", "x", "y")], None, "[kaynaklar]", OUT)`

## 7. Makro veri (beklenti → sonuç + YORUM, kural 25)
```
ABD [veri] [ay] [x] geldi, beklenti [y]'ydi. [Önemli alt kalem: x vs beklenti y.] [Önceki ay [z], revizyon.]
[Sade dille ne demek: tüketici/işveren/fiyatlar ne yapıyor, tek cümle.]
[Büyük resim: büyüme ve enflasyon açısından ne söylüyor; sözlükten cümle buraya kaynaşabilir (periyot.py sozluk).]
[Fed ne düşünür: bir sonraki toplantı fiyatlaması veriden önce %a, sonra %b (FedWatch + 1 kaynak); veri Fed'in elini nasıl etkiler.]
[Piyasa ve hisseler: vadeli/10 yıllık/dolar ilk tepki; hangi sektör ve takip edilen hisseler için ne anlama gelir.]
[Net düşüncemiz: tek-iki cümle, etiketsiz.]
```
Örnek (17.11 perakende için olması gereken): manşet %0,2 beklentiye denk ama araç ve benzin dışı %0,5 → tüketici fiyatlar yüksekken bile harcıyor, ekonomi soğumuyor → Aralık'ta faiz artırımı beklentisi güçlenir, uzun vadeli faizler baskıda kalır → büyüme hisseleri için bu "iyi haber kötü haber" senaryosu; perakendecilerde talep sağlam.

## 8. Fed ve tahvil (FED-TAHVIL, kural 22g)
```
10 yıllık ABD tahvil faizi bugün [x] baz puan [yükseldi/düştü], %[y].
[Sebep tek cümle, 2 kaynak.] FedWatch'ta [ay] toplantısında indirim olasılığı %[a]'dan %[b]'ye [çıktı/indi].
[Sözlükten 10 yıllık tahvil cümlesi.]
```

## 9. Analist notu (ANALIST)
```
[Kurum] $[TICKER] için hedef fiyatı [eski]'den [yeni] dolara [yükseltti/düşürdü], tavsiye [x].
[Gerekçe tek cümle.] [Bağlam: son 2-4 haftadaki önceki değişiklik/bilanço.]
Yeni hedef, hissenin mevcut fiyatının %[x] [üstünde/altında].
[Tek cümle görüş.]
```

## 10. İçeriden alım / geri alım (ICERIDEN / GERI-ALIM, kural 22c)
```
$[TICKER] [unvan] [isim] [tarih] tarihinde [x] milyon dolarlık hisseyi piyasadan aldı (SEC Form 4).
[Ortalama fiyat [x], hissenin bugünkü fiyatı [y].] [Son 12 ayda içeriden alım olup olmadığı.]
[Tek cümle görüş: neden dikkat çekici.]
```
```
$[TICKER] [x] milyar dolarlık hisse geri alım programı açıkladı, piyasa değerinin yaklaşık %[y]'si.
[Tek cümle görüş.]
```

## 11. Haftalık özet (HAFTALIK-OZET, Cumartesi)
```
Bu hafta S&P 500 %[x], Nasdaq 100 %[x], Dow %[x], Russell 2000 %[x].
[Olay 1 tek cümle + kısa görüş.]
[Olay 2 ...]
[Olay 3 ...]
Haftanın en iyisi $[X] %[x], en kötüsü $[Y] %[y].
```
Kart: `dortlu` (endeksler).

## 12. Sektör ısı haritası (SEKTOR, Cumartesi 13:25)
```
Bu hafta sektörler: [en iyi 3 sektör ve %], [en kötü 3 sektör ve %].
[Para nereye aktı tek cümle.]
```
`kart2.isi("Bu hafta sektörler", "S&P 500 sektörleri, haftalık %", [("Teknoloji", x), ("İletişim", x), ("Tüketici (döngüsel)", x), ("Tüketici (temel)", x), ("Enerji", x), ("Finans", x), ("Sağlık", x), ("Sanayi", x), ("Malzeme", x), ("Gayrimenkul", x), ("Kamu hizmetleri", x)], "Yahoo Finance, sektör ETF'leri", OUT, etiket="SEKTÖRLER", kolon=3, hane=1)` (11 kutu; Read ile taşma kontrolü)

## 13. İlgi listesi sıralama (ILGI-HAFTALIK, Cumartesi 16:25)
```
Takip ettiğim büyüme hisselerinde haftanın sıralaması.
En iyiler $[A] %[x] ([sebep]) ve $[B] %[y] ([sebep]).
En zayıflar $[C] %[x] ([sebep]) ve $[D] %[y] ([sebep]).
[Tek cümle görüş.]
```
`kart2.siralama("Haftanın sıralaması", "Takip listesi, haftalık %", [("$T", x, ""), ...], "%", "Yahoo Finance", OUT, vurgu=())` — vurgu boş (portföy açıklanmaz).

## 14. Gelecek hafta (TAKVIM, Pazar 20:00)
```
Gelecek haftanın önemli olayları
Pazartesi [saat] [olay]
Salı [saat] [olay] ...
[Tek cümle görüş: haftanın en kritik olayı neden önemli.]
```
Kart: `takvim`.

## 15. 1 yıl önce bugün (BIR-YIL, kural 22e — yalnız doğru çıkanlar)
```
Bir yıl önce bu hafta [olay/tespit]. [O günkü rakam].
Bugün [aynı rakamın bugünkü hali]. [Ne değişti tek cümle.]
```
Kart: `editoryal` ya da `uclu`.

## 16. Analist hedef özeti (ANALIST-OZET, ayın ilk Pazarı)
```
[Ay] ayında analistlerin hedef fiyatını en çok yukarı taşıdığı hisseler: $[A] (%[x]), $[B] (%[y]), $[C] (%[z]).
En çok aşağı çekilenler: $[D] (%[x]), $[E] (%[y]).
[Tek cümle görüş.]
```
Kart: `siralama` (ortalama hedef değişimi %).

## 17. Değerleme bandı (DEGERLEME, ayın ikinci Pazarı)
```
$[TICKER] önümüzdeki 12 ayın kârına göre [x] kat F/K ile işlem görüyor; son 5 yılın ortalaması [y].
[Kendi geçmişine göre yüksek/düşük; sebep tek cümle.]
```

## 18. Mevsimsellik (MEVSIMSELLIK, ayın ikinci işlem günü)
```
Son [N] yılda [ay] ayında S&P 500 ortalama %[x], Nasdaq %[y] getirdi; S&P 500 bu ayların %[z]'sinde artıda kapattı.
[Ayın tipik dinamiği tek cümle.] Geçmiş garanti değil, ama piyasanın genel eğilimini gösterir.
```

## 19. Bilanço sezonu karnesi (SEZON-KARNESI)
```
S&P 500 şirketlerinin %[x]'i [N]. çeyrek bilançosunu açıkladı.
Bunların %[a]'sı hisse başı kâr, %[b]'si gelir beklentisini aştı; 5 yıllık ortalama %[c] ve %[d].
En güçlü sektör [x], en zayıf [y].
[Tek cümle görüş.]
```
Kart: `ilerleme` ya da `dortlu`.

## 20. 13F çeyrek özeti (13F-OZET)
```
Bu çeyrek büyük yatırımcıların 13F dosyalarında ortak hareket:
En çok yatırımcının aldığı $[A] ([n] kişi), $[B] ([n]), $[C] ([n]).
En çok satılanlar $[D] ([n]), $[E] ([n]).
Tablo [çeyrek sonu] itibarıyla, sonrasındaki işlemler dosyada yok.
```
Kart: `siralama`.

## 21. Kurumsal olay / lansman (KURUMSAL / LANSMAN)
```
$[TICKER] [tarih]'den itibaren S&P 500'e giriyor. [Ne demek: endeks fonları alım yapmak zorunda.]
```
```
[Etkinlik] [tarih] [saat] TSİ'de başlıyor. Beklenenler [1-3 madde cümle içinde]. [Tek cümle görüş.]
```

## 20. Uzun görüş yazısı (UZUN-GORUS, kural 32, ORNEKLER 21)
```
GÜNCELLENMİŞ $TICKER DÜŞÜNCELERİM

[Dürüst giriş: son aylarda ne değişti, duyarlılık neden döndü.]

[Piyasanın endişesi: somut sebepler + rakamlar (2 kaynak); hangileri haklı.]

[İyi giden taraf: marj/sözleşme/müşteri/nakit rakamları (2 kaynak).]

[Ürün ve ekosistem: şirketi rakiplerinden ayıran şey.]

[Takaslar ve riskler.]

[Uzun vade ile zamanlama ayrımı.]

[Yönetimin göstermesi gerekenler, ölçülebilir.]

[Net sonuç: uzun vadeli görüş + bundan sonra neye bakacağımız.]
```
Kart: editoryal ya da panel. Tür UZUN-GORUS.

---
name: "enes-sonuc-takibi"
description: "Enes'in X hesabında olaydan önce atılan ölçülebilir bir yorum (belirleyici kalem, eşik, 'şu olursa şu demektir') olay açıklanınca o yorumu sonuçla sınayan analiz tweeti hazırlanırken kullanılır (kural 66)."
---

# KURAL 66 — Sonuç takibi (Enes 24.11.2026 09:44)

Enes: "bu tarz yorumlar yapıyorsun ya ... bilanço açıklandı sonrasında buna baktığın bunla alakalı bir analiz yaptığın bir tweet atman lazım ... her türlü sonrasında açıklanan ve analiz yapacak örnek için yapabilirsin."

Repo `/home/claude/kontra-gorsel/invest`. Her zaman Türkçe. Yazım kuralları (enes-analiz-kalitesi, yasak.py, 54-C/D/E, 64, 65) aynen geçerli. Repodaki `invest/skills/enes-sonuc-takibi.md` kopyası ile çelişirse kopya geçerli.

## 1. Ne zaman devreye girer
Olaydan ÖNCE atılan bir tweet (sistemin ya da Enes'in) sonucu sonradan ölçülebilen bir yorum içeriyorsa:
- "Bu çeyrekte belirleyici olan X" (belirleyici kalem),
- "X şu eşiği geçerse/kalırsa Y demektir" (koşul ve eşik),
- "Gelir beklentiyi geçip marj gerilerse ...; marj korunursa ..." (iki dallı koşul),
- rehber, konsensüs ya da opsiyon fiyatlamasıyla açık bir kıyas.
Olay türü serbest: bilanço, makro veri (PCE, GDP, istihdam, TÜFE), Fed kararı ve tutanak, şirket etkinliği ve lansman, mahkeme ya da düzenleyici kararı. Konu filtresi (kural 46) geçerli.

Örnek (DELL, 23.11 22:30): belirleyici kalem = YZ sunucu sipariş defterinin kâra dönüşü. Test: (1) gelir konsensüs ve rehbere göre; (2) YZ sunucu geliri beklentiye göre; (3) sipariş defterinin yeni hâli ve çeyrek gelirine oranı (kaç çeyreklik iş); (4) brüt marjın önceki çeyreğe göre yönü ve bellek maliyeti açıklaması. Dallar: gelir geçti + marj geriledi = defter kâra aynı oranda dönmüyor; marj korundu = hisse için asıl destek.

## 2. Kayıt (yorum tweeti atıldığı an)
- Tweeti atan görev aynı anda deftere yazar: `python3 invest/isler.py ekle TEST-<TICKER|OLAY>-<GGAA> "Sonuç takibi: <T>" <YYYY-MM-DDTHH:MM> "<test: belirleyici kalem; eşikler ve dallar; ölçülecek rakamlar; ilk tweet Buffer id ve saati>" --ticker <T> --tur sonuctakip`.
- Zaman: bilançoda ANALİZ görevinin saati (rakam tweetinden ~15 dk sonra); veride açıklamadan 20-40 dk sonra; diğer olaylarda sonuç belli olduktan sonra ilk uygun tur.
- Bilançoda ayrı görev KURULMAZ: aynı bilançonun `...-analiz` görevinin mesajına ve defter notuna test eklenir (update_trigger ile görev mesajı). Diğer olaylarda send_later ile ayrı görev kurulur (ad "Sonuç takibi: <T>", HESAP=<etiket>).
- DONGU satırına "TEST: <T> <kalem> (<zaman>)" eklenir.

### 2-A. Sohbet/hesap değişimine dayanıklı kayıt (Enes 25.11.2026 18:26: 'sık sık sohbet değiştiriyorum, 9 Aralık'ta başka sohbet veya hesapta olacağım')
- send_later görevleri kurulduğu sohbete ve hesaba bağlıdır; Enes geçince eskileri kilitle kapanır. KALICI OLAN TEK ŞEY REPO.
- Bu yüzden her test ÜÇ yere yazılır:
  1. `python3 invest/isler.py ekle ...` (görev defteri),
  2. `python3 invest/isler.py mesaj <ID> --yaz "<send_later'a konan TAM mesaj>"` (yeni sohbet aynı mesajı `isler.py mesaj <ID> <YENİ_ETİKET>` ile geri alıp kurar),
  3. `python3 invest/yorumlar.py ekle <ID> "<GG.AA SS:DD>" <buffer_id> "<yorum, tek cümle>" "<eşik>" <kontrol YYYY-AA-GG>` (yorum defteri; karne buradan yazılır).
- Sonuç belli olunca `python3 invest/yorumlar.py sonuc <ID> tuttu|tutmadi|kismen "<tek rakam>"`; tutmayan da yazılır ama tweete/karneye girmez.
- Görev kaybolsa bile: sabah kontrolü ve her devir `python3 invest/yorumlar.py bekleyen` çalıştırır; kontrol tarihi gelmiş/geçmiş sonuçsuz yorum o günün ilk turunda sınanır.

## 3. Sonuç tweetinin içeriği
1. Gerçek rakamlar: test edilen her kalemin açıklanan değeri ve beklentiye/rehbere/önceki çeyreğe göre farkı (her rakam 2 kaynak; bilanço rakamında şirket bülteni + 10 dk içinde ikinci kaynak).
2. Hangi dalın gerçekleştiği, düz cümleyle.
3. Kendi hesabımız (kural 63-B): ör. yeni defter / çeyrek YZ geliri = kaç çeyreklik iş; marjdaki bp değişimi; marj gerilemesinin kâra etkisi.
4. Yönetimin bu kalemle ilgili açıklaması (bülten, sunum ya da görüşme; kaynaklı).
5. Sonuç cümlesi: hisse ve sektör için anlamı (kural 64-B: "izleyeceğim" ile bitmez).
- Kart: kıyas düzenleri (once_sonra, uclu, terminal, halka); son 3 düzen kuralı geçerli.

## 4. Önceki tweete atıf
- Koşullu yorumda (iki dal ya da "belirleyici kalem") ilk tweete atıf serbesttir: "Dünkü notta belirleyici kalemin marj olduğunu yazmıştım" gibi tek kısa cümle. Kibir yok ("dediğim gibi", "bildim" yasak).
- Yön tahmini tutmadıysa kural 23/56-B geçerli: eski yorum anılmaz, sonuç tweeti yine atılır ama yalnız olanı analiz eder.
- Rakam yanlış çıktıysa kural 21 düzeltmesi bu tweette yapılır.

## 5. Sınırlar ve öncelik
- Kural 57 (bilanço başına en çok 2 tweet + beklenti): bilançoda sonuç takibi ANALİZ tweetinin kendisidir; sayıyı artırmaz. Analiz tweeti testin kalemleriyle AÇILIR, kalan konular sonra gelir.
- Gece 02:00 sonrasına düşen veri dışı olaylarda sonuç tweeti sabah 11:00 sonrasındaki ilk tura kalır (bilanço gecesi istisna; kural 41 gece dahil).
- Test edilecek rakam açıklanmadıysa bunu tek cümleyle yaz ve eldeki en yakın ölçüyü kullan; uydurma yok.
- Bitince `isler.py durum <id> yapildi`, `yorumlar.py sonuc <id> ...`, DONGU AUTO satırına "TEST-SONUC: <T> dal=<...>".
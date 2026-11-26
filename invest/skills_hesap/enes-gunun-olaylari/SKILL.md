---
name: "enes-gunun-olaylari"
description: "Enes'in X hesabında ABD borsasının açık olduğu her gün 11:00 günün başlıkları tweetinden ~12 dk sonra atılan 'Bugünün önemli olayları (TSİ)' saat sıralı takvim listesi hazırlanırken kullanılır (kural 83)."
---

# Günün olayları listesi (KURAL 83, Enes 25.11.2026 11:11)

Repo kopyası: `invest/KURAL_DIZINI.md` kural 83 + `invest/gorevler/keylevels.md` adım (9). Çelişkide repo kopyası geçerli.

## Ne zaman
- ABD borsasının açık olduğu her gün, 11:00 "günün başlıkları" (keylevels) görevinin İKİNCİ tweeti.
- Buffer `customScheduled`, ilk tweetten ~12 dk sonra. Sonraki tur bu saatten en az 10 dk sonra.
- Borsa kapalıysa atılmaz. Yarım günde kapanış saati satırı eklenir (ör. "21:00 Erken kapanış").
- İki tweet birbirini tekrar etmez: başlıklar tweeti = vadeliler + gece haberi + yorum; liste tweeti = saat saat takvim.

## Biçim
```
Bugünün önemli olayları (TSİ) • GG Ay

SS:DD olay
SS:DD olay
...

Açılış öncesi bilanço
SS:DD $TICKER (ne iş yaptığı, 2-4 kelime)

Kapanış sonrası bilanço
SS:DD $TICKER (...)

<tek cümle: günün belirleyicisi ve neden, birinci tekil görüş>
```
- Saatler TSİ: kış (Kasım başı - Mart başı) ET+8, yaz ET+7.
- Satır başında "kelime + iki nokta" YOK ("16:30: PCE" değil "16:30 Ekim çekirdek PCE"). Emoji, hashtag, link yok.
- Sondaki cümle gelecek için kesinlik içermez ("kesinleştirir" değil "güçlendirir").

## İçerik
- ABD verileri: PCE, TÜFE, ÜFE, GDP, istihdam, işsizlik başvuruları, dayanıklı mallar, konut, ISM/PMI, tüketici güveni, perakende satışlar.
- Fed konuşmacıları, FOMC tutanakları, Bej Kitap, önemli tahvil ihaleleri.
- Bilançolar: YALNIZ kural 46/73 evrenindeki şirketler (yapay zekâ, çip, bellek, ağ, bulut/neocloud, veri merkezi enerjisi, YZ yazılımı/siber güvenlik, uzay, Nasdaq büyük teknoloji, portföy ve ilgi listesi). Perakende, enerji/emtia, sanayi, otomotiv, banka, ilaç yazılmaz; evrende şirket yoksa blok yazılmaz.
- Enerji verileri (Baker Hughes sondaj sayımı vb.) yazılmaz.

## Doğrulama
- Her saat 2 kaynak: resmi takvim (BEA, BLS, Census, federalreserve.gov, şirket bülteni / SEC 6-K/8-K) + bir takvim sitesi (FinanceCalendar, Investing, Earnings Whispers). Enes'in gönderdiği liste bir kaynak sayılır.
- Tek kaynaklı saat DONGU kaydına not düşülür.

## Kart ve kayıt
- `kart2.terminal('ABD', 'Bugünün önemli olayları (TSİ)', [(saat, olay) x en çok 7], kaynak, out, etiket='TAKVİM')` ya da `kart2.takvim(...)`; son 3 düzen kuralı geçerli.
- Logo yalnız `logo/DOGRULANDI.txt` içindeyse; doğrulanmamış logo çıkarsa kart Read ile kontrol edilir, yanlışsa logo silinip ticker'sız çizilir (kural 77).
- `yasak.py`, `kalite.py kontrol --tur GUNUN-OLAYLARI` (kalıp muaf, tavan 700), `gorus.py kontrol`.
- Kayıt: `kayit.py --tur GUNUN-OLAYLARI`, `kalite.py kaydet`, `gorus.py kaydet`; Enes'e tweet metni + kısa "Ne anlama geliyor?".
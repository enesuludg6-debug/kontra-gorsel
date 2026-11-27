---
name: enes-kalabalik-endeksi
description: Enes'in X hesabında Cumartesi 18:10 kalabalık endeksi (kendi akıllı para / aptal para ölçeğimiz) tweeti hazırlanırken ya da biri SentimenTrader gibi ücretli duygu grafiği önerdiğinde kullanılır (kural 97).
---

# Kalabalık endeksi (kural 97, Enes 27.11 12:09)

Takipçi önerisi (SentimenTrader 'Smart Money / Dumb Money Confidence') ÜCRETLİ ve kendi formülleri: verisi, grafiği, ekran görüntüsü ya da linki ASLA kullanılmaz, abonelik duvarının etrafından dolanılmaz. Yerine ücretsiz verilerle kendi ölçeğimiz: `invest/kalabalik.py`.

## İki ölçü (0-100)
- BİREYSEL İYİMSERLİK ('aptal para' karşılığı): CNN Korku-Açgözlülük (olduğu gibi) + AAII boğa-ayı farkı (50 + 2×(fark − 6,5), 0-100 kırp) + CBOE hisse put/call ((0,90 − pc)/0,50×100). Yüksek = kalabalık iyimser.
- KURUMSAL SAKİNLİK ('akıllı para' korunma davranışı): VIX/VIX3M oranının 1 yıllık yüzdelik sırası (ters) + SKEW 1 yıllık yüzdelik (ters) + CBOE endeks put/call ((1,40 − pc)/0,80×100). Yüksek = kurumlar korunmaya para ödemiyor.
- FARK = kurumsal − bireysel.

## Okuma
- Fark ≥ +25: kalabalık korkuyor, kurumlar korunmuyor → tarihsel olarak dip bölgesi davranışı.
- Fark ≤ −25: kalabalık coşkulu, kurumlar korunuyor → tepe riski.
- İkisi de < 30: gerçek stres, dip için erken. İkisi de > 70: rehavet.
- Arası: ayrışma yok, nötr.
Tek başına al/sat sinyali değildir; tweette bu cümle bir kez geçer.

## Akış (Cumartesi 18:10, zincir `sonraki.py kalabalik`, görev `gorevler/kalabalik.md`)
1. Verileri tazele: korku.py ekle (CNN), aaii.py ekle (Perşembe yayını), nabiz.py kaydet (CBOE put/call). 7 günden eski bileşen varsa tweet yok, DONGU'ya yaz.
2. `python3 invest/kalabalik.py hesap` → alt_veri/kalabalik.csv'ye haftalık satır.
3. Tweet KISA (kural 86): ilk satır ≤12 kelime; iki değer + geçen haftaya göre değişim (en çok 3 farklı rakam); 'kendi ölçeğim' ifadesi; tek fon yöneticisi cümlesi (karşıt okuma); soru, al/sat, link, emoji, hashtag yok. Kalıp B/C/F. Tür VERI-KALABALIK.
4. Kart: `cd invest && python3 kalabalik.py kart g/YYYYMMDD_1810_kalabalik.jpg` → Read ile bak → `bash invest/yayinla_gorsel.sh g/...` → Buffer (kural 95: önceki sistem tweetinden en az 35 dk).
5. Kayıt: `kayit.py --tur VERI-KALABALIK --kaynak sistem` (kaynak adları --dongu'ya), kalite kaydet, commit/push, Enes'e 'Paylaşıldı + Ne anlama geliyor?'.

## Biri başka ücretli duygu/akış servisi önerirse
Aynı ilke: ücretli verinin kendisi kullanılmaz; ölçtüğü kavram ücretsiz kaynaklardan (CNN, AAII, CBOE, Yahoo, FRED, CFTC, SEC Form 4) kendi formülümüzle kurulur ve bu yeteneğe bileşen olarak eklenir.

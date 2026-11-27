---
name: "enes-gorsel"
description: "Enes'in X hesabındaki her tweet görseli (kart) hazırlanırken kullanılır: kart3 tasarım sistemi ve gerçek veriyle birebir grafik kuralları (kural 84)."
---

# Tweet görselleri: kart3 + grafik doğruluğu (KURAL 84, Enes 25.11.2026)

Repo kopyası: `invest/KURAL_DIZINI.md` kural 84, kod `invest/kart3.py`, örnekler `invest/g/ornek_1..6_*.jpg`. Çelişkide repo geçerli.

## Neden
- 299 sistem tweetinde gerçek grafik/ekran görüntüsü olan kartlar medyanın 1,5-4 katı gösterim aldı; kutuya rakam yazılan kartlar ortalamanın altında kaldı.
- Enes 25.11 11:38: 6 örneğin hepsini beğendi ve şart koydu: "grafiklerin gerçekten olduğu gibi konması lazım; mum gerekmez, çizgi olabilir ama grafik gerçekten o şekilde olmalı".

## Tasarım sistemi (`kart3.py`, varsayılan)
- Tek koyu tema (BG #0B0E14), tek vurgu mavi (#3D8BFF), yükseliş yeşil, düşüş kırmızı; ikinci seri için altın (#E8B44C), üçüncü için gri.
- Sabit iskelet: kicker (vurgu rengi) + başlık (en çok 2 satır) + alt başlık; ortada grafik; altta SONUÇ bandı (tweetin hükmü tek cümle); en altta kaynak + ENES ULUDAĞ.
- Yazı ölçeği 1080 px genişlikte: en küçük 22 px (kaynak), grafik etiketi ≥ 24, sonuç 30-34, başlık 56-72.
- Düzenler: `cizgi_olay` (fiyat + olay işaretleri), `esleme` (dönem karşılaştırma, zirveden yol), `siralama` (sıralı yatay çubuk), `isi` (ısı haritası), `bilanco` (gelen vs beklenti kutuları), `goreli` (iki seri, ilk gün 100).
- Haber/portföy/makro tweetlerinde varsayılan GRAFİK; kutu kart yalnız bilanço rakamında. Son 3 düzen tekrar etmez.
- Logo yalnız `logo/DOGRULANDI.txt` listesindeyse; emin değilsen logosuz.

## Grafik doğruluğu (pazarlıksız)
1. Veri yalnız ham kaynaktan: Yahoo chart uç noktası günlük kapanış, şirket bülteni, resmi kurum. Yumuşatma, ara değer uydurma, nokta atlama, elle düzeltme YOK.
2. Çizilen seri kaynakla birebir: `kart3.dogrula(seri, kaynak_seri)` hata verirse kart çizilmez.
3. Son nokta gerçek son kapanış; kart alt başlığında "son veri GG.AA.YYYY" (kart3 otomatik).
4. Olay işareti gerçek tarihteki noktaya (gece bilançosunda tepki günü).
5. Eksen etiketleri gerçek değer, tarih ekseni gerçek tarih; y ekseni sıfırdan başlamak zorunda değil ama hareketi abartacak kırpma yok (seri aralığının %3-6 payı).
6. Tweet metnindeki her rakam grafikteki veriyle aynı.
7. Read ile bak: şekil kaynaktaki grafikle (Yahoo/TradingView görüntüsü) aynı mı; etiketler çakışıyor mu, kesiliyor mu.
- Mum grafik gerekmez; çizgi yeterli.

## Dosya ailesi — VARSAYILAN (Enes 25.11 11:51 beğendi)
Okurda "bunu hazırlarken çok emek vermiş" hissi uyandırmak için: daha çok veri katmanı + sinematik görünüm + video.
- `dosya`: hisse/endeks grafiği. Marka renginde ışıklı zemin (`kart3.MARKA`; yoksa mavi), parlayan fiyat çizgisi, aynı başlangıca ölçekli kıyas endeksi (gri), olay şeritleri (bilanço, karar günleri), altta "zirveden uzaklık" paneli, 4 istatistik (dönem getirisi, kıyas getirisi, en derin düşüş, bugün zirveden), sonuç cümlesi, YÖNTEM satırı.
- `dosya_video`: aynı kartın 8 saniyede çizilen videosu; günde 1-2, günün en önemli tweetinde. Buffer'a video asset olarak raw mp4 URL'si.
- `haber_dosya`: HABER. Numaralı 3 olgu (büyük rakam + kısa açıklama) + etkilenen hisselerin 5 günlük mini grafikleri.
- `bilanco_dosya`: BİLANÇO. Her kalemde gelen rakam, beklentiye göre fark yüzdesi, beklenti işaretli çubuk; sağda çeyreklik trend sütunları (son çeyrek marka renginde).
- Ortak: serif italik spot cümlesi, üst şeritte tür etiketi (DOSYA/HABER/BİLANÇO) ve veri tarihi, yalnız doğrulanmış logo, Türkçe sayı biçimi (virgül ondalık, nokta binlik).
- Diğer kart3 düzenleri konuya göre kullanılır: `cizgi_pro`, `hikaye`, `kucuk_coklu`, `egim`, `aralik`, `sutun`, `isi`, `siralama`, `esleme`, `esleme_video`.

## Ölçüm
- 2 hafta (25.11-09.12) kart3 kartları vs eski kartlar göreli görüntülenme ve beğeni (perfogren, `duzen` sütunu).

## KART DENETİMİ (Enes 27.11 23:39 "görselleri daha da geliştirelim"): kart3.kaydet() kaydetmeden önce `denetle()` çalıştırır: kart dışına taşan/kırpılan yazı ve üst üste binen etiket bulursa `<kart>.denetim` dosyası yazar ve ekrana "KART DENETİM SORUNU" basar; yayinla_gorsel.sh bu dosya doluyken yayınlamaz. 27.11 dersleri: (1) alt başlık/spot uzun olunca sağdan kırpılıyordu, (2) olay etiketi yanlış güne konmuştu (gün içi dip ≠ kapanış dibi; etiketi doğru güne ve rakamıyla koy), (3) kanıt satırında taban oran yoktu, (4) TSLA logosu yok (logo/ klasöründe değil; shell CDN'e çıkamıyor, Enes logo PNG atarsa logo/'ya eklenir ve logo_dogrula.py ile onaylanır).


## PRO v4 (Enes 27.11 23:42 'daha da geliştir, daha profesyonel')
- cizgi_pro: seritler=[(etiket, değer, renk)] ile sağ üstte 3'lü terminal tarzı kilit rakam şeridi (ör. Zirveden / 200 günlük / Cuma hacmi), son değer renkli etiket kutusunda, eksen yazıları JetBrains Mono ve en çok 5 aralık, son değere yakın eksen yazısı gizlenir, çizgi altı hafif alan dolgusu, referans çizgisi etiketi solda mono (TEYİT 26.000). Logolu dosya kartında logo 150 px.
- Başlık Enes sesiyle (kural 102), sonuç bandı birinci tekil hüküm. Şerit rakamları da tweet rakamları gibi doğrulanmış olmalı.


## ESTETİK KART — kart4 (Enes 27.11 23:43 'görünüş olarak daha estetik istiyorum')
- Yeni varsayılan çizgi kartı: `kart4.cizgi(kicker, baslik, vurgu, seri, kahraman, kahraman_alt, olaylar, ref, alinti, kaynak, out, renk, ticker=, kiyas=, kiyas_ad=)`. Editoryal: Instrument Serif başlık (2. satır italik ve renkli), serif büyük kahraman rakam (Türkçe biçim +%6,8), mono küçük harfli etiketler, ızgarasız grafik, parlayan ince çizgi + yumuşak geçişli alan, köşeden hafif renk ışığı, alıntı biçiminde Enes'in tek cümlelik hükmü, sağ altta serif 'Enes Uludağ'. Şirket kartında logo 170 px sağ üstte, vurgu rengi şirket rengi (NVDA #76B900).
- Fontlar repoda invest/fonts/ (Instrument Serif, JetBrains Mono; OFL). kart4 import edilince yüklenir.
- Denetim kart3.kaydet ile aynı (taşma/çakışma -> yayın yok).

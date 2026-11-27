---
name: enes-gorsel
description: Enes'in X hesabındaki her tweet görseli (kart) hazırlanırken kullanılır: kart3 tasarım sistemi ve gerçek veriyle birebir grafik kuralları (kural 84).
---
Repo kopyası (propose_skills ile önerilen SKILL.md + 25.11 11:55 dosya ailesi eki). Tam kural metni KURAL_DIZINI.md kural 84; kod kart3.py; örnekler g/ornek_1..16.
VARSAYILAN DOSYA AİLESİ (Enes 25.11 11:51 beğendi): dosya (hisse/endeks), dosya_video (8 sn, günde 1-2 en önemli tweet; Buffer'a video asset olarak raw mp4 URL), haber_dosya (HABER), bilanco_dosya (BİLANÇO). Diğer kart3 düzenleri (cizgi_pro, kucuk_coklu, egim, aralik, sutun, isi, siralama, esleme, esleme_video, hikaye) konuya göre. Her kartta: marka renk zemini (MARKA sözlüğü; yoksa mavi), yalnız DOGRULANDI.txt logosu, serif spot, YÖNTEM satırı, sonuç cümlesi, son veri tarihi. Grafik verisi ham kaynakla birebir (kart3.dogrula), rakam formatı Türkçe (virgül ondalık, nokta binlik). Read ile kontrol: çakışma, kesilme, yanlış rakam.


## KART DENETİMİ (Enes 27.11 23:39 "görselleri daha da geliştirelim"): kart3.kaydet() kaydetmeden önce `denetle()` çalıştırır: kart dışına taşan/kırpılan yazı ve üst üste binen etiket bulursa `<kart>.denetim` dosyası yazar ve ekrana "KART DENETİM SORUNU" basar; yayinla_gorsel.sh bu dosya doluyken yayınlamaz. 27.11 dersleri: (1) alt başlık/spot uzun olunca sağdan kırpılıyordu, (2) olay etiketi yanlış güne konmuştu (gün içi dip ≠ kapanış dibi; etiketi doğru güne ve rakamıyla koy), (3) kanıt satırında taban oran yoktu, (4) TSLA logosu yok (logo/ klasöründe değil; shell CDN'e çıkamıyor, Enes logo PNG atarsa logo/'ya eklenir ve logo_dogrula.py ile onaylanır).


## PRO v4 (Enes 27.11 23:42 'daha da geliştir, daha profesyonel')
- cizgi_pro: seritler=[(etiket, değer, renk)] ile sağ üstte 3'lü terminal tarzı kilit rakam şeridi (ör. Zirveden / 200 günlük / Cuma hacmi), son değer renkli etiket kutusunda, eksen yazıları JetBrains Mono ve en çok 5 aralık, son değere yakın eksen yazısı gizlenir, çizgi altı hafif alan dolgusu, referans çizgisi etiketi solda mono (TEYİT 26.000). Logolu dosya kartında logo 150 px.
- Başlık Enes sesiyle (kural 102), sonuç bandı birinci tekil hüküm. Şerit rakamları da tweet rakamları gibi doğrulanmış olmalı.


## ESTETİK KART — kart4 (Enes 27.11 23:43 'görünüş olarak daha estetik istiyorum')
- Yeni varsayılan çizgi kartı: `kart4.cizgi(kicker, baslik, vurgu, seri, kahraman, kahraman_alt, olaylar, ref, alinti, kaynak, out, renk, ticker=, kiyas=, kiyas_ad=)`. Editoryal: Instrument Serif başlık (2. satır italik ve renkli), serif büyük kahraman rakam (Türkçe biçim +%6,8), mono küçük harfli etiketler, ızgarasız grafik, parlayan ince çizgi + yumuşak geçişli alan, köşeden hafif renk ışığı, alıntı biçiminde Enes'in tek cümlelik hükmü, sağ altta serif 'Enes Uludağ'. Şirket kartında logo 170 px sağ üstte, vurgu rengi şirket rengi (NVDA #76B900).
- Fontlar repoda invest/fonts/ (Instrument Serif, JetBrains Mono; OFL). kart4 import edilince yüklenir.
- Denetim kart3.kaydet ile aynı (taşma/çakışma -> yayın yok).

- kart4 v3 TASARIMCI DÜZENİ (Enes 27.11 23:47 'bir tasarımcı gibi düşün'): tek kahraman (beyaz serif dev rakam, işaret küçük-soluk, yön yalnız küçük ▲/▼), tek vurgu rengi (çizgi + italik başlık satırı), 90 px kenar ızgarası, tip ölçeği 11/17/34/58/180, kenardan kenara eksensiz grafik (yalnız zirve, olay, son değer etiketli), sağda yan=[(etiket, değer)] en çok 2 küçük veri, alıntı biçiminde Enes hükmü, ince ayraç çizgileri, iki ışık + gren + vinyet zemin.

## KART4 AİLESİ — 14 TÜR (Enes 27.11 23:49 'en az 10-15 görsel türü, hepsi estetik'); örnekler g/tur/
Hepsi aynı iskelet: üst şerit (mono, harf aralıklı) + iki satırlı serif başlık (2. satır italik vurgu, Enes sesiyle) + ince ayraç + içerik + alıntı biçiminde Enes hükmü + alt bilgi. Tek vurgu rengi (şirket rengi ya da yön). Son 3 tweette kullanılan tür tekrar edilmez.
| tür | fonksiyon | ne zaman |
|---|---|---|
| 01 çizgi | kart4.cizgi | endeks/hisse seyri, kahraman yüzde + 2 yan veri |
| 02 sıralama | kart4.siralama | aynı gün/hafta birden çok hisse kıyası, vurgulanan satır |
| 03 beklenti | kart4.beklenti | bilanço öncesi konsensüs (kural 49), logo |
| 04 sütun | kart4.sutun | çeyreklik gelir/kâr, son çubuk kesikli = beklenti |
| 05 kıyas | kart4.kiyas | A vs B iki dev rakam (faktör, iki şirket, iki dönem) |
| 06 ölçer | kart4.olcer | 0-100 göstergeler (CNN korku, kalabalık endeksi) |
| 07 ısı | kart4.isi | haftalık/günlük getiri ızgarası (6-12 hisse) |
| 08 takvim | kart4.takvim | gelecek hafta bilanço/veri takvimi |
| 09 tarihsel | kart4.tarihsel | taban oranlı tarihsel istatistik (kural 96) |
| 10 söz | kart4.soz | tartışma açan görüş tweeti, yalnız tipografi |
| 11 haber | kart4.haber | son dakika: logo + 3 numaralı olgu |
| 12 aralık | kart4.aralik | 52 haftalık aralıkta konum (2-5 hisse) |
| 13 küçük çoklu | kart4.kucuk_coklu | 4 mini grafik, aynı sektör farklı seyir |
| 14 içeriden | kart4.iceriden | yönetici alımı: dev tutar + kişi + işlem şeridi |
Kurallar: kartlardaki her rakam tweet rakamı gibi 2 kaynak; alıntı Enes sesi (kural 102), alıntı ile veri çelişmez (27.11 dersi: 'bellek ayakta' yazıp Micron −%34 göstermek yanlıştı). Denetim (kural 103) her türde çalışır.

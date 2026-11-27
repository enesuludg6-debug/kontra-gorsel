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

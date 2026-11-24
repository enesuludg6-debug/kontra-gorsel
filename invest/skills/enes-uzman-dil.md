---
name: "enes-uzman-dil"
description: "Enes'in X hesabındaki her tweette okurun 'bu adam işini biliyor' diyeceği uzmanlık izini (sektöre özgü ölçü, birinci elden belge satırı, görünür kendi hesabı, kesin emsal, ikinci derece etki) vermek için kullanılır (kural 74)."
---

# KURAL 74 — Uzman dili ve uzmanlık izi (Enes 24.11.2026 17:39)

Enes: "tweetleri daha profesyonel, daha bilgili yazmak istiyorum; insanlar okurken 'bu adam işinde çok bilgili, donanımlı' desin."

Repo `/home/claude/kontra-gorsel/invest`. Her zaman Türkçe. Bu kural enes-analiz-kalitesi (61-65), yasak.py (54-C/D/E) ve iki kaynak kuralının ÜSTÜNE eklenir; onların yerine geçmez. Uzmanlık, uzun yazmak ya da terim yığmak değildir: doğru ölçüyü seçmek ve onu doğru okumaktır.

## 1. Her tweette en az İKİ uzmanlık izi (U1-U6)
- **U1 Sektöre özgü ölçü.** Genel "gelir arttı" yerine o işin uzmanının ilk baktığı kalem (bölüm 2 sözlüğü). Örnek: sunucuda "YZ sunucu sipariş defteri / çeyrek faturalama", bellekte "HBM payı ve DRAM sözleşme fiyatı", neocloud'da "devreye alınan MW ve GPU kira fiyatı".
- **U2 Birinci elden belge satırı.** Bilgiyi haberden değil belgeden ver ve belgenin kalemini adıyla an: "8-K'daki rehber tablosu", "nakit akış tablosunda tedarikçi borçları", "10-Q'da kalan performans yükümlülüğü (RPO)", "görüşmede CFO'nun marj cümlesi". Belgenin kendisi bir kaynak sayılır; ikinci kaynak yine gerekir.
- **U3 Görünür kendi hesabı.** Hesabı sonuçla birlikte bir kez göster: "14,55 / 12,21 = çeyreklik %19", "95 Mr $ defter / 19 Mr $ çeyreklik YZ geliri = 5 çeyrek". Okur hesabı takip edebilmeli; hesap yalnız doğrulanmış girdilerle.
- **U4 Kesin emsal.** "Geçmişte de oldu" değil, tarih ve rakamla tek emsal: "En son Nisan 2025'te S&P 500 bir günde %9,5 yükselmişti; ertesi gün %3,5 geri verdi." (örnek kalıp; rakamlar tweette yine 2 kaynakla) Emsal 2 kaynaklı; benzerlik ve fark tek cümle (kural 54-C: benzetme değil veri).
- **U5 İkinci derece etki.** Haberin doğrudan etkilediği şirketin bir halka ötesi: kimin maliyeti kimin geliri (sunucu üreticisinin marjı daralırsa bellek tedarikçisinin fiyat gücü), kimin harcaması kimin siparişi (hiperölçekli capex → VRT, AVGO, ANET).
- **U6 Beklenti yapısı.** Yalnız konsensüs değil: tahmin aralığı (en düşük-en yüksek), şirket rehberi ile konsensüs farkı, opsiyonların fiyatladığı hareket ya da önceki çeyrekte aynı kalemin sürprizi.

## 2. Sektör ölçü sözlüğü (U1 için; her tweet en az bir tanesini kullanır)
- **YZ çip / GPU (NVDA, AMD, AVGO, MRVL):** veri merkezi geliri ve payı, brüt marj, ağ (networking) geliri, özel çip (ASIC) müşteri sayısı, stok günleri, tedarik taahhütleri (purchase commitments).
- **Dökümhane / paketleme (TSM, ASML):** gelişmiş düğüm payı (3nm/2nm), CoWoS kapasitesi, kapasite kullanım oranı, capex/gelir.
- **Bellek / depolama (MU, SK Hynix, SNDK, WDC, STX):** HBM gelir payı, DRAM/NAND sözleşme ve spot fiyatı, bit büyümesi vs fiyat (ASP), stok günleri, gelecek yılın satılmış kapasitesi.
- **Sunucu / donanım (DELL, HPE, SMCI):** YZ sunucu siparişleri ve sipariş defteri, defter/faturalama oranı, YZ sunucu brüt marjı, bellek maliyetinin geçişi (pass-through), işletme sermayesi (stok + tedarikçi borcu).
- **Ağ / optik (ANET, CRDO, ALAB, AAOI, COHR, LITE):** 800G/1.6T geçişi, hiperölçekli müşteri yoğunlaşması, sipariş/satış (book-to-bill), kapasite artışı.
- **Veri merkezi güç / soğutma (VRT, ETN, GEV):** sipariş defteri ve büyümesi, sipariş/satış, sıvı soğutma payı, ön ödemeler, kapasite yatırımı.
- **Bulut / neocloud (DOCN, NBIS, CRWV, ORCL, IREN):** devreye alınan ve sözleşmeli MW, GPU kira fiyatı ($/saat), kullanım oranı, kalan performans yükümlülüğü (RPO), borç/FAVÖK, capex finansmanı (borç, hisse satışı, ön ödeme), müşteri yoğunlaşması.
- **YZ yazılımı / siber güvenlik (CRWD, NET, DDOG, PLTR):** net yeni ARR, net gelir tutma (NRR), RPO, serbest nakit marjı, 40 kuralı (büyüme + FCF marjı).
- **Uzay (RKLB, ASTS, LUNR, PL):** sipariş defteri, fırlatma sıklığı ve fırlatma başına fiyat, nakit yakımı ve nakdin yeteceği çeyrek sayısı, ilk uçuş tarihi.
- **Makro (Fed, PCE, istihdam):** çekirdek değer ve aylık değişim, beklentiden sapma (baz puan), vadeli faiz fiyatlaması (FedWatch), 2 yıllık / 10 yıllık getiri ve reel faiz.

## 3. Profesyonel ton (kural 60 ve 64'ü tamamlar)
- Tek net hüküm, rakamla gerekçelendirilmiş. Belirsizlik varsa koşulla söylenir ("X %Y'nin altında kalırsa"), "belki/sanki" yok.
- Terim doğru ve yerinde kullanılır; tweette en çok iki terim, gerekirse yanına 3-5 kelimelik açıklama (ör. "RPO, yani imzalı ama henüz faturalanmamış sözleşmeler"). Uzun açıklama "Ne anlama geliyor?" mesajına gider.
- Haber tekrarı değil yorum: ilk cümle haberi, ikinci cümle haberin herkesin kaçırdığı tarafını (U2-U5) verir.
- Kaynak gücü: mümkün olduğunda birincil belge (SEC 8-K/10-Q, şirket bülteni, görüşme transkripti, Conference Board/BEA/Fed) haber sitesinin önüne konur.

## 4. Kontrol
- Yazmadan önce: bu tweetin U1-U6'dan hangi ikisini taşıdığını DONGU kaydına yaz ("uzman: U1+U3").
- `python3 invest/kalite.py kontrol` mevcut kuralları denetler; uzmanlık izini sen denetlersin. İki iz yoksa tweet atılmaz, ölçü eklenir.
- Haftalık performans raporu (Pazar 21:30) U izlerine göre medyan görüntülenmeyi ölçer (DONGU "uzman:" etiketinden); işe yarayan izler öne çıkarılır.

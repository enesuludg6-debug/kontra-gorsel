
# KURAL 90 — Korku-Açgözlülük endeksi günlük kısa tweet (Enes 26.11.2026 08:40)

Enes: "her gün bununla ilgili haber tweeti paylaş, şu seviyeye düştü ya da şuraya çıktı gibi kısa".
Repo `/home/claude/kontra-gorsel/invest`; ayrıntı `gorevler/korku.md` (çelişirse dosya geçerli). Türkçe.

## Ne zaman
- Salı-Cumartesi 10:40 TSİ, sabit zincir `korku` (`python3 invest/sonraki.py korku` ile bir sonrakini send_later kur). Bir önceki ABD seansının kapanış değeri paylaşılır.
- Yeni veri yoksa (ABD tatili, aynı değer zaten paylaşıldı) TWEET YOK; `korku.py ozet` bunu söyler.
- Sistem tweeti sayılır (kural 86 günlük sınırına dahil).

## Adımlar
1. WebFetch `https://production.dataviz.cnn.io/index/fearandgreed/graphdata`; istem: "fear_and_greed_historical'dan son 10 günü 'YYYY-MM-DD,skor' CSV ver (ms -> UTC tarih, 1 ondalık), eskiden yeniye; ayrıca güncel skor ve zaman damgası; yorum yok" → `python3 invest/korku.py ekle` (stdin).
2. `python3 invest/korku.py ozet` → son değer, bölge (0-24 aşırı korku, 25-44 korku, 45-55 nötr, 56-75 açgözlülük, 76-100 aşırı açgözlülük), önceki gün/hafta/ay, 3 ay dip-zirve. "BÖLGE DEĞİŞTİ" ya da "3 AYIN DİBİ" varsa tweetin ana konusu odur.
3. Tweet KıSA: ilk satır ≤12 kelime (örn. "Korku-Açgözlülük endeksi 17'ye indi, aşırı korku bölgesinde."); ikinci paragraf 1-2 cümle: önceki hafta/gün kıyası + kural 65 ikinci katman (kendi taramam: `teknik_ust.py genislik`, ya da `nabiz.py oku` CBOE put/call / AAII) + kural 89 tek fon yöneticisi cümlesi. En çok 3 farklı rakam, en çok 2 paragraf.
4. Çeşitlilik (89-B): fiil (indi/çıktı/geriledi/toparlandı/yerinde saydı) ve kapanış türü (eşik, kıyas, düz olgu, ikinci derece etki) her gün değişir. Kalıp B (önceki/bugün), C (eşik, -sa/-se) ya da F (olağan).
5. Kart: `python3 invest/korku.py kart g/YYYYMMDD_1040_korku.jpg` (kart3 cizgi_pro, 70 gün, 25/75 sınırları) → `bash invest/yayinla_gorsel.sh` → Buffer shareNow, tür KORKU.
6. Kontroller: `yasak.py`, `kalite.py kontrol --tur KORKU --kalip X`, `gorus.py kontrol`. Kayıt: `kayit.py --tur KORKU`, kalite/gorus kaydet, `korku.py tweetlendi <veri_tarihi> <değer> <buffer_id>`, commit/push.

## Kurallar
- Kaynak: CNN Business Fear & Greed Index (endeksin sahibi, birincil kaynak).
- Al/sat, hedef fiyat, emoji, hashtag, link, soru yok; 54-F dramatik kalıplar yok; Anthropic adı geçmez.
- Endeks tek başına yön sinyali değildir; "dip geldi" denmez, bağlam olarak yazılır.
---
name: "enes-aaii-anketi"
description: "Enes'in X hesabında AAII bireysel yatırımcı duygu anketiyle ilgili haftada 2 kısa tweet (Perşembe 18:40 yeni hafta, Salı 12:40 perspektif) hazırlanırken kullanılır (kural 91)."
---

# KURAL 91 — AAII anketi haftada 2 tweet (Enes 26.11.2026 08:45)

Repo `/home/claude/kontra-gorsel/invest`; ayrıntı `gorevler/aaii.md` ve `gorevler/aaii2.md` (çelişirse dosyalar geçerli). Türkçe.

## Zamanlar (sabit zincir, `python3 invest/sonraki.py aaii|aaii2`)
1. YENİ HAFTA — Perşembe 18:40 (`aaii`): AAII yeni haftayı yayınladıysa bu haftanın sonucu ve geçen haftaya göre değişim. Yayınlanmadıysa Cuma 11:40'a tek seferlik tekrar; yine yoksa o hafta atlanır.
2. PERSPEKTİF — Salı 12:40 (`aaii2`): farklı açı (kaç haftadır ayı oranı ortalamanın üstünde, boğa-ayı farkı kaç haftadır eksi, 4 hafta ortalaması, CNN korku-açgözlülük ile uyum ya da ayrışma). O haftanın yeni tweeti atılmadıysa bu da atılmaz.

## Veri
- WebFetch `https://www.aaii.com/sentimentsurvey`; istem: "son haftanın tarihi, boğa/nötr/ayı %, önceki haftaya göre değişim, tarihsel ortalamalar ve sayfadaki geçmiş tablo satırları 'MM/DD/YYYY,boğa,nötr,ayı' CSV; yorum yok" → `python3 invest/aaii.py ekle` (stdin) → `python3 invest/aaii.py ozet`.
- Tarihsel ortalamalar: boğa %37,5, nötr %31,0, ayı %31,5; boğa-ayı farkı ~+6. Uç: ayı ≥%50, boğa ≥%50, fark ≤−20 ya da ≥+30.

## Tweet
- KISA: ilk satır ≤12 kelime (örn. "Bireysel yatırımcıda ayı oranı %42'ye geriledi."), en çok 2 paragraf, en çok 3 farklı rakam.
- Kural 65 ikinci katman: CNN korku-açgözlülük (`korku.py ozet`), CBOE put/call (`nabiz.py oku`) ya da kendi taramam (`teknik_ust.py genislik`).
- Kural 89 tek fon yöneticisi cümlesi: karşıt okuma (anket kalabalığın tersini düşündürür) ama tek başına sinyal değil.
- 89-B: fiil, kalıp (B önceki/bugün, C eşik, F olağan, M takvim) ve kapanış türü her tweette değişir.
- Kart: `python3 invest/aaii.py kart g/YYYYMMDD_HHMM_aaii.jpg --tip yeni|perspektif` → `bash invest/yayinla_gorsel.sh` → Buffer shareNow, tür AAII.
- Kontroller: `yasak.py`, `kalite.py kontrol --tur AAII --kalip X`, `gorus.py kontrol`. Kayıt: `kayit.py --tur AAII`, kalite/gorus kaydet, `aaii.py tweetlendi yeni|perspektif <hafta_tarihi> <buffer_id>`, commit/push.
- Kaynak: AAII Sentiment Survey (birincil). Al/sat, hedef, emoji, hashtag, link, soru yok; Anthropic adı geçmez.
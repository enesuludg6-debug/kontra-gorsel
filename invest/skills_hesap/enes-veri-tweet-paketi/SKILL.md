---
name: "enes-veri-tweet-paketi"
description: "Enes'in X hesabında haftalık kısa veri tweetleri (VIX vade yapısı, kredi primi, Nasdaq genişliği, put/call, açığa satış, Fed likidite, yönetici alımları, faiz eğrisi) hazırlanırken kullanılır (kural 92)."
---

# KURAL 92 — Veri tweet paketi (Enes 26.11.2026 08:49: "1-2-3-4-5-6-7-8 hepsi okey")

Repo `/home/claude/kontra-gorsel/invest`; her konu için ayrıntı `gorevler/<anahtar>.md` (çelişirse dosya geçerli). Araç: `python3 invest/veri_icerik.py <anahtar> [--kart g/YYYYMMDD_HHMM_<anahtar>.jpg]`. Türkçe.

## Takvim (sabit send_later zincirleri; `python3 invest/sonraki.py <anahtar>`)
| anahtar | zaman (TSİ) | içerik | veri |
|---|---|---|---|
| vix | Cuma 18:10 | korku vade yapısı VIX/VIX3M, 1 üstü = ters dönmüş | Yahoo (otomatik) + 20 yıl kanıt |
| kredi | Çarşamba 12:10 | yüksek getirili tahvil primi | FRED BAMLH0A0HYM2 (WebFetch → fred_ekle) |
| genislik | Cumartesi 12:10 | Nasdaq 100 50G/200G üstü oran, yıllık dibe yakın | kendi hesabım (Yahoo) |
| putcall | Cumartesi 15:10 | CBOE hisse put/call 5 gün ort. | nabiz.json (sabah birikir; <5 gün = tweet yok) |
| aciga | Pazartesi 12:10 | portföy açığa satış 4 hafta değişim | Bigdata.com history_tearsheet (ORTEX) → alt_veri.py si |
| fed | Cuma 12:10 | Fed net likidite = bilanço − Hazine hesabı − ters repo | FRED WALCL, WTREGEN, RRPONTSYD |
| iceriden | Perşembe 12:10 | son 30 gün yönetici alım/satımı | Alpha Vantage INSIDER_TRANSACTIONS (sırayla, bütçe) |
| faiz | Pazartesi 16:10, yalnız çift ISO hafta | 10Y−2Y eğri + 10 yıllık reel faiz | FRED T10Y2Y, DFII10 |

FRED WebFetch: `https://fred.stlouisfed.org/graph/fredgraph.csv?id=<SERİ>&cosd=<bugün−120 gün>`; istem "tüm satırları 'YYYY-MM-DD,değer' CSV, yorum yok" → `veri_icerik.py fred_ekle <SERİ>` (cosd olmadan dosya 2000 yılında kesilir). Birimler: WALCL ve WTREGEN milyon $, RRPONTSYD milyar $.

## Tweet
- KISA: ilk satır ≤12 kelime, net olgu ("X şu seviyeye indi/çıktı"); en çok 2 paragraf, en çok 3 farklı rakam.
- Kural 65 ikinci katman: başka bir nabız verisiyle uyum ya da ayrışma (`korku.py ozet`, `nabiz.py oku`, `veri_icerik.py genislik|vix`).
- Kural 89 tek fon yöneticisi cümlesi; 89-B fiil, kalıp ve kapanış türünü her tweette değiştir.
- Kanıt kuralı: istatistik verilirse taban oranla (örn. VIX/VIX3M 1 üstü: 69 olay, 20 gün sonra %67 vs taban %65 = fark yok; "dip sinyali" deme).
- Kart → `bash invest/yayinla_gorsel.sh` → Buffer shareNow; tür VERI-<ANAHTAR>. Kontroller: `yasak.py`, `kalite.py kontrol --tur VERI-<ANAHTAR> --kalip X`, `gorus.py kontrol`. Kayıt: `kayit.py`, kalite/gorus kaydet, commit/push.
- Veri yoksa ya da değişim anlamsızsa (tatil, aynı değer) TWEET YOK, DONGU'ya yaz.
- Al/sat, hedef, emoji, hashtag, link, soru yok; kaynak adı kartta; Anthropic adı geçmez.
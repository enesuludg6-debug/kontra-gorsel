---
name: "enes-pro-veri-paketi"
description: "Enes'in X hesabında profesyonel haftalık veri tweetleri (Fed vadeli beklentisi, SKEW/VVIX, hisse-tahvil korelasyonu, sektör rotasyonu, faktörler, bakır/altın, kâr tahmini revizyonu, bilanço öncesi tepki) hazırlanırken kullanılır (kural 93)."
---

# KURAL 93 — Profesyonel veri paketi (Enes 26.11.2026 08:55: "bunlar da tamam, bunları da ekle")

Repo `/home/claude/kontra-gorsel/invest`; ayrıntı `gorevler/<anahtar>.md` (çelişirse dosya geçerli). Araç: `python3 invest/veri_icerik2.py <anahtar> [--kart g/YYYYMMDD_HHMM_<anahtar>.jpg]`. Türkçe.

## Takvim (sabit send_later zincirleri; `python3 invest/sonraki.py <anahtar>`)
| anahtar | zaman (TSİ) | içerik | veri |
|---|---|---|---|
| fedwatch | Salı 18:10 | Fed fon vadelilerinden toplantı başına fiyatlanan faiz değişimi ve olasılık (kendi hesabım, CME FedWatch yöntemi) | Yahoo ZQ (örn. ZQZ26.CBT); İKİNCİ KAYNAK CME FedWatch haberi (WebSearch), fark >15 puan ise tweet yerine Enes'e not |
| kuyruk | Perşembe 16:10 | SKEW (çöküş sigortası) + VVIX (korkunun oynaklığı), 5 yıl yüzdelik | Yahoo |
| korelasyon | Çarşamba 16:10, tek ISO hafta | QQQ-TLT 60 günlük korelasyon: tahvil hisseye karşı korunma mı | Yahoo |
| rotasyon | Pazar 16:10 | 11 sektör göreli güç + ivme, dört bölge (kesitsel normalize), bölge değiştirenler | Yahoo SPDR ETF'leri |
| faktor | Cuma 16:10 | momentum, değer, küçük şirket, eşit ağırlık, Nasdaq'ın S&P'ye göre 1 ay/3 ay farkı | Yahoo |
| bakir_altin | Salı 16:10, tek ISO hafta | bakır/altın oranı ve 10Y faiz: büyüme barometresi | Yahoo HG=F, GC=F, ^TNX |
| revizyon | Pazartesi 18:10 | portföy en yakın mali yıl EPS konsensüsü haftalık değişimi (yukarı/aşağı sayısı) | Bigdata.com `bigdata_computer` estimates + earnings_history (ilk hafta yalnız kayıt) |
| bilanco | portföyde 2 gün içinde bilanço varsa o gün 16:10 (sabah `veri_icerik2.py yaklasan 2` tetikler) | son 8 bilançoda fiyat tepkisi | `alt_veri/bilanco_tarih.csv` + Yahoo |

FOMC karar günleri kodda (`FOMC` listesi; Fed 12.11.2026 revize takvim: 09.12.2026, 27.01, 17.03, 28.04, 09.06, 28.07, 15.09, 17.11.2027; 27.10.2027 strateji toplantısı, karar yok). Yeni yıl takvimi açıklanınca güncelle.

## Tweet
- KISA: ilk satır ≤12 kelime net olgu; en çok 2 paragraf, en çok 3 farklı rakam. Teknik terimi bir kez Türkçe açıkla (örn. "SKEW, derin düşüşe karşı opsiyon talebi").
- Kural 65 ikinci katman (başka nabız verisiyle uyum/ayrışma) + kural 89 tek fon yöneticisi cümlesi; 89-B çeşitlilik. Kanıt verilirse taban oranla.
- Kart → `bash invest/yayinla_gorsel.sh` → Buffer shareNow; tür VERI-<ANAHTAR>. Kontroller: `yasak.py`, `kalite.py kontrol`, `gorus.py kontrol`; kayıt `kayit.py`, kalite/gorus kaydet, commit/push.
- Veri yoksa / değişim anlamsızsa TWEET YOK. Hafta sonu tavanı 10 (kural 86): Cumartesi/Pazar dolarsa bu tweetler önce atlanır.
- Al/sat, hedef, emoji, hashtag, link, soru yok; Anthropic adı geçmez.
## Kalabalık endeksi (kural 97, 27.11)
Cumartesi 18:10: `python3 invest/kalabalik.py hesap` + `kart`. Bireysel iyimserlik (CNN korku, AAII farkı, hisse put/call) ve kurumsal sakinlik (VIX/VIX3M yüzdelik, SKEW, endeks put/call), 0-100, kendi ölçeğimiz. SentimenTrader gibi ücretli kaynakların verisi, grafiği ya da linki kullanılmaz. Fark ≥+25: kalabalık korkuyor, kurumlar korunmuyor (dip davranışı); ≤−25: tepe riski. Tweet kısa, 'kendi ölçeğim', tek başına sinyal değil cümlesi.

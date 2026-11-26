---
name: "enes-akis-puan"
description: "Enes Unusual Whales opsiyon akışı / karanlık havuz ekran görüntüsü attığında kendi teknik analizimizle birleştirip her hisseye 1-10 uyum puanı verip sıralarken kullanılır (kural 94)."
---

# KURAL 94 — Kurumsal ayak izi + teknik uyum puanı (Enes 26.11 10:16)

Repo `/home/claude/kontra-gorsel/invest`. Her zaman Türkçe. Repodaki `invest/skills/enes-akis-puan.md` kopyasıyla çelişirse kopya geçerli.

Enes: ekran görüntülerini olduğu gibi yorumlama; kendi teknik analizini yap, bizim teknik düşüncemize en çok uyanları daha çok beğendiğini söyle, 1-10 puanla ve sırala.

Kaynak: arkadaşının Unusual Whales Retail Pro hesabı; listeler "Enes" (portföy 8) ve "Enes Takip" (ilgi listesi 23). Görüntüler TSİ sabah gelir.

## Akış
1. Her görüntüyü Read ile aç. Her hisse için yalnız GÖRÜNEN değerleri /tmp/akis.json'a yaz (`python3 invest/akis_puan.py sablon` biçimi): call_prim / put_prim (M$), sweep_call / sweep_put, uzun_vade (büyük işlemler >= 30 gün), dp [[fiyat, milyon adet]], not (en büyük 1-2 işlem). Görünmeyen alan boş; tahmin yok. Okunamayan görüntüyü Enes'e tek cümleyle söyle.
2. `python3 invest/akis_puan.py puan /tmp/akis.json --kart`. Gerekirse smc_ek.py, formasyon.py, raindrop.py ile kontrol (enes-teknik-smc kanıt kuralı: taban oran + Wilson).
3. Enes'e SendUserMessage: "Kurumsal ayak izi + teknik uyum — GG.AA"; en çok beğendiklerim (>=7) sıra + puan + 2 satır neden (akış + teknik + çakışma); orta (4-6) tek satır; beğenmediklerim (1-3) tek satır neden; çelişkiler ayrı. Kart SendUserFile g/akis_puan_<tarih>.png.
4. DONGU: "- SS:DD (GG.AA) AKIS-PUAN: <ilk 3 hisse ve puanları>".

## Puan (10)
TEKNİK 6 = T1 dip bölgesi 2 (aşırı satım 1 + destek yakını 1) + T2 kanıtlı kalıp 2 (yalnız tarama_kanit ÜSTÜN: dip_avcisi, derin_dip; kanıtsız dip kalıbı 1) + T3 dönüş izi 1 + T4 büyük trend 1 (EMA200 üstü ya da haftalık supertrend yukarı).
AKIŞ 4 = A1 call primi payı (>=%65: 2, >=%55: 1) + A2 uzun vade ve call sweep ağırlığı 1 + A3 karanlık havuz bloğu fiyatın 1 ATR içinde 1.
CEZA: bilanço <= 7 gün -1, destek kırılımı -1, aşırı uzama -1. Sonuç 1-10.
Ölçüm: `akis_puan.py olc` (20 işlem günü, n>=10); puan>=7 <7'den iyi gitmiyorsa Enes'e ağırlık değişikliği öner.

## Yasaklar
- Al, sat, hedef fiyat yok; "bizim yaklaşımımıza uyum" dili.
- Otomatik tweet yok. Gruba ham veri ya da UW ekran görüntüsü gitmez; yalnız bizim yorum ve kartımız.
- Karttaki tek imza "ENES ULUDAĞ" sağ alt.
# KURAL 94 — Kurumsal ayak izi + teknik uyum puanı (Enes 26.11 10:16)

Enes: "ekran görüntülerini attığım zaman onları olduğu gibi yorumlamayacaksın, aynı zamanda kendi teknik analizini yapacaksın ve bizim teknik düşüncemize en çok uyanları daha çok beğendiğini söyleyeceksin, 1'le 10 üzerinden sıralarsın."

Kaynak: arkadaşının Unusual Whales Retail Pro hesabı; listeler "Enes" (portföy 8) ve "Enes Takip" (ilgi listesi 23). Görüntüler TSİ sabah gelir.

## Akış
1. Her görüntüyü Read ile aç. Her hisse için yalnız GÖRÜNEN değerleri /tmp/akis.json'a yaz (`python3 invest/akis_puan.py sablon` biçimi): call_prim / put_prim (M$), sweep_call / sweep_put (ask tarafı sweep sayısı), uzun_vade (büyük işlemler >= 30 gün), dp [[fiyat, milyon adet]], not (en büyük 1-2 işlem: vade, kullanım fiyatı, prim). Görünmeyen alan boş; tahmin yok. Okunamayan görüntü varsa Enes'e hangisi olduğunu tek cümleyle söyle.
2. `python3 invest/akis_puan.py puan /tmp/akis.json --kart` çalıştır. Gerekirse puanı yükselten/düşüren unsuru smc_ek.py, formasyon.py, raindrop.py ile kontrol et (skill enes-teknik-smc kanıt kuralı: taban oran + Wilson).
3. Enes'e SendUserMessage:
   - Başlık: "Kurumsal ayak izi + teknik uyum — GG.AA"
   - En çok beğendiklerim (puan >= 7): sıra, puan, 2 satır neden (akış ne diyor + teknik ne diyor + çakışma).
   - Orta (4-6): tek satır.
   - Beğenmediklerim (1-3): tek satır, neden (ör. "call alımı var ama fiyat EMA200 altında ve haftalık trend aşağı; bizim tarz değil").
   - Çelişkiler: akış güçlü ama teknik zayıf (ya da tersi) olanları ayrıca belirt.
   - Kart: SendUserFile g/akis_puan_<tarih>.png.
4. DONGU: "- SS:DD (GG.AA) AKIS-PUAN: <ilk 3 hisse ve puanları>".

## Puan (10)
TEKNİK 6 = T1 dip bölgesi 2 + T2 kanıtlı kalıp 2 (yalnız tarama_kanit ÜSTÜN: dip_avcisi, derin_dip; kanıtsız dip kalıbı 1) + T3 dönüş izi 1 + T4 büyük trend 1.
AKIŞ 4 = A1 call primi payı (>=%65: 2, >=%55: 1) + A2 uzun vade ve call sweep ağırlığı 1 + A3 karanlık havuz bloğu fiyatın 1 ATR içinde 1.
CEZA: bilanço <= 7 gün -1, destek kırılımı -1, aşırı uzama -1. Sonuç 1-10.
Ağırlıklar sabit; ölçüm (`akis_puan.py olc`, 20 işlem günü ve n>=10 sonra) puan>=7'nin <7'den iyi gitmediğini gösterirse Enes'e ağırlık değişikliği öner.

## Yasaklar
- "Al", "sat", hedef fiyat yok; "bizim yaklaşımımıza uyum" dili.
- Otomatik tweet yok. Gruba ham veri / UW ekran görüntüsü gitmez; yalnız bizim yorum ve kartımız.
- Karttaki tek imza "ENES ULUDAĞ" sağ alt.

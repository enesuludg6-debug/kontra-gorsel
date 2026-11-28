---
name: enes-opsiyon-akisi
description: Enes'in X hesabında günde en az 1 opsiyon akışı (büyük put/call bahsi) tweeti hazırlanırken, akış hesapları taranıp kontrat Yahoo'dan doğrulanırken kullanılır (kural 121).
---
# KURAL 121 — OPSİYON AKIŞI TWEETİ (Enes 28.11 21:45)
Enes FL0WG0D'nin "Small $SPY bear" (SPY 694 put, 27.11 vade, 11:10'da 2.180 kontrat ask'tan, ort. 2,15, mum primi 468,9 bin $) ekranını attı: "bu tarz tweetler de atacağız, bu tarz tweet atan hesapları bul, günde en az bir tane, üst sınır yok".

## Sıklık
- Her gün EN AZ 1 (hafta sonu dahil; hafta sonu cuma akışının sonucu yazılır). Üst sınır yok. Tur `AKIS`, sayaç gun_ozet.py "AKIS n/1".
- En iyi saat: ABD seansı içinde (akış canlı) ya da kapanış sonrası "sonucu ne oldu".

## Kaynak hesaplar (yalnız arama motoru; x.com fetch/oturum YOK)
FL0WG0D (Flow God), unusual_whales, CheddarFlow, FlowAlgo, Bullflow (bullflow), tradytics, InsiderFinance, QuantData. Takipçi sayısı takipci.py defterine; 111-T oranı (görüntülenme / takipçi ≥5x) olanlar önce.
- Arama: WebSearch allowed_domains ["x.com","twitter.com"], sorgu "<hesap> $TICKER puts/calls sweep" ya da "unusual options activity <tarih>".
- Ücretli platform verisi (abone içeriği, Discord) KULLANILMAZ; yalnız herkese açık tweet + kendi doğrulamamız.

## Doğrulama (zorunlu, 2. kaynak)
`python3 invest/akis_tara.py <TICKER> <vade YYYY-AA-GG> <C|P> <kullanım fiyatı>` → Yahoo v8 opsiyon sembolü günlük kapanış + hacim + dayanak fiyatı. O günkü hacim akıştaki kontrat sayısıyla tutarlı değilse tweet ATILMAZ. Prim = kontrat x fiyat x 100 kendi hesabın. (Yahoo v7 zinciri ve Alpha Vantage opsiyon bu ortamda kapalı.)

## Yazım (3 paragraf, 400-900 karakter, kalıp serbest)
1. Kanca: kim/ne değil, PARA: "$X'te <gün> düşüşe/yükselişe yaklaşık N bin dolarlık bahis açıldı."
2. Kontrat sade Türkçe: vade, kullanım fiyatı, put/call ne demek (113-F "yani"), kaç kontrat, hangi fiyattan, ask'tan mı (agresif alıcı), dayanağa uzaklık %.
3. Benim yorumum: hedge mi yön bahsi mi, vade kısa mı, ne fiyatlanıyor; sonuç belliyse "ne oldu" (tuttu/tutmadı ikisi de yazılabilir, bu bir gözlem tweeti, Enes'in kendi yorumu değil). Kapanış 118 tek akış.
- Al/sat tavsiyesi, "takip edin", hesap adı anma (Enes istemedikçe) YOK. Ekran görüntüsü kopyalanmaz (abone içeriği); kart istenirse kart4 kendi verimizle.
- 116: kullanım fiyatı/vade AKIS tweetinde serbest (kalite.py AKIS istisnası); işlem fiili yine yasak.
- 113/114/118 aynen.

## Örnek (28.11 22:00 zamanlandı)
"$SPY'da 24 Kasım sabahı düşüşe yaklaşık 470 bin dolarlık bahis açıldı. / Kontrat 27 Kasım vadeli 694 put, yani endeks fonu 694 doların altına inerse para kazandıran bir sigorta. Alıcı 2.180 kontratı satıcının istediği fiyattan (ask), ortalama 2,15 dolardan topladı. ... / Düşüş gelmedi. $SPY cuma günü 728 dolardan kapattı ve put vadeyi 0,01 dolardan bitirdi. ..."

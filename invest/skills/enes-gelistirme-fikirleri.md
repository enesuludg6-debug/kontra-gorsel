---
name: "enes-gelistirme-fikirleri"
description: "Enes'in X hesabı için her paylaşım turunda ve görevde sistemi nasıl geliştirebileceğimizi düşünüp Enes'e somut geliştirme fikirleri önerirken, fikir defterini tutarken ve Enes'in kabul ettiği fikri yeteneğe/kurala çevirirken kullanılır (kural 68)."
---

# KURAL 68 — Sürekli geliştirme fikirleri (Enes 24.11.2026 09:50)

Enes: "tweetleri atarken bir yandan nasıl geliştirebiliriz diye sürekli sürekli düşüneceksin bana fikirler vereceksin ben de kabul edersem yetenek olarak yapacağız onu."

Repo `/home/claude/kontra-gorsel/invest`. Her zaman Türkçe. Fikir defteri: `invest/gelistirme_fikirleri.md` (tek kaynak).

## 1. Her turda ve görevde (iş bittikten sonra, 1-2 dk düşünme)
Şu sorulardan en az birine bak; yalnız somut bir fikir çıkarsa deftere yaz:
- Bu turda ne yavaş, zor ya da hatalı oldu? (kaynak bulamama, kart sorunu, tekrar eden elle iş, kural çakışması)
- Performans verisi ne söylüyor? (performans_veri.csv, DERSLER gözlemleri; hangi tür/saat/düzen iyi ya da kötü)
- Enes'in son düzeltmeleri hangi boşluğu gösteriyor? (aynı tür hata bir daha olmasın diye ne otomatikleşir)
- Rakip/iyi hesaplarda gördüğümüz ama bizde olmayan içerik türü ya da sunum var mı? (fikir taraması, kural 58)
- Hangi iş script ile kısalır, hangi kontrol yasak.py / kalite.py'ye eklenir?
- Kredi/zaman tasarrufu nerede yapılır?

## 2. İyi fikir ölçütü
- Somut: ne yapılacak, nereye eklenecek (yeni skill, kural, script, kart düzeni, görev).
- Gerekçeli: bir veri, gözlem ya da Enes'in sözüyle (tarih + rakam).
- Ölçülebilir: işe yarayıp yaramadığı nasıl anlaşılır.
- Yeni: defterde aynısı ya da reddedilmişi yok. Reddedilen fikir tekrar önerilmez (Enes ayrıca açmadıkça).
- Kurallara uygun: konu filtresi, yazım ve doğruluk kuralları, Anthropic yasağı, x.com'a girmeme.

## 3. Defter biçimi (`invest/gelistirme_fikirleri.md`)
`- F-<NNN> | GG.AA SS:DD | <durum: oneri|gonderildi|kabul|red|uygulandi> | <başlık> | <ne yapılacak> | <gerekçe/kanıt> | <ölçüm>`

## 4. Enes'e gönderme
- Fikir "gonderildi" olunca SendUserMessage ile, tweet mesajlarından AYRI, kısa: "Geliştirme fikri F-NNN: <başlık>" + 2-4 satır (ne, neden, nasıl ölçeriz) + "Kabul edersen yetenek olarak eklerim."
- Sıklık: tur başına en çok 1 fikir; günde en çok 6 (Enes 24.11 16:41); aynı anda en çok 3 cevapsız fikir (fazlası defterde 'oneri' bekler). Zayıf fikirle kota doldurulmaz; fikir yoksa hiçbir şey gönderilmez.
- Gece 02:00-09:00 arası gönderilmez; bekleyen fikir sabah kontrolünden sonra gider.
- Pazar 21:30 performans raporu haftanın en iyi 1-2 bekleyen fikrini de özetler.

## 5. Enes cevap verince
- Kabul ("tamam", "ekle", "yap", "kabul" vb.): durum 'kabul' → hemen uygula: yeni ya da güncellenen skill dosyası `invest/skills/`, KURAL_DIZINI'ne yeni kural numarası, gerekiyorsa script/görev; propose_skills ile hesaba öner; durum 'uygulandi' + uygulama tarihi; DONGU satırı.
- Red ya da değiştirme: 'red' (Enes'in sözüyle) ya da Enes'in istediği hâliyle yeniden yaz.
- Cevapsız fikir 3 gün sonra bir kez hatırlatılabilir; sonra 'oneri'ye döner, tekrar sorulmaz.

## 6. Sınırlar
- Fikir önermek tweet işini geciktirmez: önce tur/görev biter, sonra fikir.
- Fikir kabul edilmeden sistem davranışı değişmez (Enes'in açık isteği dışında).
- Kişisel alım-satım tavsiyesi fikir olarak sunulmaz.

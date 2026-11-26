---
name: "enes-gelistirme-fikirleri"
description: "Enes'in X hesabı için her paylaşım turunda ve görevde sistemi nasıl geliştirebileceğimizi düşünüp Enes'e somut geliştirme fikirleri önerirken, fikir defterini tutarken ve Enes'in kabul ettiği fikri yeteneğe/kurala çevirirken kullanılır (kural 68)."
---

# KURAL 68 — Sürekli geliştirme fikirleri (Enes 24.11.2026 09:50)

Enes: "tweetleri atarken bir yandan nasıl geliştirebiliriz diye sürekli sürekli düşüneceksin bana fikirler vereceksin ben de kabul edersem yetenek olarak yapacağız onu."

Repo `/home/claude/kontra-gorsel/invest`. Her zaman Türkçe. Fikir defteri: `invest/gelistirme_fikirleri.md` (tek kaynak). Repodaki `invest/skills/enes-gelistirme-fikirleri.md` kopyasıyla çelişirse kopya geçerli.

## 0. KURAL 68-B — FİKİRLERİN YÖNÜ (Enes 24.11 20:24, ÖNCE BUNU UYGULA)
Enes: "bundan sonra istediğim fikirler daha çok tweet'leri geliştirme yönünden, insanların daha çok beğenmesi, daha çok etkileşim ve daha çok takipçi kazanması yönünden olsun. Amacımız insanların daha çok beğenmesi, daha çok öğrenmesi, bizim daha bilgili ve daha profesyonel gözükmemiz, daha çok etkileşim alması."
- Fikirlerin ANA hedefi (hepsi birlikte): (1) daha çok beğeni ve etkileşim (yanıt, repost, alıntı, kaydetme), (2) daha çok takipçi, (3) okurun daha çok ÖĞRENMESİ, (4) hesabın daha BİLGİLİ ve PROFESYONEL görünmesi.
- Fikirlerin EN AZ 5'te 4'ü bu hedeflere dönük olur: içerik türü, açılış cümlesi/kanca, kart tasarımı, seri/format (ör. haftalık sabit seri), saat, uzunluk, kavram öğretme biçimi, veri sunumu, uzmanlık izi, gündem yakalama hızı, okuru konuşmaya çeken (ama soruyla bitmeyen) yapı, takip etme sebebi yaratan tekrar eden formatlar.
- İç işleyiş/hata önleme fikirleri (betiği, defter, logo gibi) yalnız bir hata tweet kalitesini ya da güveni doğrudan tehdit ediyorsa önerilir; en çok 5'te 1.
- Her fikirde "hangi hedefe hizmet ediyor" (beğeni/etkileşim, takipçi, öğrenme, profesyonel görünüm) açıkça yazılır ve KANIT olarak mümkünse performans verisi (performans_veri.csv, ders_analiz.py, bilanco_perf.py: görüntülenme, beğeni, yanıt, repost; tür/saat/düzen/uzunluk kırılımı) kullanılır.
- Ölçüm her zaman etkileşim metriğiyle: görüntülenme, beğeni oranı, yanıt+repost, takipçi değişimi (2 hafta, göreli skor).
- Kesin kurallar değişmez: 2 kaynak, al/sat yok, Anthropic yasağı, x.com'a girmeme, kural 46/73 konu alanı, soruyla bitmeme, emoji/hashtag yok. Etkileşim için abartı, tık tuzağı ya da doğrulanmamış iddia ÖNERİLMEZ.

## 1. Her turda ve görevde (iş bittikten sonra, 1-2 dk düşünme)
Önce KURAL 68-B sorusu: "Bu turdaki tweet daha çok beğenilsin, daha çok öğretsin, daha profesyonel dursun diye ne değişebilirdi?" Sonra:
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
- Sıklık: tur başına en çok 1 fikir; günde en çok 6 (Enes 24.11 16:41: "sınırı dört yapma altı yap"); aynı anda en çok 3 cevapsız fikir (fazlası defterde 'oneri' bekler). Zayıf fikirle kota doldurulmaz; fikir yoksa hiçbir şey gönderilmez.
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
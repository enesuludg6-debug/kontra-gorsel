# Temel analiz 18:00 (her ABD işlem günü; kesin kural 37 + 34)
Skill: enes-portfoy-analiz (çelişkide invest/skills/enes-portfoy-analiz.md kopyası geçerli; bölüm 1 bu görevin tam yöntemi). Teknik analiz YOK.
Sıra: (1) haber/8-K/Form 4/analist revizyonu taraması (7 portföy + ilgi listesi kısa) → (2) en az 2 karne (önce eksikler RKLB SITM AXON CBRS VRT, sonra 7 günden eski) → (3) tez kartı kontrolü (tez_kartlari.md; yoksa portföy hissesi için oluştur) → (4) değerleme bölgeleri (kendi 3 yıllık bandı + akran + ters DCF, ucuz/adil/pahalı fiyat aralığı, 2 kaynak) → (5) her hisse için KARAR (temel) satırı → (6) 2-3 yeni aday (`python3 invest/periyot.py etiket kontrol aday <T> 5`, kullanınca `etiket yap aday <T>`), tam karne + tez + değerleme + KARAR → (7) adaylar vs en zayıf 2 portföy hissesi kıyası → (8) özet tablo.
Mesajlar Enes'e SendUserMessage, hisse başına kısa; sade dil, deyim yok; al/sat tavsiyesi değil "ben olsam".
Kayıt: temel_karne.md, tez_kartlari.md, DONGU `- SS:DD TEMEL: ...`, her karne için `periyot.py yap karne <hisse>`, push.
Zaman kutusu (kural 36d): 60 dk içinde YAYIN görevi varsa yayından 15 dk önce bitir; kalan kısım DURUM.md 'Bekleyen kararlar'a.

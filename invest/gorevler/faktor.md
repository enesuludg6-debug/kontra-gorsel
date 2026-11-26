# Faktör panosu Cum 16:10 (kural 93; Enes 26.11 08:55 'bunlar da tamam, bunları da ekle')
VERİ: Veri Yahoo (otomatik). Ana mesaj: piyasayı kim taşıyor (eşit ağırlık vs S&P = genişlik; momentum çöküşü = lider değişimi).

ADIMLAR: (1) veri -> `python3 invest/veri_icerik2.py faktor` özet. (2) Tweet KISA: ilk satır ≤12 kelime net olgu; en çok 2 paragraf, en çok 3 farklı rakam; kural 65 ikinci katman (başka nabız verisiyle uyum/ayrışma) + kural 89 tek fon yöneticisi cümlesi; 89-B çeşitlilik. Teknik terimi bir kez Türkçe açıkla (ör. 'SKEW, derin düşüşe karşı opsiyon talebi'). (3) Kart `python3 invest/veri_icerik2.py faktor --kart g/YYYYMMDD_HHMM_faktor.jpg` -> yayinla_gorsel.sh -> Buffer shareNow; tür VERI-FAKTOR. (4) yasak.py, kalite.py kontrol --tur VERI-FAKTOR --kalip X, gorus.py kontrol; kayit.py, kalite/gorus kaydet, commit/push.
Veri yoksa / değişim anlamsızsa TWEET YOK, DONGU'ya yaz. Al/sat, hedef, emoji, hashtag, link, soru yok.

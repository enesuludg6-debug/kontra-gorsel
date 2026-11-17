# Sabah kontrolü 09:00 (her gün)
(a) ZİNCİRLER: list_triggers (enabled true) ile bu sohbetteki "Otomatik paylaşım turu" ve 14 "Sabit: ..." zincirinin (python3 invest/sonraki.py hepsi listesi) her birinin bekleyen görevi var mı bak. Eksik olanı `python3 invest/sonraki.py <anahtar>` çıktısıyla HEMEN kur ve Enes'e "X zinciri kopmuştu, kurdum" de. Otomatik tur zinciri yoksa (kural 42: pencere 11:00-02:00) 11:00'a 'Otomatik paylaşım turu' kur (ilk tur 11:00 günün başlıkları görevinden 15 dk sonra, 11:15); 09:05 vadeli tweeti YOK, vadeliler 11:00 günün başlıklarında. [eski: 09:05 vadeli turunu çalıştır ve zinciri kısa şablonla kur.
(b) PERFORMANS (kural 26): Buffer list_posts includeMetrics (dün ve önceki gün, sonucu dosyaya yaz, python ile işle) → performans_veri.csv metrik sütunlarını doldur (12+ saati dolanlar), performans.md; `python3 invest/ders_analiz.py --gun 7` → DERSLER.md "Gözlemler"e 1-2 gözlem.
(c) TAKVİM: bugün ABD tatili/yarım gün mü (kural 37: teknik kontrol yok); takvim.md bugün/yarın eksik saat/beklenti varsa doldur.
(d) DONGU'ya "- 09:0x (GG.AA) SABAH KONTROLÜ: zincirler N/15, performans ..., takvim ..." + DURUM.md "Bugün / yarın", push. Sorun yoksa Enes'e tek satır "Sabah kontrolü: her şey yolunda".
(e) GÜNE ÖZEL BLOK (kural 36b): DURUM.md'de başlık tarihi bugünden eski "BUGÜNLÜK KURAL" bloğu varsa sil, DONGU'ya "bugünlük kural süresi doldu (GG.AA)" yaz.
(f) KART/TA-FARK: dünkü DONGU'da TA-FARK ya da kart hatası varsa DERSLER 'Gözlemler'e ekle.
(g) KURAL 42: bu görev tweet atmaz. Tur zincirini 11:15'e kur; günlük hedef Pzt-Cmt 30-40 (Pazar üst 40).

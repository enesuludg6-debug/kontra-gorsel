# Sabah kontrolü 09:00 (her gün)
(a) ZİNCİRLER: list_triggers (enabled true) ile bu sohbetteki "Otomatik paylaşım turu" ve 14 "Sabit: ..." zincirinin (python3 invest/sonraki.py hepsi listesi) her birinin bekleyen görevi var mı bak. Eksik olanı `python3 invest/sonraki.py <anahtar>` çıktısıyla HEMEN kur ve Enes'e "X zinciri kopmuştu, kurdum" de. Otomatik tur zinciri yoksa (09:00-01:00) enes-tweet-turu ile 09:05 vadeli turunu çalıştır ve zinciri kısa şablonla kur.
(b) PERFORMANS (kural 26): Buffer list_posts includeMetrics (dün ve önceki gün, sonucu dosyaya yaz, python ile işle) → performans_veri.csv metrik sütunlarını doldur (12+ saati dolanlar), performans.md; `python3 invest/ders_analiz.py --gun 7` → DERSLER.md "Gözlemler"e 1-2 gözlem.
(c) TAKVİM: bugün ABD tatili/yarım gün mü (yarım günse 20:30'a tek seferlik teknik kontrol kur); takvim.md bugün/yarın eksik saat/beklenti varsa doldur.
(d) DONGU'ya "- 09:0x (GG.AA) SABAH KONTROLÜ: zincirler N/15, performans ..., takvim ..." + DURUM.md "Bugün / yarın", push. Sorun yoksa Enes'e tek satır "Sabah kontrolü: her şey yolunda".
(e) GÜNE ÖZEL BLOK (kural 36b): DURUM.md'de başlık tarihi bugünden eski "BUGÜNLÜK KURAL" bloğu varsa sil, DONGU'ya "bugünlük kural süresi doldu (GG.AA)" yaz.
(f) KART/TA-FARK: dünkü DONGU'da TA-FARK ya da kart hatası varsa DERSLER 'Gözlemler'e ekle.

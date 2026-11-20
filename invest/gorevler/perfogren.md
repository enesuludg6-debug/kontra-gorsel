# Performans öğrenme 10:15 (her gün, kural 57 — Enes 20.11 09:08)
Amaç: gösterimlerden öğrenip içerik karışımını, saatleri ve yazım biçimini SÜREKLİ ayarlamak. Bu görev tweet atmaz.
1. Buffer list_posts: organizationId 6af5719777bce44fa736607b, channelIds ["6af99a1aece6dfde5fd109c7"], status ["sent"], includeMetrics true, first 100, dueAt start = 3 gün önce 00:00 TSİ, end = dün 23:59 TSİ. Çıktı büyükse araç /tmp/claude-tool-results/... dosyasına kaydeder; o yolu kullan (gerekirse after ile 2. sayfa).
2. `python3 invest/perf_isle.py <dosya(lar)>` → performans_veri.csv güncellenir (Buffer metrikleri ~12-24 saat gecikmeli; olgunlaşmamışlar atlanır, 'SONRAKI OLCUM' satırı çıkar).
3. `python3 invest/perf_isle.py --ozet --gun 7` ve `python3 invest/ders_analiz.py --gun 14` çalıştır.
4. Öğren ve AYARLA:
   - DERSLER.md 'Gözlemler'e tarihli 1-3 gözlem (ör. "21-24 medyan 416 vs 15-18 322"; "Enes'in kısa elle tweetleri med 472, sistem 327").
   - ders_analiz eşiği geçen (>=8 tweet, 2 hafta, %25 fark, tutarlı) her bulgu → DERSLER.md 'AKTİF DERSLER'e D-xxx olarak ekle ve DURUM.md 'İÇERİK AYARI (kural 57)' bloğunu güncelle. Enes onaylı bir dersin yerine geçecekse Enes'e sor.
   - Eşik geçmeyen ama 3 gün üst üste aynı yönde görülen gözlemi 'İÇERİK AYARI' bloğunda "DENE:" satırı olarak yaz (turlar uygular; ör. "görüşlü analizleri 21-01 arasına kaydır", "13F günde en çok 1", "ilk cümle kısa ve iddialı").
   - DENE satırı 7 gün sonra ölçülür: işe yaradıysa kalır, yaramadıysa silinir (sonucu Gözlemler'e yaz).
5. Enes'e TEK kısa mesaj: dünün toplam gösterimi / medyan, en iyi 2 tweet, bugün neyi değiştirdiğin (1-2 satır).
6. DONGU '- PERF-OGREN GG.AA: ...' + push. Zincir: bu görev sabit zincirdir (sonraki.py perfogren); her çalışmada İLK İŞ sonrakini kurar; aynı adlı bekleyen varsa kurmaz. Sabah kontrolü 09:00 eksikse kurar.

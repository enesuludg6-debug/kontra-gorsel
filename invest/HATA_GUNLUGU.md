# HATA GÜNLÜĞÜ (kesin kural 21) — atılmış tweetlerdeki hatalar ve düzeltmeler

| Tarih | Tweet (saat, konu, Buffer id) | Hata | Doğrusu | Sebep | Düzeltme tweeti | Önlem |
|---|---|---|---|---|---|---|
| 17.11 | 09:38 Berkshire 13F, 10:13 Ackman 13F | "Benim okumam:" etiketli görüş girişi (yasak kalıp) | etiketsiz görüş | yasak listede "Benim görüşüm:" vardı, "okumam" türevi yoktu | yok (stil hatası) | kesin kural 11, yasak liste genişletildi |
| 17.11 | 09:38-11:41 13F kartları | logolar 0.62 küçültüldü | LOGO_BUYUT 1.8, küçültme yok | taşmayı küçültmeyle çözdüm | yok | taşarsa düzen değiştir (bilanço = uclu) |
| 17.11 | 13:16 key levels (6afc2993) | "Takvim (TSİ):" etiketli satır | etiketsiz başlık satırı | kural 11 satır kontrolünü yapmadım | yok (stil) | göndermeden önce satır başı "kelime + iki nokta" taraması zorunlu |
| 17.11 | 14:07 HD rakam (yayından önce yakalandı) | GAAP 3,72 kartta "Düzeltilmiş" etiketiyle | GAAP etiketi | hazır kartta etiket sabitti | gerekmedi | hazır kart etiketleri parametre; GAAP/düzeltilmiş ayrımı bültenden kontrol |
| 17.11 | 14:44 DIS rakam | 14 dk geç (bülten 6:30 ET, hazırlık 6:40 varsaymıştı) | 6:30 ET | açıklama saatini önceki çeyreğin dakikasından doğrulamadım | yok | takvim saati önceki 2 çeyreğin bülten zaman damgasıyla doğrulanır; yayın turu T-5 dk başlar |
| 17.11 | 14:44 DIS kart (yayından önce) | kaynak satırı "Disney bülteni" ama rakamlar haber sitelerinden | Variety, Deadline, THR | şablon kaynak satırı sabitti | gerekmedi | kaynak satırı her zaman gerçekte okunan kaynaklar |
| 17.11 | 16:31 perakende (6afc5731) | yalnız rakam, yorum yok (Fed, büyük resim, piyasa etkisi eksik) | kural 25 beş soru | sablon 7 "tek cümle görüş" diyordu | 17:35 turu yorum tweeti | kural 25, sablon 7 yeniden yazıldı |
| 17.11 | 16:31 perakende Enes notu | "Fed'in faiz indirimi acelesi azalır" | piyasa Aralık ARTIRIMI konuşuyor | Fed beklentisini o gün kontrol etmedim | Enes'e düzeltme mesajı | makro tweet/notta Fed fiyatlaması o an 2 kaynakla kontrol |
| 17.11 | 21:07 NVDA öncesi bağlam (6afc97e0) | 3. paragraf "Bu gecenin önemi şu:" ile başladı (etiketli giriş türevi) | düz cümle | göndermeden önce satır tarandı ama paragraf içi iki nokta kalıbı kaçtı | yok (stil) | tarama: paragraf başı ilk 6 kelimede iki nokta varsa yeniden yaz |
| 18.11 | 14:47 TGT analiz (6afd9046) | 'Benim görüşüm:', 'Not:', 'Rakamlar:', 'İzlenecekler net:' etiketli girişler (Enes 14:55 uyardı) | düz cümle | kural metinde vardı, uzun yazıda tarama yapılmadı | yok (stil) | kural 11-B: invest/yasak.py her tweetten önce zorunlu |
- 18.11 23:35 (B): logo/<T>.png olusturmadan once `git ls-files logo/<T>.png` ile var mi bak; CBRS logosu ustune yazildi, geri alindi. uclu() koyu (siyah) logolari cizmiyor/gorunmuyor -> koyu logolu hisselerde editoryal/dortlu sec ya da beyaz plakayla elle yapistir (PIL). kart2.uclu'ya plaka eklemek denendi, _logo None dondugu icin ise yaramadi; ileride K.logo koyu kontrolu incelenmeli.

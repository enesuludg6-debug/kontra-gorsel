# Kalabalık endeksi Cumartesi 18:10 (kural 97; Enes 27.11 12:09 'yap')
Takipçi önerisi (SentimenTrader 'akıllı/aptal para güveni') ücretli olduğu için KULLANILMAZ; verisi, grafiği ya da linki tweete girmez. Yerine kendi ölçeğimiz: `invest/kalabalik.py`.
1. Önce verileri tazele: CNN korku (korku.py ekle), AAII (aaii.py ekle; Perşembe yayınlanır), CBOE put/call (nabiz.py kaydet; cboe.com/us/options/market_statistics/daily/ WebFetch). Eskiyse kart üstünde tarih görünür; 7 günden eski bileşen varsa tweet atma, DONGU'ya yaz.
2. `python3 invest/kalabalik.py hesap` (alt_veri/kalabalik.csv'ye ekler) -> iki ölçü + fark + okuma.
3. Tweet KISA (kural 86): ilk satır ≤12 kelime, bireysel iyimserlik ve kurumsal sakinlik değeri (en çok 3 farklı rakam), geçen haftayla kıyas (kalabalik.csv), tek fon yöneticisi cümlesi (karşıt okuma, tek başına sinyal değil). 'Kendi ölçeğim' ifadesi geçer. Kalıp B/C/F, tür VERI-KALABALIK.
4. Kart: `cd invest && python3 kalabalik.py kart g/YYYYMMDD_1810_kalabalik.jpg` -> yayinla_gorsel.sh -> Buffer (kural 95: önceki sistem tweetinden en az 35 dk; gerekirse customScheduled).
5. Kayıt: kayit.py --tur VERI-KALABALIK --kaynak sistem, kalite kaydet, commit/push, Enes'e 'Paylaşıldı + Ne anlama geliyor?'.
Okuma eşikleri kalabalik.py içinde: fark ≥ +25 dip davranışı, ≤ −25 tepe riski, ikisi de <30 gerçek stres, ikisi de >70 rehavet.

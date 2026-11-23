# AKTİF HESAP KİLİDİ (kesin kural 17)

AKTIF: C

Etiketler:
- A = Enes'in kendi Claude hesabı (enesuludg6). 17.11.2026'dan beri aktif.
- B = arkadaşının Claude hesabı (Enes'in hakkı bitince kullanılır).
- C = yeni Claude hesabı (23.11.2026'dan beri).

Kural: her tur/görev/yayın en başta bu dosyayı okur. Kendi mesajındaki `HESAP=<etiket>` buradaki `AKTIF:` ile aynı değilse hiçbir şey yapmaz (tweet yok, push yok) ve kendi tekrarlayan görevlerini devre dışı bırakır.
Hesap değiştirirken yeni hesap bu satırı kendi etiketine çevirir, commit + push eder, SONRA görev kurar. Geri dönerken aynısı ters yönde.

Geçmiş:
- 17.11.2026 13:15 dosya oluşturuldu, AKTIF: A.
- 18.11.2026 01:21 A2 devraldı (sohbet devri).
- 18.11.2026 20:26 B devraldı (hesap devri).
- 20.11.2026 14:49 B2 devraldı (sohbet devri).
- 21.11.2026 18:31 Enes 'durdur' dedi: B2 durduruldu (kilit DURDU). B2'nin bütün görevleri kendini kapatır. Yeni hesap (C) devri kilidi C yapar.
- 23.11.2026 20:02 C devraldı (hesap devri; Enes onayı).

---
name: enes-seri
description: Enes'in X hesabında okuru takipçiye çeviren numaralı tekrar eden seriler (Portföy Dosyası #n, Akşam Sözlüğü #n, Haftanın Grafiği #n) hazırlanırken ve seri numarası takip edilirken kullanılır (kural 88).
---
# Numaralı seriler (kural 88)

Neden: tek tweet beğeni alır, seri takip ettirir. Okur "#4'ü kaçırmayayım" diye hesabı takip eder. Seriler kural 86'daki günlük sayının içindedir, ek tweet değildir.

## Seriler
| Seri | Ne zaman | Kaynak tür | Kart |
|---|---|---|---|
| Portföy Dosyası #n | hafta içi her gün 1 (86-c'nin biri), 20-23 | PORTFOY | kart3 `dosya` / `dosya_video` |
| Akşam Sözlüğü #n | hafta içi her gün (86-d eğitici tweet) | EGITICI | `haber_dosya` / `cizgi_pro`, kicker "NEDİR? • #n" |
| Haftanın Grafiği #n | Pazar 13:00 civarı, 1 | BAGLAM-GORUS | `cizgi_pro` ya da `esleme`, en çok konuşulan grafik |
| Tutan Yorumlarım #n | Cumartesi 20:25 (karne) | KARNE | `siralama` |

## Kurallar
- Seri adı ve numarası tweetin İLK satırında değil, kartın kicker'ında ve tweetin son satırında küçük: "Portföy Dosyası #7". İlk satır yine enes-ilk-satir kuralıyla Enes sesinde.
- Numara `invest/seriler.json` dosyasından okunur ve tweet atıldıktan sonra 1 artırılır (`python3 invest/seri.py al <seri>` / `python3 invest/seri.py artir <seri>`).
- Aynı hisse Portföy Dosyası'nda 10 gün içinde tekrar edilmez; Akşam Sözlüğü'nde aynı kavram 30 gün içinde tekrar edilmez.
- Seri tweeti kaçarsa telafi atılmaz, numara atlamaz.
- "Seri", "takip edin", "kaçırmayın" gibi çağrı yazılmaz; numara yeterli.

## Ölçüm
- performans_veri.csv `konu` alanına `[S:seri#n]` etiketi. 2 hafta sonra seri tweetlerinin beğeni ortalaması seri dışı aynı türle kıyaslanır, sonuç DERSLER.md'ye.

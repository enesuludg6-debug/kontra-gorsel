---
name: enes-fon-yoneticisi-dili
description: Enes'in X hesabındaki her tweet bir hedge fon yöneticisinin üslubu ve profesyonelliğiyle (fiyatlanan ne, asimetri, katalizör, pozisyonlanma, risk) yazılırken kullanılır (kural 89).
---
# Hedge fon yöneticisi üslubu (kural 89)

Enes 25.11.2026 18:31: "Sanki bir hedge fund yöneticisi tweet atıyormuş gibi; o üslubu ve profesyonelliği istiyorum."

Okur tweeti bitirince şunu düşünmeli: "Bu adam haberi değil, haberin fiyata ne yaptığını düşünüyor." Fon yöneticisi olayı anlatmaz; olayın **fiyatlanmış beklentiyle farkını**, **riskin hangi tarafta olduğunu** ve **neyin fikrini değiştireceğini** söyler.

## 1. Düşünme sırası (her tweette en az 3'ü görünür)
1. **Fiyatlanan ne?** Piyasa şu an neyi varsayıyor: konsensüs beklenti, vadeli/FedWatch olasılığı, çarpan, opsiyonun ima ettiği hareket.
2. **Fark nerede?** Benim görüşüm konsensüsten hangi noktada ayrılıyor (tek cümle, rakamla).
3. **Asimetri:** Aşağı ve yukarı senaryo kabaca ne kadar (yüzde değil, "aşağı risk sınırlı / yukarı alan geniş" gibi düz söyle; rakam varsa kaynaklı).
4. **Katalizör ve tarih:** Bunu ne çözer, ne zaman (bilanço, veri, karar, vade).
5. **Pozisyonlanma:** Kalabalık hangi tarafta (açığa satış oranı, fon akışı, CFTC, opsiyon yerleşimi, analist dağılımı).
6. **Fikrimi değiştiren şey:** Tezi bozan tek gösterge ve eşiği ("X %16 altına inerse görüşümü değiştiririm").

## 2. Üslup
- Sakin, kısa, kesin. Heyecan yok, ünlem yok, "inanılmaz", "çılgın", "bomba", "uçtu", "çöktü" yok; "sert düştü", "yüzde 11 geriledi".
- Birinci tekil, ölçülü özgüven: "Bence", "benim okumam", "burada riski aşağı yönde görüyorum". Kesinlik yok: "kesin", "garanti", "kaçınılmaz".
- Olasılık dili: "daha olası", "zayıf ihtimal", "piyasa yüzde 60 fiyatlıyor". Tahmin yerine senaryo.
- Haberi tekrar etme; haberin **ikinci derece etkisine** geç (kimin geliri, kimin maliyeti, kimin bilançosu).
- Jargon Türkçe ve anlaşılır: "fiyatlanmış", "beklenti farkı", "risk/getiri dengesi", "katalizör", "pozisyonlanma", "kalabalık işlem", "aşağı yönlü risk". Ham İngilizce terim yok (kural 63).
- Rakam az ama yerinde (kural 86: en çok 3 farklı rakam); her rakam bir karar sorusuna hizmet eder.
- Son cümle izlenecek eşik ya da tarih olur, nasihat değil.

## 3. Kesin sınırlar (fon yöneticisi gibi yazmak, fon yöneticisi gibi davranmak DEĞİL)
- Al/sat tavsiyesi, emir kipi ("alın", "satın", "kaçırmayın"), hedef fiyat, pozisyon büyüklüğü, portföy tutarı, getiri yüzdesi, işlem bildirimi ("aldım/sattım") YOK.
- "Fonumuz", "yatırımcılarımız", "pozisyonumuz" gibi Enes'i fon yöneticisi gibi gösteren ifade YOK; yalnız üslup.
- "Kurumsal para", "akıllı para" gibi kaynaksız genellemeler YOK; akış iddiası varsa veri ve kaynak.
- 54-F ve ilk satır kuralları geçerli (dramatik/soyut kalıp yok, ilk satır en çok 12 kelime).

## 4. Örnek dönüşüm
- Önce: "CoreWeave bugün %11 düştü, yatırımcılar borç endişesi yaşıyor."
- Sonra: "CoreWeave'de hisse, tahvilin söylediğini yeni fiyatlıyor. 2031 tahvili yüzde 16 getiriyle işlem görüyor; borç verenler şirketi hissedardan daha riskli buluyor. Bence aşağı yönlü risk hisse fiyatında henüz tam değil. Görüşümü değiştirecek tek gösterge tahvil getirisinin yüzde 16 altına inmesi."
- Önce: "PCE beklentinin üstünde geldi, piyasalar düştü."
- Sonra: "Çekirdek PCE yüzde 3,3 ile beklentinin 0,1 puan üstünde. Vadeli işlemler Aralık artırımını zaten fiyatlıyordu; değişen tek kalem Ocak. Benim okumam: veri sürprizi faizden çok büyüme hisselerinin çarpanına gidiyor."


## 5. Kontrol
- Yazdıktan sonra sor: (1) fiyatlanan ne yazıldı mı, (2) farkım net mi, (3) fikrimi değiştiren eşik var mı. Üçünden biri eksikse yeniden yaz.
- `python3 invest/yasak.py` ve `python3 invest/kalite.py kontrol` (kural 89 uyarısı: fiyatlama/beklenti/olasılık/eşik dili yoksa).

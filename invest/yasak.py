#!/usr/bin/env python3
# YASAK KALIP TARAMASI (kesin kural 11; Enes 18.11 14:55: "benim görüşüm: ifadesini kullanmayacaksın, yasaklanmıştı").
# HER Buffer create_post'TAN ÖNCE ZORUNLU. Kullanım: python3 invest/yasak.py <<'EOF'
# <tweet metni>
# EOF
# Çıkış 0 = temiz, 1 = yasak var -> metni düzelt, tekrar tara, temizse at.
import re, sys

t = sys.stdin.read()
low = t.lower()
hata = []

KALIP = ["benim okumam", "benim görüşüm", "görüşüm:", "yorumum", "bence önemli nokta şu", "asıl ilginci", "asıl ilginç", "asıl önemli", "bence ilginç olan", "ilginç olan şu",
         "burada kritik olan", "işin özü", "önemli nokta:", "sonuç olarak", "özetle", "kısaca", "bir de şu var",
         "kısa bir flood", "bu bence çok şey anlatıyor", "mesaj net", "dikkat çekiyor", "öne çıkıyor",
         "önemli bir gelişme", "nabız", "mercek altında", "gözler ", "ayrıca", "bununla birlikte",
         "risk tarafı da var", "yön net", "tablo net", "resim net", "durum net", "mesele şu", "sebep şu", "fark şu", "yine de yön", "peki ne anlama geliyor", "ters köşe", "asıl sınav", "kapı açılır", "okuyorum", "okumam", "okuması", "okunuşu", "okunuş", "olarak okumak", "olarak okunmalı", "şöyle oku", "böyle oku", "okumak gerek", "okumak lazım", "diye okuyorum", "okuyabiliriz", "hafife almıyorum", "hafife almamak", "hafife alınmamalı", "hafife alma", "göz ardı etmiyorum", "göz ardı etmemek", "göz ardı edilmemeli", "küçümsememek", "küçümsemiyorum", "küçümsenmemeli", "abartılı buluyorum ama", "ama riski de", "riski de var", "iki tarafı da var", "madalyonun", "bir yandan", "öte yandan", "her ne kadar", "şunu da belirtmek", "altını çizmek", "unutmamak gerek", "unutmamak lazım", "panik yapmıyorum", "panik yapmayın", "panik yapmamak", "panik yok", "paniğe gerek yok", "panikle satmıyorum", "sakin kalıyorum", "sakin kalmak", "soğukkanlı", "soğukkanlılık", "sabırlı olmak gerek", "sabırlı kalıyorum", "duygusal davranmıyorum", "duygusal davranmamak", "gürültüye kulak", "büyük resme bak", "büyük resim", "uzun vadeli düşünüyorum", "gördüğüm şey", "bu tabloda gördüğüm", "bu tabloda", "tablonun özeti", "kapıya koş", "çıkışa koş", "kapıya yığıl", "topluca kaç", "sürü psikolojisi", "sürü halinde", "korku satışı", "bıçak düşerken", "düşen bıçak", "fırtına", "deprem", "kan kaybı", "kan banyosu", "kıyamet", "tsunami", "kartopu", "domino etkisi", "kapı aralanıyor", "perde arkası", "asıl hikâye", "asıl hikaye", "hikâyenin özü", "işin özü şu", "resmin tamamı", "bakacağım tek", "ilk bakacağım satır", "bakacağım satır", "izlenecek tek kalem", "izlenecek kalem", "bakılacak tek kalem", "bakılacak tek rakam", "takip edilecek tek", "başka bir şey söylüyor", "başka bir şey anlatıyor", "başka bir hikâye", "başka bir hikaye", "manşet ", "manşetler ", "rakamlar başka", "veri başka", "tablo başka", "aslında başka", "farklı bir şey söylüyor", "sessizce", "fısıldıyor", "bağırıyor", "itiraf ediyor", "stres geçmiş", "stres bitmiş", "stres sürüyor", "stres hâlâ", "stres hala", "geçmiş değil", "bitmiş değil", "panik bitti", "panik geçti", "korku geçti", "korku bitti", "rahatlama geldi", "nefes aldı", "derin bir nefes"]  # 54-D devamı (Enes 22:07 "stres geçmiş değil, bu da çok ai")  # Kural 54-D (Enes 23.11 22:06): veriye/manşete konuşma yükleyen YZ kalıpları  # Kural 64 (Enes 23.11 21:31): kalıplaşmış analist cümlesi yerine konuşma dili
for k in KALIP:
    if k in low:
        hata.append(f"yasak kalıp: '{k}'")

# Paragraf ya da satır başında etiket: ilk 8 kelimede iki nokta (madde işaretli rakam satırları hariç)
for p in re.split(r"\n+", t):
    s = p.strip()
    if not s or s.startswith(("•", "-", "$")):
        continue
    ilk = " ".join(s.split()[:8])
    if ":" in ilk and not re.search(r"\d:\d", ilk):
        hata.append(f"etiketli giriş (ilk 8 kelimede ':'): '{ilk}'")

# Her cümlenin başı: ilk 6 kelimede iki nokta (Enes 18.11 17:26: "Yine de yön net:" vb. ara cümle etiketi yasak)
for c in re.split(r"(?<=[.!?;])\s+|\n+", t):
    c = c.strip()
    if not c or c.startswith(("•", "-", "$")):
        continue
    ilk = " ".join(c.split()[:6])
    if ":" in ilk and not re.search(r"\d:\d", ilk):
        hata.append(f"cümle başında etiket (':'): '{ilk}'")


# Kural 54-F (Enes 25.11 17:19: "'Asıl sürpriz büyümede.', 'masadaki soru' vb ifadeler kullanma, çok ai gibi"):
# dramatik çerçeve/vurgu kalıpları. Olgu düz cümleyle, rakamla söylenir.
for r_, ad in [
    (r"\basıl (sürpriz|soru|mesele|haber|risk|cevap|konu|fark|olay|sorun|nokta|kazanan|kaybeden|test|hamle|tehlike|neden)", "'asıl X' vurgu kalıbı"),
    (r"masadaki (soru|seçenek|konu|ihtimal)", "'masadaki soru' kalıbı"),
    (r"(soru|tartışma) artık|artık tartışma konusu değil|tartışma konusu bile değil", "'soru artık / tartışma konusu değil' kalıbı"),
    (r"işin içi başka|işin rengi|işin aslı", "'işin içi başka' kalıbı"),
    (r"(bugünün|günün|haftanın) (ikinci |asıl |en )?büyük (riski|sorusu|sürprizi)", "'günün büyük riski/sürprizi' kalıbı"),
    (r"tablo .{0,25}(sertleşti|netleşti|değişti|karardı|aydınlandı)", "'tablo sertleşti/netleşti' kalıbı"),
    (r"\bbedeli \w+(da|de|ta|te)\b|bedeli ağır|faturası", "'bedeli X'te' kalıbı"),
    (r"artık \w+(da|de|ta|te) değil, \w+(da|de|ta|te)", "'artık X'te değil, Y'de' karşıtlık kalıbı"),
    (r"\b(rakamlarda|fiyatta|manşette|sayılarda) değil\b", "'cevap rakamlarda değil' karşıtlık kalıbı"),
    (r"manşet,|manşet\.|manşet ama", "'manşet' çerçeve kalıbı"),
    (r"zincir basit|denklem basit|hesap basit|mantık basit", "'zincir basit' kalıbı"),
    (r"oyunun kuralı|oyun değiştir|kartlar yeniden", "oyun/kart mecazı"),
]:
    if re.search(r_, low):
        hata.append("54-F: " + ad)

# Kural 54-E (Enes 24.11 09:10: "'Nakit tarafı da güçlü.' çok yapay zekâ ibaresi gibi duruyor, böyle şeyler kullanmasın"):
# rakamsız "X tarafı/cephesi (da) güçlü/zayıf/sağlam..." hüküm cümleleri ve rakamsız kısa sıfat-hüküm cümleleri yasak.
SIFAT = r"(güçlü|zayıf|sağlam|temiz|olumlu|olumsuz|iyi|kötü|parlak|sağlıklı|net|rahat|sorunlu|cılız|kuvvetli|istikrarlı|dengeli|sıkıntılı)"
if re.search(r"\b(taraf[ıi]|tarafında|cephe(si|sinde)|kanad[ıi]|ayağ[ıi])\s+(da|de)\b", low):
    hata.append("54-E: 'X tarafı da / cephesinde de' kalıbı")
if re.search(r"\b(taraf[ıi]|cephesi|kanad[ıi]|ayağ[ıi])\s+(da\s+|de\s+)?(çok\s+|oldukça\s+|gayet\s+)?" + SIFAT + r"\b", low):
    hata.append("54-E: 'X tarafı güçlü/zayıf' hüküm kalıbı")
for c in re.split(r"(?<=[.!?;])\s+|\n+", t):
    c2 = c.strip().lower().rstrip(".!;")
    if c2 and not re.search(r"\d", c2) and len(c2.split()) <= 5 and re.search(r"\b(de|da)\s+(çok\s+|oldukça\s+|gayet\s+)?" + SIFAT + r"(\s*(görünüyor|duruyor|kalıyor))?$", c2):
        hata.append(f"54-E: rakamsız kısa hüküm cümlesi: '{c.strip()}'")

if re.search(r"#\w", t): hata.append("hashtag")
if re.search(r"https?://", t): hata.append("link")
if re.search(r"[\U0001F300-\U0001FAFF\u2600-\u27BF]", t): hata.append("emoji")
if t.rstrip().endswith("?"): hata.append("soruyla bitiyor")
if re.search(r"\b(alın|satın alın|hemen al|satmalı|almalı|satın)\b(?! al)", low): hata.append("al/sat dili")
if "anthropic" in low: hata.append("Anthropic adı")

if hata:
    print("YASAK VAR -> ATMA, düzelt:")
    for h in hata: print("  -", h)
    sys.exit(1)
print("TEMIZ")

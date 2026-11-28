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
    (r"\b(inanılmaz|çılgın|bomba gibi|uçtu|uçuşa geçti|çakıldı|roket gibi|kaçırmayın)\b", "89: heyecan/hype kelimesi (fon yöneticisi sakin yazar)"),
    (r"\b(fonumuz|fonumuzun|pozisyonumuz|yatırımcılarımız|müşterilerimiz)\b", "89: Enes'i fon yöneticisi gibi gösteren ifade (yalnız üslup)"),
    (r"akıllı para|kurumsal para (giriyor|çıkıyor|alıyor|satıyor)", "89: kaynaksız 'akıllı/kurumsal para' genellemesi"),
    (r"\b(bu|bugünkü|bugün|günün|haftanın|bu sabahki) (seans|satış|düşüş|yükseliş|hareket|tablo|gün|hafta|rally|ralli)\w* .{0,60}?(yansıması|ifadesi|göstergesi|fiyatlaması|sonucu|hikâyesi|hikayesi|testi)\b", "'bu seans X'in yansıması' soyut özet kalıbı"),
    (r"\w+(ın|in|un|ün|nın|nin|nun|nün) (hisselere|piyasaya|fiyatlara|borsaya|endekse) yansıması", "'X'in hisselere yansıması' kalıbı"),
    (r"büyüme hisselerinden genel bir kaçış|genel bir kaçış|risk iştahının (geri )?çekilmesi", "soyut 'genel kaçış' özeti"),
]:
    if re.search(r_, low):
        hata.append("54-F: " + ad)

# Kural 54-G (Enes 26.11 11:50: "'bunu talep sorunu saymam' çok ai gibi, bu ifadeleri kullanma"):
# hüküm yerine "saymam / olarak görmem / aynı gözle" sınıflandırma kalıpları ve "X değil, Y" karşıtlık hükümleri yasak.
# Görüş somut söylenir: hangi rakam, hangi seviye, ne olursa ne yaparım (ör. "1,03 milyonun altında kapanırsa satış derinleşir.").
for r_, ad in [
    (r"\b\w+ (sorunu|meselesi|krizi|sinyali|problemi|riski|zaafı)\s+(saymam|saymıyorum|sayılmaz|saymak için|olarak görmem|olarak görmüyorum)", "'bunu X sorunu saymam' sınıflandırma kalıbı"),
    (r"\b(saymam|saymıyorum|saymazdım|sayarım|sayıyorum)\b", "'saymam / sayarım' hüküm kalıbı"),
    (r"\bolarak (görmem|görmüyorum|görüyorum|görürüm|değerlendiririm|değerlendirmiyorum|okurum)\b", "'X olarak görmem/görüyorum' kalıbı"),
    (r"aynı gözle|bu gözle|o gözle", "'aynı gözle değerlendiririm' kalıbı"),
    (r"\b\w+(e|a|ye|ya) değil, \w+(e|a|ye|ya) bağlıyorum|\bbağlıyorum\b", "'X'e değil Y'ye bağlıyorum' kalıbı"),
    (r"fiyatlanan şey .{0,60}\bdeğil\b", "'fiyatlanan şey X değil, Y' karşıtlık kalıbı"),
    (r"kırılma noktam|benim eşiğim|benim çizgim", "'kırılma noktam' kişisel çerçeve kalıbı"),
]:
    if re.search(r_, low):
        hata.append("54-G: " + ad)


# KURAL 109 (Enes 28.11 11:49 "artık şirket isimlerini tweetlerde $TICKER şeklinde yazacaksın"): şirket adı yazılmaz, $TICKER yazılır.
SIRKET_TICKER = {
    "nvidia": "NVDA", "tesla": "TSLA", "apple": "AAPL", "microsoft": "MSFT", "alphabet": "GOOGL", "google": "GOOGL",
    "amazon": "AMZN", "meta": "META", "broadcom": "AVGO", "amd": "AMD", "marvell": "MRVL", "micron": "MU",
    "intel": "INTC", "tsmc": "TSM", "oracle": "ORCL", "netflix": "NFLX", "palantir": "PLTR", "nebius": "NBIS",
    "coreweave": "CRWV", "arm": "ARM", "qualcomm": "QCOM", "salesforce": "CRM", "adobe": "ADBE", "servicenow": "NOW",
    "snowflake": "SNOW", "crowdstrike": "CRWD", "cisco": "CSCO", "ibm": "IBM", "dell": "DELL", "supermicro": "SMCI",
    "super micro": "SMCI", "asml": "ASML", "applied materials": "AMAT", "lam research": "LRCX", "kla": "KLAC",
    "lumentum": "LITE", "coherent": "COHR", "astera": "ALAB", "vertiv": "VRT", "robinhood": "HOOD", "coinbase": "COIN",
    "uber": "UBER", "shopify": "SHOP", "spacex": "SPCX", "berkshire": "BRK.B", "jpmorgan": "JPM", "walmart": "WMT",
    "costco": "COST", "eli lilly": "LLY", "novo nordisk": "NVO", "applovin": "APP", "iren": "IREN", "oklo": "OKLO",
    "rocket lab": "RKLB", "sandisk": "SNDK", "western digital": "WDC", "seagate": "STX", "sk hynix": "SKHY",
}
_ek = r"(?:'?(?:nin|nın|nun|nün|in|ın|un|ün|a|e|ya|ye|da|de|ta|te|dan|den|tan|ten|ı|i|u|ü|yı|yi|yu|yü|la|le|yla|yle))?"
for ad_, tk_ in SIRKET_TICKER.items():
    m_ = re.search(r"(?<![\$\w])" + re.escape(ad_) + _ek + r"(?!\w)", low)
    if m_ and ("$" + tk_.lower()) not in low.replace(" ", "") or (m_ and ad_ in ("google", "alphabet") and "$goog" not in low):
        hata.append(f"109: şirket adı '{m_.group(0)}' yerine ${tk_} yaz (Türkçe ek kesme işaretiyle: ${tk_}'ın)")
    elif m_:
        hata.append(f"109: '{m_.group(0)}' ad olarak geçmesin; yalnız ${tk_} kullan")

# Kural 54-H (Enes 27.11 19:30: "'risk masada kalır.' böyle ibareler istemiyorum, çok yapay zekâ yazmış gibi"):
# süslü mecaz / kapanış vecizesi yasak. Kapanış düz ve ölçülebilir olur (ör. "Oran 1'in altına inene kadar temkinliyim.").
for r_, ad in [
    (r"\bmasa(da|ya|dan|nın|daki)\b", "'risk masada kalır / masaya geldi' mecazı"),
    (r"\bdenklem(i|in|de|e)?\b|\bterazi(si|de|nin)?\b|\bibre(si|yi|nin)?\b", "'denklem / terazi / ibre' mecazı"),
    (r"oyunun kural|kartlar(ı)? yeniden|top (artık )?\w+ (sahasında|elinde)|rüzgar(ı)? arka", "'oyunun kuralları / kartlar / top sahasında / rüzgar arkada' mecazı"),
    (r"\b(tablo|resim)(yu|u|yı|ı)? (boz|değiştir|netleş)|\bpusula|\bfırtına(nın)? (göz|öncesi)", "'tabloyu bozar / pusula / fırtına' mecazı"),
    (r"(kalabalık|piyasa|yatırımcı(lar)?|herkes)\w* (henüz |hâlâ |hala |daha )?(inanma|inanmıyor|ikna olma|ikna olmuş değil|kabullenme)", "'kalabalık henüz inanmadı' kişileştirme kalıbı (Enes 28.11 12:16 'çok AI gibi'); düz yaz: 'çoğu yatırımcı hâlâ korkuyor', 'korku endeksi hâlâ 25 altında'"),
    (r"ciddiye al(ıyorum|ırım|mak gerek|mak lazım|ınmalı)|\bbu yüzden ben\b", "'bu yüzden ben X'i ciddiye alıyorum' yapay kanaat kalıbı (Enes 28.11 11:46); kanaati düz söyle: 'kırılım geçerli', '390 altına dönmedikçe yukarı bakıyorum'"),
    (r"(perde|sahne)(si)? (aralan|kapan|açıl)|\bsahneye çık|\bsöz(ü)? (artık )?\w+(da|de)\b", "'perde aralandı / söz X'te' mecazı"),
]:
    if re.search(r_, low):
        hata.append("54-H: " + ad)

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

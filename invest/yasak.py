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
         "risk tarafı da var", "yön net", "tablo net", "resim net", "durum net", "mesele şu", "sebep şu", "fark şu", "yine de yön", "peki ne anlama geliyor", "ters köşe", "asıl sınav", "kapı açılır", "okuyorum", "okumam", "okuması", "okunuşu", "okunuş", "olarak okumak", "olarak okunmalı", "şöyle oku", "böyle oku", "okumak gerek", "okumak lazım", "diye okuyorum", "okuyabiliriz", "hafife almıyorum", "hafife almamak", "hafife alınmamalı", "hafife alma", "göz ardı etmiyorum", "göz ardı etmemek", "göz ardı edilmemeli", "küçümsememek", "küçümsemiyorum", "küçümsenmemeli", "abartılı buluyorum ama", "ama riski de", "riski de var", "iki tarafı da var", "madalyonun", "bir yandan", "öte yandan", "her ne kadar", "şunu da belirtmek", "altını çizmek", "unutmamak gerek", "unutmamak lazım"]
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

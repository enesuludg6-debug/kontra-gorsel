# Everpure (P) Q3 FY27 rakam karti. Kullanim: python3 hazir_P.py GELIR HBK BRUT_MARJ YIL_GELIR_ALT YIL_GELIR_UST
# Bulten: investor.everpuredata.com (press releases) + PR Newswire + SEC 8-K; ~4:05 PM ET = 00:05 TSI; gorusme 2:00 PM PT = 01:00 TSI
# Beklenti: gelir 1,33 Mr (EW + Investing + Arincen), HBK 0,77 (EW + Investing + Arincen), whisper 0,81 (EW); rehber gelir 1,325-1,335, faaliyet kari 265-275 Mn (Zacks + EW)
# Yil rehberi (onceki): gelir 5,03-5,07 Mr, faaliyet kari 940-960 Mn, FCF 600-800 Mn (EW + Zacks). Opsiyon ~%15-17.
import sys; sys.path.insert(0,'/home/claude/kontra-gorsel/invest'); import kart2
g,h,m,ya,yu=sys.argv[1:6]
kart2.uclu('$P','EVERPURE • MALİ 2027 3. ÇEYREK','Everpure 3. çeyrek bilançosu',[
 (f'{g} Mr $','Gelir / Beklenti: 1,33 Mr $'),
 (f'{h} $','Hisse başı kâr / Beklenti: 0,77 $'),
 (f'%{m}','Brüt marj (düzeltilmiş)')],
 'Everpure bülteni', '/home/claude/kontra-gorsel/invest/g/20261119_0005_p_rakam.jpg')
print('OK')
# TWEET ISKELETI:
# $P MALİ 2027 3. ÇEYREK BİLANÇOSU
# • Gelir: X Mr $ / Beklenti: 1,33 Mr $
# • Hisse başı kâr: X $ / Beklenti: 0,77 $
# • Düzeltilmiş faaliyet kârı: X Mn $ / Şirket rehberi: 265-275 Mn $
# • Brüt marj: %X
# 4. ÇEYREK TAHMİNİ: Gelir X
# 2027 MALİ YIL TAHMİNİ
# • Gelir: X Mr $ / Önceki: 5,03-5,07 Mr $
# • Serbest nakit akışı: X / Önceki: 600-800 Mn $

# PANW Q1 FY27 rakam karti. Kullanim: python3 hazir_PANW.py GELIR HBK NGSARR YIL_GELIR_ALT YIL_GELIR_UST
# Bulten: investors.paloaltonetworks.com/news-releases + PR Newswire (prnewswire.com/news/palo-alto-networks) + SEC 8-K (CIK 1327567)
# Beklenti: gelir 3,31 Mr (Zacks + EW + Finimize), HBK 0,97 (EW + Investing + ebc), rehber gelir 3,30-3,31 / HBK 0,96-0,98 / NGS ARR 9,54-9,56 / RPO 20,8-20,9 (IR + Zacks + BigGo)
# Yil rehberi (onceki): gelir 14,10-14,20 Mr, NGS ARR 11,075-11,175, HBK 4,16-4,19 (IR + BigGo + TradingKey)
import sys; sys.path.insert(0,'/home/claude/kontra-gorsel/invest'); import kart2
g,h,a,ya,yu=sys.argv[1:6]
kart2.uclu('$PANW','PANW • MALİ 2027 1. ÇEYREK','Palo Alto Networks 1. çeyrek bilançosu',[
 (f'{g} Mr $','Gelir / Beklenti: 3,31 Mr $'),
 (f'{h} $','Hisse başı kâr / Beklenti: 0,97 $'),
 (f'{a} Mr $','NGS ARR / Rehber: 9,54-9,56 Mr $')],
 'Palo Alto Networks bülteni', '/home/claude/kontra-gorsel/invest/g/20261119_0003_panw_rakam.jpg')
print('OK')
# TWEET ISKELETI (kural 7, CRWV formati):
# $PANW MALİ 2027 1. ÇEYREK BİLANÇOSU
# • Gelir: X Mr $ / Beklenti: 3,31 Mr $
# • Hisse başı kâr: X $ / Beklenti: 0,97 $
# • NGS ARR: X Mr $ / Şirket rehberi: 9,54-9,56 Mr $
# • Kalan sözleşme yükümlülüğü (RPO): X Mr $ / Şirket rehberi: 20,8-20,9 Mr $
#
# 2. ÇEYREK TAHMİNİ
# • Gelir: X / NGS ARR: X / Hisse başı kâr: X
# 2027 MALİ YIL TAHMİNİ
# • Gelir: X Mr $ / Önceki: 14,10-14,20 Mr $
# • NGS ARR: X Mr $ / Önceki: 11,075-11,175 Mr $

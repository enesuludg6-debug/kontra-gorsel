# Target Q3 2026 rakam karti. Kullanim: python3 /tmp/hazir_TGT.py GELIR HBK KARS(ayni magaza %) YIL_HBK_ALT YIL_HBK_UST
import sys; sys.path.insert(0,'/home/claude/kontra-gorsel/invest'); import kart2
g,h,k,a,u=sys.argv[1:6]
kart2.uclu('$TGT','TGT • 3. ÇEYREK','Target 3. çeyrek bilançosu',[
 (f'{g} Mr $','Gelir / Beklenti: 26,41-26,47 Mr $'),
 (f'{h} $','Hisse başı kâr (iade dahil) / Beklenti: 2,04-2,08 $'),
 (f'%{k}','Karşılaştırılabilir satış / Trafik +%5,0')],
 'Target bülteni', '/home/claude/kontra-gorsel/invest/g/20261118_1430_tgt_rakam.jpg')
print('OK')

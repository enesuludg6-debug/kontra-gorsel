#!/usr/bin/env python3
"""KURAL 111-T (Enes 28.11 20:29 'takipçi sayısını neden bulamadın, önüne geçecek düzenleme yap').
Takipçi defteri + patlama oranı. x.com'a giriş yok: takipçi sayısı WebSearch (allowed_domains x.com/twitter.com)
ile '<handle> followers' sorgusunun profil sonucundan okunur (snippet 'NNN.NK Followers' ya da JSON 'Follows' sayısı).
  python3 invest/takipci.py ekle <handle> <takipci> [kaynak]     ör. ekle LeopoldTracker_ 715.8K
  python3 invest/takipci.py oran <handle> <goruntulenme>          ör. oran MMMTwealth 40.2K  -> ORAN:0.62x DEĞİL
  python3 invest/takipci.py bak <handle>
  python3 invest/takipci.py liste
Kural: PATLAMA = görüntülenme >= 5 x takipçi VE >= 10.000. Defterde 30 günden eski kayıt yeniden aranır.
K111 tweeti kayit.py --konu içine 'K111 ORAN:<n>x' yazılır; gun_ozet yalnız ORAN>=5 olanları sayar.
"""
import sys, json, os, datetime as dt
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'alt_veri', 'takipci_defteri.json')
def sayi(s):
    s = str(s).strip().upper().replace(',', '.')
    k = 1
    if s.endswith('K'): k, s = 1e3, s[:-1]
    elif s.endswith('M'): k, s = 1e6, s[:-1]
    elif s.endswith('B'): k, s = 1e3, s[:-1]  # Türkçe 'B' = bin
    return int(float(s) * k)
def yukle():
    try: return json.load(open(D, encoding='utf-8'))
    except Exception: return {}
def kaydet(d):
    os.makedirs(os.path.dirname(D), exist_ok=True); json.dump(d, open(D, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
a = sys.argv[1:]
d = yukle()
if not a or a[0] == 'liste':
    for h, v in sorted(d.items()): print(f"{h:20s} {v['takipci']:>10,} {v['tarih']} {v.get('kaynak','')}")
elif a[0] == 'ekle':
    d[a[1].lstrip('@').lower()] = {'takipci': sayi(a[2]), 'tarih': dt.date.today().isoformat(), 'kaynak': ' '.join(a[3:]) or 'x.com profil (WebSearch)'}
    kaydet(d); print('EKLENDI', a[1], sayi(a[2]))
elif a[0] in ('bak', 'oran'):
    v = d.get(a[1].lstrip('@').lower())
    if not v: print(f'YOK: önce WebSearch "{a[1]} followers" (allowed_domains x.com) -> takipci.py ekle'); sys.exit(2)
    yas = (dt.date.today() - dt.date.fromisoformat(v['tarih'])).days
    if yas > 30: print(f'ESKİ ({yas} gün): yeniden ara')
    if a[0] == 'bak': print(v); sys.exit(0)
    g = sayi(a[2]); r = g / max(v['takipci'], 1)
    ok = r >= 5 and g >= 10000
    print(f"ORAN:{r:.2f}x {'PATLAMA' if ok else 'DEĞİL'} (görüntülenme {g:,} / takipçi {v['takipci']:,})")
    sys.exit(0 if ok else 1)

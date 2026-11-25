#!/usr/bin/env python3
"""Seri numarası (kural 88). python3 invest/seri.py al|artir|liste <seri>"""
import json, os, sys
F = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'seriler.json')
S = json.load(open(F, encoding='utf-8')) if os.path.exists(F) else {"Portföy Dosyası": 1, "Akşam Sözlüğü": 1, "Haftanın Grafiği": 1, "Tutan Yorumlarım": 1}
k, ad = (sys.argv[1] if len(sys.argv) > 1 else 'liste'), ' '.join(sys.argv[2:])
if k == 'al': print(f"{ad} #{S.get(ad, 1)}")
elif k == 'artir': S[ad] = S.get(ad, 1) + 1; print(f"{ad} sıradaki #{S[ad]}")
else: print(json.dumps(S, ensure_ascii=False))
json.dump(S, open(F, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

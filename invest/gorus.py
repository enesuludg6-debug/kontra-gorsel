#!/usr/bin/env python3
"""Kural 50-B: görüş paragrafında kalıp tekrarını engeller.
Kullanım:
  python3 invest/gorus.py kontrol < tweet.txt   -> son 12 tweetin görüş açılışı/kalıplarıyla çakışırsa çıkış 1
  python3 invest/gorus.py kaydet  < tweet.txt   -> tweet atıldıktan sonra görüşü deftere yaz
Görüş = tweetin son paragrafı (ya da 'bence/beğen/buldum/bana göre' geçen son paragraf)."""
import sys, os, re, json
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gorus_defteri.json')
KALIPLAR = [r'\bkarışık buldum', r'\bbeğendim\b', r'\bbeğenmedim\b', 
            r'yapay zekâdan çıkmıyor', r'bu da .* uyumlu', r'izlenecek', r'ilk somut', r'tam aradığı', r'okuyorum', r'okumam', r'okunuşu',
            r'\bçünkü\b', r'olumlu sinyal', r'mesaj şu', r'asıl soru', r'işaret ediyor']
def gorus(t):
    ps=[p.strip() for p in t.strip().split('\n\n') if p.strip()]
    for p in reversed(ps):
        if re.search(r'bence|beğen|buldum|bana göre|kanaatim|bence', p, re.I): return p
    return ps[-1] if ps else ''
def ac(p): return ' '.join(re.findall(r'\w+', p.lower())[:3])
def yukle():
    try: return json.load(open(D))
    except Exception: return []
def main():
    m=sys.argv[1] if len(sys.argv)>1 else 'kontrol'; t=sys.stdin.read(); g=gorus(t)
    d=yukle(); son=d[-12:]
    if m=='kaydet':
        d.append({'acilis':ac(g),'kaliplar':[k for k in KALIPLAR if re.search(k,g,re.I)],'metin':g[:160]})
        json.dump(d[-60:],open(D,'w'),ensure_ascii=False,indent=0); print('KAYDEDILDI'); return
    hata=[]
    if any(x['acilis']==ac(g) for x in son): hata.append(f"açılış tekrar: '{ac(g)}' (son 12 görüşte var)")
    for k in KALIPLAR:
        if re.search(k,g,re.I):
            n=sum(1 for x in son[-6:] if k in x['kaliplar'])
            if n>=1 and k not in (r'\bçünkü\b',): hata.append(f"kalıp son 6 görüşte kullanıldı: {k}")
    if hata: print('GORUS TEKRAR -> yeniden yaz:\n  - '+'\n  - '.join(hata)); sys.exit(1)
    print('GORUS TEMIZ')
if __name__=='__main__': main()

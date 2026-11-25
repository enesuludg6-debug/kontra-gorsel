#!/usr/bin/env python3
"""Konu seçimi puanı (skill enes-konu-secimi, Enes 25.11 18:11 'daha da geliştir').

Her turda 2-4 konu adayını 0-100 arası puanlar; en yüksek puanlı aday atılır,
60 altı aday atılmaz (hafta içi 18 alt sınırına yetişmek gerekiyorsa en az 50).

Kullanım:
  python3 invest/konu_puan.py --tur PORTFOY --saat 21 --portfoy 1 --kaynak 2 --taze 1 --egitici 0
    --tur     planlanan tür (performans_veri.csv'deki tur değerleri; * ve büyük/küçük harf yok sayılır)
    --saat    planlanan saat (0-23)
    --portfoy 1 = Enes'in portföy/ilgi listesindeki hisse
    --kaynak  doğrulanmış bağımsız kaynak sayısı (0/1/2+)
    --taze    1 = son 2 saatte çıkmış olgu
    --tekrar  1 = son 7 günde aynı konu atıldı
Çıktı: puan ve bileşenler. Puan tüm adaylar için DONGU'ya yazılır ('KONU-PUAN: a=72 b=55').
"""
import csv, os, sys, collections

D = os.path.dirname(os.path.abspath(__file__))

def arg(k, v=None, t=str):
    a = sys.argv
    return t(a[a.index(k) + 1]) if k in a else v

def f(x):
    try: return float(x or 0)
    except: return 0.0

def norm(t): return (t or '?').replace('*', '').upper()

def main():
    tur = norm(arg('--tur', '?')); saat = arg('--saat', 20, int)
    port = arg('--portfoy', 0, int); kay = arg('--kaynak', 2, int)
    taze = arg('--taze', 0, int); tek = arg('--tekrar', 0, int)
    R = [r for r in csv.DictReader(open(os.path.join(D, 'performans_veri.csv'), encoding='utf-8')) if f(r.get('gorunt')) > 0]
    ort = sum(f(r['begeni']) for r in R) / max(1, len(R))
    gt = collections.defaultdict(list); gs = collections.defaultdict(list)
    for r in R:
        gt[norm(r['tur'])].append(f(r['begeni'])); gs[(r.get('saat') or '00')[:2]].append(f(r['begeni']))
    def oran(g, k):
        v = g.get(k, [])
        if len(v) < 3: return 1.0
        return (sum(v) / len(v)) / max(ort, 0.1)
    p_tur = min(25, 12.5 * oran(gt, tur))
    p_saat = min(20, 10 * oran(gs, f"{saat:02d}"))
    p_port = 20 if port else 5
    p_kay = 20 if kay >= 2 else (8 if kay == 1 else 0)
    p_taze = 15 if taze else 5
    ceza = 30 if tek else 0
    puan = round(max(0, min(100, p_tur + p_saat + p_port + p_kay + p_taze - ceza)))
    print(f"KONU-PUAN {puan}  (tür {p_tur:.0f}/25, saat {p_saat:.0f}/20, portföy {p_port}/20, kaynak {p_kay}/20, tazelik {p_taze}/15, tekrar −{ceza})")
    if kay < 2: print("  not: tek kaynak -> rakam 'civarı' (kural 78) ya da atma")
    print("  karar:", "AT" if puan >= 60 else ("ancak 18 alt sınırı için" if puan >= 50 else "ATMA"))

if __name__ == '__main__':
    main()

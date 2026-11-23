#!/usr/bin/env python3
"""KURAL 61 — Analiz kalitesi standardı (Enes 23.11 20:08) mekanik kontrolü.
Skill: enes-analiz-kalitesi (yoksa invest/skills/enes-analiz-kalitesi.md). Asıl metin: invest/taslak/kalite_standardi_asil.txt

Kullanım (yasak.py ve gorus.py ile birlikte, HER create_post'tan önce):
  python3 invest/kalite.py kontrol --tur <TUR> < tweet.txt
  python3 invest/kalite.py kaydet  --tur <TUR> < tweet.txt     (tweet atıldıktan SONRA)
  python3 invest/kalite.py sinirlar                            (tür -> karakter sınırı listesi)

Çıkış: 0 = temiz | 1 = HATA (atma, düzelt, tekrar kontrol) | 2 = yalnız UYARI
(atılabilir; her UYARI için DONGU satırına 'kalite: <uyarı> -> <tek cümle gerekçe>' yazılır).
Bu betik yalnız ölçülebilen hataları yakalar; skill'deki düşünme adımlarının yerini TUTMAZ.
"""
import sys, os, re, json, datetime as dt

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'kalite_defteri.json')

# Karakter üst sınırları (23.11 ölçümü: sistem tweeti medyan ~790, en uzun 1093; Enes'in kendi tweetleri ~270
# ve İÇERİK AYARI kısa+iddialı olanın daha iyi gittiğini söylüyor). Sınır HEDEF DEĞİL, tavandır.
SINIR = {
    'SONDAKIKA': 600, 'HABER': 600, 'VADELI': 500, 'BEKLENTI': 500, 'OPSIYON': 600, 'KEYLEVELS': 700,
    'BILANCO-RAKAM': 700, 'TAKIP': 700, 'ICERIDEN-ALIM': 700, 'FED-TAHVIL': 700, 'MAKRO': 700, 'KRIPTO': 700,
    'BAGLAM-GORUS': 800, 'PORTFOY': 800, 'FIKIR': 800, 'SEKTOR': 800, 'ENES-HABER': 800, 'ENES-ISTEGI': 900,
    'EGITICI': 900, '13F': 1000, 'ANALIST': 1000, 'BILANCO-ANALIZ': 1200, 'HAFTALIK-OZET': 1200, 'AYIN-OZETI': 1200,
}
VARSAYILAN = 800
UZUN_UYARI = 700          # bu uzunluğu geçen her metin "kısa yazılınca değer kaybeder mi?" sorusunu cevaplar
OZET_TURLER = {'BILANCO-ANALIZ', 'HAFTALIK-OZET', 'AYIN-OZETI'}
BILANCO_TURLER = {'BILANCO-RAKAM', 'BILANCO-ANALIZ', 'BEKLENTI'}

YIL = dt.date.today().year
# Tarihsel atıf: geçerli yıl -2'den eski yıllar + bilinen kriz/dönem adları
KRIZ = {  # dönem adı -> kanonik yıl (aynı dönem iki kez sayılmaz)
    r'dot-?com': '2000', r'internet balonu': '2000', r'2000 balonu': '2000', r'2008 krizi': '2008', r'mortgage krizi': '2008',
    r'lehman': '2008', r'büyük buhran': '1929', r'kara pazartesi': '1987', r'black monday': '1987', r'asya krizi': '1997',
    r'ltcm': '1998', r'pandemi (çöküşü|dibi)': '2020', r'covid (çöküşü|dibi)': '2020', r'enron': '2001',
    r'nifty fifty': '1972', r'japonya balonu': '1989', r'lale çılgınlığı': '1637', r'2022 ayı': '2022', r'taper tantrum': '2013'}
BENZETME = [r'\bbenzer şekilde\b', r'\bo dönem(de)?\b', r'\bo zaman da\b', r'\baynı (senaryo|tablo|film)\b',
            r'\btarih tekerrür', r'\bbenzeri\b', r'\banımsatıyor\b', r'\bhatırlatıyor\b', r'\bdejavu\b', r'\bdéjà vu\b',
            r'\bgibi (olur|olacak|biter|bitecek)\b', r'\bbenz(iyor|eşiyor|etiyor)', r'\bandırıyor', r'\btekrarı (olabilir|gibi|yaşan)']
FARK = [r'\bfark', r'\baksine\b', r'\bbu kez\b', r'\bbu sefer\b', r'\bbugün ise\b', r'\bo dönemden farklı',
        r'\bo zaman .{0,40}yoktu\b', r'\bayrılıyor\b', r'\bkarşılaştırılamaz\b']
REKOR = r'(sonrası|beri|bu yana|yılından beri)\s+(en|ilk)\b'
KESINLIK = [r'\bkesinlikle\b', r'\bkaçınılmaz', r'\bgaranti\b', r'\bgarantili\b', r'\bşüphesiz\b', r'\bkuşkusuz\b',
            r'hiç şüphe yok', r'\bmutlaka (yüksel|düş|gel|ol|çık|toparlan)', r'\bkesin olarak (yüksel|düş|gel|ol|çık)',
            r'\b%100 (yüksel|düş|olur)', r'\bkaçışı yok\b']
AKIS = [r'kurumsal akış', r'\bfonlar (sat|al|boşalt|çık|kaç|topl)', r'akıllı para', r'büyük oyuncular', r'\bbalinalar',
        r'pozisyon (boşalt|kapat|biriktir)', r'short squeeze', r'açığa satış sıkışması', r'kısa pozisyon kapan',
        r'\bmarjinal alıcı', r'kaldıraç (çözül|temizlen)', r'tasfiye (dalga|zincir)']
SENARYO = [r'boğa senaryo', r'ayı senaryo', r'(baz|temel) senaryo']
TERIM = ['capex', 'sermaye harcaması', 'katalizör', 'konsensüs', 'çarpan daralması', 'çarpan genişlemesi',
         'değerleme çarpanı', 'f/k', 'fd/favök', 'brüt marj', 'faaliyet marjı', 'serbest nakit akışı', 'arr',
         'rpo', 'kalan performans yükümlülüğü', 'pozisyonlanma', 'pozisyon yoğunlaşması', 'marjinal alıcı',
         'kurumsal akış', 'içsel değer', 'hiperölçekli', 'likidite', 'parasal aktarım', 'getiri eğrisi',
         'vade primi', 'risk primi', 'gamma', 'delta', 'örtük oynaklık', 'implied vol', 'skew', 'fonlama oranı',
         'açık pozisyon', 'mikro yapı', 'sipariş defteri', 'sipariş görünürlüğü', 'büyümenin kalitesi', 'ivmelenme',
         'rehber revizyonu', 'risk azaltımı', 'durasyon', 'duration', 'reel faiz', 'terminal faiz', 'bilanço daralması',
         'operasyonel kaldıraç', 'birim ekonomisi', 'nakit yakımı', 'sulandırma', 'hisse geri alımı']
# Bilanço tweetinde makro/kripto bağlantısı ve kripto tweetinde tahvil bağlantısı: zorlama riski
ZORLA = {
    'BILANCO': [r'\bfed\b', r'faiz', r'tahvil', r'bitcoin', r'kripto', r'dolar endeksi', r'\bdxy\b'],
    'KRIPTO': [r'tahvil', r'10 yıllık', r'getiri eğrisi'],
    'MAKRO': [r'opsiyon', r'gamma', r'skew'],
}

def low(t): return t.lower().replace('İ', 'i').replace('I', 'ı')
def kelime(s, n): return ' '.join(re.findall(r'\w+', s.lower())[:n])
def paragraflar(t): return [p.strip() for p in re.split(r'\n\s*\n', t.strip()) if p.strip()]

def ozellik(t):
    l = low(t)
    # "Mart 2020 sonrası en kötü hafta" gibi REKOR istatistiği benzetme değil veridir: yılı ayrı sayılır
    rek = set(re.findall(r'\b((?:19|20)\d{2})(?:\'?\w*)?\s+(?:sonrası|beri|bu yana|yılından beri)\s+(?:en|ilk)\b', l))
    tarih = set()
    for y in re.findall(r'\b(19\d{2}|20\d{2})\b', l):
        if int(y) <= YIL - 2 and y not in rek:
            tarih.add(y)
    for k, y in KRIZ.items():
        if re.search(k, l): tarih.add(y)
    terim = sorted({k for k in TERIM if re.search(r'(?<!\w)' + re.escape(k) + r'(?!\w)', l)})
    ps = paragraflar(t)
    return {
        'tarih': sorted(tarih), 'terim': terim,
        'acilis': kelime(ps[0], 4) if ps else '', 'kapanis': kelime(ps[-1], 4) if ps else '',
        'rekor': len(re.findall(REKOR, l)),
    }

def yukle():
    try: return json.load(open(D, encoding='utf-8'))
    except Exception: return []

def main():
    a = sys.argv[1:]
    m = a[0] if a else 'kontrol'
    if m == 'sinirlar':
        for k, v in sorted(SINIR.items(), key=lambda x: x[1]): print(f'{k:15} {v}')
        print(f'{"(diğer)":15} {VARSAYILAN}'); return
    tur = (a[a.index('--tur') + 1] if '--tur' in a else 'DIGER').upper()
    t = sys.stdin.read()
    if not t.strip(): sys.exit('boş metin')
    f = ozellik(t); d = yukle()
    if m == 'kaydet':
        f.update({'tur': tur, 'zaman': dt.datetime.now().strftime('%d.%m %H:%M'), 'uzunluk': len(t.strip())})
        d.append(f); json.dump(d[-60:], open(D, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
        print('KALITE KAYDEDILDI'); return

    l = low(t); n = len(t.strip()); hata = []; uyari = []
    # 1) Uzunluk (bölüm 8-9: uzunluğu konu belirler, derinlik != kelime sayısı)
    sinir = SINIR.get(tur, VARSAYILAN)
    if n > sinir:
        hata.append(f'uzunluk {n} > {tur} tavanı {sinir}. Kısalt: tekrar eden bağlamı, ikinci örneği, ikinci senaryoyu, '
                    f'terim açıklamasını at; derinliği Enes\'e "Ne anlama geliyor?" mesajına taşı.')
    elif n > UZUN_UYARI:
        uyari.append(f'uzunluk {n} (> {UZUN_UYARI}): "daha kısa yazılınca değer kaybeder mi?" sorusuna cevap ver; kaybetmiyorsa kısalt.')
    # 2) Tarihsel karşılaştırma disiplini (bölüm 4)
    if len(f['tarih']) > 1:
        hata.append(f'birden fazla tarihsel atıf {f["tarih"]}: en fazla 1, o da gerçekten açıklayıcıysa.')
    benz = [k for k in BENZETME if re.search(k, l)]
    if re.search(r'tarih tekerrür', l):
        hata.append('"tarih tekerrür" kalıbı: geçmişin aynı sonucu doğuracağı varsayımı (bölüm 4) — sil.')
    elif (f['tarih'] or benz) and benz and not any(re.search(k, l) for k in FARK):
        hata.append(f'tarihsel benzetme var ({benz[0]}) ama kritik fark yazılmamış: farkı tek cümleyle yaz ya da karşılaştırmayı sil.')
    if f['rekor'] > 3 and tur not in OZET_TURLER:
        hata.append(f'{f["rekor"]} adet "X sonrası en/ilk" rekor ifadesi: en anlamlı 1-2 tanesini bırak.')
    elif f['rekor'] > 2:
        uyari.append(f'{f["rekor"]} adet "X sonrası en/ilk" rekor ifadesi: en anlamlı 1-2 tanesini bırak (her biri 2 kaynak).')
    # 3) Belirsizlik: olasılık kesinlik gibi sunulmaz (bölüm 6)
    for k in KESINLIK:
        mm = re.search(k, l)
        if mm: hata.append(f'kesinlik ifadesi "{mm.group(0)}": tahmini koşula bağla ("... olursa ...") ya da sil.')
    # 4) Senaryo: her tweete boğa/ayı/baz konmaz (bölüm 6)
    sn = sum(1 for k in SENARYO if re.search(k, l))
    if sn == 3:
        (uyari if tur in OZET_TURLER else hata).append('boğa/ayı/baz üçlüsü: her tweete konmaz; en çok tek koşul cümlesi + geçersiz kılan gelişme.')
    # 5) Terim yığını (bölüm 2, 9)
    if len(f['terim']) > 6:
        hata.append(f'{len(f["terim"])} teknik terim {f["terim"]}: terim yığını. Analize somut katkısı olmayanları sil (en çok 4-5).')
    elif len(f['terim']) > 4:
        uyari.append(f'{len(f["terim"])} terim {f["terim"]}: her birinin somut katkısı var mı, okur anlıyor mu?')
    # 6) Uydurma akış/pozisyonlanma riski (bölüm 3)
    ak = [re.search(k, l).group(0) for k in AKIS if re.search(k, l)]
    if ak:
        uyari.append(f'akış/pozisyonlanma iddiası {ak}: veri kaynağı (BofA anketi, CFTC, ETF akışı, 13F, borsa verisi) DONGU\'ya yazılmadıysa SİL.')
    # 7) Zorlama bağlantı (bölüm 7)
    grup = 'BILANCO' if tur in BILANCO_TURLER else tur if tur in ZORLA else None
    if grup:
        zz = [re.search(k, l).group(0) for k in ZORLA[grup] if re.search(k, l)]
        if zz: uyari.append(f'{tur} tweetinde {zz}: bu bağlantı şirketin/konunun rakamlarına doğrudan etki ediyor mu? Etmiyorsa sil.')
    # 8) Tekrar (bölüm 8): son tweetlerle aynı tarihsel örnek / açılış / kapanış / terim seti
    son15, son30 = d[-15:], d[-30:]
    for y in f['tarih']:
        if any(y in x.get('tarih', []) for x in son15):
            hata.append(f'tarihsel örnek "{y}" son 15 tweette kullanıldı: tekrar etme.')
    if f['acilis'] and any(x.get('acilis') == f['acilis'] for x in son30):
        hata.append(f'açılış "{f["acilis"]}" son 30 tweette var: farklı kur.')
    if f['kapanis'] and any(x.get('kapanis') == f['kapanis'] for x in son15):
        hata.append(f'kapanış "{f["kapanis"]}" son 15 tweette var: farklı bitir.')
    if f['terim'] and len(d) >= 3:
        ort = set(f['terim']).intersection(*[set(x.get('terim', [])) for x in d[-3:]])
        if ort: uyari.append(f'terim(ler) {sorted(ort)} son 3 tweetin hepsinde geçti: eş anlamlı ya da somut ifade kullan.')
    if hata:
        print('KALITE HATA -> atma, düzelt, tekrar kontrol et:\n  - ' + '\n  - '.join(hata + uyari)); sys.exit(1)
    if uyari:
        print('KALITE UYARI -> atılabilir; her biri için DONGU\'ya tek cümle gerekçe yaz ya da düzelt:\n  - ' + '\n  - '.join(uyari)); sys.exit(2)
    print('KALITE TEMIZ')

if __name__ == '__main__':
    main()

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
    'EGITICI': 900, 'DERIN-ANALIZ': 1200, '13F': 1000, 'ANALIST': 1000, 'BILANCO-ANALIZ': 1200, 'HAFTALIK-OZET': 1200, 'AYIN-OZETI': 1200,
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
# KURAL 62 (Enes 23.11 20:40: "çok fazla fiyatlandı iskonto ve bunun gibi kelimeler kullanıyorsun, bunları bu kadar sık kullanmanı istemiyorum"):
# piyasa jargonu aileleri. Her aile tweet başına en çok 1 kez, son 6 tweette geçtiyse HATA; bir tweette en çok 1 aile.
JARGON = {
    'fiyatlama': r'fiyatla(n|m|d|y)\w*|fiyatlıyor\w*|fiyattan (çık|düş)\w*|fiyata (yansı|gir)\w*|fiyatına (yansı|gir)\w*',
    'iskonto': r'iskonto\w*',
    'prim': r'\bprim(i|ini|le|li)?\b|risk primi',
    'denklem': r'denklem\w*',
    'çarpan': r'çarpan\w*',
    'katalizör': r'katalizör\w*',
    'pozisyonlanma': r'pozisyonlan\w*|pozisyon yoğunlaş\w*',
    'konsensüs': r'konsensüs\w*',
    'iştah': r'iştah\w*',
    'kâr satışı': r'kâr (satış|realiz)\w*|kar satış\w*',
    'belirsizlik': r'belirsizli\w*',
    'ayrışma': r'ayrış\w*',
}
# KURAL 63 (Enes 23.11 20:44): derinlik evet, ham İngilizce opsiyon/fon jargonu hayır (okur anlamıyor). Ne yaptığını Türkçe anlat.
HAM_JARGON = [r'\bvanna\b', r'\bvega\b', r'\bgamma\b', r'\bdelta (hedge|hedg|nötr|riski)', r'\biv\b', r'\batm\b', r'\botm\b',
              r'\bitm\b', r'\bskew\b', r'\bnav\b', r'deleverag', r'squeeze', r'\broll\b', r'\bcollar\b', r'catch-?up trade',
              r'\bfeedback loop', r'\bspot down', r'\bvol down', r'\bhedge\b', r'\bleptokurt']
DERIN_GUNLUK = 2
# KURAL 63-B (Enes 23.11 21:11: "çoğunun etkisini göremiyorum, görmek istiyorum"): her tweet --kalip A..F ile yazılır ve kalıbın izi metinde olmalı.
KALIP_MUAF = {'VADELI', 'BEKLENTI', 'BILANCO-RAKAM', 'KEYLEVELS', 'ENES-ISTEGI', 'ENES-HABER'}
def _sayilar(l): return re.findall(r'\d+(?:[.,]\d+)?', l)
def kalip_kontrol(k, l, t):
    cumle = [c for c in re.split(r'[.!\n]+', t) if c.strip()]
    if k == 'A':
        bag = len(re.findall(r'\b(bu yüzden|bu da|böylece|dolayısıyla|bu nedenle|o yüzden|bunun sonucunda|sonra|ardından|bu durumda)\b|→', l))
        return bag >= 2 and len(cumle) >= 4, 'A zinciri: en az 3 adım ve en az 2 bağlaç (bu yüzden, bu da, böylece, dolayısıyla, ardından...) gerekli'
    if k == 'B':
        return bool(re.search(r'\b(o zaman|o dönem|geçen sefer|önceki|o seferde)\b', l)) and bool(re.search(r'\b(bugün|şimdi|bu kez|bu sefer)\b', l)), 'B: geçmişteki durum (o zaman/önceki) ve bugünkü durum (bugün/şimdi/bu kez) açıkça karşılaştırılmalı'
    if k == 'C':
        return bool(re.search(r'\w+(?:ırsa|irse|ursa|ürse|arsa|erse|sa|se)\b', l)) and len(_sayilar(l)) >= 2, 'C eşik: en az bir koşul (-sa/-se) ve eşik rakamı gerekli'
    if k == 'D':
        return len(_sayilar(l)) >= 3 and bool(re.search(r'piyasa değer|katı|katından|kat\b|nakit|yıllığa|biçiyor|değer veriyor|oran', l)), 'D değer hesabı: en az 3 rakam ve kendi hesap ifadesi (piyasa değeri, kârın X katı, nakit, yıllığa çevrilince, biçilen değer) gerekli'
    if k == 'E':
        return len(cumle) >= 3, 'E tek kavram dersi: kavram + örnek + çıkarım'
    if k == 'G':
        return bool(re.search(r'beklen|tahmin', l)) and bool(re.search(r'geldi|açıkla|gerçekleş|oldu', l)) and len(_sayilar(l)) >= 2, 'G beklenti farkı: beklenen rakam ve gelen rakam yan yana (en az 2 rakam)'
    if k == 'H':
        return bool(re.search(r'başına', l)) and len(_sayilar(l)) >= 2, 'H birim ekonomisi: "X başına" hesap (müşteri/MW/fırlatma/GPU saati başına) ve rakam'
    if k == 'I':
        return bool(re.search(r'nakit akış|serbest nakit|hisse sayısı|seyrel|geri alım|yatırım harcama|borç|nakd', l)) and len(_sayilar(l)) >= 2, 'I nakit ve sermaye: kâr ile nakit farkı, yatırım harcaması, borç, seyrelme ya da geri alım rakamla'
    if k == 'J':
        return len(set(re.findall(r'\$[A-Z]{1,5}', t))) >= 2 and bool(re.search(r'müşteri|tedarikçi|harcama|sipariş|geliri', l)), 'J değer zinciri: bir şirketin haberinden müşterisine/tedarikçisine geçiş (en az 2 $TICKER ve müşteri/tedarikçi bağı)'
    if k == 'K':
        return bool(re.search(r'haklı çıka|gerekiyor|gerekir|büyümesi gerek|için .{0,30}gerek', l)) and len(_sayilar(l)) >= 2, 'K tersine hesap: bugünkü fiyatın haklı çıkması için neyin olması gerektiği, rakamla'
    if k == 'L':
        return len(set(re.findall(r'\$[A-Z]{1,5}', t))) >= 2 and bool(re.search(r'göre|kıyasla|karşılaştır|aynı ölçü', l)) and len(_sayilar(l)) >= 3, 'L akran kıyası: en az 2 şirket aynı ölçüyle, en az 3 rakam'
    if k == 'M':
        return bool(re.search(r'\b\d{1,2} (ocak|şubat|mart|nisan|mayıs|haziran|temmuz|ağustos|eylül|ekim|kasım|aralık)|aralık|ocak|haftaya|yarın|perşembe|cuma', l)) and bool(re.search(r'bakacağım|izleyeceğim|belirleyecek|gösterecek|netleşecek', l)), 'M tetikleyici takvimi: somut tarih ve o tarihte bakılacak rakam'
    if k == 'N':
        return bool(re.search(r'bozar|bozulur|yeter|çeyrek boyunca|dayanır|kırılma', l)) and len(_sayilar(l)) >= 2, 'N kırılma noktası: tezi bozacak tek şey ve bugünkü mesafesi, rakamla (ör. nakit kaç çeyrek yeter)'
    if k == 'F':
        return bool(re.search(r'olağan|normal|sık görülür|alışılmış', l)), 'F: hareketin olağan olduğunu açıkça söyle'
    return False, 'kalıp A-N olmalı'
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
    jar = {k: len(re.findall(v, l)) for k, v in JARGON.items()}
    return {
        'jargon': {k: n for k, n in jar.items() if n},
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
        _n = dt.datetime.now(dt.timezone(dt.timedelta(hours=3)))
        f.update({'kalip': (a[a.index('--kalip') + 1].upper() if '--kalip' in a else ''), 'tur': tur, 'zaman': _n.strftime('%d.%m %H:%M'), 'gun': (_n - dt.timedelta(hours=2)).strftime('%d.%m'), 'uzunluk': len(t.strip())})
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
    # 7-0) KURAL 63-B: kalıp zorunlu ve izi görünmeli
    kalip = (a[a.index('--kalip') + 1].upper() if '--kalip' in a else '')
    if tur not in KALIP_MUAF:
        if not kalip:
            hata.append('kural 63-B: --kalip A-N ver (A zincir, B o zaman/şimdi, C koşullu eşik, D değer hesabı, E tek kavram, F normalleştirme, G beklenti farkı, H birim ekonomisi, I nakit/sermaye, J değer zinciri, K tersine hesap, L akran kıyası, M tetikleyici takvimi, N kırılma noktası).')
        else:
            ok, msg = kalip_kontrol(kalip, l, t)
            if not ok: hata.append('kural 63-B: ' + msg)
        if len(_sayilar(l)) < 2 and tur != 'EGITICI':
            hata.append('kural 63-B: rakamla konuş; en az 2 doğrulanmış rakam.')
    if kalip and len(d) >= 2 and all(x.get('kalip') == kalip for x in d[-2:]):
        hata.append(f'kural 63-B: {kalip} kalıbı son 2 tweette kullanıldı; başka kalıp seç (çeşitlilik).')
    # 7a) KURAL 63: ham jargon ve derin analiz günlük sınırı
    hj = [re.search(k, l).group(0) for k in HAM_JARGON if re.search(k, l)]
    if hj: hata.append(f'kural 63: ham İngilizce jargon {hj}: terimi yazma, ne yaptığını gündelik Türkçeyle anlat (ör. "piyasa yapıcılar riskten korunmak için vadeli satıyor").')
    if tur == 'DERIN-ANALIZ':
        bugun = dt.datetime.now(dt.timezone(dt.timedelta(hours=3))) - dt.timedelta(hours=2)
        n_bugun = sum(1 for x in d if x.get('tur') == 'DERIN-ANALIZ' and x.get('gun') == bugun.strftime('%d.%m'))
        if n_bugun >= DERIN_GUNLUK: hata.append(f'kural 63: bugün zaten {n_bugun} DERIN-ANALIZ atıldı (günde en çok {DERIN_GUNLUK}); başka türde, kısa yaz.')
    # 7b) KURAL 62 piyasa jargonu sıklığı
    jg = f['jargon']
    for k, n in jg.items():
        if n > 1: hata.append(f'kural 62: "{k}" ailesi bu tweette {n} kez: en çok 1, gerekirse hiç kullanma, düz anlat.')
        son6 = [x for x in d[-6:] if k in x.get('jargon', {})]
        if son6: hata.append(f'kural 62: "{k}" ailesi son 6 tweette {len(son6)} kez geçti: bu tweette kullanma, ne olduğunu düz cümleyle söyle.')
    if len(jg) > 1:
        hata.append(f'kural 62: bir tweette birden fazla piyasa jargonu {sorted(jg)}: en çok 1.')
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

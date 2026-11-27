#!/usr/bin/env python3
"""kalabalik.py — kural 97 (Enes 27.11 12:09 'yap'): KALABALIK ENDEKSİ, ücretsiz verilerle kendi
'akıllı para / aptal para' karşılığımız (SentimenTrader ücretli; verisi/grafiği KULLANILMAZ).

İki ölçü, ikisi de 0-100:
  BİREYSEL İYİMSERLİK ('aptal para' karşılığı; yüksek = kalabalık iyimser, karşıt okumada tepe riski)
    - CNN Korku-Açgözlülük (0-100, olduğu gibi)            alt_veri/korku_seri.csv
    - AAII boğa-ayı farkı: 50 + 2*(fark - 6.5), 0-100 kırpılır  alt_veri/aaii.csv (tarihsel ort. fark +6.5)
    - CBOE hisse put/call: (0.90 - pc) / 0.50 * 100, 0-100 kırpılır  alt_veri/nabiz.json
  KURUMSAL SAKİNLİK ('akıllı para' tarafının korunma davranışı; yüksek = kurumlar korunmaya para ödemiyor)
    - VIX/VIX3M oranı, son 1 yılın yüzdelik sırası, ters çevrilmiş (Yahoo)
    - SKEW, son 1 yılın yüzdelik sırası, ters çevrilmiş (Yahoo)
    - CBOE endeks put/call: (1.40 - pc) / 0.80 * 100, 0-100 kırpılır  alt_veri/nabiz.json
Okuma: bireysel iyimserlik düşük + kurumsal sakinlik yüksek = kalabalık korkuyor, kurumlar korkmuyor (tarihsel olarak dip bölgesi
       davranışı); tersi = kalabalık coşkulu, kurumlar korunuyor (tepe riski). Ölçek kendi yöntemimizdir, tweette 'kendi ölçeğim' denir.
Kullanım:
  python3 invest/kalabalik.py hesap        bugünkü iki ölçü + bileşenler, alt_veri/kalabalik.csv'ye ekler
  python3 invest/kalabalik.py kart g/YYYYMMDD_HHMM_kalabalik.jpg
"""
import sys, os, json, csv, datetime as dt, urllib.request
D = os.path.dirname(os.path.abspath(__file__)); A = os.path.join(D, "alt_veri"); KAYIT = os.path.join(A, "kalabalik.csv")
kirp = lambda x: max(0.0, min(100.0, x))

def yahoo(s, aralik="1y"):
    u = f"https://query1.finance.yahoo.com/v8/finance/chart/{s}?range={aralik}&interval=1d"
    d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=30))["chart"]["result"][0]
    return {dt.datetime.fromtimestamp(t, dt.timezone.utc).date().isoformat(): c for t, c in zip(d["timestamp"], d["indicators"]["quote"][0]["close"]) if c}

def yuzdelik(seri, deger):
    v = sorted(seri); return 100.0 * sum(1 for x in v if x <= deger) / len(v)

def hesap(yaz=True):
    b, k = {}, {}
    fg = list(csv.reader(open(os.path.join(A, "korku_seri.csv"))))[-1]; b["CNN korku-açgözlülük"] = (float(fg[1]), f"{float(fg[1]):.0f} ({fg[0]})")
    aa = [r for r in csv.reader(open(os.path.join(A, "aaii.csv"))) if r and r[0][:1].isdigit()][-1]
    fark = float(aa[1]) - float(aa[3]); b["AAII boğa-ayı farkı"] = (kirp(50 + 2 * (fark - 6.5)), f"{fark:+.1f} puan ({aa[0]})")
    nb = json.load(open(os.path.join(A, "nabiz.json")))[-1]
    if nb.get("pc_hisse"): b["Hisse put/call"] = (kirp((0.90 - nb["pc_hisse"]) / 0.50 * 100), f"{nb['pc_hisse']:.2f} ({nb['tarih']})")
    if nb.get("pc_endeks"): k["Endeks put/call"] = (kirp((1.40 - nb["pc_endeks"]) / 0.80 * 100), f"{nb['pc_endeks']:.2f} ({nb['tarih']})")
    vx, v3, sk = yahoo("^VIX"), yahoo("^VIX3M"), yahoo("^SKEW")
    oran = {t: vx[t] / v3[t] for t in vx if t in v3}; son = max(oran)
    k["VIX/VIX3M"] = (100 - yuzdelik(oran.values(), oran[son]), f"{oran[son]:.2f} ({son})")
    ss = max(sk); k["SKEW"] = (100 - yuzdelik(sk.values(), sk[ss]), f"{sk[ss]:.0f} ({ss})")
    bi = sum(v for v, _ in b.values()) / len(b); ku = sum(v for v, _ in k.values()) / len(k)
    if ku - bi >= 25: okuma = "kalabalık korkuyor, kurumlar korunmuyor: karşıt okumada dip bölgesi davranışı"
    elif bi - ku >= 25: okuma = "kalabalık iyimser, kurumlar korunuyor: karşıt okumada tepe riski"
    elif bi < 30 and ku < 30: okuma = "iki taraf da korkuyor: gerçek stres, dip için erken"
    elif bi > 70 and ku > 70: okuma = "iki taraf da rahat: rehavet"
    else: okuma = "ayrışma yok, nötr bölge"
    print(f"KALABALIK ENDEKSİ {dt.date.today()}\n  BİREYSEL İYİMSERLİK {bi:.0f}/100")
    for n, (v, a) in b.items(): print(f"    {n:24s} {v:5.0f}   ham {a}")
    print(f"  KURUMSAL SAKİNLİK   {ku:.0f}/100")
    for n, (v, a) in k.items(): print(f"    {n:24s} {v:5.0f}   ham {a}")
    print(f"  FARK (kurumsal - bireysel) {ku - bi:+.0f} -> {okuma}")
    if yaz:
        yeni = not os.path.exists(KAYIT); f = open(KAYIT, "a", newline="", encoding="utf-8"); w = csv.writer(f)
        if yeni: w.writerow(["tarih", "bireysel", "kurumsal", "fark", "okuma"])
        w.writerow([dt.date.today().isoformat(), round(bi), round(ku), round(ku - bi), okuma])
    return bi, ku, b, k, okuma

def kart(out):
    import kart3 as K
    bi, ku, b, k, okuma = hesap(yaz=False)
    kal = [("BİREYSEL İYİMSERLİK", f"{bi:.0f}/100", "CNN + AAII + hisse put/call", bi >= 50),
           ("KURUMSAL SAKİNLİK", f"{ku:.0f}/100", "VIX vade + SKEW + endeks put/call", ku >= 50),
           ("FARK", f"{ku - bi:+.0f}", "kurumsal eksi bireysel", ku >= bi)]
    K.bilanco("PİYASA NABZI · KALABALIK ENDEKSİ", "Kalabalık korkuyor, kurumlar ne yapıyor" if bi < 45 else "Kalabalık iyimser, kurumlar ne yapıyor",
              "Kendi ölçeğim, 0-100 (ücretsiz verilerle)", kal, okuma[:1].upper() + okuma[1:].split(":")[0],
              "CNN, AAII, CBOE, Yahoo; kendi hesabım", out)
    print("kart:", out)

if __name__ == "__main__":
    a = sys.argv[1:]
    if not a or a[0] == "hesap": hesap()
    elif a[0] == "kart": kart(a[1])
    else: print(__doc__)

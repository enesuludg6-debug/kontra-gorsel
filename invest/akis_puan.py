#!/usr/bin/env python3
"""akis_puan.py — Unusual Whales ekran görüntüsü + kendi teknik analizimiz -> 1-10 uyum puanı (kural 94, Enes 26.11 10:16).
Enes (arkadaşının hesabından) akış/karanlık havuz ekran görüntüsü atar. Görüntü OLDUĞU GİBİ yorumlanmaz:
her hisse için kendi teknik analizimiz yapılır ve 'bizim teknik düşüncemize' uyum puanlanır, sonra sıralanır.

Kullanım:
  python3 invest/akis_puan.py sablon > /tmp/akis.json        boş giriş şablonu
  python3 invest/akis_puan.py puan /tmp/akis.json [--kart]     puanla, sırala, alt_veri/akis_puan.csv'ye yaz
  python3 invest/akis_puan.py teknik AVGO,RKLB                 akış olmadan yalnız teknik kısım (0-6)

Giriş JSON (ekran görüntüsünden ELLE okunur; görüntüde olmayan alan boş bırakılır, uydurulmaz):
{"tarih":"2026-11-28","kaynak":"Unusual Whales ekran görüntüsü",
 "hisseler":{"AVGO":{"call_prim":12.5,"put_prim":4.0,     # milyon $, görünen toplam prim
                     "sweep_call":5,"sweep_put":1,         # ask tarafı sweep sayısı
                     "uzun_vade":true,                     # büyük işlemlerin vadesi >= 30 gün mü
                     "dp":[[285.4,1.2]],                   # karanlık havuz blokları [fiyat, milyon adet]
                     "not":"3 Ocak 320 call 4,1 M$"}}}

PUAN (10 üzerinden) = TEKNİK (6) + AKIŞ (4) - CEZA
 TEKNİK — bizim yaklaşımımız: kanıtlı dip bölgesinde, büyük trend bozulmadan alım
  T1 dip bölgesi (0-2): RSI<35 ya da stoch<20 (+1); fiyat Bollinger alt bandına / 20 gün dibine 1 ATR yakın (+1)
  T2 kanıtlı kalıp (0-2): tarama_kanit'te ÜSTÜN çıkan kalıp (dip_avcisi, derin_dip) eşleşiyor (2); kanıtsız dip kalıbı (supurme_donus, birikim) (1)
  T3 dönüş izi (0-1): dip süpürmesi, çekiç, supertrend ya da MACD yukarı dönüşü
  T4 büyük resim (0-1): kapanış EMA200 üstü ya da haftalık supertrend yukarı
 AKIŞ — kurumsal ayak izi
  A1 yön (0-2): call primi payı >= %65 (2), >= %55 (1)
  A2 kalite (0-1): uzun vadeli ve sweep ağırlıklı (call sweep > put sweep)
  A3 karanlık havuz çakışması (0-1): blok seviyesi fiyatın 1 ATR içinde ve fiyatın altında ya da üstünde destek gibi
 CEZA: bilanço <= 7 gün (-1, oynaklık); destek kırılımı kalıbı (-1); aşırı uzama/tepe riski (-1)
Puan al/sat tavsiyesi DEĞİLDİR: 'bizim yaklaşımımıza uyum' ölçüsüdür.
"""
import sys, os, json, csv, datetime as dt, warnings
warnings.filterwarnings("ignore")
KOK = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, KOK)
from gosterge import veri, hesapla, degerlendir
from tarama import HAZIR

KANIT = {}
try: KANIT = json.load(open(os.path.join(KOK, "tarama_kanit.json")))
except Exception: pass
USTUN = [k for k, v in KANIT.items() if v.get("hukum") == "ÜSTÜN"] or ["dip_avcisi", "derin_dip"]
DIP_KALIP = ["supurme_donus", "birikim"]
CSV = os.path.join(KOK, "alt_veri", "akis_puan.csv")

_ref = None
def cerceve(t):
    global _ref
    if _ref is None: _ref = veri("QQQ", "5y")
    return hesapla(veri(t, "5y"), _ref)

def bilanco_gun(t):
    yol = os.path.join(KOK, "alt_veri", "bilanco_tarih.csv"); bugun = dt.date.today(); en = None
    try:
        for r in csv.DictReader(open(yol)):
            if r["t"] != t: continue
            g = (dt.date.fromisoformat(r["reporting_date"]) - bugun).days
            if g >= 0 and (en is None or g < en): en = g
    except Exception: pass
    return en

def teknik(t):
    x = cerceve(t); r = x.iloc[-1]; n = []; p = {}
    eslesen = [k for k, (_, ifade) in HAZIR.items() if degerlendir(x, ifade).iloc[-1]]
    t1 = 0
    if r.rsi < 35 or r.stoch_k < 20: t1 += 1; n.append(f"aşırı satım (RSI {r.rsi:.0f}, stoch {r.stoch_k:.0f})")
    yakin = min(abs(r.kapanis - r.bb_alt), abs(r.kapanis - r.dusuk20)) <= r.atr
    if yakin: t1 += 1; n.append(f"destek yakını (BB alt {r.bb_alt:.2f}, 20g dip {r.dusuk20:.2f})")
    p["T1"] = t1
    us = [k for k in eslesen if k in USTUN]; dk = [k for k in eslesen if k in DIP_KALIP]
    p["T2"] = 2 if us else (1 if dk else 0)
    if us: n.append("kanıtlı kalıp: " + ",".join(us))
    elif dk: n.append("kanıtsız dip kalıbı: " + ",".join(dk))
    p["T3"] = 1 if (r.sup_boga or r.cekic or r.st_yukari or r.macd_yukari) else 0
    if p["T3"]: n.append("dönüş izi var")
    p["T4"] = 1 if (r.kapanis > r.ema200 or r.get("h_supertrend_yon", 0) == 1) else 0
    import math
    if p["T4"]: n.append("büyük trend sağlam")
    elif math.isnan(r.ema200): n.append("EMA200 için geçmiş yetersiz (yeni halka arz)")
    else: n.append(f"EMA200 ({r.ema200:.2f}) altında, haftalık trend aşağı")
    ceza = 0; b = bilanco_gun(t)
    if b is not None and b <= 7: ceza += 1; n.append(f"bilanço {b} gün sonra")
    if "kirilim_asagi" in eslesen: ceza += 1; n.append("destek kırılımı")
    if "asiri_alim" in eslesen: ceza += 1; n.append("aşırı uzama")
    return dict(t=t, fiyat=round(float(r.kapanis), 2), atr=float(r.atr), teknik=sum(p.values()), parca=p,
                ceza=ceza, kaliplar=eslesen, notlar=n)

def akis(a, tk):
    if not a: return 0, {}, ["akış verisi yok"]
    p, n = {}, []
    c, pu = a.get("call_prim"), a.get("put_prim")
    if c is not None and pu is not None and c + pu > 0:
        pay = c / (c + pu); p["A1"] = 2 if pay >= .65 else (1 if pay >= .55 else 0)
        n.append(f"call payı %{pay*100:.0f} ({c} / {pu} M$)")
    else: p["A1"] = 0; n.append("prim verisi eksik")
    sc, sp = a.get("sweep_call", 0) or 0, a.get("sweep_put", 0) or 0
    p["A2"] = 1 if (a.get("uzun_vade") and sc > sp) else 0
    if p["A2"]: n.append(f"uzun vadeli, call sweep ağırlıklı ({sc}/{sp})")
    dp = a.get("dp") or []
    yakin = [f for f, _ in dp if abs(f - tk["fiyat"]) <= tk["atr"]]
    p["A3"] = 1 if yakin else 0
    if dp: n.append("karanlık havuz " + ", ".join(f"{f}" for f, _ in dp) + (" (fiyata yakın)" if yakin else " (uzak)"))
    if a.get("not"): n.append(a["not"])
    return sum(p.values()), p, n

def puanla(yol, kart=False):
    g = json.load(open(yol)); sonuc = []
    for t, a in g["hisseler"].items():
        t = t.upper()
        try: tk = teknik(t)
        except Exception as e: print(f"{t}: veri hatası {e}"); continue
        ak, ap, an = akis(a, tk)
        puan = max(1, min(10, tk["teknik"] + ak - tk["ceza"]))
        sonuc.append(dict(t=t, puan=puan, teknik=tk["teknik"], akis=ak, ceza=tk["ceza"], fiyat=tk["fiyat"],
                          parca={**tk["parca"], **ap}, notlar=tk["notlar"] + an))
    sonuc.sort(key=lambda s: (-s["puan"], -s["teknik"]))
    print(f"AKIŞ + TEKNİK UYUM PUANI — {g.get('tarih','?')} (bizim yaklaşımımıza uyum, al/sat tavsiyesi değil)\n")
    for i, s in enumerate(sonuc, 1):
        print(f"{i}. {s['t']}  {s['puan']}/10   teknik {s['teknik']}/6 + akış {s['akis']}/4 - ceza {s['ceza']}   fiyat {s['fiyat']}")
        print("   " + " | ".join(s["notlar"]))
    yeni = not os.path.exists(CSV)
    with open(CSV, "a", newline="") as f:
        w = csv.writer(f)
        if yeni: w.writerow(["tarih", "t", "puan", "teknik", "akis", "ceza", "fiyat"])
        for s in sonuc: w.writerow([g.get("tarih"), s["t"], s["puan"], s["teknik"], s["akis"], s["ceza"], s["fiyat"]])
    print(f"\nKayıt: {CSV} (ileriye dönük ölçüm: 5/20 gün sonra yüksek puanlılar düşüklerden iyi gitti mi -> 'olc')")
    if kart: kart_ciz(sonuc, g.get("tarih", ""))
    return sonuc

def kart_ciz(sonuc, tarih):
    import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
    s = sonuc[::-1]; fig, ax = plt.subplots(figsize=(9, max(3, .45 * len(s) + 1.2)), dpi=160)
    fig.patch.set_facecolor("#0f1115"); ax.set_facecolor("#0f1115")
    ax.barh([x["t"] for x in s], [x["teknik"] for x in s], color="#c9a227", label="Teknik (6)")
    ax.barh([x["t"] for x in s], [x["akis"] for x in s], left=[x["teknik"] for x in s], color="#4a90d9", label="Akış (4)")
    for i, x in enumerate(s): ax.text(10.15, i, f"{x['puan']}/10", va="center", color="white", fontsize=9, fontweight="bold")
    ax.set_xlim(0, 11); ax.tick_params(colors="#cfd3da"); [sp.set_visible(False) for sp in ax.spines.values()]
    ax.set_title(f"Kurumsal ayak izi + teknik uyum puanı  {tarih}", color="white", loc="left", fontsize=11)
    ax.legend(loc="lower right", frameon=False, labelcolor="#cfd3da", fontsize=8)
    fig.text(.99, .01, "ENES ULUDAĞ", ha="right", color="#8a8f98", fontsize=7)
    os.makedirs(os.path.join(KOK, "g"), exist_ok=True)
    yol = os.path.join(KOK, "g", f"akis_puan_{tarih}.png"); fig.savefig(yol, bbox_inches="tight", facecolor=fig.get_facecolor())
    print("Kart:", yol)

def olc():
    import pandas as pd
    if not os.path.exists(CSV): print("Kayıt yok."); return
    d = pd.read_csv(CSV); out = []
    for _, r in d.iterrows():
        try: c = cerceve(r.t)["kapanis"]
        except Exception: continue
        sonra = c[c.index > pd.Timestamp(r.tarih)]
        for u in (5, 20):
            if len(sonra) > u: out.append(dict(u=u, yuksek=r.puan >= 7, getiri=sonra.iloc[u] / r.fiyat - 1))
    if not out: print("Henüz olgunlaşmış kayıt yok (5 işlem günü gerekir)."); return
    o = pd.DataFrame(out)
    for u, gr in o.groupby("u"):
        y, d_ = gr[gr.yuksek].getiri, gr[~gr.yuksek].getiri
        print(f"{u} gün: puan>=7 n={len(y)} ort %{y.mean()*100:.2f} | puan<7 n={len(d_)} ort %{d_.mean()*100:.2f}"
              + ("  (n<10: kanıt yok)" if len(y) < 10 else ""))

if __name__ == "__main__":
    a = sys.argv[1:]
    if not a or a[0] == "sablon":
        print(json.dumps({"tarih": dt.date.today().isoformat(), "kaynak": "Unusual Whales ekran görüntüsü",
            "hisseler": {"AVGO": {"call_prim": None, "put_prim": None, "sweep_call": 0, "sweep_put": 0,
                                  "uzun_vade": False, "dp": [], "not": ""}}}, ensure_ascii=False, indent=1))
    elif a[0] == "puan": puanla(a[1], "--kart" in a)
    elif a[0] == "teknik":
        for t in a[1].split(","):
            tk = teknik(t.strip().upper()); print(f"{tk['t']} teknik {tk['teknik']}/6 ceza {tk['ceza']} | " + " | ".join(tk["notlar"]))
    elif a[0] == "olc": olc()

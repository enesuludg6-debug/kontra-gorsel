"""18:00 / 23:30 teknik kontrol otomasyonu.
Her hisse için 4 dilimde (1s/4s/G/H) 21 göstergeyi hesaplar (ta2.all_ind), destek/direnç adaylarını toplar,
en az 2 farklı gösterge/dilim çakışan bölgeleri kademe olarak seçer, gerekçeli görsel (ta_grafik) ve
tweet taslağı + 'ben olsam' notu üretir. Çıktı: /tmp/tk/<TICKER>.json + g/ta/<tarih>_<ticker>_teknik.jpg
Kullanım: python3 tk_auto.py ETIKET TICKER1 TICKER2 ...
"""
import json, os, re, sys, datetime as dt

argv = sys.argv[:]
sys.argv = [argv[0]]
import ta2  # noqa: E402  (ta2 import sırasında argüman olmadan hiçbir şey basmaz)
import ta_grafik  # noqa: E402

TF = [("1s", "60m", "60d", 1), ("4s", "60m", "180d", 4), ("G", "1d", "2y", 1), ("H", "1wk", "5y", 1)]
NUM = r"(-?\d+(?:\.\d+)?)"


def fl(x):
    return f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def analiz(tk):
    out = {"ticker": tk, "dilim": {}, "destek": [], "direnc": []}
    price = None
    for name, iv, rg, k in TF:
        r = ta2.fetch(tk, iv, rg)
        if k > 1:
            r = ta2.resample(r, k)
        try:
            L, R = ta2.all_ind(r)
        except Exception:
            out["dilim"][name] = {"yukari": 0, "asagi": 0, "notr": 0, "detay": {}, "yetersiz": True}
            continue
        if name == "1s":
            price = L
        bull = sum(1 for x in R.values() if x[1] == 1)
        bear = sum(1 for x in R.values() if x[1] == -1)
        out["dilim"][name] = {"yukari": bull, "asagi": bear, "notr": len(R) - bull - bear,
                             "detay": {kk: [R[kk][1], R[kk][2]] for kk in R}}
        def add(lo, hi, lab):
            if lo is None or hi is None:
                return
            lo, hi = min(lo, hi), max(lo, hi)
            direnc_tip = any(x in lab for x in ("bear FVG", "SAT", "son tepe"))
            destek_tip = any(x in lab for x in ("bull FVG", "AL", "son dip"))
            if direnc_tip and lo < price * 0.995:
                return
            if destek_tip and hi > price * 1.005:
                return
            (out["destek"] if hi <= price * 1.005 else out["direnc"] if lo >= price * 0.995 else out["destek"]).append(
                {"lo": lo, "hi": hi, "lab": f"{name} {lab}"})
        st = R.get("Supertrend", (0, 0, ""))[2]
        m = re.search(r"cizgi " + NUM, st)
        if m:
            add(float(m.group(1)), float(m.group(1)), "Supertrend " + ("AL" if "BUY" in st else "SAT"))
        if "EMA200" in R:
            add(R["EMA200"][0], R["EMA200"][0], "EMA 200")
        vw = R.get("VWAP20", (0, 0, ""))
        m = re.search(NUM, vw[2])
        if m:
            add(float(m.group(1)), float(m.group(1)), "VWAP")
        smc = R.get("SMC", (0, 0, ""))[2]
        for kind, a, b in re.findall(r"(bull|bear) FVG " + NUM + "-" + NUM, smc):
            add(float(a), float(b), f"{kind} FVG")
        m = re.search(r"dip " + NUM, smc)
        if m:
            add(float(m.group(1)), float(m.group(1)), "son dip")
        m = re.search(r"swing tepe " + NUM, smc)
        if m:
            add(float(m.group(1)), float(m.group(1)), "son tepe")
        m = re.search(r"OTE " + NUM + "-" + NUM, R.get("Fib", (0, 0, ""))[2])
        if m:
            add(float(m.group(1)), float(m.group(2)), "Fib OTE")
        m = re.search(r"POC " + NUM + " VA " + NUM + "-" + NUM, R.get("VolProfile", (0, 0, ""))[2])
        if m:
            add(float(m.group(1)), float(m.group(1)), "VP POC")
            add(float(m.group(2)), float(m.group(2)), "VP değer alanı altı")
        m = re.search(r"bulut " + NUM + "-" + NUM, R.get("Ichimoku", (0, 0, ""))[2])
        if m:
            add(float(m.group(1)), float(m.group(2)), "Ichimoku bulutu")
        if name == "G":
            out["atr"] = R["ATR"][0]
    out["fiyat"] = price
    return out


def kumele(items, price, yon):
    # dar bölgeleri (geniş OTE/VA hariç) kümeler; en az 2 farklı etiket çakışırsa bölge
    pts = []
    for it in items:
        w = (it["hi"] - it["lo"]) / price
        if w > 0.12:  # çok geniş aralıklar (ör. haftalık OTE) yalnız "içinde" bilgisi olarak kullanılır
            continue
        pts.append(it)
    pts.sort(key=lambda x: -(x["lo"] + x["hi"]) / 2 if yon == "destek" else (x["lo"] + x["hi"]) / 2)
    zones = []
    for it in pts:
        mid = (it["lo"] + it["hi"]) / 2
        for z in zones:
            if abs(mid - z["mid"]) / price <= 0.03:
                z["items"].append(it)
                z["lo"] = min(z["lo"], it["lo"]); z["hi"] = max(z["hi"], it["hi"])
                z["mid"] = (z["lo"] + z["hi"]) / 2
                break
        else:
            zones.append({"lo": it["lo"], "hi": it["hi"], "mid": mid, "items": [it]})
    for z in zones:
        z["n"] = len({i["lab"] for i in z["items"]})
        geniş = [i for i in items if (i["hi"] - i["lo"]) / price > 0.12 and i["lo"] <= z["mid"] <= i["hi"]]
        z["ek"] = [i["lab"] for i in geniş]
    return zones


def plan(a):
    p = a["fiyat"]
    ds = [z for z in kumele(a["destek"], p, "destek") if z["n"] >= 2]
    ds.sort(key=lambda z: -z["mid"])
    dr = [z for z in kumele(a["direnc"], p, "direnc") if z["n"] >= 1 and z["lo"] > p * 1.01]
    dr.sort(key=lambda z: z["mid"])
    k1 = ds[0] if ds else None
    k2 = next((z for z in ds[1:] if k1 and z["hi"] < k1["lo"] * 0.985), None)
    dips = sorted([i["lo"] for i in a["destek"] if "son dip" in i["lab"] and i["lo"] < (k2 or k1 or {"lo": p})["lo"]], reverse=True)
    base = (k2 or k1)
    tez = dips[0] if dips else (base["lo"] - 1.0 * a.get("atr", 0) if base else None)
    hedef = dr[0] if dr else None
    hedef2 = dr[1] if len(dr) > 1 else None
    g, h = a["dilim"]["G"], a["dilim"]["H"]
    s4, s1 = a["dilim"]["4s"], a["dilim"]["1s"]
    if g["yukari"] > g["asagi"] and s4["yukari"] > s4["asagi"]:
        bakis = "trend yukarı dönmüş, geri çekilmeler alım bölgesi"
    elif k1 and k1["lo"] <= p <= k1["hi"] * 1.02 and g["asagi"] > g["yukari"] + 10:
        bakis = "düşüş trendi güçlü ama fiyat destek bölgesine geldi"
    elif k1 and k1["lo"] <= p <= k1["hi"] * 1.02:
        bakis = "dibe yakın, destek bölgesinde"
    elif g["asagi"] > g["yukari"] + 5:
        bakis = "daha dip arıyor, düşüş trendi sürüyor"
    else:
        bakis = "kararsız, yön belirlemesini bekliyor"
    return {"k1": k1, "k2": k2, "tez": tez, "hedef": hedef, "hedef2": hedef2, "bakis": bakis}


def neden(z, n=4):
    labs = []
    for i in z["items"]:
        if i["lab"] not in labs:
            labs.append(i["lab"])
    s = " + ".join(labs[:n])
    if z.get("ek"):
        s += " (ayrıca " + ", ".join(z["ek"][:2]) + " içinde)"
    return s


SADE = {"bull FVG": "doldurulmamış boşluk", "bear FVG": "üstte boşluk/direnç", "Supertrend AL": "trend göstergesi desteği",
        "Supertrend SAT": "trend göstergesi direnci", "EMA 200": "200'lük ortalama", "VWAP": "hacim ağırlıklı ortalama",
        "son dip": "son dip", "son tepe": "son tepe", "VP POC": "en çok işlem gören fiyat", "VP değer alanı altı": "hacim bölgesinin alt sınırı",
        "Ichimoku bulutu": "Ichimoku bulutu", "Fib OTE": "geri çekilmenin ideal bölgesi"}
DIL = {"1s": "1 saatlikte", "4s": "4 saatlikte", "G": "günlükte", "H": "haftalıkta"}


def sade(z, n=3):
    out = []
    for i in z["items"]:
        d, lab = i["lab"].split(" ", 1)
        t = f"{DIL[d]} {SADE.get(lab, lab)}"
        if t not in out:
            out.append(t)
    return ", ".join(out[:n])


def aralik(z):
    return f"{fl(z['lo'])} civarından" if abs(z['hi'] - z['lo']) / z['lo'] < 0.004 else f"{fl(z['lo'])}-{fl(z['hi'])} arasından"


def tweet(tk, a, pl):
    p = a["fiyat"]
    t = [f"${tk} bence {pl['bakis']}. Fiyat şu an {fl(p)} dolar."]
    if not pl["k1"]:
        t.append("Şu an en az iki göstergenin çakıştığı net bir alım bölgesi göremiyorum, ben acele etmem.")
    if pl["k1"]:
        t.append(f"Ben {aralik(pl['k1'])} bir kademe eklerim. Sebebi: {sade(pl['k1'])} burada üst üste geliyor.")
    if pl["k2"]:
        t.append(f"Orayı aşağı kırarsa {aralik(pl['k2'])} bir kademe daha eklerim ({sade(pl['k2'], 2)}).")
    if pl["tez"]:
        t.append(f"{fl(pl['tez'])} altında kapanış olursa benim için hikaye değişir.")
    if pl["hedef"]:
        t.append(f"Yukarıda ilk engel {fl(pl['hedef']['mid'])} civarı.")
    return " ".join(t[:1]) + "\n\n" + " ".join(t[1:3]) + ("\n\n" + " ".join(t[3:]) if len(t) > 3 else "")


def main():
    etiket = argv[1]
    os.makedirs("/tmp/tk", exist_ok=True)
    tarih = dt.datetime.now().strftime("%Y%m%d")
    for tk in argv[2:]:
        try:
            a = analiz(tk)
            pl = plan(a)
            res = {"ticker": tk, "fiyat": a["fiyat"], "bakis": pl["bakis"],
                   "dilim": {k: {x: v[x] for x in ("yukari", "asagi", "notr")} for k, v in a["dilim"].items()},
                   "k1": pl["k1"] and {"lo": pl["k1"]["lo"], "hi": pl["k1"]["hi"], "neden": neden(pl["k1"])},
                   "k2": pl["k2"] and {"lo": pl["k2"]["lo"], "hi": pl["k2"]["hi"], "neden": neden(pl["k2"])},
                   "tez": pl["tez"], "hedef": pl["hedef"] and {"mid": pl["hedef"]["mid"], "neden": neden(pl["hedef"])},
                   "hedef2": pl["hedef2"] and {"mid": pl["hedef2"]["mid"], "neden": neden(pl["hedef2"])},
                   "tweet": tweet(tk, a, pl)}
            bolgeler, cizgiler, etik = [], [], []
            if pl["k1"]:
                bolgeler.append((pl["k1"]["lo"], pl["k1"]["hi"], "al")); etik.append((pl["k1"]["mid"], "al", f"1. kademe {fl(pl['k1']['lo'])}-{fl(pl['k1']['hi'])}: {neden(pl['k1'], 2)}"))
            if pl["k2"]:
                bolgeler.append((pl["k2"]["lo"], pl["k2"]["hi"], "al")); etik.append((pl["k2"]["mid"], "al", f"2. kademe {fl(pl['k2']['lo'])}-{fl(pl['k2']['hi'])}: {neden(pl['k2'], 2)}"))
            if pl["tez"]:
                cizgiler.append((pl["tez"], "sat", "-")); etik.append((pl["tez"], "sat", f"Tez bozulur: {fl(pl['tez'])} altı kapanış"))
            if pl["hedef"]:
                bolgeler.append((pl["hedef"]["lo"], pl["hedef"]["hi"], "direnc")); etik.append((pl["hedef"]["mid"], "sat", f"İlk engel ~{fl(pl['hedef']['mid'])}: {neden(pl['hedef'], 2)}"))
            etik.append((a["fiyat"], "fiyat", f"● Fiyat {fl(a['fiyat'])}"))
            ys = [a["fiyat"]] + [x[0] for x in etik]
            lo_, hi_ = min(ys), max(ys)
            pad = (hi_ - lo_) * 0.25 + a["fiyat"] * 0.03
            gd = a["dilim"]
            notlar = [f"Günlük {gd['G']['yukari']}↑ {gd['G']['asagi']}↓ | Haftalık {gd['H']['yukari']}↑ {gd['H']['asagi']}↓",
                      f"4 saatlik {gd['4s']['yukari']}↑ {gd['4s']['asagi']}↓ | 1 saatlik {gd['1s']['yukari']}↑ {gd['1s']['asagi']}↓",
                      "OBV: hacim akışı"]
            out = f"g/ta/{tarih}_{etiket}_{tk.lower()}_teknik.jpg"
            ta_grafik.ciz(tk, pl["bakis"][:1].upper() + pl["bakis"][1:], bolgeler, cizgiler, etik, notlar, a["fiyat"], out,
                          ylim=(lo_ - pad, hi_ + pad), N=90, tarih=dt.datetime.now().strftime("%d.%m.%Y"),
                          kaynak_notu="Veri: Yahoo Finance (gün içi) • 21 gösterge x 4 dilim, kendi hesabım")
            res["gorsel"] = out
            json.dump(res, open(f"/tmp/tk/{tk}.json", "w"), ensure_ascii=False, indent=1)
            print("OK", tk, round(a["fiyat"], 2), pl["bakis"], "| k1", res["k1"] and (round(res["k1"]["lo"], 2), round(res["k1"]["hi"], 2)),
                  "| k2", res["k2"] and (round(res["k2"]["lo"], 2), round(res["k2"]["hi"], 2)), "| tez", res["tez"] and round(res["tez"], 2),
                  "| hedef", res["hedef"] and round(res["hedef"]["mid"], 2))
        except Exception as e:
            print("HATA", tk, e)


if __name__ == "__main__":
    main()

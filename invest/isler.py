#!/usr/bin/env python3
"""İŞ DEFTERİ (kesin kural 43): sohbetler arası kaybolmaması gereken her tek seferlik iş burada.
Sohbet değişince yeni sohbet bu defterden açık işleri okur ve görevlerini yeniden kurar; hafızaya güvenilmez.

Komutlar:
  python3 isler.py liste [--hepsi]              açık işler (bekliyor/kuruldu), zamana göre
  python3 isler.py kontrol                      zamanı geçmiş ama yapılmamış işler (EKSİK)
  python3 isler.py devir                        yeni sohbette kurulacak görevler (zamanı gelmemiş açık işler + geçmişte kalıp yapılmamışlar)
  python3 isler.py ekle <id> "<ad>" <YYYY-MM-DDTHH:MM> "<ne yapılacak>" [--ticker T] [--tur X]
  python3 isler.py durum <id> <bekliyor|kuruldu|yapildi|iptal|atlandi> [--not "..."] [--trigger trig_x] [--soz "Enes'in aynen sözü (iptal için zorunlu)"]
  python3 isler.py bilanco <TICKER> <YYYY-MM-DDTHH:MM açıklama TSİ> <acilis_oncesi|kapanis_sonrasi> ["görüşme saati HH:MM"]
      → standart bilanço adımlarını ekler: opsiyon (kural 39), hazirlik (T-60), yayin (T-2), analiz (+15 dk),
        detay (+30 dk, beklemeden, kural 41), cagri (kural 40), beklenen_hareket (ilk açılış +15 dk, kural 22n)
"""
import json, sys, datetime as dt, os, signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)

YOL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "is_defteri.json")
TZ = dt.timezone(dt.timedelta(hours=3))


def yukle():
    try:
        return json.load(open(YOL, encoding="utf-8"))
    except FileNotFoundError:
        return {"isler": []}


def kaydet(d):
    d["isler"].sort(key=lambda i: i["zaman"])
    json.dump(d, open(YOL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


def simdi():
    return dt.datetime.now(TZ)


def zaman(s):
    return dt.datetime.fromisoformat(s).replace(tzinfo=TZ)


def bul(d, i):
    for x in d["isler"]:
        if x["id"] == i:
            return x
    return None


def ekle(d, i, ad, z, ne, ticker="", tur="tek", durum="bekliyor", notu=""):
    if bul(d, i):
        return False
    d["isler"].append({"id": i, "ad": ad, "zaman": z, "ne": ne, "ticker": ticker, "tur": tur,
                       "durum": durum, "not": notu, "trigger": "", "soz": "", "guncelleme": simdi().strftime("%d.%m %H:%M")})
    return True


def acik(x):
    return x["durum"] in ("bekliyor", "kuruldu")


def satir(x):
    return f'{x["zaman"].replace("T"," ")}  [{x["durum"]:8}] {x["id"]:28} {x["ad"]}  — {x["ne"][:150]}' + (f'  (not: {x["not"][:80]})' if x["not"] else "")


def acilis_sonrasi(t):
    """bilançodan sonraki ilk ABD açılışı +15 dk (TSİ 17:45; hafta sonu atlanır)"""
    g = t
    if t.hour >= 17 or (t.hour == 17 and t.minute >= 30):
        g = t + dt.timedelta(days=1)
    while g.weekday() >= 5:
        g += dt.timedelta(days=1)
    return g.replace(hour=17, minute=45, second=0, microsecond=0)


def bilanco(d, T, z, tip, gorusme=None):
    t = zaman(z)
    f = lambda x: x.strftime("%Y-%m-%dT%H:%M")
    adimlar = [
        ("opsiyon", f"Opsiyon: {T}", t - dt.timedelta(hours=6) if tip == "kapanis_sonrasi" else t.replace(hour=11, minute=0),
         "Kural 39: opsiyonların fiyatladığı hareket (±%, 2 kaynak) açıklamadan önce en az bir tweette; DONGU '- OPSIYON: T'"),
        ("hazirlik", f"Hazırlık: {T}", t - dt.timedelta(minutes=60), "Kural 16: beklentiler 2 kaynak, CRWV iskeleti, /tmp/hazir_T.py kart, bülten URL'leri"),
        ("yayin", f"Yayın: {T} bilanço", t - dt.timedelta(minutes=2), "Kural 16 + O-011: rakam tweeti tam CRWV formatı, 3-5 dk içinde; Yahoo canlı blog/CNBC yedek"),
        ("analiz", f"Analiz: {T} bilanço", t + dt.timedelta(minutes=15), "Kural 25: kapsamlı analiz tweeti"),
        ("detay", f"Detay: {T}", t + dt.timedelta(minutes=30), "Kural 41: belgeden 2-7 AYRI detay tweeti, BEKLEMEDEN (gece dahil), aralık serbest"),
    ]
    if tip == "acilis_oncesi":
        gz = t.replace(hour=int(gorusme.split(':')[0]), minute=int(gorusme.split(':')[1])) if gorusme else t + dt.timedelta(minutes=90)
        adimlar.append(("cagri", f"Çağrı: {T}", gz + dt.timedelta(hours=2), "Kural 40: görüşme önemli yerleri, AYNI GÜN, her konu ayrı tweet"))
    else:
        sabah = (t if t.hour < 9 else t + dt.timedelta(days=1)).replace(hour=11, minute=40)
        adimlar.append(("cagri", f"Çağrı: {T}", sabah, "Kural 40: görüşme önemli yerleri, gece bilançosunda AYNI SABAH, her konu ayrı tweet"))
    adimlar.append(("beklenen", f"Beklenen hareket: {T}", acilis_sonrasi(t), "Kural 22n/39: opsiyon fiyatlaması vs açılıştaki gerçek hareket"))
    n = 0
    for k, ad, zz, ne in adimlar:
        n += ekle(d, f"{T}-{t.strftime('%m%d')}-{k}", ad, f(zz), ne, ticker=T, tur="bilanco")
    return n


def main(a):
    d = yukle()
    if not a or a[0] == "liste":
        hepsi = "--hepsi" in a
        for x in d["isler"]:
            if hepsi or acik(x):
                print(satir(x))
        return
    if a[0] == "kontrol":
        n = simdi()
        ek = [x for x in d["isler"] if acik(x) and zaman(x["zaman"]) < n - dt.timedelta(minutes=10)]
        for x in ek:
            print("  EKSIK IS:", satir(x))
        if not ek:
            print("  acik is gecikmesi yok")
        return
    if a[0] == "devir":
        n = simdi()
        print("# Yeni sohbette kurulacak/yapılacak işler (kural 43). Zamanı geçenleri hemen yap ya da Enes'e sor; kalanlara send_later kur ve `durum <id> kuruldu --trigger <id>` yaz.")
        for x in d["isler"]:
            if acik(x):
                etiket = "GECIKMIS" if zaman(x["zaman"]) < n else "KUR"
                print(f"{etiket:8} {satir(x)}")
        print("# İPTAL edilenler (Enes'in sözüyle):")
        for x in d["isler"]:
            if x["durum"] == "iptal":
                print(f'         {x["id"]}: {x["soz"] or x["not"]}')
        return
    if a[0] == "ekle":
        i, ad, z, ne = a[1], a[2], a[3], a[4]
        # KURAL 76 (F-006): zaman alani dogrulanir; ad/zaman yer degistirmisse duzeltir, degilse reddeder
        def _tarih(v):
            try:
                dt.datetime.fromisoformat(v.strip().replace(" ", "T")); return True
            except Exception:
                return False
        if not _tarih(z) and _tarih(ad):
            ad, z = z, ad
            print("UYARI kural 76: ad ve zaman yer degistirmisti, duzeltildi")
        if not _tarih(z):
            print("HATA kural 76: zaman YYYY-AA-GGTSS:DD olmali. Dogru sira: isler.py ekle <ID> \"<ad>\" <YYYY-AA-GGTSS:DD> \"<ne>\" [--ticker T] [--tur tur|test|tek]")
            sys.exit(1)
        z = z.strip().replace(" ", "T")[:16]
        ticker = a[a.index("--ticker") + 1] if "--ticker" in a else ""
        tur = a[a.index("--tur") + 1] if "--tur" in a else "tek"
        print("eklendi" if ekle(d, i, ad, z, ne, ticker, tur) else "zaten var")
        kaydet(d)
        return
    if a[0] == "durum":
        x = bul(d, a[1])
        if not x:
            sys.exit(f"yok: {a[1]}")
        yeni = a[2]
        soz = a[a.index("--soz") + 1] if "--soz" in a else ""
        if yeni == "iptal" and not soz:
            sys.exit("iptal için --soz \"Enes'in aynen sözü\" zorunlu (kural 43: en dar yorum)")
        x["durum"] = yeni
        if "--not" in a:
            x["not"] = a[a.index("--not") + 1]
        if "--trigger" in a:
            x["trigger"] = a[a.index("--trigger") + 1]
        if soz:
            x["soz"] = soz
        x["guncelleme"] = simdi().strftime("%d.%m %H:%M")
        kaydet(d)
        print(satir(x))
        return
    if a[0] == "bilanco":
        n = bilanco(d, a[1], a[2], a[3], a[4] if len(a) > 4 else None)
        kaydet(d)
        print(f"{n} adım eklendi")
        return
    sys.exit(__doc__)


if __name__ == "__main__":
    main(sys.argv[1:])

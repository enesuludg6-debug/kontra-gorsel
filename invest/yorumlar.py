#!/usr/bin/env python3
"""YORUM DEFTERİ (kural 66 + 86-g; Enes 25.11 18:26: 'sık sohbet/hesap değiştiriyorum').
Ölçülebilir her yorum ve sonucu REPODA durur; hangi sohbet ya da hesap olursa olsun karne buradan yazılır.
Sohbet geçmişine, send_later'a ya da hafızaya güvenilmez.

  python3 invest/yorumlar.py ekle <ID> <tweet GG.AA SS:DD> <buffer_id> "<yorum, tek cümle>" "<eşik/ölçüt>" <kontrol YYYY-AA-GG>
  python3 invest/yorumlar.py sonuc <ID> <tuttu|tutmadi|kismen|olcülemedi> "<tek rakamla ne oldu>"
  python3 invest/yorumlar.py bekleyen          kontrol tarihi gelmiş/geçmiş ama sonucu yazılmamış yorumlar
  python3 invest/yorumlar.py karne [gun=7]     son N günde sonucu 'tuttu' olanlar (karne tweeti yalnız bunlardan)
  python3 invest/yorumlar.py liste
"""
import json, os, sys, datetime as dt
F = os.path.join(os.path.dirname(os.path.abspath(__file__)), "yorum_defteri.json")
TZ = dt.timezone(dt.timedelta(hours=3))

def yukle():
    try: return json.load(open(F, encoding="utf-8"))
    except FileNotFoundError: return []

def kaydet(d): json.dump(d, open(F, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

def main(a):
    d = yukle(); bugun = dt.datetime.now(TZ).date()
    k = a[0] if a else "liste"
    if k == "ekle":
        i, tw, bid, yorum, esik, kontrol = a[1:7]
        if any(x["id"] == i for x in d): print("zaten var"); return
        d.append({"id": i, "tweet": tw, "buffer": bid, "yorum": yorum, "esik": esik, "kontrol": kontrol, "sonuc": "", "ne_oldu": "", "sonuc_tarih": ""})
        kaydet(d); print("eklendi", i); return
    if k == "sonuc":
        for x in d:
            if x["id"] == a[1]:
                x["sonuc"], x["ne_oldu"], x["sonuc_tarih"] = a[2], (a[3] if len(a) > 3 else ""), bugun.isoformat()
                kaydet(d); print(x["id"], x["sonuc"], x["ne_oldu"]); return
        sys.exit("yok: " + a[1])
    if k == "bekleyen":
        for x in d:
            if not x["sonuc"] and dt.date.fromisoformat(x["kontrol"]) <= bugun:
                print(f'BEKLEYEN {x["id"]} (kontrol {x["kontrol"]}): {x["yorum"]} | eşik: {x["esik"]}')
        return
    if k == "karne":
        gun = int(a[1]) if len(a) > 1 else 7
        t = [x for x in d if x["sonuc"] == "tuttu" and x["sonuc_tarih"] and (bugun - dt.date.fromisoformat(x["sonuc_tarih"])).days < gun]
        print(f"# Son {gun} günde TUTAN yorumlar ({len(t)}). Tutan 2'den azsa karne atılmaz. Tutmayanlar yazılmaz.")
        for x in t: print(f'{x["tweet"][:5]} • {x["id"]} • {x["yorum"]} • {x["ne_oldu"]}')
        return
    for x in d: print(f'{x["id"]:22} {x["kontrol"]}  [{x["sonuc"] or "bekliyor"}]  {x["yorum"][:80]}')

if __name__ == "__main__":
    main(sys.argv[1:])

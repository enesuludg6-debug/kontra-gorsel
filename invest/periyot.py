#!/usr/bin/env python3
"""PERIYOT DEFTERI (kesin kural 24). Sohbet degisse de "en son ne zaman yapildi / kac kez yapildi"
bilgisi hafizada degil burada tutulur. Tarihler Europe/Istanbul.

Kullanim:
  python3 periyot.py durum               # bugun yapilabilir / yapilmali / yasak olanlar
  python3 periyot.py kontrol <anahtar>   # tek is: UYGUN / BEKLE (sebep) ; cikis kodu 0 = uygun
  python3 periyot.py yap <anahtar> [not] # isi yaptin: tarihi kaydeder (sonra commit + push)
  python3 periyot.py sozluk <Veri> [A|B] # sozluk cumlesi secimi: 14 gunde tekrar etmeyen varyasyonu verir
  python3 periyot.py ekle <anahtar> <tur> <deger> "<aciklama>"   # yeni periyodik is
  python3 periyot.py etiket kontrol <grup> <deger> <gun> [son_n]  # "bu deger son <gun> gunde / son <son_n> kayitta kullanildi mi" (0=uygun)
  python3 periyot.py etiket yap <grup> <deger>                    # kullanimi kaydet (ornek: aday TSM, cerceve B, uzun_ticker NBIS)
  python3 periyot.py etiket liste <grup> [n]                      # son n kayit

Kural turleri (periyot.json "isler"):
  min_gun N        : son yapilistan en az N gun gecmeli (ornek 21 = uc haftada bir)
  gunluk_max N     : ayni takvim gununde en fazla N
  haftalik_min/max : Pazartesi-Pazar haftasinda adet (min gerideyse 'yapilmali' der)
  aylik_min/max    : takvim ayinda adet
  ayin_pazari K    : ayin K. Pazari (1 = ilk Pazar); ayni ay bir kez
  baslangic_gun N  : "baslangic" tarihinden N gun sonra acilir (ornek 3 haftalik veri)
  her_n S          : "sayac" anahtarindaki olay her S adette bir (ornek 5 karnede bir kalibrasyon)
"""
import json, sys, datetime as dt
from zoneinfo import ZoneInfo
P = __file__.rsplit("/", 1)[0] + "/periyot.json"
TZ = ZoneInfo("Europe/Istanbul")

def yukle(): return json.load(open(P, encoding="utf-8"))
def kaydet(d): json.dump(d, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
def bugun(): return dt.datetime.now(TZ).date()
def tarih(s): return dt.date.fromisoformat(s[:10])

def kayitlar(d, k): return [tarih(x["t"]) for x in d["kayit"].get(k, [])]

def degerlendir(d, k, g=None):
    g = g or bugun(); i = d["isler"][k]; ks = kayitlar(d, k); son = max(ks) if ks else None
    pzt = g - dt.timedelta(days=g.weekday())
    if "min_gun" in i and son and (g - son).days < i["min_gun"]:
        return "BEKLE", f"son {son}, {i['min_gun']} gun dolmadi (sonraki {son + dt.timedelta(days=i['min_gun'])})"
    if "gunluk_max" in i and sum(1 for x in ks if x == g) >= i["gunluk_max"]:
        return "BEKLE", f"bugun {i['gunluk_max']} kez yapildi"
    hf = sum(1 for x in ks if pzt <= x <= g)
    if "haftalik_max" in i and hf >= i["haftalik_max"]:
        return "BEKLE", f"bu hafta {hf}/{i['haftalik_max']}"
    ay = sum(1 for x in ks if (x.year, x.month) == (g.year, g.month))
    if "aylik_max" in i and ay >= i["aylik_max"]:
        return "BEKLE", f"bu ay {ay}/{i['aylik_max']}"
    if "ayin_pazari" in i:
        K = i["ayin_pazari"]
        if g.weekday() != 6 or (g.day - 1) // 7 + 1 != K: return "BEKLE", f"bugun ayin {K}. Pazari degil"
        if ay: return "BEKLE", "bu ay yapildi"
    if "baslangic_gun" in i:
        acilis = tarih(i["baslangic"]) + dt.timedelta(days=i["baslangic_gun"])
        if g < acilis: return "BEKLE", f"{acilis} tarihinde acilir"
    if "her_n" in i:
        n = len(d["kayit"].get(i["sayac"], [])); son_n = i.get("son_sayac", 0)
        if n - son_n < i["her_n"]: return "BEKLE", f"{i['sayac']} {n - son_n}/{i['her_n']}"
    # yapilmali mi (alt sinir geride)
    if "haftalik_min" in i and hf < i["haftalik_min"]:
        kalan = 7 - g.weekday()  # bugun dahil
        acil = (i["haftalik_min"] - hf) * max(1, i.get("min_gun", 1)) >= kalan
        return "UYGUN", ("ACIL BUGUN YAP: " if acil else "YAPILMALI: ") + f"bu hafta {hf}/{i['haftalik_min']} (bugun dahil kalan gun {kalan})"
    if "aylik_min" in i and ay < i["aylik_min"]:
        return "UYGUN", f"YAPILMALI: bu ay {ay}/{i['aylik_min']}"
    return "UYGUN", f"son {son or '-'}"

def main(a):
    d = yukle(); c = a[0] if a else "durum"
    if c == "durum":
        print(f"PERIYOT {bugun()} ({['Pzt','Sal','Car','Per','Cum','Cmt','Paz'][bugun().weekday()]})")
        for k, i in d["isler"].items():
            s, n = degerlendir(d, k); print(f"  {s:5} {k:22} {n}  | {i['aciklama']}")
    elif c == "kontrol":
        s, n = degerlendir(d, a[1]); print(s, n); sys.exit(0 if s == "UYGUN" else 1)
    elif c == "yap":
        k = a[1]; assert k in d["isler"] or k.startswith("sozluk:"), "bilinmeyen anahtar: " + k
        d["kayit"].setdefault(k, []).append({"t": dt.datetime.now(TZ).strftime("%Y-%m-%d %H:%M"), "not": " ".join(a[2:])})
        i = d["isler"].get(k, {})
        if "her_n" in i: i["son_sayac"] = len(d["kayit"].get(i["sayac"], []))
        kaydet(d); print("kaydedildi", k)
    elif c == "sozluk":
        veri = a[1]; ister = a[2] if len(a) > 2 else None; g = bugun(); uygun = []
        for v in ([ister] if ister else ["A", "B"]):
            ks = kayitlar(d, f"sozluk:{veri}-{v}"); son = max(ks) if ks else None
            if not son or (g - son).days >= 14: uygun.append((son or dt.date(2000, 1, 1), v))
        if not uygun: print("BEKLE: iki varyasyon da son 14 gunde kullanildi -> sozluk cumlesi koyma"); sys.exit(1)
        v = min(uygun)[1]; print(f"KULLAN: {veri}-{v}  (kullaninca: python3 periyot.py yap sozluk:{veri}-{v})")
    elif c == "etiket":
        alt, grup = a[1], a[2]; E = d.setdefault("etiket", {}).setdefault(grup, [])
        if alt == "yap":
            E.append({"t": dt.datetime.now(TZ).strftime("%Y-%m-%d %H:%M"), "v": a[3]}); kaydet(d); print("kaydedildi", grup, a[3])
        elif alt == "liste":
            n = int(a[3]) if len(a) > 3 else 10
            for x in E[-n:]: print(x["t"], x["v"])
        elif alt == "kontrol":
            deger, gun = a[3], int(a[4]); son_n = int(a[5]) if len(a) > 5 else 0; g = bugun()
            yakin = [x for x in E if x["v"] == deger and (g - tarih(x["t"])).days < gun]
            sonlar = [x["v"] for x in E[-son_n:]] if son_n else []
            if yakin: print(f"BEKLE: {deger} {tarih(yakin[-1]['t'])} tarihinde kullanildi ({gun} gun dolmadi)"); sys.exit(1)
            if deger in sonlar: print(f"BEKLE: {deger} son {son_n} kayitta var: {sonlar}"); sys.exit(1)
            print("UYGUN", deger)
    elif c == "ekle":
        k, tur, deger, ac = a[1], a[2], a[3], a[4]
        d["isler"][k] = {tur: int(deger) if deger.isdigit() else deger, "aciklama": ac}; kaydet(d); print("eklendi", k)
    else: print(__doc__)

if __name__ == "__main__": main(sys.argv[1:])

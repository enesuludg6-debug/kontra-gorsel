#!/usr/bin/env python3
"""SABIT GOREV ZINCIRI (kesin kural 29): her sabit gorev bu sohbette send_later zinciridir; calisinca ILK IS bir sonrakini kurar.
Kullanim: python3 invest/sonraki.py <anahtar>   -> send_later 'at' degeri (2026-11-18T18:00:00[Europe/Istanbul]) + ad + mesaj
          python3 invest/sonraki.py hepsi       -> tum gorevlerin sonraki zamani
"""
import sys, datetime as dt
from zoneinfo import ZoneInfo
TZ = ZoneInfo("Europe/Istanbul")
# anahtar: (ad, tur, saat, ek)  tur: gunluk | hafta_ici | haftalik(gun 0=Pzt..6=Paz) | ay_ilk7 | yillik([(ay,gun),...])
G = {
 "sabah":       ("Sabit: sabah kontrolü 09:00", "gunluk", "09:00", None),
 "keylevels":   ("Sabit: key levels 10:30", "hafta_ici", "10:30", None),
 "radar":       ("Sabit: içeriden alım radarı 14:20", "hafta_ici", "14:20", None),
 "teknik1800":  ("Sabit: teknik kontrol 18:00", "hafta_ici", "18:00", None),
 "teknik2330":  ("Sabit: teknik kontrol 23:30", "hafta_ici", "23:30", None),
 "haftalikozet":("Sabit: haftalık özet Cmt 10:55", "haftalik", "10:55", 5),
 "sektor":      ("Sabit: sektör ısı haritası Cmt 13:25", "haftalik", "13:25", 5),
 "ilgisira":    ("Sabit: ilgi listesi sıralama Cmt 16:25", "haftalik", "16:25", 5),
 "analist":     ("Sabit: analist özeti / değerleme Paz 12:25", "haftalik", "12:25", 6),
 "sezon":       ("Sabit: bilanço sezonu karnesi Paz 14:25", "haftalik", "14:25", 6),
 "takvim":      ("Sabit: haftalık takvim Paz 20:00", "haftalik", "20:00", 6),
 "performans":  ("Sabit: performans raporu Paz 21:30", "haftalik", "21:30", 6),
 "ayinozeti":   ("Sabit: ayın özeti + mevsimsellik 10:55", "ay_ilk7", "10:55", None),
 "13f":         ("Sabit: 13F serisi başlangıcı 09:05", "yillik", "09:05", [(2, 15), (5, 16), (8, 15), (11, 15)]),
}
def sonraki(k, simdi=None):
    ad, tur, saat, ek = G[k]; s = simdi or dt.datetime.now(TZ); h, m = map(int, saat.split(":"))
    for i in range(0, 400):
        g = (s + dt.timedelta(days=i)).date(); t = dt.datetime(g.year, g.month, g.day, h, m, tzinfo=TZ)
        if t <= s + dt.timedelta(minutes=2): continue
        if tur == "gunluk" or (tur == "hafta_ici" and g.weekday() < 5) or (tur == "haftalik" and g.weekday() == ek) \
           or (tur == "ay_ilk7" and g.day <= 7) or (tur == "yillik" and (g.month, g.day) in ek):
            return t
def mesaj(k, H="A"):
    return (f"HESAP={H}. Önce invest/AKTIF_HESAP.md oku; AKTIF: {H} değilse hiçbir şey yapma (tweet ve push yok) ve bu görevi kapat. "
            f"SABİT GÖREV ZİNCİRİ ({G[k][0]}, kesin kural 29). İLK İŞ: `python3 invest/sonraki.py {k}` çalıştır ve verdiği zamana, verdiği ad ve "
            f"BU MESAJIN AYNISIYLA send_later kur (list_triggers'ta aynı adlı bekleyen varsa kurma). SONRA invest/gorevler/_ORTAK.md ve invest/gorevler/{k}.md dosyalarını oku ve harfiyen uygula. "
            f"Bütün mesajlar bu sohbete (SendUserMessage / SendUserFile).")
if __name__ == "__main__":
    a = sys.argv[1] if len(sys.argv) > 1 else "hepsi"
    for k in (G if a == "hepsi" else [a]):
        t = sonraki(k); print(f"{k}\tat={t.strftime('%Y-%m-%dT%H:%M:00')}[Europe/Istanbul]\tad={G[k][0]}")
        if a != "hepsi": print("mesaj=" + mesaj(k))

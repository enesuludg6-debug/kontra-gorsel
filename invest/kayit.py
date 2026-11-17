#!/usr/bin/env python3
"""TWEET SONRASI TEK CAGRI KAYIT (kesin kural 28, tasarruf). Kurallari DEGISTIRMEZ; tweetten sonraki kayit adimlarini tek komutta yapar:
DURUM.md hak sayaci (varsa) + KULLANILAN + 'Son 3 duzen' + DONGU satiri + performans.md + performans_veri.csv + (istenirse) periyot kaydi + commit + push.

Kullanim:
  python3 invest/kayit.py --saat 17:36 --tur MAKRO-YORUM --konu "Perakende yorum" --duzen uclu \
     --buffer 6afc... --dosya 20261117_1740_x.jpg --gorus evet --dongu "kaynaklar, rakamlar..." \
     [--hak serbest|ayrilan|yok] [--periyot sozluk:Perakende-B] [--kaynak sistem|enes]
--hak: bugunluk sayac varsa 'serbest' ya da 'ayrilan' 1 dusurur; 'yok' dokunmaz (varsayilan: sayac varsa dusur).
"""
import argparse, re, subprocess, datetime as dt, os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
a = argparse.ArgumentParser()
for k in ["saat", "tur", "konu", "duzen", "buffer", "dosya", "dongu"]: a.add_argument("--" + k, required=True)
a.add_argument("--gorus", default="evet"); a.add_argument("--hak", default="otomatik"); a.add_argument("--periyot", default="")
a.add_argument("--kaynak", default="sistem"); a.add_argument("--mesaj", default="")
x = a.parse_args()
bugun = dt.datetime.now(dt.timezone(dt.timedelta(hours=3)))
gun = bugun.strftime("%d.%m"); iso = bugun.strftime("%Y-%m-%d")

s = open("DURUM.md", encoding="utf-8").read(); kalan = None
m = re.search(r"KALAN TWEET HAKKI = (\d+)", s)
blok = re.search(r"BUGÜNLÜK KURAL \(Enes (\d\d\.\d\d)", s)
pgun = (bugun - dt.timedelta(hours=2)).strftime("%d.%m")  # paylasim gunu 02:00'de biter (kural 42)
if m and blok and blok.group(1) != pgun: m = None  # 17.11 22:00: eski gunun sayaci dusurulmez
if m and x.hak != "yok":
    kalan = max(0, int(m.group(1)) - 1)
    s = s.replace(m.group(0), f"KALAN TWEET HAKKI = {kalan}", 1)
    s = re.sub(r"(- KULLANILAN \([^)]*\): )(.*)", lambda q: q.group(1) + (q.group(2).rstrip("-").rstrip() + ", " if q.group(2).strip() not in ("-", "") else "") + f"{x.saat} {x.konu}" + (f" ({x.hak})" if x.hak in ("serbest", "ayrilan") else ""), s, count=1)
m3 = re.search(r"Son 3 düzen: ([^.]*)\.", s)
if m3:
    eski = [p.strip() for p in m3.group(1).split(",")]
    yeni = (eski + [f"{x.duzen} ({x.konu[:20]})"])[-3:]
    s = s.replace(m3.group(0), "Son 3 düzen: " + ", ".join(yeni) + ".", 1)
s = re.sub(r"Son güncelleme: [^T]*TSİ", f"Son güncelleme: {bugun.strftime('%d.%m.%Y %H:%M')} TSİ", s, count=1)
open("DURUM.md", "w", encoding="utf-8").write(s)
son3 = ", ".join(p.split(" (")[0] for p in (yeni if m3 else []))
satir = f"- {x.saat} ({gun}) AUTO ({x.tur}): {x.dosya} ({x.duzen}) - {x.dongu} Buffer {x.buffer}." + (f" hak: kalan {kalan}." if kalan is not None else "") + (f" Son 3 duzen: {son3}." if son3 else "")
open("DONGU.md", "a", encoding="utf-8").write(satir + "\n")
open("performans.md", "a", encoding="utf-8").write(f"| {gun} | {x.saat} | {x.tur} | {x.konu} | {x.duzen} | {x.buffer} |\n")
open("performans_veri.csv", "a", encoding="utf-8").write(f"{iso},{x.saat},{x.kaynak},{x.tur},{x.gorus},{x.konu.replace(',', ' ')},{x.duzen},{x.buffer},,,,,,\n")
subprocess.run([sys.executable, "periyot.py", "yap", "tweet_gunluk", f"{x.saat} {x.tur}"], check=False)
if x.periyot:
    for p in x.periyot.split(";"): subprocess.run([sys.executable, "periyot.py", "yap", p, f"{x.saat} {x.konu}"], check=False)
msg = x.mesaj or f"{x.saat} {x.tur} {x.konu}"
cs = os.environ.get("CS")
tam = msg + "\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>" + (f"\nClaude-Session: {cs}" if cs else "")
r = subprocess.run(["git", "add", "-A"]); r = subprocess.run(["git", "commit", "-qm", tam])
if r.returncode == 0:
    subprocess.run(["git", "pull", "--rebase", "-q"]); r = subprocess.run(["git", "-c", "push.negotiate=true", "push", "-q", "origin", "main"])

print(satir); print("PUSH", "OK" if r.returncode == 0 else "HATA")

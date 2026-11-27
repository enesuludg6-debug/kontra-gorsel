#!/usr/bin/env python3
"""Kural 101: her tur yazmadan önce Enes'in sesinden 3 rastgele örnek + ses özellikleri."""
import random, re, os
s = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "SES_ORNEKLERI.md")).read()
oz = s.split("## SES ÖZELLİKLERİ")[1].split("## ÖRNEKLER")[0].strip()
orn = [l for l in s.split("## ÖRNEKLER")[1].split("## AYNI")[0].splitlines() if l.startswith("- [")]
iki = s.split("## AYNI KONU, İKİ SES")[1].strip()
print("ENES SESİ (kopyalama, tonu al):"); print(oz)
print("ÖRNEK 3:"); [print(" ", x) for x in random.sample(orn, 3)]
print("İKİ SES:"); print(iki)

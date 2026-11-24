#!/usr/bin/env python3
"""KURAL 77 (F-007): logo doğrulama listesi. Kullanım: python3 logo_dogrula.py ekle <T> | sil <T> | kontrol <T> | liste"""
import sys, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
F = "logo/DOGRULANDI.txt"
def oku():
    return [l.strip() for l in open(F) if l.strip() and not l.startswith("#")] if os.path.exists(F) else []
def dogrulandi(t):
    return t.upper().lstrip("$") in oku()
if __name__ == "__main__":
    a = sys.argv[1:]
    if not a: print(__doc__); sys.exit(1)
    if a[0] == "liste": print(" ".join(oku()))
    elif a[0] == "kontrol": ok = dogrulandi(a[1]); print("DOGRULANDI" if ok else "DOGRULANMADI"); sys.exit(0 if ok else 1)
    elif a[0] == "ekle":
        t = a[1].upper().lstrip("$")
        if t not in oku(): open(F, "a").write(t + "\n")
        print("eklendi", t)
    elif a[0] == "sil":
        t = a[1].upper().lstrip("$"); s = [l for l in open(F) if l.strip() != t]; open(F, "w").writelines(s); print("silindi", t)

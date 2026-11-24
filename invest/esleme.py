#!/usr/bin/env python3
"""KURAL 81-82: Nasdaq 100 (ya da başka endeks) bugünkü zirve ile tarihsel dönemi takvim takvime eşler.
Kullanım: python3 invest/esleme.py [^NDX] -> 2018 (zirve 2018-10-01) ve 2022 (zirve 2021-11-19) yollarını bugünkü zirveye uygular."""
import sys, json, urllib.request, datetime as dt
T = sys.argv[1] if len(sys.argv) > 1 else "^NDX"
def seri(p1, p2):
    u = f"https://query1.finance.yahoo.com/v8/finance/chart/{T}?interval=1d&period1={int(p1.timestamp())}&period2={int(p2.timestamp())}"
    m = json.load(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=15))["chart"]["result"][0]
    return [(dt.datetime.fromtimestamp(a, dt.timezone.utc).date(), b) for a, b in zip(m["timestamp"], m["indicators"]["quote"][0]["close"]) if b]
now = dt.datetime.now(dt.timezone.utc)
bug = seri(now - dt.timedelta(days=400), now)
zirve = max(bug, key=lambda x: x[1]); zi = bug.index(zirve); n = len(bug) - 1 - zi
print(f"BUGUN {T}: zirve {zirve[0]} {zirve[1]:.0f}, son {bug[-1][0]} {bug[-1][1]:.0f}, zirveden {100*(bug[-1][1]/zirve[1]-1):.1f}%, zirveden beri {n} işlem günü")
for ad, z in [("2018", dt.datetime(2018, 10, 1, tzinfo=dt.timezone.utc)), ("2022", dt.datetime(2021, 11, 19, tzinfo=dt.timezone.utc))]:
    s = seri(z - dt.timedelta(days=3), z + dt.timedelta(days=420)); i0 = max(range(min(10, len(s))), key=lambda i: s[i][1]); s = s[i0:]
    ayni = s[min(n, len(s) - 1)]; dip = min(s[:300], key=lambda x: x[1])
    print(f"{ad}: aynı gün ({n}. işlem günü) {100*(ayni[1]/s[0][1]-1):.1f}% | dip {dip[0]} {100*(dip[1]/s[0][1]-1):.1f}% ({s.index(dip)}. gün) -> bugünkü zirveye uygulanınca {zirve[1]*dip[1]/s[0][1]:.0f}")
    for g in (n + 5, n + 21, n + 42, n + 63):
        if g < len(s): print(f"   +{g-n} işlem günü sonra: {100*(s[g][1]/s[0][1]-1):.1f}% -> {zirve[1]*s[g][1]/s[0][1]:.0f}")

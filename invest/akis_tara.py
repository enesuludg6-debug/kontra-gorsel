"""KURAL 121 — opsiyon akışı doğrulama (Yahoo v8 chart, opsiyon sembolüyle; ücretsiz).

Not: Yahoo opsiyon zinciri (v7) bu ortamda kapalı (crumb/401). v8 chart opsiyon sembolünde çalışıyor:
günlük kapanış ve hacim verir. Akış hesabının paylaştığı kontratı buradan teyit ederiz.

  python3 invest/akis_tara.py SPY 2026-11-27 P 694      -> SPY261127P00694000 günlük fiyat/hacim + dayanak
"""
import sys, json, urllib.request, datetime as dt


def _chart(sym, rng="3mo"):
    u = f"https://query1.finance.yahoo.com/v8/finance/chart/{sym}?interval=1d&range={rng}"
    d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=20))["chart"]["result"][0]
    q = d["indicators"]["quote"][0]
    return [(dt.datetime.fromtimestamp(t, dt.UTC).date(), c, v) for t, c, v in zip(d["timestamp"], q["close"], q["volume"]) if c is not None]


def occ(t, vade, tip, k):
    y = dt.date.fromisoformat(vade)
    return f"{t.upper()}{y:%y%m%d}{tip.upper()[0]}{int(round(float(k) * 1000)):08d}"


if __name__ == "__main__":
    t, vade, tip, k = sys.argv[1:5]
    s = occ(t, vade, tip, k)
    print("KONTRAT", s)
    for g, c, v in _chart(s)[-15:]: print(f"  {g}  kapanış {c:.2f}  hacim {v}")
    print("DAYANAK", t.upper())
    for g, c, _ in _chart(t.upper(), "1mo")[-8:]: print(f"  {g}  {c:.2f}")

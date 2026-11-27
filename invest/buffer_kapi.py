#!/usr/bin/env python3
"""Kural 100 (27.11, Claude Academy 'Hooks' dersi: atlanamayan kural hook ile zorlanır).
PreToolUse hook: mcp__buffer__create_post / edit_post metni yayin_kontrol.sh'tan 'GEÇTİ' almadıysa çağrıyı DURDURUR.
yayin_kontrol.sh GEÇTİ verince metnin özetini invest/.onay/<sha> dosyasına yazar (3 saat geçerli)."""
import sys, json, hashlib, os, time, re
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".onay")
def ozet(t): return hashlib.sha256(re.sub(r"\s+", " ", t).strip().encode()).hexdigest()[:20]
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "onayla":
        t = sys.stdin.read(); os.makedirs(D, exist_ok=True)
        open(os.path.join(D, ozet(t)), "w").write(str(time.time())); print("onay kaydı", ozet(t)); sys.exit(0)
    try: j = json.load(sys.stdin)
    except Exception: sys.exit(0)
    metin = (j.get("tool_input") or {}).get("text") or ""
    if not metin.strip(): sys.exit(0)
    f = os.path.join(D, ozet(metin))
    if os.path.exists(f) and time.time() - float(open(f).read() or 0) < 3 * 3600: sys.exit(0)
    print("KURAL 100: bu metin yayin_kontrol.sh'tan GEÇTİ almadı (ya da metin kontrol edilenden farklı). "
          "Önce: bash invest/yayin_kontrol.sh <TUR> <KALIP> < metin -> GEÇTİ, sonra AYNI metni gönder.", file=sys.stderr)
    sys.exit(2)

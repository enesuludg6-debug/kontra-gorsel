#!/bin/bash
# KART PUSH + RAW URL KONTROLU TEK CAGRI (kesin kural 28). Kurali degistirmez: 200 degilse gorselsiz tweet ATILMAZ.
# Kullanim: bash invest/yayinla_gorsel.sh g/20261117_1740_x.jpg
cd "$(dirname "$0")" || exit 1
F=$1; [ -f "$F" ] || { echo "dosya yok: $F"; exit 1; }
MSG="kart $(basename "$F")

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"; [ -n "$CS" ] && MSG="$MSG
Claude-Session: $CS"
git add "$F" && git commit -qm "$MSG" && git pull --rebase -q && git -c push.negotiate=true push -q origin main || { echo "PUSH HATA -> tweet atma"; exit 1; }
U="https://raw.githubusercontent.com/enesuludg6-debug/kontra-gorsel/main/invest/$F"
for i in 1 2 3; do sleep 4; C=$(curl -s -o /dev/null -w "%{http_code}" "$U"); [ "$C" = 200 ] && { echo "OK $U"; exit 0; }; sleep 6; done
echo "RAW $C -> gorselsiz tweet ATMA, yeni dosya adiyla tekrar"; exit 1

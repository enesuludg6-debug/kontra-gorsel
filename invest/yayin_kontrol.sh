#!/bin/bash
# YAYIN KAPISI (kural 99, Claude Academy 'kaliteyi hook/test zorlasın'): yasak + kalite + 35 dk + günlük üst sınır.
# Kullanım: bash invest/yayin_kontrol.sh <TUR> <KALIP> < metin.txt   -> son satır GEÇTİ ya da DUR
cd "$(dirname "$0")" || exit 1
T=$(mktemp); cat > "$T"; HATA=0
python3 yasak.py < "$T" | tail -5 | tee /tmp/yk_yasak.txt; grep -q "YASAK VAR" /tmp/yk_yasak.txt && HATA=1
python3 kalite.py kontrol --tur "$1" --kalip "$2" < "$T" | tail -6 | tee /tmp/yk_kalite.txt; grep -q "KALITE HATA" /tmp/yk_kalite.txt && HATA=1
python3 ses_kontrol.py < "$T" | tee /tmp/yk_ses.txt; grep -q "SES HATA" /tmp/yk_ses.txt && HATA=1
O=$(python3 gun_ozet.py); echo "$O" | sed -n '1p;3p'
echo "$O" | grep -q "ÜST SINIR DOLDU" && { echo "  günlük üst sınır doldu"; HATA=1; }
echo "$O" | grep -q "BEKLE / customScheduled" && echo "  UYARI: 35 dk dolmadı -> Buffer customScheduled en erken saatle"
[ $HATA = 0 ] && python3 buffer_kapi.py onayla < "$T" >/dev/null; rm -f "$T"; [ $HATA = 0 ] && echo "GEÇTİ" || echo "DUR"

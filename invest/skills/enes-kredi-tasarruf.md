# KURAL 115 — KREDİ TASARRUFU (Enes 28.11 20:24 'kredinin idareli kullanımı için yetenekler oluştur ama hiçbir işin akışı bozulmasın')
Amaç: aynı işi, aynı kaliteyle, daha az token/araç çağrısıyla yapmak. HİÇBİR GÖREV, ZİNCİR, SAYAÇ, KALİTE KAPISI YA DA DOĞRULAMA ATLANMAZ; yalnız NASIL yapıldığı kısalır.

## 1. Okuma
- Büyük dosyaları baştan okuma (skills/*.md, KURALLAR_TAM.md, DONGU.md, tur.md dışındakiler). Gerekeni `grep -n -A5 "<başlık>"` ile aç.
- DONGU için `tail -n 15`, gun_ozet için `| sed -n 1,8p` yeter (konu listesi gerekirse ayrıca).
- Aynı dosyayı aynı turda iki kez okuma; ilk çıktıyı kullan.
- Görsel kontrolü: kartı 1 kez Read et; düzeltme gerekirse yalnız sorunlu bölgeyi PIL ile kırpıp oku.

## 2. Araç çağrısı
- Bağımsız komutları tek Bash çağrısında birleştir (git pull + kilit + gun_ozet + ses_ornek tek seferde).
- Her komut çıktısını kırp: `| tail -3`, `| grep -E "GEÇTİ|HATA|DUR"`; tam çıktı yalnız hata ayıklarken.
- yayin_kontrol.sh çıktısında yalnız hata satırlarına bak; GEÇTİ ise devam.
- Kalıp seçimi: kalite.py'nin 'son 4 kalıp' listesini gun_ozet'ten al, döngüyle 9 kalıp deneme; uygun kalıbı baştan seç.

## 3. Arama
- WebSearch varsayılan "standard"; "extended" yalnız standard boş/eski dönerse ya da fiyat/son dakika gerekiyorsa.
- Tur başına en çok 3 arama (X nabzı dahil, kural 106'nın 2'si bunun içinde). Doğrulama için ikinci kaynak aramasını ilk aramayla birleştir (tek sorguda iki kaynak çıkıyorsa yeter).
- Aynı gün aynı konu için yapılmış aramayı tekrarlama: sonuç ve kaynak DONGU satırında yazılıysa oradan kullan.
- WebFetch yalnız arama özeti rakamı vermiyorsa.

## 4. Veri
- Yahoo verisini aynı turda bir kez çek, gereken tüm hisseleri tek Python çağrısında hesapla.
- Hafta sonu ve seans dışında fiyat değişmez: o günün ilk hesabını alt_veri/ ya da DONGU satırından tekrar kullan.

## 5. Yetenek (skill) güncellemeleri
- propose_skills her kural değişikliğinde DEĞİL, günde en çok 2 kez toplu: öğle ve gün sonu. Aradaki kurallar repoda (invest/skills/*.md, KURAL_DIZINI.md) anında geçerlidir (kural 36: repo kopyası kazanır), iş akışı beklemez.
- propose_skills reddederse (kaydedilmemiş öneri) aynı düzenlemeyi tekrar gönder, uzun SKILL.md'yi yeniden okumaya çalışma.
- Hesap SKILL.md'leri kısa tutulur: repo yolunu gösteren yönlendirme + en kritik 5-10 satır. Ayrıntı repoda.

## 6. Mesajlar
- Enes'e mesaj: 'Paylaşıldı + Ne anlama geliyor?' 4-6 kısa madde; tekrar eden açıklama yok.
- Tur sonu özeti 3-4 cümle; yapılanların uzun dökümü yok (DONGU zaten kayıt).
- Bir turda tek SendUserMessage (taslak da aynı mesajda).

## 7. Turlar
- Haber zayıfsa hazır taslak havuzu (invest/taslak/) önce: 20:00 sonrası bir turda 2-3 taslak birlikte hazırlanır (kapıdan geçmiş hâliyle), sonraki turlar yalnız kontrol edip atar.
- Sabit görev zinciri kurulumları (send_later) tek mesajda; list_triggers yalnız yeni sohbete geçişte.
- Bildirim gelince ReadNotifications bir kez; boş tur yok.

## 8. Asla kısılmayan şeyler (akış bozulmasın)
- 2 kaynak doğrulama, yayin_kontrol.sh (yasak + kalite + ses), buffer_kapi hook, AKTIF_HESAP kilidi, kayit.py/kalite kaydet/DONGU, sonraki tur send_later, Enes'e 'Paylaşıldı' mesajı, sabit görev zincirleri, günlük alt sınırlar (kural 110/111/112).

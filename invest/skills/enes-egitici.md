---
name: enes-egitici
description: Enes'in X hesabında akşam 20-23 arası günde 1 atılan eğitici 'X nedir, neden önemli, bugün nerede' tweeti hazırlanırken kullanılır (kural 86-d).
---
# Akşam eğitici tweet (kural 86-d)

Veri: EGITICI tweetler ort. 5,8 beğeni (sistem ort. 2,3); "DRAM ve NAND ayrımı" 3.986 gösterim. Okur öğrenince kaydeder ve beğenir.

## Ne zaman
- Hafta içi her akşam 20:00-23:00 arasında 1 tane (hafta sonu isteğe bağlı, 10 tavanına dahil).
- Konu O GÜNÜN olayından çıkar: bugün PCE geldiyse "çekirdek PCE nedir", bellek hisseleri düştüyse "HBM nedir", tahvil oynadıysa "2 yıllık faiz neden Fed'i izler".
- Aynı kavram 30 gün içinde tekrar edilmez (`grep -i kavram performans_veri.csv DONGU.md`).

## Yapı (3 paragraf, kalıp E)
1. İlk satır (en çok 12 kelime): kavramın adı + okurun neden umursaması gerektiği, Enes'in birinci tekil sesiyle. Ör. "Bugün herkes çekirdek PCE'yi konuştu, kısaca ne olduğunu anlatayım."
2. Tanım: tek cümle, gündelik Türkçe, İngilizce terim parantezde en çok bir kez. Ardından tek somut örnek (bir şirket ya da bir hane).
3. Bugün nerede: tek güncel rakam (2 kaynak) + bu rakamın piyasada neyi değiştirdiği, tek cümle.
- En çok 3 farklı rakam; tanım cümlesinde rakam yok.

## Yasaklar
- 54-F dramatik/soyut kalıplar; "basitçe söylemek gerekirse", "kısaca özetlersek" gibi ders kitabı girişleri.
- Liste emojisi, "1/", "🧵", soru ile bitirme.
- Al/sat, hedef fiyat.

## Kart
- kart3 `haber_dosya` (3 madde: tanım rakamı / bugünkü değer / önceki değer) ya da `cizgi_pro` (kavramın son 2-5 yıllık gerçek serisi, `kart3.dogrula`).
- Kicker "NEDİR?" + kavram adı.

## Kayıt
- Tür EGITICI, kalıp E. `kayit.py --tur EGITICI`; ölçüm performans_veri.csv'de EGITICI ortalaması 5,8'in üstünde kalıyor mu.

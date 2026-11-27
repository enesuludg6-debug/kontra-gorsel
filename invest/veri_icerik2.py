#!/usr/bin/env python3
"""veri_icerik2.py — kural 93: profesyonel veri tweet paketi (Enes 26.11 08:55 "bunlar da tamam, bunları da ekle").
  fedwatch     Fed fon vadelilerinden (ZQ, Yahoo) toplantı başına fiyatlanan faiz ve artırım/indirim olasılığı (kendi hesabım, CME FedWatch yöntemi)
  kuyruk       Kuyruk riski fiyatı: SKEW ve VVIX (Yahoo), 5 yıllık yüzdelik
  korelasyon   Hisse-tahvil korelasyonu: QQQ ve TLT günlük getirileri, 60 gün (tahvil hâlâ korunma mı)
  rotasyon     Sektör rotasyon haritası (RRG yaklaşımı): 11 SPDR sektör ETF'inin SPY'a göre göreli güç oranı ve ivmesi, 4 bölge
  faktor       Faktör panosu: momentum (MTUM), değer (VLUE), küçük şirket (IWM), eşit ağırlık (RSP), Nasdaq (QQQ) – SPY farkı, 1 ay / 3 ay
  bakir_altin  Bakır/altın oranı (HG=F/GC=F) ve 10 yıllık faiz (^TNX): büyüme beklentisi barometresi
  revizyon     Kâr tahmini revizyonu (Bigdata.com estimates): haftalık anlık görüntü -> yukarı/aşağı revize sayısı ve büyüklüğü
  bilanco      Bilanço tepki istatistiği: portföy hissesinin son 8 bilançodaki ertesi gün hareketi (Bigdata.com tarihleri + Yahoo fiyatları)
Kullanım: python3 invest/veri_icerik2.py <komut> [--kart g/YYYYMMDD_HHMM_<komut>.jpg] [--t AVGO]
          python3 invest/veri_icerik2.py revizyon_ekle < csv   (t,date,eps_avg,revenue_avg,num_analysts_eps — bigdata_computer çıktısı)
          python3 invest/veri_icerik2.py tarih_ekle < csv      (t,reporting_date,eps_surprise_pct,revenue_surprise_pct)
          python3 invest/veri_icerik2.py yaklasan [gun]       portföyde önümüzdeki N gün bilançosu olanlar
"""
import sys, os, io, json, calendar, datetime as dt, warnings
import numpy as np, pandas as pd
warnings.filterwarnings("ignore")
from gosterge import veri
D = os.path.dirname(os.path.abspath(__file__)); AV = os.path.join(D, "alt_veri")
def arg(a, k, v=None): return a[a.index(k) + 1] if k in a else v
FOMC = ["2026-12-09", "2027-01-27", "2027-03-17", "2027-04-28", "2027-06-09", "2027-07-28", "2027-09-15", "2027-11-17", "2028-01-26"]  # karar günleri (Fed 12.11.2026 revize takvim; 27.10.2027 strateji toplantısı, karar yok)
AY = "FGHJKMNQUVXZ"

def zq(y, m):
    t = f"ZQ{AY[m - 1]}{str(y)[2:]}.CBT"
    try: return 100 - veri(t, "3mo", ttl=3 * 3600).close.iloc[-1]
    except Exception: return None

def fedwatch(a):
    bugun = dt.date.today(); r = zq(bugun.year, bugun.month); bas = r; satir = []
    for fd in FOMC:
        d = dt.date.fromisoformat(fd)
        if d < bugun: continue
        N = calendar.monthrange(d.year, d.month)[1]; avg = zq(d.year, d.month)
        if avg is None or r is None: break
        gun = d.day  # karar gününe kadar (dahil) eski faiz; ertesi gün yeni
        post = (avg * N - gun * r) / (N - gun) if N > gun else avg
        nxt = d.replace(day=1) + dt.timedelta(days=32); nxt = nxt.replace(day=1)
        if not any(dt.date.fromisoformat(f).year == nxt.year and dt.date.fromisoformat(f).month == nxt.month for f in FOMC):
            z = zq(nxt.year, nxt.month); post = z if z is not None else post
        fark = (post - r) * 100; satir.append((fd, r, post, fark)); r = post
        if len(satir) >= 5: break
    print(f"Fed fon vadelileri (Yahoo ZQ) — bugünkü ima edilen ort. faiz %{bas:.3f}")
    for fd, a_, b_, f_ in satir:
        yon = "artırım" if f_ > 0 else "indirim"; olas = min(100, abs(f_) / 25 * 100)
        print(f"   {fd}: toplantı öncesi %{a_:.2f} -> sonrası %{b_:.2f} ({f_:+.0f} bp) => 25 bp {yon} olasılığı ~%{olas:.0f}")
    top = sum(f for *_, f in satir); print(f"   {len(satir)} toplantıda toplam fiyatlanan değişim {top:+.0f} bp")
    if arg(a, "--kart"):
        import kart3 as K
        K.siralama("Piyasa nabzı • Fed beklentisi", f"Piyasa {satir[0][0][8:10]}.{satir[0][0][5:7]} toplantısı için {satir[0][3]:+.0f} bp fiyatlıyor".replace("-", "−"),
                   "Fed fon vadelilerinden toplantı başına ima edilen değişim, baz puan (kendi hesabım)",
                   [(f"{fd[8:10]}.{fd[5:7]}.{fd[2:4]}", round(f_, 1)) for fd, _, _, f_ in satir], f"{len(satir)} toplantıda toplam {top:+.0f} bp".replace("-", "−"),
                   "CBOT 30 günlük Fed fon vadelileri (Yahoo Finance), kendi hesabım", arg(a, "--kart"), birim=" bp")
        print("kart:", arg(a, "--kart"))

def kuyruk(a):
    s, vv = veri("^SKEW", "5y").close, veri("^VVIX", "5y").close
    ps, pv = (s < s.iloc[-1]).mean() * 100, (vv < vv.iloc[-1]).mean() * 100
    print(f"SKEW {s.iloc[-1]:.1f} (5 yılın %{ps:.0f}. yüzdeliği; 1 hafta önce {s.iloc[-6]:.1f}) | VVIX {vv.iloc[-1]:.1f} (%{pv:.0f}. yüzdelik; 1 hafta önce {vv.iloc[-6]:.1f})")
    print("okuma: SKEW yüksek = derin çöküş sigortası pahalı (kurumlar kuyruğa para ödüyor); VVIX yüksek = korkunun kendisi oynak, ani VIX sıçramalarına hazırlık")
    if arg(a, "--kart"):
        import kart3 as K
        x = s.tail(250); K.cizgi_pro("Piyasa nabzı • Kuyruk riski", f"SKEW {s.iloc[-1]:.0f}, VVIX {vv.iloc[-1]:.0f}", "Cboe SKEW: derin düşüşe karşı opsiyon talebi", [(str(i.date()), float(v)) for i, v in x.items()], [],
                    f"SKEW 5 yılın %{ps:.0f}'inden, VVIX %{pv:.0f}'inden yüksek", "Cboe (Yahoo Finance), kendi hesabım", arg(a, "--kart"), zirve=False); print("kart:", arg(a, "--kart"))

def korelasyon(a):
    q, t = veri("QQQ", "5y").close.pct_change(), veri("TLT", "5y").close.pct_change()
    k = q.rolling(60).corr(t).dropna(); son = k.iloc[-1]
    print(f"QQQ-TLT 60 günlük korelasyon {k.index[-1].date()}: {son:+.2f} (1 ay önce {k.iloc[-22]:+.2f}, 5 yıl aralığı {k.min():+.2f}..{k.max():+.2f})")
    print("okuma: " + ("NEGATİF: tahvil hisse düşüşünde korunma sağlıyor" if son < -0.2 else "POZİTİF: hisse ve tahvil birlikte düşüyor, klasik 60/40 korunması çalışmıyor (faiz kaynaklı rejim)" if son > 0.2 else "nötr: tahvil zayıf korunma"))
    if arg(a, "--kart"):
        import kart3 as K
        x = k.tail(500); K.cizgi_pro("Piyasa nabzı • Korelasyon", f"Hisse-tahvil korelasyonu {son:+.2f}".replace(".", ",").replace("-", "−"), "QQQ ve TLT günlük getirileri, 60 günlük korelasyon",
                    [(str(i.date()), float(v)) for i, v in x.items()], [], "Pozitif = tahvil korunma sağlamıyor", "Yahoo Finance, kendi hesabım", arg(a, "--kart"), zirve=False, ref=[(0, "0")]); print("kart:", arg(a, "--kart"))

SEK = {"XLK": "Teknoloji", "XLE": "Enerji", "XLV": "Sağlık", "XLF": "Finans", "XLY": "Tüketici (döngüsel)", "XLP": "Temel tüketim", "XLI": "Sanayi", "XLB": "Malzeme", "XLU": "Kamu hizmetleri", "XLRE": "Gayrimenkul", "XLC": "İletişim"}
def rotasyon(a):
    spy = veri("SPY", "2y").close; R = []
    for t, ad in SEK.items():
        rs = (veri(t, "2y").close / spy).dropna(); ratio = 100 * rs / rs.rolling(50).mean(); mom = 100 * ratio / ratio.shift(10)
        R.append((ad, t, ratio.iloc[-1], mom.iloc[-1], ratio.iloc[-6], mom.iloc[-6]))
    # kesitsel normalize (JdK yaklaşımı): sektörler birbirine göre; ortalama 100
    mx, my, mx0, my0 = (np.mean([z[i] for z in R]) for i in (2, 3, 4, 5))
    R = [(ad, t, 100 + x - mx, 100 + y - my, 100 + x0 - mx0, 100 + y0 - my0) for ad, t, x, y, x0, y0 in R]
    def bolge(x, y): return "LİDER" if x >= 100 and y >= 100 else "ZAYIFLAYAN" if x >= 100 else "GERİDE" if y < 100 else "TOPARLANAN"
    for ad, t, x, y, x0, y0 in sorted(R, key=lambda z: -z[2]): print(f"   {ad:<20} göreli güç {x:6.1f}  ivme {y:6.1f}  -> {bolge(x, y)}" + (f" (1 hafta önce {bolge(x0, y0)})" if bolge(x, y) != bolge(x0, y0) else ""))
    if arg(a, "--kart"):
        import kart3 as K, matplotlib.pyplot as plt
        fig, r = K.cerceve("Piyasa nabzı • Sektör rotasyonu", "Sektörler dört bölgede", "S&P 500'e göre göreli güç (yatay) ve ivme (dikey), 50 gün / 10 gün", "Sağ üst lider, sağ alt zayıflayan, sol alt geride, sol üst toparlanan", "SPDR ETF'leri, kendi hesabım")
        ax = K._ax(fig, r, (0.04, 0.06, 0.04, 0.02)); xs = [z[2] for z in R]; ys = [z[3] for z in R]
        lx = max(abs(np.array(xs) - 100).max(), 1) * 1.25; ly = max(abs(np.array(ys) - 100).max(), 1) * 1.25
        ax.set_xlim(100 - lx, 100 + lx); ax.set_ylim(100 - ly, 100 + ly); ax.axvline(100, color=K.GREY, lw=1.2); ax.axhline(100, color=K.GREY, lw=1.2)
        for (x0, y0, c) in ((1, 1, K.UP), (1, -1, K.GOLD), (-1, -1, K.DOWN), (-1, 1, K.ACC)):
            ax.fill_between([100, 100 + x0 * lx], 100, 100 + y0 * ly, color=c, alpha=0.06)
        KISA = {"Tüketici (döngüsel)": "Döngüsel tük.", "Kamu hizmetleri": "Kamu hizm.", "Temel tüketim": "Temel tük."}
        yerler = []
        for ad, t, x, y, x0, y0 in sorted(R, key=lambda z: -z[3]):
            ax.scatter([x], [y], s=90, color=K.INK, zorder=4)
            ty, adim, k_ = y, ly * 0.07, 0
            while any(abs(ty - py) < ly * 0.065 and abs(x - px) < lx * 0.45 for px, py in yerler):
                k_ += 1; ty = y + (adim * ((k_ + 1) // 2)) * (1 if k_ % 2 else -1)
            yerler.append((x, ty))
            ax.annotate(KISA.get(ad, ad), (x, y), (x + lx * 0.04, ty), va="center", ha="left", fontsize=15, color=K.INK, family=K.FAM, fontweight="bold",
                        arrowprops=dict(arrowstyle="-", color=K.GREY, lw=0.8) if abs(ty - y) > 1e-9 else None)
        for (tx, ty_, et, c) in ((100 + lx * .95, 100 + ly * .92, "LİDER", K.UP), (100 + lx * .95, 100 - ly * .92, "ZAYIFLAYAN", K.GOLD), (100 - lx * .95, 100 - ly * .92, "GERİDE", K.DOWN), (100 - lx * .95, 100 + ly * .92, "TOPARLANAN", K.ACC)):
            ax.text(tx, ty_, et, ha="right" if tx > 100 else "left", va="center", fontsize=16, color=c, family=K.FAM, fontweight="bold")
        K.kaydet(fig, arg(a, "--kart")); print("kart:", arg(a, "--kart"))

def faktor(a):
    spy = veri("SPY", "2y").close; F = {"MTUM": "Momentum", "VLUE": "Değer", "IWM": "Küçük şirket", "RSP": "Eşit ağırlık", "QQQ": "Nasdaq 100"}; R = []
    for t, ad in F.items():
        c = veri(t, "2y").close; R.append((ad, (c.iloc[-1] / c.iloc[-22] - spy.iloc[-1] / spy.iloc[-22]) * 100, (c.iloc[-1] / c.iloc[-64] - spy.iloc[-1] / spy.iloc[-64]) * 100))
    for ad, m1, m3 in R: print(f"   {ad:<14} S&P 500'e göre 1 ay {m1:+.1f} puan, 3 ay {m3:+.1f} puan")
    rsp = dict((z[0], z) for z in R)["Eşit ağırlık"]; print("okuma: " + ("eşit ağırlık önde: yükseliş/düşüş GENİŞ tabanlı, devler dışındakiler daha iyi" if rsp[1] > 0 else "eşit ağırlık geride: piyasayı birkaç dev şirket taşıyor (dar taban)"))
    if arg(a, "--kart"):
        import kart3 as K
        K.siralama("Piyasa nabzı • Faktörler", "Piyasayı kim taşıyor, son 1 ay", "S&P 500'e göre getiri farkı, puan", [(ad, round(m1, 1)) for ad, m1, m3 in R],
                   "3 aylıkta: " + ", ".join(f"{ad} {m3:+.1f}" for ad, m1, m3 in R[:3]).replace(".", ","), "ETF verisi (Yahoo), kendi hesabım", arg(a, "--kart")); print("kart:", arg(a, "--kart"))

def bakir_altin(a):
    hg, gc, tnx = veri("HG=F", "5y").close, veri("GC=F", "5y").close, veri("^TNX", "5y").close
    o = (hg / gc * 1000).dropna(); son = o.iloc[-1]; k = o.pct_change(20).rolling(250).corr(tnx.diff(20)).dropna()
    print(f"Bakır/altın oranı (x1000) {o.index[-1].date()}: {son:.3f} (1 ay önce {o.iloc[-22]:.3f}, {((son / o.iloc[-22]) - 1) * 100:+.1f}%; 5 yılın %{(o < son).mean() * 100:.0f}. yüzdeliği) | 10Y %{tnx.iloc[-1]:.2f} (1 ay {tnx.iloc[-1] - tnx.iloc[-22]:+.2f})")
    print("okuma: oran düşüyor + faiz yüksek = piyasa büyüme beklemiyor ama faiz inmiyor (stagflasyon kokusu); oran yükseliyor + faiz yükseliyor = büyüme kaynaklı faiz")
    if arg(a, "--kart"):
        import kart3 as K
        x = o.tail(250); K.cizgi_pro("Piyasa nabzı • Büyüme barometresi", f"Bakır/altın oranı {son:.2f}".replace(".", ","), "Bakır vadeli fiyatı / altın vadeli fiyatı x1000",
                    [(str(i.date()), float(v)) for i, v in x.items()], [], f"10 yıllık faiz %{tnx.iloc[-1]:.2f}".replace(".", ","), "COMEX (Yahoo Finance), kendi hesabım", arg(a, "--kart"), zirve=False); print("kart:", arg(a, "--kart"))

def revizyon_ekle(metin):
    y = pd.read_csv(io.StringIO(metin.strip())); y["kayit"] = dt.date.today().isoformat(); f = os.path.join(AV, "revizyon.csv")
    x = pd.concat([pd.read_csv(f) if os.path.exists(f) else None, y]); x.drop_duplicates(["t", "date", "kayit"], keep="last").to_csv(f, index=False); print(f"revizyon anlık görüntüsü kaydedildi: {len(y)} satır")
def revizyon(a):
    f = os.path.join(AV, "revizyon.csv")
    if not os.path.exists(f): sys.exit("kayıt yok: bigdata_computer estimates -> revizyon_ekle")
    x = pd.read_csv(f); k = sorted(x.kayit.unique())
    if len(k) < 2: print(f"yalnız 1 anlık görüntü ({k[0]}); revizyon için gelecek hafta ikinci kayıt gerekiyor -> TWEET YOK"); return
    s, o = x[x.kayit == k[-1]], x[x.kayit == k[-2]]; R = []
    for t in sorted(set(s.t)):
        a_ = s[s.t == t]; yil = sorted(a_.date)[0] if len(a_) else None; b_ = o[(o.t == t) & (o.date == yil)]
        if yil and len(b_): R.append((t, yil[:4], b_.eps_avg.iloc[0], a_[a_.date == yil].eps_avg.iloc[0]))
    yuk = [r for r in R if r[3] > r[2] * 1.002]; asg = [r for r in R if r[3] < r[2] * 0.998]
    for t, y_, e0, e1 in R: print(f"   {t:<5} {y_} EPS beklentisi {e0:.2f} -> {e1:.2f} ({(e1 / e0 - 1) * 100:+.1f}%)")
    print(f"revizyon genişliği ({k[-2]} -> {k[-1]}): {len(yuk)} yukarı, {len(asg)} aşağı, {len(R) - len(yuk) - len(asg)} değişmedi")
    if arg(a, "--kart") and R:
        import kart3 as K
        K.siralama("Piyasa nabzı • Analist beklentisi", f"Kâr tahminleri: {len(yuk)} yukarı, {len(asg)} aşağı", "Portföy, en yakın mali yıl EPS konsensüsü, haftalık değişim %",
                   [(t, round((e1 / e0 - 1) * 100, 2)) for t, y_, e0, e1 in R], "Fiyat tahminlerden önce hareket eder mi: haftalık izliyorum", "Bigdata.com analist konsensüsü", arg(a, "--kart")); print("kart:", arg(a, "--kart"))

def tarih_ekle(metin):
    y = pd.read_csv(io.StringIO(metin.strip())); f = os.path.join(AV, "bilanco_tarih.csv")
    x = pd.concat([pd.read_csv(f) if os.path.exists(f) else None, y]); x.drop_duplicates(["t", "reporting_date"], keep="last").sort_values(["t", "reporting_date"]).to_csv(f, index=False); print(f"bilanço tarihleri: {len(x)} satır")
def yaklasan(a):
    n = int(a[1]) if len(a) > 1 else 7; x = pd.read_csv(os.path.join(AV, "bilanco_tarih.csv")); b = dt.date.today()
    y = x[(pd.to_datetime(x.reporting_date).dt.date >= b) & (pd.to_datetime(x.reporting_date).dt.date <= b + dt.timedelta(days=n))]
    print("\n".join(f"{r.t} {r.reporting_date}" for r in y.itertuples()) or f"önümüzdeki {n} günde portföy bilançosu yok")
def bilanco(a):
    t = arg(a, "--t", "AVGO"); x = pd.read_csv(os.path.join(AV, "bilanco_tarih.csv")); x = x[(x.t == t) & x.eps_surprise_pct.notna()].tail(8)
    c = veri(t, "5y"); R = []
    for r in x.itertuples():
        d = pd.Timestamp(r.reporting_date); i = c.index.searchsorted(d)
        if i + 1 >= len(c) or i < 1: continue
        # şirket kapanıştan sonra açıklıyorsa tepki ertesi gün; öncesinde açıklıyorsa aynı gün: ikisinin büyüğünü al (mutlak)
        g0, g1 = c.close.iloc[i] / c.close.iloc[i - 1] - 1, c.close.iloc[i + 1] / c.close.iloc[i] - 1
        g = g1 if abs(g1) >= abs(g0) else g0; R.append((r.reporting_date, r.eps_surprise_pct, g * 100))
    if not R: print("veri yok"); return
    g = np.array([z[2] for z in R]); print(f"{t} son {len(R)} bilanço tepkisi: ortalama mutlak hareket %{np.abs(g).mean():.1f}, yükselen {int((g > 0).sum())}/{len(g)}, en büyük {g[np.abs(g).argmax()]:+.1f}%")
    for d_, s_, g_ in R: print(f"   {d_}: EPS sürprizi {s_:+.1f}% -> fiyat {g_:+.1f}%")
    if arg(a, "--kart"):
        import kart3 as K
        K.siralama("Bilanço öncesi • Geçmiş tepkiler", f"{t}: son {len(R)} bilançoda ort. %{np.abs(g).mean():.1f} hareket".replace(".", ","), "Bilanço sonrası ilk işlem günü fiyat değişimi, %",
                   [(d_[2:].replace("-", "."), round(g_, 1)) for d_, s_, g_ in R], f"{int((g > 0).sum())}/{len(g)} bilançoda yükseldi", "Bigdata.com bilanço tarihleri, Yahoo Finance, kendi hesabım", arg(a, "--kart")); print("kart:", arg(a, "--kart"))

if __name__ == "__main__":
    a = sys.argv[1:]
    if not a: print(__doc__); sys.exit()
    k = a[0]
    if k in ("revizyon_ekle", "tarih_ekle"): globals()[k](sys.stdin.read())
    else: globals()[k](a)

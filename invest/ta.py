# Enes'in zorunlu gosterge seti (16.11 13:27): EMA200, VWAP, RSI14, MACD, ATR14, Volume Profile, ADX14, Fibonacci/OTE, OBV
import json,sys,urllib.request,datetime
def get(s,rng="1y"):
    r=urllib.request.Request(f"https://query1.finance.yahoo.com/v8/finance/chart/{s}?range={rng}&interval=1d&includePrePost=true",headers={"User-Agent":"Mozilla/5.0"})
    d=json.load(urllib.request.urlopen(r,timeout=20))["chart"]["result"][0]
    q=d["indicators"]["quote"][0]; t=d["timestamp"]
    rows=[(t[i],q["open"][i],q["high"][i],q["low"][i],q["close"][i],q["volume"][i] or 0) for i in range(len(t)) if q["close"][i] is not None]
    return d["meta"],rows
def ema(a,n):
    k=2/(n+1); e=a[0]; o=[]
    for x in a: e=x*k+e*(1-k); o.append(e)
    return o
def wilder(a,n):
    o=[None]*len(a); s=sum(a[1:n+1])/n; o[n]=s
    for i in range(n+1,len(a)): s=(s*(n-1)+a[i])/n; o[i]=s
    return o
def rsi(c,n=14):
    g=[0]+[max(c[i]-c[i-1],0) for i in range(1,len(c))]; l=[0]+[max(c[i-1]-c[i],0) for i in range(1,len(c))]
    ag,al=wilder(g,n),wilder(l,n)
    return [None if ag[i] is None else (100 if al[i]==0 else 100-100/(1+ag[i]/al[i])) for i in range(len(c))]
def analiz(s):
    m,r=get(s); o=[x[1] for x in r];h=[x[2] for x in r];l=[x[3] for x in r];c=[x[4] for x in r];v=[x[5] for x in r]
    n=len(c); last=c[-1]; dt=datetime.datetime.fromtimestamp(r[-1][0],datetime.timezone.utc).date()
    pre=m.get("preMarketPrice") or m.get("regularMarketPrice")
    e200=ema(c,200)[-1] if n>=200 else None; e50=ema(c,50)[-1]
    tr=[h[0]-l[0]]+[max(h[i]-l[i],abs(h[i]-c[i-1]),abs(l[i]-c[i-1])) for i in range(1,n)]
    atr=wilder(tr,14)[-1]
    pdm=[0]+[(h[i]-h[i-1]) if (h[i]-h[i-1])>(l[i-1]-l[i]) and (h[i]-h[i-1])>0 else 0 for i in range(1,n)]
    mdm=[0]+[(l[i-1]-l[i]) if (l[i-1]-l[i])>(h[i]-h[i-1]) and (l[i-1]-l[i])>0 else 0 for i in range(1,n)]
    atrs=wilder(tr,14); sp=wilder(pdm,14); sm=wilder(mdm,14)
    dx=[None]*n; pdi=mdi=0
    for i in range(14,n):
        pdi=100*sp[i]/atrs[i]; mdi=100*sm[i]/atrs[i]; dx[i]=100*abs(pdi-mdi)/(pdi+mdi) if pdi+mdi else 0
    dxv=[x for x in dx if x is not None]; adx=sum(dxv[:14])/14
    for x in dxv[14:]: adx=(adx*13+x)/14
    R=rsi(c); m12,m26=ema(c,12),ema(c,26); md=[a-b for a,b in zip(m12,m26)]; sg=ema(md,9); hist=[a-b for a,b in zip(md,sg)]
    obv=[0]
    for i in range(1,n): obv.append(obv[-1]+(v[i] if c[i]>c[i-1] else -v[i] if c[i]<c[i-1] else 0))
    # OBV uyumsuzluk: son 20 gun fiyat ve OBV egimi
    pf=(c[-1]-c[-21]); of=(obv[-1]-obv[-21]); div="yok"
    if pf<0 and of>0: div="POZITIF (fiyat dusuyor, OBV yukseliyor)"
    if pf>0 and of<0: div="NEGATIF (fiyat yukseliyor, OBV dusuyor)"
    tp=[(h[i]+l[i]+c[i])/3 for i in range(n)]
    vw20=sum(tp[i]*v[i] for i in range(n-20,n))/sum(v[-20:])
    lo_i=min(range(n),key=lambda i:l[i]); hi_i=max(range(n),key=lambda i:h[i])
    a=max(lo_i,hi_i); vwA=sum(tp[i]*v[i] for i in range(a,n))/max(1,sum(v[a:])) # son buyuk dip/tepeden anchored VWAP
    # Volume profile (son 120 gun, 30 kutu)
    k=min(120,n); H=max(h[-k:]);L=min(l[-k:]); B=30; bw=(H-L)/B; bins=[0]*B
    for i in range(n-k,n):
        lo,hi=l[i],h[i]; span=max(hi-lo,1e-9)
        for b in range(B):
            a0,a1=L+b*bw,L+(b+1)*bw; ov=max(0,min(hi,a1)-max(lo,a0))
            bins[b]+=v[i]*ov/span
    poc=max(range(B),key=lambda b:bins[b]); tot=sum(bins); inc={poc}; acc=bins[poc]
    while acc<0.7*tot:
        lo_b=min(inc)-1; hi_b=max(inc)+1
        cand=[(bins[b],b) for b in (lo_b,hi_b) if 0<=b<B]
        if not cand: break
        val,b=max(cand); inc.add(b); acc+=val
    POC=L+(poc+.5)*bw; VAL=L+min(inc)*bw; VAH=L+(max(inc)+1)*bw
    # Fibonacci: 1y swing (tepe->dip ya da dip->tepe hangisi sonra)
    HI,LO=h[hi_i],l[lo_i]
    if hi_i<lo_i: # dusus: tepe->dip, geri cekilme yukari
        f=lambda r_:LO+(HI-LO)*r_; yon="dusus bacagi (tepe->dip), direnc seviyeleri"
    else:
        f=lambda r_:HI-(HI-LO)*r_; yon="yukselis bacagi (dip->tepe), destek seviyeleri"
    print(f"\n=== {s} | kapanis {dt} {last:.2f} | anlik/pre {pre}")
    print(f"EMA200 {e200:.2f} -> fiyat {'USTUNDE' if e200 and last>e200 else 'ALTINDA'} (ana trend {'yukari' if e200 and last>e200 else 'asagi'}) | EMA50 {e50:.2f}" if e200 else f"EMA200 yok (veri<200g) | EMA50 {e50:.2f}")
    print(f"VWAP20g {vw20:.2f} | Anchored VWAP (son ana dip/tepe {datetime.datetime.fromtimestamp(r[a][0],datetime.timezone.utc).date()}) {vwA:.2f} -> fiyat {'ustunde' if last>vwA else 'altinda'}")
    print(f"RSI14 {R[-1]:.0f} (5g once {R[-6]:.0f}) | MACD {md[-1]:.2f} sinyal {sg[-1]:.2f} hist {hist[-1]:+.2f} (dun {hist[-2]:+.2f}) -> {'yukari kesisim' if hist[-1]>0 and hist[-2]<=0 else 'asagi kesisim' if hist[-1]<0 and hist[-2]>=0 else ('pozitif' if hist[-1]>0 else 'negatif')}, momentum {'artiyor' if hist[-1]>hist[-2] else 'azaliyor'}")
    print(f"ATR14 {atr:.2f} (%{atr/last*100:.1f}) -> 1,5xATR stop mesafesi {1.5*atr:.2f}, 2xATR {2*atr:.2f}")
    print(f"ADX14 {adx:.0f} ({'guclu trend' if adx>=25 else 'zayif/yatay'}) +DI {pdi:.0f} -DI {mdi:.0f} ({'alicilar' if pdi>mdi else 'saticilar'} baskin)")
    print(f"Volume Profile 120g: POC {POC:.2f} | deger alani {VAL:.2f}-{VAH:.2f} | fiyat {'deger alani ICINDE' if VAL<=last<=VAH else 'deger alaninin USTUNDE' if last>VAH else 'deger alaninin ALTINDA'}")
    print(f"Fibonacci ({yon}): tepe {HI:.2f} dip {LO:.2f} | 0.382 {f(.382):.2f} 0.5 {f(.5):.2f} 0.618 {f(.618):.2f} 0.705 {f(.705):.2f} 0.786 {f(.786):.2f} | OTE bolgesi {min(f(.618),f(.786)):.2f}-{max(f(.618),f(.786)):.2f}")
    print(f"OBV 20g degisim {of/1e6:+.1f}M, fiyat 20g {pf/c[-21]*100:+.1f}% -> uyumsuzluk {div}")
for s in sys.argv[1:]:
    try: analiz(s)
    except Exception as e: print(s,"HATA",e)

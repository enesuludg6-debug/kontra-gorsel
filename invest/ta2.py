# Tam gosterge seti, coklu zaman dilimi (Enes 16.11 13:28). Kullanim: python3 ta2.py NBIS RKLB ...  [-v detay]
import json,sys,urllib.request,datetime,math
UA={"User-Agent":"Mozilla/5.0"}
def fetch(s,interval,rng):
    u=f"https://query1.finance.yahoo.com/v8/finance/chart/{s}?range={rng}&interval={interval}"
    d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=20))["chart"]["result"][0]
    q=d["indicators"]["quote"][0];t=d["timestamp"]
    return [(t[i],q["open"][i],q["high"][i],q["low"][i],q["close"][i],q["volume"][i] or 0) for i in range(len(t)) if q["close"][i] is not None and q["high"][i] is not None]
def resample(r,k):
    o=[]
    for i in range(0,len(r),k):
        g=r[i:i+k]; o.append((g[0][0],g[0][1],max(x[2] for x in g),min(x[3] for x in g),g[-1][4],sum(x[5] for x in g)))
    return o
def ema(a,n):
    k=2/(n+1);e=a[0];o=[]
    for x in a:e=x*k+e*(1-k);o.append(e)
    return o
def sma(a,n): return [None]*(n-1)+[sum(a[i-n+1:i+1])/n for i in range(n-1,len(a))]
def wil(a,n):
    o=[None]*len(a)
    if len(a)<=n: return o
    s=sum(a[1:n+1])/n;o[n]=s
    for i in range(n+1,len(a)):s=(s*(n-1)+a[i])/n;o[i]=s
    return o
def std(a,n): return [None]*(n-1)+[(sum((x-sum(a[i-n+1:i+1])/n)**2 for x in a[i-n+1:i+1])/n)**.5 for i in range(n-1,len(a))]
def all_ind(r):
    o=[x[1] for x in r];h=[x[2] for x in r];l=[x[3] for x in r];c=[x[4] for x in r];v=[x[5] for x in r];n=len(c);L=c[-1];R={}
    tr=[h[0]-l[0]]+[max(h[i]-l[i],abs(h[i]-c[i-1]),abs(l[i]-c[i-1])) for i in range(1,n)]
    atr=wil(tr,14)
    # RSI
    g=[0]+[max(c[i]-c[i-1],0) for i in range(1,n)];ls=[0]+[max(c[i-1]-c[i],0) for i in range(1,n)]
    ag,al=wil(g,14),wil(ls,14);rsi=[None if ag[i] is None else (100 if al[i]==0 else 100-100/(1+ag[i]/al[i])) for i in range(n)]
    R["RSI"]=(rsi[-1], 1 if rsi[-1]>55 else -1 if rsi[-1]<45 else 0, f"{rsi[-1]:.0f}"+(" asiri alim" if rsi[-1]>70 else " asiri satim" if rsi[-1]<30 else ""))
    m=[a-b for a,b in zip(ema(c,12),ema(c,26))];sg=ema(m,9);hi=[a-b for a,b in zip(m,sg)]
    R["MACD"]=(hi[-1],1 if hi[-1]>0 else -1,f"hist {hi[-1]:+.2f}"+(" YUKARI KESISIM" if hi[-1]>0>=hi[-2] else " ASAGI KESISIM" if hi[-1]<0<=hi[-2] else ""))
    e20,e50=ema(c,20)[-1],ema(c,50)[-1];R["EMA20/50"]=(0,1 if L>e20>e50 else -1 if L<e20<e50 else 0,f"{e20:.2f}/{e50:.2f}")
    if n>=200:
        e200=ema(c,200)[-1];R["EMA200"]=(e200,1 if L>e200 else -1,f"{e200:.2f}")
        s200=sma(c,200)[-1];R["SMA200"]=(s200,1 if L>s200 else -1,f"{s200:.2f}")
    s50=sma(c,50)[-1];R["SMA50"]=(s50,1 if L>s50 else -1,f"{s50:.2f}")
    s20=sma(c,20)[-1];sd=std(c,20)[-1];bu,bl=s20+2*sd,s20-2*sd;pb=(L-bl)/(bu-bl)
    R["Bollinger"]=(pb,1 if pb>0.8 else -1 if pb<0.2 else 0,f"{bl:.2f}-{bu:.2f} %B {pb:.2f}")
    tp=[(h[i]+l[i]+c[i])/3 for i in range(n)];vw=sum(tp[i]*v[i] for i in range(n-20,n))/max(1,sum(v[-20:]))
    R["VWAP20"]=(vw,1 if L>vw else -1,f"{vw:.2f}")
    rv=[x for x in rsi if x is not None];st=[None]*len(rv)
    for i in range(13,len(rv)):
        w=rv[i-13:i+1];st[i]=0 if max(w)==min(w) else (rv[i]-min(w))/(max(w)-min(w))*100
    k=sma([x for x in st if x is not None],3);d=sma([x for x in k if x is not None],3)
    R["StochRSI"]=(k[-1],1 if k[-1]>d[-1] and k[-1]<80 else -1 if k[-1]<d[-1] and k[-1]>20 else 0,f"K {k[-1]:.0f} D {d[-1]:.0f}"+(" asiri alim" if k[-1]>80 else " asiri satim" if k[-1]<20 else ""))
    pdm=[0]+[(h[i]-h[i-1]) if h[i]-h[i-1]>l[i-1]-l[i] and h[i]-h[i-1]>0 else 0 for i in range(1,n)]
    mdm=[0]+[(l[i-1]-l[i]) if l[i-1]-l[i]>h[i]-h[i-1] and l[i-1]-l[i]>0 else 0 for i in range(1,n)]
    sp,sm=wil(pdm,14),wil(mdm,14);dx=[];pdi=mdi=0
    for i in range(14,n):
        pdi=100*sp[i]/atr[i] if atr[i] else 0;mdi=100*sm[i]/atr[i] if atr[i] else 0;dx.append(100*abs(pdi-mdi)/(pdi+mdi) if pdi+mdi else 0)
    adx=sum(dx[:14])/14
    for x in dx[14:]:adx=(adx*13+x)/14
    R["ADX"]=(adx,(1 if pdi>mdi else -1) if adx>=25 else 0,f"{adx:.0f} +DI {pdi:.0f} -DI {mdi:.0f} "+("guclu" if adx>=25 else "zayif"))
    if n>=78:
        tk=(max(h[-9:])+min(l[-9:]))/2;kj=(max(h[-26:])+min(l[-26:]))/2
        sa=((max(h[-35:-26])+min(l[-35:-26]))/2+(max(h[-52:-26])+min(l[-52:-26]))/2)/2;sb=(max(h[-78:-26])+min(l[-78:-26]))/2
        top,bot=max(sa,sb),min(sa,sb)
        R["Ichimoku"]=(0,1 if L>top and tk>kj else -1 if L<bot and tk<kj else 0,f"bulut {bot:.2f}-{top:.2f} tenkan {tk:.2f} kijun {kj:.2f} fiyat {'ustunde' if L>top else 'altinda' if L<bot else 'icinde'}")
    md=[sum(abs(x-sum(tp[i-19:i+1])/20) for x in tp[i-19:i+1])/20 for i in range(n-1,n)][0];cci=(tp[-1]-sum(tp[-20:])/20)/(0.015*md) if md else 0
    R["CCI"]=(cci,1 if cci>100 else -1 if cci<-100 else 0,f"{cci:.0f}")
    wr=(max(h[-14:])-L)/(max(h[-14:])-min(l[-14:]))*-100
    R["Williams%R"]=(wr,1 if wr>-20 else -1 if wr<-80 else 0,f"{wr:.0f}"+(" asiri alim" if wr>-20 else " asiri satim" if wr<-80 else ""))
    # Parabolic SAR
    up=True;af=.02;ep=h[0];sar=l[0]
    for i in range(1,n):
        sar=sar+af*(ep-sar)
        if up:
            sar=min(sar,l[i-1],l[i-2] if i>1 else l[i-1])
            if l[i]<sar: up=False;sar=ep;ep=l[i];af=.02
            elif h[i]>ep: ep=h[i];af=min(af+.02,.2)
        else:
            sar=max(sar,h[i-1],h[i-2] if i>1 else h[i-1])
            if h[i]>sar: up=True;sar=ep;ep=h[i];af=.02
            elif l[i]<ep: ep=l[i];af=min(af+.02,.2)
    R["PSAR"]=(sar,1 if up else -1,f"{sar:.2f} {'yukari' if up else 'asagi'}")
    # Supertrend 10,3
    fu=fl=0;trend=1;stl=0
    for i in range(10,n):
        mid=(h[i]+l[i])/2;bu_=mid+3*atr[i] if atr[i] else mid;bl_=mid-3*atr[i] if atr[i] else mid
        fu=bu_ if (bu_<fu or c[i-1]>fu) else fu;fl=bl_ if (bl_>fl or c[i-1]<fl) else fl
        if trend==1 and c[i]<fl: trend=-1
        elif trend==-1 and c[i]>fu: trend=1
        stl=fl if trend==1 else fu
    R["Supertrend"]=(stl,trend,f"{'BUY' if trend==1 else 'SELL'} cizgi {stl:.2f}")
    # MFI
    pos=neg=0
    for i in range(n-14,n):
        mf=tp[i]*v[i]
        if tp[i]>tp[i-1]:pos+=mf
        elif tp[i]<tp[i-1]:neg+=mf
    mfi=100-100/(1+pos/neg) if neg else 100
    R["MFI"]=(mfi,1 if mfi>55 else -1 if mfi<45 else 0,f"{mfi:.0f}"+(" asiri alim" if mfi>80 else " asiri satim" if mfi<20 else ""))
    ke=ema(c,20)[-1];ku,kl=ke+2*atr[-1],ke-2*atr[-1];R["Keltner"]=(0,1 if L>ku else -1 if L<kl else 0,f"{kl:.2f}-{ku:.2f}")
    a=25;hh=max(range(a+1),key=lambda j:h[n-1-a+j]);ll=min(range(a+1),key=lambda j:l[n-1-a+j]);au,ad=hh/a*100,ll/a*100
    R["Aroon"]=(au-ad,1 if au>70 and au>ad else -1 if ad>70 and ad>au else 0,f"up {au:.0f} down {ad:.0f}")
    obv=[0]
    for i in range(1,n):obv.append(obv[-1]+(v[i] if c[i]>c[i-1] else -v[i] if c[i]<c[i-1] else 0))
    pf=c[-1]-c[-21];of=obv[-1]-obv[-21];dv="POZITIF uyumsuzluk" if pf<0<of else "NEGATIF uyumsuzluk" if of<0<pf else "uyumlu"
    R["OBV"]=(of,1 if of>0 else -1,f"20 bar {of/1e6:+.1f}M {dv}")
    kk=min(120,n);H=max(h[-kk:]);Lw=min(l[-kk:]);B=30;bw=(H-Lw)/B or 1;bins=[0]*B
    for i in range(n-kk,n):
        sp_=max(h[i]-l[i],1e-9)
        for b in range(B):
            ov=max(0,min(h[i],Lw+(b+1)*bw)-max(l[i],Lw+b*bw));bins[b]+=v[i]*ov/sp_
    p=max(range(B),key=lambda b:bins[b]);inc={p};acc=bins[p];tot=sum(bins)
    while acc<.7*tot:
        cand=[(bins[b],b) for b in (min(inc)-1,max(inc)+1) if 0<=b<B]
        if not cand:break
        val,b=max(cand);inc.add(b);acc+=val
    POC=Lw+(p+.5)*bw;VAL=Lw+min(inc)*bw;VAH=Lw+(max(inc)+1)*bw
    R["VolProfile"]=(POC,1 if L>VAH else -1 if L<VAL else 0,f"POC {POC:.2f} VA {VAL:.2f}-{VAH:.2f}")
    hi_i=max(range(n),key=lambda i:h[i]);lo_i=min(range(n),key=lambda i:l[i]);HI,LO=h[hi_i],l[lo_i]
    f=(lambda q:LO+(HI-LO)*q) if hi_i<lo_i else (lambda q:HI-(HI-LO)*q)
    ote=(min(f(.618),f(.786)),max(f(.618),f(.786)))
    R["Fib"]=(0,0,f"{'tepe->dip' if hi_i<lo_i else 'dip->tepe'} {HI:.2f}/{LO:.2f} .5 {f(.5):.2f} OTE {ote[0]:.2f}-{ote[1]:.2f} "+("FIYAT OTE ICINDE" if ote[0]<=L<=ote[1] else ""))
    # SMC yaklasik: swing (5 bar) yapisi, BOS/CHoCH, FVG
    sw=5;SH=[(i,h[i]) for i in range(sw,n-sw) if h[i]==max(h[i-sw:i+sw+1])];SL=[(i,l[i]) for i in range(sw,n-sw) if l[i]==min(l[i-sw:i+sw+1])]
    smc="";sd_=0
    if len(SH)>=2 and len(SL)>=2:
        hh_=SH[-1][1]>SH[-2][1];hl_=SL[-1][1]>SL[-2][1]
        struct="yukselen (HH/HL)" if hh_ and hl_ else "dusen (LH/LL)" if not hh_ and not hl_ else "karisik"
        sd_=1 if hh_ and hl_ else -1 if not hh_ and not hl_ else 0
        ev=""
        if L>SH[-1][1]: ev=("BOS yukari" if sd_==1 else "CHoCH yukari (donus)")+f" {SH[-1][1]:.2f} kirildi"
        elif L<SL[-1][1]: ev=("BOS asagi" if sd_==-1 else "CHoCH asagi (donus)")+f" {SL[-1][1]:.2f} kirildi"
        fvg=[]
        for i in range(n-30,n-1):
            if l[i+1]>h[i-1]: fvg.append(f"bull FVG {h[i-1]:.2f}-{l[i+1]:.2f}") if L>h[i-1] and min(l[i+1:]+[L])>h[i-1] else None
            if h[i+1]<l[i-1]: fvg.append(f"bear FVG {h[i+1]:.2f}-{l[i-1]:.2f}") if L<l[i-1] and max(h[i+1:]+[L])<l[i-1] else None
        smc=f"yapi {struct}; son swing tepe {SH[-1][1]:.2f} dip {SL[-1][1]:.2f}; {ev}; acik FVG: {', '.join(fvg[-2:]) or 'yok'}"
    R["SMC"]=(0,sd_,smc)
    R["ATR"]=(atr[-1],0,f"{atr[-1]:.2f} (%{atr[-1]/L*100:.1f}) stop 1.5x {1.5*atr[-1]:.2f}")
    return L,R
TF=[("1H","60m","60d",1),("4H","60m","180d",4),("1G","1d","2y",1),("1HF","1wk","5y",1)]
v="-v" in sys.argv
for s in [a for a in sys.argv[1:] if a!="-v"]:
    print(f"\n######## {s}")
    for name,iv,rg,k in TF:
        try:
            r=fetch(s,iv,rg)
            if k>1:r=resample(r,k)
            L,R=all_ind(r);sc=sum(x[1] for x in R.values());tot=sum(1 for x in R.values() if x[1]!=0 or True)
            bull=sum(1 for x in R.values() if x[1]==1);bear=sum(1 for x in R.values() if x[1]==-1)
            print(f"[{name}] son {L:.2f} | yukari {bull} / asagi {bear} / notr {len(R)-bull-bear}")
            keys=R.keys() if (v or name=="1G") else ["Supertrend","SMC","EMA200","RSI","MACD","ADX","StochRSI","OBV"]
            for kk in keys:
                if kk in R:print(f"   {kk:11s} {'+' if R[kk][1]==1 else '-' if R[kk][1]==-1 else '0'} {R[kk][2]}")
        except Exception as e: print(f"[{name}] HATA {e}")

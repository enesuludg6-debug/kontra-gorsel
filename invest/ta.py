import json,sys,urllib.request,datetime
def get(s):
    r=urllib.request.Request(f"https://query1.finance.yahoo.com/v8/finance/chart/{s}?range=1y&interval=1d",headers={"User-Agent":"Mozilla/5.0"})
    d=json.load(urllib.request.urlopen(r,timeout=20))["chart"]["result"][0]
    q=d["indicators"]["quote"][0]; t=d["timestamp"]
    rows=[(t[i],q["close"][i],q["high"][i],q["low"][i],q["volume"][i]) for i in range(len(t)) if q["close"][i] is not None]
    return d["meta"],rows
def sma(a,n): return sum(a[-n:])/n if len(a)>=n else None
def ema(a,n):
    k=2/(n+1); e=a[0]; out=[]
    for x in a: e=x*k+e*(1-k); out.append(e)
    return out
def rsi(c,n=14):
    g=l=0
    for i in range(1,n+1):
        d=c[i]-c[i-1]; g+=max(d,0); l+=max(-d,0)
    g/=n;l/=n
    for i in range(n+1,len(c)):
        d=c[i]-c[i-1]; g=(g*(n-1)+max(d,0))/n; l=(l*(n-1)+max(-d,0))/n
    return 100-100/(1+g/l) if l else 100
for s in sys.argv[1:]:
    m,r=get(s); c=[x[1] for x in r]; v=[x[4] or 0 for x in r]
    last=c[-1]; date=datetime.datetime.utcfromtimestamp(r[-1][0]).date()
    m12,m26=ema(c,12),ema(c,26); macd=[a-b for a,b in zip(m12,m26)]; sig=ema(macd,9)
    s20=sma(c,20); sd=(sum((x-s20)**2 for x in c[-20:])/20)**.5
    hi52=max(x[2] for x in r); lo52=min(x[3] for x in r)
    hi20=max(x[2] for x in r[-20:]); lo20=min(x[3] for x in r[-20:])
    ch5=(last/c[-6]-1)*100; ch20=(last/c[-21]-1)*100
    print(f"{s} {date} son {last:.2f} | 5g {ch5:+.1f}% 20g {ch20:+.1f}% | SMA20 {s20:.2f} SMA50 {sma(c,50):.2f} SMA200 {(sma(c,200) or 0):.2f} | RSI {rsi(c):.0f} | MACD {macd[-1]:.2f} sig {sig[-1]:.2f} hist {macd[-1]-sig[-1]:+.2f} (önce {macd[-2]-sig[-2]:+.2f}) | BB {s20-2*sd:.2f}-{s20+2*sd:.2f} | 20g dip/tepe {lo20:.2f}/{hi20:.2f} | 52h {lo52:.2f}/{hi52:.2f} ({(last/hi52-1)*100:+.0f}%) | hacim/20g ort {v[-1]/(sum(v[-21:-1])/20):.1f}x")

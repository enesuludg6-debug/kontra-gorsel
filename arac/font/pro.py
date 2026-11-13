import sys; sys.path.insert(0,"/home/claude/font"); sys.path.insert(0,"/home/claude/gol")
from kart import *
from golfoto import TEMA
from PIL import ImageDraw, ImageFilter, ImageEnhance, ImageOps, ImageChops
import random
INK=(7,10,18)
ABR={"GALATASARAY":"GS","FENERBAHÇE":"FB","BEŞİKTAŞ":"BJK","TRABZONSPOR":"TS"}
def cover(path,w,h,yb=0.0):
    ph=Image.open(path).convert("RGB"); sc=max(w/ph.width,h/ph.height)
    ph=ph.resize((int(ph.width*sc+.5),int(ph.height*sc+.5)),Image.LANCZOS)
    x0=(ph.width-w)//2; y0=int((ph.height-h)*yb)
    return ph.crop((x0,y0,x0+w,y0+h))
def grade(im,sat=0.75,con=1.15,bri=0.8):
    im=ImageEnhance.Color(im).enhance(sat); im=ImageEnhance.Contrast(im).enhance(con); im=ImageEnhance.Brightness(im).enhance(bri)
    return im.filter(ImageFilter.UnsharpMask(2,60,3))
def grain(c,amt=14):
    n=Image.effect_noise(c.size,40).convert("L").point(lambda v:v)
    g=Image.merge("RGBA",(n,n,n,Image.new("L",c.size,amt))); c.alpha_composite(g)
def vgrad(c,y0,y1,col,a0,a1,x0=0,x1=None):
    x1=x1 or c.width; lay=Image.new("RGBA",c.size,(0,0,0,0)); d=ImageDraw.Draw(lay)
    for y in range(y0,y1): d.line([(x0,y),(x1,y)],fill=col+(int(a0+(a1-a0)*(y-y0)/max(1,y1-y0)),))
    c.alpha_composite(lay)
def vignette(c,s=0.55):
    m=Image.new("L",(W//4,H//4),0); d=ImageDraw.Draw(m); d.ellipse((-W//8*0.6,-H//8*0.4,W//4+W//8*0.6,H//4+H//8*0.4),fill=255)
    m=m.filter(ImageFilter.GaussianBlur(40)).resize((W,H)); inv=ImageOps.invert(m).point(lambda v:int(v*s))
    c.alpha_composite(Image.merge("RGBA",(Image.new("L",(W,H),0),)*3+(inv,)))
def alpha(l,a): l=l.copy(); l.putalpha(l.getchannel("A").point(lambda v:v*a//255)); return l
def sq(c,x,y,s,col): rect(c,(x,y,x+s,y+s),col,radius=3)

# A — EDITORYAL
def kart_A(photo,durum,ev,dep,tev,tdep,sev,sdep,gol_ev,gol_dep,alt,out):
    Ze,Ve=TEMA[tev]; Zd,Vd=TEMA[tdep]; biten=durum=="MAÇ SONUCU"
    c=Image.new("RGBA",(W,H),INK+(255,))
    c.paste(grade(cover(photo,W,H)),(0,0)); vignette(c,0.6)
    vgrad(c,0,260,INK,200,0); vgrad(c,640,H,INK,0,250)
    logo(c,60,56,52)
    put(c,text_layer(alt,BEBAS,30,(205,212,226),track=7),1020,82,align="right",valign="middle")
    # baslik satiri
    yb=880
    t=text_layer(durum,BEBAS,38,WHITE,track=10); put(c,t,60,yb,valign="middle")
    rect(c,(60+t.width+28,yb-1,1020,yb+1),WHITE,alpha=90)
    # skor
    ys=1035
    ae=255 if not(biten and sdep>sev) else 110; ad=255 if not(biten and sev>sdep) else 110
    a1=alpha(text_layer(ABR.get(ev,ev[:3]),ANTON,84,WHITE,track=2),ae); a2=alpha(text_layer(ABR.get(dep,dep[:3]),ANTON,84,WHITE,track=2),ad)
    put(c,a1,60,ys,valign="middle"); put(c,a2,1020,ys,align="right",valign="middle")
    sq(c,60,ys-a1.height/2-30,16,Ve)
    sq(c,1020-16,ys-a2.height/2-30,16,Vd)
    n1=alpha(text_layer(str(sev),ANTON,250,WHITE),ae); n2=alpha(text_layer(str(sdep),ANTON,250,WHITE),ad)
    put(c,n1,W/2-60,ys,align="right",valign="middle"); put(c,n2,W/2+60,ys,align="left",valign="middle")
    rect(c,(W/2-2,ys-80,W/2+2,ys+80),WHITE,alpha=140)
    # golculer
    yg=1170
    rect(c,(60,yg-22,1020,yg-21),WHITE,alpha=50)
    put(c,text_layer("  ·  ".join(gol_ev),BEBAS,32,(200,206,220),track=4),60,yg)
    put(c,text_layer("  ·  ".join(gol_dep),BEBAS,32,(200,206,220),track=4),1020,yg,align="right")
    put(c,text_layer("@KONTRA_11",BEBAS,28,(150,160,180),track=8),W/2,1290,align="center",valign="middle")
    grain(c,10); c.convert("RGB").save(out,quality=95)

# B — CAM PANEL
def kart_B(photo,durum,ev,dep,tev,tdep,sev,sdep,gol_ev,gol_dep,alt,out):
    Ze,Ve=TEMA[tev]; Zd,Vd=TEMA[tdep]; biten=durum=="MAÇ SONUCU"
    base=grade(cover(photo,W,H),sat=0.85,bri=0.85)
    c=Image.new("RGBA",(W,H)); c.paste(base,(0,0)); vignette(c,0.5)
    vgrad(c,0,240,INK,190,0); vgrad(c,760,H,INK,0,200)
    logo(c,60,56,52)
    put(c,text_layer(alt,BEBAS,30,(225,230,240),track=7),1020,82,align="right",valign="middle")
    px0,py0,px1,py1=56,940,1024,1268
    blur=c.crop((px0,py0,px1,py1)).filter(ImageFilter.GaussianBlur(28))
    m=Image.new("L",blur.size,0); ImageDraw.Draw(m).rounded_rectangle((0,0,blur.width-1,blur.height-1),radius=34,fill=255)
    c.paste(blur,(px0,py0),m)
    gl=Image.new("RGBA",(W,H),(0,0,0,0)); gd=ImageDraw.Draw(gl)
    gd.rounded_rectangle((px0,py0,px1,py1),radius=34,fill=(14,18,30,150),outline=(255,255,255,60),width=2)
    c.alpha_composite(gl)
    # durum
    t=text_layer(durum,BEBAS,34,WHITE,track=10); dot=Ve if not biten else (255,255,255)
    put(c,t,W/2+12,py0+52,align="center",valign="middle")
    lay=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(lay).ellipse((W/2-t.width/2-18,py0+45,W/2-t.width/2-4,py0+59),fill=(236,64,64,255) if not biten else (180,190,205,255)); c.alpha_composite(lay)
    ys=py0+168
    ae=255 if not(biten and sdep>sev) else 120; ad=255 if not(biten and sev>sdep) else 120
    put(c,text_layer(f"{sev}",ANTON,150,WHITE),W/2-34,ys,align="right",valign="middle")
    put(c,text_layer(f"{sdep}",ANTON,150,WHITE),W/2+34,ys,align="left",valign="middle")
    rect(c,(W/2-10,ys-4,W/2+10,ys+4),WHITE)
    for side,name,V,a in (("L",ev,Ve,ae),("R",dep,Vd,ad)):
        l=alpha(fit(name,BEBAS,50,WHITE,300,track=3),a)
        x=120 if side=="L" else 960
        rect(c,(x-2 if side=="L" else x-58,ys-46,x+58 if side=="L" else x+2,ys-40),V)
        put(c,l,x if side=="L" else x,ys+4,align="left" if side=="L" else "right",valign="middle")
    yg=py1-58
    put(c,text_layer("  ·  ".join(gol_ev),BEBAS,30,(210,216,228),track=4),120,yg,valign="middle")
    put(c,text_layer("  ·  ".join(gol_dep),BEBAS,30,(210,216,228),track=4),960,yg,align="right",valign="middle")
    put(c,text_layer("@KONTRA_11",BEBAS,26,(190,198,215),track=8),W/2,1305,align="center",valign="middle")
    grain(c,8); c.convert("RGB").save(out,quality=95)

# C — DUOTON POSTER (kazananin renkleri)
def duotone(im,dark_c,light_c,mid_c=None):
    g=ImageOps.autocontrast(im.convert("L"),cutoff=1)
    if mid_c: return ImageOps.colorize(g,dark_c,light_c,mid=mid_c,blackpoint=0,whitepoint=255,midpoint=110)
    return ImageOps.colorize(g,dark_c,light_c)
MID={"GALATASARAY":(200,30,40),"FENERBAHCE":(30,60,150),"BESIKTAS":(110,110,110),"TRABZONSPOR":(150,25,60)}
def kart_C(photo,durum,ev,dep,tev,tdep,sev,sdep,gol_ev,gol_dep,alt,out):
    Ze,Ve=TEMA[tev]; Zd,Vd=TEMA[tdep]
    k = tev if sev>=sdep else tdep
    Z,V=TEMA[k]
    c=Image.new("RGBA",(W,H),INK+(255,))
    ph=duotone(cover(photo,W,980),tuple(int(v*0.3) for v in Z),V,MID.get(k)).convert("RGBA")
    c.alpha_composite(ph,(0,0))
    vgrad(c,560,980,INK,0,255); vgrad(c,0,220,INK,170,0)
    logo(c,60,56,52)
    put(c,text_layer(alt,BEBAS,30,(230,232,240),track=7),1020,82,align="right",valign="middle")
    big=text_layer(f"{sev}–{sdep}",ANTON,330,WHITE,track=10)
    put(c,big,W/2,820,align="center",valign="middle")
    t=text_layer(durum,BEBAS,36,V,track=12); put(c,t,W/2,1030,align="center",valign="middle")
    put(c,fit(ev,ANTON,62,WHITE,430,track=2),60,1080)
    put(c,fit(dep,ANTON,62,WHITE,430,track=2),1020,1080,align="right")
    rect(c,(60,1160,140,1165),Ve); rect(c,(940,1160,1020,1165),Vd)
    put(c,text_layer("  ·  ".join(gol_ev),BEBAS,30,(200,206,220),track=4),60,1186)
    put(c,text_layer("  ·  ".join(gol_dep),BEBAS,30,(200,206,220),track=4),1020,1186,align="right")
    put(c,text_layer("@KONTRA_11",BEBAS,26,(150,160,180),track=8),W/2,1305,align="center",valign="middle")
    grain(c,10); c.convert("RGB").save(out,quality=95)
if __name__=="__main__":
    o="/mnt/user-data/outputs/"; f="/mnt/user-data/uploads/b31bb179-image.jpg"
    a=(f,"MAÇ SONUCU","GALATASARAY","FENERBAHÇE","GALATASARAY","FENERBAHCE",2,1,["OSIMHEN 23'","SANE 78'"],["GREENWOOD 38'"],"SÜPER LİG · 12. HAFTA")
    kart_A(*a,o+"KONTRA_stil_A.png"); kart_B(*a,o+"KONTRA_stil_B.png"); kart_C(*a,o+"KONTRA_stil_C.png")

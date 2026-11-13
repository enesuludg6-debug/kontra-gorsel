import sys; sys.path.insert(0,"/home/claude/font")
from kart import *
from PIL import Image, ImageFilter, ImageEnhance
TEMA={ # (zemin, vurgu, yazi_vurgu)
 "KONTRA":((10,26,58),(167,196,242)),
 "FENERBAHCE":((12,24,58),(255,214,0)),
 "GALATASARAY":((110,10,20),(253,185,19)),
 "BESIKTAS":((12,12,12),(255,255,255)),
 "TRABZONSPOR":((100,16,40),(80,170,230)),
 "BASAKSEHIR":((14,30,70),(240,100,20)),
 "SAMSUNSPOR":((150,10,20),(255,255,255)),
 "GOZTEPE":((150,15,25),(255,200,0)),
 "MILLI":((180,10,20),(255,255,255)),
 "BELCIKA":((120,10,25),(253,218,36)),
 "KONYASPOR":((15,80,45),(255,255,255)),
}
def gol_foto(photo, cut, oyuncu, ev, skor, dep, dk=None, out="out.png", tema="KONTRA", alt_sag=None):
    Z,V=TEMA[tema]
    c=Image.new("RGBA",(W,H),Z+(255,))
    ph=Image.open(photo).convert("RGBA"); sc=W/ph.width
    ph=ph.resize((W,int(ph.height*sc)),Image.LANCZOS); oy=-30
    bg=ImageEnhance.Brightness(ph.filter(ImageFilter.GaussianBlur(3))).enhance(0.55)
    c.alpha_composite(bg,(0,oy))
    # lacivert ton
    rect(c,(0,0,W,H),Z,alpha=120)
    # GOOOL arkada
    put(c,text_layer("GOOOL",ANTON,330,WHITE if tema=="KONTRA" else V,track=6,shear=0.2),W/2,135,align="center")
    # oyuncu onde
    ct=Image.open(cut).convert("RGBA").resize(ph.size,Image.LANCZOS)
    c.alpha_composite(ct,(0,oy))
    gradient(c,800,1150,Z); rect(c,(0,1150,W,H),Z)
    logo(c,60,44,64)
    put(c,text_layer("@KONTRA_11",BEBAS,36,WHITE,track=3),1020,76,align="right",valign="middle")
    rect(c,(60,1028,74,1150),V)
    put(c,fit(oyuncu,ANTON,140,WHITE,900,track=4,shear=0.2),96,1028)
    y=1215
    x=60
    if dk:
        rect(c,(60,y-38,230,y+38),WHITE,radius=38)
        put(c,text_layer(dk,BEBAS,46,Z,track=3),145,y,align="center",valign="middle"); x=260
    e=fit(ev,BEBAS,56,WHITE,330,track=3); put(c,e,x,y,valign="middle"); x+=e.width+24
    rect(c,(x,y-40,x+150,y+40),V,radius=12)
    put(c,text_layer(skor,ANTON,58,Z,track=2,shear=0.2),x+75,y,align="center",valign="middle"); x+=174
    put(c,fit(dep,BEBAS,56,WHITE,1020-x,track=3),x,y,valign="middle")
    rect(c,(60,1282,1020,1285),V,alpha=120)
    put(c,text_layer("TRENDYOL SÜPER LİG",BEBAS,32,(143,163,191),track=4),60,1315,valign="middle")
    put(c,text_layer(alt_sag or "GOL",BEBAS,32,V,track=4),1020,1315,align="right",valign="middle")
    c.convert("RGB").save(out)
if __name__=="__main__":
    gol_foto("/mnt/user-data/uploads/5f242299-image.jpg","cut.png","GREENWOOD","FENERBAHÇE","2-1","GAZİANTEP FK",out="/mnt/user-data/outputs/KONTRA_gol_greenwood.png",alt_sag="FENERBAHÇE ÖNE GEÇTİ")
    gol_foto("/mnt/user-data/uploads/5f242299-image.jpg","cut.png","GREENWOOD","FENERBAHÇE","2-1","GAZİANTEP FK",dk="67'",out="/mnt/user-data/outputs/KONTRA_gol_greenwood_FB.png",tema="FENERBAHCE",alt_sag="FENERBAHÇE ÖNE GEÇTİ")

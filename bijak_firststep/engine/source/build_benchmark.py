#!/usr/bin/env python3
"""BIJAK MATEMATIK — penanda aras editorial 12 halaman.
Run: python source/build_benchmark.py  (from the bijak folder).
All coordinates are millimetres from top left. No remote assets.
"""
from pathlib import Path
import json, math, re, shutil
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor, Color, white
from reportlab.lib.utils import simpleSplit
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'pdf'; ASSET=ROOT/'assets'; QA=ROOT/'qa'
for p in [OUT,ASSET,QA,ASSET/'fonts']: p.mkdir(parents=True,exist_ok=True)
for file in ['DejaVuSans.ttf','DejaVuSans-Bold.ttf']:
    dest=ASSET/'fonts'/file
    if not dest.exists(): shutil.copy('/usr/share/fonts/truetype/dejavu/'+file,dest)
pdfmetrics.registerFont(TTFont('BM',str(ASSET/'fonts/DejaVuSans.ttf')))
pdfmetrics.registerFont(TTFont('BM-Bold',str(ASSET/'fonts/DejaVuSans-Bold.ttf')))
MM=72/25.4; W=210*MM; H=297*MM
BLUE='#1768AD'; ORANGE='#D97119'; GREEN='#087D63'; PURPLE='#7051A3'; YELLOW='#F2C94C'; NAVY='#17324B'; GRAY='#53616C'

TIGER='''<svg xmlns="http://www.w3.org/2000/svg" width="300" height="310" viewBox="0 0 300 310">
<g stroke="#17324B" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">
<path d="M218 248 Q293 277 275 208 Q268 186 252 202" fill="none" stroke="#D97119" stroke-width="17"/>
<ellipse cx="151" cy="235" rx="65" ry="61" fill="#F5A63A"/>
<ellipse cx="151" cy="242" rx="39" ry="43" fill="#FFF2D4"/>
<ellipse cx="105" cy="288" rx="31" ry="14" fill="#F5A63A"/><ellipse cx="198" cy="288" rx="31" ry="14" fill="#F5A63A"/>
<path d="M101 211 Q63 249 50 221 Q43 207 64 189" fill="#F5A63A"/>
<path d="M205 216 Q234 213 246 182" fill="none" stroke="#F5A63A" stroke-width="25"/>
<path d="M243 183 L257 157" stroke-width="8"/>
<circle cx="73" cy="64" r="35" fill="#F5A63A"/><circle cx="229" cy="64" r="35" fill="#F5A63A"/>
<circle cx="73" cy="64" r="19" fill="#F4C1A3"/><circle cx="229" cy="64" r="19" fill="#F4C1A3"/>
<path d="M49 109 Q53 34 150 34 Q250 35 253 111 L244 155 Q224 201 151 206 Q75 202 55 157 Z" fill="#F5A63A"/>
<path d="M135 36 L150 66 L164 36 M51 108 L82 119 L53 128 M250 107 L220 119 L248 131" fill="#17324B"/>
<ellipse cx="113" cy="120" rx="10" ry="14" fill="#17324B"/><ellipse cx="190" cy="120" rx="10" ry="14" fill="#17324B"/>
<circle cx="116" cy="115" r="3" fill="white" stroke="none"/><circle cx="193" cy="115" r="3" fill="white" stroke="none"/>
<ellipse cx="127" cy="157" rx="29" ry="23" fill="#FFF2D4"/><ellipse cx="175" cy="157" rx="29" ry="23" fill="#FFF2D4"/>
<path d="M137 144 Q151 136 165 144 L151 156 Z" fill="#17324B"/>
<path d="M151 156 L151 165 M131 165 Q151 190 174 165" fill="none"/>
<path d="M83 150 L62 145 M84 163 L62 168 M218 150 L238 144 M219 164 L239 169" fill="none" stroke-width="3"/>
<path d="M115 196 L150 217 L186 196 L185 223 L150 239 L116 223 Z" fill="#1768AD"/>
<path d="M92 241 L109 247 M211 241 L194 248" fill="none"/>
</g></svg>'''
(ASSET/'tiger_bijak.svg').write_text(TIGER)
APPLE='''<svg xmlns="http://www.w3.org/2000/svg" width="40" height="44" viewBox="0 0 40 44"><path d="M20 12 Q4 1 3 23 Q3 44 19 40 Q36 44 37 22 Q36 4 20 12Z" fill="#E9A64E" stroke="#17324B" stroke-width="2"/><path d="M20 13 L21 4" stroke="#17324B" stroke-width="3"/><path d="M22 9 Q24 0 34 3 Q32 12 22 9" fill="#087D63"/><path d="M10 18 Q6 24 9 29" stroke="white" fill="none" stroke-width="2"/></svg>'''
(ASSET/'epal.svg').write_text(APPLE)
PENCIL='''<svg xmlns="http://www.w3.org/2000/svg" width="20" height="90" viewBox="0 0 20 90"><path d="M4 14 H16 V69 L10 86 L4 69 Z" fill="#F2C94C" stroke="#17324B" stroke-width="2"/><path d="M4 14 V5 H16 V14" fill="#D97119" stroke="#17324B" stroke-width="2"/><path d="M4 69 H16 L10 86Z" fill="#F5DEB3" stroke="#17324B" stroke-width="2"/><path d="M8 80 L10 86 L12 80Z" fill="#17324B"/><path d="M10 16 V67" stroke="#17324B"/></svg>'''
(ASSET/'pensel.svg').write_text(PENCIL)

# Every printed arithmetic equation is supplied through eq(), which records
# a machine-checkable identity. Blanks are assessed through explicit data.
ledger=[]; layout=[]
class Book:
 def __init__(self,name,ink=False):
  self.ink=ink; self.name=name; self.page=0
  self.c=canvas.Canvas(str(OUT/name),pagesize=(W,H),pageCompression=1)
  self.c.setTitle('BIJAK MATEMATIK | Rahsia Kuasai Sifir 1–12 | Penanda aras')
  self.c.setAuthor('BIJAK MATEMATIK — edisi pembangunan')
 def color(self,h):
  c=HexColor(h)
  if self.ink:
   if h in [NAVY,GRAY]: return HexColor('#222222' if h==NAVY else '#555555')
   return HexColor('#333333')
  return c
 def box(self,x,y,w,h,color=BLUE,tint=True,dash=False):
  c=self.c;c.setLineWidth(.65);c.setStrokeColor(HexColor('#AAB1B6') if self.ink else self.color(color))
  c.setFillColor(white if self.ink or not tint else Color(*self.color(color).rgb(),alpha=.075))
  if dash:c.setDash(3,2)
  c.roundRect(x*MM,H-(y+h)*MM,w*MM,h*MM,3*MM,stroke=1,fill=1)
  c.setDash()
 def text(self,x,y,s,size=11,bold=False,color=NAVY,align='left'):
  f='BM-Bold' if bold else 'BM'; self.c.setFont(f,size);self.c.setFillColor(self.color(color))
  width=pdfmetrics.stringWidth(s,f,size)/MM
  left=x if align=='left' else x-width/2 if align=='center' else x-width
  # Baseline at y, with conservative top/bottom text bounds.
  layout.append({'file':self.name,'page':self.page,'text':s,'x0':round(left,2),'x1':round(left+width,2),'top':round(y-size/MM*.83,2),'bottom':round(y+size/MM*.23,2)})
  if align=='left':self.c.drawString(x*MM,H-y*MM,s)
  elif align=='center':self.c.drawCentredString(x*MM,H-y*MM,s)
  else:self.c.drawRightString(x*MM,H-y*MM,s)
 def para(self,x,y,s,w,size=10.3,color=NAVY,bold=False,leading=None):
  leading=leading or size/MM*1.44
  for line in simpleSplit(s,'BM-Bold' if bold else 'BM',size,w*MM):
   self.text(x,y,line,size,bold,color); y+=leading
  return y
 def line(self,x,y,w,color='#AAB1B6',dash=False):
  self.c.setStrokeColor(self.color(color));self.c.setLineWidth(.6)
  self.c.setDash(2,2) if dash else self.c.setDash()
  self.c.line(x*MM,H-y*MM,(x+w)*MM,H-y*MM); self.c.setDash()
 def svg(self,name,x,y,w,h):
  drawing=svg2rlg(str(ASSET/name)); drawing.scale(w*MM/drawing.width,h*MM/drawing.height)
  if self.ink:
   # Recursively remove chromatic fills; keep black detail and white space.
   from reportlab.graphics.shapes import Group
   def desaturate(obj):
    for attr in ['fillColor','strokeColor']:
     col=getattr(obj,attr,None)
     if col is not None and hasattr(col,'red'):
      g=.2126*col.red+.7152*col.green+.0722*col.blue
      if attr=='fillColor' and g>.40:g=.96
      setattr(obj,attr,Color(g,g,g))
    for item in getattr(obj,'contents',[]):desaturate(item)
   desaturate(drawing)
  renderPDF.draw(drawing,self.c,x*MM,H-(y+h)*MM)
 def eq(self,x,y,s,size=13,bold=True,color=NAVY):
  ledger.append({'file':self.name,'page':self.page,'equation':s})
  self.text(x,y,s,size,bold,color)
 def tag(self,x,y,s,color=BLUE,w=43):
  self.box(x,y,w,8,color);self.text(x+3,y+5.5,s,8,True,color)
 def header(self,n,title,sub,stage='FAHAM',color=BLUE):
  self.page=n
  self.text(15,20,'BIJAK MATEMATIK',9,True,color)
  self.text(195,20,'PENANDA ARAS • 12 HALAMAN',7.2,False,GRAY,'right')
  self.line(15,24,180,color)
  self.text(15,36,title,21,True)
  self.para(15,44,sub,180,9.5,GRAY)
  self.text(15,281,'RAHSIA KUASAI SIFIR 1–12  /  '+stage,7.4,True,GRAY)
  self.text(195,281,f'{n:02d} / 12',8,True,GRAY,'right')
 def end(self): self.c.showPage()
 def save(self): self.c.save()
 def dots(self,x,y,rows,cols,step=5.5,split=None,r=1.65):
  for i in range(rows):
   for j in range(cols):
    col=BLUE if split is None or j<split else ORANGE
    self.c.setStrokeColor(self.color(col));self.c.setLineWidth(.65)
    self.c.setFillColor(white if self.ink else self.color(col))
    self.c.circle((x+j*step)*MM,H-(y+i*step)*MM,r*MM,stroke=1,fill=1)
    if self.ink and split is not None and j>=split:
     self.c.line((x+j*step-r*.6)*MM,H-(y+i*step-r*.6)*MM,(x+j*step+r*.6)*MM,H-(y+i*step+r*.6)*MM)
 def ruled(self,x,y,w,count=2,gap=8):
  for i in range(count):self.line(x,y+i*gap,w,dash=True)
 def table(self,n,x=15,y=72,w=43,row=7.2):
  self.box(x,y,w,12*row+10,BLUE)
  self.text(x+w/2,y+7,'BACA • TUTUP • CUBA',7.3,True,BLUE,'center')
  for a in range(1,13):self.eq(x+4,y+16+(a-1)*row,f'{a} × {n} = {a*n}',10.3)


def cover(b):
 b.page=1
 b.text(15,21,'BIJAK MATEMATIK',13,True,BLUE)
 b.text(195,21,'EDISI PENANDA ARAS',8,True,GRAY,'right')
 b.line(15,27,180,BLUE)
 b.text(15,47,'RAHSIA',32,True)
 b.text(15,63,'KUASAI SIFIR',32,True)
 b.text(15,86,'1–12',55,True,BLUE)
 b.text(15,100,'Teknik Visual, Formula Mudah',13,True)
 b.text(15,108,'dan Matematik Mental',13,True)
 b.para(15,122,'Faham Dahulu, Kira Dengan Bijak,\nHafal Dengan Mudah!'.replace('\n',' '),99,12,color=GREEN,bold=True)
 b.svg('tiger_bijak.svg',111,112,83,86)
 b.tag(123,202,'TIGER BIJAK',ORANGE,61)
 b.box(15,151,90,53,BLUE)
 b.text(21,161,'LUPA JAWAPAN?',12,True,BLUE)
 b.text(21,169,'Bina semula dengan strategi.',9.4)
 b.eq(21,181,'7 × 8 = (5 × 8) + (2 × 8)',10.3)
 b.eq(21,192,'7 × 8 = 40 + 16 = 56',13)
 for i,(word,col) in enumerate([('FAHAM',BLUE),('KIRA',ORANGE),('INGAT',PURPLE),('KUASAI',GREEN)]):
  b.box(15+i*46,219,42,14,col);b.text(36+i*46,228,word,10,True,col,'center')
 b.text(15,246,'Nama: ______________________________________',11)
 b.text(15,257,'Kelas: ______________    Tarikh mula: ______________',10)
 b.para(15,270,'Sampel untuk semakan reka bentuk • A4 • Umur 7–12 tahun',180,8.8,GRAY)
 b.text(195,281,'01 / 12',8,True,GRAY,'right'); b.end()

DIAG=[
 ('A  KENAL NOMBOR','Baca nombor 14 dan 41. Bulatkan nombor yang lebih besar.'),
 ('B  KUMPULAN SAMA BANYAK','Ada 3 beg. Setiap beg ada 4 epal. Tulis ayat darab: __________'),
 ('C  TAMBAH BERULANG','4 + 4 + 4 = ______'),
 ('D  BILANG LOMPAT','5, 10, 15, ______, 25'),
 ('E  INGAT FAKTA','6 × 7 = ______  Cuba tanpa melihat jadual.'),
 ('F  KIRA SECARA MENTAL','8 × 6 = (8 × 5) + 8 = ______ + 8 = ______'),
 ('G  BEZAKAN FAKTA','7 × 8:  54 / 56     dan     6 × 9:  54 / 56. Bulatkan jawapan.'),
 ('H  GUNA DALAM CERITA','4 kotak ada 6 pensel setiap satu. Jumlah pensel: ______ batang.')]
def diagnostic(b):
 b.header(2,'Di mana saya bermula?','Buat sendiri dahulu. Jika perlu bantuan, tandakan B. Ini bukan perlumbaan.','FAHAM')
 b.text(15,57,'Nama: ____________________   Tarikh: __________   Pemerhati: __________',9.3)
 for i,(label,q) in enumerate(DIAG):
  y=63+i*19.6;b.box(15,y,180,18.1,BLUE if i%2==0 else GREEN)
  b.text(19,y+5.7,label,8,True,BLUE)
  b.para(19,y+12.4,q,158,9.3)
  b.text(189,y+6,'B',8,False,GRAY,'right')
 b.box(15,224,180,47,PURPLE)
 b.text(20,232,'UNTUK ORANG DEWASA • 8 DOMAIN, MAKSIMUM 8 MATA',8.5,True,PURPLE)
 b.para(20,239,'1 mata setiap domain jika tepat tanpa bantuan; 0 jika salah, belum cuba atau dibantu. A perlu bacaan tepat dan pilihan 41; G perlu kedua-duanya tepat.',169,8.8)
 b.para(20,251,'Jika A–D ada 0: mula di halaman 3–4 dan guna objek sebenar. Jika A–D semuanya 1 tetapi E–H ada 0: mula strategi halaman 5–7. Jika semua 1: cuba halaman 9–10.',169,8.8)
 b.text(20,266,'Skor: ____ / 8. Catat cara murid, bukan skor sahaja. Panduan lanjut: halaman 12.',8.2)
 b.end()

def foundations(b):
 b.header(3,'Darab ialah kumpulan sama banyak','JOM FAHAM! Sentuh objek, lihat gambar, kemudian tulis simbol.','FAHAM')
 b.tag(15,54,'1  PEGANG & SUSUN',BLUE,62)
 b.para(15,69,'Ambil 12 penutup botol. Susun menjadi 3 kumpulan, 4 dalam setiap kumpulan.',180,11)
 for i in range(3):
  x=18+i*60;b.box(x,83,54,37,ORANGE)
  for j in range(4):b.svg('epal.svg',x+5+(j%2)*24,87+(j//2)*16,10,12)
  b.text(x+27,127,'4 epal',10,True,ORANGE,'center')
 b.text(15,140,'3 kumpulan × 4 epal setiap kumpulan',13,True)
 b.eq(15,153,'3 × 4 = 4 + 4 + 4 = 12',20,color=BLUE)
 b.tag(15,165,'2  LOMPAT SAMA JAUH',GREEN,72)
 b.text(15,180,'Mula pada 0. Buat 3 lompatan, 4 setiap kali.',10.5)
 b.line(25,202,155,NAVY)
 for i,value in enumerate([0,4,8,12]):
  x=25+i*50;b.c.setStrokeColor(b.color(NAVY));b.c.line(x*MM,H-200*MM,x*MM,H-204*MM)
  b.text(x,212,str(value),11,True,align='center')
  if i<3:
   p=b.c.beginPath();p.moveTo(x*MM,H-199*MM);p.curveTo((x+12)*MM,H-183*MM,(x+38)*MM,H-183*MM,(x+50)*MM,H-199*MM)
   b.c.setStrokeColor(b.color(GREEN));b.c.setLineWidth(1.5);b.c.drawPath(p)
   b.text(x+25,190,'+4',10,True,GREEN,'center')
 b.box(15,225,86,44,BLUE);b.box(107,225,88,44,GREEN)
 b.text(20,233,'DARAB DAN BAHAGI',9,True,BLUE)
 b.eq(20,244,'3 × 4 = 12',13);b.eq(20,254,'12 ÷ 3 = 4',13)
 b.text(20,263,'12 epal diagih ke 3 kumpulan.',8.1)
 b.text(112,233,'SATU BUKAN SIFAR',9,True,GREEN)
 b.eq(112,244,'4 × 1 = 4',13);b.eq(112,254,'4 × 0 = 0',13)
 b.text(112,263,'4 kumpulan kosong: tiada objek.',7.9)
 b.end()

def arrays(b):
 b.header(4,'Pusing susunan, kekal jumlah','JOM FAHAM! Baris melintang. Lajur menegak.','FAHAM')
 b.box(15,56,85,62,BLUE);b.box(110,56,85,62,ORANGE)
 b.dots(32,72,3,4,12,r=3);b.dots(132,67,4,3,12,r=3)
 b.text(57.5,106,'3 baris, 4 lajur',10,True,BLUE,'center')
 b.text(152.5,112,'4 baris, 3 lajur',10,True,ORANGE,'center')
 b.eq(27,131,'3 × 4 = 12',17,color=BLUE);b.eq(119,131,'4 × 3 = 12',17,color=ORANGE)
 b.para(15,145,'Sifat tukar tertib: faktor boleh bertukar tempat. Jumlah tidak berubah. Cerita kumpulannya mungkin berbeza.',180,10.5)
 b.tag(15,164,'MISI SIFIR',PURPLE,45)
 b.para(15,181,'1. Warnakan 3 baris dengan 5 petak setiap baris.\n2. Tulis dua ayat darab bagi petak yang diwarnakan.'.replace('\n',' '),180,10.5)
 x0,y0,sz=22,196,8
 for i in range(5):
  for j in range(6):
   b.c.setStrokeColor(b.color(GRAY));b.c.setFillColor(white)
   b.c.rect((x0+j*sz)*MM,H-(y0+(i+1)*sz)*MM,sz*MM,sz*MM,stroke=1,fill=1)
 b.text(88,204,'______ × ______ = ______',12,True)
 b.text(88,219,'______ × ______ = ______',12,True)
 b.para(88,233,'3. Pada ruang bawah, lukis 2 baris dengan 6 titik setiap baris.',103,10)
 b.ruled(22,254,163,2,12)
 b.end()

def lesson7(b):
 b.header(5,'Sifir 7 • lima tambah dua','KIRA DALAM KEPALA: gunakan sifir 5 dan sifir 2 yang sudah difahami.','KIRA',PURPLE)
 b.box(15,54,180,15,PURPLE);b.eq(22,64,'n × 7 = (n × 5) + (n × 2)',18,color=PURPLE)
 b.table(7,y=76,row=7)
 b.tag(65,76,'JOM FAHAM!',BLUE,45)
 b.dots(71,92,4,7,6,split=5,r=1.8)
 b.text(119,95,'4 baris × 5 = 20',9.4,True,BLUE)
 b.text(119,104,'4 baris × 2 = 8',9.4,True,ORANGE)
 b.eq(119,115,'20 + 8 = 28',12)
 b.text(65,125,'7 lajur dipecah kepada 5 lajur dan 2 lajur.',9)
 b.text(65,138,'TIGA CONTOH KERJA',9,True,PURPLE)
 for i,(a,t) in enumerate([(4,'20 + 8 = 28'),(8,'40 + 16 = 56'),(12,'60 + 24 = 84')]):
  b.eq(65,149+i*10,f'{a} × 7 = {t}',12)
 b.box(65,178,130,28,ORANGE)
 b.text(70,186,'TIP TIGER • JANGAN TAMBAH 2 SAHAJA',8.5,True,ORANGE)
 b.para(70,194,'Daripada n × 5, tambah dua kumpulan n, iaitu n × 2. Corak hasil: bertambah 7 setiap langkah.',119,9.1)
 b.text(15,218,'BIMBINGAN  6 × 7 = 30 + ______ = ______',11,True)
 b.text(15,231,'CUBA SENDIRI  9 × 7 = ______   11 × 7 = ______',11)
 b.text(15,244,'INGAT SEMULA  Tutup jadual:  7 × 7 = ____   8 × 7 = ____',10)
 b.para(15,257,'CARI CARA PALING MUDAH: 9 × 7 boleh juga dikira sebagai (10 × 7) − 7. Terangkan cara pilihan kamu.',180,9.8)
 b.end()

def lesson8(b):
 b.header(6,'Sifir 8 • gandakan tiga kali','Ganda dua bermaksud tambah kuantiti yang sama, bukan tambah 2.','KIRA',GREEN)
 b.box(15,54,180,15,GREEN);b.text(22,64,'n × 8:  n → ganda dua → ganda dua → ganda dua',13,True,GREEN)
 b.table(8,y=76,row=7)
 b.tag(65,76,'JOM FAHAM!',GREEN,45)
 for i,(a,group) in enumerate([(1,'1 bahagian'),(2,'2 bahagian'),(4,'4 bahagian'),(8,'8 bahagian')]):
  y=92+i*11
  for j in range(a):
   b.box(65+j*8,y,7,7,GREEN)
   b.text(68.5+j*8,y+5,'n',8,True,GREEN,'center')
  b.text(135,y+5,group,9.5)
 b.text(65,140,'Setiap pusingan menggandakan jumlah.',8.8)
 b.text(65,152,'TIGA CONTOH KERJA',9,True,GREEN)
 b.eq(65,163,'3 → 6 → 12 → 24',12)
 b.eq(65,174,'7 → 14 → 28 → 56',12)
 b.eq(65,185,'12 → 24 → 48 → 96',12)
 b.box(65,192,130,17,ORANGE)
 b.text(70,199,'CARA LAIN: sepuluh tolak dua',8.5,True,ORANGE)
 b.eq(70,205,'7 × 8 = 70 − 14 = 56',10.5)
 b.text(15,221,'BIMBINGAN  6 → 12 → ______ → ______',11,True)
 b.text(15,234,'CUBA SENDIRI  8 × 8 = ______   11 × 8 = ______',11)
 b.text(15,247,'INGAT SEMULA  Tutup jadual:  9 × 8 = ____   12 × 8 = ____',10)
 b.para(15,260,'TIP TIGER: 7, 14, 28, 56 ialah 3 kali ganda dua. Menggandakan dua kali sahaja memberikan sifir 4.',180,9.8)
 b.end()

def lesson9(b):
 b.header(7,'Sifir 9 • sepuluh tolak satu','Bina sepuluh kumpulan n, kemudian keluarkan satu kumpulan n.','KIRA',ORANGE)
 b.box(15,54,180,15,ORANGE);b.eq(22,64,'n × 9 = (n × 10) − n',18,color=ORANGE)
 b.table(9,y=76,row=7)
 b.text(65,82,'JOM FAHAM!  8 × 10 menjadi 8 × 9',9.5,True,ORANGE)
 # Ten equal blocks of 8; last block crossed out.
 for j in range(10):
  x=66+j*12.5;b.box(x,88,11,12,BLUE if j<9 else ORANGE)
  b.text(x+5.5,96,'8',9,True,align='center')
  if j==9:
   b.c.setStrokeColor(b.color(ORANGE));b.c.line(x*MM,H-88*MM,(x+11)*MM,H-100*MM)
 b.text(65,109,'10 bahagian lapan, tolak 1 bahagian lapan.',8.5)
 b.eq(65,123,'4 × 9 = 40 − 4 = 36',12)
 b.eq(65,134,'8 × 9 = 80 − 8 = 72',12)
 b.eq(65,145,'12 × 9 = 120 − 12 = 108',12)
 b.text(65,158,'BIMBINGAN  7 × 9 = 70 − ____ = ____',9.4,True)
 b.text(65,170,'CUBA  6 × 9 = ____   11 × 9 = ____',10)
 b.box(15,178,180,49,PURPLE)
 b.text(20,186,'TEKNIK 10 JARI • HANYA UNTUK FAKTOR 1 HINGGA 10',8.8,True,PURPLE)
 b.para(20,193,'Buka kedua-dua tangan. Nomborkan jari 1–10 dari kiri ke kanan. Untuk 8 × 9, lipat jari ke-8.',169,9)
 for j in range(10):
  x=25+j*11;b.box(x,204 if j!=7 else 210,7,12 if j!=7 else 6,PURPLE)
  b.text(x+3.5,222,str(j+1),8,False,PURPLE,'center')
 b.text(143,209,'Kiri: 7 puluh',9,True)
 b.text(143,219,'Kanan: 2 sa',9,True)
 b.para(15,236,'CORAK 9 × 1 hingga 9 × 10: 09, 18, 27, 36, 45, 54, 63, 72, 81, 90. Digit puluh naik; digit sa turun. Tidak terus begitu untuk 99 dan 108.',180,9.2)
 b.para(15,253,'Semak digit: 7 + 2 = 9, tetapi 63 juga berjumlah digit 9. Corak digit sahaja tidak membuktikan jawapan betul. Jangan guna teknik jari ini untuk 11 atau 12.',180,9.2)
 b.text(15,270,'INGAT SEMULA  Tutup jadual:  9 × 9 = ______   12 × 9 = ______',10,True)
 b.end()

CARDS=[
 (1,'KEKAL SAMA','n × 1 = n','7 × 1 = 7'),
 (2,'GANDA DUA','n × 2 = n + n','7 × 2 = 7 + 7 = 14'),
 (3,'DUA TAMBAH SATU','n × 3 = (n × 2) + n','8 × 3 = 16 + 8 = 24'),
 (4,'GANDA DUA KALI','n → 2n → 4n','7 → 14 → 28'),
 (5,'SEPARUH SEPULUH','n × 5 = (n × 10) ÷ 2','7 × 5 = 70 ÷ 2 = 35'),
 (6,'LIMA TAMBAH SATU','n × 6 = (n × 5) + n','7 × 6 = 35 + 7 = 42'),
 (7,'LIMA TAMBAH DUA','n × 7 = (n × 5) + (n × 2)','8 × 7 = 40 + 16 = 56'),
 (8,'GANDA TIGA KALI','n → 2n → 4n → 8n','7 → 14 → 28 → 56'),
 (9,'SEPULUH TOLAK SATU','n × 9 = (n × 10) − n','8 × 9 = 80 − 8 = 72'),
 (10,'NILAI TEMPAT','n × 10: nilai digit × 10','12 × 10 = 120'),
 (11,'SEPULUH TAMBAH SATU','n × 11 = (n × 10) + n','12 × 11 = 120 + 12 = 132'),
 (12,'SEPULUH TAMBAH DUA','n × 12 = (n × 10) + (n × 2)','8 × 12 = 80 + 16 = 96')]
def cards(b):
 b.header(8,'Kad poket • 12 strategi','n ialah nombor yang didarab. Garis putus-putus ialah garis potong.','KIRA → INGAT',PURPLE)
 b.para(15,56,'Cetak satu muka pada skala 100%. Gunting dengan bantuan orang dewasa. Untuk nombor bulat dalam buku ini; kad 10 bukan petua umum bagi perpuluhan.',180,9.2)
 for i,(n,title,formula,example) in enumerate(CARDS):
  x=15+(i%3)*61.5;y=71+(i//3)*47.8;col=[BLUE,GREEN,PURPLE,ORANGE][i%4]
  b.box(x,y,57,43.5,col,dash=True)
  b.text(x+4,y+9,f'SIFIR {n}',13,True,col)
  b.text(x+4,y+16,title,6.4,True)
  # Formula sizes fit even long factor decomposition.
  fs=8.2 if n not in [7,11,12] else 7
  if n not in [4,8,10]: b.eq(x+4,y+25,formula,fs)
  else:b.text(x+4,y+25,formula,fs,True)
  if n not in [4,8]:b.eq(x+4,y+34,example,7.9 if n!=11 else 7)
  else:b.text(x+4,y+34,example,8.8,True)
 b.text(15,271,'TIP TIGER: pilih strategi yang kamu faham. Kad ini membantu mengira, bukan mengganti penerangan.',8.3)
 b.end()

MAZE=[[(7,2),(3,7),(6,6),(8,8)],[(9,9),(7,4),(6,8),(8,9)],[(6,9),(5,7),(7,6),(4,9)],[(3,8),(9,10),(8,7),(7,9)]]
MAZE_PATH=[(0,0),(0,1),(1,1),(2,1),(2,2),(3,2),(3,3)]
CODE=[(6,7,'H'),(7,8,'E'),(7,9,'B'),(8,8,'A'),(8,9,'T')]
def games(b):
 b.header(9,'Misi kertas • cari, kira, semak','Dua aktiviti boleh dimainkan sendiri atau berpasangan. Tiada had masa.','INGAT',GREEN)
 b.tag(15,55,'A  JEJAK GANDAAN 7',GREEN,72)
 b.para(15,70,'Mula di kiri atas. Kira hasil darab. Gerak satu petak ke atas, bawah, kiri atau kanan hanya jika hasilnya gandaan 7. Jangan ulang petak. Cari jalan ke TAMAT.',180,10)
 x0,y0,sz=19,91,27
 for i in range(4):
  for j in range(4):
   x=x0+j*sz;y=y0+i*sz;b.box(x,y,sz-1,sz-1,GREEN)
   if (i,j)==(0,0):b.text(x+13,y+6,'MULA',7,True,GREEN,'center')
   if (i,j)==(3,3):b.text(x+13,y+6,'TAMAT',7,True,GREEN,'center')
   a,c=MAZE[i][j];b.text(x+13,y+17,f'{a} × {c}',13,True,align='center')
 b.svg('tiger_bijak.svg',143,99,43,45)
 b.para(139,157,'Tulis hasil pada petak. Kemudian lukis laluan dengan pensel.',52,10)
 b.tag(15,208,'B  KOD RAHSIA',PURPLE,60)
 b.text(15,224,'Kunci: 42 → H   56 → E   63 → B   64 → A   72 → T',11,True,PURPLE)
 for j,(a,c,char) in enumerate(CODE):
  x=15+j*36.8;b.box(x,232,33,26,PURPLE)
  b.text(x+16.5,241,f'{a} × {c}',11,True,align='center')
  b.text(x+16.5,252,'___ → ___',10,align='center')
 b.text(15,269,'CABARAN BIJAK: terangkan satu pengiraan kamu kepada rakan.',10)
 b.end()

DAILY_RECALL=[(6,7),(7,8),(8,8),(9,7),(12,7),(11,8),(9,9),(12,9)]
def daily(b):
 b.header(10,'Latihan harian • bina keyakinan','Contoh helaian 10–15 minit. Pendekkan sesi jika penat; ketepatan didahulukan.','KIRA → INGAT')
 b.text(15,57,'Nama: ______________________   Tarikh: __________   Sesi: ______',9.6)
 b.box(15,64,180,26,BLUE)
 b.text(20,72,'1  PANASKAN MINDA',8.8,True,BLUE)
 b.text(20,83,'Ganda dua 8: ____    5, 10, 15, ____, ____    4 + 4 + 4 = ____',10.8)
 b.box(15,96,180,25,GREEN)
 b.text(20,104,'2  ULANG FAKTA LAMA',8.8,True,GREEN)
 b.text(20,115,'7 × 5 = ____       8 × 2 = ____       12 × 10 = ____',11.5)
 b.box(15,127,180,33,ORANGE)
 b.text(20,135,'3  SATU STRATEGI • LIMA TAMBAH DUA',8.8,True,ORANGE)
 b.eq(20,145,'8 × 7 = (8 × 5) + (8 × 2) = 40 + 16 = 56',12)
 b.text(20,155,'Ikut cara ini:  6 × 7 = (6 × 5) + (6 × 2) = ____ + ____ = ____',10.3)
 b.text(15,173,'4  CUBA INGAT • JIKA LUPA, BINA SEMULA',9.5,True,PURPLE)
 for i,(a,c) in enumerate(DAILY_RECALL):
  b.text(18+(i%4)*45,186+(i//4)*13,f'{a} × {c} = ____',11)
 b.box(15,208,180,33,GREEN)
 b.text(20,216,'5  CERITA HARI INI',8.8,True,GREEN)
 b.text(20,225,'Ada 7 kotak buku. Setiap kotak ada 8 buku. Berapa jumlah buku?',10)
 b.text(20,236,'Ayat matematik: __________________  Jawapan: __________ buku',10)
 b.text(15,253,'6  REFLEKSI  □ Perlu gambar  □ Boleh kira  □ Boleh ingat sendiri',10)
 b.text(15,264,'Satu fakta untuk diulang: __________   Cara saya: __________________',9.4)
 b.text(15,272,'Ulang fakta ini selepas kira-kira 1, 3, 7 dan 14 hari. Catat tarikh: ____ / ____ / ____ / ____',8.1)
 b.end()

def answers(b):
 b.header(11,'Jawapan & semakan kendiri','Semak selepas mencuba. Baca strategi; betulkan satu langkah pada satu masa.','SEMAK',GREEN)
 # Two columns; references explicit and stable in both editions.
 x=15;w=86
 b.text(x,60,'HALAMAN 2 • DIAGNOSTIK',10,True,BLUE)
 y=b.para(x,69,'A: 14 (empat belas), 41 (empat puluh satu); bulatkan 41. B: 3 × 4 = 12; terima 4 × 3 = 12 jika murid boleh menerangkan 3 kumpulan empat.',w,9.5)
 y=b.para(x,y+2,'C: 12. D: 20. E: 42. F: 40, 48. G: 56 dan 54. H: 24 batang pensel.',w,9.5)
 b.text(x,118,'HALAMAN 3–4 • ASAS',10,True,BLUE)
 b.para(x,127,'Hlm. 3: contoh berpandu. Hlm. 4: warnakan 15 petak; 3 × 5 = 15 dan 5 × 3 = 15. Lukisan: 2 baris, 6 titik sebaris; 12 titik.',w,9.5)
 b.text(x,156,'HALAMAN 5 • SIFIR 7',10,True,PURPLE)
 b.para(x,165,'Bimbingan: 12, 42. Sendiri: 63, 77. Ingat semula: 49, 56. Cara lain bagi 9 × 7: 70 − 7 = 63.',w,9.5)
 b.text(x,192,'HALAMAN 6 • SIFIR 8',10,True,GREEN)
 b.para(x,201,'Bimbingan: 24, 48. Sendiri: 64, 88. Ingat semula: 72, 96. Tiga ganda dua bagi 6 ialah 12, 24, 48.',w,9.5)
 b.text(x,228,'HALAMAN 7 • SIFIR 9',10,True,ORANGE)
 b.para(x,237,'Bimbingan: 7, 63. Cuba: 54, 99. Ingat semula: 81, 108. Jari ke-8: 7 di kiri dan 2 di kanan → 72.',w,9.5)
 b.line(105,55,0)
 x=111;w=84
 b.text(x,60,'HALAMAN 8 • KAD POKET',10,True,PURPLE)
 b.para(x,69,'Bahan rujukan; tiada item untuk dijawab. Kad 4 dan 8 menunjukkan penggandaan berperingkat.',w,9.5)
 b.text(x,95,'HALAMAN 9 • JEJAK & KOD',10,True,GREEN)
 b.para(x,104,'A: hasil di laluan ialah 14 → 21 → 28 → 35 → 42 → 56 → 63. Laluan tunggal ditunjukkan di bawah.',w,9.5)
 for i in range(4):
  for j in range(4):
   xx=x+j*12;yy=126+i*10
   b.box(xx,yy,11,9,GREEN,tint=(i,j) in MAZE_PATH)
   if (i,j) in MAZE_PATH:b.text(xx+5.5,yy+6,str(MAZE_PATH.index((i,j))+1),9,True,GREEN,'center')
 b.text(x,177,'B: 42, 56, 63, 64, 72 → HEBAT.',9.5,True,PURPLE)
 b.text(x,193,'HALAMAN 10 • HARIAN',10,True,BLUE)
 b.para(x,202,'1: 16; 20, 25; 12. 2: 35, 16, 120. 3: 30 + 12 = 42. 4: mengikut turutan kiri ke kanan, baris atas dahulu: 42, 56, 64, 63, 84, 88, 81, 108.',w,9.5)
 b.para(x,236,'5: 7 × 8 = 56, jadi 56 buah buku. 6: jawapan peribadi; pilih fakta yang belum stabil.',w,9.5)
 b.text(15,269,'Silap ialah maklumat. Cuba semula tanpa melihat jawapan selepas beberapa soalan lain.',9.5,True,GREEN)
 b.end()

def guide(b):
 b.header(12,'Panduan ibu bapa & guru','Gunakan penanda aras untuk menilai kesesuaian reka bentuk, bahasa dan aras.','PANDUAN',PURPLE)
 b.text(15,58,'01  MULAKAN DENGAN PEMAHAMAN',10,True,BLUE)
 b.para(15,66,'Gunakan halaman 2 sebagai saringan ringkas, bukan ujian piawai atau diagnosis klinikal. Satu item tidak mengesahkan penguasaan domain. Baca arahan jika perlu dan catat bantuan; minta 2–3 contoh tambahan untuk menyemak kesukaran. Jika kenal nombor atau kumpulan belum kukuh, ulang halaman 3–4 dengan objek.',180,9.2)
 b.text(15,91,'02  RUTIN RINGKAS TANPA TEKANAN',10,True,GREEN)
 b.para(15,99,'Ambil kira-kira 10–15 minit: 2 minit objek/gambar, 3 minit contoh dan latihan berpandu, 3–5 minit cuba ingat, 2 minit semak serta bincang. Campur fakta lama dan baharu. Kurangkan bantuan secara beransur-ansur. Jangan hukum kiraan perlahan; masa hanyalah pilihan apabila murid tepat dan yakin.',180,9.2)
 b.text(15,124,'03  DENGAR CARANYA, BUKAN JAWAPAN SAHAJA',10,True,ORANGE)
 b.para(15,132,'Dewasa: “Bagaimana kamu mendapat 54 untuk 7 × 8?” Anak: “Saya terlupa.” Dewasa: “Tidak mengapa. Kita tahu 5 × 8 = 40. Berapa 2 × 8?” Anak: “16.” Dewasa: “Jadi 40 + 16?” Anak: “56!” Cuba fakta itu sekali lagi selepas beberapa soalan lain.',180,9.2)
 b.text(15,157,'04  ULANG, LARAS DAN CATAT',10,True,PURPLE)
 b.para(15,165,'Pilih 3–5 fakta yang belum stabil. Cuba dahulu, semak kemudian. Ulang sekitar 1, 3, 7 dan 14 hari; sela ini ialah cadangan praktikal, bukan jadual wajib daripada kajian. Jika masih sukar menjelaskan atau kerap tersilap, kembali kepada gambar dan ulang pelajaran. Tandakan kemajuan sendiri, bukan banding dengan rakan. Tiada jaminan hafal dalam 30 hari.',180,9.2)
 b.text(15,194,'05  CETAK DENGAN BETUL',10,True,BLUE)
 b.para(15,202,'A4 potret, saiz sebenar / 100%, tanpa “fit to page”. Semua kandungan utama dalam margin 15 mm. Kedua-dua edisi setara; edisi jimat dakwat menggunakan garisan dan label, bukan warna sahaja. Halaman 8: cetak satu muka, potong garis putus-putus dengan pengawasan dewasa. Ukur garis ini: 50 mm.',158,8.7)
 b.line(15,225,50,NAVY);b.line(15,223,0);b.line(65,223,0)
 b.text(15,237,'RUJUKAN PENDEK • ASAS REKA BENTUK PEMBELAJARAN',9,True,PURPLE)
 b.para(15,245,'[1] Pashler, H. et al. (2007). Organizing Instruction and Study to Improve Student Learning. IES, NCER 2007-2004. Cadangan 1–5 dan 7: sela, contoh, visual, konkrit–abstrak, kuiz dan penjelasan. ies.ed.gov/ncee/wwc/practiceguide/1',180,8)
 b.para(15,261,'[2] Education Endowment Foundation (2017). Improving Mathematics in Key Stages Two and Three. Cadangan 1–5: penilaian, representasi, strategi, hubungan dan motivasi. Pautan penuh dalam fail RUJUKAN.md. Produk ini belum diuji keberkesanannya secara khusus.',180,8)
 b.end()


def build():
 for ink in [False,True]:
  b=Book('BIJAK_MATEMATIK_BENCHMARK_'+('INKSAVING' if ink else 'COLOR')+'.pdf',ink)
  for fn in [cover,diagnostic,foundations,arrays,lesson7,lesson8,lesson9,cards,games,daily,answers,guide]:fn(b)
  b.save()
 (QA/'equation_ledger.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2))
 (QA/'layout_ledger.json').write_text(json.dumps(layout,ensure_ascii=False,indent=2))
 (ROOT/'source'/'activity_data.json').write_text(json.dumps({'maze':MAZE,'maze_path':MAZE_PATH,'code':CODE,'daily_recall':DAILY_RECALL,'cards':CARDS},ensure_ascii=False,indent=2))
 print('Created both 12-page benchmark editions.')
if __name__=='__main__':build()

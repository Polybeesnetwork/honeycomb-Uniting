"""Shared vector publishing system, content registries and reusable components."""
from pathlib import Path
import json,math,random
import build_benchmark as B
from reportlab.lib.colors import HexColor,white,Color
from reportlab.pdfbase import pdfmetrics
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'pdf';QA=ROOT/'qa';ASSET=ROOT/'assets'
B.OUT=OUT;B.ASSET=ASSET
MM=B.MM;W=B.W;H=B.H
BLUE=B.BLUE;ORANGE=B.ORANGE;GREEN=B.GREEN;PURPLE=B.PURPLE;NAVY=B.NAVY;GRAY=B.GRAY;YELLOW=B.YELLOW
QUESTIONS={};PAGES=[];GEOMETRY=[];DOCS={}
COLORS=[BLUE,GREEN,PURPLE,ORANGE]
STRATEGIES={
1:('Kekal sama','n × 1 = n','Satu kumpulan n, atau n kumpulan satu: kuantiti asal kekal.','Jangan keliru × 1 dengan + 1.','Hasil sama seperti nombor asal.'),
2:('Ganda dua','n × 2 = n + n','Dua kumpulan sama banyak boleh ditambah.','Ganda dua bukan tambah 2.','Semua hasil ialah nombor genap.'),
3:('Dua tambah satu','n × 3 = (n × 2) + n','Pecahkan tiga kumpulan kepada dua kumpulan dan satu kumpulan.','Selepas ganda dua, tambah n, bukan tambah 3.','Hasil bertambah 3 setiap langkah.'),
4:('Ganda dua kali','n → 2n → 4n','Satu bahagian menjadi dua, kemudian empat bahagian yang sama.','Dua kali ganda dua bukan n + 4.','Gandakan hasil sifir 2 untuk mendapat sifir 4.'),
5:('Separuh sepuluh','n × 5 = (n × 10) ÷ 2','Lima kumpulan ialah separuh daripada sepuluh kumpulan sama banyak.','Bahagikan keseluruhan hasil sifir 10 dengan 2.','Digit sa berselang-seli 5 dan 0.'),
6:('Lima tambah satu','n × 6 = (n × 5) + n','Enam kumpulan boleh dipisah menjadi lima dan satu.','Tambah satu kumpulan n, bukan tambah 1.','Cara lain: gandakan hasil sifir 3.'),
7:('Lima tambah dua','n × 7 = (n × 5) + (n × 2)','Tujuh lajur boleh dipisah menjadi lima lajur dan dua lajur.','Tambah dua kumpulan n, bukan tambah 2.','Hasil seterusnya bertambah 7.'),
8:('Ganda tiga kali','n → 2n → 4n → 8n','Tiga pusingan ganda dua menghasilkan lapan bahagian sama banyak.','Dua pusingan sahaja menghasilkan sifir 4, bukan 8.','Cara lain: sifir 10 tolak sifir 2.'),
9:('Sepuluh tolak satu','n × 9 = (n × 10) − n','Sembilan kumpulan ialah sepuluh kumpulan ditolak satu kumpulan.','Tolak n, bukan tolak 1.','Bagi 9 hingga 90: puluh naik, sa turun.'),
10:('Nilai tempat','n × 10: nilai setiap digit menjadi 10 kali','Bagi nombor bulat, setiap digit beralih satu tempat ke kiri dalam carta nilai tempat.','Tambah sifar di hujung hanya petua nombor bulat di sini.','Contoh: 12 menjadi 120, bukan 12 + 10.'),
11:('Sepuluh tambah satu','n × 11 = (n × 10) + n','Sebelas kumpulan boleh dipecah kepada sepuluh dan satu.','Digit berulang hanya petua faktor satu digit.','1 × 11 hingga 9 × 11: 11, 22, …, 99.'),
12:('Sepuluh tambah dua','n × 12 = (n × 10) + (n × 2)','Dua belas kumpulan ialah sepuluh kumpulan dan dua kumpulan.','Tambah dua kali n, bukan tambah 2.','Gunakan sifir 10 sebagai fakta sauh.')}

def work(n,k):
 p=n*k
 if k==1:return f'{n} × 1 = {n}'
 if k==2:return f'{n} × 2 = {n} + {n} = {p}'
 if k==3:return f'{n} × 3 = {2*n} + {n} = {p}'
 if k==4:return f'{n} → {2*n} → {4*n}'
 if k==5:return f'{n} × 5 = {10*n} ÷ 2 = {p}'
 if k==6:return f'{n} × 6 = {5*n} + {n} = {p}'
 if k==7:return f'{n} × 7 = {5*n} + {2*n} = {p}'
 if k==8:return f'{n} → {2*n} → {4*n} → {8*n}'
 if k==9:return f'{n} × 9 = {10*n} − {n} = {p}'
 if k==10:return f'{n} × 10 = {p}'
 if k==11:return f'{n} × 11 = {10*n} + {n} = {p}'
 return f'{n} × 12 = {10*n} + {2*n} = {p}'

def answer_text(a):return ', '.join(map(str,a)) if isinstance(a,(list,tuple)) else str(a)
class Book(B.Book):
 def __init__(self,filename,code,label,ink=False):
  super().__init__(filename,ink);self.code=code;self.label=label;self.count=0
  self.c.setTitle('BIJAK MATEMATIK | '+label);self.c.setAuthor('BIJAK MATEMATIK')
 def start(self,title,sub='',stage='FAHAM',color=BLUE,kind='lesson'):
  self.count+=1;self.page=self.count
  self.text(15,20,'BIJAK MATEMATIK',9,True,color)
  self.text(195,20,self.label.upper(),7.2,False,GRAY,'right');self.line(15,24,180,color)
  fs=21
  while pdfmetrics.stringWidth(title,'BM-Bold',fs)>180*MM:fs-=.5
  self.text(15,36,title,fs,True)
  self.para(15,44,sub,180,9.2,GRAY)
  self.text(15,281,self.code+' / '+stage,7.5,True,GRAY)
  self.text(195,281,f'{self.page:02d}',8,True,GRAY,'right')
  PAGES.append({'file':self.name,'page':self.page,'title':title,'kind':kind})
 def header(self,n,title,sub,stage='FAHAM',color=BLUE):self.start(title,sub,stage,color)
 def save(self):
  super().save();DOCS[self.name]={'pages':self.count,'code':self.code,'label':self.label}
 def rect(self,x,y,w,h,color=BLUE,fill=False,dash=False):
  self.c.setStrokeColor(self.color(color));self.c.setLineWidth(.65);self.c.setFillColor(white if self.ink or not fill else Color(*self.color(color).rgb(),alpha=.1))
  if dash:self.c.setDash(3,2)
  self.c.rect(x*MM,H-(y+h)*MM,w*MM,h*MM,stroke=1,fill=1);self.c.setDash()
  GEOMETRY.append({'file':self.name,'page':self.page,'x':x,'y':y,'w':w,'h':h,'type':'rect'})
 def record(self,qid,prompt,ans,calc=None,note=''):
  new={'id':qid,'prompt':prompt,'answer':answer_text(ans),'calc':calc,'note':note,'refs':[]}
  if qid in QUESTIONS:
   assert QUESTIONS[qid]['answer']==new['answer'],(qid,new)
  else:QUESTIONS[qid]=new
  QUESTIONS[qid]['refs'].append({'file':self.name,'page':self.page})
 def q(self,qid,x,y,a,b,kind='mul',size=11,label=True,show=True):
  if kind=='mul':prompt=f'{a} × {b}';ans=a*b;calc=['mul',a,b]
  elif kind=='div':prompt=f'{a} ÷ {b}';ans=a//b;calc=['div',a,b]
  elif kind=='missing':prompt=f'{a} × ____ = {a*b}';ans=b;calc=['missing',a,a*b]
  elif kind=='add':prompt=f'{a} + {b}';ans=a+b;calc=['add',a,b]
  elif kind=='sub':prompt=f'{a} − {b}';ans=a-b;calc=['sub',a,b]
  self.record(qid,prompt,ans,calc)
  if show:
   s=(qid+'  ' if label else '')+prompt+(' = ____' if kind!='missing' else '')
   self.text(x,y,s,size)
  return ans
 def answer_box(self,x,y,w,h,label=''):
  self.rect(x,y,w,h,GRAY)
  if label:self.text(x+3,y+5,label,8,False,GRAY)

def grid(b,x,y,cell=12,mode='full',legend=True):
 for r in range(13):
  for c in range(13):
   xx=x+c*cell;yy=y+r*cell
   color=BLUE if r==0 or c==0 else PURPLE if r==c else GREEN if r<c else ORANGE
   b.rect(xx,yy,cell,cell,color,fill=(mode=='full' or r==0 or c==0))
   if r==0 and c==0:s='×'
   elif r==0:s=str(c)
   elif c==0:s=str(r)
   elif mode=='full':s=str(r*c)
   else:s=''
   if s:b.text(xx+cell/2,yy+cell*.66,s,10.2 if cell>=12 else 9,True,color,'center')

def calendar_data():
 topics={1:'Kumpulan sama banyak',2:'Susunan dan tukar tertib',3:'Sifir 1 dan sifar',4:'Sifir 2',5:'Sifir 5',6:'Sifir 10',7:'Ulang asas',8:'Sifir 3',9:'Sifir 4',10:'Sifir 9',11:'Campur 3, 4 dan 9',12:'Darab dan bahagi',13:'Pilih strategi',14:'Ulang kumulatif',15:'Sifir 6',16:'Sifir 7',17:'Sifir 8',18:'Fakta 6, 7 dan 8',19:'Fakta jiran',20:'Cerita sifir',21:'Ulang kumulatif',22:'Sifir 11',23:'Sifir 12',24:'Darab dan bahagi',25:'Campur semua sifir',26:'Matematik mental',27:'Aplikasi harian',28:'Ulang kumulatif',29:'Ulang fakta peribadi',30:'Penilaian akhir'}
 introduced={3:[1],4:[2],5:[5],6:[10],8:[3],9:[4],10:[9],15:[6],16:[7],17:[8],22:[11],23:[12]}
 days=[]
 for d in range(1,31):
  reviews=sorted({k for day,ks in introduced.items() for k in ks if d-day in [1,3,7,14]})
  known=sorted({k for day,ks in introduced.items() for k in ks if day<d})
  days.append({'day':d,'topic':topics[d],'new':introduced.get(d,[]),'reviews':reviews,'known':known})
 return days
DAYS=calendar_data()

def calendar(b,title='30 hari • sedikit tetapi kerap'):
 b.start(title,'Kira-kira 10–15 minit sehari; laras mengikut keperluan. Tandakan selepas mencuba.','PELAN',GREEN,kind='calendar')
 for d in DAYS:
  i=d['day']-1;x=15+(i%5)*36.5;y=60+(i//5)*32.2
  b.box(x,y,34,30,GREEN if d['day']<8 else BLUE if d['day']<15 else ORANGE if d['day']<22 else PURPLE)
  b.text(x+3,y+6,f"{d['day']:02d}  □",9,True)
  b.para(x+3,y+12,d['topic'],28,7.1,leading=3.6)
  rev='Ulang: '+(', '.join(map(str,d['reviews'])) if d['reviews'] else 'fakta lama')
  b.para(x+3,y+25,rev,28,6.5,leading=3.2)
 b.para(15,264,'Ulang fakta baharu selepas kira-kira 1, 3, 7 dan 14 hari jika masih dalam jadual. Teruskan sela di luar 30 hari. Ini pelan latihan, bukan janji penguasaan.',180,9)
 b.end()

def export_registries():
 (QA/'questions.json').write_text(json.dumps(list(QUESTIONS.values()),ensure_ascii=False,indent=2))
 (QA/'equations.json').write_text(json.dumps(B.ledger,ensure_ascii=False,indent=2))
 (QA/'layout.json').write_text(json.dumps(B.layout,ensure_ascii=False,indent=2))
 (QA/'geometry.json').write_text(json.dumps(GEOMETRY,ensure_ascii=False,indent=2))
 (QA/'pages.json').write_text(json.dumps(PAGES,ensure_ascii=False,indent=2))
 (QA/'documents.json').write_text(json.dumps(DOCS,ensure_ascii=False,indent=2))
 (ROOT/'source/calendar_data.json').write_text(json.dumps(DAYS,ensure_ascii=False,indent=2))

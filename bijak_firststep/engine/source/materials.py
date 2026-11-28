from core import *
from main_workbook import FOCUS
from reportlab.graphics.shapes import Drawing,Path as GPath

FLASH_LAYOUT=[]
def circle(b,x,y,r,col=BLUE,fill=False,dash=False):
 b.c.setStrokeColor(b.color(col));b.c.setFillColor(white);b.c.setLineWidth(.8)
 if dash:b.c.setDash(3,2)
 b.c.circle(x*MM,H-y*MM,r*MM,stroke=1,fill=fill);b.c.setDash()
def seg(b,x1,y1,x2,y2,col=GRAY,dash=False):
 b.c.setStrokeColor(b.color(col));b.c.setLineWidth(.65)
 if dash:b.c.setDash(3,2)
 b.c.line(x1*MM,H-y1*MM,x2*MM,H-y2*MM);b.c.setDash()

def formula_deck(b,page):
 b.start(f'Kad poket • set {page}/2','Garis luar putus-putus: potong. Kad ini digunakan satu muka.','ALAT',PURPLE,'cutout')
 for i,k in enumerate(range(1+(page-1)*6,1+page*6)):
  x=15+(i%2)*94;y=62+(i//2)*66;title,formula,why,mistake,pattern=STRATEGIES[k];col=COLORS[(k-1)%4]
  b.box(x,y,86,59,col,dash=True);b.text(x+5,y+10,f'SIFIR {k} • {title.upper()}',8.8,True,col)
  b.para(x+5,y+21,formula,76,10.2,bold=True)
  b.eq(x+5,y+36,work(7,k),10.3)
  b.para(x+5,y+46,pattern,76,8.3)
 b.text(15,272,'n ialah nombor yang didarab. Pilih strategi yang kamu faham, bukan semata-mata paling pendek.',8.7);b.end()

def wheel_base(b,k=None):
 b.start('Roda sifir • tapak '+(str(k) if k else 'boleh isi'),'Cetak 100%. Potong bulatan luar; lubang pusat dibuat oleh orang dewasa.','ALAT',BLUE,'wheel')
 cx,cy,r=105,153,70
 circle(b,cx,cy,r,BLUE);circle(b,cx,cy,29,GRAY);circle(b,cx,cy,49,GRAY)
 for i in range(12):
  a=math.radians(90-i*30);edge=math.radians(105-i*30)
  seg(b,cx+29*math.cos(edge),cy-29*math.sin(edge),cx+70*math.cos(edge),cy-70*math.sin(edge))
  b.text(cx+59*math.cos(a),cy-59*math.sin(a)+1.5,str(i+1),13,True,BLUE,'center')
  b.text(cx+39*math.cos(a),cy-39*math.sin(a)+1.5,str((i+1)*k) if k else '___',11,True,GREEN,'center')
 circle(b,cx,cy,2,NAVY);b.text(cx,cy-12,'SIFIR '+(str(k) if k else '____'),13,True,BLUE,'center')
 b.text(cx,cy+15,'FAKTOR → HASIL',7,True,align='center')
 b.para(15,242,'Baca nombor luar sebagai faktor. Nombor di gelang dalam ialah hasil. Untuk tapak kosong, pilih satu sifir 1–12 dan isi semua hasil dengan bantuan peta sifir.',180,10.2)
 b.text(15,271,'Simpan tapak yang tidak digunakan. Satu penutup boleh digunakan untuk setiap tapak.',9);b.end()

def wheel_cover(b):
 b.start('Roda sifir • penutup bertingkap','Potong bulatan luar dan tingkap bergaris putus-putus. Dewasa mengendalikan lubang.','ALAT',ORANGE,'wheel')
 cx,cy,r=105,153,70;circle(b,cx,cy,r,BLUE,True)
 pts=[]
 for radius,angles in [(67,range(80,101,2)),(29,range(100,79,-2))]:
  for deg in angles:
   a=math.radians(deg);pts.append((cx+radius*math.cos(a),cy-radius*math.sin(a)))
 p=b.c.beginPath();p.moveTo(pts[0][0]*MM,H-pts[0][1]*MM)
 for x,y in pts[1:]:p.lineTo(x*MM,H-y*MM)
 p.close();b.c.setDash(3,2);b.c.setStrokeColor(b.color(ORANGE));b.c.drawPath(p,stroke=1,fill=0);b.c.setDash()
 b.text(105,73,'POTONG TINGKAP INI',10,True,ORANGE,'center')
 b.text(105,153-15,'TIGER BIJAK',13,True,BLUE,'center');circle(b,105,153,2,NAVY)
 b.text(105,179,'Kira dahulu, kemudian semak.',9.8,True,align='center')
 b.text(105,193,'Sifir: ______',12,True,align='center')
 b.para(15,241,'Letakkan penutup ini di atas tapak. Tingkap memperlihatkan satu faktor dan hasilnya. Tutup hasil dengan jari ketika mencuba ingat; alihkan jari untuk menyemak.',180,10.5)
 b.end()

def assembly(b):
 b.start('Pasang roda dengan selamat','Bahan: tapak, penutup, gunting, kad keras dan pengikat berkaki dua.','ALAT',GREEN)
 for x,y,r in [(55,108,27),(132,108,27)]:circle(b,x,y,r,BLUE)
 b.text(55,109,'TAPAK',12,True,BLUE,'center');b.text(132,109,'PENUTUP',11,True,BLUE,'center')
 seg(b,86,108,100,108,ORANGE);b.text(93,103,'+',14,True,ORANGE,'center')
 b.text(105,153,'↓ susun, tebuk pusat, pasang pengikat ↓',11,True,GREEN,'center')
 circle(b,105,195,27,BLUE);circle(b,105,195,2,NAVY)
 b.text(105,211,'BOLEH DIPUSING',8,True,BLUE,'center')
 b.para(15,238,'1. Lekatkan helaian pada kad jika mahu lebih kukuh. 2. Potong bentuk luar. 3. Dewasa memotong tingkap dan menebuk kedua-dua pusat. 4. Sambung dengan pengikat yang tidak terlalu ketat. 5. Pastikan tiada hujung tajam terdedah.',180,9.8)
 b.text(15,271,'Jangan gunakan pisau atau penebuk tanpa pengawasan orang dewasa.',9.5,True,ORANGE);b.end()

def flipbook(b,part):
 b.start(f'Buku selak sifir • jalur {part}/2','Potong setiap jalur. Garis tengah putus-putus ialah garis lipat, bukan potong.','ALAT',PURPLE,'cutout')
 facts=[(a,k) for a,k in zip([6,7,8,9,11,12,6,7,8,9,11,12],[2,3,4,5,6,7,8,9,10,11,12,12])]
 for j,(a,k) in enumerate(facts[(part-1)*6:part*6]):
  x=15;y=62+j*33;b.rect(x,y,180,30,PURPLE)
  seg(b,105,y,105,y+30,PURPLE,True)
  b.eq(20,y+12,f'{a} × {k} = {a*k}',13)
  b.text(20,y+23,work(a,k),8.5)
  b.text(111,y+9,f'SOALAN LUAR: {a} × {k}',10.5,True,PURPLE)
  b.para(111,y+17,'Tulis soalan ini di belakang petak ini. Lipat petak kanan ke kiri menutupi jawapan.',78,7.9)
 b.para(15,268,'Baca soalan pada luar penutup. Jawab, kemudian selak ke kanan. Susun jalur dan kokot bahagian kiri dengan bantuan dewasa untuk menjadi buku kecil.',180,8.4)
 b.end()

def triangles(b,part):
 b.start(f'Kad segi tiga • keluarga fakta {part}/2','Nombor atas ialah hasil. Dua nombor bawah ialah faktor. Potong garis luar.','ALAT',GREEN,'cutout')
 facts=FOCUS+[(11,12),(12,12)]
 for i,(a,c) in enumerate(facts[(part-1)*6:part*6]):
  x=15+(i%2)*94;y=61+(i//2)*68;b.box(x,y,86,61,GREEN,dash=True)
  points=[(x+43,y+10),(x+16,y+37),(x+70,y+37)]
  for p,q in zip(points,points[1:]+points[:1]):seg(b,*p,*q,GREEN)
  b.text(x+43,y+9,str(a*c),12,True,GREEN,'center')
  b.text(x+13,y+41,str(a),12,True,BLUE,'center');b.text(x+73,y+41,str(c),12,True,ORANGE,'center')
  b.text(x+5,y+51,f'{a} × {c} = {a*c}     {c} × {a} = {a*c}',8.1,True)
  b.text(x+5,y+58,f'{a*c} ÷ {a} = {c}     {a*c} ÷ {c} = {a}',8.1,True)
 b.text(15,272,'Tutup satu nombor. Gunakan hubungan darab dan bahagi untuk mencarinya.',9.2);b.end()

def build_formula():
 b=Book('BIJAK_MATEMATIK_KAD_FORMULA_SIFIR.pdf','ALAT','Kad formula & alat kertas')
 b.start('Kit alat ingatan sifir','Kad poket • roda sifir • buku selak • kad segi tiga','ALAT',BLUE)
 b.svg('tiger_bijak.svg',133,65,52,54)
 y=66
 for t,s in [('Kad poket','Halaman 2–3: 12 strategi. Baca selepas pelajaran berkaitan; cuba menutup contoh.'),('Roda sifir','Halaman 4–7: tapak sifir 7, 8, 9 dan tapak kosong. Halaman 8: penutup. Halaman 9: pemasangan.'),('Buku selak','Halaman 10–11: 12 jalur. Soalan disalin pada luar penutup sebelum latihan.'),('Kad segi tiga','Halaman 12–13: keluarga darab/bahagi. Tutup satu nombor dan cari nombor itu.')]:
  b.text(20,y,t.upper(),11,True,BLUE);y=b.para(20,y+10,s,105,10.3)+17
 b.para(15,243,'Cetak A4 satu muka pada 100%. Gunting garis luar; lipat hanya garis yang dilabel LIPAT. Gunakan kertas tebal jika sesuai. Bantuan orang dewasa diperlukan untuk gunting, lubang dan kokot.',180,10)
 b.end()
 for p in [1,2]:formula_deck(b,p)
 for k in [7,8,9,None]:wheel_base(b,k)
 wheel_cover(b);assembly(b)
 for p in [1,2]:flipbook(b,p)
 for p in [1,2]:triangles(b,p)
 assert b.count==13;b.save()

def flash_strategy(a,c):
 order=[1,2,5,10,3,4,9,6,7,8,11,12]
 k=min([a,c],key=lambda x:order.index(x));n=c if k==a else a
 level='A' if k in [1,2,5,10] else 'B' if k in [3,4,9] else 'C'
 return n,k,level

def build_flash():
 b=Book('BIJAK_MATEMATIK_FLASHCARD_SIFIR.pdf','KAD IMBAS','144 kad imbas • dupleks')
 b.start('Kad imbas • 144 fakta','Semua pasangan tersusun 1 × 1 hingga 12 × 12 disertakan.','ALAT',BLUE)
 for y,t,s in [(64,'01  CETAK PASANGAN YANG BETUL','Cetak halaman 3–26 secara dupleks, A4 potret, 100%, balik pada sisi panjang. Halaman ganjil ialah soalan; halaman genap berikutnya ialah jawapan. Jangan susun halaman mengikut jenis.'),(108,'02  UJI SATU HELAI DAHULU','Cetak halaman 3–4 sahaja. Angkat ke cahaya: F001 pada muka mesti sepadan dengan F001 di belakang. Jika pemacu pencetak memutar belakang, ubah tetapan putaran atau suapan sebelum meneruskan.'),(152,'03  POTONG SELEPAS MENCETAK','Bahagian belakang dicerminkan kiri–kanan secara kedudukan, bukan tulisannya. Potong garis putus-putus selepas memastikan penjajaran. Toleransi pencetak boleh berbeza.'),(196,'04  LATIHAN RINGKAS','Pilih 3–5 fakta sasaran dan beberapa fakta lama. Jawab dahulu, kemudian balik kad untuk semak. Jika silap, bina semula dan cuba lagi selepas beberapa kad.')]:
  b.text(15,y,t,10.5,True,BLUE);b.para(15,y+10,s,180,10)
 b.para(15,252,'Label A (hijau): fakta sauh; B (biru): bina melalui pola; C (ungu): gabung strategi. Ini cadangan sokongan, bukan tahap kesukaran yang tetap bagi semua murid.',180,9.5);b.end()
 b.start('Ujian ukuran & cara menyimpan','Halaman ini tidak perlu dipotong menjadi kad. Cetak dupleks hanya halaman 3–26.','ALAT',GREEN)
 b.text(15,67,'Ukur garis ini: 50 mm',12,True);b.line(15,82,50,NAVY)
 b.box(15,99,180,56,GREEN);b.text(21,110,'SEMAK PENJAJARAN',12,True,GREEN)
 b.para(21,122,'Kotak kad di depan dan belakang mempunyai saiz 57 × 45 mm. Kedudukan x ialah 15, 76.5 dan 138 mm. Belakang menukar lajur 1 dengan lajur 3; baris kekal. Semua kad mempunyai ID pada kedua-dua muka.',167,10.3)
 b.para(15,176,'Jika penjajaran dupleks pencetak tidak memuaskan, cetak muka soalan dan jawapan secara berasingan pada 100%. Potong mengikut ID, kemudian lekatkan belakang pasangan yang sepadan. Jangan padankan mengikut kedudukan kiri sahaja.',180,11)
 b.para(15,221,'Asingkan kad kepada “perlu gambar”, “boleh kira” dan “ingat sendiri”. Label ini boleh berubah. Uji semula pada hari berlainan sebelum menganggap sesuatu fakta stabil.',180,11)
 b.end()
 facts=[(a,c) for a in range(1,13) for c in range(1,13)]
 for sheet in range(12):
  batch=facts[sheet*12:(sheet+1)*12]
  for side in ['front','back']:
   b.start(f'Kad imbas • helaian {sheet+1:02d} • '+('soalan' if side=='front' else 'jawapan'),'Pasangan muka–belakang berkongsi ID. Potong garis putus-putus.','ALAT',BLUE,kind='flashcard')
   for i,(a,c) in enumerate(batch):
    qid=f'F{sheet*12+i+1:03d}';row,col=divmod(i,3)
    x=15+(col if side=='front' else 2-col)*61.5;y=65+row*50
    n,k,level=flash_strategy(a,c);color={'A':GREEN,'B':BLUE,'C':PURPLE}[level]
    b.box(x,y,57,45,color,dash=True);b.text(x+4,y+7,qid+' • '+level,8,True,color)
    if side=='front':
     b.text(x+28.5,y+25,f'{a} × {c}',20,True,align='center')
     b.text(x+28.5,y+38,'Cuba ingat atau kira.',8.2,align='center')
    else:
     b.text(x+28.5,y+22,str(a*c),21,True,color,'center')
     b.para(x+3,y+32,work(n,k),51,7.8,bold=True,leading=3.9)
    FLASH_LAYOUT.append({'id':qid,'side':side,'sheet':sheet+1,'page':b.page,'x':x,'y':y,'w':57,'h':45,'a':a,'b':c,'answer':a*c,'strategy_n':n,'strategy_k':k})
   b.end()
 assert b.count==26;b.save()
 (QA/'flash_layout.json').write_text(json.dumps(FLASH_LAYOUT,indent=2))

def build_poster():
 b=Book('BIJAK_MATEMATIK_POSTER_SIFIR_1_12.pdf','POSTER','Poster sifir 1–12')
 for ink in [False,True]:
  b.ink=ink;b.start('PETA SIFIR 1–12','Faham Dahulu, Kira Dengan Bijak, Hafal Dengan Mudah!','POSTER',BLUE,'poster')
  grid(b,24,64,12.4)
  b.eq(20,244,'7 × 8 = 8 × 7 = 56',18,color=GREEN)
  b.para(20,258,'Tutup hasil untuk cuba ingat. Jika lupa, bina semula dengan fakta sauh. Baris dan lajur ialah rakan cermin.',170,10.5)
  b.text(15,272,'Edisi '+('jimat dakwat' if ink else 'warna')+' • Cetak A4 100%',8.5,False,GRAY);b.end()
 b.save()

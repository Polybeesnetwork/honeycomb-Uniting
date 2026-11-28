from core import *

FOCUS=[(6,6),(6,7),(6,8),(7,7),(7,8),(8,8),(6,9),(7,9),(8,9),(9,9)]

def cover(b):
 b.start('RAHSIA KUASAI SIFIR 1–12','Teknik Visual, Formula Mudah dan Matematik Mental','MULA',BLUE,'cover')
 b.text(15,72,'FAHAM DAHULU.',27,True,BLUE)
 b.text(15,88,'KIRA DENGAN BIJAK.',24,True)
 b.text(15,104,'HAFAL DENGAN MUDAH!',20,True,GREEN)
 b.svg('tiger_bijak.svg',114,124,77,80)
 b.box(15,127,91,70,BLUE)
 b.text(21,138,'LUPA BUKAN PENGHUJUNG.',10.8,True,BLUE)
 b.para(21,149,'Gunakan fakta yang sudah kamu tahu untuk membina jawapan.',78,11)
 b.eq(21,172,'7 × 8 = 40 + 16 = 56',13)
 b.text(21,186,'Saya boleh belajar, satu langkah',9.5)
 b.text(21,192,'pada satu masa.',9.5)
 for i,(word,col) in enumerate([('FAHAM',BLUE),('KIRA',ORANGE),('INGAT',PURPLE),('KUASAI',GREEN)]):
  b.box(15+i*46,217,42,14,col);b.text(36+i*46,226,word,10,True,col,'center')
 b.text(15,247,'Nama: ___________________________________________',11)
 b.text(15,260,'Kelas: ________________   Tarikh mula: ________________',10)
 b.text(15,271,'Buku murid • Umur 7–12 tahun • Boleh digunakan mengikut aras',8.8,False,GRAY)
 b.end()

def contents(b):
 b.start('Peta perjalanan saya','Tidak perlu habiskan semua halaman dalam satu sesi.','MULA',GREEN)
 for y,title,detail in [(65,'01  FAHAM  •  halaman 3–7','Mulakan dengan saringan, objek sebenar, gambar dan simbol.'),(96,'02  KIRA  •  halaman 8–31','Dua halaman bagi setiap sifir: belajar strategi, kemudian cuba sendiri.'),(127,'03  INGAT  •  halaman 32–39','Gunakan peta sifir, kit penyelamat dan latihan ingat semula.'),(158,'04  KUASAI  •  halaman 40–48','Matematik mental, kalendar 30 hari, penilaian akhir dan refleksi.')]:
  b.box(15,y-6,180,26,COLORS[(y//30)%4]);b.text(21,y+3,title,12,True);b.para(21,y+12,detail,166,10)
 b.text(15,198,'BAHAN RAKAN PEMBELAJARAN',11,True,BLUE)
 b.para(15,208,'Gunakan PDF Latihan 30 Hari, Kad Formula, Kad Imbas, Permainan dan Penjejak Kemajuan bersama buku ini. Buku Jawapan menggunakan kod soalan yang sama, contohnya S07.B1.',180,10.5)
 b.box(15,237,180,33,ORANGE)
 b.text(21,247,'TIP TIGER • CUBA → SEMAK → BAIKI → CUBA LAGI',10,True,ORANGE)
 b.para(21,257,'Tiada hukuman kerana lambat. Beritahu orang dewasa bagaimana kamu mendapat jawapan. Kejayaan kamu tidak perlu dibandingkan dengan rakan.',168,9.5)
 b.end()

def diagnostics(b,part):
 b.start(f'Saringan awal • bahagian {part}/2','Cuba tanpa jadual dahulu. Orang dewasa boleh membaca arahan; catat bantuan.','FAHAM',BLUE,'diagnostic')
 items=[
 ('A  KENAL NOMBOR',[('D.A1','Baca 14 dan 41. Bulatkan nombor yang lebih besar.','Bacaan tepat; 41',None),('D.A2','Tulis nombor selepas 29: ______',30,['add',29,1])]),
 ('B  MAKNA DARAB',[('D.B1','3 beg, 4 epal setiap beg. Tulis ayat darab dan jumlah.','3 × 4 = 12; terima 4 × 3 dengan penjelasan',['mul',3,4]),('D.B2','2 kotak, 5 buku setiap kotak. Lukis kumpulan dan tulis jumlah.',10,['mul',2,5])]),
 ('C  TAMBAH BERULANG',[('D.C1','4 + 4 + 4 = ______',12,['sum',4,4,4]),('D.C2','6 + 6 + 6 + 6 = ______',24,['sum',6,6,6,6])]),
 ('D  BILANG LOMPAT',[('D.D1','5, 10, 15, ______, 25',20,['add',15,5]),('D.D2','3, 6, 9, ______, 15',12,['add',9,3])]),
 ('E  INGAT FAKTA',[('D.E1','6 × 7 = ______',42,['mul',6,7]),('D.E2','8 × 8 = ______',64,['mul',8,8])]),
 ('F  KIRA SECARA MENTAL',[('D.F1','8 × 6 = (8 × 5) + 8. Kira dan terangkan.',48,['mul',8,6]),('D.F2','9 × 7 = (10 × 7) − 7. Kira dan terangkan.',63,['mul',9,7])]),
 ('G  BEZAKAN FAKTA',[('D.G1','7 × 8: 54 / 56. Bulatkan jawapan.',56,['mul',7,8]),('D.G2','6 × 9: 54 / 56. Bulatkan jawapan.',54,['mul',6,9])]),
 ('H  GUNA DALAM CERITA',[('D.H1','4 kotak, 6 pensel setiap kotak. Jumlah: ______ batang.',24,['mul',4,6]),('D.H2','7 hari, baca 5 halaman sehari. Jumlah: ______ halaman.',35,['mul',7,5])])]
 for j,(title,qs) in enumerate(items[(part-1)*4:part*4]):
  y=61+j*51;b.box(15,y,180,47,COLORS[j])
  b.text(20,y+8,title,9.5,True,COLORS[j])
  for k,(qid,prompt,ans,calc) in enumerate(qs):
   b.para(20,y+18+k*17,qid+'  '+prompt,159,9.7)
   b.record(qid,prompt,ans,calc)
   if qid=='D.B2':b.line(21,y+44,159,dash=True)
  b.text(188,y+8,'B □',8,False,GRAY,'right')
 b.text(15,273,'1 mata setiap item tepat tanpa bantuan. B = dibantu. Skor dan cadangan aras: Panduan Dewasa.',8.3)
 b.end()

def relations(b):
 b.start('Satu keluarga, empat ayat','JOM FAHAM! Darab dan bahagi saling berkait.','FAHAM',GREEN)
 b.box(15,58,180,63,GREEN)
 b.dots(30,76,3,4,12,r=3)
 b.text(95,74,'3 kumpulan, 4 objek setiap kumpulan.',11,True)
 b.eq(95,90,'3 × 4 = 12',16);b.eq(95,106,'12 ÷ 3 = 4',16)
 b.eq(20,136,'4 × 3 = 12',16);b.eq(110,136,'12 ÷ 4 = 3',16)
 b.box(15,149,86,42,BLUE);b.box(108,149,87,42,ORANGE)
 b.text(20,158,'DARAB DENGAN SATU',9.5,True,BLUE)
 b.eq(20,170,'7 × 1 = 7',15);b.text(20,182,'7 kumpulan, satu setiap kumpulan.',8.5)
 b.text(113,158,'DARAB DENGAN SIFAR',9.5,True,ORANGE)
 b.eq(113,170,'7 × 0 = 0',15);b.eq(113,183,'0 × 7 = 0',13)
 b.text(15,206,'MISI SIFIR • lengkapkan keluarga fakta',11,True,PURPLE)
 b.q('A07.1',20,221,5,6);b.q('A07.2',110,221,30,5,'div')
 b.q('A07.3',20,237,6,5);b.q('A07.4',110,237,30,6,'div')
 b.q('A07.5',20,253,9,0);b.q('A07.6',110,253,12,1)
 b.text(15,269,'Bahagi dengan sifar tidak ditakrifkan. Kita tidak melakukan operasi itu dalam buku ini.',9)
 b.end()

def strategy_visual(b,k):
 if k in [3,6,7,11,12]:
  split={3:2,6:5,7:5,11:10,12:10}[k];step=4.6 if k>8 else 6
  b.dots(70,99,4,k,step,split=split,r=1.45)
  b.text(70,126,f'4 baris: {split} lajur + {k-split} lajur',9.2,True)
 elif k in [4,8]:
  for i,a in enumerate([1,2,4,8] if k==8 else [1,2,4]):
   for j in range(a):
    b.box(66+j*8,94+i*9,7,7,GREEN);b.text(69.5+j*8,99+i*9,'n',7.5,True,align='center')
   b.text(138,99+i*9,f'{a} bahagian',9)
 elif k==10:
  for i,t in enumerate(['RATUS','PULUH','SA']):
   b.box(73+i*36,94,34,35,BLUE);b.text(90+i*36,101,t,8,True,BLUE,'center')
   b.text(90+i*36,112,['0','1','2'][i],13,True,align='center');b.text(90+i*36,125,['1','2','0'][i],13,True,align='center')
  b.text(66,138,'12 × 10: 1 puluh → 1 ratus; 2 sa → 2 puluh.',8.3)
 elif k in [5,9]:
  for j in range(10):
   b.rect(66+j*12.5,98,11,15,BLUE if j<(5 if k==5 else 9) else ORANGE,True)
   b.text(71.5+j*12.5,108,'6' if k==5 else '8',9,True,align='center')
   if k==9 and j==9:
    b.c.line((66+j*12.5)*MM,H-98*MM,(77+j*12.5)*MM,H-113*MM)
  b.text(66,126,'Ambil 5 daripada 10 bahagian.' if k==5 else 'Potong 1 daripada 10 bahagian.',9.5)
 elif k==1:
  b.box(66,94,120,36,BLUE)
  for j in range(4):b.svg('epal.svg',75+j*26,99,12,14)
  b.text(72,125,'Satu kumpulan empat masih empat.',9.5)
 elif k==2:
  for j in range(2):
   b.box(66+j*62,94,58,34,BLUE)
   b.dots(74+j*62,104,1,5,9,r=2)
  b.text(66,139,'5 objek + 5 objek = 10 objek',10)

def lesson(b,k):
 title,formula,why,mistake,pattern=STRATEGIES[k];col=COLORS[(k-1)%4]
 b.start(f'Sifir {k} • {title.lower()}','JOM FAHAM! Baca contoh, jelaskan caranya, kemudian tutup bantuan.','KIRA',col)
 b.box(15,56,180,18,col)
 b.text(21,68,formula,13 if k not in [4,8,10] else 12,True,col)
 b.table(k,y=83,row=7.2)
 b.tag(65,83,'JOM FAHAM!',col,50);strategy_visual(b,k)
 b.para(65,148,why,129,9.3)
 b.text(65,167,'TIGA CONTOH KERJA',9,True,col)
 for i,n in enumerate([4,7,12]):
  s=work(n,k)
  if '→' in s:b.eq(65,178+i*10,s,12)
  else:b.eq(65,178+i*10,s,11.7)
 b.box(15,212,180,24,ORANGE)
 b.text(20,220,'TIP TIGER • ELAK SILAP INI',9,True,ORANGE)
 b.para(20,229,mistake,168,9.6)
 b.para(15,248,'CORAK INGATAN: '+pattern,180,10)
 b.text(15,266,'Tutup jadual. Cuba ingat, atau bina semula dengan strategi.',10,True,GREEN)
 b.end()

def practice(b,k):
 col=COLORS[(k-1)%4];prefix=f'S{k:02d}'
 b.start(f'Sifir {k} • giliran saya','BIMBINGAN → SENDIRI → INGAT. Jika lupa, lukis atau guna fakta sauh.','INGAT',col)
 b.text(15,60,'A  LATIHAN BERPANDU',10,True,col)
 for i,n in enumerate([3,6,8,11]):
  y=74+i*15;qid=prefix+f'.A{i+1}'
  if k in [3,6,7,11,12]:
   a=2 if k==3 else 5 if k in [6,7] else 10;c=k-a
   prompt=f'{n} × {k} = ({n} × {a}) + ({n} × {c}) = ____ + ____ = ____'
   ans=[n*a,n*c,n*k];calc=['split',n,k,a,c]
  elif k==5:prompt=f'{n} × 5 = ____ ÷ 2 = ____';ans=[n*10,n*5];calc=['half10',n]
  elif k==9:prompt=f'{n} × 9 = ____ − {n} = ____';ans=[n*10,n*9];calc=['tenminus',n]
  elif k in [4,8]:
   count=2 if k==4 else 3;prompt=f'{n} → '+' → '.join(['____']*count);ans=[n*2**j for j in range(1,count+1)];calc=['double',n,count]
  elif k==2:prompt=f'{n} × 2 = {n} + ____ = ____';ans=[n,n*2];calc=['doublestep',n]
  else:prompt=f'{n} × {k} = ____';ans=n*k;calc=['mul',n,k]
  b.text(19,y,qid+'  '+prompt,10.2);b.record(qid,prompt,ans,calc)
 b.line(15,127,180,col)
 b.text(15,138,'B  CUBA SENDIRI • TANPA JADUAL DAHULU',10,True,col)
 for i,n in enumerate([2,5,7,9,10,12,4,11]):b.q(prefix+f'.B{i+1}',19+(i%2)*91,152+(i//2)*13,n,k,size=10.8)
 b.text(15,202,'C  LATIHAN BERCAMPUR',10,True,GREEN)
 others=[(7,2),(8,5),(9,10),(6,min(k,12))]
 for i,(a,c) in enumerate(others):b.q(prefix+f'.C{i+1}',19+(i%2)*91,215+(i//2)*13,a,c,size=10.8)
 b.box(15,237,180,25,ORANGE)
 prompt=f'Ada {k} pek pelekat. Setiap pek ada 6 pelekat. Berapa jumlah pelekat?'
 b.text(20,245,prefix+'.D1  '+prompt,9.5)
 b.text(20,256,'Ayat matematik: __________________  Jawapan: __________ pelekat',10)
 b.record(prefix+'.D1',prompt,6*k,['mul',k,6])
 b.text(15,272,'Saya: □ perlukan gambar  □ boleh kira  □ boleh ingat. Fakta untuk ulang: __________',9)
 b.end()

def chart_pages(b):
 b.start('Peta sifir lengkap • 12 × 12','Cari baris faktor pertama dan lajur faktor kedua. Pertemuan ialah hasil darab.','INGAT',BLUE,'chart')
 grid(b,24,62,12.4)
 b.para(15,238,'TIP TIGER: 7 × 8 dan 8 × 7 berkongsi hasil 56. 144 pasangan tersusun boleh diwakili oleh 78 pasangan tanpa mengira tertib: 12 pada pepenjuru + 66 pasangan cermin.',180,10.5)
 b.text(15,270,'Bukti kiraan: (144 + 12) ÷ 2 = 78.',11,True,GREEN);b.end()
 b.start('Peta kosong • bina sendiri','Isi sedikit demi sedikit. Semak menggunakan strategi, bukan menyalin semata-mata.','INGAT',GREEN,'chart')
 grid(b,24,62,12.4,'blank')
 b.para(15,239,'Mula dengan sifir 1, 2, 5 dan 10. Kemudian pilih satu baris yang sedang dipelajari. Pusing faktor untuk membantu mengisi petak cermin.',180,10.5)
 b.text(15,265,'Baris yang saya lengkapkan hari ini: ______  Tarikh: __________',10.5);b.end()
 b.start('Peta penguasaan peribadi','Jangan warnakan berdasarkan satu cubaan sahaja. Gunakan bukti pada hari berbeza.','KUASAI',PURPLE,'tracker')
 grid(b,24,62,12.4,'blank')
 b.para(15,238,'Dalam setiap petak tulis G (guna gambar), K (boleh kira) atau I (ingat tepat tanpa bantuan pada 3 sesi berasingan). Pilihan warna: kuning G, biru K, hijau I. Tulis hasil dahulu jika mahu.',180,10)
 b.text(15,266,'Boleh kira dengan strategi juga satu kemajuan. Tarikh semakan: __________',10);b.end()
 b.start('Rahsia cermin & nombor kuasa dua','Gunakan peta lengkap di halaman 32 untuk menyiasat.','KUASAI',PURPLE)
 b.text(15,62,'A  SIMETRI • PASANGAN CERMIN',11,True,BLUE)
 for i,(a,c) in enumerate([(3,8),(6,9),(7,12),(4,11)]):
  y=79+i*16;qid=f'P35.A{i+1}'
  b.text(20,y,f'{qid}  {a} × {c} = ____ ; {c} × {a} = ____',12)
  b.record(qid,f'{a} × {c}; {c} × {a}',[a*c,a*c],['pair',a,c])
 b.text(15,150,'B  PEPENJURU • FAKTOR YANG SAMA',11,True,PURPLE)
 for i,n in enumerate(range(1,13)):b.q(f'P35.B{i+1}',20+(i%3)*59,166+(i//3)*15,n,n,size=10.5)
 b.para(15,232,'Warnakan pepenjuru peta sifir. Nombor 1, 4, 9, 16, … dipanggil nombor kuasa dua. Lukis 4 × 4 titik di bawah; terangkan mengapa susunannya berbentuk segi empat sama.',180,10)
 b.ruled(20,258,170,2,11);b.record('P35.C','Lukis susunan 4 × 4',16,['mul',4,4]);b.end()
 b.start('Petak hilang & fakta sasaran','MISI SIFIR: gunakan fakta jiran atau tukar tertib apabila perlu.','KUASAI',ORANGE)
 for i,(a,c) in enumerate([(6,7),(8,9),(12,8),(7,7),(11,12),(9,9)]):
  b.q(f'P36.A{i+1}',20+(i%2)*90,72+(i//2)*19,a,c,'missing',size=11.5)
 b.text(15,132,'FAKTA SASARAN SAYA',12,True,ORANGE)
 b.para(15,142,'Pilih 4 fakta yang belum stabil. Cuba dahulu; semak dan catat strategi. Ulang pada hari lain. Jadual penuh ada dalam PDF Penjejak Kemajuan.',180,10.5)
 for i in range(4):
  y=163+i*24;b.box(15,y,180,22,ORANGE)
  b.text(20,y+8,'Fakta: __________   Strategi: _________________________________',10)
  b.text(20,y+17,'Tarikh: ________  G / K / I: ____   Cuba semula pada: __________',9.5)
 b.end()

RESCUE_NOTES=[
 'Enam kotak, enam buku: 30 buku dahulu, tambah 6 menjadi 36.',
 'Tujuh hari, enam bintang sehari: 35 bintang dahulu, tambah 7 menjadi 42.',
 'Lapan bakul, enam epal setiap bakul: 40 + 8 = 48.',
 'Petak 7 × 7 ialah kuasa dua: (7 × 5) + (7 × 2) = 35 + 14.',
 'Petunjuk 5, 6, 7, 8: 56 ialah 7 × 8. Ini pembayang ingatan, bukan formula umum.',
 'Papan 8 baris, 8 petak setiap baris: ganda 8 → 16 → 32 → 64.',
 'Sembilan kumpulan enam: 60 − 6 = 54. Enam puluh kurang enam, lima puluh empat.',
 'Sembilan kumpulan tujuh: 70 − 7 = 63. Tujuh puluh kurang tujuh, enam puluh tiga.',
 'Sembilan kumpulan lapan: 80 − 8 = 72. Ingat lapan diambil sekali.',
 'Sembilan kumpulan sembilan: 90 − 9 = 81. Berhampiran fakta sauh 90.']
def rescue(b,part):
 b.start(f'Kit penyelamat • cerita fakta {part}/2','Ini contoh fakta tumpuan, bukan senarai kesukaran yang sama bagi semua murid.','INGAT',ORANGE)
 for j,idx in enumerate(range((part-1)*5,part*5)):
  a,c=FOCUS[idx];y=60+j*41.8;b.box(15,y,180,38,ORANGE)
  b.eq(21,y+12,f'{a} × {c} = {a*c}',17,color=ORANGE)
  b.para(80,y+10,RESCUE_NOTES[idx],109,9.4)
  b.text(21,y+29,'Lihat → tutup → sebut fakta dan caranya → semak.',9.1)
 b.end()

def rescue_recall(b,part):
 b.start(f'Kit penyelamat • ingat semula {part}/2','Cuba tanpa melihat cerita fakta. Jika lupa, gunakan fakta sauh.','INGAT',GREEN)
 facts=FOCUS if part==1 else list(reversed(FOCUS))
 for i,(a,c) in enumerate(facts):b.q(f'R{part}.{i+1}',20+(i%2)*90,72+(i//2)*19,a,c,size=11.5)
 b.text(15,177,'BINA SEMULA, JANGAN TEKA',11,True,GREEN)
 for i,(a,c) in enumerate([(7,8),(8,9),(6,7)]):
  y=193+i*22;b.text(20,y,f'R{part}.S{i+1}  {a} × {c}: strategi saya ________________________',10.5)
  b.record(f'R{part}.S{i+1}',f'Terangkan {a} × {c}',a*c,['mul',a,c],note='Terima penguraian atau strategi yang betul.')
 b.para(15,260,'Tandakan 3 fakta untuk diulang selepas kira-kira 1, 3, 7 dan 14 hari. Jangan anggap satu jawapan pantas sebagai bukti penguasaan kekal.',180,10)
 b.end()

def mental(b,part):
 titles=['Kira dalam kepala','Cari cara paling mudah','Cabaran bijak • guna dalam hidup']
 b.start(titles[part-1],'Gunakan bahagian ini selepas memahami kumpulan sama banyak dan strategi asas.','KUASAI',PURPLE)
 if part==1:
  ex=[('7 × 8 = (5 × 8) + (2 × 8)','7 × 8 = 40 + 16 = 56'),('9 × 7 = (10 × 7) − 7','9 × 7 = 70 − 7 = 63'),('8 × 6: ganda 6 tiga kali','6 → 12 → 24 → 48'),('12 × 7 = (10 × 7) + (2 × 7)','12 × 7 = 70 + 14 = 84')]
  for i,(intro,s) in enumerate(ex):
   y=62+i*43;b.box(15,y,180,37,COLORS[i]);b.text(21,y+12,intro,12,True)
   b.eq(21,y+27,s,15,color=COLORS[i])
  b.text(15,249,'M41.1  Cuba 8 × 7 dengan dua cara: __________________________',10.3)
  b.record('M41.1','8 × 7 dengan dua cara',56,['mul',8,7],note='Contoh: 40 + 16 atau 80 − 24.')
  b.ruled(20,266,170,1)
 elif part==2:
  for i,(a,c) in enumerate([(6,8),(9,8),(7,12),(11,9),(12,12),(8,11)]):
   y=65+i*29;b.q(f'M42.{i+1}',20,y,a,c,size=12)
   b.text(90,y,'Saya pilih: __________________________',10.5);b.ruled(20,y+13,170,1)
  b.para(15,252,'Bandingkan cara dengan rakan. Ada lebih daripada satu cara yang betul. Pilih cara yang mengurangkan beban ingatan kamu.',180,10.5)
 else:
  stories=[(7,8,'7 meja mempunyai 8 kerusi setiap satu. Berapa jumlah kerusi?','kerusi'),(12,6,'12 kotak ada 6 botol air setiap satu. Berapa jumlah botol?','botol'),(9,11,'9 pek ada 11 kad setiap satu. Berapa jumlah kad?','kad'),(8,12,'8 minggu, 12 buku dibaca setiap minggu. Berapa jumlah buku?','buku')]
  for i,(a,c,s,u) in enumerate(stories):
   y=62+i*49;b.box(15,y,180,44,COLORS[i]);b.para(20,y+10,f'M43.{i+1}  '+s,168,11)
   b.text(20,y+32,'Ayat matematik: _______________  Jawapan: __________ '+u,10)
   b.record(f'M43.{i+1}',s,a*c,['mul',a,c])
  b.text(15,271,'Semak: adakah unit jawapan sesuai dengan soalan?',10,True,GREEN)
 b.end()

FINAL_FACTS=[(7,8),(6,9),(12,11),(8,8),(9,9),(7,7),(12,8),(11,9),(6,7),(12,12),(5,9),(4,8)]
def final_test(b,part):
 b.start(f'Penilaian akhir • bahagian {part}/2','Tanpa had masa. Cuba sendiri dahulu; catat jika bantuan digunakan.','KUASAI',GREEN,'assessment')
 if part==1:
  b.text(15,62,'F45.1  Lukis 3 kumpulan, 4 objek setiap kumpulan. Tulis ayat darab.',10.5)
  b.answer_box(15,70,180,35);b.record('F45.1','Lukis 3 kumpulan 4',12,['mul',3,4])
  b.text(15,119,'F45.2  Tukar 6 + 6 + 6 + 6 kepada ayat darab.',11)
  b.ruled(20,134,170,1);b.record('F45.2','6 + 6 + 6 + 6','4 × 6 = 24',['sum',6,6,6,6])
  b.text(15,151,'F45.3  Lengkapkan 8 × 7 = 40 + ____ = ____.',11)
  b.record('F45.3','8 × 7 = 40 + …',[16,56],['splitlast',8,7,5])
  b.q('F45.4',20,174,42,6,'div',size=12);b.q('F45.5',110,174,7,9,'missing',size=12)
  for i,(a,c) in enumerate(FINAL_FACTS[:8]):b.q(f'F45.{i+6}',20+(i%2)*90,198+(i//2)*18,a,c,size=11.5)
 else:
  for i,(a,c) in enumerate(FINAL_FACTS[8:]):b.q(f'F46.{i+1}',20+(i%2)*90,72+(i//2)*20,a,c,size=11.5)
  for i,(a,c,p) in enumerate([(7,8,'7 kotak mengandungi 8 buku setiap satu. Berapa jumlah buku?'),(12,9,'12 pek mengandungi 9 pelekat setiap satu. Berapa jumlah pelekat?')]):
   y=125+i*54;b.box(15,y,180,47,ORANGE);b.para(20,y+12,f'F46.{i+5}  '+p,168,11)
   b.ruled(20,y+32,168,1);b.record(f'F46.{i+5}',p,a*c,['mul',a,c])
  b.text(15,244,'F46.7  Jelaskan dua cara untuk 9 × 8.',11,True)
  b.record('F46.7','Dua cara untuk 9 × 8',72,['mul',9,8],note='Contoh: 80 − 8 atau 40 + 32.')
  b.ruled(20,257,170,2,11)
 b.end()

def last_pages(b):
 b.start('Latihan pendek, kemajuan sebenar','Gunakan PDF LATIHAN 30 HARI bersama kalendar pada halaman 44.','TERUSKAN',GREEN)
 for i,(t,s) in enumerate([('01  Pilih aras','Jika objek dan gambar masih membantu, gunakannya. Selesaikan sedikit latihan dengan teliti.'),('02  Cuba ingat','Tutup jadual. Cuba 3–5 fakta sasaran. Jika lupa, kira dengan strategi sebelum menyemak.'),('03  Semak dan baiki','Cari satu langkah yang tersilap. Bina semula jawapan. Cuba fakta itu semula selepas soalan lain.'),('04  Ulang selepas sela','Semak lagi pada hari berbeza. Selepas hari 30, teruskan fakta yang belum stabil.')]):
  y=62+i*42;b.box(15,y,180,36,COLORS[i]);b.text(21,y+11,t,12,True,COLORS[i]);b.para(21,y+22,s,166,10)
 b.para(15,246,'Cabaran masa ialah pilihan, bukan syarat. Cuba hanya apabila ketepatan dan keyakinan meningkat. Bandingkan dengan rekod sendiri, bukan dengan murid lain.',180,10.5);b.end()
 b.start('Tahniah kerana terus mencuba!','Saya belajar untuk memahami, mengira, mengingat dan menggunakan sifir.','TERUSKAN',ORANGE)
 b.svg('tiger_bijak.svg',72,62,66,68)
 b.text(105,148,'KEMAJUAN SAYA',21,True,BLUE,'center')
 for y,s in [(170,'Dahulu saya sukar: __________________________________'),(191,'Sekarang saya boleh: _________________________________'),(212,'Strategi kegemaran saya: ______________________________'),(233,'Langkah seterusnya: __________________________________')]:b.text(20,y,s,11)
 b.para(15,257,'TIP TIGER: jika jawapan belum teringat, kamu masih boleh membinanya. Raikan usaha, penjelasan yang baik dan kemajuan kecil yang berterusan.',180,10.5)
 b.end()

def build_main(ink=False):
 filename='BIJAK_MATEMATIK_RAHSIA_SIFIR_'+('INKSAVING' if ink else 'COLOR')+'.pdf'
 b=Book(filename,'BUKU MURID','Buku utama • '+('jimat dakwat' if ink else 'warna'),ink)
 cover(b);contents(b);diagnostics(b,1);diagnostics(b,2)
 B.foundations(b);B.arrays(b)
 b.record('A06.1','3 baris dengan 5 petak','3 × 5 = 15; 5 × 3 = 15',['mul',3,5])
 b.record('A06.2','2 baris dengan 6 titik',12,['mul',2,6])
 relations(b)
 for k in range(1,13):lesson(b,k);practice(b,k)
 chart_pages(b)
 for p in [1,2]:rescue(b,p)
 for p in [1,2]:rescue_recall(b,p)
 for p in [1,2,3]:mental(b,p)
 calendar(b)
 for p in [1,2]:final_test(b,p)
 last_pages(b);assert b.count==48,b.count;b.save()

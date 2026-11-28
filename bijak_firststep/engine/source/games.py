from core import *
from materials import seg
GKEYS=[];CLAIMS=[]
MAZE=[[(7,2),(3,7),(6,6),(8,8)],[(9,9),(7,4),(6,8),(8,9)],[(6,9),(5,7),(7,6),(4,9)],[(3,8),(9,10),(8,7),(7,9)]]
MPATH=[(0,0),(0,1),(1,1),(2,1),(2,2),(3,2),(3,3)]
BINGO_FACTS=[(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,8),(8,9),(9,9)]
PATTERN=[
[24,12,12,24,24,12,12,24],
[12,16,12,12,12,12,16,12],
[12,12,16,12,12,16,12,12],
[12,8,16,12,12,16,8,12],
[12,8,8,8,8,8,8,12],
[12,8,16,8,8,16,8,12],
[24,12,8,16,16,8,12,24],
[24,24,12,12,12,12,24,24]]
CROSS_ENTRIES=[{'label':'1 melintang','a':3,'b':4,'cells':[(0,0),(0,1)]}, {'label':'2 melintang','a':12,'b':12,'cells':[(2,0),(2,1),(2,2)]},{'label':'4 melintang','a':9,'b':9,'cells':[(3,2),(3,3)]},{'label':'1 menegak','a':11,'b':11,'cells':[(0,0),(1,0),(2,0)]},{'label':'3 menegak','a':6,'b':8,'cells':[(2,2),(3,2)]}]
MEMORY=[(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,8),(9,9),(8,9),(7,9),(6,9),(12,12)]
DOMINO=MEMORY[:]
TREASURE=[('MULA',6,7),('42',7,8),('56',8,8),('64',9,9),('81',7,9),('63',8,9),('72',6,6),('36',None,None)]
SNAKES={20:12,24:18};LADDERS={3:11,8:16}

def key(name,text):GKEYS.append((name,text))
def build_games():
 b=Book('BIJAK_MATEMATIK_PERMAINAN_SIFIR.pdf','PERMAINAN','Permainan kertas sifir')
 b.start('Misi bermain, misi memahami','13 permainan utama + domino. Boleh dimainkan tanpa telefon atau komputer.','MAIN',GREEN)
 b.svg('tiger_bijak.svg',136,65,49,51)
 b.para(15,65,'Peralatan asas: pensel, pemadam, pensel warna, gunting, penanda kecil dan dua dadu. Jika tiada dadu, cetak jaring pada halaman 9 dan pasang dengan bantuan dewasa.',111,11)
 for i,s in enumerate(['Bingo sifir • Jejak gandaan 7 • Warna ikut darab','Detektif matematik • Kod rahsia • Silang nombor','Golek dan darab • Cari harta • Faktor hilang','Padan dan sambung • Ular dan tangga','Ingatan berpasangan • Bilik misteri • Domino']):b.text(20,133+i*14,s,10.5,True,COLORS[i%4])
 b.box(15,214,180,54,ORANGE)
 b.text(21,225,'PERATURAN BERSAMA',11,True,ORANGE)
 b.para(21,236,'Baca arahan setiap permainan. Kira dahulu, semak selepas menjawab. Jika silap, gunakan strategi dan cuba lagi. Bantu rakan tanpa mengejek. Tiada hukuman kerana lambat. Jawapan lengkap ada di hujung PDF ini dan dalam Buku Jawapan.',167,10.2)
 b.end()
 bingo(b);maze(b);coloring(b);detective(b);code(b);crossword(b);roll(b);dice(b);treasure(b);missing(b);match(b);snakes(b);snake_cards(b);memory(b,1);memory(b,2);escape(b);domino(b)
 for p in range(0,len(GKEYS),4):
  b.start(f'Jawapan permainan • set {p//4+1}','Semak selepas mencuba. Penerangan matematik lebih penting daripada menang.','SEMAK',GREEN)
  y=61
  for title,txt in GKEYS[p:p+4]:
   b.text(15,y,title,11,True,BLUE);y=b.para(15,y+10,txt,180,10.2)+14
  b.end()
 b.save()
 (ROOT/'source/game_data.json').write_text(json.dumps({'maze':MAZE,'maze_path':MPATH,'bingo_facts':BINGO_FACTS,'color_pattern':PATTERN,'crossword':CROSS_ENTRIES,'memory':MEMORY,'domino':DOMINO,'treasure':TREASURE,'snakes':SNAKES,'ladders':LADDERS,'claims':CLAIMS,'keys':GKEYS},ensure_ascii=False,indent=2))

def bingo(b):
 b.start('01  Bingo sifir','2 pemain dan seorang pemanggil. Potong papan dan kad panggilan; guna penanda kecil.','MAIN',BLUE,'game')
 b.para(15,59,'Kocok kad panggilan. Pemanggil baca soalan; pemain mengira lalu menutup hasil pada papan. Menang apabila 3 petak sebaris, selajur atau menyerong ditutup. Semak semua 3 hasil sebelum mengisytiharkan “Bingo!”.',180,9.5)
 products=[a*c for a,c in BINGO_FACTS];orders=[list(range(9)),[4,8,0,6,2,7,1,5,3]]
 for board,order in enumerate(orders):
  x=15+98*board;y=92;b.text(x,y-5,'PAPAN '+('A' if board==0 else 'B'),10,True,BLUE)
  for idx,num in enumerate(order):
   xx=x+(idx%3)*26;yy=y+(idx//3)*26;b.rect(xx,yy,26,26,BLUE,True);b.text(xx+13,yy+16,str(products[num]),19,True,align='center')
 b.text(15,180,'KAD PANGGILAN • potong dan kocok',9.5,True,GREEN)
 for i,(a,c) in enumerate(BINGO_FACTS):
  x=15+(i%3)*61.5;y=186+(i//3)*27;b.box(x,y,57,23,GREEN,dash=True);b.text(x+28.5,y+14,f'{a} × {c}',15,True,align='center')
  b.record(f'G01.{i+1}',f'Bingo {a} × {c}',a*c,['mul',a,c])
 b.end();key('01  BINGO','Kad panggilan mengikut turutan cetak: 6, 12, 20, 30, 42, 56, 64, 72, 81. Kedua-dua papan menggunakan hasil yang sama dalam susunan berlainan. Pemenang bergantung pada urutan kad yang dikocok.')

def maze(b):
 b.start('02  Jejak gandaan 7','Seorang atau berpasangan. Guna pensel untuk menguji laluan.','MAIN',GREEN,'game')
 b.para(15,59,'Mula di kiri atas. Gerak satu petak ke atas, bawah, kiri atau kanan hanya apabila hasil darab petak baharu ialah gandaan 7. Jangan ulang petak atau bergerak menyerong. Cari TAMAT.',180,10)
 for r in range(4):
  for c in range(4):
   x=25+c*39;y=88+r*39;b.box(x,y,37,37,GREEN)
   if (r,c) in [(0,0),(3,3)]:b.text(x+18.5,y+8,'MULA' if r==0 else 'TAMAT',8,True,GREEN,'center')
   a,k=MAZE[r][c];b.text(x+18.5,y+22,f'{a} × {k}',17,True,align='center')
   b.record(f'G02.{r+1}{c+1}',f'Petak baris {r+1}, lajur {c+1}: {a} × {k}',a*k,['mul',a,k])
 b.text(15,263,'Tulis hasil dalam setiap petak yang kamu lalui. Terangkan mengapa petak lain tidak dipilih.',9.3)
 b.end();key('02  JEJAK GANDAAN 7','Laluan tunggal, (baris, lajur): (1,1) → (1,2) → (2,2) → (3,2) → (3,3) → (4,3) → (4,4). Hasil laluan: 14 → 21 → 28 → 35 → 42 → 56 → 63. Semua gandaan 7; petak lain bukan gandaan 7.')

def coloring(b):
 b.start('03  Warna ikut darab','Kira setiap petak dahulu. Warnakan berdasarkan hasil, bukan tekaan bentuk.','MAIN',ORANGE,'game')
 b.text(15,60,'8 = kuning (K)   12 = jingga (J)   16 = kelabu gelap (G)   24 = putih (P)',9.5,True)
 b.para(15,70,'Jika mencetak tanpa warna, tulis huruf K, J, G atau P dalam petak. Semua petak mempunyai satu jawapan yang menentukan warnanya.',180,9.3)
 choices={8:[(2,4),(4,2),(1,8)],12:[(3,4),(2,6),(6,2)],16:[(2,8),(4,4),(8,2)],24:[(3,8),(4,6),(6,4)]}
 for r in range(8):
  for c in range(8):
   x=25+c*20;y=88+r*20;p=PATTERN[r][c];a,k=choices[p][(r+c)%3]
   b.rect(x,y,20,20,GRAY);b.text(x+10,y+12,f'{a} × {k}',9.3,True,align='center')
   b.record(f'G03.{r+1}{c+1}',f'Warna petak {r+1},{c+1}: {a} × {k}',p,['mul',a,k])
 b.text(15,266,'Gambar piksel siap ialah wajah harimau. Setiap hasil masih perlu disemak.',10,True,ORANGE);b.end()
 key('03  WARNA IKUT DARAB','K = 8, J = 12, G = 16, P = 24. Baris atas ke bawah: PJJP PJJP (abaikan ruang); JGJJJJGJ; JJGJJGJJ; JKGJJGKJ; JKKKKKKJ; JKGKKGKJ; PJKGGKJP; PPJJJJPP. Gunakan kunci petak G03 dalam Buku Jawapan jika ragu. Bentuknya wajah harimau piksel.')

def detective(b):
 b.start('04  Detektif matematik','Dakwaan di bawah sengaja mengandungi kesilapan. Jangan hafal sebagai fakta.','MAIN',PURPLE,'game')
 cases=[(7,8,54),(8,6,46),(9,7,63),(12,11,121)]
 for i,(a,c,claim) in enumerate(cases):
  y=62+i*49;b.box(15,y,180,43,PURPLE)
  b.text(21,y+11,f'G04.{i+1}  DAKWAAN: {a} × {c} = {claim}',14,True,PURPLE)
  b.text(21,y+23,'□ Betul  □ Salah. Pembetulan / sebab: ___________________',10.5)
  b.ruled(21,y+36,166,1)
  ans=('Betul' if a*c==claim else 'Salah')+f'; hasil betul {a*c}'
  b.record(f'G04.{i+1}',f'Semak dakwaan {a} × {c} = {claim}',ans,['claim',a,c,claim])
  CLAIMS.append({'file':b.name,'page':b.page,'expression':f'{a} × {c} = {claim}','true':a*c==claim})
 b.para(15,267,'Tugas detektif: jelaskan menggunakan strategi, bukan sekadar menukar nombor.',180,9.5);b.end()
 key('04  DETEKTIF','G04.1 salah: 7 × 8 = 56 (40 + 16). G04.2 salah: 8 × 6 = 48 (40 + 8). G04.3 betul: 9 × 7 = 63 (70 − 7). G04.4 salah: 12 × 11 = 132 (120 + 12). Petua digit berulang tidak digunakan secara umum untuk faktor dua digit.')

def code(b):
 b.start('05  Cabaran kod rahsia','Kira, cari huruf dalam kunci, kemudian baca mesej tersembunyi.','MAIN',PURPLE,'game')
 b.box(15,63,180,32,PURPLE);b.text(21,75,'KUNCI KOD',10,True,PURPLE)
 b.text(21,87,'42 → H     56 → E     63 → B     64 → A     72 → T',12,True)
 facts=[(6,7),(7,8),(7,9),(8,8),(8,9)]
 for i,(a,c) in enumerate(facts):
  y=108+i*25;b.box(15,y,180,22,PURPLE)
  b.q(f'G05.{i+1}',21,y+14,a,c,size=13);b.text(121,y+14,'Huruf: ______',12)
 b.text(15,254,'MESEJ: ____  ____  ____  ____  ____',17,True,PURPLE)
 b.text(15,270,'Terangkan satu strategi yang kamu gunakan untuk membuka kod.',10);b.end()
 key('05  KOD RAHSIA','Hasil: 42, 56, 63, 64, 72. Huruf: H, E, B, A, T. Mesej: HEBAT. Setiap hasil mempunyai tepat satu huruf dalam kunci.')

def crossword(b):
 b.start('06  Silang nombor sifir','Tulis satu digit dalam setiap petak putih. Petak gelap tidak diisi.','MAIN',BLUE,'game')
 cells={p for e in CROSS_ENTRIES for p in e['cells']};starts={(0,0):1,(2,0):2,(2,2):3,(3,2):4}
 for r in range(4):
  for c in range(4):
   x=48+c*28;y=65+r*28
   if (r,c) in cells:
    b.rect(x,y,28,28,BLUE)
    if (r,c) in starts:b.text(x+3,y+6,str(starts[(r,c)]),8,True,BLUE)
   else:
    b.c.setFillColor(b.color(NAVY));b.c.rect(x*MM,H-(y+28)*MM,28*MM,28*MM,fill=1,stroke=0)
 b.text(15,194,'MELINTANG',11,True,BLUE);b.text(113,194,'MENEGAK',11,True,GREEN)
 for i,e in enumerate(CROSS_ENTRIES):
  across='melintang' in e['label'];j=i if across else i-3;x=20 if across else 118;y=210+j*18
  b.text(x,y,f"{e['label'].split()[0]}.  {e['a']} × {e['b']}",13,True)
  b.record(f'G06.{i+1}',e['label']+f": {e['a']} × {e['b']}",e['a']*e['b'],['mul',e['a'],e['b']])
 b.text(15,270,'Digit pada persilangan mesti sama untuk kedua-dua arah.',10);b.end()
 key('06  SILANG NOMBOR','Melintang 1: 12; 2: 144; 4: 81. Menegak 1: 121; 3: 48. Setiap persilangan telah disemak: baris 1 ialah 1,2; baris 2 ialah 2; baris 3 ialah 1,4,4; baris 4 ialah 8,1 bermula pada lajur 3.')

def roll(b):
 b.start('07  Golek dan darab','1–2 pemain. Dua dadu biasa atau jaring dadu halaman seterusnya.','MAIN',GREEN,'game')
 b.para(15,60,'Golek dua dadu. Darabkan dua nombor yang muncul; terangkan cara. Mod A: guna nilai 1–6. Mod B, selepas bersedia: tambah 6 pada kedua-dua nilai untuk faktor 7–12. Catat 8 pusingan; semak bersama.',180,10.5)
 b.eq(20,88,'Contoh A: 3 × 5 = 15',13)
 b.eq(20,100,'Contoh B: (3 + 6) × (5 + 6) = 9 × 11 = 99',12)
 widths=[18,28,28,49,57];xs=[15]
 for w in widths:xs.append(xs[-1]+w)
 for r in range(9):
  for c in range(5):b.rect(xs[c],113+r*15,widths[c],15,GREEN,fill=(r==0))
  if r==0:
   for c,t in enumerate(['Sesi','Dadu A','Dadu B','Faktor / ayat darab','Hasil & strategi']):b.text(xs[c]+2,122,t,7.8,True)
  else:b.text(19,122+r*15,str(r),10)
 b.text(15,262,'Semakan: gunakan peta sifir atau strategi. Jawapan berubah mengikut gulungan.',9.8)
 b.end();key('07  GOLEK DAN DARAB','Jawapan berubah mengikut dua dadu. Mod A menggunakan faktor 1–6. Mod B menggunakan faktor 7–12 selepas menambah 6 pada setiap dadu. Contoh: dadu 3 dan 5 memberi 15 dalam Mod A atau 99 dalam Mod B. Semak semua rekod dengan peta sifir.')

def dice(b):
 b.start('Jaring dua dadu • potong & lipat','Garis luar padu: potong. Garis dalaman putus-putus: lipat. Gunakan pita pelekat.','ALAT',ORANGE,'cutout')
 net={(1,0):1,(0,1):2,(1,1):3,(2,1):4,(1,2):5,(1,3):6}
 for setno in range(2):
  x0=20+100*setno;y0=80;s=22
  b.text(x0,70,'DADU '+str(setno+1),12,True,ORANGE)
  for (c,r),v in net.items():
   x=x0+c*s;y=y0+r*s;b.text(x+s/2,y+s*.65,str(v),20,True,align='center')
   for dc,dr,p1,p2 in [(-1,0,(x,y),(x,y+s)),(1,0,(x+s,y),(x+s,y+s)),(0,-1,(x,y),(x+s,y)),(0,1,(x,y+s),(x+s,y+s))]:
    if (c+dc,r+dr) not in net:seg(b,*p1,*p2,ORANGE)
    elif (dc,dr) in [(1,0),(0,1)]:seg(b,*p1,*p2,GRAY,True)
 b.para(15,199,'1. Potong sepanjang sempadan luar sahaja. 2. Lipat pada semua garis dalaman. 3. Bentukkan kiub. 4. Lekatkan tepi yang bertemu menggunakan pita. Tiada tab diperlukan. Dewasa membantu memotong dan memasang.',180,11)
 b.para(15,240,'Gunakan kertas tebal jika ada. Dadu buatan sendiri mungkin tidak seimbang; ia memadai untuk latihan tetapi bukan untuk eksperimen kebarangkalian.',180,10.5);b.end()

def treasure(b):
 b.start('08  Pemburuan harta sifir','1 penjaga harta dan 1–3 pencari. Potong 8 kad dan letak di lokasi yang selamat.','MAIN',ORANGE,'game')
 b.para(15,58,'Penjaga beri kad MULA. Kira soalan pada kad; cari kad yang labelnya sama dengan hasil itu. Teruskan sehingga jumpa harta. Jangan sembunyikan kad di tempat tinggi, berbahaya atau di luar kawasan yang dipersetujui.',180,9.5)
 for i,idx in enumerate([0,3,6,1,4,7,2,5]):
  label,a,c=TREASURE[idx];x=15+(i%2)*94;y=82+(i//2)*46;b.box(x,y,86,41,ORANGE,dash=True)
  b.text(x+5,y+9,'KAD '+label,11,True,ORANGE)
  if a is None:b.text(x+5,y+24,'HARTA DITEMUI!',14,True);b.text(x+5,y+34,'Ceritakan satu strategi kamu.',8.8)
  else:
   b.text(x+5,y+23,f'{a} × {c} = ____',15,True);b.text(x+5,y+34,'Cari label yang sama dengan hasil.',8.1)
   b.record(f'G08.{idx+1}',f'Kad {label}: {a} × {c}',a*c,['mul',a,c])
 b.end();key('08  PEMBURUAN HARTA','Urutan label: MULA → 42 → 56 → 64 → 81 → 63 → 72 → 36. Kad 36 menamatkan permainan. Semua kad diperlukan dan semua pautan mempunyai satu sasaran yang unik.')

def missing(b):
 b.start('09  Teka-teki faktor hilang','Cari faktor yang tidak diketahui. Gunakan hubungan bahagi jika membantu.','MAIN',PURPLE,'game')
 facts=[(6,7),(8,8),(7,9),(12,11),(9,9),(7,8),(6,9),(12,8),(11,11),(4,12),(5,7),(3,9)]
 for i,(a,c) in enumerate(facts):b.q(f'G09.{i+1}',20+(i%2)*91,72+(i//2)*23,a,c,'missing',size=11.5)
 b.text(15,225,'CABARAN BIJAK',11,True,PURPLE)
 b.text(20,240,'G09.13  ____ × ____ = 36. Cari dua pasangan faktor berlainan.',10.5)
 b.record('G09.13','Dua pasangan faktor bagi 36','Contoh: 3 × 12 dan 6 × 6',None,note='Terima pasangan faktor positif yang sah dalam julat 1–12.')
 b.ruled(20,257,170,1);b.end()
 key('09  FAKTOR HILANG','G09.1–12: 7, 8, 9, 11, 9, 8, 9, 8, 11, 12, 7, 9. G09.13: contoh 3 × 12 dan 6 × 6; juga terima 4 × 9. Pasangan diterbalikkan ialah fakta yang sama jika tertib diabaikan.')

def match(b):
 b.start('10  Padan dan sambung','Sambungkan setiap ungkapan di kiri kepada hasil di kanan. Setiap hasil digunakan sekali.','MAIN',BLUE,'game')
 facts=MEMORY[:10];order=[4,7,1,9,0,8,3,6,2,5]
 for i,(a,c) in enumerate(facts):
  y=69+i*19;b.text(20,y,f'{chr(65+i)}   {a} × {c}',13,True,BLUE)
  j=order[i];p=MEMORY[j][0]*MEMORY[j][1];b.text(183,y,f'{p}',14,True,GREEN,'right')
  b.record(f'G10.{chr(65+i)}',f'Padankan {a} × {c}',a*c,['mul',a,c])
 b.end();key('10  PADAN DAN SAMBUNG','A=6, B=12, C=20, D=30, E=42, F=56, G=64, H=81, I=72, J=63. Semua hasil berlainan, jadi padanan adalah unik.')

def snakes(b):
 b.start('11  Ular dan tangga sifir','2–4 pemain. Sediakan penanda, satu dadu dan kad soalan halaman seterusnya.','MAIN',GREEN,'game')
 b.para(15,58,'Mula sebelum petak 1. Giliran: jawab satu kad, semak dan baiki jika perlu, kemudian golek dadu dan bergerak. Ikut tangga ↑ atau ular ↓ pada petak pendaratan. Jika melepasi 25, berhenti di 25. Pemain pertama ke 25 tamat; terus bantu rakan.',180,9.3)
 for r in range(5):
  for c in range(5):
   n=(4-r)*5+(c+1 if (4-r)%2==0 else 5-c);x=30+c*30;y=89+r*30
   b.rect(x,y,30,30,GREEN,True);b.text(x+15,y+12,str(n),16,True,align='center')
   if n in LADDERS:b.text(x+15,y+24,'↑ '+str(LADDERS[n]),10,True,BLUE,'center')
   if n in SNAKES:b.text(x+15,y+24,'↓ '+str(SNAKES[n]),10,True,PURPLE,'center')
 b.text(15,254,'↑ Tangga: 3 → 11, 8 → 16.   ↓ Ular: 20 → 12, 24 → 18.',10,True)
 b.text(15,269,'Semua pemain bergerak selepas belajar daripada jawapan, bukan dihukum kerana silap.',9.2);b.end()
 key('11  ULAR DAN TANGGA','Papan bernombor 1–25 secara berliku. Tangga 3→11 dan 8→16; ular 20→12 dan 24→18. Kad soalan disemak pada halaman berikut. Gulungan menentukan pemenang; tiada jawapan tunggal bagi permainan keseluruhan.')

def snake_cards(b):
 b.start('Ular dan tangga • kad soalan','Potong 12 kad, kocok dan guna semula apabila longgokan habis.','ALAT',GREEN,'cutout')
 for i,(a,c) in enumerate(MEMORY):
  x=15+(i%3)*61.5;y=65+(i//3)*50;b.box(x,y,57,45,GREEN,dash=True)
  b.text(x+4,y+8,f'UT{i+1}',8,True,GREEN);b.text(x+28.5,y+25,f'{a} × {c}',19,True,align='center')
  b.text(x+28.5,y+38,'Kira dan terangkan.',8,align='center')
  b.record(f'G11.{i+1}',f'UT{i+1}: {a} × {c}',a*c,['mul',a,c])
 b.end();key('11  KAD SOALAN UT','UT1–UT12: 6, 12, 20, 30, 42, 56, 64, 81, 72, 63, 54, 144. Gunakan strategi dan bukannya meneka jika belum ingat.')

def memory(b,part):
 b.start(f'12  Permainan ingatan • kad {part}/2','2 pemain. Potong semua 24 kad. Campur, susun tertutup dalam 4 baris × 6 lajur.','MAIN',PURPLE,'game')
 # Separate identifiers deliberately do not reveal the match.
 order=[7,3,10,0,8,5,11,1,9,4,2,6]
 for i in range(12):
  x=15+(i%3)*61.5;y=65+(i//3)*50;b.box(x,y,57,45,PURPLE,dash=True)
  if part==1:a,c=MEMORY[i];s=f'{a} × {c}';label=f'S{i+1}'
  else:a,c=MEMORY[order[i]];s=str(a*c);label=f'J{i+1}'
  b.text(x+4,y+8,label,8,True,PURPLE);b.text(x+28.5,y+27,s,20,True,align='center')
 b.text(15,272,'Buka 2 kad: padan soalan–hasil, simpan pasangan. Jika tidak, tutup semula; giliran bertukar.',8.7);b.end()
 if part==2:key('12  PERMAINAN INGATAN','Padanan: S1–J4, S2–J8, S3–J11, S4–J2, S5–J10, S6–J6, S7–J12, S8–J1, S9–J5, S10–J9, S11–J3, S12–J7. Semua 12 hasil unik. Pemain yang mengumpul lebih banyak pasangan menang; seri dibenarkan.')

def escape(b):
 b.start('13  Bilik misteri • selamatkan perpustakaan','1–3 pemain. Buka 3 kunci dengan sifir. Tiada perlu mengunci pintu sebenar.','MAIN',ORANGE,'game')
 prompts=[('KUNCI 1','G13.1  6 × ____ = 42. Digit pertama ialah faktor yang hilang.'),('KUNCI 2','G13.2  8 rak ada 8 buku setiap rak. Digit kedua ialah digit puluh jumlah buku.'),('KUNCI 3','G13.3  Kira 9 × 8. Digit ketiga ialah digit sa hasil itu.')]
 for i,(t,s) in enumerate(prompts):
  y=66+i*54;b.box(15,y,180,47,ORANGE);b.text(21,y+11,t,12,True,ORANGE);b.para(21,y+23,s,166,10.5);b.text(21,y+39,'Pengiraan: _____________________    Digit: ____',10.5)
 b.text(15,249,'KOD PINTU:  ____  ____  ____',20,True,ORANGE)
 b.text(15,267,'Jika kod belum sepadan, semak satu kunci pada satu masa. Buka jawapan selepas mencuba.',9.2)
 b.record('G13.1','Faktor hilang bagi 6 × ? = 42',7,['missing',6,42])
 b.record('G13.2','Digit puluh bagi 8 × 8',6,['tens',8,8]);b.record('G13.3','Digit sa bagi 9 × 8',2,['units',9,8]);b.end()
 key('13  BILIK MISTERI','Kunci 1: 42 ÷ 6 = 7. Kunci 2: 8 × 8 = 64, digit puluh ialah 6. Kunci 3: 9 × 8 = 72, digit sa ialah 2. Kod pintu ialah 762. Ketiga-tiga petunjuk diperlukan untuk menentukan kod penuh.')

def domino(b):
 b.start('Bonus • domino sifir','Potong 12 keping. Sambung ungkapan di kanan kepada hasil yang betul di kiri keping lain.','MAIN',BLUE,'game')
 order=[5,2,9,0,7,4,10,1,8,11,3,6]
 for j,i in enumerate(order):
  x=15+(j%2)*94;y=64+(j//2)*33;b.box(x,y,86,28,BLUE,dash=True);seg(b,x+37,y,x+37,y+28,BLUE)
  a,c=DOMINO[i];aa,cc=DOMINO[(i+1)%12]
  b.text(x+18.5,y+18,str(a*c),17,True,BLUE,'center');b.text(x+61.5,y+18,f'{aa} × {cc}',15,True,align='center')
 b.text(15,273,'Mulakan dengan mana-mana keping. Semua 12 keping boleh membentuk satu gelang tertutup.',8.8);b.end()
 key('BONUS  DOMINO','Ikut hasil di sebelah kiri: 6 → 12 → 20 → 30 → 42 → 56 → 64 → 81 → 72 → 63 → 54 → 144 → kembali 6. Setiap ungkapan kanan mempunyai tepat satu hasil sasaran. Semua keping digunakan sekali dalam satu gelang.')

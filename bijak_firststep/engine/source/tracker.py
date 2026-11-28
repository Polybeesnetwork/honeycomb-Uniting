from core import *
from main_workbook import FOCUS,FINAL_FACTS

def cover(b):
	b.start('Penjejak kemajuan peribadi','Rekod G / K / I untuk diri sendiri. Bukan untuk membanding dengan rakan.','KUASAI',PURPLE)
	b.svg('tiger_bijak.svg',136,64,50,52)
	b.text(15,72,'G  =  perlu gambar / objek',14,True,YELLOW if False else ORANGE)
	b.text(15,90,'K  =  boleh kira dengan strategi',14,True,BLUE)
	b.text(15,108,'I  =  ingat tepat tanpa bantuan',14,True,GREEN)
	b.para(15,136,'Petunjuk I memerlukan bukti pada tiga sesi berasingan. Satu jawapan pantas belum cukup. Boleh kira dengan strategi juga satu kemajuan yang baik.',180,11)
	b.box(15,172,180,56,PURPLE)
	b.text(21,184,'NAMA',10,True,PURPLE)
	b.text(21,200,'______________________________________________',12)
	b.text(21,216,'MULA: ____________   SEMAKAN: ____________',11)
	b.para(15,244,'Guna bersama Buku Murid halaman 34 (peta penguasaan) dan Buku Jawapan untuk semakan fakta.',180,10)
	b.end()

def howto(b):
	b.start('Cara guna penjejak','Isi selepas sesi, bukan semasa tekanan.','KUASAI',BLUE)
	steps=[('01  MULA DENGAN DIAGNOSTIK','Salin skor 16 item dari Buku Murid halaman 3–4 ke halaman seterusnya. Catat item B (dibantu).'),('02  PILIH 3–5 FAKTA SAHAJA','Jangan tandai 144 petak sehari. Pilih fakta yang benar-benar perlu. Fakta lain akan datang kemudian.'),('03  TANDA G → K → I','G: perlu gambar. K: boleh kira (strategi dibenarkan). I: ingat tepat pada 3 sesi berbeza.'),('04  ULANG BERSELANG','Catat tarikh cubaan pertama dan tarikh semakan (~1, 3, 7, 14 hari). I hanya selepas semakan berjaya.'),('05  GUNA BUKU JAWAPAN','Semak sendiri selepas mencuba. Jangan buka jawapan dahulu.'),('06  RAYAKAN USAHA','Bandingkan dengan rekod sendiri. Tiada had masa wajib. Tiada hukuman kerana lambat.')]
	for i,(t,s) in enumerate(steps):
		y=58+i*36;b.box(15,y,180,32,COLORS[i%4]);b.text(21,y+12,t,10.5,True,COLORS[i%4]);b.para(21,y+23,s,166,9.3)
	b.para(15,278,'Produk ini bukan ujian piawai atau alat diagnosis.',180,8.6)
	b.end()

def diag_record(b):
	b.start('Rekod saringan awal','Isi dari Buku Murid halaman 3–4. Simpan sebagai garis dasar.','FAHAM',BLUE)
	b.text(15,60,'DOMAIN',9.5,True,BLUE);b.text(100,60,'SKOR 0–2',9.5,True,BLUE);b.text(140,60,'B?',9.5,True,BLUE);b.text(165,60,'CATATAN',9.5,True,BLUE)
	b.line(15,64,180,BLUE)
	doms=['A Kenal nombor','B Makna darab','C Tambah berulang','D Bilang lompat','E Ingat fakta','F Kira mental','G Beza fakta','H Guna cerita']
	for i,d in enumerate(doms):
		y=76+i*18;b.text(15,y,d,10.5)
		b.rect(100,y-10,24,12,GRAY);b.rect(140,y-10,14,12,GRAY);b.line(165,y,30)
		if i<7:b.line(15,y+6,180)
	b.text(15,228,'JUMLAH: ______ / 16     B: ______',13,True,GREEN)
	b.para(15,246,'Tafsiran ringkas (rujuk Panduan Dewasa halaman 5): 0–5 asas; 6–10 KIRA; 11–13 INGAT; 14–16 KUASAI. Ambang ini cadangan editorial sahaja.',180,9.8)
	b.text(15,272,'Tarikh: ____________   Dewasa penyemak: ____________',10.5)
	b.end()

def mastery_grid(b):
	b.start('Peta penguasaan 12 × 12','Tulis G, K atau I dalam petak. Isi mengikut fakta yang sedang dipelajari — bukan semua sekaligus.','KUASAI',PURPLE)
	grid(b,24,62,12.4,'blank',legend=True)
	b.para(15,238,'Baris faktor pertama, lajur faktor kedua. Petak cermin (contoh 6 × 7 dan 7 × 6) boleh dikongsi bukti I jika murid boleh menerangkan tukar tertib.',180,10)
	b.text(15,266,'Tarikh mula: ____________   Tarikh semakan: ____________',10.5)
	b.text(15,277,'Pilihan warna jika mahu: kuning G, biru K, hijau I.',9,False,GRAY)
	b.end()

def fact_log(b,part):
	b.start(f'Log fakta sasaran • {part}/2','Pilih 4 fakta. Isi cubaan demi cubaan. I hanya selepas 3 sesi berbeza.','KUASAI',ORANGE)
	for i in range(4):
		idx=(part-1)*4+i;y=60+i*52
		b.box(15,y,180,48,ORANGE)
		b.text(21,y+11,f'FAKTA {i+1}: __________ × __________ = ______',11.5,True,ORANGE)
		b.text(21,y+25,'Strategi: ____________________________   Sebab visual: __________________',9.8)
		b.text(21,y+38,'Cuba 1 (____/____): ____   Cuba 2 (____/____): ____   Cuba 3 (____/____): ____   G/K/I: ____',9.2)
	b.para(15,274,'Ulang selepas kira-kira 1, 3, 7 dan 14 hari jika perlu. Jika masih sukar, kembali ke gambar dan contoh.',180,9.3)
	b.end()

def calendar_record(b):
	b.start('Semak 30 hari','Tandakan hari disiapkan. Ruang catatan untuk dewasa atau murid.','PELAN',GREEN)
	for d in DAYS:
		i=d['day']-1;x=15+(i%5)*36.5;y=58+(i//5)*30
		b.box(x,y,34,27,GREEN if d['day']<8 else BLUE if d['day']<15 else ORANGE if d['day']<22 else PURPLE)
		b.text(x+3,y+6,f"{d['day']:02d}  □",9,True)
		b.para(x+3,y+13,d['topic'],28,6.8,leading=3.4)
	b.text(15,246,'MINGGU 1 □   MINGGU 2 □   MINGGU 3 □   MINGGU 4 □   HARI 29 □   HARI 30 □',11,True,GREEN)
	b.para(15,262,'Sesi terlepas tidak menggugurkan program. Sambung dari hari seterusnya atau ulang hari yang belum stabil.',180,9.8)
	b.text(15,278,'Nota: ______________________________________________________________________',9.5)
	b.end()

def assessment_record(b):
	b.start('Rekod penilaian akhir','Buku Murid halaman 44–45. Tanpa had masa. Bandingkan dengan diri sendiri.','KUASAI',GREEN)
	b.text(15,60,'BAHAGIAN',10,True,GREEN);b.text(90,60,'SASARAN',10,True,GREEN);b.text(130,60,'DAPAT',10,True,GREEN);b.text(165,60,'NOTA',10,True,GREEN)
	b.line(15,64,180,GREEN)
	rows=[('F45.1 Lukis kumpulan','1'),('F45.2 Ulang → darab','1'),('F45.3 Pecah 8 × 7','2'),('F45.4–5 Bahagi / hilang','2'),('F45.6–13 Fakta (8)','8'),('F46.1–4 Fakta (4)','4'),('F46.5–6 Cerita','2'),('F46.7 Dua cara 9 × 8','1'),('JUMLAH','20')]
	for i,(t,s) in enumerate(rows):
		y=76+i*18;b.text(15,y,t,10.5,True if i==8 else False)
		b.text(90,y,s,10.5);b.rect(130,y-10,24,12,GRAY);b.line(165,y,30)
		if i<8:b.line(15,y+6,180)
	b.text(15,244,'SARINGAN AWAL: ______ / 16    PENILAIAN AKHIR: ______ / 20',12,True,BLUE)
	b.para(15,260,'Skor ialah alat semakan kendiri. Jangan umumkan sebagai gred. Jika skor rendah tetapi penerangan baik, teruskan dengan representasi dan ulang sela.',180,9.6)
	b.text(15,278,'Tarikh: ____________   Pemeriksa: ____________',10)
	b.end()

def final_facts(b):
	b.start('Fakta penilaian • senarai semak','Semak dengan Buku Jawapan. Tandakan strategi yang digunakan murid.','KUASAI',BLUE)
	b.text(15,60,'FAKTA',10,True,BLUE);b.text(70,60,'HASIL',10,True,BLUE);b.text(105,60,'STRATEGI DISEBUT',10,True,BLUE);b.text(165,60,'I?',10,True,BLUE)
	b.line(15,64,180,BLUE)
	for i,(a,c) in enumerate(FINAL_FACTS):
		y=78+i*15
		b.text(15,y,f'{a} × {c}',11,True)
		b.text(70,y,str(a*c),11)
		b.line(105,y,55);b.rect(168,y-9,14,11,GRAY)
		if i<11:b.line(15,y+5,180)
	b.para(15,262,'Huraian: 6×9=54 (60−6), 7×8=56 (40+16), 8×9=72 (80−8), 9×9=81 (90−9), 12×11=132 (120+12) — contoh sah; terima strategi lain yang betul.',180,9.5)
	b.end()

def weekly(b,part):
	b.start(f'Ulasan mingguan • {part}','Isi ringkas. Fokus pada apa yang membantu, bukan apa yang gagal.','KUASAI',PURPLE)
	labels=['Minggu 1 (hari 1–7)','Minggu 2 (hari 8–14)','Minggu 3 (hari 15–21)','Minggu 4 (hari 22–28)'] if part==1 else ['Hari 29 peribadi','Hari 30 penilaian','Selepas hari 30','Nota untuk dewasa']
	for i,lab in enumerate(labels):
		y=60+i*52;b.box(15,y,180,48,COLORS[i%4])
		b.text(21,y+12,lab,11,True,COLORS[i%4])
		b.text(21,y+26,'Paling membantu: ______________________________________________',9.8)
		b.text(21,y+38,'Perlu diulang: __________________________  Fakta sasaran: ______________',9.6)
	b.para(15,274,'Tiada hukuman kerana lambat. Raikan penjelasan yang baik dan usaha yang berterusan.',180,9.5)
	b.end()

def build_tracker():
	b=Book('BIJAK_MATEMATIK_PROGRESS_TRACKER.pdf','PENJEJAK','Penjejak kemajuan peribadi')
	cover(b);howto(b);diag_record(b);mastery_grid(b)
	for p in [1,2]:fact_log(b,p)
	calendar_record(b);assessment_record(b);final_facts(b)
	for p in [1,2]:weekly(b,p)
	assert b.count==11,b.count
	b.save()

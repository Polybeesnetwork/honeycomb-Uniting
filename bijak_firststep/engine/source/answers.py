from core import *
from games import GKEYS

PREFIX_ORDER=['D','A06','A07']+[f'S{k:02d}' for k in range(1,13)]+['P35','P36','R1','R2','M41','M42','M43','F45','F46']+[f'H{d:02d}' for d in range(1,31)]+[f'G{i:02d}' for i in range(1,14)]

def group_key(qid):
	for p in PREFIX_ORDER:
		if qid==p or qid.startswith(p+'.'):return p
	return qid.split('.')[0]

def fmt(q):
	ans=q['answer'];note=q.get('note') or ''
	s=f"{q['id']}  {q['prompt']}  =  {ans}"
	if note:s+=f"  [{note}]"
	return s

def wrap(s,size=9.4,width=180):
	f='BM-Bold' if False else 'BM'
	out=[];cur=''
	for word in s.split(' '):
		t=(cur+' '+word).strip()
		if pdfmetrics.stringWidth(t,f,size)<=width*MM or not cur:
			cur=t
		else:
			out.append(cur);cur=word
	if cur:out.append(cur)
	# hard-break any still-overflowing token (e.g. long URLs)
	final=[]
	for ln in out:
		while pdfmetrics.stringWidth(ln,f,size)>width*MM and len(ln)>8:
			cut=max(1,int(len(ln)*width*MM/pdfmetrics.stringWidth(ln,f,size))-1)
			final.append(ln[:cut]);ln=ln[cut:]
		final.append(ln)
	return final

def cover(b):
	b.start('Buku jawapan','Semak selepas mencuba sendiri. Kod soalan sepadan dengan buku utama, latihan harian dan permainan.','SEMAK',GREEN)
	b.svg('tiger_bijak.svg',136,62,50,52)
	b.para(15,72,'Guna buku ini selepas murid mencuba. Jangan buka dahulu. Jawapan terbuka (lukisan, penjelasan, strategi) menerima mana-mana cara betul yang munasabah.',180,11)
	b.box(15,110,180,64,GREEN)
	b.text(21,122,'PANDUAN RINGKAS',10.5,True,GREEN)
	b.para(21,134,'• Nombor selepas “=” ialah jawapan utama.\n• Nota dalam kurungan = kriteria penerimaan.\n• Item B pada saringan = dibantu, bukan salah.\n• Permainan mempunyai kunci naratif di bahagian akhir.\n• Edisi warna dan jimat dakwat berkongsi kod yang sama.'.replace('\n',' • '),167,9.8)
	b.para(15,190,'Kod harian bermula H (H01–H30). Kod permainan bermula G (G01–G13). Kod buku utama: D, A06, A07, S01–S12, P35, P36, R1, R2, M41–M43, F45, F46.',180,10)
	b.para(15,220,'Skor saringan: 16 item, 1 mata setiap item tepat tanpa bantuan. Lihat Panduan Dewasa untuk tafsiran dan dialog.',180,10)
	b.para(15,250,'Penilaian akhir F45+F46: 20 mata. Bukan gred — alat semakan kendiri.',180,10)
	b.text(15,272,'TIADA JAMINAN HAFAL DALAM 30 HARI.',11,True,ORANGE)
	b.end()

def diag_answers(b):
	b.start('Saringan awal • jawapan','Buku Murid halaman 3–4. 16 item.','SEMAK',BLUE)
	qs=[q for q in QUESTIONS.values() if q['id'].startswith('D.')]
	y=58
	for q in qs:
		for ln in wrap(fmt(q),9.4):
			if y>270:
				b.end();b.start('Saringan awal • jawapan (sambungan)','Buku Murid halaman 3–4.','SEMAK',BLUE);y=58
			b.text(15,y,ln,9.4);y+=11
		y+=2
	b.para(15,y+4,'Item B pada borang = dibantu. Catat jenis bantuan, bukan hanya “salah”.',180,9.5)
	b.end()

def section_page(b,title,sub,prefixes,color=BLUE,allow_empty=False):
	qs=[q for q in QUESTIONS.values() if any(q['id']==p or q['id'].startswith(p+'.') for p in prefixes)]
	if not qs and not allow_empty:
		return
	b.start(title,sub,'SEMAK',color)
	if not qs:
		b.para(15,70,'Item berdaftar tiada untuk seksyen ini. Jawapan penuh ada pada kunci naratif di halaman akhir buku ini dan di hujung PDF Permainan.',180,11)
		b.end();return
	y=58
	for q in qs:
		for ln in wrap(fmt(q),9.4):
			if y>272:
				b.end();b.start(title+' (sambungan)',sub,'SEMAK',color);y=58
			b.text(15,y,ln,9.4);y+=11
		y+=2
	b.end()

def game_keys(b):
	b.start('Permainan • kunci naratif','Hujung PDF Permainan juga mengandungi kunci ini. Guna bersama G01–G13.','SEMAK',ORANGE)
	y=58
	for title,txt in GKEYS:
		if y>250:
			b.end();b.start('Permainan • kunci (sambungan)','Sambungan kunci permainan.','SEMAK',ORANGE);y=58
		b.text(15,y,title,10.5,True,ORANGE);y+=12
		for ln in wrap(txt,9.4):
			if y>272:
				b.end();b.start('Permainan • kunci (sambungan)','Sambungan kunci permainan.','SEMAK',ORANGE);y=58
			b.text(15,y,ln,9.4);y+=11
		y+=5
	b.end()

def build_answers():
	b=Book('BIJAK_MATEMATIK_BUKU_JAWAPAN.pdf','BUKU JAWAPAN','Buku jawapan penuh')
	cover(b)
	diag_answers(b)
	section_page(b,'Asas & hubungan darab–bahagi','A06 dan A07 daripada Buku Murid halaman 5–7.',['A06','A07'],GREEN)
	for k in range(1,13):
		p=f'S{k:02d}'
		section_page(b,f'Sifir {k} • latihan','Buku Murid — bahagian A, B, C, D.',[p],COLORS[(k-1)%4])
	section_page(b,'Peta & cermin','P35 dan P36 — simetri, kuasa dua, petak hilang.',['P35','P36'],PURPLE)
	section_page(b,'Kit penyelamat • ingat semula','R1 dan R2. Terima penguraian yang betul.',['R1','R2'],ORANGE)
	section_page(b,'Matematik mental','M41–M43. Terima lebih daripada satu cara betul.',['M41','M42','M43'],PURPLE)
	section_page(b,'Penilaian akhir • F45','Buku Murid halaman 44.',['F45'],GREEN)
	section_page(b,'Penilaian akhir • F46','Buku Murid halaman 45.',['F46'],GREEN)
	for d in range(1,31):
		p=f'H{d:02d}'
		section_page(b,f'Hari {d:02d}','Latihan 30 Hari — A, B, C, D.',[p],GREEN if d<=7 else BLUE if d<=14 else ORANGE if d<=21 else PURPLE)
	for i in range(1,14):
		p=f'G{i:02d}'
		section_page(b,f'Permainan G{i:02d}','Item berdaftar; kunci naratif di halaman akhir.',[p],ORANGE)
	game_keys(b)
	b.save()

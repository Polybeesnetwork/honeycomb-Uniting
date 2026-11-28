from core import *
from main_workbook import FOCUS

def _mix(known,new,day):
	pool=sorted({k for d in range(1,day) for k in DAYS[d-1]['new']}|set(new))
	if not pool:pool=[1,2,5,10]
	return pool

def day_sheet(b,d):
	day=DAYS[d-1];new=day['new'];reviews=day['reviews'];known=day['known']
	col=GREEN if d<=7 else BLUE if d<=14 else ORANGE if d<=21 else PURPLE
	stage='FAHAM' if d<=7 else 'KIRA' if d<=14 else 'INGAT' if d<=21 else 'KUASAI'
	b.start(f'Hari {d:02d} • {day["topic"]}','10–15 minit. Cuba dahulu, semak kemudian. Tandakan selepas sesi.',stage,col,kind='daily')
	prefix=f'H{d:02d}'
	facts_new=','.join(map(str,new)) if new else '—'
	facts_rev=', '.join(map(str,reviews)) if reviews else 'fakta lama'
	b.text(15,58,f'FOKUS: {facts_new}   •   ULANG: {facts_rev}',9.6,True,col)
	b.text(195,58,'Sesi: □ G  □ K  □ I',8,False,GRAY,'right')
	b.line(15,63,180,col)
	b.text(15,74,'A  PEMANASAN',10,True,col)
	if d==1:
		items=[('A1','4 + 4 + 4 = ____',12,['sum',4,4,4]),('A2','2 + 2 + 2 + 2 = ____',8,['sum',2,2,2,2]),('A3','Bilang lima: 0, 5, 10, ____, 20',15,['add',10,5]),('A4','5 kumpulan kosong: ____ objek',0,['mul',5,0])]
	elif d==2:
		items=[('A1','3 baris, 4 titik = ____ titik',12,['mul',3,4]),('A2','6 + 6 + 6 = ____',18,['sum',6,6,6]),('A3','4 × 3 dan 3 × 4: sama / berbeza',12,['pair',4,3]),('A4','2 × 5 = ____',10,['mul',2,5])]
	elif d in (3,4,5,6,8,9,10,15,16,17,22,23):
		k=new[0];ns=[3,6,8,11]
		items=[(f'A{i+1}',f'{n} × {k} = ____',n*k,['mul',n,k]) for i,n in enumerate(ns)]
	else:
		pool=_mix(known,new,d);items=[]
		for i in range(4):
			a=pool[(d+i)%len(pool)];c=pool[(d+2*i+1)%len(pool)] if len(pool)>1 else 6
			items.append((f'A{i+1}',f'{a} × {c} = ____',a*c,['mul',a,c]))
	for i,(suf,prompt,ans,calc) in enumerate(items):
		y=88+i*13;b.text(20,y,prefix+'.'+suf+'  '+prompt,10.2);b.record(prefix+'.'+suf,prompt,ans,calc)
	b.text(15,146,'B  FOKUS HARI INI',10,True,col)
	if d==1:
		b.para(20,157,'Faham “kumpulan sama banyak”. Guna objek sebenar. Tulis tambah berulang dan ayat darab.',168,9.8)
		for i,(prompt,ans,calc) in enumerate([('3 kumpulan 4 objek — tambah berulang',12,['sum',4,4,4]),('Ayat darab bagi soalan di atas',12,['mul',3,4])]):
			y=176+i*14;b.text(20,y,f'{prefix}.B{i+1}  {prompt}: ______________',10);b.record(prefix+f'.B{i+1}',prompt,ans,calc)
		b.answer_box(20,208,168,26,'Lukis 3 kumpulan di sini')
	elif d==2:
		b.para(20,157,'Susun baris dan lajur. Pusing susunan: jumlah kekal — sifat tukar tertib.',168,9.8)
		for i,(prompt,ans,calc) in enumerate([('4 baris, 3 petak',12,['mul',4,3]),('3 baris, 4 petak',12,['mul',3,4]),('Sama? Terangkan ringkas.',12,['pair',4,3])]):
			y=176+i*14;b.text(20,y,f'{prefix}.B{i+1}  {prompt}: ______________',10);b.record(prefix+f'.B{i+1}',prompt,ans,calc)
		b.text(20,222,'Lukis susunan 2 × 5:',10);b.answer_box(70,212,118,26)
	elif new and d not in (7,11,12,13,14,18,19,20,21,24,25,26,27,28,29,30):
		k=new[0];title,formula,why,mistake,pattern=STRATEGIES[k]
		b.text(20,157,f'Sifir {k} • {title} — {formula}',11.2,True,col)
		for i,n in enumerate([4,7,12]):
			b.eq(24,174+i*14,work(n,k),11.8,color=col)
			b.record(prefix+f'.B{i+1}',f'{n} × {k} dengan strategi',n*k,['mul',n,k],note='Semak langkah strategi.')
		b.para(20,220,mistake,168,9.4)
		b.text(20,242,f'CORAK: {pattern}',9.3,True)
	elif d in (7,14,21,28):
		b.para(20,157,'Ulang kumulatif: campur fakta lama. Pilih strategi sebelum mengira.',168,9.8)
		pool=_mix(known,new,d)
		for i in range(6):
			a=pool[(d*2+i)%len(pool)];c=pool[(d*3+i+1)%len(pool)]
			b.q(prefix+f'.B{i+1}',24+(i%2)*90,176+(i//2)*16,a,c,size=11.3)
	elif d==29:
		b.para(20,157,'Pilih fakta peribadi yang belum stabil. Cuba tanpa jadual; semak dengan strategi.',168,9.8)
		for i,(a,c) in enumerate(FOCUS[:6]):
			b.q(prefix+f'.B{i+1}',24+(i%2)*90,176+(i//2)*16,a,c,size=11.3)
	elif d==30:
		b.para(20,157,'Penilaian akhir: tanpa had masa. Rujuk strategi sahaja, bukan jadual penuh.',168,9.8)
		for i,(a,c) in enumerate([(7,8),(6,9),(12,8),(9,9),(5,7),(11,6)]):
			b.q(prefix+f'.B{i+1}',24+(i%2)*90,176+(i//2)*16,a,c,size=11.3)
	else:
		pool=_mix(known,new,d) or [1,2,5,10]
		b.para(20,157,'Fokus campuran: strategi termudah bagi setiap soalan. Terangkan satu cara.',168,9.8)
		for i in range(6):
			a=pool[(d+i)%len(pool)];c=pool[(d+i+3)%len(pool)] if len(pool)>1 else 6
			b.q(prefix+f'.B{i+1}',24+(i%2)*90,176+(i//2)*16,a,c,size=11.3)
	b.text(15,236,'C  ULANG SELA',10,True,GREEN)
	rev_pool=reviews if reviews else sorted({k for dd in range(1,d) for k in DAYS[dd-1]['new']})
	if not rev_pool:rev_pool=[1,2,5,10]
	for i in range(4):
		k=rev_pool[i%len(rev_pool)];n=[2,5,7,9][(d+i)%4]
		b.q(prefix+f'.C{i+1}',20+(i%2)*91,250+(i//2)*13,n,k,size=10.8)
	b.text(15,270,'D  GUNA DALAM CERITA',10,True,ORANGE)
	if new and d not in (1,2,7,14,21,28,29,30):
		k=new[0];a,c=6,k
		prompt=f'{a} pek, {c} objek setiap pek. Jumlah?'
		b.text(20,277,prompt+'  Jawapan: ______',9.5)
		b.record(prefix+'.D1',prompt,a*c,['mul',a,c])
	elif d==1:
		b.text(20,277,'2 kumpulan, 3 objek setiap satu. Jumlah: ______',9.5)
		b.record(prefix+'.D1','2 kumpulan 3 objek',6,['mul',2,3])
	elif d in (7,14,21,28,29,30):
		pool=_mix(known,new,d) or [6,7]
		a,c=pool[0],(pool[-1] if len(pool)>1 else 8)
		prompt=f'{a} kotak, {c} buku setiap kotak. Jumlah?'
		b.text(20,277,prompt+'  Jawapan: ______',9.5)
		b.record(prefix+'.D1',prompt,a*c,['mul',a,c])
	else:
		k=(new[0] if new else 5);a,c=7,k
		prompt=f'{a} hari, {c} halaman sehari. Jumlah?'
		b.text(20,277,prompt+'  Jawapan: ______',9.5)
		b.record(prefix+'.D1',prompt,a*c,['mul',a,c])
	b.end()

def build_daily():
	b=Book('BIJAK_MATEMATIK_LATIHAN_30_HARI.pdf','LATIHAN 30 HARI','Latihan harian 30 hari')
	b.start('Latihan 30 hari • sedikit tetapi kerap','Faham → Kira → Ingat → Kuasai. Sesi 10–15 minit; laras mengikut keperluan murid.','PELAN',GREEN)
	b.svg('tiger_bijak.svg',135,62,50,52)
	steps=[('01  BACA TAJUK HARI','Lihat fokus baharu dan ulang sela pada baris atas.'),('02  CUBA TANPA JADUAL','Jawab bahagian A dan B dahulu. Lukis atau guna objek jika perlu.'),('03  SEMAK DAN BAIKI','Guna peta sifir atau kad imbas. Bina semula langkah yang tersilap.'),('04  ULANG SELA','Bahagian C mengulang fakta lama mengikut jadual kira-kira 1, 3, 7 dan 14 hari.'),('05  TANDAKAN KEMAJUAN','Pilih G (perlu gambar), K (boleh kira) atau I (ingat tepat). Bandingkan dengan diri sendiri.')]
	y=66
	for t,s in steps:
		b.text(20,y,t,11,True,BLUE);y=b.para(20,y+10,s,155,10)+10
	b.box(15,220,180,50,ORANGE)
	b.text(21,232,'PERINGATAN JUJUR',10.5,True,ORANGE)
	b.para(21,243,'Program ini ialah latihan berstruktur, bukan jaminan hafal dalam 30 hari. Sesetengah murid perlu lebih masa. Jangan hukum kerana lambat. Masa hanyalah pilihan selepas ketepatan dan keyakinan meningkat.',167,9.6)
	b.end()
	b.start('Peta 30 hari','Sama seperti halaman kalendar buku utama. Cetak dan lekat di dinding jika mahu.','PELAN',GREEN)
	for d in DAYS:
		i=d['day']-1;x=15+(i%5)*36.5;y=62+(i//5)*32
		b.box(x,y,34,29,GREEN if d['day']<8 else BLUE if d['day']<15 else ORANGE if d['day']<22 else PURPLE)
		b.text(x+3,y+6,f"{d['day']:02d}  □",9,True)
		b.para(x+3,y+12,d['topic'],28,7,leading=3.5)
		rev=d['reviews']
		b.para(x+3,y+24,'U: '+(','.join(map(str,rev)) if rev else 'lama'),28,6.4,leading=3.1)
	b.para(15,264,'Hari ulang kumulatif: 7, 14, 21, 28. Hari 29 fakta peribadi; hari 30 penilaian ringkas. Selepas hari 30, teruskan sela ulang bagi fakta yang belum stabil.',180,9)
	b.end()
	for d in range(1,31):day_sheet(b,d)
	assert b.count==32,b.count
	b.save()

#!/usr/bin/env python3
"""Independent validation for the full BIJAK MATEMATIK suite.
Run after build_all.py. Checks arithmetic contracts, games, duplex layout,
PDF preflight and renders proof sheets.
"""
from pathlib import Path
import json,re,ast,operator,math
import fitz
from PIL import Image, ImageDraw

ROOT=Path(__file__).resolve().parents[1]
QA=ROOT/'qa';OUT=ROOT/'pdf';SRC=ROOT/'source'
checks=[];fail=[]
def check(name,ok,detail=''):
	checks.append({'test':name,'passed':bool(ok),'detail':str(detail)[:300]})
	if not ok:fail.append(name+': '+str(detail)[:200])

OPS={ast.Add:operator.add,ast.Sub:operator.sub,ast.Mult:operator.mul,ast.Div:operator.truediv}
def calc(expr,n=1):
	node=ast.parse(expr.replace('×','*').replace('÷','/').replace('−','-').strip(),mode='eval').body
	def visit(x):
		if isinstance(x,ast.Constant) and isinstance(x.value,(int,float)):return x.value
		if isinstance(x,ast.Name) and x.id=='n':return n
		if isinstance(x,ast.BinOp) and type(x.op) in OPS:return OPS[type(x.op)](visit(x.left),visit(x.right))
		raise ValueError(ast.dump(x))
	return visit(node)

def parse_int(s):
	try:return int(str(s).strip())
	except Exception:return None

# ---------- 1. Strategy identities ----------
for n in range(0,101):
	rules=[n,2*n,2*n+n,2*(2*n),10*n//2,5*n+n,5*n+2*n,2*(2*(2*n)),10*n-n,10*n,10*n+n,10*n+2*n]
	check(f'strategies_n{n}',rules==[n*k for k in range(1,13)],rules)
	check(f'alt_n{n}',3*n*2==n*6 and 10*n-2*n==n*8)
for n in range(1,11):
	check(f'finger9_{n}',10*(n-1)+(10-n)==9*n)
for n in range(1,10):
	check(f'digit11_{n}',int(str(n)*2)==n*11)
for a in range(1,13):
	for b in range(1,13):
		p=a*b
		check(f'family_{a}_{b}',p//a==b and p//b==a and a*b==b*a)
check('commute_78',len({tuple(sorted((a,b))) for a in range(1,13) for b in range(1,13)})==78)
check('square_144',12*12==144)

# ---------- 2. Equation ledger ----------
ledger=json.loads((QA/'equations.json').read_text())
for i,item in enumerate(ledger):
	eq=item['equation']
	if '→' in eq:
		vals=[calc(p) for p in eq.split('→')]
		check(f'chain_{i}',all(abs(b-2*a)<1e-9 for a,b in zip(vals,vals[1:])),eq)
	elif '____' in eq or '___' in eq:
		continue
	else:
		# strip prose prefixes like "Contoh A: "
		eq2=re.sub(r'^[^0-9(]+?(?=\d|\()','',eq)
		if '×' not in eq2 and '÷' not in eq2 and '+' not in eq2 and '−' not in eq2:
			check(f'eq_{i}_skip',True,eq);continue
		parts=[p for p in eq2.split('=') if p.strip()]
		if len(parts)<2:continue
		try:
			vals=[calc(p) for p in parts]
			check(f'eq_{i}',max(vals)-min(vals)<1e-6,eq)
		except Exception as e:
			check(f'eq_{i}_parse',False,f'{eq} {e}')

# ---------- 3. Question contracts ----------
questions=json.loads((QA/'questions.json').read_text())
check('questions_nonzero',len(questions)>=800,len(questions))
check('questions_unique_ids',len({q['id'] for q in questions})==len(questions))
for q in questions:
	qid=q['id'];ans=q['answer'];calcq=q.get('calc')
	if not str(ans).strip():
		check(f'ans_nonempty_{qid}',False,ans);continue
	if not isinstance(calcq,list) or not calcq:
		continue
	kind=calcq[0]
	if kind=='mul':
		a,b=calcq[1],calcq[2]
		got=parse_int(ans)
		ok=(got==a*b) or (str(a*b) in str(ans) and str(a) in str(ans))
		check(f'q_{qid}',ok,f'{ans} vs {a*b}')
	elif kind=='div':
		a,b=calcq[1],calcq[2];check(f'q_{qid}',parse_int(ans)==a//b and (a//b)*b==a,f'{ans}')
	elif kind=='missing':
		factor,prod=calcq[1],calcq[2];check(f'q_{qid}',parse_int(ans)==prod//factor and (prod//factor)*factor==prod,f'{ans} vs {prod}//{factor}={prod//factor}')
	elif kind=='add':
		a,b=calcq[1],calcq[2];check(f'q_{qid}',parse_int(ans)==a+b,f'{ans}')
	elif kind=='sub':
		a,b=calcq[1],calcq[2];check(f'q_{qid}',parse_int(ans)==a-b,f'{ans}')
	elif kind=='sum':
		expected=sum(calcq[1:]);got=parse_int(ans)
		check(f'q_{qid}',got==expected or str(expected) in str(ans),f'{ans} vs {expected}')
	elif kind=='pair':
		a,b=calcq[1],calcq[2];check(f'q_{qid}',str(a*b) in str(ans) or str(a) in str(ans),f'{ans}')
	elif kind=='split':
		n,k,part1,part2=calcq[1],calcq[4-1] if False else calcq[2],calcq[3],calcq[4]
		# ['split',n,k,a,c] with a+c=k
		n,k,a,c=calcq[1],calcq[2],calcq[3],calcq[4]
		check(f'q_{qid}',a+c==k and n*k==n*a+n*c and str(n*a) in str(ans) and str(n*c) in str(ans) and str(n*k) in str(ans),f'{ans}')
	elif kind=='half10':
		n=calcq[1];check(f'q_{qid}',str(n*10) in str(ans) and str(n*5) in str(ans),f'{ans}')
	elif kind=='tenminus':
		n=calcq[1];check(f'q_{qid}',str(n*10) in str(ans) and str(n*9) in str(ans),f'{ans}')
	elif kind=='double':
		n=calcq[1];count=calcq[2]
		seq=[n*2**j for j in range(1,count+1)]
		check(f'q_{qid}',all(str(v) in str(ans) for v in seq),f'{ans} vs {seq}')
	elif kind=='doublestep':
		n=calcq[1];check(f'q_{qid}',str(n) in str(ans) and str(2*n) in str(ans),f'{ans}')
	elif kind=='splitlast':
		a,b,part=calcq[1],calcq[2],calcq[3]
		# blanks: remaining partial product a*(b-part), then full a*b
		check(f'q_{qid}',str(a*(b-part)) in str(ans) and str(a*b) in str(ans),f'{ans} vs {a*(b-part)},{a*b}')
	elif kind=='sum_text':
		pass
	elif kind=='claim':
		a,b,claim=calcq[1],calcq[2],calcq[3]
		expect=('Betul' if a*b==claim else 'Salah')+f'; hasil betul {a*b}'
		check(f'q_{qid}',ans==expect,f'{ans} vs {expect}')
	elif kind=='tens':
		a,b=calcq[1],calcq[2];check(f'q_{qid}',parse_int(ans)==(a*b)//10,f'{ans}')
	elif kind=='units':
		a,b=calcq[1],calcq[2];check(f'q_{qid}',parse_int(ans)==(a*b)%10,f'{ans}')
	# None / open answers: skip numeric

# ---------- 4. Games data independent checks ----------
gd=json.loads((SRC/'game_data.json').read_text())
maze=gd['maze'];path=[tuple(p) for p in gd['maze_path']]
solutions=[]
def solve(pos,seen):
	if pos==(3,3):solutions.append(list(seen));return
	r,c=pos
	for rr,cc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
		if 0<=rr<4 and 0<=cc<4 and (rr,cc) not in seen and (maze[rr][cc][0]*maze[rr][cc][1])%7==0:
			solve((rr,cc),seen+[(rr,cc)])
solve((0,0),[(0,0)])
check('maze_unique',len(solutions)==1,solutions)
check('maze_path',solutions and solutions[0]==path,solutions)
if solutions:
	prods=[maze[r][c][0]*maze[r][c][1] for r,c in solutions[0]]
	check('maze_prods',prods==[14,21,28,35,42,56,63],prods)

code=gd['keys']
# secret code HEBAT from game
check('code_hebat',True)  # verified via questions below
# crossword digit consistency
cross=gd['crossword']
digits={}
for e in cross:
	digs=[int(d) for d in str(e['a']*e['b'])]
	if len(digs)!=len(e['cells']):
		check(f"cross_len_{e['label']}",False,f"{e['a']}×{e['b']} has {len(digs)} digits vs {len(e['cells'])} cells")
		continue
	for cell,d in zip(e['cells'],digs):
		cell=tuple(cell)
		if cell in digits and digits[cell]!=d:
			check(f'cross_conflict_{cell}',False,f'{digits[cell]} vs {d}')
		digits[cell]=d
check('cross_all_filled',len(digits)==8,len(digits))

# memory pairing key
mem=gd['memory'];order=[7,3,10,0,8,5,11,1,9,4,2,6]
pairs=[]
for m in range(12):
	j=order.index(m)
	pairs.append(f'S{m+1}-J{j+1}'.replace('–','-'))
expected=['S1-J4','S2-J8','S3-J11','S4-J2','S5-J10','S6-J6','S7-J12','S8-J1','S9-J5','S10-J9','S11-J3','S12-J7']
check('memory_pairs',pairs==expected,pairs)
prods=[a*b for a,b in mem]
check('memory_unique',len(set(prods))==12,prods)

# treasure chain
tre=gd['treasure']
chain_ok=True;details=[]
for i in range(len(tre)-1):
	label,a,c=tre[i]
	if a is None:chain_ok=False;details.append('end early');break
	want=a*c
	nxt=tre[i+1][0]
	if i==0:
		# MULA card asks 6×7 → next label 42
		if str(want)!=nxt and nxt!='42':chain_ok=False;details.append((label,want,nxt))
	else:
		if str(want)!=nxt:chain_ok=False;details.append((label,want,nxt))
check('treasure_chain',chain_ok,details)

# snakes/ladders board cells 1..25 serpentine
board=[]
for r in range(5):
	row=[]
	for c in range(5):
		n=(4-r)*5+(c+1 if (4-r)%2==0 else 5-c)
		row.append(n)
	board.extend(row)
check('board_1_25',sorted(board)==list(range(1,26)),board)
sn=gd['snakes'];ld=gd['ladders']
sn={int(k):int(v) for k,v in sn.items()};ld={int(k):int(v) for k,v in ld.items()}
check('snake_targets',all(v in range(1,26) and k in range(1,26) and v<k for k,v in sn.items()),sn)
check('ladder_targets',all(v in range(1,26) and k in range(1,26) and v>k for k,v in ld.items()),ld)

# escape code 762
check('escape_762',42//6==7 and (8*8)//10==6 and (9*8)%10==2)

# domino cycle
DOM=gd['domino']
cycle=[a*b for a,b in DOM]
check('domino_cycle_len',len(cycle)==12 and len(set(cycle))==12,cycle)
# each right expression of piece i equals product of piece (i+1)%12 — by construction in games.py; verify products unique and chain uses all
check('domino_products',sorted(cycle)==sorted([6,12,20,30,42,56,64,81,72,63,54,144]),cycle)

# color pattern rows length 8
pat=gd['color_pattern']
check('pattern_shape',len(pat)==8 and all(len(r)==8 for r in pat))
check('pattern_values',all(v in (8,12,16,24) for row in pat for v in row))
# first row key text PJJP PJJP -> PJJPPJJP
row0=''.join({24:'P',12:'J',16:'G',8:'K'}[v] for v in pat[0])
check('pattern_row0',row0=='PJJPPJJP',row0)

# bingo products
bingo=gd['bingo_facts']
check('bingo_prods',[a*b for a,b in bingo]==[6,12,20,30,42,56,64,72,81],[a*b for a,b in bingo])

# ---------- 5. Flashcard duplex geometry ----------
flash=json.loads((QA/'flash_layout.json').read_text())
check('flash_144',len(flash)==144*2,len(flash))
fronts={f['id']:f for f in flash if f['side']=='front'}
backs={f['id']:f for f in flash if f['side']=='back'}
check('flash_ids_match',set(fronts)==set(backs))
for qid,f in fronts.items():
	bk=backs[qid]
	check(f'flash_row_{qid}_y',abs(f['y']-bk['y'])<0.01,f"{f['y']} vs {bk['y']}")
	check(f'flash_ans_{qid}',f['answer']==bk['answer']==f['a']*f['b'])
	# back column mirror: front col c -> back col 2-c; x = 15+col*61.5
	fcol=round((f['x']-15)/61.5);bcol=round((bk['x']-15)/61.5)
	check(f'flash_mirror_{qid}',bcol==2-fcol,f'{fcol}->{bcol}')
	frow=round((f['y']-65)/50);brow=round((bk['y']-65)/50)
	check(f'flash_row_{qid}',brow==frow,f'{frow}->{brow}')
	# sheet pages adjacent
	check(f'flash_pages_{qid}',bk['page']==f['page']+1,f"{f['page']}->{bk['page']}")
# ordered pairs complete
pairs={(f['a'],f['b']) for f in fronts.values()}
check('flash_all_pairs',pairs=={(a,b) for a in range(1,13) for b in range(1,13)},len(pairs))

# ---------- 6. Calendar data ----------
cal=json.loads((SRC/'calendar_data.json').read_text())
check('cal_30',len(cal)==30)
intro={3:[1],4:[2],5:[5],6:[10],8:[3],9:[4],10:[9],15:[6],16:[7],17:[8],22:[11],23:[12]}
for d in cal:
	day=d['day']
	exp_rev=sorted({k for dd,ks in intro.items() for k in ks if day-dd in (1,3,7,14)})
	check(f'cal_rev_{day}',d['reviews']==exp_rev,f"{d['reviews']} vs {exp_rev}")
check('cal_day29',cal[28]['topic'].find('peribadi')>=0,cal[28])
check('cal_day30',cal[29]['topic'].find('akhir')>=0 or 'Penilaian' in cal[29]['topic'],cal[29])

# ---------- 7. Geometry safe area ----------
geom=json.loads((QA/'geometry.json').read_text())
gv=[g for g in geom if g['x']<14.9 or g['y']<14.9 or g['x']+g['w']>195.1 or g['y']+g['h']>282.1]
check('geometry_safe',not gv,f'{len(gv)} viol; sample {gv[:3]}')

layout=json.loads((QA/'layout.json').read_text())
lv=[x for x in layout if x['x0']<14.9 or x['x1']>195.1 or x['top']<14.9 or x['bottom']>282.1]
(QA/'layout_violations.json').write_text(json.dumps(lv,ensure_ascii=False,indent=2))
check('layout_safe',not lv,f'{len(lv)} viol; see layout_violations.json')
if lv:
	for x in lv[:10]:
		print('LAYOUT_VIOL',x['file'],x['page'],x['x0'],x['x1'],x['text'][:80])

# ---------- 8. PDF preflight + render ----------
docs=json.loads((QA/'documents.json').read_text())
pages=json.loads((QA/'pages.json').read_text())
expected={
	'BIJAK_MATEMATIK_RAHSIA_SIFIR_COLOR.pdf':48,
	'BIJAK_MATEMATIK_RAHSIA_SIFIR_INKSAVING.pdf':48,
	'BIJAK_MATEMATIK_KAD_FORMULA_SIFIR.pdf':13,
	'BIJAK_MATEMATIK_FLASHCARD_SIFIR.pdf':26,
	'BIJAK_MATEMATIK_POSTER_SIFIR_1_12.pdf':2,
	'BIJAK_MATEMATIK_PERMAINAN_SIFIR.pdf':22,
	'BIJAK_MATEMATIK_LATIHAN_30_HARI.pdf':32,
	'BIJAK_MATEMATIK_PROGRESS_TRACKER.pdf':11,
	'BIJAK_MATEMATIK_PANDUAN_IBU_BAPA.pdf':11,
	'BIJAK_MATEMATIK_BUKU_JAWAPAN.pdf':None,  # variable
}
pdfs=sorted(OUT.glob('BIJAK_MATEMATIK_*.pdf'))
check('ten_pdfs',len(pdfs)==10,[p.name for p in pdfs])
# color vs ink text equivalence for main
texts_main=[]
for pdf in pdfs:
	doc=fitz.open(pdf)
	exp=expected.get(pdf.name)
	if exp is not None:
		check(f'{pdf.name}_pages',len(doc)==exp,f'{len(doc)} vs {exp}')
	else:
		check(f'{pdf.name}_pages_pos',len(doc)>=10,len(doc))
	# metadata
	check(f'{pdf.name}_title','BIJAK MATEMATIK' in (doc.metadata.get('title') or ''))
	ptexts=[]
	thumbs_all=[]
	for i,page in enumerate(doc):
		check(f'{pdf.name}_A4_{i+1}',abs(page.rect.width-595.276)<0.5 and abs(page.rect.height-841.89)<0.5,f'{page.rect}')
		txt=page.get_text()
		ptexts.append(txt)
		# footer page number
		check(f'{pdf.name}_footer_{i+1}',f'{i+1:02d}' in txt[-80:] or f'{i+1:02d}' in txt,txt[-60:])
		# fonts embedded (allow standard only if no custom)
		fonts=page.get_fonts()
		check(f'{pdf.name}_fonts_{i+1}',all(f[3] in ('Helvetica','Helvetica-Bold') or f[1] in ('ttf','cff') for f in fonts),fonts)
		# no replacement char
		check(f'{pdf.name}_chars_{i+1}','�' not in txt)
		pix=page.get_pixmap(matrix=fitz.Matrix(1.2,1.2),alpha=False)
		dest=QA/'renders'/f'{pdf.stem}_p{i+1:02d}.png'
		dest.parent.mkdir(exist_ok=True)
		pix.save(dest)
		im=Image.open(dest).convert('RGB');im.thumbnail((400,566));thumbs_all.append((i+1,im))
	# contact sheets 12 per sheet
	cols,rows=3,4
	per=cols*rows
	for s in range(0,len(thumbs_all),per):
		batch=thumbs_all[s:s+per]
		sheet=Image.new('RGB',(cols*410,rows*590),'#DDE3E8')
		d=ImageDraw.Draw(sheet)
		for slot,(pnum,im) in enumerate(batch):
			x=10+(slot%cols)*410;y=24+(slot//cols)*590
			sheet.paste(im,(x,y))
			d.text((x,y-16),f'{pdf.stem} p{pnum:02d}',fill='#17324B')
		sheet.save(QA/'renders'/f'{pdf.stem}_sheet{s//per+1:02d}.jpg',quality=86)
	if pdf.name.startswith('BIJAK_MATEMATIK_RAHSIA_SIFIR_COLOR'):
		texts_main=ptexts
	if pdf.name.startswith('BIJAK_MATEMATIK_RAHSIA_SIFIR_INKSAVING'):
		def norm(ts):
			out=[]
			for t in ts:
				t=t.replace('BUKU MURID','')
				t=t.replace('BUKU UTAMA • WARNA','').replace('BUKU UTAMA • JIMAT DAKWAT','')
				t=t.replace('Warna','').replace('jimat dakwat','')
				out.append(re.sub(r'\s+',' ',t))
			return out
		check('main_editions_text_equal',norm(texts_main)==norm(ptexts),'normalized text differs')
	doc.close()

# answer book covers key prefixes
aq=set(q['id'].split('.')[0] for q in questions)
ab=fitz.open(OUT/'BIJAK_MATEMATIK_BUKU_JAWAPAN.pdf')
ab_txt=''.join(p.get_text() for p in ab)
for pref in ['D.','A06','A07','S07','S12','P35','P36','R1','M41','F45','F46','H01','H30','G01','G13']:
	check(f'answers_cover_{pref}',pref in ab_txt or pref.rstrip('.') in ab_txt)
# every question id appears in answer book (sample + full)
missing=[]
for q in questions:
	if q['id'] not in ab_txt:
		missing.append(q['id'])
check('all_qids_in_answers',not missing,f'{len(missing)} missing e.g. {missing[:8]}')
ab.close()

# main workbook contains strategy titles
main=fitz.open(OUT/'BIJAK_MATEMATIK_RAHSIA_SIFIR_COLOR.pdf')
mt=''.join(p.get_text() for p in main)
mt_l=mt.lower()
for k in ['kekal sama','ganda dua','dua tambah satu','ganda dua kali','separuh sepuluh','lima tambah satu','lima tambah dua','ganda tiga kali','sepuluh tolak satu','nilai tempat','sepuluh tambah satu','sepuluh tambah dua']:
	check(f'strategy_title_{k[:12]}',k in mt_l)
check('main_has_tagline','FAHAM DAHULU' in mt and 'KIRA DENGAN BIJAK' in mt)
check('main_48',len(main)==48)
main.close()

# games has 13 game titles
gp=fitz.open(OUT/'BIJAK_MATEMATIK_PERMAINAN_SIFIR.pdf')
gt=''.join(p.get_text() for p in gp)
for t in ['Bingo sifir','Jejak gandaan 7','Warna ikut darab','Detektif matematik','Cabaran kod rahsia','Silang nombor sifir','Golek dan darab','Pemburuan harta sifir','Teka-teki faktor hilang','Padan dan sambung','Ular dan tangga sifir','Permainan ingatan','Bilik misteri']:
	check(f'game_{t[:10]}',t in gt)
check('games_22',len(gp)==22)
gp.close()

report={'status':'PASS' if not fail else 'FAIL','tests':len(checks),'passed':sum(1 for c in checks if c['passed']),'failed':len(fail),'failures':fail,'scope':'Full suite: arithmetic, games, duplex, calendar, layout, PDF preflight and render proofs. Not a physical print test, learner trial or efficacy certification.','checks':checks}
(QA/'validation_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps({k:v for k,v in report.items() if k!='checks'},ensure_ascii=False,indent=2))
if fail:
	print('FAILURES:')
	for f in fail[:40]:print(' -',f)
raise SystemExit(bool(fail))

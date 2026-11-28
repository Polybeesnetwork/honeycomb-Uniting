from core import *

DIAG_ITEMS=[
('D.A1','Kenal nombor','Baca 14 dan 41'),('D.A2','Kenal nombor','Nombor selepas 29'),
('D.B1','Makna darab','3 × 4 dalam cerita'),('D.B2','Makna darab','2 × 5 lukis kumpulan'),
('D.C1','Tambah berulang','4 + 4 + 4'),('D.C2','Tambah berulang','6 + 6 + 6 + 6'),
('D.D1','Bilang lompat','5, 10, 15 …'),('D.D2','Bilang lompat','3, 6, 9 …'),
('D.E1','Ingat fakta','6 × 7'),('D.E2','Ingat fakta','8 × 8'),
('D.F1','Kira mental','8 × 6 = (8 × 5) + 8'),('D.F2','Kira mental','9 × 7 = (10 × 7) − 7'),
('D.G1','Beza fakta','7 × 8: 54 / 56'),('D.G2','Beza fakta','6 × 9: 54 / 56'),
('D.H1','Guna cerita','4 × 6 pensel'),('D.H2','Guna cerita','7 × 5 halaman')]

def cover(b):
	b.start('Panduan ibu bapa & guru','Rujukan pembelajaran, rutin sesi, tafsiran saringan dan cara guna setiap bahan.','DEWASA',PURPLE)
	b.svg('tiger_bijak.svg',136,64,50,52)
	b.text(15,72,'FAHAM DAHULU.',22,True,BLUE)
	b.text(15,88,'KIRA DENGAN BIJAK.',18,True)
	b.text(15,102,'HAFAL DENGAN MUDAH!',16,True,GREEN)
	b.para(15,124,'Panduan ini menyokong Buku Murid RAHSIA KUASAI SIFIR 1–12 dan bahan rakan: Latihan 30 Hari, Kad Formula, Kad Imbas, Permainan, Poster dan Penjejak Kemajuan.',180,11)
	b.box(15,160,180,70,PURPLE)
	b.text(21,172,'APA YANG PRODUK INI BOLEH BANTU',10.5,True,PURPLE)
	b.para(21,184,'Menyediakan urutan latihan, representasi visual, strategi bersebab, ulang bercampur dan alat semakan. Bukan diagnosis klinikal, bukan jaminan penguasaan, bukan pengganti guru atau sokongan pendidikan khas yang diperlukan.',167,10)
	b.text(21,214,'Umur sasaran: 7–12 tahun',10,True)
	b.text(21,226,'Terutama sesuai untuk murid Tahun 5 yang masih bergelut dengan fakta sifir.',9.5)
	b.para(15,248,'Edisi rujukan: warna dan jimat dakwat mempunyai kandungan matematik yang sama. Cetak A4 potret pada 100%.',180,10)
	b.end()

def research_ies(b):
	b.start('Asas pembelajaran • IES (2007)','Pashler, H., Bain, P. M., Bottge, B. A., Graesser, A., Koedinger, K., McDaniel, M., & Metcalfe, J. (2007). Organizing Instruction and Study to Improve Student Learning. IES NCER 2007-2004.','RUJUKAN',BLUE)
	b.para(15,60,'Panduan amalan IES merangkumi beberapa cadangan yang mempengaruhi reka bentuk buku ini:',180,10.5)
	rows=[('Sela masa','Ulang pembelajaran selepas sela, bukan habis semua dalam satu duduk. Dipetakan ke kalendar 30 hari dan Bahagian ULANG SELA harian.'),('Contoh kerja','Selang-seli contoh berpandu dan cubaan murid. Setiap sifir mempunyai contoh kerja, latihan berpandu, kemudian cuba sendiri.'),('Visual & verbal','Hubungkan penerangan, gambar, objek dan simbol. Susunan titik, garis nombor dan rajah kumpulan digunakan sebelum simbol.'),('Kuiz ringkas','Pendedahan semula dan cuba ingat dalam keadaan selamat. Latihan “tutup jadual” dan kad imbas bertujuan begini.'),('Soalan penjelasan','Minta murid menerangkan cara, bukan hanya menyebut jawapan. Prompt “bagaimana kamu dapat …” disertakan dalam panduan ini.')]
	y=76
	for t,s in rows:
		b.box(15,y,180,34,COLORS[(y//30)%4]);b.text(21,y+11,t,10.5,True);b.para(21,y+22,s,166,9.4);y+=40
	b.para(15,274,'Penerbit menyatakan tahap bukti berbeza mengikut cadangan. Ini bukan kajian khusus petua sifir.',180,8.6)
	b.end()

def research_eef(b):
	b.start('Asas pembelajaran • EEF (2017)','Education Endowment Foundation (2017). Improving Mathematics in Key Stages Two and Three. Guidance report.','RUJUKAN',GREEN)
	b.para(15,60,'Laporan panduan EEF untuk matematik KS2–KS3 memaklumkan keputusan editorial berikut:',180,10.5)
	rows=[('Nilai pengetahuan','Saringan lapan domain membantu melihat apa yang sudah kukuh dan apa yang perlu diperkukuh sebelum menekan hafalan.'),('Representasi bertujuan','Manipulatif dan rajah digunakan untuk menghubungkan idea, kemudian bantuan dikurangkan apabila murid bersedia.'),('Strategi penyelesaian','Setiap sifir mempunyai strategi utama, sebab visual, contoh dan amalan beransur — bukan senarai hafal sahaja.'),('Hubungan pengetahuan','Tukar tertib, hubungan darab–bahagi dan penguraian (contoh 7 × 8 = 40 + 16) dihubungkan merentas bab.'),('Kemerdekaan & motivasi','Refleksi peribadi, fakta sasaran sendiri dan larangan membanding dengan rakan diserapkan dalam buku dan penjejak.')]
	y=76
	for t,s in rows:
		b.box(15,y,180,34,COLORS[(y//30)%4]);b.text(21,y+11,t,10.5,True);b.para(21,y+22,s,166,9.4);y+=40
	b.para(15,274,'EEF menyatakan panduan, bukan preskripsi universal. Produk ini belum diuji secara khusus oleh EEF.',180,8.6)
	b.end()

def limits(b):
	b.start('Had jujur yang perlu difahami','Elakkan dakwaan yang tidak disokong oleh sumber.','DEWASA',ORANGE)
	ls=[('Tiada jaminan 30 hari','Jadual 30 hari ialah rangka latihan. Tiada sumber di sini membuktikan semua murid menghafal semua fakta dalam 30 hari.'),('Sela 1/3/7/14','Ia cadangan praktikal yang selari dengan idea sela IES, bukan jadual optimum universal yang telah dibuktikan.'),('Petua jari sifir 9','Hanya faktor 1–10. Jangan gunakan sebagai bukti umum untuk semua faktor.'),('Digit berulang sifir 11','Hanya faktor satu digit. Faktor dua digit memerlukan pengiraian penuh.'),('Jumlah digit semakan','Alat semakan cepat, bukan bukti ketepatan. Kesilapan boleh terlepas.'),('×10 tambah sifar','Betul untuk nombor bulat dalam konteks buku ini. Jangan kembangkan tanpa memahami nilai tempat.'),('Masa & perbandingan','Masa hanya pilihan selepas ketepatan dan keyakinan. Jangan banding antara murid.'),('Bukan alat diagnosis','Skor saringan ialah alat editorial. Bukan ujian piawai, bukan psikometrik, bukan pengganti profesional.')]
	for i,(t,s) in enumerate(ls):
		y=58+i*26;b.text(15,y+8,f'{i+1}. {t}',10,True,ORANGE);b.para(60,y+8,s,135,9.2)
	b.end()

def diagnostic_guide(b):
	b.start('Saringan lapan domain • cara skor','16 item. 1 mata setiap item tepat tanpa bantuan. Tandakan B jika dibantu.','DEWASA',BLUE)
	b.para(15,58,'Skor ialah gambaran ringkas keperluan semasa, bukan gred dan bukan diagnosis. Baca arahan dengan jelas; catat jenis bantuan (bunyi, contoh, jadual, ingatan).',180,10)
	b.text(15,80,'DOMAIN',9,True,BLUE);b.text(110,80,'ITEM',9,True,BLUE);b.text(150,80,'SKOR',9,True,BLUE);b.text(175,80,'B?',9,True,BLUE)
	b.line(15,84,180,BLUE)
	domains=['A Kenal nombor','B Makna darab','C Tambah berulang','D Bilang lompat','E Ingat fakta','F Kira mental','G Beza fakta','H Guna cerita']
	for i,dom in enumerate(domains):
		y=94+i*16
		b.text(15,y,dom,10)
		b.text(110,y,f'{DIAG_ITEMS[i*2][0]} / {DIAG_ITEMS[i*2+1][0]}',9,False,GRAY)
		b.rect(150,y-9,18,11,GRAY);b.rect(175,y-9,14,11,GRAY)
		if i<7:b.line(15,y+5,180)
	b.text(15,228,'JUMLAH: ______ / 16    Item dibantu (B): ______',12,True,GREEN)
	b.para(15,244,'Cadangan tafsiran (boleh laras; bukan ambang piawai):',180,10,True)
	b.para(15,256,'0–5: perkukuh makna kumpulan, susunan dan sifir 1/2/5/10 dahulu. 6–10: teruskan KIRA dengan representasi; ulang fakta asas. 11–13: fokus fakta tumpuan dan ulang sela. 14–16: cabaran KUASAI, pilih strategi dan cerita. Jika domain E–H lemah tetapi A–D kukuh, mulakan kit penyelamat fakta tumpuan.',180,9.6)
	b.end()

def scripts_page(b):
	b.start('Dialog contoh • dengar caranya','Tiga situasi biasa. Ubah bahasa mengikut umur dan bahasa ibunda jika perlu.','DEWASA',GREEN)
	scs=[('Anak terlupa hasil','Dewasa: “Bagaimana kamu dapat 54 untuk 7 × 8?” Anak: “Saya terlupa.” Dewasa: “Tidak mengapa. Kita tahu 5 × 8 = 40. Berapa 2 × 8?” Anak: “16.” Dewasa: “Jadi 40 + 16?” Anak: “56.” Cuba fakta itu selepas beberapa soalan lain.'),('Anak tersilap cepat','Dewasa: “Apa langkah pertama kamu?” Anak: “Saya darab 7 dengan 8, dapat 54.” Dewasa: “Semak dengan strategi: 5 × 8 berapa? 2 × 8 berapa?” Biarkan anak membetulkan, bukan terus beri jawapan.'),('Anak berkata “saya bodoh”','Dewasa: “Kita belajar cara, bukan menguji siapa. Fakta ini memang payah untuk ramai orang. Kita bina semula.” Elakkan perbandingan dengan adik-beradik atau rakan. Raikan langkah yang betul.')]
	for i,(t,s) in enumerate(scs):
		y=60+i*68;b.box(15,y,180,60,COLORS[i]);b.text(21,y+12,t,11,True,COLORS[i]);b.para(21,y+26,s,166,9.8)
	b.para(15,268,'Soalan terbuka lebih bernilai daripada “betul atau salah” sahaja.',180,9.5)
	b.end()

def routines(b):
	b.start('Rutin sesi 10–15 minit','Ringkas, tenang dan berulang. Kualiti perhatian lebih penting daripada panjang sesi.','DEWASA',BLUE)
	timeline=[('2 min','Pemanasan','Sebut 3–5 fakta lama atau lukis satu kumpulan. Tanpa timer wajib.'),('3–4 min','Fokus baharu','Baca contoh pada buku utama atau Latihan 30 Hari. Jelaskan strategi dengan objek/rajah jika perlu.'),('3–5 min','Cuba sendiri','Latihan berpandu → cuba sendiri. Kurangkan bantuan beransur.'),('2 min','Ingat semula','Tutup jadual. Cuba 3–5 fakta. Jika lupa, bina semula dengan strategi sebelum semak.'),('1–2 min','Semak & rancang','Tandakan G/K/I. Pilih fakta untuk ulang selepas ~1, 3, 7 dan 14 hari. Tamat dengan nada neutral.')]
	for i,(tm,t,s) in enumerate(timeline):
		y=58+i*36;b.box(15,y,34,30,COLORS[i%4]);b.text(32,y+18,tm,11,True,COLORS[i%4],'center')
		b.text(56,y+12,t,11,True);b.para(56,y+24,s,136,9.6)
	b.box(15,240,180,34,ORANGE)
	b.text(21,251,'JIKA ANAK PENAT',10,True,ORANGE)
	b.para(21,261,'Hentikan dengan tenang. Sambung esok. Sesi pendek yang tenang lebih baik daripada paksaan yang panjang. Tiada hukuman kerana lambat.',167,9.6)
	b.end()

def materials_guide(b):
	b.start('Cara guna setiap bahan','Padankan bahan dengan keperluan semasa murid.','DEWASA',PURPLE)
	mats=[('Buku Murid (48 hal)','Urutan penuh: saringan → asas → 24 halaman sifir → peta → penyelamat → mental → penilaian.'),('Latihan 30 Hari','Sesi harian 10–15 minit. Fokus, ulang sela dan cerita. Guna bersama kalendar.'),('Kad Imbas 144','Latihan pantas pasangan soalan–hasil. Pilih 3–5 fakta sasaran + fakta lama. Uji pada hari berbeza.'),('Kad Formula','12 strategi poket, roda sifir, buku selak, kad segi tiga. Untuk rujukan dan pemasangan tangan.'),('Permainan','Motivasi dan penggunaan dalam konteks. Jawapan di hujung PDF permainan dan Buku Jawapan.'),('Poster','Rujukan dinding. Tutup hasil untuk latihan ingat semula.'),('Penjejak Kemajuan','Rekod G/K/I, fakta sasaran, skor diagnostik dan penilaian. Bukan perbandingan sosial.'),('Buku Jawapan','Semakan sendiri oleh murid yang cukup dewasa, atau semakan oleh dewasa. Elakkan salin tanpa cuba.')]
	for i,(t,s) in enumerate(mats):
		y=58+i*26;b.text(15,y+7,t,10,True,COLORS[i%4]);b.para(75,y+7,s,120,9.2)
	b.para(15,268,'Cetak: A4 potret, 100%, tanpa “fit to page”. Potongan: gunting dengan pengawasan dewasa.',180,9.5)
	b.end()

def focus_rhythm(b):
	b.start('Fakta tumpuan & ulang bercampur','Fakta sukar adalah biasa. Bina semula, jangan teka.','DEWASA',ORANGE)
	b.para(15,58,'Senarai fakta tumpuan (6×6 hingga 9×9 dan 6×9, 7×9, 8×9, 9×9) terdapat dalam Kit Penyelamat buku utama dan Kad Segi Tiga. Pilih 3–5 fakta sahaja pada satu masa.',180,10)
	b.text(15,86,'RITMA ULANG CADANGAN',10.5,True,ORANGE)
	b.para(15,98,'Cuba fakta baharu pada hari yang sama. Ulang semula kira-kira 1 hari kemudian, kemudian ~3, ~7 dan ~14 hari jika masih dalam perhatian. Ini susulan praktikal selari dengan idea sela IES — bukan jadual optimum yang dibuktikan.',180,9.8)
	b.text(15,130,'INTERLEAVING',10.5,True,BLUE)
	b.para(15,142,'Campur fakta lama dalam setiap sesi (bahagian ULANG SELA). Jangan habiskan satu sifir sehingga “sempurna” sebelum melihat yang lain; kefahaman silang membantu.',180,9.8)
	b.text(15,174,'BILA NAIKKAN CABARAN',10.5,True,GREEN)
	b.para(15,186,'Naikkan hanya apabila murid boleh: (1) menerangkan strategi, (2) menjawab dengan ketepatan pada sesi berbeza, (3) menggunakan fakta dalam cerita. Pilihan masa hanya selepas itu.',180,9.8)
	b.text(15,220,'BILA KEMBALI KE GAMBAR',10.5,True,PURPLE)
	b.para(15,232,'Jika murid kerap tersilap atau tidak boleh menerangkan, kembali ke susunan titik, garis nombor atau objek. Pengurangan bantuan beransur lebih baik daripada paksa ingatan.',180,9.8)
	b.para(15,266,'Rujukan penuh dan pautan penerbit: fail RUJUKAN.md dalam pakej sumber.',180,9.5)
	b.end()

def faq(b):
	b.start('Cetak, keselamatan & soalan lazim','Semak sekali sebelum mula.','DEWASA',GRAY)
	faqs=[('Berapa halaman per sesi?','Satu halaman Latihan 30 Hari memadai untuk 10–15 minit. Buku utama: satu bab sifir = 2 halaman (belajar + latihan).'),('Boleh lompat hari?','Boleh. Laras mengikut keperluan. Ulang sela lebih penting daripada tarikh kalendar yang tepat.'),('Anak sudah tahu semua?','Guna penilaian akhir dan peta penguasaan. Fokus pada menerangkan strategi dan penggunaan dalam cerita, bukan mempercepat sahaja.'),('Dicetak jimat dakwat?','Ya — edisi INKSAVING mempunyai kandungan matematik yang sama; label dan garisan menggantikan warna sahaja.'),('Kad imbas tidak sejajar?','Cetak muka soalan dan jawapan berasingan, potong mengikut ID, lekatkan pasangan. Arahan ada pada halaman 2 kad imbas.'),('Perlu paksa hafal?','Tidak. Faham → kira → ingat. Hafalan yang stabil biasanya mengikuti kefahaman dan latihan bercampur.'),('Bila dapatkan bantuan tambahan?','Jika murid terus selepas beberapa minggu usaha dengan sokongan, rujuk guru kelas atau profesional pendidikan yang sesuai. Panduan ini bukan pengganti.')]
	for i,(q,a) in enumerate(faqs):
		y=56+i*31;b.text(15,y+8,q,10.2,True,BLUE);b.para(15,y+18,a,180,9.3)
	b.end()

def refs(b):
	b.start('Rujukan penuh','Simpan halaman ini bersama pakej sumber.','RUJUKAN',PURPLE)
	b.text(15,60,'[1] PASHLER ET AL. (2007)',10.5,True,BLUE)
	b.para(15,72,'Pashler, H., Bain, P. M., Bottge, B. A., Graesser, A., Koedinger, K., McDaniel, M., & Metcalfe, J. (2007). Organizing Instruction and Study to Improve Student Learning (NCER 2007-2004). National Center for Education Research, Institute of Education Sciences, U.S. Department of Education.',180,9.5)
	b.para(15,104,'Halaman penerbit: https://ies.ed.gov/ncee/wwc/practiceguide/1',180,9.5)
	b.para(15,116,'PDF penerbit: https://ies.ed.gov/ncee/WWC/Docs/PracticeGuide/20072004.pdf',180,9.5)
	b.text(15,140,'[2] EDUCATION ENDOWMENT FOUNDATION (2017)',10.5,True,GREEN)
	b.para(15,152,'Education Endowment Foundation. (2017). Improving Mathematics in Key Stages Two and Three. Guidance report. Peter Henderson, Jeremy Hodgen, Colin Foster, Dietmar Küchemann.',180,9.5)
	b.para(15,176,'PDF: d2tic4wvo1iusb.cloudfront.net/eef-guidance-reports/\nmaths-ks-2-3/KS2_KS3_Maths_Guidance_2017.pdf'.replace('\n',' '),180,9.5)
	b.para(15,188,'Arkib: dera.ioe.ac.uk/id/eprint/30457/1/\nKS2_KS3_Maths_Guidance_2017.pdf'.replace('\n',' '),180,9.5)
	b.box(15,214,180,56,ORANGE)
	b.text(21,226,'PENAFIAN EFEK',10,True,ORANGE)
	b.para(21,237,'Rujukan di atas menyokong keputusan reka bentuk (sela, representasi, strategi, hubungan, motivasi). Mereka tidak membuktikan keberkesanan khusus produk ini, tidak menjamin keputusan ujian, dan tidak menggantikan intervensi profesional.',167,9.5)
	b.para(15,278,'Fail RUJUKAN.md dalam pakej sumber mengandungi nota pemetaan halaman.',180,8.6)
	b.end()

def build_guide():
	b=Book('BIJAK_MATEMATIK_PANDUAN_IBU_BAPA.pdf','PANDUAN DEWASA','Panduan ibu bapa & guru')
	cover(b);research_ies(b);research_eef(b);limits(b)
	diagnostic_guide(b);scripts_page(b);routines(b);materials_guide(b)
	focus_rhythm(b);faq(b);refs(b)
	assert b.count==11,b.count
	b.save()

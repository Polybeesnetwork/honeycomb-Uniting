#!/usr/bin/env python3
"""BIJAK MATEMATIK — Edisi Khas Transisi ke Tahun 1.
Pupil Activity Book content: front matter + Unit A (pre-number skills).
Colony 11 — Mission COL-11-BIJAK-FIRSTSTEP-001. All content newly authored."""
from prod_engine import (MM, W, H, BLUE, ORANGE, GREEN, PURPLE, YELLOW, NAVY, GRAY,
                         white, ITEMS, reg, Book)
from content_helpers import (obj_grid, dots_grid, trace_num, write_nums,
                             write_lines, match_row, qbox, choice_row,
                             section_banner, mascot, OBJ_SVG)
from reportlab.lib.utils import simpleSplit

# ---------------------------------------------------------------- cover
def cover(b):
    from prod_engine import PAGES_LOG
    b.count += 1
    b.page = b.count
    PAGES_LOG.append({'file': b.name, 'page': b.page,
                      'title': 'BIJAK MATEMATIK — COVER', 'kind': 'cover'})
    # top band
    b.c.setFillColor(b.color(BLUE))
    b.c.rect(0, H - 90 * MM, W, 90 * MM, stroke=0, fill=1)
    b.c.setFillColor(b.color(ORANGE))
    b.c.rect(0, H - 96 * MM, W, 6 * MM, stroke=0, fill=1)
    b.text(15, 34, 'BIJAK', 40, True, YELLOW)
    b.text(15, 58, 'MATEMATIK', 40, True, white)
    b.text(15, 78, 'Edisi Khas Transisi ke Tahun 1', 13, True, YELLOW)
    # mascot
    b.svg('lebah_bijak.svg', 120, 100, 78, 78)
    b.text(120, 186, 'Lebah Bijak membantu', 10, True, NAVY, 'center')
    b.text(120, 198, 'kamu belajar kira!', 10, True, NAVY, 'center')
    b.box(15, 208, 180, 30, ORANGE)
    b.text(20, 220, 'Langkah Pertama Menuju Alam', 11, True, white)
    b.text(20, 230, 'Persekolahan', 11, True, white)
    # four stage tags
    for i, (word, col) in enumerate([('JOM FAHAM', BLUE), ('JOM KIRA', ORANGE),
                                     ('JOM CUBA', PURPLE), ('JOM KUASAI', GREEN)]):
        b.box(15 + i * 46, 254, 42, 14, col)
        b.text(36 + i * 46, 263, word, 9.5, True, white, 'center')
    b.text(15, 272, 'Untuk kanak-kanak 6–7 tahun • Buku aktiviti', 9, False, GRAY)
    b.text(15, 279, 'Hebat! Selesai satu aktiviti, dapatkan ★ Bijak.',
           8.5, False, GRAY)
    b.c.showPage()

def welcome(b):
    b.start('Selamat datang, kawan!', 'Buku ini untuk kamu yang akan masuk Tahun 1. Mari belajar matematik sambil bermain.',
            'JOM FAHAM', BLUE, kind='front')
    mascot(b, 15, 56, 40, 40, note='Hai! Saya Lebah Bijak.')
    b.para(15, 112, 'Dalam buku ini, kamu akan:', 180, 11, NAVY)
    for i, txt in enumerate([
        'Kira benda di sekeliling kamu.',
        'Belajar nombor 1 hingga 20.',
        'Belajar tambah dan tolak dengan gambar.',
        'Mengenali bentuk dan kedudukan.',
        'Bermain sambil belajar!']):
        b.text(22, 122 + i * 13, '●', 10, True, ORANGE)
        b.text(28, 122 + i * 13, txt, 10.5, False, NAVY)
    b.box(15, 200, 180, 62, GREEN, tint=True)
    b.text(20, 210, 'BAGAIMANA GUNA BUKU INI', 9, True, GREEN)
    b.para(20, 219, '1. Baca arahan dengan teliti. Jika belum faham, tanya orang dewasa.',
           170, 9.3, NAVY)
    b.para(20, 231, '2. Gunakan pensel. Jika tersilap, hapus dan cuba semula.',
           170, 9.3, NAVY)
    b.para(20, 243, '3. Selesaikan satu aktiviti pada satu masa.',
           170, 9.3, NAVY)
    b.para(20, 255, '4. Tandakan ★ apabila kamu selesai. Kamu hebat!',
           170, 9.3, NAVY)
    b.finish()

def tracker_intro(b):
    b.start('Penjejak Bijak saya', 'Setiap kali selesai satu unit, tampal atau warna satu ★. Kamu semakin hampir ke Tahun 1!',
            'JOM FAHAM', PURPLE, kind='front')
    mascot(b, 15, 62, 36, 36, note='Kerja bagus!')
    b.text(15, 110, 'UNIT-UNIT DI DALAM BUKU INI', 10, True, PURPLE)
    units = [('A', 'Kemahiran sebelum nombor'), ('B', 'Nombor 1 hingga 10'),
             ('C', 'Nombor 11 hingga 20'), ('D', 'Tambah dan tolak'),
             ('E', 'Matematik seharian')]
    for i, (code, name) in enumerate(units):
        b.box(15, 124 + i * 24, 30, 20, BLUE if i % 2 == 0 else ORANGE)
        b.text(30, 133 + i * 24, code, 12, True, white, 'center')
        b.text(50, 133 + i * 24, name, 10.5, False, NAVY)
        for s in range(3):
            b.star(180, 131 + i * 24 + s * 7, 3, YELLOW)
    b.box(15, 258, 180, 26, GREEN, tint=True)
    b.text(20, 272, 'Apabila semua ★ berwarna: "Saya sedia untuk Tahun 1!"', 9, True, GREEN)
    b.finish()

# ------------------------------------------------- UNIT A: pre-number
def unit_a_intro(b):
    b.start('Unit A • Kemahiran sebelum nombor', 'Sebelum kira nombor, kita belajar cara melihat, mengelas dan menyusun. Jom!',
            'JOM FAHAM', BLUE, kind='unit')
    mascot(b, 130, 60, 46, 46)
    b.box(15, 130, 86, 60, ORANGE, tint=True)
    b.text(20, 140, 'APA YANG KITA ADALAH', 9, True, ORANGE)
    b.para(20, 148, 'Dalam Unit A, kamu akan:', 76, 9.3, NAVY)
    for i, t in enumerate(['Padankan benda yang sama.', 'Asingkan benda mengikut warna dan saiz.',
                           'Cari perbezaan dan persamaan.', 'Membuat corak mudah.']):
        b.text(24, 160 + i * 12, '•', 9, True, ORANGE)
        b.text(29, 160 + i * 12, t, 9, False, NAVY)
    b.box(111, 130, 84, 60, GREEN, tint=True)
    b.text(116, 140, 'PERASAN SEMUA', 9, True, GREEN)
    b.para(116, 148, 'Aktiviti ini tiada jawapan betul atau salah. Fokus kepada melihat dengan teliti. Seronok dan sabar adalah kunci!',
           74, 9, NAVY)
    b.finish()

def a_matching(b):
    b.start('Padankan benda yang sama', 'Carilah benda di sebelah kanan yang sama dengan benda di sebelah kiri. Sambungkan dengan garisan.',
            'JOM FAHAM', BLUE, kind='lesson')
    b.objective_line('Padankan objek yang mempunyai ciri yang sama.')
    left = [('epal', 'epal'), ('bola', 'bola'), ('buku', 'buku'), ('pensel', 'pensel')]
    right = [('epal', 'epal'), ('pensel', 'pensel'), ('bola', 'bola'), ('buku', 'buku')]
    match_row(b, 15, 58, 180, left, right, row_h=27)
    b.para(15, 162, 'Tiga lagi padanan untuk kamu.', 180, 10, NAVY, True)
    left2 = [('epal', 'epal'), ('bola', 'bola'), ('buku', 'buku')]
    right2 = [('epal', 'epal'), ('buku', 'buku'), ('bola', 'bola')]
    match_row(b, 15, 178, 180, left2, right2, row_h=25)
    reg('A1-01', 'Padankan objek serupa', 'A1 Mencari kesamaan', 'Basic',
        'Padankan setiap benda di kiri dengan benda sama di kanan.',
        'epal–epal, bola–bola, buku–buku, pensel–pensel (7 padanan)',
        book=b.name, page=b.page)
    b.help_box(15, 244, 180, 'Jika tidak pasti, lihat warna dan bentuk. Dua benda yang sama akan kelihatan sama sahaja.')
    b.check_strip(15, 266, 180, 'Selesai? Tandakan ★ di penjejak.')
    b.finish()

def a_matching2(b):
    b.start('Padankan corak dan bentuk', 'Sambungkan bentuk di kiri dengan bentuk yang sama bentuk di kanan.',
            'JOM FAHAM', BLUE, kind='practice')
    shapes_l = ['△', '○', '□', '☆']
    shapes_r = ['○', '☆', '△', '□']
    for i in range(4):
        y = 64 + i * 30
        b.text(25, y + 10, shapes_l[i], 16, True, BLUE, 'center')
        b.c.setStrokeColor(b.color(GRAY)); b.c.setLineWidth(.4); b.c.setDash(2, 2)
        b.c.line(45 * MM, H - (y + 11) * MM, 150 * MM, H - (y + 11) * MM)
        b.c.setDash()
        b.text(165, y + 10, shapes_r[i], 16, True, ORANGE, 'center')
    # color matching
    b.para(15, 196, 'Padankan warna yang sama.', 180, 10.5, NAVY, True)
    colors_l = [('#D97119', 'oren'), ('#087D63', 'hijau'), ('#1768AD', 'biru')]
    colors_r = [('#1768AD', 'biru'), ('#D97119', 'oren'), ('#087D63', 'hijau')]
    for i in range(3):
        y = 214 + i * 26
        b.c.setFillColor(b.color(colors_l[i][0]))
        b.c.circle(25 * MM, H - (y + 10) * MM, 7 * MM, stroke=1, fill=1)
        b.c.setStrokeColor(b.color(GRAY)); b.c.setLineWidth(.4); b.c.setDash(2, 2)
        b.c.line(40 * MM, H - (y + 10) * MM, 145 * MM, H - (y + 10) * MM)
        b.c.setDash()
        b.c.setFillColor(b.color(colors_r[i][0]))
        b.c.circle(155 * MM, H - (y + 10) * MM, 7 * MM, stroke=1, fill=1)
    reg('A1-02', 'Padankan bentuk dan warna', 'A1 Mencari kesamaan', 'Basic',
        'Sambungkan bentuk sama dengan bentuk sama; padankan warna sama.',
        '△–△, ○–○, □–□, ☆–☆; oren–oren, hijau–hijau, biru–biru',
        book=b.name, page=b.page)
    b.finish()

def a_sorting(b):
    b.start('Asingkan mengikut warna', 'Asingkan benda-benda ini kepada dua kumpulan: warna merah dan warna biru.',
            'JOM FAHAM', ORANGE, kind='lesson')
    b.objective_line('Mengasingkan objek mengikut satu ciri (warna).')
    b.box(15, 60, 88, 120, ORANGE, tint=True)
    b.text(20, 70, 'KUMPULAN MERAH', 9.5, True, ORANGE)
    red_pos = [(24, 84), (62, 84), (24, 110), (62, 110), (24, 136), (45, 148)]
    import random
    rnd = random.Random(7)
    for (x, y) in red_pos:
        b.c.setFillColor(b.color('#D9534F'))
        b.c.setStrokeColor(b.color(NAVY)); b.c.setLineWidth(.4)
        b.c.circle(x * MM, H - y * MM, 6 * MM, stroke=1, fill=1)
    b.box(107, 60, 88, 120, BLUE, tint=True)
    b.text(112, 70, 'KUMPULAN BIRU', 9.5, True, BLUE)
    blue_pos = [(116, 84), (154, 84), (116, 110), (154, 110), (116, 136), (135, 148)]
    for (x, y) in blue_pos:
        b.c.setFillColor(b.color(BLUE))
        b.c.setStrokeColor(b.color(NAVY)); b.c.setLineWidth(.4)
        b.c.circle(x * MM, H - y * MM, 6 * MM, stroke=1, fill=1)
    b.para(15, 200, 'Sekarang, kamu pula. Asingkan benda di bawah kepada kumpulan biji dan kumpulan buah.', 180, 10, NAVY, True)
    obj_grid(b, 25, 214, 10, 5, gap_x=18, gap_y=16, size=11,
             names=['epal', 'bola', 'epal', 'bola', 'epal',
                    'bola', 'epal', 'bola', 'epal', 'bola'])
    
    b.text(15, 272, 'Bijian □□□□□', 9, True, GREEN)
    b.text(107, 272, 'Buah □□□□□', 9, True, GREEN)
    reg('A2-01', 'Mengasingkan mengikut warna', 'A2 Pengasingan', 'Basic',
        'Asingkan bulatan merah dan biru kepada dua kumpulan.',
        '6 bulatan merah dalam kumpulan merah; 6 bulatan biru dalam kumpulan biru',
        book=b.name, page=b.page)
    reg('A2-02', 'Mengasingkan mengikut jenis', 'A2 Pengasingan', 'Basic',
        'Asingkan epal dan bola kepada kumpulan biji dan buah (5 epal, 5 bola).',
        '5 epal dalam kumpulan buah; 5 bola dalam kumpulan biji',
        book=b.name, page=b.page, status='PARTIAL')
    b.help_box(15, 280 - 8, 180, 'Lihat warna dahulu. Letak satu benda ke dalam kumpulan yang tepat sebelum pergi ke benda seterusnya.')
    b.finish()

def a_sorting2(b):
    b.start('Asingkan mengikut saiz', 'Asingkan bentuk-bentuk ini kepada kumpulan BESAR dan kumpulan KECIL.',
            'JOM FAHAM', ORANGE, kind='practice')
    b.objective_line('Mengasingkan objek mengikut saiz (besar/kecil).')
    b.box(15, 60, 88, 150, GREEN, tint=True)
    b.text(20, 70, 'BENTUK BESAR', 9.5, True, GREEN)
    for (kind, x, y, s) in [('square', 30, 100, 22), ('circle', 68, 100, 22),
                            ('triangle', 30, 150, 22), ('star', 68, 150, 22)]:
        b.shape(kind, x, y, s, GREEN)
    b.box(107, 60, 88, 150, PURPLE, tint=True)
    b.text(112, 70, 'BENTUK KECIL', 9.5, True, PURPLE)
    for (kind, x, y, s) in [('square', 122, 100, 12), ('circle', 150, 100, 12),
                            ('triangle', 122, 150, 12), ('star', 150, 150, 12)]:
        b.shape(kind, x, y, s, PURPLE)
    b.para(15, 222, 'Lilitkan bulatan di sekeliling bentuk besar. Ketatakan bentuk kecil dengan tanda silang.', 180, 10, NAVY)
    for (x, y, s, big) in [(30, 100, 22, True), (68, 100, 22, True),
                           (30, 150, 22, True), (68, 150, 22, True),
                           (122, 100, 12, False), (150, 100, 12, False),
                           (122, 150, 12, False), (150, 150, 12, False)]:
        b.c.setStrokeColor(b.color(GREEN if big else PURPLE))
        b.c.setLineWidth(1.4)
        if big:
            b.c.circle(x * MM, H - y * MM, (s / 2 + 4) * MM, stroke=1, fill=0)
        else:
            b.c.line((x - s / 2 - 2) * MM, H - (y - s / 2 - 2) * MM,
                     (x + s / 2 + 2) * MM, H - (y + s / 2 + 2) * MM)
            b.c.line((x - s / 2 - 2) * MM, H - (y + s / 2 + 2) * MM,
                     (x + s / 2 + 2) * MM, H - (y - s / 2 - 2) * MM)
    reg('A2-03', 'Mengasingkan dan menandakan saiz', 'A2 Pengasingan', 'Basic',
        'Asingkan bentuk besar dan kecil; lilit bulatan pada besar, tanda silang pada kecil.',
        '4 bentuk besar dililit bulatan; 4 bentuk kecil ditandakan silang',
        book=b.name, page=b.page)
    b.check_strip(15, 268, 180, 'Selesai? Tandakan ★ di penjejak.')
    b.finish()

def a_classify(b):
    b.start('Yang mana satu tidak sama?', 'Lihat setiap baris. Cari satu benda yang berbeza daripada yang lain. tandakan padanya.',
            'JOM FAHAM', PURPLE, kind='lesson')
    b.objective_line('Mengelaskan objek dan mengenal pasti yang tidak sekumpulan.')
    rows = [
        ([('epal', ''), ('epal', ''), ('bola', ''), ('epal', '')], '4 epal dan 1 bola'),
        ([('bola', ''), ('bola', ''), ('buku', ''), ('bola', '')], '3 bola dan 1 buku'),
        ([('pensel', ''), ('epal', ''), ('epal', ''), ('epal', '')], '3 epal dan 1 pensel'),
    ]
    for i, (items, hint) in enumerate(rows):
        y = 66 + i * 34
        b.text(15, y, f'{i+1}.', 11, True, PURPLE)
        for j, (nm, _) in enumerate(items):
            b.svg(OBJ_SVG[nm], 30 + j * 42, y - 4, 18, 18)
        b.text(15, y + 20, 'Beza: ' + hint, 8.5, False, GRAY)
    b.para(15, 196, 'Cuba pula dengan bentuk. Lingkarkan benda yang berbeza.', 180, 10, NAVY, True)
    shapes = ['○', '○', '△', '○', '□', '□', '☆', '□', '○', '○', '○', '△']
    for j, sh in enumerate(shapes):
        col, row = j % 4, j // 4
        x, y = 30 + col * 45, 196 + row * 26
        b.text(x, y + 8, sh, 15, True, BLUE if sh != '△' else ORANGE, 'center')
    reg('A3-01', 'Mengenali kumpulan yang sama', 'A3 Pengelasan', 'Basic',
        'Kenal pasti objek yang berbeza dalam setiap baris (bola, buku, pensel).',
        'Baris 1: bola; Baris 2: buku; Baris 3: pensel; Baris 4 (bentuk): dua segitiga (△) berbeza daripada bulatan',
        book=b.name, page=b.page)
    b.tip(15, 252, 180, 'Lihat berapa banyak setiap benda. Yang kuantitinya berbeza itulah yang berbeza.',
          PURPLE, 'BIJAK NAK COUNTET')
    b.finish()

def a_patterns(b):
    b.start('Corak yang berulang', 'Corak mengikut turutan. Ikut corak dan lengkapkan tempat kosong.',
            'JOM FAHAM', GREEN, kind='lesson')
    b.objective_line('Menyelesaikan dan melanjutkan corak berulang.')
    b.text(15, 62, '1. ○ △ ○ △ ○ ____', 12, True, NAVY)
    b.text(15, 78, '2. □ □ △ □ □ ____', 12, True, NAVY)
    b.text(15, 94, '3. ★ ○ ★ ○ ★ ____', 12, True, NAVY)
    for i, ans in enumerate(['△', '△', '○']):
        b.box(95, 60 + i * 16, 30, 14, GREEN, tint=False, dash=True)
        b.text(110, 67 + i * 16, ans, 10, True, GREEN, 'center')
    b.para(15, 128, 'Ikut corak warna di bawah. Warnakan mengikut turutan.', 180, 10, NAVY, True)
    pat = [('#D97119', '#1768AD'), ('#1768AD', '#D97119'), ('#D97119', '#1768AD'),
           ('#1768AD', '#D97119'), ('#D97119', '#1768AD'), ('#1768AD', None)]
    for j, (c1, c2) in enumerate(pat):
        x = 30 + j * 28
        b.c.setFillColor(b.color(c1)); b.c.setStrokeColor(b.color(NAVY)); b.c.setLineWidth(.4)
        b.c.circle(x * MM, H - 158 * MM, 9 * MM, stroke=1, fill=1)
        if c2:
            b.c.setFillColor(b.color(c2))
            b.c.circle((x + 14) * MM, H - 158 * MM, 9 * MM, stroke=1, fill=1)
        else:
            b.c.setStrokeColor(b.color(GRAY)); b.c.setLineWidth(.5)
            b.c.setDash(2, 2)
            b.c.circle((x + 14) * MM, H - 158 * MM, 9 * MM, stroke=1, fill=0)
            b.c.setDash()
    b.para(15, 182, 'Tulis corak kamu sendiri di bawah. Guru atau ibu bapa boleh membantu.', 180, 10, NAVY)
    write_lines(b, 15, 200, 180, 3)
    reg('A4-01', 'Melengkapkan corak berulang', 'A4 Corak', 'Basic',
        'Lengkapkan corak: ○△○△○__; □□△□□__; ★○★○★__.',
        '△; △; ○. Corak warna: oren, biru, oren, biru, oren, biru.',
        book=b.name, page=b.page)
    reg('A4-02', 'Mencipta corak sendiri', 'A4 Corak', 'Open',
        'Tulis corak sendiri pada garisan.',
        'OPEN — terima sebarang corak berulang yang konsisten',
        book=b.name, page=b.page, status='OPEN-ENDED')
    b.check_strip(15, 276, 180, 'Selesai? Tandakan ★ di penjejak.')
    b.finish()

def a_spatial(b):
    b.start('Kedudukan di mana?', 'Mari belajar perkataan kedudukan: atas, bawah, dalam, luar, sebelah kiri, sebelah kanan.',
            'JOM FAHAM', PURPLE, kind='lesson')
    b.objective_line('Menggunakan bahasa kedudukan untuk menerangkan lokasi.')
    # house with sun above, ball below
    b.box(70, 90, 80, 60, ORANGE, tint=False)
    b.text(110, 108, 'Rumah', 10, True, NAVY, 'center')
    b.c.setFillColor(b.color(YELLOW))
    b.c.setStrokeColor(b.color(NAVY)); b.c.setLineWidth(.6)
    b.c.circle(45 * MM, H - 55 * MM, 12 * MM, stroke=1, fill=1)
    b.text(45, 84, 'Matahari', 8.5, True, NAVY, 'center')
    b.svg('bola.svg', 150, 175, 16, 16)
    b.text(150, 196, 'Bola', 8.5, True, NAVY, 'center')
    b.text(150, 70, 'atas rumah', 8, False, GRAY, 'center')
    b.text(150, 200, 'bawah rumah', 8, False, GRAY, 'center')
    b.para(15, 208, 'Letakkan satu benda di setiap kedudukan.', 180, 10, NAVY, True)
    b.text(25, 224, '1. Atas meja:', 10, False, NAVY)
    b.box(75, 216, 30, 14, GRAY, tint=False, dash=True)
    b.text(25, 240, '2. Dalam kotak:', 10, False, NAVY)
    b.box(75, 232, 30, 14, GRAY, tint=False, dash=True)
    b.text(105, 224, '3. Sebelah kiri:', 10, False, NAVY)
    b.box(155, 216, 30, 14, GRAY, tint=False, dash=True)
    b.text(105, 240, '4. Sebelah kanan:', 10, False, NAVY)
    b.box(155, 232, 30, 14, GRAY, tint=False, dash=True)
    reg('A5-01', 'Menggunakan bahasa kedudukan', 'A5 Kedudukan', 'Basic',
        'Menyumbang objek pada kedudukan yang disebut (atas, bawah, dalam, kiri, kanan, belakang, hadapan).',
        'OPEN — penilaian melalui contoh yang dilukis pada kedudukan betul',
        book=b.name, page=b.page, status='OPEN-ENDED')
    b.tip(15, 278, 180, 'Kedudukan bergantung pada tempat kamu melihat. "Kiri" ialah kiri kamu, bukan kiri buku.',
          PURPLE, 'BIJAK NAK COUNTET')
    b.finish()

def a_review(b):
    b.start('Semakan Unit A', 'Mari semak apa yang telah kita belajar dalam Unit A.',
            'JOM KUASAI', GREEN, kind='review')
    mascot(b, 150, 60, 36, 36, note='Sama-sama!')
    b.text(15, 112, '1. Padankan:', 10.5, True, NAVY)
    b.svg(OBJ_SVG['epal'], 40, 120, 14, 14)
    b.svg(OBJ_SVG['bola'], 40, 145, 14, 14)
    b.svg(OBJ_SVG['epal'], 140, 120, 14, 14)
    b.svg(OBJ_SVG['buku'], 140, 145, 14, 14)
    b.c.setStrokeColor(b.color(GRAY)); b.c.setLineWidth(.4); b.c.setDash(2, 2)
    b.c.line(58 * MM, H - 126 * MM, 135 * MM, H - 126 * MM)
    b.c.line(58 * MM, H - 151 * MM, 135 * MM, H - 151 * MM)
    b.c.setDash()
    b.text(15, 172, '2. Asingkan mengikut warna:', 10.5, True, NAVY)
    for j, col in enumerate(['#D9534F', '#1768AD', '#D9534F', '#1768AD', '#D9534F', '#1768AD']):
        b.c.setFillColor(b.color(col)); b.c.setStrokeColor(b.color(NAVY)); b.c.setLineWidth(.4)
        b.c.circle((25 + j * 14) * MM, H - 196 * MM, 6 * MM, stroke=1, fill=1)
    b.box(110, 186, 30, 20, ORANGE, tint=True)
    b.text(125, 196, 'Merah', 8.5, True, ORANGE, 'center')
    b.box(145, 186, 30, 20, BLUE, tint=True)
    b.text(160, 196, 'Biru', 8.5, True, BLUE, 'center')
    b.text(15, 220, '3. Lengkapkan corak:', 10.5, True, NAVY)
    b.text(25, 238, '○ □ ○ □ ○ ____', 12, True, NAVY)
    b.box(120, 230, 30, 14, GREEN, tint=False, dash=True)
    b.text(135, 237, '□', 10, True, GREEN, 'center')
    reg('AR-01', 'Semakan Unit A — padanan', 'AR Semakan', 'Basic',
        'Padankan epal dengan epal, bola dengan buku (kesalahan sengaja) — jawapan betul: epal–epal, bola–bola.',
        'epal dihubungkan ke epal; bola dihubungkan ke bola',
        book=b.name, page=b.page)
    reg('AR-02', 'Semakan Unit A — corak', 'AR Semakan', 'Basic',
        'Lengkapkan corak ○□○□○____.', '□', book=b.name, page=b.page)
    b.check_strip(15, 268, 180, 'Selesai Unit A? Tandakan ★ di penjejak.')
    b.finish()

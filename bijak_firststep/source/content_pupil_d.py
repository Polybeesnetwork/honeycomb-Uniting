#!/usr/bin/env python3
"""Pupil Book Unit D — Foundational calculation (Colony 11).
Concepts: part-part-whole, number bonds, addition as combining,
subtraction as removing, subtraction as comparing, one-step problems."""
from prod_engine import (MM, W, H, BLUE, ORANGE, GREEN, PURPLE, YELLOW, NAVY, GRAY,
                         white, ITEMS, reg, Book)
from content_helpers import (obj_grid, dots_grid, trace_num, write_nums,
                             write_lines, match_row, qbox, choice_row,
                             section_banner, mascot, OBJ_SVG)

def unit_d_intro(b):
    b.start('Unit D • Tambahan dan tolak', 'Tambah bermaksud gabungkan. Tolak bermaksud ambil atau banding. Mari kira dengan bijak!',
            'JOM FAHAM', BLUE, kind='unit')
    mascot(b, 128, 60, 48, 48)
    b.box(15, 130, 86, 66, ORANGE, tint=True)
    b.text(20, 140, 'APA YANG KITA ADALAH', 9, True, ORANGE)
    b.para(20, 148, 'Dalam Unit D, kamu akan:', 76, 9.3, NAVY)
    for i, t in enumerate(['Belajar nombor gabungan hingga 10.',
                           'Tambah dua kuantiti.', 'Tolak dengan ambil dan banding.',
                           'Selesaikan masalah satu langkah.']):
        b.text(24, 160 + i * 12, '•', 9, True, ORANGE)
        b.text(29, 160 + i * 12, t, 9, False, NAVY)
    b.box(111, 130, 84, 66, GREEN, tint=True)
    b.text(116, 140, 'PERASAN SEMUA', 9, True, GREEN)
    b.para(116, 148, 'Kita tidak hafal sahaja. Kita guna gambar dan objek supaya faham mengapa jawapannya begitu.',
           74, 9, NAVY)
    b.finish()

def d_ppartwhole(b):
    b.start('Bahagi dan gabung semula', 'Satu nombor boleh dipecahkan kepada dua bahagian. Dua bahagian itu boleh digabung semula.',
            'JOM FAHAM', PURPLE, kind='lesson')
    b.objective_line('Memahami hubungan bahagian-bahagian-keseluruhan (part-part-whole).')
    # 5 apples split 2+3
    b.text(15, 62, '5 epal dibahagi kepada dua kumpulan.', 11, True, NAVY)
    obj_grid(b, 20, 74, 2, 2, gap_x=14, gap_y=14, size=12, names=['epal'])
    b.text(62, 88, 'dan', 10, False, GRAY, 'center')
    obj_grid(b, 82, 74, 3, 3, gap_x=14, gap_y=14, size=12, names=['epal'])
    b.text(20, 118, '2', 14, True, ORANGE, 'center')
    b.text(88, 118, '3', 14, True, BLUE, 'center')
    b.text(120, 118, '= 5', 14, True, GREEN, 'center')
    b.para(15, 134, '2 dan 3 ialah bahagian. 5 ialah keseluruhan.', 180, 10, NAVY)
    b.box(15, 148, 180, 34, GREEN, tint=True)
    b.text(20, 158, 'CONTOH KERJA', 8.5, True, GREEN)
    b.para(20, 166, 'Bahagi 5 kepada 4 dan 1:  4 + 1 = 5. Kedua-duanya masih 5 epal.', 170, 9.5, NAVY)
    b.para(15, 194, 'Bahagi 6 kepada dua bahagian. Isi kotak.', 180, 10, NAVY, True)
    b.text(25, 212, '____ + ____ = 6', 12, True, NAVY)
    b.box(60, 200, 30, 22, GRAY, tint=False, dash=True)
    b.box(100, 200, 30, 22, GRAY, tint=False, dash=True)
    b.para(15, 240, '____ + ____ = 6 (cara lain)', 12, True, NAVY)
    b.box(60, 228, 30, 22, GRAY, tint=False, dash=True)
    b.box(100, 228, 30, 22, GRAY, tint=False, dash=True)
    reg('D1-01', 'Konsep bahagian-keseluruhan', 'D1 Part-part-whole', 'Basic',
        '5 = 2 + 3; 5 = 4 + 1; pecahkan 6 kepada dua bahagian (cth. 3+3, 4+2, 5+1).',
        '5=2+3, 5=4+1; 6 boleh 3+3, 4+2, 5+1 atau 1+5, 2+4 (mana-mana dua yang jumlah 6)',
        book=b.name, page=b.page, status='OPEN-ENDED')
    b.tip(15, 268, 180, 'Bahagian yang berbeza boleh menghasilkan keseluruhan yang sama.',
          PURPLE, 'BIJAK NAK COUNTET')
    b.finish()

def d_bonds(b):
    b.start('Nombor gabungan hingga 10', 'Nombor gabungan ialah dua nombor yang menjadi satu nombor. 4 + 6 = 10.',
            'JOM FAHAM', PURPLE, kind='lesson')
    b.objective_line('Mengetahui pasangan nombor yang tambah menjadi 10 (number bonds).')
    # bonds of 10 visual
    for i, (a, bb) in enumerate([(1, 9), (2, 8), (3, 7), (4, 6), (5, 5)]):
        x = 15 + i * 37
        b.ten_frame(x, 60, 34, a, color=BLUE)
        b.text(x + 17, 100, f'{a}', 12, True, BLUE, 'center')
        b.text(x + 24, 100, '+', 12, True, NAVY, 'center')
        b.text(x + 31, 100, f'{bb}', 12, True, ORANGE, 'center')
        b.text(x + 17, 114, '= 10', 11, True, GREEN, 'center')
    b.para(15, 126, 'Nombor gabungan untuk 10:', 180, 10.5, NAVY, True)
    b.box(15, 140, 180, 30, GREEN, tint=True)
    b.text(20, 150, '10 = 1 + 9 = 2 + 8 = 3 + 7 = 4 + 6 = 5 + 5', 10, True, GREEN)
    b.para(15, 180, 'Isi nombor gabungan untuk setiap soalan.', 180, 10, NAVY, True)
    for i, (a, total) in enumerate([(3, 10), (6, 10), (2, 10), (7, 10)]):
        x = 15 + i * 47
        b.text(x, 196, f'{a} + ____ = {total}', 10.5, True, NAVY)
        b.box(x + 60, 190, 26, 20, GRAY, tint=False, dash=True)
    reg('D2-01', 'Nombor gabungan hingga 10', 'D2 Nombor gabungan', 'Basic',
        'Pasangan tambah kepada 10: 1+9, 2+8, 3+7, 4+6, 5+5. Isi: 3+7=10, 6+4=10, 2+8=10, 7+3=10.',
        '1+9, 2+8, 3+7, 4+6, 5+5; jawapan: 7, 4, 8, 3', book=b.name, page=b.page)
    b.help_box(15, 232, 180, 'Jika sukar, guna ten-frame: isi petang yang ada, lihat berapa lagi perlu untuk cukup 10.')
    b.check_strip(15, 266, 180, 'Selesai? Tandakan ★ di penjejak.')
    b.finish()

def d_add_intro(b):
    b.start('Tambah: gabungkan dua kumpulan', 'Tambah bermaksud gabungkan dua kumpulan menjadi satu kumpulan yang lebih besar.',
            'JOM FAHAM', BLUE, kind='lesson')
    b.objective_line('Memahami penambahan sebagai penggabungan dua kuantiti.')
    b.text(15, 62, 'Ada 3 epal. Lebuh 2 epal lagi. Berapa jumlah?', 11, True, NAVY)
    obj_grid(b, 20, 74, 3, 3, gap_x=14, gap_y=14, size=12, names=['epal'])
    b.text(105, 88, '+', 18, True, GREEN, 'center')
    obj_grid(b, 125, 74, 2, 2, gap_x=14, gap_y=14, size=12, names=['epal'])
    b.text(165, 118, '= 5', 16, True, BLUE, 'center')
    b.worked(15, 134, 180, ['Langkah 1: Kira kumpulan pertama: 3.',
                            'Langkah 2: Kira kumpulan kedua: 2.',
                            'Langkah 3: Gabungkan: 3 + 2 = 5.'])
    b.para(15, 184, 'Tulis tambahan untuk setiap soalan. Guna gambar jika perlu.', 180, 10, NAVY, True)
    rows = [(2, 1), (3, 2), (4, 3), (1, 4)]
    for i, (a, bb) in enumerate(rows):
        x = 15 + (i % 2) * 92
        y = 198 + (i // 2) * 34
        obj_grid(b, x, y, a, 4, gap_x=13, gap_y=13, size=11, names=['bola'])
        b.text(x + a * 14 + 4, y + 4, '+', 13, True, GREEN)
        obj_grid(b, x + 62, y, bb, 4, gap_x=13, gap_y=13, size=11, names=['bola'])
        b.box(x + 62 + bb * 14 + 8, y, 30, 22, GRAY, tint=False, dash=True)
    reg('D3-01', 'Tambah sebagai penggabungan', 'D3 Penambahan', 'Basic',
        '3 + 2 = 5; tambah kumpulan kecil: 2+1=3, 3+2=5, 4+3=7, 1+4=5.',
        '5; 3, 5, 7, 5', book=b.name, page=b.page)
    b.tip(15, 266, 180, 'Kira kumpulan pertama, kemudian terus kira kumpulan kedua dari kiraan tadi.',
          BLUE, 'BIJAK NAK COUNTET')
    b.finish()

def d_add_practice(b):
    b.start('Latih tambah hingga 10', 'Selesaikan tambahan ini. Tulis jawapan dalam kotak.',
            'JOM FAHAM', BLUE, kind='practice')
    b.objective_line('Menyelesaikan penambahan dalam julat 1–10.')
    b.worked(15, 60, 180, ['Contoh: 4 + 3',
                           'Kira 4: □□□□',
                           'Tambah 3 lagi: □□□',
                           'Jumlah: 7.  4 + 3 = 7.'])
    rows = [(2, 3), (5, 2), (1, 6), (4, 4), (3, 5), (6, 2), (7, 1), (5, 4)]
    for i, (a, bb) in enumerate(rows):
        x = 15 + (i % 2) * 92
        y = 130 + (i // 2) * 30
        b.text(x, y, f'{a} + {bb} =', 11, True, NAVY)
        b.box(x + 52, y - 4, 30, 22, GRAY, tint=False, dash=True)
    reg('D3-02', 'Penambahan dalam 1–10', 'D3 Penambahan', 'Basic',
        'Selesaikan 2+3, 5+2, 1+6, 4+4, 3+5, 6+2, 7+1, 5+4.',
        '5, 7, 7, 8, 8, 8, 8, 9', book=b.name, page=b.page)
    b.help_box(15, 264, 180, 'Guna jari, gambar atau objek sebenar. Apa pun cara, pastikan kiraan tepat.')
    b.check_strip(15, 266, 180, 'Selesai? Tandakan ★ di penjejak.')
    b.finish()

def d_sub_intro(b):
    b.start('Tolak: ambil daripada kumpulan', 'Tolak bermaksud mengambil beberapa benda daripada kumpulan. Baki ialah jawapan.',
            'JOM FAHAM', ORANGE, kind='lesson')
    b.objective_line('Memahami penolakan sebagai pengambilan daripada satu kuantiti.')
    b.text(15, 62, 'Ada 5 epal. Ambil 2 epal. Berapa baki?', 11, True, NAVY)
    obj_grid(b, 20, 74, 5, 5, gap_x=14, gap_y=14, size=12, names=['epal'])
    b.text(100, 88, '− 2', 16, True, ORANGE, 'center')
    b.box(130, 74, 46, 34, GREEN, tint=True)
    b.text(153, 100, 'baki', 9, True, GREEN, 'center')
    b.text(153, 92, '= 3', 18, True, BLUE, 'center')
    b.worked(15, 134, 180, ['Langkah 1: Kira semua epal: 5.',
                            'Langkah 2: Ambil 2 epal keluar.',
                            'Langkah 3: Kira baki: 5 − 2 = 3.'])
    b.para(15, 184, 'Selesaikan tolak ini.', 180, 10, NAVY, True)
    rows = [(6, 2), (5, 3), (8, 4), (7, 1)]
    for i, (a, bb) in enumerate(rows):
        x = 15 + (i % 2) * 92
        y = 198 + (i // 2) * 34
        b.text(x, y, f'{a} − {bb} =', 11, True, NAVY)
        b.box(x + 52, y - 4, 30, 22, GRAY, tint=False, dash=True)
    reg('D4-01', 'Tolak sebagai pengambilan', 'D4 Penolakan', 'Basic',
        '5 − 2 = 3; selesaikan 6−2, 5−3, 8−4, 7−1.',
        '3; 4, 2, 4, 6', book=b.name, page=b.page)
    b.tip(15, 266, 180, 'Tolak bermaksud "ambil keluar". Kira yang tinggal, bukan yang diambil.',
          ORANGE, 'BIJAK NAK COUNTET')
    b.finish()

def d_sub_practice(b):
    b.start('Latih tolak hingga 10', 'Selesaikan penolakan ini. Tulis jawapan dalam kotak.',
            'JOM FAHAM', ORANGE, kind='practice')
    b.objective_line('Menyelesaikan penolakan dalam julat 1–10.')
    b.worked(15, 60, 180, ['Contoh: 9 − 4',
                           'Kira semua: □□□□□□□□□ (9)',
                           'Hapus 4: □□□□',
                           'Baki: 5.  9 − 4 = 5.'])
    rows = [(8, 3), (7, 2), (10, 6), (6, 4), (9, 5), (10, 2), (8, 6), (5, 1)]
    for i, (a, bb) in enumerate(rows):
        x = 15 + (i % 2) * 92
        y = 130 + (i // 2) * 30
        b.text(x, y, f'{a} − {bb} =', 11, True, NAVY)
        b.box(x + 52, y - 4, 30, 22, GRAY, tint=False, dash=True)
    reg('D4-02', 'Penolakan dalam 1–10', 'D4 Penolakan', 'Basic',
        'Selesaikan 8−3, 7−2, 10−6, 6−4, 9−5, 10−2, 8−6, 5−1.',
        '5, 5, 4, 2, 4, 8, 2, 4', book=b.name, page=b.page)
    b.help_box(15, 264, 180, 'Jika nombor besar, kira dari belakang: 10, 9, 8… sambil menghapus benda.')
    b.check_strip(15, 266, 180, 'Selesai? Tandakan ★ di penjejak.')
    b.finish()

def d_sub_compare(b):
    b.start('Tolak: bandingkan dua kumpulan', 'Tolak juga bermaksud mencari beza antara dua kumpulan. Lebih banyak berapa?',
            'JOM FAHAM', GREEN, kind='lesson')
    b.objective_line('Memahami penolakan sebagai perbezaan antara dua kuantiti.')
    b.text(15, 62, 'Kucing ada 7 ekor. Anjing ada 3 ekor. Berapa lebih banyak kucing?', 11, True, NAVY)
    obj_grid(b, 20, 74, 7, 4, gap_x=13, gap_y=13, size=11, names=['epal'])
    b.text(120, 88, '−', 18, True, GREEN, 'center')
    obj_grid(b, 145, 74, 3, 3, gap_x=13, gap_y=13, size=11, names=['bola'])
    b.text(15, 118, 'Beza: 7 − 3 = 4. Kucing ada 4 lebih banyak.', 11, True, NAVY)
    b.worked(15, 134, 180, ['Langkah 1: Kira kumpulan besar: 7.',
                            'Langkah 2: Kira kumpulan kecil: 3.',
                            'Langkah 3: Cari beza: 7 − 3 = 4.'])
    b.para(15, 184, 'Cari beza untuk setiap pasangan.', 180, 10, NAVY, True)
    pairs = [(6, 2), (9, 4), (8, 5), (10, 7)]
    for i, (a, bb) in enumerate(pairs):
        x = 15 + (i % 2) * 92
        y = 198 + (i // 2) * 34
        b.text(x, y, f'{a} − {bb} =', 11, True, NAVY)
        b.box(x + 52, y - 4, 30, 22, GRAY, tint=False, dash=True)
    reg('D5-01', 'Tolak sebagai perbezaan', 'D5 Penolakan', 'Basic',
        '7 − 3 = 4 (beza); cari beza: 6−2=4, 9−4=5, 8−5=3, 10−7=3.',
        '4; 4, 5, 3, 3', book=b.name, page=b.page)
    b.tip(15, 266, 180, 'Beza bermaksud "berapa lebih" antara dua kumpulan. Tolak kumpulan kecil daripada kumpulan besar.',
          GREEN, 'BIJAK NAK COUNTET')
    b.finish()

def d_word_problems(b):
    b.start('Masalah satu langkah', 'Selesaikan masalah ini. Baca dengan teliti dahulu.',
            'JOM FAHAM', BLUE, kind='lesson')
    b.objective_line('Menyelesaikan masalah satu langkah tambah atau tolak.')
    b.worked(15, 60, 180, ['Contoh: Ali ada 4 biji gula-gula. Ibu beri 3 lagi.',
                           'Soalan: tambah atau tolak? → tambah.',
                           '4 + 3 = 7. Ali ada 7 biji gula-gula.'])
    probs = [
        ('1. Siti ada 5 epal. Dia makan 2. Berapa epal tinggal?', '5 − 2 = 3'),
        ('2. Terdapat 3 orang budak di sebelah kiri. 2 orang lagi datang. Berapa orang semuanya?', '3 + 2 = 5'),
        ('3. Di dalam beg ada 8 buku. 3 buku dikeluarkan. Berapa buku tinggal?', '8 − 3 = 5'),
        ('4. Enam orang kanak-kanak berbaris. 1 orang lagi menyertai. Berapa orang?', '6 + 1 = 7'),
    ]
    for i, (text, ans) in enumerate(probs):
        y = 128 + i * 29
        b.box(15, y, 180, 26, BLUE if i % 2 == 0 else ORANGE, tint=True)
        b.para(19, y + 8, text, 172, 9.3, NAVY)
        b.text(175, y + 17, '→', 10, True, GRAY, 'right')
    reg('D6-01', 'Masalah satu langkah tambah', 'D6 Masalah', 'Basic',
        'Selesaikan masalah satu langkah: 3+2=5, 6+1=7.',
        '5 orang; 7 orang', book=b.name, page=b.page)
    reg('D6-02', 'Masalah satu langkah tolak', 'D6 Masalah', 'Basic',
        'Selesaikan masalah satu langkah: 5−2=3, 8−3=5.',
        '3 epal; 5 buku', book=b.name, page=b.page)
    b.help_box(15, 264, 180, 'Baca dua kali. cari perkataan "tambah" (gabung) atau "tolak" (ambil/tinggal).')
    b.check_strip(15, 266, 180, 'Selesai? Tandakan ★ di penjejak.')
    b.finish()

def d_add_within20(b):
    b.start('Tambah hingga 20', 'Tambah dua nombor hingga 20. Gunakan nombor gabungan 10 jika boleh.',
            'JOM FAHAM', BLUE, kind='lesson')
    b.objective_line('Menyelesaikan penambahan dalam julat 1–20 menggunakan strategi nombor gabungan.')
    b.worked(15, 60, 180, ['Contoh: 8 + 5',
                           'Pecahkan 5 kepada 2 + 3.',
                           '8 + 2 = 10 (nombor gabungan!).',
                           '10 + 3 = 13.  8 + 5 = 13.'])
    rows = [(8, 5), (9, 4), (7, 6), (11, 3), (12, 5), (10, 9), (6, 8), (13, 4)]
    for i, (a, bb) in enumerate(rows):
        x = 15 + (i % 2) * 92
        y = 130 + (i // 2) * 30
        b.text(x, y, f'{a} + {bb} =', 11, True, NAVY)
        b.box(x + 52, y - 4, 30, 22, GRAY, tint=False, dash=True)
    reg('D7-01', 'Penambahan hingga 20', 'D7 Penambahan', 'Intermediate',
        'Selesaikan: 8+5=13, 9+4=13, 7+6=13, 11+3=14, 12+5=17, 10+9=19, 6+8=14, 13+4=17.',
        '13, 13, 13, 14, 17, 19, 14, 17', book=b.name, page=b.page)
    b.tip(15, 266, 180, 'Cari pasangan yang cukup 10 dahulu. 8 + 2 = 10, kemudian tambah baki.',
          BLUE, 'BIJAK NAK COUNTET')
    b.finish()

def d_sub_within20(b):
    b.start('Tolak hingga 20', 'Tolak dua nombor hingga 20. Jika nombor besar, kira secara berperingkat.',
            'JOM FAHAM', ORANGE, kind='lesson')
    b.objective_line('Menyelesaikan penolakan dalam julat 1–20.')
    b.worked(15, 60, 180, ['Contoh: 15 − 6',
                           'Pecahkan: tolak ke 10 dahulu.',
                           '15 − 5 = 10.',
                           '10 − 1 = 9.  15 − 6 = 9.'])
    rows = [(15, 6), (18, 8), (14, 5), (12, 4), (20, 7), (16, 9), (17, 8), (11, 3)]
    for i, (a, bb) in enumerate(rows):
        x = 15 + (i % 2) * 92
        y = 130 + (i // 2) * 30
        b.text(x, y, f'{a} − {bb} =', 11, True, NAVY)
        b.box(x + 52, y - 4, 30, 22, GRAY, tint=False, dash=True)
    reg('D8-01', 'Penolakan hingga 20', 'D8 Penolakan', 'Intermediate',
        'Selesaikan: 15−6=9, 18−8=10, 14−5=9, 12−4=8, 20−7=13, 16−9=7, 17−8=9, 11−3=8.',
        '9, 10, 9, 8, 13, 7, 9, 8', book=b.name, page=b.page)
    b.help_box(15, 264, 180, 'Guna nombor garis: gerak ke belakang. Atau tolak ke 10 dahulu, kemudian baki.')
    b.check_strip(15, 266, 180, 'Selesai? Tandakan ★ di penjejak.')
    b.finish()

def d_review(b):
    b.start('Semakan Unit D', 'Mari semak tambah dan tolak yang telah kita belajar.',
            'JOM KUASAI', GREEN, kind='review')
    mascot(b, 152, 58, 34, 34, note='Kira dengan bijak!')
    rows = [('4 + 5', '9'), ('10 − 3', '7'), ('6 + 7', '13'), ('12 − 5', '7'),
            ('2 + 9', '11'), ('15 − 8', '7')]
    for i, (q, a) in enumerate(rows):
        x = 15 + (i % 3) * 62
        y = 118 + (i // 3) * 44
        b.box(x, y, 58, 34, BLUE if i % 2 == 0 else ORANGE, tint=True)
        b.text(x + 29, y + 18, q, 13, True, NAVY, 'center')
        b.text(x + 29, y + 8, '= ____', 9, True, GRAY, 'center')
    b.text(15, 206, 'Selesaikan dua masalah ini.', 10.5, True, NAVY)
    b.box(15, 218, 180, 30, GREEN, tint=True)
    b.para(19, 226, '1. Lima biji marbles di dalam beg. Tiga lagi dimasukkan. Berapa semuanya?', 172, 9.3, NAVY)
    b.box(15, 252, 180, 30, GREEN, tint=True)
    b.para(19, 260, '2. Di tempat main ada 12 orang. 4 orang pulang. Berapa orang tinggal?', 172, 9.3, NAVY)
    reg('DR-01', 'Semakan Unit D — operasi', 'DR Semakan', 'Basic',
        '4+5=9, 10−3=7, 6+7=13, 12−5=7, 2+9=11, 15−8=7.',
        '9, 7, 13, 7, 11, 7', book=b.name, page=b.page)
    reg('DR-02', 'Semakan Unit D — masalah', 'DR Semakan', 'Basic',
        '5+3=8 marbles; 12−4=8 orang tinggal.',
        '8; 8', book=b.name, page=b.page)
    b.check_strip(15, 286 - 6, 180, 'Selesai Unit D? Tandakan ★ di penjejak.')
    b.finish()

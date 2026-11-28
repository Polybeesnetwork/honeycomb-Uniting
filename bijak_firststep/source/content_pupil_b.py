#!/usr/bin/env python3
"""Pupil Book Unit B — Number sense: numbers 1 to 10 (Colony 11)."""
from prod_engine import (MM, W, H, BLUE, ORANGE, GREEN, PURPLE, YELLOW, NAVY, GRAY,
                         white, ITEMS, reg, Book)
from content_helpers import (obj_grid, dots_grid, trace_num, write_nums,
                             write_lines, match_row, qbox, choice_row,
                             section_banner, mascot, OBJ_SVG)

def unit_b_intro(b):
    b.start('Unit B • Nombor 1 hingga 10', 'Nombor berapakah benda-benda ini? Mari kira dan belajar nombor 1 hingga 10.',
            'JOM FAHAM', BLUE, kind='unit')
    mascot(b, 128, 60, 48, 48)
    b.box(15, 130, 86, 66, BLUE, tint=True)
    b.text(20, 140, 'APA YANG KITA ADALAH', 9, True, BLUE)
    b.para(20, 148, 'Dalam Unit B, kamu akan:', 76, 9.3, NAVY)
    for i, t in enumerate(['Mengira benda satu per satu.', 'Membaca dan menulis nombor.',
                           'Mengetahui apa itu sifar.', 'Membandingkan kuantiti: lebih, kurang, sama.']):
        b.text(24, 160 + i * 12, '•', 9, True, BLUE)
        b.text(29, 160 + i * 12, t, 9, False, NAVY)
    b.box(111, 130, 84, 66, GREEN, tint=True)
    b.text(116, 140, 'PERASAN SEMUA', 9, True, GREEN)
    b.para(116, 148, 'Kira dengan perlahan.sentuh setiap benda sambil menyebut nombor. Ini membantu otak kamu belajar.',
           74, 9, NAVY)
    b.finish()

def b_count1(b):
    b.start('Mari kira 1, 2, 3', 'Kira benda di bawah. Tulis nombor yang betul di dalam kotak.',
            'JOM FAHAM', BLUE, kind='lesson')
    b.objective_line('Mengira set objek 1 hingga 5 secara satu-satu (satu-ke-satu).')
    # three groups
    groups = [(3, 'epal', 15, 64), (4, 'bola', 100, 64), (5, 'epal', 15, 130)]
    for n, nm, x, y in groups:
        obj_grid(b, x, y, n, n, gap_x=16, gap_y=16, size=13, names=[nm])
        b.box(x + n * 17 + 6, y, 26, 20, GRAY, tint=False, dash=True)
        b.text(x + n * 17 + 19, y + 7, str(n), 11, True, NAVY, 'center')
    b.para(15, 200, 'Kira lagi kumpulan ini. Tulis nombornya.', 180, 10, NAVY, True)
    obj_grid(b, 20, 216, 5, 5, gap_x=18, gap_y=18, size=13, names=['buku'])
    b.box(20 + 5 * 19 + 6, 216, 26, 20, GRAY, tint=False, dash=True)
    reg('B1-01', 'Mengira set 1–5', 'B1 Mengira', 'Basic',
        'Kira tiga kumpulan (3, 4, 5 epal/bola) dan tulis nombor.',
        '3, 4, 5; kumpulan buku: 5', book=b.name, page=b.page)
    b.tip(15, 246, 180, 'Sentuh setiap benda sambil menyebut: satu, dua, tiga… Jangan laju sangat.',
          BLUE, 'BIJAK NAK COUNTET')
    b.check_strip(15, 266, 180, 'Selesai? Tandakan ★ di penjejak.')
    b.finish()

def b_count2(b):
    b.start('Kira hingga 10', 'Kira benda-benda ini hingga 10. Tulis nombornya.',
            'JOM FAHAM', BLUE, kind='practice')
    b.objective_line('Mengira set objek hingga 10 secara satu-satu.')
    obj_grid(b, 18, 62, 10, 5, gap_x=19, gap_y=19, size=13, names=['epal', 'bola'])
    b.box(18 + 5 * 20 + 8, 62, 26, 20, GRAY, tint=False, dash=True)
    b.text(18 + 5 * 20 + 21, 69, '10', 11, True, NAVY, 'center')
    b.para(15, 120, 'Kira daun-daun di bawah. Tulis nombornya pula.', 180, 10, NAVY, True)
    dots_grid(b, 30, 138, 7, 4, step=11, r=3, color=GREEN)
    b.box(30 + 4 * 12, 138, 26, 20, GRAY, tint=False, dash=True)
    b.text(30 + 4 * 12 + 13, 145, '7', 11, True, NAVY, 'center')
    b.para(15, 186, 'Tulis nombor 1 hingga 10 dalam kotak di bawah, mengikut turutan.', 180, 10, NAVY, True)
    write_nums(b, 18, 196, [1, 2, 3, 4, 5], size=11, gap=12, boxw=28, boxh=26)
    write_nums(b, 18, 228, [6, 7, 8, 9, 10], size=11, gap=12, boxw=28, boxh=26)
    reg('B1-02', 'Mengira set hingga 10', 'B1 Mengira', 'Basic',
        'Kira 10 epal/bola; kira 7 titik; tulis 1–10 mengikut turutan.',
        '10; 7; turutan 1,2,3,4,5,6,7,8,9,10', book=b.name, page=b.page)
    b.finish()

def b_recognize(b):
    b.start('Kenal nombor 1 hingga 5', 'Nombor ini bernama apa? Sama banyakkah benda dengan nombor itu?',
            'JOM FAHAM', ORANGE, kind='lesson')
    b.objective_line('Mengecakan kuantiti dengan numeral 1–5.')
    nums = [(1, 'epal', 15), (2, 'bola', 68), (3, 'epal', 121), (4, 'bola', 15), (5, 'epal', 68)]
    yy = [64, 140]
    for idx, (n, nm, x) in enumerate(nums):
        row = idx // 3
        b.svg(OBJ_SVG[nm], x, yy[row], 13, 13)
        for j in range(n - 1):
            b.svg(OBJ_SVG[nm], x + 17 + j * 17, yy[row], 13, 13)
        b.box(x + n * 17 + 5, yy[row], 24, 18, ORANGE, tint=False)
        b.text(x + n * 17 + 17, yy[row] + 6, str(n), 11, True, NAVY, 'center')
    b.para(15, 205, 'Lingkarkan nombor yang sama dengan kuantiti benda di bawah.', 180, 10, NAVY, True)
    obj_grid(b, 25, 220, 3, 3, gap_x=18, gap_y=18, size=12, names=['buku'])
    b.text(110, 230, 'Pilih nombor:', 9.5, True, NAVY)
    for i, n in enumerate([2, 3, 4, 5]):
        b.box(110 + i * 24, 242, 22, 16, GRAY, tint=False, dash=True)
        b.text(121 + i * 24, 248, str(n), 10, True, NAVY, 'center')
    reg('B2-01', 'Mengecakan kuantiti dengan numeral', 'B2 Mengenal nombor', 'Basic',
        'Kaitkan kuantiti 1–5 dengan numeral yang sama; lingkarkan nombor 3 untuk 3 buku.',
        '1, 2, 3, 4, 5 kaitan betul; lingkaran pada nombor 3',
        book=b.name, page=b.page)
    b.help_box(15, 266, 180, 'Kira dahulu. Kemudian cari nombor yang sama nilainya dengan kiraan kamu.')
    b.finish()

def b_readwrite(b):
    b.start('Baca dan tulis nombor 1 hingga 10', 'Baca nombor di bawah. Kemudian tulis nombor itu dalam kotak.',
            'JOM FAHAM', ORANGE, kind='lesson')
    b.objective_line('Membaca numeral dan menulisnya dengan tepat.')
    b.para(15, 60, 'Baca nombor ini:  7', 11, True, NAVY)
    b.box(15, 76, 40, 26, BLUE, tint=False, dash=True)
    b.text(35, 92, '7', 18, True, NAVY, 'center')
    b.para(15, 118, 'Tulis nombor 7 dalam kotak besar di bawah.', 180, 10, NAVY)
    trace_num(b, 60, 130, 7, size=40)
    b.para(15, 190, 'Tulis nombor-nombor ini dengan cantik:', 180, 10, NAVY, True)
    write_nums(b, 15, 204, [3, 5, 8, 2], size=11, gap=14, boxw=30, boxh=24)
    reg('B3-01', 'Menulis numeral 1–10', 'B3 Menulis nombor', 'Basic',
        'Tulis nombor 7 (untuk latihan) dan nombor 3, 5, 8, 2 dalam kotak.',
        '7; 3, 5, 8, 2 (penilaian penulisan oleh guru/ibu bapa)',
        book=b.name, page=b.page, status='MANUAL REVIEW REQUIRED')
    b.tip(15, 250, 180, 'Tulis nombor dengan arah yang betul: bermula dari atas, turun ke bawah.',
          ORANGE, 'BIJAK NAK COUNTET')
    b.check_strip(15, 266, 180, 'Selesai? Tandakan ★ di penjejak.')
    b.finish()

def b_trace(b):
    b.start('Latih tulis nombor', 'Sambung menulis nombor dengan garisan putus-putus. Kemudian tulis sendiri sekali.',
            'JOM FAHAM', ORANGE, kind='practice')
    b.objective_line('Membentuk numeral 1–10 melalui latihan mengesan.')
    nums = [1, 2, 3, 4, 5]
    for i, n in enumerate(nums):
        x = 15 + i * 37
        trace_num(b, x, 66, n, size=30)
        b.box(x, 110, 34, 34, GRAY, tint=False, dash=True)
    nums2 = [6, 7, 8, 9, 10]
    for i, n in enumerate(nums2):
        x = 15 + i * 37
        trace_num(b, x, 156, n, size=30)
        b.box(x, 200, 34, 34, GRAY, tint=False, dash=True)
    b.para(15, 248, 'Tulis nombor 1 hingga 10 mengikut turutan di bawah.', 180, 10, NAVY, True)
    write_lines(b, 15, 260, 180, 2, gap=10)
    reg('B3-02', 'Latihan mengesan nombor 1–10', 'B3 Menulis nombor', 'Basic',
        'Menyempurnakan penulisan nombor 1–10 melalui pengesanan dan penulisan sendiri.',
        'Penilaian penulisan (MANUAL) — semua nombor 1–10 ditulis',
        book=b.name, page=b.page, status='MANUAL REVIEW REQUIRED')
    b.finish()

def b_onetoone(b):
    b.start('Satu benda, satu nombor', 'Setiap benda mendapat satu nombor. Pasangkan setiap benda dengan nombornya.',
            'JOM FAHAM', GREEN, kind='lesson')
    b.objective_line('Memahami korespondensi satu-ke-satu.')
    b.para(15, 60, 'Kira benda dan sambungkan kepada nombor yang betul.', 180, 10, NAVY)
    items = [('epal', 4, 15, 76), ('bola', 6, 100, 76), ('buku', 3, 15, 160), ('pensel', 5, 100, 160)]
    for nm, n, x, y in items:
        obj_grid(b, x, y, n, min(n, 3), gap_x=16, gap_y=14, size=12, names=[nm])
        b.box(x + (3 if n <= 3 else 4) * 18 + 8, y, 24, 18, GREEN, tint=False)
        b.text(x + (3 if n <= 3 else 4) * 18 + 20, y + 6, str(n), 11, True, NAVY, 'center')
    b.para(15, 232, 'Mengapa satu benda hanya dapat satu nombor?', 180, 10, NAVY, True)
    write_lines(b, 15, 248, 180, 2, gap=10)
    reg('B4-01', 'Korespondensi satu-ke-satu', 'B4 Konsep nombor', 'Basic',
        'Kaitkan set 4, 6, 3, 5 objek dengan nombor yang sama banyak.',
        'epal–4, bola–6, buku–3, pensel–5', book=b.name, page=b.page)
    reg('B4-02', 'Menjelaskan konsep satu-satu', 'B4 Konsep nombor', 'Open',
        'Terangkan mengapa setiap benda mendapat satu nombor sahaja.',
        'OPEN — jawapan seperti: setiap benda dikira sekali, satu nombor untuk satu benda',
        book=b.name, page=b.page, status='OPEN-ENDED')
    b.tip(15, 274, 180, 'Jika kiraan dan nombor tidak sama, kira semula. Setiap benda mesti ada nombornya sendiri.',
          GREEN, 'BIJAK NAK COUNTET')
    b.finish()

def b_zero(b):
    b.start('Nombor istimewa: sifar', 'Sifar bermaksud tiada apa-apa. Kosong!',
            'JOM FAHAM', PURPLE, kind='lesson')
    b.objective_line('Memahami maksud sifar sebagai tiada kuantiti.')
    b.box(15, 62, 86, 70, PURPLE, tint=True)
    b.text(20, 72, 'KOTAK KOSONG', 9.5, True, PURPLE)
    b.para(20, 82, 'Tiada benda di dalam kotak ini. Bilangan benda ialah sifar.', 76, 9.3, NAVY)
    b.big_num(58, 118, 0, 34, PURPLE, 'center')
    b.text(58, 138, 'sifar', 10, True, NAVY, 'center')
    b.box(111, 62, 84, 70, BLUE, tint=True)
    b.text(116, 72, 'KOTAK ADA 3 BENDA', 9.5, True, BLUE)
    obj_grid(b, 118, 82, 3, 3, gap_x=14, gap_y=14, size=12, names=['epal'])
    b.big_num(153, 118, 3, 34, BLUE, 'center')
    b.text(153, 138, 'tiga', 10, True, NAVY, 'center')
    b.para(15, 150, 'Lingkarkan kumpulan yang mempunyai sifar benda.', 180, 10, NAVY, True)
    b.box(15, 164, 40, 30, GRAY, tint=False, dash=True)
    b.text(35, 184, 'tiada', 9, False, GRAY, 'center')
    b.box(65, 164, 40, 30, GRAY, tint=False, dash=True)
    obj_grid(b, 74, 172, 2, 2, gap_x=12, gap_y=12, size=10, names=['bola'])
    b.box(115, 164, 40, 30, GRAY, tint=False, dash=True)
    b.text(135, 184, 'tiada', 9, False, GRAY, 'center')
    reg('B5-01', 'Memahami sifar', 'B5 Sifar', 'Basic',
        'Mengenal pasti kumpulan kosong sebagai sifar; melingkar dua kumpulan kosong.',
        'Dua kumpulan "tiada" (kotak 1 dan 3) dilingkarkan; sifar = 0 benda',
        book=b.name, page=b.page)
    b.tip(15, 214, 180, 'Sifar bukan "tiada nombor". Sifar ialah nombor yang memberitahu tiada benda.',
          PURPLE, 'BIJAK NAK COUNTET')
    b.check_strip(15, 266, 180, 'Selesai? Tandakan ★ di penjejak.')
    b.finish()

def b_compare(b):
    b.start('Lebih, kurang, sama banyak', 'Kira kedua-dua kumpulan. Pilih perkataan yang betul: lebih, kurang, atau sama.',
            'JOM FAHAM', ORANGE, kind='lesson')
    b.objective_line('Membandingkan dua kuantiti menggunakan lebih/kurang/sama.')
    b.para(15, 58, '1.', 11, True, NAVY)
    obj_grid(b, 25, 64, 4, 4, gap_x=14, gap_y=14, size=12, names=['epal'])
    b.para(120, 58, '2.', 11, True, NAVY)
    obj_grid(b, 130, 64, 3, 3, gap_x=14, gap_y=14, size=12, names=['bola'])
    b.text(15, 112, 'Kumpulan 1 ____ kumpulan 2', 10.5, True, NAVY)
    choice_row(b, 15, 124, ['lebih', 'kurang', 'sama'])
    b.para(15, 148, '2.', 11, True, NAVY)
    obj_grid(b, 25, 154, 5, 5, gap_x=14, gap_y=14, size=12, names=['epal'])
    b.para(120, 148, '2.', 11, True, NAVY)
    obj_grid(b, 130, 154, 5, 5, gap_x=14, gap_y=14, size=12, names=['bola'])
    b.text(15, 200, 'Kumpulan 1 ____ kumpulan 2', 10.5, True, NAVY)
    choice_row(b, 15, 212, ['lebih', 'kurang', 'sama'])
    reg('B6-01', 'Membandingkan kuantiti', 'B6 Perbandingan', 'Basic',
        'Pilih lebih/kurang/sama untuk dua pasangan kuantiti (4 vs 3; 5 vs 5).',
        '4 lebih daripada 3 → "lebih"; 5 dan 5 → "sama"',
        book=b.name, page=b.page)
    b.help_box(15, 262, 180, 'Kira setiap kumpulan dengan berhati-hati. Bandingkan nombor kiraan, bukan saiz benda.')
    b.finish()

def b_compare2(b):
    b.start('Nombor lebih besar, nombor lebih kecil', 'Baca dua nombor. Bulatkan nombor yang lebih besar.',
            'JOM FAHAM', ORANGE, kind='practice')
    b.objective_line('Membandingkan nilai numeral (lebih besar/kecil).')
    pairs = [(3, 7), (9, 4), (2, 8), (6, 6), (5, 1), (10, 4)]
    for i, (a, bb) in enumerate(pairs):
        row, col = i // 2, i % 2
        x = 15 + col * 92
        y = 64 + row * 42
        b.box(x, y, 26, 26, GRAY, tint=False)
        b.text(x + 13, y + 9, str(a), 13, True, NAVY, 'center')
        b.text(x + 30, y + 10, 'dan', 9, False, GRAY, 'center')
        b.box(x + 40, y, 26, 26, GRAY, tint=False)
        b.text(x + 53, y + 9, str(bb), 13, True, NAVY, 'center')
        b.text(x + 70, y + 10, '→', 12, True, GRAY)
        b.box(x + 80, y, 26, 26, ORANGE, tint=False, dash=True)
    b.para(15, 214, 'Lengkapkan: tulis nombor yang lebih kecil dalam kotak.', 180, 10, NAVY, True)
    pairs2 = [(8, 5), (2, 9)]
    for i, (a, bb) in enumerate(pairs2):
        x = 15 + i * 92
        b.box(x, 230, 26, 26, GRAY, tint=False)
        b.text(x + 13, 239, str(a), 13, True, NAVY, 'center')
        b.text(x + 30, 240, 'dan', 9, False, GRAY, 'center')
        b.box(x + 40, 230, 26, 26, GRAY, tint=False)
        b.text(x + 53, 239, str(bb), 13, True, NAVY, 'center')
        b.text(x + 70, 240, '→', 12, True, GRAY)
        b.box(x + 80, 230, 26, 26, GREEN, tint=False, dash=True)
    reg('B6-02', 'Membandingkan nilai numeral', 'B6 Perbandingan', 'Basic',
        'Bulatkan nombor lebih besar (3&7→7; 9&4→9; 2&8→8; 6&6→sama; 5&1→5; 10&4→10); tulis yang lebih kecil (8&5→5; 2&9→2; 7&7→7).',
        'Bulatan: 7, 9, 8, 6 atau 6 (sama), 5, 10. Lebih kecil: 5, 2, 7',
        book=b.name, page=b.page)
    b.tip(15, 266, 180, 'Nombor yang lebih jauh dari sifar ialah nombor yang lebih besar.',
          ORANGE, 'BIJAK NAK COUNTET')
    b.finish()

def b_order(b):
    b.start('Susun nombor mengikut turutan', 'Susun nombor-nombor ini dari yang terkecil kepada yang terbesar.',
            'JOM FAHAM', GREEN, kind='lesson')
    b.objective_line('Menyusun nombor 1–10 mengikut turutan menaik.')
    sets = [[4, 2, 7, 1], [9, 3, 6, 5], [8, 1, 10, 4]]
    for i, s in enumerate(sets):
        y = 64 + i * 34
        b.text(15, y, f'{i+1}.', 11, True, GREEN)
        for j, n in enumerate(s):
            b.box(30 + j * 30, y - 4, 24, 20, GRAY, tint=False)
            b.text(42 + j * 30, y + 4, str(n), 11, True, NAVY, 'center')
        for j in range(4):
            b.c.setStrokeColor(b.color(GRAY)); b.c.setLineWidth(.5)
            b.c.setDash(2, 2)
            b.c.line((74 + j * 30) * MM, H - (y + 6) * MM, (94 + j * 30) * MM, H - (y + 6) * MM)
            b.c.setDash()
    b.para(15, 172, 'Susun dari yang terbesar kepada yang terkecil.', 180, 10, NAVY, True)
    b.box(30, 188, 24, 20, GRAY, tint=False)
    b.text(42, 198, '3', 11, True, NAVY, 'center')
    b.box(60, 188, 24, 20, GRAY, tint=False)
    b.text(72, 198, '9', 11, True, NAVY, 'center')
    b.box(90, 188, 24, 20, GRAY, tint=False)
    b.text(102, 198, '5', 11, True, NAVY, 'center')
    reg('B7-01', 'Menyusun nombor mengikut turutan', 'B7 Susunan', 'Basic',
        'Susun 4,2,7,1 → 1,2,4,7; 9,3,6,5 → 3,5,6,9; 8,1,10,4 → 1,4,8,10; 3,9,5 menurun → 9,5,3.',
        '1,2,4,7 | 3,5,6,9 | 1,4,8,10 | 9,5,3', book=b.name, page=b.page)
    b.help_box(15, 236, 180, 'Jika sukar, tulis nombor 1–10 di tepi kertas sebagai rujukan.')
    b.check_strip(15, 266, 180, 'Selesai? Tandakan ★ di penjejak.')
    b.finish()

def b_review(b):
    b.start('Semakan Unit B', 'Mari semak nombor 1 hingga 10 yang telah kita pelajari.',
            'JOM KUASAI', GREEN, kind='review')
    mascot(b, 152, 58, 34, 34, note='Kira dengan yakin!')
    b.text(15, 108, '1. Kira dan tulis nombor:', 10.5, True, NAVY)
    obj_grid(b, 25, 118, 6, 3, gap_x=16, gap_y=16, size=12, names=['epal', 'bola'])
    b.box(110, 118, 26, 20, GRAY, tint=False, dash=True)
    b.text(123, 125, '6', 11, True, NAVY, 'center')
    b.text(15, 158, '2. Nombor berapakah ini? Tulis:', 10.5, True, NAVY)
    b.text(40, 175, '8', 22, True, BLUE, 'center')
    b.box(90, 166, 30, 22, GRAY, tint=False, dash=True)
    b.text(15, 202, '3. Lebih atau kurang? 2 ____ 5', 10.5, True, NAVY)
    choice_row(b, 15, 214, ['lebih', 'kurang'])
    b.text(100, 202, '4. Susun: 4, 1, 3', 10.5, True, NAVY)
    for j, n in enumerate([1, 3, 4]):
        b.box(138 + j * 22, 210, 22, 20, GRAY, tint=False, dash=True)
        b.text(149 + j * 22, 217, str(n), 11, True, NAVY, 'center')
    reg('BR-01', 'Semakan Unit B — mengira', 'BR Semakan', 'Basic',
        'Kira 6 objek; baca nombor 8; bandingkan 2 dan 5; susun 4,1,3.',
        '6; 8; "kurang" (2 kurang daripada 5); 1, 3, 4', book=b.name, page=b.page)
    b.check_strip(15, 268, 180, 'Selesai Unit B? Tandakan ★ di penjejak.')
    b.finish()

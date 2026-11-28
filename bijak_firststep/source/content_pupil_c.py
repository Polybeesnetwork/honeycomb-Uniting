#!/usr/bin/env python3
"""Pupil Book Unit C — Numbers 11 to 20 (Colony 11)."""
from prod_engine import (MM, W, H, BLUE, ORANGE, GREEN, PURPLE, YELLOW, NAVY, GRAY,
                         white, ITEMS, reg, Book)
from content_helpers import (obj_grid, dots_grid, trace_num, write_nums,
                             write_lines, match_row, qbox, choice_row,
                             section_banner, mascot, OBJ_SVG)

def unit_c_intro(b):
    b.start('Unit C • Nombor 11 hingga 20', 'Nombor lebih besar daripada 10. Mari kenal nombor 11 hingga 20!',
            'JOM FAHAM', PURPLE, kind='unit')
    mascot(b, 130, 60, 46, 46)
    b.box(15, 130, 86, 66, PURPLE, tint=True)
    b.text(20, 140, 'APA YANG KITA ADALAH', 9, True, PURPLE)
    b.para(20, 148, 'Dalam Unit C, kamu akan:', 76, 9.3, NAVY)
    for i, t in enumerate(['Mengira hingga 20.', 'Baca dan tulis nombor 11–20.',
                           'Membandingkan nombor hingga 20.', 'Susun nombor hingga 20.']):
        b.text(24, 160 + i * 12, '•', 9, True, PURPLE)
        b.text(29, 160 + i * 12, t, 9, False, NAVY)
    b.box(111, 130, 84, 66, ORANGE, tint=True)
    b.text(116, 140, 'PERASAN SEMUA', 9, True, ORANGE)
    b.para(116, 148, 'Nombor 11 hingga 20 ialah nombor dua digit. Ten-frame membantu kamu melihat berapa banyak.',
           74, 9, NAVY)
    b.finish()

def c_count11_20(b):
    b.start('Kira hingga 20', 'Kira benda-benda ini. Tulis nombornya.',
            'JOM FAHAM', PURPLE, kind='lesson')
    b.objective_line('Mengira set objek hingga 20 secara satu-satu dan berkumpulan.')
    obj_grid(b, 15, 62, 15, 5, gap_x=19, gap_y=19, size=13, names=['epal'])
    b.box(15 + 5 * 20 + 10, 62, 28, 20, GRAY, tint=False, dash=True)
    b.text(15 + 5 * 20 + 29, 69, '15', 11, True, NAVY, 'center')
    b.para(15, 116, 'Kira lagi. Kumpulan ini ada 20 benda.', 180, 10, NAVY, True)
    dots_grid(b, 25, 132, 20, 5, step=12, r=3, color=ORANGE)
    b.box(25 + 5 * 13 + 10, 132, 28, 20, GRAY, tint=False, dash=True)
    b.text(25 + 5 * 13 + 29, 139, '20', 11, True, NAVY, 'center')
    b.para(15, 178, 'Tulis nombor 11 hingga 20 mengikut turutan.', 180, 10, NAVY, True)
    write_nums(b, 15, 188, [11, 12, 13, 14, 15], size=11, gap=13, boxw=28, boxh=26)
    write_nums(b, 15, 220, [16, 17, 18, 19, 20], size=11, gap=13, boxw=28, boxh=26)
    reg('C1-01', 'Mengira hingga 20', 'C1 Mengira', 'Basic',
        'Kira 15 epal dan 20 titik; tulis turutan 11–20.',
        '15; 20; 11,12,13,14,15,16,17,18,19,20', book=b.name, page=b.page)
    b.tip(15, 248, 180, 'Kira 5 demi 5 jika sudah pandai. 5, 10, 15, 20.',
          PURPLE, 'BIJAK NAK COUNTET')
    b.check_strip(15, 266, 180, 'Selesai? Tandakan ★ di penjejak.')
    b.finish()

def c_teen_structure(b):
    b.start('Nombor belasan: 1 puluhan + beberapa sa', 'Nombor 12 bermaksud 1 puluhan dan 2 sa. Ten-frame menunjukkan 10 dan baki.',
            'JOM FAHAM', PURPLE, kind='lesson')
    b.objective_line('Memahami struktur dua digit: 1 puluhan + beberapa sa.')
    for i, (n, fill) in enumerate([(12, 2), (15, 5), (18, 8)]):
        x = 15 + i * 62
        b.ten_frame(x, 64, 44, fill, color=BLUE)
        b.big_num(x + 22, 118, n, 20, ORANGE, 'center')
        b.text(x + 22, 132, str(n), 10, False, NAVY, 'center')
        b.text(x + 22, 146, f'10 + {n-10}', 10, True, GREEN, 'center')
    b.para(15, 170, 'Lihat nombor 17 di bawah. Isi ten-frame mengikut nombor itu.', 180, 10, NAVY, True)
    b.text(60, 192, '17', 22, True, ORANGE, 'center')
    b.ten_frame(105, 176, 44, 0, color=BLUE)
    b.para(15, 230, 'Tulis nombor untuk setiap ten-frame.', 180, 10, NAVY, True)
    b.box(30, 244, 40, 24, GRAY, tint=False, dash=True)
    b.ten_frame(95, 240, 40, 4, color=GREEN)
    b.text(150, 250, '____', 12, True, NAVY)
    reg('C2-01', 'Memahami nombor belasan', 'C2 Struktur nombor', 'Basic',
        'Mengikut ten-frame: 12 = 10+2; 15 = 10+5; 18 = 10+8. Isi ten-frame untuk 17 (7 diisi).',
        '12, 15, 18; ten-frame 17: 7 petak diisi; ten-frame dengan 4 diisi = 14',
        book=b.name, page=b.page)
    b.help_box(15, 244, 180, 'Nombor belasan bermula dengan angka 1 di tempat puluhan. Baki ialah angka belakang.')
    b.finish()

def c_readwrite(b):
    b.start('Baca dan tulis nombor 11 hingga 20', 'Baca nombor. Tulis nombor itu dalam kotak.',
            'JOM FAHAM', PURPLE, kind='practice')
    b.objective_line('Membaca dan menulis numeral 11–20.')
    pairs = [(13, '13'), (16, '16'), (19, '19'), (11, '11'), (20, '20')]
    for i, (n, _) in enumerate(pairs):
        x = 15 + i * 37
        b.box(x, 62, 32, 26, BLUE, tint=False)
        b.text(x + 16, 74, str(n), 16, True, NAVY, 'center')
        b.box(x, 100, 32, 26, GRAY, tint=False, dash=True)
    b.para(15, 140, 'Tulis nombor-nombor ini dengan cantik:', 180, 10, NAVY, True)
    write_nums(b, 15, 154, [12, 14, 17, 18], size=11, gap=15, boxw=30, boxh=24)
    reg('C3-01', 'Baca dan tulis 11–20', 'C3 Menulis nombor', 'Basic',
        'Baca dan tulis numeral 13, 16, 19, 11, 20; tulis 12, 14, 17, 18.',
        '13, 16, 19, 11, 20; 12, 14, 17, 18 (penilaian penulisan MANUAL)',
        book=b.name, page=b.page, status='MANUAL REVIEW REQUIRED')
    b.tip(15, 204, 180, 'Tulis angka 1 dahulu, kemudian angka belakang. 1 lalu 3 = 13.',
          PURPLE, 'BIJAK NAK COUNTET')
    b.check_strip(15, 266, 180, 'Selesai? Tandakan ★ di penjejak.')
    b.finish()

def c_compare(b):
    b.start('Nombor 11–20: lebih besar atau lebih kecil?', 'Bulatkan nombor yang lebih besar dalam setiap pasangan.',
            'JOM FAHAM', ORANGE, kind='lesson')
    b.objective_line('Membandingkan nilai numeral dalam julat 11–20.')
    pairs = [(12, 18), (20, 15), (14, 14), (17, 11), (19, 16), (13, 20)]
    for i, (a, bb) in enumerate(pairs):
        row, col = i // 2, i % 2
        x = 15 + col * 92
        y = 64 + row * 44
        b.box(x, y, 26, 26, GRAY, tint=False)
        b.text(x + 13, y + 9, str(a), 13, True, NAVY, 'center')
        b.text(x + 30, y + 10, 'dan', 9, False, GRAY, 'center')
        b.box(x + 40, y, 26, 26, GRAY, tint=False)
        b.text(x + 53, y + 9, str(bb), 13, True, NAVY, 'center')
        b.text(x + 70, y + 10, '→', 12, True, GRAY)
        b.box(x + 80, y, 26, 26, ORANGE, tint=False, dash=True)
    b.para(15, 214, 'Isi kotak dengan nombor yang lebih kecil.', 180, 10, NAVY, True)
    pairs2 = [(18, 12), (20, 17)]
    for i, (a, bb) in enumerate(pairs2):
        x = 15 + i * 92
        b.box(x, 232, 26, 26, GRAY, tint=False)
        b.text(x + 13, 241, str(a), 13, True, NAVY, 'center')
        b.text(x + 30, 242, 'dan', 9, False, GRAY, 'center')
        b.box(x + 40, 232, 26, 26, GRAY, tint=False)
        b.text(x + 53, 241, str(bb), 13, True, NAVY, 'center')
        b.text(x + 70, 242, '→', 12, True, GRAY)
        b.box(x + 80, 232, 26, 26, GREEN, tint=False, dash=True)
    reg('C4-01', 'Membandingkan nombor 11–20', 'C4 Perbandingan', 'Basic',
        'Bulat nombor lebih besar: (12,18)→18; (20,15)→20; (14,14)→sama; (17,11)→17; (19,16)→19; (13,20)→20. Tulis lebih kecil: 12, 17, 11.',
        '18, 20, 14 (sama), 17, 19, 20; lebih kecil: 12, 17, 11',
        book=b.name, page=b.page)
    b.help_box(15, 246, 180, 'Semua nombor belasan bermula dengan 1. Bandingkan angka belakang: lebih besar di belakang, lebih besar nilainya.')
    b.check_strip(15, 266, 180, 'Selesai? Tandakan ★ di penjejak.')
    b.finish()

def c_order(b):
    b.start('Susun nombor hingga 20', 'Susun nombor-nombor ini mengikut turutan dari terkecil.',
            'JOM FAHAM', GREEN, kind='practice')
    b.objective_line('Menyusun nombor dalam julat 1–20 mengikut turutan menaik.')
    sets = [[14, 11, 17], [20, 13, 16], [19, 12, 18]]
    for i, s in enumerate(sets):
        y = 64 + i * 34
        b.text(15, y, f'{i+1}.', 11, True, GREEN)
        for j, n in enumerate(s):
            b.box(30 + j * 34, y - 4, 26, 20, GRAY, tint=False)
            b.text(43 + j * 34, y + 4, str(n), 11, True, NAVY, 'center')
        for j in range(2):
            b.c.setStrokeColor(b.color(GRAY)); b.c.setLineWidth(.5)
            b.c.setDash(2, 2)
            b.c.line((78 + j * 34) * MM, H - (y + 6) * MM, (96 + j * 34) * MM, H - (y + 6) * MM)
            b.c.setDash()
    b.para(15, 172, 'Tulis nombor 11 hingga 20 mengikut turutan di bawah.', 180, 10, NAVY, True)
    write_lines(b, 15, 190, 180, 2, gap=11)
    reg('C5-01', 'Menyusun nombor hingga 20', 'C5 Susunan', 'Basic',
        'Susun 14,11,17 → 11,14,17; 20,13,16 → 13,16,20; 19,12,18 → 12,18,19.',
        '11,14,17 | 13,16,20 | 12,18,19', book=b.name, page=b.page)
    b.tip(15, 236, 180, 'Nombor yang lebih kecil datang dahulu. 11 ialah nombor belasan yang paling kecil.',
          GREEN, 'BIJAK NAK COUNTET')
    b.finish()

def c_review(b):
    b.start('Semakan Unit C', 'Mari semak nombor 11 hingga 20.',
            'JOM KUASAI', GREEN, kind='review')
    mascot(b, 152, 58, 34, 34, note='Hebat!')
    b.text(15, 108, '1. Kira dan tulis nombor:', 10.5, True, NAVY)
    dots_grid(b, 25, 120, 18, 5, step=12, r=3, color=BLUE)
    b.box(140, 120, 28, 20, GRAY, tint=False, dash=True)
    b.text(154, 127, '18', 11, True, NAVY, 'center')
    b.text(15, 158, '2. 10 + 6 = ____', 11, True, NAVY)
    b.box(80, 154, 30, 22, GRAY, tint=False, dash=True)
    b.text(15, 182, '3. Bulat nombor lebih besar: 15 dan 12', 10.5, True, NAVY)
    b.box(30, 190, 26, 24, GRAY, tint=False)
    b.text(43, 202, '15', 12, True, NAVY, 'center')
    b.text(80, 194, 'dan', 9, False, GRAY)
    b.box(105, 190, 26, 24, GRAY, tint=False)
    b.text(118, 202, '12', 12, True, NAVY, 'center')
    b.text(140, 194, '→', 12, True, GRAY)
    b.box(160, 190, 26, 24, ORANGE, tint=False, dash=True)
    reg('CR-01', 'Semakan Unit C', 'CR Semakan', 'Basic',
        'Kira 18 titik; 10+6; bandingkan 15 dan 12 → bulatkan 15.',
        '18; 16; 15', book=b.name, page=b.page)
    b.check_strip(15, 268, 180, 'Selesai Unit C? Tandakan ★ di penjejak.')
    b.finish()

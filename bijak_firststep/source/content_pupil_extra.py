#!/usr/bin/env python3
"""Pupil Book — Extra practice pages (Colony 11): fill-in and mixed practice."""
from prod_engine import (MM, W, H, BLUE, ORANGE, GREEN, PURPLE, YELLOW, NAVY, GRAY,
                         white, ITEMS, reg, Book)
from content_helpers import (obj_grid, dots_grid, write_nums, choice_row,
                             section_banner, mascot)


def bx_fill(b):
    """Unit B practice: fill in the missing numbers 1 to 10."""
    b.start('Isi nombor yang tertinggal', 'Nombor-nombor ini tertinggal beberapa. Isi nombor yang kosong.',
            'JOM FAHAM', BLUE, kind='practice')
    b.objective_line('Isi nombor yang tertinggal dalam turutan 1 hingga 10.')
    seqs = [
        ([2, 3, 4, None, 6, 7, None, 9, 10], '1.'),
        ([1, None, 3, 4, None, 6, 7, 8, None, 10], '2.'),
        ([None, 2, None, 4, 5, None, 7, None, 9, None], '3.'),
    ]
    for i, (seq, num) in enumerate(seqs):
        for r in range(2):
            y = 56 + i * 50 + r * 24
            b.text(15, y + 5, num if r == 0 else '', 11, True, BLUE)
            x = 28
            for n in seq[r * 5:r * 5 + 5]:
                if n is None:
                    b.box(x, y, 24, 18, GRAY, tint=False, dash=True)
                else:
                    b.box(x, y, 24, 18, GRAY, tint=False)
                    b.text(x + 12, y + 6, str(n), 10, True, NAVY, 'center')
                x += 24 + 8
    b.para(15, 214, 'Kira dan tulis nombor untuk setiap kumpulan.', 180, 10, NAVY, True)
    obj_grid(b, 22, 226, 5, 5, gap_x=14, gap_y=14, size=12, names=['epal'])
    b.box(22 + 5 * 26 + 4, 226, 26, 20, GRAY, tint=False, dash=True)
    obj_grid(b, 130, 226, 3, 3, gap_x=14, gap_y=14, size=12, names=['bola'])
    b.box(130 + 3 * 26 + 4, 226, 26, 20, GRAY, tint=False, dash=True)
    reg('BX-01', 'Isi nombor tertinggal 1–10', 'BX Latihan tambahan', 'Basic',
        'Tiga turutan nombor dengan nombor kosong; isi nombor yang tertinggal. Kira dua kumpulan (5 dan 3).',
        '1) 5, 8; 2) 2, 5, 9; 3) 1, 3, 6, 8, 10; kumpulan: 5 dan 3', book=b.name, page=b.page)
    b.tip(15, 244, 180, 'Tulis nombor mengikut turutan. Cuba tulis 1 hingga 10 di tepi kertas dahulu.',
          BLUE, 'BIJAK NAK COUNTET')
    b.check_strip(15, 266, 180, 'Selesai? Tandakan ★ di penjejak.')
    b.finish()


def cx_fill(b):
    """Unit C practice: fill in the missing numbers 11 to 20."""
    b.start('Isi nombor yang tertinggal', 'Nombor-nombor belasan ini tertinggal beberapa. Isi nombor yang kosong.',
            'JOM FAHAM', GREEN, kind='practice')
    b.objective_line('Isi nombor yang tertinggal dalam turutan 11 hingga 20.')
    seqs = [
        ([11, 12, None, 14, 15, 16, None, 18, 19, 20], '1.'),
        ([11, None, 13, 14, None, 16, 17, None, 19, 20], '2.'),
        ([11, 12, 13, None, 15, None, 17, 18, None, 20], '3.'),
    ]
    for i, (seq, num) in enumerate(seqs):
        for r in range(2):
            y = 54 + i * 50 + r * 24
            b.text(15, y + 5, num if r == 0 else '', 11, True, GREEN)
            x = 28
            for n in seq[r * 5:r * 5 + 5]:
                if n is None:
                    b.box(x, y, 24, 18, GRAY, tint=False, dash=True)
                else:
                    b.box(x, y, 24, 18, GRAY, tint=False)
                    b.text(x + 12, y + 6, str(n), 9.5, True, NAVY, 'center')
                x += 24 + 8
    b.para(15, 204, 'Bulat nombor yang paling besar dalam setiap pasangan.', 180, 10, NAVY, True)
    pairs = [(12, 17), (15, 14)]
    for i, (m, n) in enumerate(pairs):
        y = 212 + i * 14
        b.box(30, y, 24, 18, GRAY, tint=False)
        b.text(42, y + 6, str(m), 10.5, True, NAVY, 'center')
        b.text(66, y + 6, 'dan', 9, False, GRAY)
        b.box(90, y, 24, 18, GRAY, tint=False)
        b.text(102, y + 6, str(n), 10.5, True, NAVY, 'center')
        b.text(122, y + 6, '→', 10, True, GRAY)
        b.box(142, y, 24, 18, ORANGE, tint=False, dash=True)
    reg('CX-01', 'Isi nombor tertinggal 11–20', 'CX Latihan tambahan', 'Basic',
        'Tiga turutan nombor belasan dengan nombor kosong; isi nombor yang tertinggal. Bulat yang terbesar: 17, 15.',
        '1) 13, 17; 2) 12, 15, 18; 3) 14, 16, 19; bulatan: 17, 15', book=b.name, page=b.page)
    b.tip(15, 248, 180, 'Nombor belasan sentiasa bermula dengan 1. Lihat angka belakang untuk bandingkan.',
          GREEN, 'BIJAK NAK COUNTET')
    b.check_strip(15, 268, 180, 'Selesai? Tandakan ★ di penjejak.')
    b.finish()


def dx_mixed(b):
    """Unit D practice: mixed addition and subtraction within 10."""
    b.start('Latihan tambah dan tolak', 'Selesaikan semua pengiraan ini. Isi jawapan yang betul.',
            'JOM FAHAM', PURPLE, kind='practice')
    b.objective_line('Menyelesaikan tambah dan tolak dalam lingkungan 10 secara bercampur.')
    rows = [('4 + 3 =', 7), ('9 - 2 =', 7), ('5 + 4 =', 9), ('8 - 5 =', 3),
            ('2 + 6 =', 8), ('10 - 3 =', 7), ('7 + 2 =', 9), ('6 - 1 =', 5)]
    for i, (eq, ans) in enumerate(rows):
        y = 62 + i * 22
        b.text(18, y + 5, f'{i+1}.', 10, True, PURPLE)
        b.text(32, y + 5, eq, 12, True, NAVY)
        b.box(120, y, 30, 20, GRAY, tint=False, dash=True)
    reg('DX-01', 'Latihan tambah dan tolak (dalam 10)', 'DX Latihan tambahan', 'Basic',
        'Selesaikan lapan pengiraan tambah dan tolak dalam lingkungan 10.',
        '7, 7, 9, 3, 8, 7, 9, 5', book=b.name, page=b.page)
    b.tip(15, 248, 180, 'Kira dengan jari. Tolak: kira ke belakang. Tambah: kira ke hadapan.',
          PURPLE, 'BIJAK NAK COUNTET')
    b.check_strip(15, 266, 180, 'Selesai? Tandakan ★ di penjejak.')
    b.finish()


def ex_practice(b):
    """Unit E consolidation: shapes, counting and comparison."""
    b.start('Latihan Permulaan', 'Mari ulang kaji bentuk, pengiraan dan perbandingan.',
            'JOM FAHAM', ORANGE, kind='practice')
    b.objective_line('Mengulang kaji bentuk, mengira dan membandingkan kuantiti.')
    b.text(15, 62, '1. Namakan bentuk di bawah.', 10.5, True, NAVY)
    b.c.setStrokeColor(b.color(NAVY)); b.c.setLineWidth(1.5)
    shapes = [('Bulatan', 22, 74, 'circle'), ('Segi empat', 100, 74, 'rect'),
              ('Segi tiga', 158, 74, 'tri')]
    for label, x, y, kind in shapes:
        s = 26
        if kind == 'circle':
            b.c.circle((x + s / 2) * MM, H - (y + s / 2) * MM, (s / 2) * MM)
        elif kind == 'rect':
            b.c.rect(x * MM, H - (y + s) * MM, s * MM, s * MM)
        else:
            p1 = (x * MM, H - y * MM)
            p2 = ((x + s) * MM, H - y * MM)
            p3 = ((x + s / 2) * MM, H - (y + s * 0.82) * MM)
            for a, c in ((p1, p2), (p2, p3), (p3, p1)):
                b.c.line(a[0], a[1], c[0], c[1])
        b.text(x, y + 34, label, 9, False, NAVY, 'center')
    b.text(15, 134, '2. Kira dan bandingkan.', 10.5, True, NAVY)
    obj_grid(b, 22, 146, 7, 4, gap_x=15, gap_y=15, size=12, names=['epal'])
    b.box(104, 146, 26, 20, GRAY, tint=False, dash=True)
    obj_grid(b, 130, 146, 3, 3, gap_x=15, gap_y=15, size=12, names=['bola'])
    b.box(130 + 3 * 16 + 4, 146, 26, 20, GRAY, tint=False, dash=True)
    b.para(15, 180, 'Kumpulan epal ____ kumpulan bola', 10.5, True, NAVY)
    choice_row(b, 15, 192, ['lebih', 'kurang', 'sama'])
    b.para(15, 222, '3. Tulis nombor 15 dan 18. Nombor manakah yang lebih besar?', 180, 10, NAVY, True)
    b.box(30, 232, 30, 22, GRAY, tint=False, dash=True)
    b.box(100, 232, 30, 22, GRAY, tint=False, dash=True)
    reg('EX-01', 'Latihan Permulaan: bentuk dan pengiraan', 'EX Latihan tambahan', 'Basic',
        'Namakan tiga bentuk; kira 7 epal dan 3 bola (lebih); tulis 15 dan 18, 18 lebih besar.',
        'Bulatan, segi empat, segi tiga; 7 dan 3 (epal lebih); 15 dan 18, 18 lebih besar', book=b.name, page=b.page)
    b.tip(15, 244, 180, 'Ambil masa perlahan-lahan. Semak pengiraan kamu sekali lagi.',
          ORANGE, 'BIJAK NAK COUNTET')
    b.check_strip(15, 268, 180, 'Selesai? Tandakan ★ di penjejak.')
    b.finish()

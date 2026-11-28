#!/usr/bin/env python3
"""Pupil Book Unit E — Everyday mathematics + creative + assessment (Colony 11)."""
from prod_engine import (MM, W, H, BLUE, ORANGE, GREEN, PURPLE, YELLOW, NAVY, GRAY,
                         white, ITEMS, reg, Book)
from content_helpers import (obj_grid, dots_grid, trace_num, write_nums,
                             write_lines, match_row, qbox, choice_row,
                             section_banner, mascot, OBJ_SVG)

def unit_e_intro(b):
    b.start('Unit E • Matematik seharian', 'Matematik ada di mana-mana: bentuk, arah, saiz, masa dan data. Jom cari!',
            'JOM FAHAM', GREEN, kind='unit')
    mascot(b, 130, 60, 46, 46)
    b.box(15, 130, 86, 66, GREEN, tint=True)
    b.text(20, 140, 'APA YANG KITA ADALAH', 9, True, GREEN)
    b.para(20, 148, 'Dalam Unit E, kamu akan:', 76, 9.3, NAVY)
    for i, t in enumerate(['Mengenali bentuk 2D dan 3D.', 'Belajar arah dan kedudukan.',
                           'Membandingkan panjang dan saiz.', 'Belajar tentang masa setiap hari.']):
        b.text(24, 160 + i * 12, '•', 9, True, GREEN)
        b.text(29, 160 + i * 12, t, 9, False, NAVY)
    b.box(111, 130, 84, 66, ORANGE, tint=True)
    b.text(116, 140, 'PERASAN SEMUA', 9, True, ORANGE)
    b.para(116, 148, 'Cari matematik di rumah: bentuk tingkap, arah pintu, panjang rambut. Seronok melihat dunia secara matematik!',
           74, 9, NAVY)
    b.finish()

def e_shapes(b):
    b.start('Bentuk di sekeliling kita', 'Bulat, segi empat, segi tiga. Kenal pasti dan warnakan bentuk mengikut arahan.',
            'JOM FAHAM', GREEN, kind='lesson')
    b.objective_line('Mengenali dan menamakan bentuk 2D: bulatan, segi empat, segi tiga.')
    shapes = [('circle', 'Bulatan', BLUE), ('square', 'Segi empat', ORANGE),
              ('triangle', 'Segi tiga', GREEN), ('rect', 'Segi empat panjang', PURPLE),
              ('star', 'Bintang', ORANGE), ('heart', 'Hati', BLUE)]
    for i, (kind, name, col) in enumerate(shapes):
        x = 15 + (i % 3) * 62
        y = 64 + (i // 3) * 46
        b.shape(kind, x + 22, y + 12, 30, col)
        b.text(x + 22, y + 40, name, 9, True, NAVY, 'center')
    b.para(15, 172, 'Warnakan: bulatan biru, segi tiga hijau, bintang oren.', 180, 10, NAVY, True)
    for (kind, col) in [('circle', BLUE), ('triangle', GREEN), ('star', ORANGE)]:
        b.shape(kind, 45, 200, 34, col)
    b.shape('square', 100, 205, 34, GRAY)
    b.shape('rect', 150, 205, 34, GRAY)
    b.text(15, 242, 'Cari tiga benda di rumah yang berbentuk segi tiga. Tanya ibu atau ayah.', 9.5, False, NAVY)
    reg('E1-01', 'Mengenali bentuk 2D', 'E1 Bentuk', 'Basic',
        'Menamakan 6 bentuk (bulatan, segi empat, segi tiga, segi empat panjang, bintang, hati) dan mewarnakan 3 bentuk mengikut arahan.',
        'Bulatan, segi empat, segi tiga, segi empat panjang, bintang, hati; warna: bulatan biru, segi tiga hijau, bintang oren',
        book=b.name, page=b.page, status='PARTIAL')
    b.tip(15, 252, 180, 'Bulatan tiada bucu. Segi tiga ada 3 bucu. Segi empat ada 4 bucu.',
          GREEN, 'BIJAK NAK COUNTET')
    b.finish()

def e_shapes2(b):
    b.start('Bentuk 3D: gebukan dan kubus', 'Bentuk 3D mempunyai isipadu. Kenal pasti bentuk 3D di bawah.',
            'JOM FAHAM', GREEN, kind='practice')
    b.objective_line('Mengenali bentuk 3D asas: kubus, gebukan, sfera, kon.')
    shapes3d = [('kubus', 'Kubus', BLUE), ('gebukan', 'Gebukan', ORANGE),
                ('sfera', 'Sfera', GREEN), ('kon', 'Kon', PURPLE)]
    for i, (name, label, col) in enumerate(shapes3d):
        x = 15 + i * 47
        b.box(x, 64, 42, 70, col, tint=True)
        b.text(x + 21, 84, label, 10, True, col, 'center')
        if name == 'kubus':
            b.c.setStrokeColor(b.color(NAVY)); b.c.setLineWidth(.7)
            b.c.rect(x + 8 * MM, H - 118 * MM, 26 * MM, 26 * MM, stroke=1, fill=0)
            b.c.line((x + 8) * MM, H - 118 * MM, (x + 19) * MM, H - 107 * MM)
            b.c.line((x + 34) * MM, H - 118 * MM, (x + 45) * MM, H - 107 * MM)
        elif name == 'gebukan':
            b.c.setStrokeColor(b.color(NAVY)); b.c.setLineWidth(.7)
            b.c.circle((x + 21) * MM, H - 96 * MM, 15 * MM, stroke=1, fill=0)
            b.c.ellipse((x + 6) * MM, H - 112 * MM, (x + 36) * MM, H - 100 * MM, stroke=1, fill=0)
        elif name == 'sfera':
            b.c.setFillColor(b.color(col))
            b.c.setStrokeColor(b.color(NAVY)); b.c.setLineWidth(.7)
            b.c.circle((x + 21) * MM, H - 96 * MM, 15 * MM, stroke=1, fill=1)
        elif name == 'kon':
            b.c.setStrokeColor(b.color(NAVY)); b.c.setLineWidth(.7)
            p = b.c.beginPath()
            p.moveTo((x + 21) * MM, H - 76 * MM)
            p.lineTo((x + 8) * MM, H - 116 * MM)
            p.lineTo((x + 34) * MM, H - 116 * MM)
            p.close()
            b.c.drawPath(p, stroke=1, fill=0)
            b.c.ellipse((x + 8) * MM, H - 118 * MM, (x + 34) * MM, H - 112 * MM, stroke=1, fill=0)
    b.para(15, 158, 'Tampal atau lukis: cari satu benda di rumah untuk setiap bentuk 3D.', 180, 10, NAVY, True)
    for i in range(4):
        b.box(15 + i * 45, 178, 40, 26, GRAY, tint=False, dash=True)
    b.text(15, 220, 'Kubus ada 6 muka yang sama. Gebukan ada 6 muka, tetapi bukan semuanya sama.', 9.5, False, NAVY)
    reg('E1-02', 'Mengenali bentuk 3D', 'E1 Bentuk', 'Basic',
        'Menamakan kubus, gebukan, sfera, kon dan mencari contoh di rumah.',
        'Kubus, gebukan, sfera, kon (penilaian contoh rumah OPEN)',
        book=b.name, page=b.page, status='OPEN-ENDED')
    b.finish()

def e_position(b):
    b.start('Arah dan kedudukan', 'Atas, bawah, kiri, kanan, depan, belakang. Lihat gambar dan ikut arahan.',
            'JOM FAHAM', PURPLE, kind='lesson')
    b.objective_line('Menggunakan bahasa arah dan kedudukan dalam konteks gambar.')
    # simple scene: house, tree, car
    b.box(60, 120, 70, 50, ORANGE, tint=False)
    b.text(95, 138, 'Rumah', 9, True, NAVY, 'center')
    b.shape('triangle', 45, 96, 34, GREEN)
    b.shape('circle', 150, 96, 24, YELLOW)
    b.svg('bola.svg', 20, 180, 14, 14)
    b.svg('bola.svg', 175, 180, 14, 14)
    b.text(27, 166, 'kiri', 8, False, GRAY, 'center')
    b.text(182, 166, 'kanan', 8, False, GRAY, 'center')
    b.text(95, 186, 'bawah', 8, False, GRAY, 'center')
    b.text(95, 78, 'atas', 8, False, GRAY, 'center')
    b.para(15, 204, 'Ikut arahan:', 180, 10.5, NAVY, True)
    for i, t in enumerate(['1. Warnakan rumah di atas garisan.',
                           '2. Wajarkan bulatan di sebelah kanan rumah.',
                           '3. Lintang pada bola di sebelah kiri.']):
        b.text(22, 220 + i * 12, t, 9.5, False, NAVY)
    reg('E2-01', 'Menggunakan arah dan kedudukan', 'E2 Arah', 'Basic',
        'Mengikut arahan kedudukan: warnakan rumah, warnakan bulatan di kanan, lintang bola di kiri.',
        'OPEN — penilaian melalui lukisan yang mengikut arahan',
        book=b.name, page=b.page, status='OPEN-ENDED')
    b.tip(15, 256, 180, 'Arah "kiri" dan "kanan" bergantung pada pandangan kamu, bukan pandangan orang lain.',
          PURPLE, 'BIJAK NAK COUNTET')
    b.finish()

def e_compare_measure(b):
    b.start('Panjang dan saiz', 'Panjang atau pendek? Besar atau kecil? Bandingkan dan lingkar.',
            'JOM FAHAM', ORANGE, kind='lesson')
    b.objective_line('Membandingkan panjang dan saiz secara langsung.')
    # crayons of different lengths
    crayon_len = [50, 38, 62]
    for i, ln in enumerate(crayon_len):
        x = 30 + i * 55
        b.c.setFillColor(b.color([BLUE, ORANGE, GREEN][i]))
        b.c.setStrokeColor(b.color(NAVY)); b.c.setLineWidth(.5)
        b.c.rect(x * MM, H - 84 * MM, 12 * MM, ln * MM, stroke=1, fill=1)
        b.c.setFillColor(b.color(NAVY))
        b.c.circle((x + 6) * MM, H - 84 * MM, 3 * MM, stroke=0, fill=1)
    b.text(15, 96, 'Lingkarkan yang paling panjang.', 10, True, NAVY)
    b.text(15, 110, 'Lingkarkan yang paling pendek.', 10, True, NAVY)
    b.c.setStrokeColor(b.color(ORANGE)); b.c.setLineWidth(1.6)
    b.c.circle(92 * MM, H - 70 * MM, 14 * MM, stroke=1, fill=0)
    b.c.setStrokeColor(b.color(BLUE)); b.c.setLineWidth(1.6)
    b.c.circle(38 * MM, H - 84 * MM, 12 * MM, stroke=1, fill=0)
    b.para(15, 130, 'Bandingkan saiz bentuk di bawah. Tulis "besar" atau "kecil".', 180, 10, NAVY, True)
    for i, s in enumerate([('square', 36, BLUE), ('square', 18, GREEN),
                           ('circle', 34, ORANGE), ('circle', 16, PURPLE)]):
        x = 25 + (i % 2) * 90
        y = 150 + (i // 2) * 40
        b.shape(s[0], x + s[1] / 2, y + s[1] / 2, s[1], s[2])
        b.box(x + s[1] + 10, y, 40, 20, GRAY, tint=False, dash=True)
    reg('E3-01', 'Membandingkan panjang', 'E3 Panjang', 'Basic',
        'Lingkarkan crayon paling panjang (62mm, hijau) dan paling pendek (38mm, oren).',
        'Paling panjang: crayon hijau; paling pendek: crayon oren',
        book=b.name, page=b.page)
    reg('E3-02', 'Membandingkan saiz', 'E3 Saiz', 'Basic',
        'Tulis "besar" untuk bentuk besar dan "kecil" untuk bentuk kecil (4 bentuk).',
        'Besar, kecil, besar, kecil', book=b.name, page=b.page)
    b.finish()

def e_time(b):
    b.start('Masa setiap hari', 'Hari ini ialah hari apa? Aktiviti apa yang kamu lakukan pada waktu pagi?',
            'JOM FAHAM', BLUE, kind='lesson')
    b.objective_line('Mengetahui hari dalam minggu dan aktiviti harian.')
    days = ['Isnin', 'Selasa', 'Rabu', 'Khamis', 'Jumaat', 'Sabtu', 'Ahad']
    for i, d in enumerate(days):
        x = 15 + i * 26.5
        b.box(x, 62, 24, 22, BLUE if i < 5 else GREEN, tint=False)
        b.text(x + 12, 72, d, 8.5, True, white, 'center')
    b.para(15, 100, 'Isi jadual aktiviti kamu.', 180, 10, NAVY, True)
    rows = [('Waktu pagi', 'Bersiap ke sekolah'), ('Waktu tengah hari', 'Makan tengah hari'),
            ('Waktu petang', 'Main di luar'), ('Waktu malam', 'Tidur')]
    for i, (waktu, act) in enumerate(rows):
        y = 118 + i * 28
        b.box(15, y, 52, 22, ORANGE, tint=True)
        b.text(41, y + 8, waktu, 9, True, ORANGE, 'center')
        b.box(72, y, 123, 22, GRAY, tint=False, dash=True)
        b.text(76, y + 8, act, 9, False, NAVY)
    b.para(15, 236, 'Tulis tiga aktiviti kamu pada waktu pagi.', 180, 10, NAVY, True)
    write_lines(b, 15, 252, 180, 3, gap=10)
    reg('E4-01', 'Hari dalam minggu', 'E4 Masa', 'Basic',
        'Mengetahui turutan hari: Isnin hingga Ahad.',
        'Isnin, Selasa, Rabu, Khamis, Jumaat, Sabtu, Ahad', book=b.name, page=b.page)
    reg('E4-02', 'Aktiviti harian', 'E4 Masa', 'Open',
        'Menyebut aktiviti mengikut waktu (pagi, tengah hari, petang, malam).',
        'OPEN — terima jawapan yang munasabah',
        book=b.name, page=b.page, status='OPEN-ENDED')
    b.tip(15, 276, 180, 'Setiap hari ada aktiviti sendiri. Masa membantu kamu bertindak mengikut turutan.',
          BLUE, 'BIJAK NAK COUNTET')
    b.finish()

def e_data(b):
    b.start('Kumpulkan data mudah', 'Kita kira dan susun maklumat. Ini dipanggil data.',
            'JOM FAHAM', PURPLE, kind='lesson')
    b.objective_line('Mengumpul dan membaca data mudah (gambar jadual).')
    b.text(15, 62, 'Kira setiap jenis buah di dalam gambar jadual ini.', 11, True, NAVY)
    fruits = [('epal', 4), ('bola', 3), ('buku', 2)]
    for i, (nm, n) in enumerate(fruits):
        y = 80 + i * 30
        for j in range(n):
            b.svg(OBJ_SVG[nm], 25 + j * 18, y, 14, 14)
        b.text(15, y + 6, {'epal': 'Epal', 'bola': 'Bola', 'buku': 'Buku'}[nm], 9.5, True, NAVY)
    b.para(15, 176, '1. Berapa banyak epal?  ____', 180, 10.5, NAVY)
    b.box(90, 170, 26, 20, GRAY, tint=False, dash=True)
    b.para(15, 198, '2. Berapa banyak bola?  ____', 180, 10.5, NAVY)
    b.box(90, 192, 26, 20, GRAY, tint=False, dash=True)
    b.para(15, 220, '3. Buah manakah paling banyak?', 180, 10.5, NAVY)
    b.box(150, 214, 45, 20, GREEN, tint=False, dash=True)
    reg('E5-01', 'Data mudah dan jadual gambar', 'E5 Data', 'Basic',
        'Kira epal (4), bola (3), buku (2); mengenal yang paling banyak.',
        '4; 3; epal', book=b.name, page=b.page)
    b.help_box(15, 248, 180, 'Kira satu jenis demi satu jenis. Tunggu hingga selesai sebelum menjawab.')
    b.finish()

# ---------------------------------------------------- creative extras
def creative_colour(b):
    b.start('Warnakan mengikut nombor', 'Setiap nombor mempunyai warna sendiri. Warnakan kawasan mengikut nombor.',
            'JOM CUBA', GREEN, kind='creative')
    legend = [('1', '#D97119'), ('2', '#1768AD'), ('3', '#087D63'), ('4', '#7051A3'), ('5', '#F2C94C')]
    for i, (n, col) in enumerate(legend):
        x = 15 + i * 37
        b.c.setFillColor(b.color(col)); b.c.setStrokeColor(b.color(NAVY)); b.c.setLineWidth(.4)
        b.c.circle(x * MM, H - 66 * MM, 8 * MM, stroke=1, fill=1)
        b.text(x + 16, 62, n, 10, True, NAVY)
    # colouring scene: house, sun, tree, clouds
    b.box(60, 100, 80, 60, GRAY, tint=False, dash=True)
    b.shape('triangle', 42, 78, 40, GRAY)
    b.c.setStrokeColor(b.color(GRAY)); b.c.setLineWidth(.5); b.c.setDash(2, 2)
    b.c.circle(150 * MM, H - 90 * MM, 18 * MM, stroke=1, fill=0)
    b.c.setDash()
    b.shape('circle', 30, 160, 26, GRAY)
    b.shape('square', 150, 160, 30, GRAY)
    b.text(15, 186, '1 = oren, 2 = biru, 3 = hijau, 4 = ungu, 5 = kuning', 8.5, False, GRAY)
    reg('F1-01', 'Mewarnakan mengikut nombor', 'F1 Kreatif', 'Open',
        'Mewarnakan kawasan dengan warna mengikut nombor peta.',
        'OPEN — penilaian melalui hasil warnan yang mengikut legenda',
        book=b.name, page=b.page, status='OPEN-ENDED')
    b.finish()

def creative_maze(b):
    b.start('Labirin nombor', 'Ikut lorong nombor mengikut turutan 1 hingga 10. Cari jalan ke Lebah Bijak!',
            'JOM CUBA', PURPLE, kind='creative')
    grid = [
        [1, 0, 3, 0, 5],
        [0, 2, 0, 4, 0],
        [9, 0, 7, 0, 6],
        [0, 10, 0, 8, 0],
    ]
    cell = 26
    ox, oy = 40, 80
    for r, row in enumerate(grid):
        for c, v in enumerate(row):
            x = ox + c * cell
            y = oy + r * cell
            if v == 0:
                b.box(x, y, cell - 2, cell - 2, GRAY, tint=True)
            else:
                b.box(x, y, cell - 2, cell - 2, BLUE if v <= 5 else GREEN, tint=True)
                b.text(x + cell / 2 - 1, y + 8, str(v), 10, True, white, 'center')
    mascot(b, 150, 186, 30, 30)
    b.text(150, 222, 'Lebah Bijak di hujung!', 8.5, True, GREEN, 'center')
    reg('F2-01', 'Labirin turutan nombor', 'F2 Kreatif', 'Basic',
        'Ikut lorong nombor 1 hingga 10 dari permulaan hingga Lebah Bijak.',
        'Laluan: 1→2→3→4→5→6→7→8→9→10', book=b.name, page=b.page)
    b.tip(15, 250, 180, 'Mula pada 1. Seterusnya cari nombor seterusnya di sebelah atau bawah.',
          PURPLE, 'BIJAK NAK COUNTET')
    b.finish()

def creative_puzzle(b):
    b.start('Teka-teki nombor', 'Selesaikan teka-teki ini. Tulis jawapan dalam kotak.',
            'JOM CUBA', ORANGE, kind='creative')
    b.box(15, 60, 86, 60, BLUE, tint=True)
    b.text(20, 70, '1. Saya nombor antara 4 dan 6.', 9, True, BLUE)
    b.para(20, 80, 'Siapa saya?', 76, 9, NAVY)
    b.box(20, 98, 40, 20, GRAY, tint=False, dash=True)
    b.box(109, 60, 86, 60, GREEN, tint=True)
    b.text(114, 70, '2. Saya 2 lebih daripada 5.', 9, True, GREEN)
    b.para(114, 80, 'Siapa saya?', 76, 9, NAVY)
    b.box(114, 98, 40, 20, GRAY, tint=False, dash=True)
    b.box(15, 138, 86, 60, ORANGE, tint=True)
    b.text(20, 148, '3. 3 + ____ = 10', 9, True, ORANGE)
    b.para(20, 158, 'Isi nombor yang hilang.', 76, 9, NAVY)
    b.box(20, 176, 40, 20, GRAY, tint=False, dash=True)
    b.box(109, 138, 86, 60, PURPLE, tint=True)
    b.text(114, 148, '4. 8 − ____ = 3', 9, True, PURPLE)
    b.para(114, 158, 'Isi nombor yang hilang.', 76, 9, NAVY)
    b.box(114, 176, 40, 20, GRAY, tint=False, dash=True)
    reg('F3-01', 'Teka-teki nombor', 'F3 Kreatif', 'Intermediate',
        '1. Nombor antara 4 dan 6 → 5. 2. 2 lebih daripada 5 → 7. 3. 3+____=10 → 7. 4. 8−____=3 → 5.',
        '5; 7; 7; 5', book=b.name, page=b.page)
    b.check_strip(15, 266, 180, 'Selesai? Tandakan ★ di penjejak.')
    b.finish()

def creative_cutout(b):
    b.start('Potong dan guna: kad nombor', 'Potong kad nombor di bawah. Guna kad ini untuk bermain tambah dan tolak dengan keluarga.',
            'JOM CUBA', GREEN, kind='creative')
    b.text(15, 58, 'Potong garisan putus-putus. Minta bantuan orang dewasa.', 9.5, False, GRAY)
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i, n in enumerate(nums):
        x = 15 + (i % 5) * 37
        y = 74 + (i // 5) * 46
        b.box(x, y, 32, 36, BLUE if i % 2 == 0 else ORANGE, tint=False)
        b.text(x + 16, y + 20, str(n), 16, True, white, 'center')
    b.para(15, 180, 'Cara bermain: ambil dua kad. Tambah dua kad tersebut. Contoh: 4 + 5 = 9.', 180, 9.5, NAVY)
    b.box(15, 200, 180, 46, GREEN, tint=True)
    b.text(20, 210, 'CABUARAN: cuba dapatkan jumlah 10.', 9, True, GREEN)
    b.para(20, 220, 'Cari dua kad yang tambah menjadi 10. Berapa banyak gabungan boleh kamu temui?', 170, 9, NAVY)
    b.para(20, 234, 'Contoh: 1 + 9, 2 + 8, 3 + 7, 4 + 6, 5 + 5.', 170, 9, NAVY)
    reg('F4-01', 'Kad nombor potong', 'F4 Kreatif', 'Open',
        'Menyediakan kad nombor 1–10 dan mencari pasangan tambah 10.',
        '5 gabungan: 1+9, 2+8, 3+7, 4+6, 5+5', book=b.name, page=b.page,
        status='PARTIAL')
    b.finish()

def creative_spotdiff(b):
    b.start('Cari perbezaan', 'Kedua-dua gambar hampir sama. Cari 5 perbezaan.',
            'JOM CUBA', PURPLE, kind='creative')
    # left picture
    b.box(15, 60, 85, 100, GRAY, tint=False, dash=True)
    b.text(57, 54, 'GAMBAR 1', 8, True, GRAY, 'center')
    b.svg(OBJ_SVG['epal'], 30, 78, 14, 14)
    b.svg(OBJ_SVG['epal'], 52, 78, 14, 14)
    b.svg(OBJ_SVG['bola'], 74, 78, 14, 14)
    b.svg(OBJ_SVG['epal'], 30, 104, 14, 14)
    b.svg(OBJ_SVG['bola'], 52, 104, 14, 14)
    b.svg(OBJ_SVG['bola'], 74, 104, 14, 14)
    b.svg(OBJ_SVG['epal'], 30, 130, 14, 14)
    b.svg(OBJ_SVG['epal'], 52, 130, 14, 14)
    b.svg(OBJ_SVG['epal'], 74, 130, 14, 14)
    b.shape('circle', 57, 148, 14, ORANGE)
    # right picture (differences: missing apple top-left, ball->apple mid, missing circle)
    b.box(110, 60, 85, 100, GRAY, tint=False, dash=True)
    b.text(152, 54, 'GAMBAR 2', 8, True, GRAY, 'center')
    b.svg(OBJ_SVG['epal'], 125, 78, 14, 14)
    b.svg(OBJ_SVG['epal'], 147, 78, 14, 14)
    b.svg(OBJ_SVG['bola'], 169, 78, 14, 14)
    b.svg(OBJ_SVG['epal'], 125, 104, 14, 14)
    b.svg(OBJ_SVG['epal'], 147, 104, 14, 14)
    b.svg(OBJ_SVG['bola'], 169, 104, 14, 14)
    b.svg(OBJ_SVG['epal'], 125, 130, 14, 14)
    b.svg(OBJ_SVG['epal'], 147, 130, 14, 14)
    b.svg(OBJ_SVG['epal'], 169, 130, 14, 14)
    b.text(152, 152, '○', 14, True, GRAY, 'center')
    b.para(15, 176, 'Perbezaan: (1) tiada epal kiri atas, (2) bola tengah jadi epal, (3) bulatan hilang.', 180, 9, GRAY)
    reg('F5-01', 'Spot perbezaan matematik', 'F5 Kreatif', 'Basic',
        'Menemui perbezaan kuantiti antara dua gambar (3 perbezaan tersorot).',
        '3 perbezaan: epal kiri atas hilang; bola tengah menjadi epal; bulatan bawah hilang',
        book=b.name, page=b.page)
    b.tip(15, 210, 180, 'Kira setiap kumpulan di kedua-dua gambar. Kuantiti yang berbeza itulah perbezaannya.',
          PURPLE, 'BIJAK NAK COUNTET')
    b.finish()

# ---------------------------------------------------- assessment
def final_assessment_1(b):
    b.start('Pentaksiran kesediaan 1', 'Inilah saatnya! Selesaikan semua soalan di bawah dengan tenang.',
            'JOM KUASAI', GREEN, kind='assessment')
    b.text(15, 58, 'Nama: ____________________   Tarikh: ____________', 9.5, False, NAVY)
    b.text(15, 74, '1. Kira dan tulis nombor:', 10.5, True, NAVY)
    obj_grid(b, 22, 84, 7, 4, gap_x=15, gap_y=15, size=12, names=['epal', 'bola'])
    b.box(120, 84, 28, 20, GRAY, tint=False, dash=True)
    b.text(15, 120, '2. Tulis nombor ini:', 10.5, True, NAVY)
    b.text(45, 140, '14', 20, True, BLUE, 'center')
    b.box(90, 132, 30, 24, GRAY, tint=False, dash=True)
    b.text(15, 170, '3. Lengkapkan nombor gabungan: 6 + ____ = 10', 10.5, True, NAVY)
    b.box(130, 164, 30, 24, GRAY, tint=False, dash=True)
    b.text(15, 196, '4. Selesaikan: 5 + 3 = ____', 10.5, True, NAVY)
    b.box(80, 190, 30, 24, GRAY, tint=False, dash=True)
    b.text(15, 222, '5. Selesaikan: 9 − 4 = ____', 10.5, True, NAVY)
    b.box(80, 216, 30, 24, GRAY, tint=False, dash=True)
    reg('FA-1', 'Pentaksiran kesediaan — mengira', 'FA Pentaksiran', 'Basic',
        'Kira 7 objek; tulis 14; 6+____=10; 5+3; 9−4.',
        '7; 14; 4; 8; 5', book=b.name, page=b.page)
    b.tip(15, 262, 180, 'Baca setiap soalan dengan teliti. Kamu sudah belajar semua ini!',
          GREEN, 'BIJAK NAK COUNTET')
    b.finish()

def final_assessment_2(b):
    b.start('Pentaksiran kesediaan 2', 'Teruskan! Kamu hampir selesai.',
            'JOM KUASAI', GREEN, kind='assessment')
    b.text(15, 58, '6. Bandingkan: 12 ____ 16 (isi lebih/kurang/sama)', 10.5, True, NAVY)
    choice_row(b, 15, 72, ['lebih', 'kurang', 'sama'])
    b.text(15, 104, '7. Susun mengikut turutan: 8, 11, 13', 10.5, True, NAVY)
    for j in range(3):
        b.box(60 + j * 34, 96, 28, 22, GRAY, tint=False, dash=True)
    b.text(15, 136, '8. Selesaikan: 7 + 6 = ____', 10.5, True, NAVY)
    b.box(80, 130, 30, 24, GRAY, tint=False, dash=True)
    b.text(15, 162, '9. Selesaikan: 15 − 8 = ____', 10.5, True, NAVY)
    b.box(80, 156, 30, 24, GRAY, tint=False, dash=True)
    b.text(15, 188, '10. Masalah: Enam orang kanak-kanak bermain. Tiga lagi datang. Berapa orang?', 10.5, True, NAVY)
    b.box(80, 182, 30, 24, GRAY, tint=False, dash=True)
    b.text(15, 214, '11. Bentuk: Lingkar semua bulatan di bawah.', 10.5, True, NAVY)
    for j, sh in enumerate(['○', '□', '○', '△', '○', '□']):
        b.text(30 + j * 26, 238, sh, 14, True, BLUE, 'center')
    reg('FA-2', 'Pentaksiran kesediaan — perbandingan', 'FA Pentaksiran', 'Basic',
        '12 kurang daripada 16; susun 8,11,13 → 8,11,13 (sudah tersusun); 7+6=13; 15−8=7.',
        '"kurang"; 8, 11, 13; 13; 7', book=b.name, page=b.page)
    reg('FA-3', 'Pentaksiran kesediaan — masalah dan bentuk', 'FA Pentaksiran', 'Basic',
        '6+3=9 orang; lingkarkan 3 bulatan.',
        '9; 3 bulatan dilingkarkan', book=b.name, page=b.page)
    b.check_strip(15, 270, 180, 'Selesai pentaksiran? Tandakan ★ terakhir!')
    b.finish()

def achievement(b):
    b.count += 1
    b.page = b.count
    from prod_engine import PAGES_LOG
    PAGES_LOG.append({'file': b.name, 'page': b.page,
                      'title': 'SIJIL KECEMERLANGAN', 'kind': 'achievement'})
    # certificate style
    b.c.setFillColor(b.color(YELLOW))
    b.c.rect(0, H - 90 * MM, W, 90 * MM, stroke=0, fill=1)
    b.c.setFillColor(b.color(ORANGE))
    b.c.rect(0, H - 96 * MM, W, 6 * MM, stroke=0, fill=1)
    b.text(15, 34, 'SIJIL KECEMERLANGAN', 24, True, NAVY)
    b.text(15, 60, 'BIJAK MATEMATIK', 13, True, BLUE)
    b.svg('lebah_bijak.svg', 120, 100, 60, 60)
    b.box(15, 190, 180, 40, BLUE, tint=False)
    b.text(20, 214, 'Dipersembahkan kepada:', 9, True, NAVY)
    b.text(20, 232, '________________________', 11, True, NAVY)
    b.para(15, 246, 'atas kejayaan menyelesaikan BIJAK MATEMATIK — Edisi Khas', 180, 9, NAVY)
    b.para(15, 258, 'Transisi ke Tahun 1. Kamu sudah bersedia untuk sekolah!', 180, 9, NAVY)
    for i, s in enumerate(['★', '★', '★', '★', '★']):
        b.star(40 + i * 24, 272, 5, YELLOW)
    b.text(195, 280, f'{b.page:02d}', 8, True, GRAY, 'right')
    b.finish()

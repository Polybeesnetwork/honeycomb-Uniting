#!/usr/bin/env python3
"""Build the BIJAK FirstStep Parent/Teacher Guide (Colony 11)."""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from prod_engine import (MM, W, H, BLUE, ORANGE, GREEN, PURPLE, YELLOW, NAVY, GRAY,
                         white, Book)
from content_helpers import mascot

QA = Path('../qa')
REG = json.loads(Path('../data/item_registry.json').read_text())
BOOK = '03_BIJAK_FirstStep_Parent_Teacher_Guide.pdf'


def ctext(b, cx, y, text, size, bold, color, maxw=176):
    from reportlab.pdfbase import pdfmetrics
    f = 'BM-Bold' if bold else 'BM'
    if pdfmetrics.stringWidth(text, f, size) <= maxw:
        b.text(cx - pdfmetrics.stringWidth(text, f, size) / 2, y, text, size, bold, color)
        return
    if bold:
        while size > 10 and pdfmetrics.stringWidth(text, f, size) > maxw:
            size -= .5
        b.text(cx - pdfmetrics.stringWidth(text, f, size) / 2, y, text, size, bold, color)
        return
    lines = text.split()
    out, cur = [], ''
    for wd in lines:
        trial = (cur + ' ' + wd).strip()
        if pdfmetrics.stringWidth(trial, f, size) <= maxw or not cur:
            cur = trial
        else:
            out.append(cur)
            cur = wd
    if cur:
        out.append(cur)
    for ln in out:
        b.text(cx - pdfmetrics.stringWidth(ln, f, size) / 2, y, ln, size, bold, color)
        y += size + 4


def bullets(b, x, y, items, size=9.5, color=NAVY, gap=12, marker='•', mcolor=None, w=170):
    from reportlab.pdfbase import pdfmetrics
    for t in items:
        words = t.split()
        lines, cur = [], ''
        for wd in words:
            trial = (cur + ' ' + wd).strip()
            if pdfmetrics.stringWidth(trial, 'BM', size) <= w - 12 or not cur:
                cur = trial
            else:
                lines.append(cur)
                cur = wd
        if cur:
            lines.append(cur)
        if y > 224:
            break
        b.text(x, y, marker, size, True, mcolor or color)
        for ln in lines:
            if y > 222:
                break
            b.text(x + 8, y, ln, size, False, color)
            y += size + 3
        y += gap - (size + 3)
    return y


def title_page(b):
    b.start('BIJAK MATEMATIK', 'Edisi Khas Transisi ke Tahun 1 — Buku Panduan Ibu Bapa & Guru',
            'BUKU PANDUAN', NAVY, kind='cover')
    mascot(b, 84, 80, 46, 46, note=None)
    ctext(b, 105, 156, 'BIJAK MATEMATIK', 26, True, NAVY)
    ctext(b, 105, 178, 'Edisi Khas Transisi ke Tahun 1', 13, True, BLUE)
    ctext(b, 105, 196, 'Buku Panduan Ibu Bapa & Guru', 15, True, GREEN)
    ctext(b, 105, 214, 'Panduan untuk kanak-kanak 6–7 tahun', 9.5, False, GRAY)
    ctext(b, 105, 230, 'menghadapi alam persekolahan Tahun 1 dengan yakin.', 9.5, False, GRAY)
    b.finish()


def intro_page(b):
    b.start('Mengenal Buku Aktiviti BIJAK', 'Apa itu BIJAK MATEMATIK dan bagaimana ia membantu anak anda.',
            'BUKU PANDUAN', NAVY, kind='lesson')
    b.objective_line('Memahami tujuan dan struktur buku aktiviti BIJAK MATEMATIK.')
    y = bullets(b, 15, 62, [
        'BIJAK MATEMATIK ialah buku aktiviti untuk kanak-kanak 6–7 tahun yang bersedia memasuki Tahun 1.',
        'Buku ini merangkumi nombor, pengiraan asas, bentuk, arah, masa dan data — asas utama Tahun 1.',
        'Setiap unit bermula dengan objek dan gambar, kemudian beralih kepada nombor dan pengiraan.',
        'Anak tidak perlu menyiapkan semua aktiviti dalam satu hari. Kualiti lebih penting daripada kepantasan.',
    ])
    b.help_box(15, 246, 180, 'Gunakan buku ini sebagai teman pembelajaran, bukan ujian. Tujuannya ialah membina keyakinan dan kesediaan.')
    b.finish()


def principles_page(b):
    b.start('Prinsip Pembelajaran Matematik Awal', 'Prinsip yang diikuti oleh setiap aktiviti dalam buku ini.',
            'BUKU PANDUAN', BLUE, kind='lesson')
    b.objective_line('Memahami prinsip pembelajaran yang membentuk setiap aktiviti BIJAK.')
    y = bullets(b, 15, 62, [
        'Konkrit dahulu: anak belajar dengan benda sebenar, kemudian gambar, kemudian nombor.',
        'Tiada hafalan semata-mata: setiap konsep didahului dengan objek, gambar dan contoh langkah.',
        'Kira dengan sentuh: setiap objek disentuh sambil menyebut nombor untuk mengaitkan kuantiti dengan nombor.',
        'Satu langkah pada satu masa: aktiviti disusun dari mudah kepada mencakar secara beransur-ansur.',
        'Usaha didahului jawapan: puji cara pemikiran anak, bukan sekadar jawapan yang betul.',
    ], color=NAVY)
    b.tip(15, 246, 180, 'Jika anak sudah selesa dengan satu konsep, teruskan ke aktiviti seterusnya. Jika belum, ulang dengan objek sebenar.',
          BLUE, 'BIJAK NAK COUNTET')
    b.finish()


def routine_page(b):
    b.start('Routine Harian yang Mudah', 'Cadangan cara menggunakan buku aktiviti 15–20 minit sehari.',
            'BUKU PANDUAN', GREEN, kind='lesson')
    b.objective_line('Merancang rutin pembelajaran yang santai dan berkesan.')
    y = bullets(b, 15, 62, [
        'Pilih masa yang tenang — contohnya selepas sarapan atau sebelum tidur. 15–20 minit sudah memadai.',
        'Mulakan dengan membaca objektif aktiviti bersama anak, kemudian lakukan aktiviti secara berturut-turut.',
        'Gunakan objek di rumah untuk membantu pengiraan, terutama pada Unit B dan Unit D.',
        'Berhenti ketika anak masih berminat. Elakkan memaksa hingga anak rasa penat atau bosan.',
        'Semak jawapan bersama selepas aktiviti selesai, dan tandakan ★ di penjejak setiap aktiviti yang siap.',
    ], color=NAVY)
    b.help_box(15, 246, 180, 'Tiga hingga lima kali seminggu sudah cukup. Yang penting ialah anak merasa seronok setiap kali membuka buku.')
    b.finish()


UNITS = [
    ('A', 'Unit A • Permulaan Awal', 'Padanan, pengasingan, pengelasan, corak dan kedudukan.', BLUE,
     'Membina kemahiran awal pemikiran matematik sebelum nombor.',
     ['Bermain padanan: cari dua benda yang sama bentuk, warna atau jenis.',
      'Kumpulkan benda di rumah mengikut kategori (kutleri, mainan, buku).',
      'Cari corak sekitar rumah — warna, corak jubin, corak kain.',
      'Ajar kedudukan: atas, bawah, kiri, kanan, hadapan, belakang.'],
     ['Mana dua benda yang sama?',
      'Bentuk atau warna apa yang sama?',
      'Apakah corak yang seterusnya?',
      'Di manakah bola ini letak? (atas/bawah/kiri/kanan)'],
     'Jika anak keliru dengan kategori, turunkan kepada dua pilihan dahulu sebelum tiga atau empat.'),
    ('B', 'Unit B • Nombor 1 hingga 10', 'Mengira, membaca, menulis dan membandingkan nombor 1 hingga 10.', BLUE,
     'Membentuk asas kuantiti dan nombor 1 hingga 10.',
     ['Kira objek satu per satu sambil menyentuh setiap benda.',
      'Tunjuk nombor dan minta anak menyebut serta menulisnya.',
      'Ajarkan sifar sebagai "tiada" atau "kosong".',
      'Bandingkan dua kuantiti: lebih banyak, kurang, atau sama banyak.'],
     ['Berapa banyak benda ini?',
      'Nombor berapa ini? Boleh tulis?',
      'Nombor selepas 7 ialah?',
      'Kumpulan mana lebih banyak?'],
     'Jika anak tertinggal ketika mengira, latih kira dengan menyentuh dan menyebut perlahan. Gunakan jari atau objek sebenar.'),
    ('C', 'Unit C • Nombor 11 hingga 20', 'Mengenali struktur nombor belasan, menulis dan membandingkan.', GREEN,
     'Memperluas kefahaman nombor kepada 11 hingga 20.',
     ['Tunjuk bahawa 11 hingga 19 ialah "satu puluh dan beberapa sa".',
      'Ajarkan menulis nombor belasan dengan angka 1 di depan.',
      'Bandingkan dua nombor belasan: lihat angka belakang.',
      'Latih turutan 11 hingga 20 secara berturut-turut.'],
     ['11 bermaksud apa? (satu puluh satu)',
      'Nombor sebelum 15 ialah?',
      'Mana lebih besar, 17 atau 13?',
      'Tulis nombor 14 — mula dengan angka berapa?'],
     'Nombor belas sentiasa bermula dengan 1. Jika anak keliru, gunakan 10 objek + 1 hingga 9 objek untuk menunjukkan nilai.'),
    ('D', 'Unit D • Pengiraan', 'Part-part-whole, nombor gabungan, penambahan dan penolakan.', PURPLE,
     'Membentuk kefahaman pengiraan asas tambah dan tolak.',
     ['Ajarkan nombor gabungan 10: 7 dan 3, 6 dan 4, 5 dan 5.',
      'Tunjuk penambahan sebagai "gabung dua kumpulan".',
      'Tunjuk penolakan sebagai "buang" dan "bandingkan".',
      'Sediakan masalah cerita satu langkah menggunakan objek atau gambar.'],
     ['7 dan 3 menjadi berapa?',
      'Jika kita ada 5 epal dan tambah 2, berapa sekarang?',
      '8 tolak 3 tinggal berapa?',
      'Ada 4 biji gula-gula, makan 1, tinggal berapa?'],
     'Gunakan objek atau jari untuk setiap pengiraan. Jangan biarkan anak menghafal jawapan tanpa memahami prosesnya.'),
    ('E', 'Unit E • Matematik Harian', 'Bentuk, arah, panjang, saiz, masa dan data.', ORANGE,
     'Mengaitkan matematik dengan kehidupan harian.',
     ['Cari bentuk di rumah: bulatan pada clock, segi empat pada pintu.',
      'Main arahan arah: letak mainan di kiri, di atas, di belakang.',
      'Bandingkan panjang dan saiz objek sebenar.',
      'Bincangkan waktu harian: sarapan pukul 7 pagi, tidur pukul 8 malam.'],
     ['Bentuk apakah ini? Berapa bucu?',
      'Di manakah letak buku ini? (kiri/kanan/atas)',
      'Mana lebih panjang?',
      'Aktiviti apa yang kita lakukan pada waktu pagi?'],
     'Matematik harian paling berkesan apabila diajar dalam konteks sebenar, bukan sebagai latihan kertas semata-mata.'),
    ('F', 'Unit F • Kreativiti dan Keseronokan', 'Aktiviti kreatif untuk mengukuhkan pembelajaran.', YELLOW,
     'Menambahkan keseronokan dan mengukuhkan kefahaman melalui aktiviti kreatif.',
     ['Warnakan mengikut nombor untuk mengukuhkan pengenalan nombor.',
      'Ikut laluan nombor dalam maze untuk latihan turutan.',
      'Selesaikan teka-teki nombor secara santai.',
      'Guna kad nombor untuk permainan tambah dan tolak mudah.'],
     ['Nombor warna apa untuk ruang ini?',
      'Nombor apakah yang mengikut laluan ini?',
      'Nombor apakah yang tertinggal?'],
     'Gunakan aktiviti kreatif sebagai ganjaran selepas latihan utama, atau sebagai pengisi waktu yang menyeronokkan.'),
]


def unit_page(b, letter, title, sub, color, goal, help_tips, ask, difficulty):
    group = [it for it in REG if (it['category'][:2] == letter if letter == 'FA'
                                  else it['category'][0] == letter)]
    group.sort(key=lambda it: it['id'])
    b.start(title, sub, 'BUKU PANDUAN', color, kind='unit')
    b.objective_line(goal)
    b.para(15, 56, 'Aktiviti dalam unit ini:', 180, 10, NAVY, True)
    ids = ', '.join(it['id'] for it in group)
    b.text(18, 68, ids, 9, False, GRAY)
    b.text(15, 84, 'Cara membantu anak:', 10, True, color)
    bullets(b, 15, 94, help_tips, size=9.3, mcolor=color)
    b.tip(15, 246, 180, 'Sediakan objek sebenar di rumah untuk membantu anak memahami setiap konsep secara konkrit.',
          color, 'BIJAK NAK COUNTET')
    b.finish()
    b.start(title + ' — Soalan', 'Soalan untuk ditanya kepada anak during unit ini.',
            'BUKU PANDUAN', color, kind='lesson')
    b.text(15, 62, 'Soalan untuk ditanya:', 10, True, color)
    bullets(b, 15, 72, ask, size=9.5, mcolor=color)
    b.help_box(15, 246, 180, difficulty)
    b.check_strip(15, 266, 180, 'Unit ini selesai? Tandakan ★ di penjejak buku aktiviti.')
    b.finish()


def assessment_page(b):
    b.start('Pentaksiran Kesediaan', 'Cara menggunakan aktiviti pentaksiran (FA-1 hingga FA-3) dengan santai.',
            'BUKU PANDUAN', NAVY, kind='lesson')
    b.objective_line('Menilai kesediaan anak memasuki Tahun 1 tanpa tekanan.')
    y = bullets(b, 15, 62, [
        'Lakukan pentaksiran setelah semua unit selesai, bukan di awal buku.',
        'Beri anak persekitaran tenang dan masa yang cukup untuk setiap soalan.',
        'Catatkan jawapan anak secara kasar — tujuannya mengenal pasti kekuatan dan kelemahan.',
        'Jangan gred dengan tegas. Fokus pada kemahiran yang sudah ada dan yang perlu dilatih lagi.',
        'Jika anak tidak dapat menjawab, kembali ke unit yang berkaitan dan ulang aktiviti asas.',
    ], color=NAVY)
    b.help_box(15, 246, 180, 'Pentaksiran ini ialah penunjuk, bukan penentu. Setiap anak berkembang mengikut rentaknya sendiri.')
    b.finish()


def difficulty_page(b):
    b.start('Kesulitan Lazim dan Cara Membantu', 'Apa yang sering berlaku, dan apa yang boleh dilakukan.',
            'BUKU PANDUAN', ORANGE, kind='lesson')
    b.objective_line('Mengenal pasti kesulitan lazim kanak-kanak dan strategi bantuan.')
    rows = [
        ('Kira tertinggal atau laju',
         'Train kira dengan menyentuh setiap objek. Kurangkan kuantiti kepada 3–5 dahulu, kemudian tambah secara beransur.'),
        ('Menulis nombor terbalik',
         'Tunjuk contoh nombor yang betul dan latih menulis di atas garis berlapis. Banyakkan pujian untuk setiap percubaan.'),
        ('Keliru antara tambah dan tolak',
         'Gunakan objek: tambah ialah gabung dua kumpulan; tolak ialah buang atau bandingkan. Sentiasa berlaku objek sebenar.'),
        ('Tidak ingat nombor gabungan 10',
         'Amalkan secara kerap dengan permainan kad atau objek. 7 dan 3, 6 dan 4, 5 dan 5 — ulang sehingga anak selesa.'),
        ('Mudah hilang tumpuan',
         'Pendekkan masa kepada 10 minit. Gunakan aktiviti kreatif sebagai selingan, dan berhenti ketika anak masih seronok.'),
        ('Rasa bimbang salah',
         'Beri ruang untuk salah. Tanya "bagaimana kamu fikir?" dan raikan usaha mencari jalan, bukan sekadar jawapan betul.'),
    ]
    y = 60
    for title, tip in rows:
        b.box(15, y, 180, 26, ORANGE, tint=True)
        b.text(20, y + 6, title, 9.5, True, ORANGE)
        b.para(20, y + 13, tip, 172, 8.3, NAVY)
        y += 30
    b.finish()


def checklist_page(b):
    b.start('Checklist Ibu Bapa Mingguan', 'Catatan ringkas untuk setiap minggu pembelajaran.',
            'BUKU PANDUAN', GREEN, kind='lesson')
    b.objective_line('Mencatat perkembangan anak secara konsisten setiap minggu.')
    rows = ['Hari 1: aktiviti yang diselesaikan dan kekalsan utama.',
            'Hari 2: aktiviti yang diselesaikan dan kekalsan utama.',
            'Hari 3: aktiviti yang diselesaikan dan kekalsan utama.',
            'Hari 4: aktiviti yang diselesaikan dan kekalsan utama.',
            'Hari 5: aktiviti yang diselesaikan dan kekalsan utama.']
    y = 62
    for i, t in enumerate(rows, 1):
        b.text(15, y, f'Minggu {i}', 10, True, GREEN)
        b.box(70, y - 2, 120, 20, GRAY, tint=False, dash=True)
        b.text(74, y + 4, t, 8.5, False, GRAY)
        y += 28
    b.text(15, y + 2, 'Catatan tambahan:', 10, True, GREEN)
    b.box(70, y, 120, 60, GRAY, tint=False, dash=True)
    b.help_box(15, 246, 180, 'Checklist ini membantu anda melihat corak perkembangan dan menentukan fokus latihan pada minggu berikutnya.')
    b.finish()


def closing_page(b):
    b.start('Penutup', 'Setiap langkah kecil membawa anak lebih jauh.',
            'BUKU PANDUAN', NAVY, kind='lesson')
    mascot(b, 152, 60, 34, 34, note='Teruskan usaha!')
    y = bullets(b, 15, 108, [
        'Setiap anak mempunyai rentak pembelajaran sendiri. Bandingkan anak hari ini dengan anak semalam, bukan dengan orang lain.',
        'Apa yang anak telah pelajari dalam buku ini ialah asas yang kukuh untuk Tahun 1.',
        'Teruskan sikap positif terhadap nombor dan pengiraan — ia akan membentuk sikap anak terhadap matematik pada masa depan.',
        'Jika ada sebarang kesukaran yang berterusan, rujuklah kepada guru sekolah atau pakar perkembangan kanak-kanak.',
    ], color=NAVY, size=9.5)
    b.tip(15, 246, 180, 'Terima kasih kerana menyertai anak anda dalam perjalanan pertama ke alam persekolahan.',
          NAVY, 'BIJAK NAK COUNTET')
    b.finish()


def main():
    b = Book(BOOK, 'PTG', 'Buku Panduan')
    title_page(b)
    intro_page(b)
    principles_page(b)
    routine_page(b)
    for letter, title, sub, color, goal, help_tips, ask, difficulty in UNITS:
        unit_page(b, letter, title, sub, color, goal, help_tips, ask, difficulty)
    assessment_page(b)
    difficulty_page(b)
    checklist_page(b)
    closing_page(b)
    b.save()
    # Non-destructive export (keep pupil/answer registries intact)
    import json as _json
    from prod_engine import B as _B, PAGES_LOG as _PAGES, DOCS as _DOCS
    (QA / 'layout_03_guide.json').write_text(
        _json.dumps([e for e in _B.layout if e.get('file') == BOOK], ensure_ascii=False, indent=2))
    old_pages = _json.loads((QA / 'pages.json').read_text()) if (QA / 'pages.json').exists() else []
    merged_pages = [p for p in old_pages if p.get('file') != BOOK]
    merged_pages += [p for p in _PAGES if p.get('file') == BOOK]
    (QA / 'pages.json').write_text(_json.dumps(merged_pages, ensure_ascii=False, indent=2))
    old_docs = _json.loads((QA / 'documents.json').read_text()) if (QA / 'documents.json').exists() else {}
    old_docs.update(_DOCS)
    (QA / 'documents.json').write_text(_json.dumps(old_docs, ensure_ascii=False, indent=2))
    print(f'GUIDE BOOK DONE: {b.count} pages')


if __name__ == '__main__':
    main()

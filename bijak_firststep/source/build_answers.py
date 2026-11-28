#!/usr/bin/env python3
"""Build the BIJAK FirstStep Answer Book (Colony 11) from the item registry."""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from reportlab.pdfbase import pdfmetrics
from prod_engine import (MM, W, H, BLUE, ORANGE, GREEN, PURPLE, YELLOW, NAVY, GRAY,
                         white, Book)

QA = Path('../qa')
from content_helpers import mascot

REG = json.loads(Path('../data/item_registry.json').read_text())

UNITS = [
    ('A', 'Unit A • Permulaan Awal', 'Padanan, pengasingan, pengelasan, corak dan kedudukan.', BLUE),
    ('B', 'Unit B • Nombor 1 hingga 10', 'Mengira, membaca, menulis dan membandingkan nombor 1 hingga 10.', BLUE),
    ('C', 'Unit C • Nombor 11 hingga 20', 'Mengenali nombor belasan, menulis dan membandingkan.', GREEN),
    ('D', 'Unit D • Pengiraan', 'Part-part-whole, nombor gabungan, penambahan dan penolakan.', PURPLE),
    ('E', 'Unit E • Matematik Harian', 'Bentuk, arah, panjang, saiz, masa dan data.', ORANGE),
    ('F', 'Unit F • Kreativiti', 'Aktiviti kreatif untuk mencantikkan pembelajaran.', YELLOW),
    ('FA', 'Pentaksiran Kesediaan', 'Ujian kecil untuk melihat kesediaan ke Tahun 1.', NAVY),
]


def ctext(b, cx, y, text, size, bold, color, maxw=176):
    f = 'BM-Bold' if bold else 'BM'
    if pdfmetrics.stringWidth(text, f, size) <= maxw:
        b.text(cx - pdfmetrics.stringWidth(text, f, size) / 2, y, text, size, bold, color)
        return
    if bold:  # titles: shrink to a single line instead of wrapping
        while size > 10 and pdfmetrics.stringWidth(text, f, size) > maxw:
            size -= .5
        b.text(cx - pdfmetrics.stringWidth(text, f, size) / 2, y, text, size, bold, color)
        return
    lines = wrap(b, text, size, maxw)
    for ln in lines:
        b.text(cx - pdfmetrics.stringWidth(ln, f, size) / 2, y, ln, size, bold, color)
        y += size + 4


def wrap(b, text, size, width):
    """Greedy wrap using the registered font metrics."""
    f = 'BM-Bold'
    words = text.split()
    lines, cur = [], ''
    for wd in words:
        trial = (cur + ' ' + wd).strip()
        if pdfmetrics.stringWidth(trial, f, size) <= width or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = wd
    if cur:
        lines.append(cur)
    return lines


def title_page(b):
    b.start('BIJAK MATEMATIK', 'Edisi Khas Transisi ke Tahun 1 — Buku Jawapan',
            'BUKU JAWAPAN', NAVY, kind='cover')
    mascot(b, 84, 80, 46, 46, note=None)
    ctext(b, 105, 156, 'BIJAK MATEMATIK', 26, True, NAVY)
    ctext(b, 105, 178, 'Edisi Khas Transisi ke Tahun 1', 13, True, BLUE)
    ctext(b, 105, 196, 'Buku Jawapan', 15, True, GREEN)
    ctext(b, 105, 214, 'Jawapan lengkap untuk setiap aktiviti dalam buku aktiviti.', 9.5, False, GRAY)
    ctext(b, 105, 238, 'Untuk ibu bapa dan guru — simpan buku ini supaya jawapan tidak kelihatan oleh murid.',
          9, False, GRAY)
    b.finish()


def guide_page(b):
    b.start('Cara Menggunakan Buku Jawapan', 'Buku ini menyenaraikan jawapan untuk setiap aktiviti dalam buku aktiviti.',
            'BUKU JAWAPAN', NAVY, kind='lesson')
    tips = [
        'Setiap jawapan diberikan mengikut nombor aktiviti (contoh: A1-01, B3-02).',
        'Semak jawapan murid selepas setiap aktiviti selesai, bukan sebelumnya.',
        'Jika jawapan murid berbeza, tanya semula cara dia mengira sebelum menunjukkan jawapan.',
        'Tekankan pemahaman, bukannya menghafal. Pujilah usaha dan kemajuan murid.',
        'Jawapan kadang-kadang mempunyai lebih daripada satu cara yang betul — raikan cara yang logik.',
    ]
    y = 62
    for i, tip in enumerate(tips, 1):
        lines = wrap(b, tip, 9, 146)
        h = 22 + 10 * (len(lines) - 1)
        if y + h > 234:
            b.finish()
            b.start('Cara Menggunakan Buku Jawapan', 'Sambungan: cara menggunakan buku jawapan ini.',
                    'BUKU JAWAPAN', NAVY, kind='lesson')
            y = 62
        b.box(15, y, 20, 20, NAVY, tint=True)
        b.text(25, y + 7, str(i), 10, True, NAVY, 'center')
        for k, ln in enumerate(lines):
            b.text(45, y + 6 + k * 10, ln, 9, False, NAVY)
        y += h + 8
    b.help_box(15, 246, 180, 'Jawapan dalam buku ini dijana daripada daftar aktiviti yang telah disahkan (item registry).')
    b.finish()


def item_block(b, it, y):
    """Render one item answer block. Returns new y."""
    prompt_lines = wrap(b, it['prompt'], 8.5, 118)
    ans_text = 'Jawapan: ' + it['answer']
    ans_lines = wrap(b, ans_text, 8.5, 118)
    b.box(15, y, 54, 20, NAVY, tint=True)
    b.text(27, y + 6, it['id'], 10, True, NAVY, 'center')
    b.text(74, y + 6, it['objective'], 10, True, NAVY)
    yy = y + 16
    for ln in prompt_lines:
        b.text(74, yy, ln, 8.5, False, GRAY)
        yy += 10
    for ln in ans_lines:
        b.text(74, yy, ln, 8.5, False, GREEN)
        yy += 10
    return yy + 8


def main():
    b = Book('02_BIJAK_FirstStep_Answer_Book.pdf', 'JWB', 'Buku Jawapan')
    title_page(b)
    guide_page(b)
    state = {'y': 60}

    def ensure(h):
        if state['y'] + h > 240:
            b.finish()
            b.start('Jawapan Buku Aktiviti', 'Jawapan untuk setiap aktiviti, disusun mengikut unit.',
                    'JAWAPAN', NAVY, kind='lesson')
            state['y'] = 60

    for letter, title, sub, color in UNITS:
        group = [it for it in REG if (it['category'][:2] == letter if letter == 'FA'
                                       else it['category'][0] == letter)]
        if not group:
            continue
        group.sort(key=lambda it: it['id'])
        b.start(title, sub, 'JAWAPAN', color, kind='unit')
        mascot(b, 150, 60, 34, 34, note='Semak jawapan!')
        ctext(b, 105, 100, f'{len(group)} aktiviti dalam unit ini', 10, True, color)
        state['y'] = 116
        for it in group:
            h = 30 + 10 * (len(wrap(b, it['prompt'], 8.5, 118)) +
                           len(wrap(b, 'Jawapan: ' + it['answer'], 8.5, 118)))
            ensure(h)
            state['y'] = item_block(b, it, state['y'])
        b.finish()
    b.save()
    # Non-destructive export: keep the pupil registries intact; write the
    # answer-book ledger and merge page/document records only.
    import json as _json
    from prod_engine import B as _B, PAGES_LOG as _PAGES, DOCS as _DOCS
    ans = '02_BIJAK_FirstStep_Answer_Book.pdf'
    (QA / 'layout_02_answers.json').write_text(
        _json.dumps([e for e in _B.layout if e.get('file') == ans], ensure_ascii=False, indent=2))
    old_pages = _json.loads((QA / 'pages.json').read_text()) if (QA / 'pages.json').exists() else []
    merged_pages = [p for p in old_pages if p.get('file') != ans]
    merged_pages += [p for p in _PAGES if p.get('file') == ans]
    (QA / 'pages.json').write_text(_json.dumps(merged_pages, ensure_ascii=False, indent=2))
    old_docs = _json.loads((QA / 'documents.json').read_text()) if (QA / 'documents.json').exists() else {}
    old_docs.update(_DOCS)
    (QA / 'documents.json').write_text(_json.dumps(old_docs, ensure_ascii=False, indent=2))
    print(f'ANSWER BOOK DONE: {b.count} pages, {len(REG)} items covered')


if __name__ == '__main__':
    main()

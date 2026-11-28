#!/usr/bin/env python3
"""BIJAK MATEMATIK — Edisi Khas Transisi ke Tahun 1.

PRODUCTION ENGINE for Colony 11 (Mission COL-11-BIJAK-FIRSTSTEP-001).

Inherited from the frozen BIJAK Production Engine (sha256-pinned baseline in
engine/source/): the Book canvas class (mm coordinates, palette, box/text/para/
line/svg/eq/tag/dots primitives), the equation ledger, and the layout ledger.
See engine/BASELINE_SHA256.json for the immutable baseline record.

Newly developed in this mission: child-friendly components for ages 6-7
(ten frames, number lines, part-part-whole bars, shapes, stickers, tip boxes),
an original mascot (NOT the legacy tiger), and the item registry that powers
traceable answers.
"""
import sys
import math
from pathlib import Path

ENGINE = Path(__file__).resolve().parents[1] / 'engine' / 'source'
sys.path.insert(0, str(ENGINE))

import build_benchmark as B  # INHERITED: frozen engine publishing core
from reportlab.lib.colors import HexColor, Color, white
from reportlab.lib.utils import simpleSplit

MM = B.MM; W = B.W; H = B.H
BLUE = B.BLUE; ORANGE = B.ORANGE; GREEN = B.GREEN; PURPLE = B.PURPLE
YELLOW = B.YELLOW; NAVY = B.NAVY; GRAY = B.GRAY

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'pdf'
ASSET = ROOT / 'assets'
QA = ROOT / 'qa'
for p in (OUT, ASSET, ASSET / 'fonts', QA):
    p.mkdir(parents=True, exist_ok=True)

# Re-point the inherited engine's output/asset/QA paths at this mission's
# production tree (the same technique the engine's own core.py uses).
B.OUT = OUT
B.ASSET = ASSET
B.QA = QA

# The frozen engine materializes its own asset SVGs on import. The legacy
# tiger artwork is never rendered in any product page; remove it from the
# working asset tree so the production visual line stays tiger-free.
_legacy = ASSET / 'tiger_bijak.svg'
if _legacy.exists():
    _legacy.unlink()

# ---------------------------------------------------------------- registry
ITEMS = {}   # item registry: qid -> {id, objective, category, difficulty,
             # prompt, answer, page, refs, status, provenance}
PAGES_LOG = []

def reg(qid, objective, category, difficulty, prompt, answer, book=None,
        page=None, ref=None, status='VALIDATED', provenance='COL-11 authored'):
    entry = {
        'id': qid, 'objective': objective, 'category': category,
        'difficulty': difficulty, 'prompt': prompt, 'answer': str(answer),
        'status': status, 'provenance': provenance, 'refs': [],
    }
    if book is not None and page is not None:
        entry['refs'].append({'book': book, 'page': page})
    ITEMS[qid] = entry
    return entry

# ------------------------------------------------------------- book wrapper
class Book(B.Book):
    """Inherited engine Book + Colony 11 production components."""

    def color(self, h):
        # Shim: accept reportlab Color objects as well as hex strings,
        # so callers can pass either (the inherited engine expects hex).
        if hasattr(h, 'red'):
            return h
        return super().color(h)

    def __init__(self, name, code, label, ink=False):
        super().__init__(name, ink)
        self.code = code
        self.label = label
        self.count = 0
        self.c.setTitle('BIJAK MATEMATIK | ' + label)
        self.c.setAuthor('BIJAK MATEMATIK')

    # ---- page frame -------------------------------------------------
    def start(self, title, sub='', stage='JOM FAHAM', color=BLUE, kind='lesson'):
        self.count += 1
        self.page = self.count
        self.text(15, 20, 'BIJAK MATEMATIK', 9, True, color)
        self.text(195, 20, self.label.upper(), 7.2, False, GRAY, 'right')
        self.line(15, 24, 180, color)
        fs = 21
        from reportlab.pdfbase import pdfmetrics
        while pdfmetrics.stringWidth(title, 'BM-Bold', fs) > 178 * MM:
            fs -= .5
        self.text(15, 36, title, fs, True)
        if sub:
            self.para(15, 44, sub, 180, 9.2, GRAY)
        self.text(15, 281, self.code + '  /  ' + stage, 7.5, True, GRAY)
        self.text(195, 281, f'{self.page:02d}', 8, True, GRAY, 'right')
        PAGES_LOG.append({'file': self.name, 'page': self.page,
                          'title': title, 'kind': kind})

    def save(self):
        super().save()
        DOCS[self.name] = {'pages': self.count, 'code': self.code,
                           'label': self.label}

    # ---- components ------------------------------------------------
    def tip(self, x, y, w, text, color=PURPLE, title='BIJAK NAK COUNTET'):
        y = min(y, 252)  # keep inside content zone (footer at 276+)
        self.box(x, y, w, 24, color, tint=True)
        self.text(x + 4, y + 6, title, 8, True, color)
        self.para(x + 4, y + 13, text, w - 8, 8.2, NAVY)

    def help_box(self, x, y, w, text, color=ORANGE):
        y = min(y, 246)
        self.box(x, y, w, 30, color, tint=True, dash=True)
        self.text(x + 4, y + 6, 'JIKA PERLU BANTUAN', 8, True, color)
        self.para(x + 4, y + 13, text, w - 8, 8.2, NAVY)

    def check_strip(self, x, y, w, text):
        y = min(y, 260)
        self.box(x, y, w, 20, GREEN, tint=True)
        self.text(x + 4, y + 7, text, 8.5, True, GREEN)
        self.text(x + w - 22, y + 7, '□ □ □', 9, True, GREEN, 'right')

    def star_row(self, x, y, n=3, color=YELLOW):
        for i in range(n):
            self.star(x + i * 9, y, 3.4, color)

    def star(self, x, y, r, color=YELLOW):
        c = self.c
        c.saveState()
        c.setFillColor(self.color(color))
        c.setStrokeColor(self.color(NAVY))
        c.setLineWidth(.3)
        p = c.beginPath()
        for i in range(10):
            rr = r if i % 2 == 0 else r * 0.45
            a = math.radians(i * 36 - 90)
            px, py = x + rr * math.cos(a), y + rr * math.sin(a)
            if i == 0:
                p.moveTo(px * MM, H - py * MM)
            else:
                p.lineTo(px * MM, H - py * MM)
        p.close()
        c.drawPath(p, stroke=1, fill=1)
        c.restoreState()

    def sticker(self, x, y, r, color=BLUE, face=True):
        c = self.c
        c.saveState()
        c.setFillColor(self.color(color))
        c.setStrokeColor(self.color(NAVY))
        c.setLineWidth(.4)
        c.circle(x * MM, H - y * MM, r * MM, stroke=1, fill=1)
        if face:
            c.setFillColor(self.color(NAVY))
            c.circle((x - r * .35) * MM, H - (y - r * .15) * MM, r * .12 * MM, stroke=0, fill=1)
            c.circle((x + r * .35) * MM, H - (y - r * .15) * MM, r * .12 * MM, stroke=0, fill=1)
            c.setStrokeColor(self.color(NAVY))
            c.setLineWidth(.5)
            c.arc((x - r * .3) * MM, H - (y + r * .2) * MM,
                  (x + r * .3) * MM, H - (y - r * .45) * MM, 10, 80)
        c.restoreState()

    def shape(self, kind, x, y, s, color=BLUE):
        c = self.c
        c.saveState()
        c.setFillColor(Color(*self.color(color).rgb(), alpha=.35))
        c.setStrokeColor(self.color(color))
        c.setLineWidth(.8)
        if kind == 'circle':
            c.circle(x * MM, H - y * MM, s * MM / 2, stroke=1, fill=1)
        elif kind == 'square':
            c.rect(x * MM - s * MM / 2, H - (y + s / 2) * MM, s * MM, s * MM, stroke=1, fill=1)
        elif kind == 'triangle':
            p = c.beginPath()
            p.moveTo(x * MM, H - (y + s / 2) * MM)
            p.lineTo((x - s / 2) * MM, H - (y - s / 2) * MM)
            p.lineTo((x + s / 2) * MM, H - (y - s / 2) * MM)
            p.close()
            c.drawPath(p, stroke=1, fill=1)
        elif kind == 'rect':
            c.rect(x * MM - s * MM / 2, H - (y + s * .62) * MM, s * MM, s * MM * .62, stroke=1, fill=1)
        elif kind == 'star':
            p = c.beginPath()
            for i in range(10):
                rr = s / 2 if i % 2 == 0 else s / 4.2
                a = math.radians(i * 36 - 90)
                px, py = x + rr * math.cos(a), y + rr * math.sin(a)
                if i == 0:
                    p.moveTo(px * MM, H - py * MM)
                else:
                    p.lineTo(px * MM, H - py * MM)
            p.close()
            c.drawPath(p, stroke=1, fill=1)
        elif kind == 'heart':
            p = c.beginPath()
            p.moveTo(x * MM, H - (y - s * .3) * MM)
            p.curveTo((x - s * .9) * MM, H - (y + s * .5) * MM,
                      (x - s * .35) * MM, H - (y - s * .1) * MM,
                      x * MM, H - (y - s * .35) * MM)
            p.curveTo((x + s * .35) * MM, H - (y - s * .1) * MM,
                      (x + s * .9) * MM, H - (y + s * .5) * MM,
                      x * MM, H - (y - s * .3) * MM)
            p.close()
            c.drawPath(p, stroke=1, fill=1)
        c.restoreState()

    def big_num(self, x, y, n, size=22, color=BLUE, align='center'):
        self.text(x, y, str(n), size, True, color, align)

    def ten_frame(self, x, y, w, filled, total=10, color=BLUE, label=''):
        """Ten-frame component. x,y top-left; w = frame width in mm."""
        cell = (w - 6) / 2
        self.box(x, y, w, w * .82, color, tint=False)
        for r in range(2):
            for cidx in range(5):
                cx = x + 3 + cidx * cell
                cy = y + 3 + r * (cell * .82)
                on = filled > (r * 5 + cidx)
                self.c.setStrokeColor(self.color(GRAY))
                self.c.setLineWidth(.3)
                self.c.setFillColor(self.color(color) if on else white)
                self.c.rect(cx * MM, H - (cy + cell * .7) * MM,
                            cell * .7 * MM, cell * .68 * MM, stroke=1, fill=1)
        if label:
            self.text(x + w / 2, y + w * .82 + 6, label, 9, True, NAVY, 'center')

    def number_line(self, x, y, w, n_from, n_to, mark=None, color=NAVY,
                    jump=None, label=''):
        n = n_to - n_from + 1
        step = w / (n + 1)
        self.c.setStrokeColor(self.color(color))
        self.c.setLineWidth(.8)
        self.c.line(x * MM, H - y * MM, (x + w) * MM, H - y * MM)
        for v in range(n_from, n_to + 1):
            cx = x + step * (v - n_from + 1)
            hl = (mark is not None and v == mark)
            self.c.setStrokeColor(self.color(GREEN if hl else color))
            self.c.setLineWidth(1.2 if hl else .6)
            self.c.line(cx * MM, H - (y - 2) * MM, cx * MM, H - (y + 2) * MM)
            self.text(cx, y + 6, str(v), 9, hl, GREEN if hl else color, 'center')
        if jump:
            xs = x + step * (jump[0] - n_from + 1)
            xe = x + step * (jump[1] - n_from + 1)
            self.c.setStrokeColor(self.color(ORANGE))
            self.c.setLineWidth(1.6)
            self.c.line(xs * MM, H - (y - 5) * MM, xe * MM, H - (y - 5) * MM)
            self.c.setFillColor(self.color(ORANGE))
            self.c.circle(xs * MM, H - (y - 5) * MM, 1.6 * MM, stroke=0, fill=1)
            self.c.circle(xe * MM, H - (y - 5) * MM, 1.6 * MM, stroke=0, fill=1)

    def bond_bar(self, x, y, w, h, parts, colors=(BLUE, ORANGE), total=None):
        """Part-part-whole bar. parts = list of part values summing to total."""
        n = len(parts)
        seg = w / n
        for i, p in enumerate(parts):
            sx = x + i * seg
            self.c.setFillColor(Color(*self.color(colors[i % 2]).rgb(), alpha=.45))
            self.c.setStrokeColor(self.color(colors[i % 2]))
            self.c.setLineWidth(.7)
            self.c.rect(sx * MM, H - (y + h) * MM, seg * MM, h * MM, stroke=1, fill=1)
            self.text(sx + seg / 2, y + h / 2 + 3, str(p), 11, True,
                      colors[i % 2], 'center')
        if total is not None:
            self.text(x + w / 2, y + h + 8, str(total), 12, True, NAVY, 'center')

    def worked(self, x, y, w, lines, color=GREEN):
        """Worked example block: numbered steps."""
        self.box(x, y, w, 12 + len(lines) * 9.5, color, tint=True)
        self.text(x + 4, y + 7, 'CONTOH KERJA', 8, True, color)
        yy = y + 15
        for ln in lines:
            self.text(x + 4, yy, ln, 9.5, False, NAVY)
            yy += 9.5

    def objective_line(self, objective):
        self.text(15, 52, 'MATLAMAT: ' + objective, 8.5, False, PURPLE)

    def finish(self):
        self.c.showPage()

DOCS = {}

def export_registries():
    import json
    (QA / 'items.json').write_text(json.dumps(list(ITEMS.values()), ensure_ascii=False, indent=2))
    (QA / 'pages.json').write_text(json.dumps(PAGES_LOG, ensure_ascii=False, indent=2))
    (QA / 'equations.json').write_text(json.dumps(B.ledger, ensure_ascii=False, indent=2))
    (QA / 'layout.json').write_text(json.dumps(B.layout, ensure_ascii=False, indent=2))
    (QA / 'documents.json').write_text(json.dumps(DOCS, ensure_ascii=False, indent=2))
    (ROOT / 'data' / 'item_registry.json').write_text(
        json.dumps(list(ITEMS.values()), ensure_ascii=False, indent=2))

#!/usr/bin/env python3
"""Shared layout helpers for BIJAK FirstStep pupil content (Colony 11)."""
import math
from prod_engine import (MM, W, H, BLUE, ORANGE, GREEN, PURPLE, YELLOW,
                         NAVY, GRAY, white, Color, ITEMS, reg, Book)
from reportlab.lib.utils import simpleSplit
from reportlab.pdfbase import pdfmetrics

OBJ_SVG = {'epal': 'epal.svg', 'bola': 'bola.svg', 'buku': 'buku.svg',
           'pensel': 'pensel.svg'}

def obj_grid(b, x, y, total, per_row, gap_x=16, gap_y=16, size=12, names=None):
    """Draw `total` object SVGs in a grid. Returns bottom y."""
    names = names or ['epal']
    r, c = divmod(total, per_row)
    rows = r if total % per_row == 0 else r + 1
    for i in range(total):
        rr, cc = divmod(i, per_row)
        nm = names[i % len(names)]
        b.svg(OBJ_SVG[nm], x + cc * (size + gap_x), y + rr * (size + gap_y),
              size, size)
    return y + rows * (size + gap_y)

def dots_grid(b, x, y, total, per_row, step=9, r=2.6, split=None,
              color=BLUE, color2=ORANGE):
    """Dot array; split draws first `split` dots in color, rest in color2."""
    for i in range(total):
        rr, cc = divmod(i, per_row)
        col = color if split is None or i < split else color2
        b.c.setStrokeColor(b.color(col))
        b.c.setLineWidth(.5)
        b.c.setFillColor(white if b.ink else b.color(col))
        b.c.circle((x + cc * step) * MM, H - (y + rr * step) * MM, r * MM,
                   stroke=1, fill=1)
        if b.ink and split is not None and i >= split:
            b.c.setStrokeColor(b.color(NAVY))
            b.c.setLineWidth(.5)
            b.c.line((x + cc * step - r * .55) * MM, H - (y + rr * step - r * .55) * MM,
                     (x + cc * step + r * .55) * MM, H - (y + rr * step + r * .55) * MM)
    return y + math.ceil(total / per_row) * step

def trace_num(b, x, y, n, size=34, color=BLUE):
    """Large numeral with dashed guide box for tracing practice."""
    b.box(x, y, size + 10, size + 8, color, tint=False, dash=True)
    b.text(x + size / 2 + 5, y + size / 2 + 3, str(n), size, False, color,
           'center')

def write_nums(b, x, y, nums, size=12, gap=14, boxw=30, boxh=30):
    """Row of numerals to copy into boxes."""
    for i, n in enumerate(nums):
        b.box(x + i * (boxw + gap), y, boxw, boxh, GRAY, tint=False, dash=True)
        b.text(x + i * (boxw + gap) + 3, y + 5, str(n), 11, True, NAVY)

def write_lines(b, x, y, w, count=3, gap=9):
    """Dashed writing lines."""
    for i in range(count):
        b.line(x, y + i * gap, w, dash=True)

def match_row(b, x, y, w, left_items, right_items, row_h=30, kind='match'):
    """Matching layout: left column items, right column items, join lines."""
    n = len(left_items)
    lx = x
    rx = x + w * .55
    for i in range(n):
        yy = y + i * row_h
        # left item
        if isinstance(left_items[i], tuple):
            nm, label = left_items[i]
            b.svg(OBJ_SVG[nm], lx, yy + 4, 14, 14)
            if label:
                b.text(lx + 18, yy + 9, label, 9, False, NAVY)
        else:
            b.text(lx, yy + 9, left_items[i], 10, True, NAVY)
        # right item
        if isinstance(right_items[i], tuple):
            nm, label = right_items[i]
            b.svg(OBJ_SVG[nm], rx, yy + 4, 14, 14)
            if label:
                b.text(rx + 18, yy + 9, label, 9, False, NAVY)
        else:
            b.text(rx, yy + 9, right_items[i], 10, True, NAVY)
        # join line (dashed for child to draw)
        b.c.setStrokeColor(b.color(GRAY))
        b.c.setLineWidth(.4)
        b.c.setDash(2, 2)
        b.c.line(lx + 26 * MM, H - (yy + 11) * MM, rx * MM, H - (yy + 11) * MM)
        b.c.setDash()

def qbox(b, x, y, w=42, h=26, prompt='', size=10, color=BLUE, regid=None,
         objective=None, category=None, difficulty='Basic', answer=None):
    """A question box with prompt and writing space; registers item."""
    b.box(x, y, w, h, color, tint=False)
    if prompt:
        b.para(x + 3, y + h - 8, prompt, w - 6, size, NAVY)
    if regid:
        reg(regid, objective or '', category or '', difficulty, prompt,
            answer if answer is not None else '', book=b.name, page=b.page,
            status='VALIDATED')

def choice_row(b, x, y, options, prompt='', w=180, boxw=44, boxh=22, gap=8):
    """Multiple choice: prompt + option boxes."""
    if prompt:
        b.para(x, y, prompt, w, 10, NAVY)
        y += 14
    for i, opt in enumerate(options):
        b.box(x + i * (boxw + gap), y, boxw, boxh, GRAY, tint=False, dash=True)
        b.text(x + i * (boxw + gap) + 4, y + 8, opt, 10, False, NAVY)

def section_banner(b, x, y, w, text, color=ORANGE):
    b.box(x, y, w, 15, color)
    b.text(x + 6, y + 6, text, 11, True, white, 'left')

def mascot(b, x, y, w=34, h=34, note=None):
    b.svg('lebah_bijak.svg', x, y, w, h)
    if note:
        b.para(x, y + h + 5, note, min(95, 193 - x), 8.5, NAVY)

#!/usr/bin/env python3
"""Build the BIJAK FirstStep Pupil Activity Book (Colony 11)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from prod_engine import Book, export_registries
import content_pupil_a as A
import content_pupil_b as B
import content_pupil_c as C
import content_pupil_d as D
import content_pupil_e as E
import content_pupil_extra as X

def main():
    b = Book('01_BIJAK_FirstStep_Pupil_Book.pdf', 'PUPIL', 'Buku Aktiviti')
    # front matter
    A.cover(b)
    A.welcome(b)
    A.tracker_intro(b)
    # Unit A
    A.unit_a_intro(b)
    A.a_matching(b)
    A.a_matching2(b)
    A.a_sorting(b)
    A.a_sorting2(b)
    A.a_classify(b)
    A.a_patterns(b)
    A.a_spatial(b)
    A.a_review(b)
    # Unit B
    B.unit_b_intro(b)
    B.b_count1(b)
    B.b_count2(b)
    B.b_recognize(b)
    B.b_readwrite(b)
    B.b_trace(b)
    B.b_onetoone(b)
    B.b_zero(b)
    B.b_compare(b)
    B.b_compare2(b)
    B.b_order(b)
    X.bx_fill(b)
    B.b_review(b)
    # Unit C
    C.unit_c_intro(b)
    C.c_count11_20(b)
    C.c_teen_structure(b)
    C.c_readwrite(b)
    C.c_compare(b)
    C.c_order(b)
    X.cx_fill(b)
    C.c_review(b)
    # Unit D
    D.unit_d_intro(b)
    D.d_ppartwhole(b)
    D.d_bonds(b)
    D.d_add_intro(b)
    D.d_add_practice(b)
    D.d_sub_intro(b)
    D.d_sub_practice(b)
    D.d_sub_compare(b)
    D.d_word_problems(b)
    D.d_add_within20(b)
    D.d_sub_within20(b)
    X.dx_mixed(b)
    D.d_review(b)
    # Unit E
    E.unit_e_intro(b)
    E.e_shapes(b)
    E.e_shapes2(b)
    E.e_position(b)
    E.e_compare_measure(b)
    E.e_time(b)
    E.e_data(b)
    X.ex_practice(b)
    # creative
    E.creative_colour(b)
    E.creative_maze(b)
    E.creative_puzzle(b)
    E.creative_cutout(b)
    E.creative_spotdiff(b)
    # assessment + achievement
    E.final_assessment_1(b)
    E.final_assessment_2(b)
    E.achievement(b)
    b.save()
    export_registries()
    from prod_engine import ITEMS
    print(f'PUPIL BOOK DONE: {b.count} pages, {len(ITEMS)} items')

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Bina keseluruhan suite BIJAK MATEMATIK (10 PDF) + eksport registri QA."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))

from core import export_registries,QUESTIONS,PAGES,DOCS
import main_workbook as M
import materials as MAT
import games as G
import daily as D
import guide as GD
import tracker as T
import answers as A

def main():
	print('== Buku utama (color) ==')
	M.build_main(ink=False)
	print('== Buku utama (jimat dakwat) ==')
	M.build_main(ink=True)
	print('== Kad formula ==')
	MAT.build_formula()
	print('== Kad imbas ==')
	MAT.build_flash()
	print('== Poster ==')
	MAT.build_poster()
	print('== Permainan ==')
	G.build_games()
	print('== Latihan 30 hari ==')
	D.build_daily()
	print('== Penjejak ==')
	T.build_tracker()
	print('== Panduan dewasa ==')
	GD.build_guide()
	print('== Buku jawapan ==')
	A.build_answers()
	export_registries()
	print('Dokumen:')
	for name,meta in DOCS.items():
		print(f"  {name}: {meta['pages']} pages ({meta['code']})")
	print(f'Soalan berdaftar: {len(QUESTIONS)}')
	print(f'Halaman direkod: {len(PAGES)}')
	print('SELESAI.')

if __name__=='__main__':
	main()

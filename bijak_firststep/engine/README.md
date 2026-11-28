# BIJAK MATEMATIK — RAHSIA KUASAI SIFIR 1–12 (Pakej Penuh)

Siri pendidikan matematik Bahasa Melayu untuk murid umur 7–12 tahun, terutama yang masih bergelut dengan fakta sifir (contoh: Tahun 5).

**Tagline:** Faham Dahulu, Kira Dengan Bijak, Hafal Dengan Mudah!

Mascot: **TIGER BIJAK** (ilustrasi SVG asal, bukan aset pihak ketiga).

## Kandungan pakej (10 PDF)

| Fail | Halaman | Keterangan |
|------|---------|------------|
| `pdf/BIJAK_MATEMATIK_RAHSIA_SIFIR_COLOR.pdf` | 48 | Buku utama edisi warna |
| `pdf/BIJAK_MATEMATIK_RAHSIA_SIFIR_INKSAVING.pdf` | 48 | Buku utama edisi jimat dakwat (kandungan setara) |
| `pdf/BIJAK_MATEMATIK_KAD_FORMULA_SIFIR.pdf` | 13 | Kad poket, roda sifir, buku selak, kad segi tiga |
| `pdf/BIJAK_MATEMATIK_FLASHCARD_SIFIR.pdf` | 26 | 144 kad imbas dupleks (muka soalan + belakang jawapan) |
| `pdf/BIJAK_MATEMATIK_PERMAINAN_SIFIR.pdf` | 22 | 13 permainan + domino + kunci |
| `pdf/BIJAK_MATEMATIK_POSTER_SIFIR_1_12.pdf` | 2 | Poster peta sifir (warna + jimat dakwat) |
| `pdf/BIJAK_MATEMATIK_LATIHAN_30_HARI.pdf` | 32 | Kalendar + 30 helaian harian berpandu |
| `pdf/BIJAK_MATEMATIK_BUKU_JAWAPAN.pdf` | 69 | Semua jawapan mengikut kod soalan |
| `pdf/BIJAK_MATEMATIK_PANDUAN_IBU_BAPA.pdf` | 11 | Rujukan IES/EEF, rutin sesi, tafsiran saringan |
| `pdf/BIJAK_MATEMATIK_PROGRESS_TRACKER.pdf` | 11 | Penjejak G/K/I peribadi, log fakta, rekod penilaian |

## Struktur pembelajaran

- **FAHAM** → saringan 8 domain, kumpulan sama banyak, susunan, tukar tertib
- **KIRA** → 24 halaman (2 × setiap sifir 1–12): strategi visual, contoh, berpandu → sendiri → ingat
- **INGAT** → peta 12×12 (lengkap/kosong/penguasaan), simetri & kuasa dua, kit penyelamat fakta tumpuan
- **KUASAI** → matematik mental, kalendar 30 hari, penilaian akhir, refleksi

## Strategi yang diajar (bukan “petua ajaib”)

Identity, double, double+one, double twice, half ten, five+one, five+two, triple double, ten−one, place value ×10, ten+one, ten+two.

**Had jujur (dinyatakan dalam produk):**
- Tiada jaminan hafal dalam 30 hari
- Sela ulang ~1/3/7/14 hari = cadangan praktikal, bukan jadual optimum universal
- Jari ×9 hanya faktor 1–10; digit berulang ×11 hanya faktor satu digit
- Jumlah digit = alat semakan, bukan bukti ketepatan
- ×10 tambah sifar untuk nombor bulat sahaja dalam konteks buku ini
- Masa hanyalah pilihan selepas ketepatan & keyakinan; tiada perbandingan antara murid

## Cetak

- A4 potret, **100% / saiz sebenar**, tanpa “fit to page”
- Margin selamat ≥ 15 mm; nombor halaman & pengepala konsisten
- Font DejaVu disemat (lihat `assets/fonts/`)
- Kad imbas: cetak dupleks **balik pada sisi panjang (long-edge)**; uji helaian 3–4 dahulu
- Potongan: gunting dengan pengawasan dewasa

## Sumber boleh ubah

```
source/   penjana Python (ReportLab) — semua kandungan dijana secara program
assets/   SVG asal (tiger_bijak, epal, pensel) + fon DejaVu + lesen
templates/ design_system.json, lesson_template.json, templat_halaman.svg
qa/       registri soalan, persamaan, geometri, laporan pengesahan, render bukti
RUJUKAN.md  petikan penuh IES (2007) & EEF (2017) + pemetaan halaman
```

Jana semula:

```bash
python source/build_all.py      # bina 10 PDF + eksport registri QA
python source/validate_full.py  # 3,600+ semakan bebas + render bukti
```

## Pengesahan

- **3,682/3,682** semakan automatik LULUS (`qa/validation_report.json`)
- Semak: identiti 12 strategi, 144 keluarga fakta, ledger persamaan, kontrak soalan, labirin/kerkunci permainan, geometri dupleks kad, kalendar sela, sempadan 15 mm, metadata PDF, kesamaan teks dua edisi, liputan Buku Jawapan
- Halaman PDF dirender dan disemak secara visual (27 helaian bukti dalam `qa/renders/`)
- **Bukan** ujian cetakan fizikal, ujian dengan murid, pensijilan keberkesanan, atau PDF/A

## Rujukan pembelajaran

1. Pashler, H. et al. (2007). *Organizing Instruction and Study to Improve Student Learning*. IES NCER 2007-2004. https://ies.ed.gov/ncee/wwc/practiceguide/1
2. Education Endowment Foundation (2017). *Improving Mathematics in Key Stages Two and Three*. https://dera.ioe.ac.uk/id/eprint/30457/1/KS2_KS3_Maths_Guidance_2017.pdf

Lihat `RUJUKAN.md` untuk pemetaan halaman dan had tafsiran.

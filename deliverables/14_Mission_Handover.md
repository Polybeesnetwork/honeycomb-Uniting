# 14 — Mission Handover

**Mission:** COL-11-BIJAK-FIRSTSTEP-001 · **Arm:** Engine Inheritance · **Colony:** 11
**Product:** BIJAK MATEMATIK — Edisi Khas Transisi ke Tahun 1 (subtitle: Langkah Pertama Menuju Alam Persekolahan)
**Status:** Production complete · QA complete · **NOT SEALED** — unpublished candidate pending Colonel approval and independent verification

## 1. What is delivered

A complete premium educational publication package for Malaysian children aged 6–7 preparing
for Year 1, in natural Bahasa Melayu Malaysia:

- **Pupil activity book** (62 A4 pages, within the 60–90 target): Unit A pre-number
  foundations; Unit B numbers 1–10; Unit C numbers 11–20; Unit D calculation (part-part-
  whole, bonds to 10, addition/subtraction within 10 then 20, word problems); Unit E
  everyday maths (shapes, directions, length/size, time, data); Unit F creative activities;
  readiness assessment (FA-1..FA-3); achievement certificate; star tracker.
- **Answer book** (52 pages): every one of the 62 registered activities answered.
- **Parent/teacher guide** (20 pages): usage routine, learning principles, per-unit
  guidance with questions to ask, assessment guidance, difficulty register, weekly checklist.
- **Reports and manifests** (05–14) with SHA-256 hashes and verification evidence.

## 2. Where things live

```
deliverables/                        — the 14 authoritative deliverables
bijak_firststep/engine/              — frozen BIJAK engine baseline (immutable, 21/21 sha256)
bijak_firststep/source/              — production engine + content modules + build scripts
bijak_firststep/assets/              — mascot and object SVGs + font licence note
bijak_firststep/pdf/                 — build outputs (01–03)
bijak_firststep/qa/                  — QA ledgers (layout, pages, items, documents, per-book ledgers)
bijak_firststep/data/item_registry.json — the 62-item registry
```

## 3. How to rebuild

```bash
cd /home/user/honeycomb-Uniting
.venv/bin/python3 bijak_firststep/source/build_pupil.py     # 01 (62 pages, 62 items)
.venv/bin/python3 bijak_firststep/source/build_answers.py   # 02 (52 pages)
.venv/bin/python3 bijak_firststep/source/build_guide.py     # 03 (20 pages)
```

Builds take ~1.0 s / 0.3 s / 0.3 s respectively. QA ledgers are re-exported at build time;
answer/guide builds export non-destructively so the pupil registry is never overwritten.

## 4. How to verify

1. **Hashes:** compare deliverable SHA-256 values in 07 / 10 against the committed files
   (`sha256sum`); read back via `git show <rev>:deliverables/<file>`.
2. **QA:** the 20-check table in 07 records PASS / MANUAL REVIEW / NOT TESTED with evidence.
   Final layout state: 0 margin violations, 0 significant text overlaps.
3. **Open items requiring a human/independent party:**
   - Visual page review (07 check 16 — MANUAL REVIEW; the producing agent has no image-vision).
   - Curriculum alignment sign-off against primary DoE documents (07 check 17 — MANUAL REVIEW).
   - Independent SENTINEL verification before any SEAL (07 check 20 — NOT TESTED).

## 5. Constraints honoured

- Founder-authorized frozen BIJAK Production Engine executed as the baseline; no unauthorized
  historical content loaded; contamination disclosed (11).
- No internal codes, colony names or technical jargon on pupil pages; no answer leakage
  (verified by rendered-text scans, 07 checks 9–10).
- Calculation taught through concrete → pictorial → symbolic understanding, never
  memorization alone.
- No fabricated validation results; unavailable metrics recorded as UNAVAILABLE.
- No other colony's workspace or outputs touched.

## 5.1 Final hash record

13_Harvest_Report.md embeds a hash table and is self-referential; its final SHA-256 is:

`76268d986521e53a49da82682b8d563ab823150d6dad2523b92c55f6de65ae23`

## 6. Sign-off line

Product is submitted as an **unpublished candidate**. Awaiting: (a) Colonel review and
approval; (b) independent verification; (c) SEALED decision made only after such verification.

# 09 — Defect and Limitation Register

**Mission:** COL-11-BIJAK-FIRSTSTEP-001 · **Arm:** Engine Inheritance · **Generated:** 2026-11-28

## 1. Defects found and fixed

| ID | Defect | Severity | Round | Root cause | Fix | Status |
|----|--------|----------|-------|------------|-----|--------|
| D-01 | 15 right-edge margin violations (pupil book) | Medium | 1 | Components (tip/help_box/check_strip) and content rows drawn past printable right edge | Component clamp zones in `prod_engine.py`; 5-number rows re-laid as 2×5 stacks; 3-column compare layouts redesigned to 2 columns | FIXED |
| D-02 | 39 bottom-edge margin violations | Medium | 1 | Components drawn below the content zone into the footer area | tip clamped ≤252, help_box ≤246, check_strip ≤260 (content zone above footer at 276+) | FIXED |
| D-03 | 19 text overlaps (footer collisions, mascot note overflow, choice marks on instruction lines) | Medium | 1–2 | Note text placed beside mascot (past right edge); footer text too low; choice-mark boxes overlapping instruction text | Mascot note repositioned below mascot with right clamp; cover footer raised; instruction/choice rows repositioned; achievement page number moved into zone | FIXED |
| D-04 | `b.para()` argument-order bug in 4 calls (missing width argument) | High (build-blocking) | 1 | Inherited signature `para(x, y, text, w, size, color, bold)` called with 5 args | Width argument inserted; build completes | FIXED |
| D-05 | Latent engine shim bugs (NameError on H/W, missing `import math`, colour TypeError on reportlab Color objects, `star()` moveTo assertion, SVG asset path) | High (build-blocking) | 1 | Production engine adaptation incomplete | All fixed in `prod_engine.py` | FIXED |
| D-06 | Answer/guide builds clobbered the pupil item registry (`ITEMS` empty in fresh engine import) | High (data-integrity) | 2 | `export_registries()` writes from shared module state; answer/guide builds have no content-module `reg()` calls | Registry restored from snapshot; answer/guide builds now export non-destructively (ledger + merged pages/documents only) | FIXED |
| D-07 | Unfinished pages at unit boundaries in the answer book (51 starts vs 45 rendered pages) | Medium | 2 | `b.finish()` not called at end of each unit loop | `b.finish()` added at each unit boundary | FIXED |
| D-08 | Answer-book title page centered text overflowed left margin; guide bullets overflowed into help/tip components | Medium | 2–3 | Over-wide single-line centered text; bullet line count underestimated | Titles shrink-to-fit single line; bullets rewritten with per-line clamp at y≤222 | FIXED |
| D-09 | Extra-practice pages (62-page expansion) overflowed the right edge; two tip/strip collisions | Medium | 3 | 9–10 number sequences laid in a single row; tips placed on the same baseline as check strips | Sequences re-laid 5-per-row; pair rows and tips repositioned | FIXED |

**Final state:** 0 margin violations, 0 significant text overlaps across all three books
(verified by deterministic layout-ledger QA).

## 2. Limitations (disclosed, not fixable within this environment)

| ID | Limitation | Impact | Mitigation |
|----|-----------|--------|------------|
| L-01 | Agent has **no image-vision capability**; rendered pages could not be visually inspected | Visual QA (alignment, aesthetics, glyph rendering) cannot be performed directly | Deterministic layout-ledger QA (bounding-box margin/overlap checks over 2,691 recorded text boxes) substituted and documented; listed as MANUAL REVIEW where visual judgement is required (07 checks 16) |
| L-02 | **No primary Malaysian DoE curriculum document** was accessible | No official curriculum alignment claim can be made | Secondary sources used and disclosed in 05; alignment claim marked MANUAL REVIEW (07 check 17) |
| L-03 | **Independent SENTINEL verification not performed** | SEALED status cannot be claimed | SEALED recorded as NOT TESTED (07 check 20); package is an unpublished candidate pending Colonel approval |
| L-04 | Historical engine package contains embedded historical intelligence (Tiger artwork, font binaries, historical multiplication content) | Potential contamination if used as-is | Tiger artwork and font binaries excluded from the build; multiplication content replaced with mission-authored transition content; disclosed in 11 |
| L-05 | PDF byte-level reproducibility not guaranteed | Hashes differ across rebuilds due to embedded timestamps | Page/item-count reproducibility verified; per-build hashes recorded in 10 |
| L-06 | Answer-leakage scan is string-based | A numeric answer that coincidentally matches page text could be missed | Scan performed against rendered PDF text for every registry answer; AR-02 false positive explained in 07 |
| L-07 | Upload/read-back target is the colony Git repository (no external publishing channel in this environment) | "Upload" interpreted as committing to the mission branch | Deliverables committed to branch `arena/70663e3b-honeycomb-uniting`; read-back verified via git |

## 3. Outstanding (deliberately not fixed)

- None. All build-blocking and layout defects are resolved. The package remains an
  **unpublished candidate** pending Colonel (human founder) approval and independent
  verification before any SEAL.

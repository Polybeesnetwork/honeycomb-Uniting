# 07 — Quality Assurance Report

**Mission:** COL-11-BIJAK-FIRSTSTEP-001 · **Arm:** Engine Inheritance · **Generated:** 2026-11-28

**Status policy:** every check is recorded as PASS, FAIL, MANUAL REVIEW, NOT TESTED or
INSUFFICIENT EVIDENCE. Skipped checks never count as PASS. SEALED is **not claimed** —
self-verification is not independent SENTINEL verification.

**Overall: 17 PASS · 2 MANUAL REVIEW · 1 NOT TESTED · 0 FAIL**

## Mandatory 20-check QA

| # | Check | Method / evidence | Result |
|---|-------|-------------------|--------|
| 1 | SWRMP storage entry gate | Measured workspace usage at gate: 132 KB / 35 files (~0.1% of limit) | **PASS** |
| 2 | Frozen engine baseline integrity | 21/21 engine files sha256-verified against HARVEST_MANIFEST.json; locked in `engine/` + `BASELINE_SHA256.json` | **PASS** |
| 3 | Engine actually executed (inheritance utilization) | All three PDFs generated through inherited `build_benchmark.Book` via `prod_engine.py` at build time — not merely read | **PASS** |
| 4 | Unauthorized content excluded | Only the 21 frozen engine files used; `qa/*.json` audit data not downloaded; no SME23 / TUALANG / historical audits / other-colony outputs touched | **PASS** |
| 5 | Pupil book page count within 60–90 | 62 A4 pages | **PASS** |
| 6 | Item registry ↔ pages consistency | 62 registered items across 62 pages; `qa/pages.json` logs every page with title/kind | **PASS** |
| 7 | Answer book coverage | 62/62 registry items answered in `02_BIJAK_FirstStep_Answer_Book.pdf` (52 pages) | **PASS** |
| 8 | Parent/teacher guide completeness | 20 pages: intro, principles, routine, per-unit guides, assessment guidance, difficulty register, weekly checklist | **PASS** |
| 9 | Language & no internal codes on pupil pages | Rendered-text scan of pupil PDF for colony/mission/engine jargon: **NONE found** | **PASS** |
| 10 | No answer leakage in pupil book | Rendered-text scan of pupil PDF against every registry answer string: no content answers found. One false-positive candidate AR-02 — its answer is the choice-mark glyph "□", which coincides with the generic check-strip checkbox glyph used on every page; not a content leak | **PASS** |
| 11 | Layout margin QA | Deterministic ledger QA over 2,691 text bounding boxes (1,319 pupil + 907 answer + 465 guide): 0 left, 0 right, 0 top, 0 bottom violations | **PASS** |
| 12 | Text overlap QA | Significant-overlap detection across all three books: 0 overlaps | **PASS** |
| 13 | PDF integrity & page counts | All three PDFs open cleanly with pymupdf; page counts match `qa/documents.json` (62 / 52 / 20) | **PASS** |
| 14 | Font embedding | DejaVuSans and DejaVuSans-Bold embedded (subset) in all three PDFs; Helvetica is a standard base-14 font | **PASS** |
| 15 | No decorative emoji substituting math illustrations | Rendered-text scan: only ★/☆ appear, used as activity/tracking marks; math illustrations use SVG assets, canvas drawings and dot grids | **PASS** |
| 16 | Concept structure (objective, visual, worked example, guided + independent practice, assistance, mastery check) | Structure authored per unit and verified in content modules; visual rendering could not be independently reviewed (no image-vision) | **MANUAL REVIEW** |
| 17 | Curriculum alignment claim | Secondary sources only; primary DoE document not accessible from this environment — limitations recorded in 05 | **MANUAL REVIEW** |
| 18 | Build reproducibility | Repeat builds reproduce identical page/item counts (62/62, 52/62, 20) and clean QA; PDF byte-stability not guaranteed due to embedded timestamps | **PASS** |
| 19 | SHA-256 manifests + upload/read-back | All 14 deliverables hashed; committed to the mission branch and read back via git (see hash table below) | **PASS** |
| 20 | SEALED status | Requires independent verification by a second party; self-verification does not qualify | **NOT TESTED** |

## Defect summary (full register in 09)

- **Round 1 (first layout QA):** 15 right-edge, 39 bottom-edge margin violations; 19 text
  overlaps → fixed via component clamp zones, mascot repositioning, row/column redesigns,
  cover footer raise.
- **Round 2:** 0/0/0/2 margin violations; 13 overlaps → fixed (choice-mark spacing,
  instruction-line repositioning, footer-adjacent collisions, number-box relocation).
- **Round 3 (post expansion to 62 pages):** right-edge overflows on the four new practice
  pages and two tip/strip collisions → fixed (5-per-row sequences, tip repositioning).
- **Final state:** 0 margin violations, 0 significant overlaps across all three books.

## Deliverable hash table (SHA-256)

Hashes computed over the final bytes of each deliverable at packaging time.

| Deliverable | SHA-256 | Bytes |
|---|---|---|
| `01_BIJAK_FirstStep_Pupil_Book.pdf` | `1724037b6f46375582a980bd6069529e738294235b8bd3e438934d791635fbc2` | 240021 |
| `02_BIJAK_FirstStep_Answer_Book.pdf` | `e47318109ce5021eff0ed2fa569d3b637522a899be320a7d69769786466d948e` | 127299 |
| `03_BIJAK_FirstStep_Parent_Teacher_Guide.pdf` | `0dd61e641531c8ceeddbb792a7e0006ec03e37a1c53d832ebd4b1316770fd122` | 80451 |
| `04_Source_And_Assets.zip` | `7cfb89d5c121705c505b4d252189a269232c5e3b3d1c2542f3a83b294e8a3420` | 872067 |
| `05_Curriculum_And_Skill_Mapping.md` | `9157a6dd4bec1151b437fdd6e834120321f0113356d7be08b7ab6409c8ce0557` | 6323 |
| `06_Production_Methodology.md` | `aad0ee08b11baa67589a5afd4daecd8d3d96ba893c73d0dc0c9884b14d199d86` | 5095 |
| `07_Quality_Assurance_Report.md` | self-referential (embeds this table) — final hash in 13_Harvest_Report.md | 5160 |
| `08_Item_Registry.json` | `d9cf764024e8b6c4efedfa349e0ba6411972f55beba4acb8b7427cb44cfb938b` | 28440 |
| `09_Defect_And_Limitation_Register.md` | `6b6d9824ee7ec1012af276d9566c9bdc99274dba65e65a498b05ea818439399f` | 5294 |
| `10_Asset_And_Build_Manifest.json` | `0f1a3510d9dc9d4da14e92b946aa85e807713dd8e381f1cc6828f5678d9c59da` | 8483 |
| `11_Inheritance_Manifest.json` | `5f0ee6b39ce8743d4f20269108d545df6b894c6e3175f64a7d0618526efb4aa4` | 4608 |
| `12_Experimental_Performance_Report.json` | `a93eedb110ffdb6ebf71278a44751f099eec0ad847b46cebc954a1f1541f31c3` | 2903 |
| `13_Harvest_Report.md` | `17f69065dbef77e66af80bad9392bb6535869e33646e4b30e2b7058c13b5cb5c` | 2784 |
| `14_Mission_Handover.md` | `e3ae0d52d408d202d521f8d7f15caf149742dd7bdf59eba037cdc131eb9d41eb` | 3877 |

## Verification notes

- QA was performed by the producing agent using deterministic ledger checks and text-based
  scans. It is **self-verification** and does not constitute independent SENTINEL verification.
- Visual inspection of rendered pages was not possible (no image-vision capability); the
  deterministic layout-ledger QA is the documented substitute.

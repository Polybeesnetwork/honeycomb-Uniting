# 06 — Production Methodology

**Mission:** COL-11-BIJAK-FIRSTSTEP-001 · **Arm:** Engine Inheritance · **Generated:** 2026-11-28

## 1. Protocol stages executed

| Stage | What was done | Evidence |
|-------|---------------|----------|
| GENESIS | Read SWARM DNA, SOG entry gate, mission allocation; confirmed COL-11 authorization and the Engine Inheritance arm | HIVE root, START_HERE.md, AGENTS.md, UNIVERSAL_DNA.md, UHCP.md, 06_MISSION_ALLOCATION |
| SPAWN | Created the colony-specific mission workspace tree `bijak_firststep/` (engine/, source/, assets/, pdf/, qa/, data/, reports/) inside the authorized repository | Workspace layout |
| FORAGE | Confirmed Malaysian Year-1/transition maths scope from secondary sources; retrieved the founder-authorized frozen BIJAK Production Engine (21 files, sha256-verified) | Section 2 sources (see 05), engine/BASELINE_SHA256.json |
| SYNTHESIS | Designed unit structure and activity taxonomy; authored all child-facing content in Bahasa Melayu Malaysia | `source/content_pupil_*.py`, `source/content_helpers.py` |
| PRODUCTION | Executed the production engine to build the three PDFs; registered every activity in the item registry | Build logs, `qa/items.json`, `data/item_registry.json` |
| REFINEMENT | Iterative layout QA on the engine's deterministic layout ledger; fixed all margin violations and text overlaps; added extra practice pages to reach the 60–90 page target | `qa/layout*.json`, 07 QA report |
| SEAL | Not claimed. Sealing requires independent verification (see 07 check 20) | — |
| HARVEST | Packaged deliverables 01–14 with hashes, manifests and handover | This package |

## 2. Engine inheritance method (actually executed)

1. **Recovery:** Downloaded the 21 source files of the frozen BIJAK Production Engine from the
   founder-authorized Drive folder (`1ACmLpCpx-d5IJJxULeqoH_2PpoA6tpfI`). `qa/*.json` historical
   audit data was **deliberately excluded** per Inheritance Policy §03.
2. **Integrity lock:** All 21 files sha256-verified against `HARVEST_MANIFEST.json` (21/21
   match) and locked immutably in `bijak_firststep/engine/` with `BASELINE_SHA256.json`.
3. **Execution (not mere reading):** `source/prod_engine.py` imports the frozen
   `build_benchmark.Book` and extends it with mission-specific components and registries,
   re-pointing output paths at the mission tree (the same technique the engine's own
   `core.py` uses). Every page of all three PDFs was rendered **through the inherited engine**.
4. **Contamination handling:** Tiger artwork and font binaries in the historical package were
   excluded from the build. The historical multiplication content was replaced with
   age-appropriate transition content authored for this mission. All of this is disclosed in
   `11_Inheritance_Manifest.json`.

## 3. Content authoring method

- **Language:** natural Bahasa Melayu Malaysia throughout; no internal codes, colony names or
  technical jargon on pupil pages (verified by rendered-text scan — see 07).
- **Structure per major concept:** objective → intuitive concrete introduction → accurate
  visuals (SVG assets / canvas drawings / dot grids) → genuine worked example → step-by-step
  explanation → guided practice → independent practice → targeted assistance (tip /
  help-box components) → mastery check (review items and pentaksiran).
- **No memorization-only:** calculation concepts are grounded in objects, dot grids,
  ten-frames and number lines before symbolic practice.
- **Registry-driven:** every activity calls `reg()` with objective, category, difficulty,
  prompt and answer, producing the item registry that drives the answer book.

## 4. Build pipeline

```
build_pupil.py   → 01_BIJAK_FirstStep_Pupil_Book.pdf        (62 pages, 62 items)
build_answers.py → 02_BIJAK_FirstStep_Answer_Book.pdf      (52 pages, driven by item registry)
build_guide.py   → 03_BIJAK_FirstStep_Parent_Teacher_Guide.pdf (20 pages)
```

- Environment: Python 3.11 venv; reportlab 5.1.2; svglib; pymupdf (QA/rendering only).
- Build times (measured): pupil 1.04 s, answers 0.34 s, guide 0.29 s.
- QA ledgers exported at build time: `qa/layout.json`, `qa/layout_02_answers.json`,
  `qa/layout_03_guide.json`, `qa/pages.json`, `qa/documents.json`, `qa/items.json`.
- Answer/guide builds export **non-destructively**: the pupil item registry is never
  overwritten by downstream builds.

## 5. Quality assurance method

Because this agent has **no image-vision capability**, visual QA is substituted with
deterministic checks over the engine's layout ledger (`qa/layout*.json`, which records every
text bounding box):

- margin violations (left/right/top/bottom against the printable zone),
- significant text-overlap detection (intersection area > threshold),
- PDF integrity and page-count verification (pymupdf),
- rendered-text scans for jargon, answer leakage and decorative symbols,
- font-embedding inspection.

Three QA rounds were run on the pupil book; the final state of all three books is
**0 margin violations and 0 significant text overlaps**. Details in 07.

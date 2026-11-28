# 13 — Harvest Report

**Mission:** COL-11-BIJAK-FIRSTSTEP-001 · **Arm:** Engine Inheritance · **Generated:** 2026-11-28
**Protocol:** STRATA GENESIS · **Colony:** 11 (Swarm Protocol) · **Status:** harvest complete; product remains an unpublished candidate pending Colonel approval

## 1. What was harvested

| # | Deliverable | Description |
|---|-------------|-------------|
| 01 | `01_BIJAK_FirstStep_Pupil_Book.pdf` | Pupil activity book — 62 A4 pages, 62 registered activities, Bahasa Melayu Malaysia |
| 02 | `02_BIJAK_FirstStep_Answer_Book.pdf` | Complete answer book — 52 pages, all 62 registry items answered |
| 03 | `03_BIJAK_FirstStep_Parent_Teacher_Guide.pdf` | Parent/teacher guide — 20 pages |
| 04 | `04_Source_And_Assets.zip` | Frozen engine baseline + mission source + assets for rebuild |
| 05 | `05_Curriculum_And_Skill_Mapping.md` | Skill mapping + curriculum sources with access limitations |
| 06 | `06_Production_Methodology.md` | Protocol stages, engine inheritance method, build pipeline |
| 07 | `07_Quality_Assurance_Report.md` | 20-check mandatory QA (17 PASS, 2 MANUAL REVIEW, 1 NOT TESTED, 0 FAIL) |
| 08 | `08_Item_Registry.json` | Machine-readable registry of all 62 activities with answers |
| 09 | `09_Defect_And_Limitation_Register.md` | 9 defects found-and-fixed; 7 disclosed limitations |
| 10 | `10_Asset_And_Build_Manifest.json` | Asset hashes, build commands, outputs, QA artifacts |
| 11 | `11_Inheritance_Manifest.json` | Engine inheritance record + contamination disclosure |
| 12 | `12_Experimental_Performance_Report.json` | Measured build/QA performance metrics |
| 13 | `13_Harvest_Report.md` | This report |
| 14 | `14_Mission_Handover.md` | Handover record |

## 2. Harvest verification

- **SHA-256 hashes** computed over the final bytes of every deliverable (table in 07 and 10).
- **Upload/read-back:** all 14 deliverables committed to the mission branch
  `arena/70663e3b-honeycomb-uniting` in repository `Polybeesnetwork/honeycomb-Uniting`;
  read-back verified via `git` (tree listing + object hashes).
- **Build evidence:** the three PDFs were produced by executing the inherited engine;
  `qa/pages.json` (134 entries) and `qa/documents.json` (3 documents) record the build outputs.

## 2.1 Final deliverable hashes (SHA-256)

| Deliverable | SHA-256 |
|---|---|
| `01_BIJAK_FirstStep_Pupil_Book.pdf` | `1724037b6f46375582a980bd6069529e738294235b8bd3e438934d791635fbc2` |
| `02_BIJAK_FirstStep_Answer_Book.pdf` | `e47318109ce5021eff0ed2fa569d3b637522a899be320a7d69769786466d948e` |
| `03_BIJAK_FirstStep_Parent_Teacher_Guide.pdf` | `0dd61e641531c8ceeddbb792a7e0006ec03e37a1c53d832ebd4b1316770fd122` |
| `04_Source_And_Assets.zip` | `7cfb89d5c121705c505b4d252189a269232c5e3b3d1c2542f3a83b294e8a3420` |
| `05_Curriculum_And_Skill_Mapping.md` | `9157a6dd4bec1151b437fdd6e834120321f0113356d7be08b7ab6409c8ce0557` |
| `06_Production_Methodology.md` | `aad0ee08b11baa67589a5afd4daecd8d3d96ba893c73d0dc0c9884b14d199d86` |
| `07_Quality_Assurance_Report.md` | `b540b2512659ac1b095e774a1e9cc3e584b13d054d0f9ab4d377d9dde2277a26` |
| `08_Item_Registry.json` | `d9cf764024e8b6c4efedfa349e0ba6411972f55beba4acb8b7427cb44cfb938b` |
| `09_Defect_And_Limitation_Register.md` | `6b6d9824ee7ec1012af276d9566c9bdc99274dba65e65a498b05ea818439399f` |
| `10_Asset_And_Build_Manifest.json` | `0f1a3510d9dc9d4da14e92b946aa85e807713dd8e381f1cc6828f5678d9c59da` |
| `11_Inheritance_Manifest.json` | `5f0ee6b39ce8743d4f20269108d545df6b894c6e3175f64a7d0618526efb4aa4` |
| `12_Experimental_Performance_Report.json` | `a93eedb110ffdb6ebf71278a44751f099eec0ad847b46cebc954a1f1541f31c3` |
| `13_Harvest_Report.md` | self-referential (embeds this table) — final hash recorded in 14_Mission_Handover.md |
| `14_Mission_Handover.md` | `e3ae0d52d408d202d521f8d7f15caf149742dd7bdf59eba037cdc131eb9d41eb` |

## 3. Governance statements

- The frozen BIJAK Production Engine was used **only** as the founder-authorized baseline,
  executed in the workflow; no unauthorized historical intelligence was merged into the
  child-facing content (contamination disclosed in 11).
- Mandatory 20-check QA was performed with honest statuses; **SEALED is not claimed** —
  independent verification remains outstanding (07 check 20).
- The product is an **unpublished candidate**. Final decision authority rests with the
  Colonel (human founder).

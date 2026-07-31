# SingCLOUD — NUHS HFSI

| | |
|---|---|
| **Status** | ⚪ Stub |
| **Profiled on** | 2026-07-23 |
| **Last reviewed** | *not yet reviewed* |

**Objects included in this page**

| # | Object | Prefix |
|---:|---|---|
| 1 | `VW_NUHS_HFSI_F_Export_22-07-2024.csv` | `PriorityTables-B1/` |
| 2 | `VW_NUHS_HFSI_F_Export_30-10-2024.csv` | `FreeText_FTA/` |
| 3 | `VW_NUHS_HFSI_F_Export_30-10-2024.csv` | `Updated_HFSI/` |

All prefixes relative to `common-data/SingCLoud/`. Three objects, none partitioned.

## Read this first

| | Issue | What to do |
|---|---|---|
| 🔴 | **Three copies of one dataset, not three partitions.** Objects 2 and 3 share an extract date, 575 columns and 68.49% missing — but differ by 4 rows and 52 MB | Never sum across them. Pick one copy; ask the owner which is authoritative |
| 🔴 | **No patient identifier found** in the ~65 columns read. `RECORD_ID` is REDCap's record key, not a patient ID | Do not substitute `RECORD_ID`. Check whether a patient column exists at all before planning any linkage |
| 🟡 | **This is a REDCap export**, so probably longitudinal — one row per record *per event* | Test whether `RECORD_ID` repeats before treating row counts as patient counts |
| 🟡 | **Schema changed between extracts** — 572 columns in July, 575 in October | Any analysis spanning both must handle 3 columns that did not exist earlier |
| 🟡 | **`PriorityTables-B1/` appears to hold copies, not originals** — it contains only this object and `VW_SCDB_HF_F`, and both are duplicated elsewhere | Confirm before treating anything under that prefix as canonical |
| 📋 | **~510 of 575 column names not transcribed** | Ask for the **REDCap data dictionary** — it documents every column at once, with descriptions |

---

## Dataset Overview

**Category:** NUHS HFSI — taken from the dataset name. Not yet confirmed against a data
dictionary or the data owner. **What `NUHS` and `HFSI` stand for is unknown.**

**Description:** Unknown — to be filled in.

**Data source:** Unknown — to confirm with data owner.

**Population:** Unknown — to confirm with data owner. At 47,805 rows across 575 columns, this
is the widest and one of the smallest datasets in the catalogue — the shape of a study cohort
or registry rather than a system-wide extract. That is a guess and is not adopted.

**Institutional / geographic coverage:** Unknown — to confirm with data owner.

**Unit of observation:** **Unknown — to confirm with data owner.** The presence of
`REDCAP_EVENT_NAME` (see *Key Variables*) points to one row per record *per study event*
rather than one row per patient, which would mean `RECORD_ID` repeats. Not tested, and not
adopted — but it must be settled before any row count here is read as a patient count.

**Rows vs people:** 47,805 rows in the largest copy (profiler, 2026-07-23); distinct patients
**not counted**. Do not sum across the three objects — see the warning above.

**What is *not* in it:** Unknown — to be filled in.

### Access

| | |
|---|---|
| **Catalogue alias(es)** | Unknown — to be filled in |
| **Source object(s)** | Three copies under three prefixes — see the object table above |
| **Partitions** | None. All three objects are unpartitioned |
| **Extract date** | Two dates: `22-07-2024` (one copy) and `30-10-2024` (two copies). **`30-10-2024` is the latest extract date in the entire profiler run** |
| **Format** | CSV by file extension. Delimiter and encoding unknown |
| **Refresh cadence** | Unknown — to confirm with data owner. That a `30-10-2024` extract exists alongside a `22-07-2024` one shows the dataset *is* refreshed; the interval is not established |
| **Free-text content** | Unknown. One copy sits under `FreeText_FTA/`, the others do not — the same data filed under two different content classifications |

---

## Key Variables

**Most column names are outstanding.** Roughly 65 of 575 have been transcribed and appear
below; the object's report block runs some 15,000 pixels, more than a full screenshot
section.

**What is established:** the objects declare 575 columns (copies 2 and 3) and 572 columns
(copy 1). **The three-column difference between the July and October extracts is itself a
finding** — the schema changed between them, and which three columns were added is not known.

**Outstanding for every column:** name, type, missing %, Description, Class, Coding / units,
Sensitivity.

### Columns transcribed so far — ~65 of 575

Fill Description, Class, Coding / units and Sensitivity in pass 2.

| # | Variable | Type | Missing % | Description | Class | Coding / units | Sensitivity | Description | Class | Coding / units | Sensitivity |
|---:|---|---|---:|---|---|---|---|---|---|---|---|
| 1 | `DATA_SOURCE` | categorical | 0.0 | | | | | | | | |
| 2 | `RECORD_ID` | numeric | 0.0 | | | | | | | | |
| 3 | `REDCAP_EVENT_NAME` | categorical | 0.0 | | | | | | | | |
| 4 | `REDCAP_DATA_ACCESS_GROUP` | categorical | 0.01 | | | | | | | | |
| … | `MAIN_CAREGIVER___3` … `___9` | numeric | 8.05 | | | | | | | | |
| … | `OTHER_MAIN_CAREGIVER` | categorical | 99.09 | | | | | | | | |
| … | `HEIGHT` | numeric | 44.21 | | | | | | | | |
| … | `WEIGHT` | numeric | 52.26 | | | | | | | | |
| … | `BMI` | numeric | 54.84 | | | | | | | | |
| … | `LVEF_DATE_V2_X` / `_Z` | date | 82.58 | | | | | | | | |
| … | `LVEF_V2` | numeric | 82.57 | | | | | | | | |
| … | `NYHA_6MTHLY` | numeric | 74.40 | | | | | | | | |
| … | `NYHA_1` | numeric | 89.16 | | | | | | | | |
| … | `VISITS_COMPLETE` | numeric | 8.05 | | | | | | | | |
| … | `CO_MORBID_CONDITIONS___1` … `___16` | numeric | 77.11–77.40 | | | | | | | | |
| … | `CO_MORBID_HISTO` | categorical | 98.28 | | | | | | | | |
| … | `OTHER_CO_MORBID` | categorical | 81.76 | | | | | | | | |
| … | `PAST_MEDICAL_HISTORY1___1` … `___16` | numeric | 77.25–77.40 | | | | | | | | |
| 5–575 | *remaining columns not yet transcribed* | | | | | | | | | | |

*(missing %; profiler, 2026-07-23. Ordinals are unknown for the fragment — the block was read
mid-table.)*

**Notes on this schema**

- **REDCap export.** Columns 3 and 4 are REDCap's own metadata, so this is a study instrument,
  hand-entered on a case report form — not a clinical system extract.
- **`___N` suffix = checkbox expansion.** One column per option, which is why
  `CO_MORBID_CONDITIONS` fills sixteen columns sharing one missing percentage. Much of the 575
  width is this, not 575 distinct concepts.
- **`REDCAP_DATA_ACCESS_GROUP` is an access-control field** — usually the owning site or team.
  The export may span groups whose upstream permissions differ.
- **Resolved:** a cardiac-catheterisation block (`LPA1_SAT`, `OCXLAB`, `SEPTLAB` …) sits at a
  damaged join in `section_04.png` and was briefly thought to be this family. It is
  **`VW_NUHCS_ECHO_D`** (270,906 rows × 371 columns) — identified by the full screenshot sweep
  of 2026-07-31, which read the object order either side of the seam. It is covered by
  [the dimension index](singcloud-dimension-tables-index.md), not by this page.

> **Value strings drift between extracts** (`SINGAPORE PINK IC` vs `SINGAPORE PINK NRIC`).
> This page lists no values for any column. Enumerate the distinct values in your own extract
> before filtering, and re-check them against each new extract — a value string that has
> drifted returns zero rows without raising an error.

---

## Time Coverage

| Date column | Start | End | Source |
|---|---|---|---|
| `LVEF_DATE_V2_X` | Unknown | Unknown | |
| `LVEF_DATE_V2_Z` | Unknown | Unknown | |
| *other date columns not yet transcribed* | | | |

- No date range established; no principal date column identified.
- **Date format:** Unknown. The profiler parses `dayfirst=True`, so `01/02/2021` reads as
  1 February. A month-first column would produce wrong dates silently.

**Completeness over the period:** Unknown.

**Variable availability over time** — partly established: the schema grew from 572 to 575
columns between the July and October extracts. Which three columns, and from when they are
populated, is unknown.

| Variable | Usable from | Evidence |
|---|---|---|
| *3 columns added Oct 2024 — identify them* | | July copy has 572 cols, October 575 |
| | | |

---

## Dataset Information

*Transcribed from the condensed profiler summary, run 2026-07-23.*

| Object | Prefix | Size (MB) | Rows | Cols | Overall missing % |
|---|---|---:|---:|---:|---:|
| `VW_NUHS_HFSI_F_Export_22-07-2024.csv` | `PriorityTables-B1/` | 78.24 | 32,480 | 572 | 64.08 |
| `VW_NUHS_HFSI_F_Export_30-10-2024.csv` | `FreeText_FTA/` | 59.57 | 47,805 | 575 | 68.49 |
| `VW_NUHS_HFSI_F_Export_30-10-2024.csv` | `Updated_HFSI/` | 111.97 | 47,801 | 575 | 68.49 |

*Every row count above is a lower bound: the profiler reads with `on_bad_lines="skip"`
([tools/s3_data_catalog.py](../tools/s3_data_catalog.py)), so unparseable lines are dropped
silently and never counted.*

**No family total is given, deliberately.** These are three copies of one dataset. Summing
their rows would count the same records two or three times, and summing their sizes would
describe a storage footprint rather than a dataset.

**The two October copies differ by exactly four rows and by 52 MB.** A 4-row difference on
47,800 rows is too small to be a different cohort and too large to be nothing. The size gap is
the more striking of the two: near-identical row and column counts, nearly double the bytes.
That is the signature of a different serialisation — different quoting, encoding or column
widths — rather than different content, but nothing here establishes it.

| Metric | Value |
|---|---|
| Sample size (distinct patients) | **not counted** — the profiler does not compute it |
| Schema consistent across copies | **No.** 572 columns in the July copy, 575 in both October copies |

---

## Provenance & Processing

Every field here is owner-only, and none is inferred from column naming.

**Collection mechanism:** Unknown — to confirm with data owner.

**Who enters it, and under what incentive:** Unknown — to confirm with data owner. A
575-column table at 47,805 rows, 68.49% empty, is the shape of a case report form rather than
a transactional extract — which would make it hand-entered, with all that implies for
completeness. Not established.

**Extract pipeline:** Unknown — to confirm with data owner. The three-prefix arrangement is
itself the pipeline question: the same object name appears under `FreeText_FTA/`,
`Updated_HFSI/` and `PriorityTables-B1/`, and no source available here explains what those
locations mean or which is canonical.

**Processing applied:** Unknown — to confirm with data owner.

**Standardisation mappings:** Unknown — column names are not established.

**Transformations at load:** Unknown. Inspect `df.columns` after loading.

**Raw vs interpreted — what is lost:** Unknown.

**Identifier handling:** Unknown — to confirm with data owner.

---

## Data Quality

### Missingness

| Metric | Value |
|---|---|
| Overall missing (share of all cells) | 64.08% (July copy), 68.49% (both October copies) |
| Columns >50% missing | Unknown — per-column figures not transcribed |
| Columns 100% missing | Unknown — per-column figures not transcribed |

- **Missingness rose between extracts** — 64.08% → 68.49%, while the schema gained 3 columns
  and 15,325 rows. Adding sparse columns would do that without any field worsening; not
  established either way.

**Columns that matter** *(fill in pass 2)*:

| Variable | Missing % | Consequence if unusable |
|---|---:|---|
| | | |

**Disguised missing:** **Not checked.**

- Profiler counts only `""`, `NA`, `N/A`, `NULL`, `null`, `None`, `NaN`, `.` as missing.
- `UNKNOWN`, `NIL`, `9`, `999`, `1900-01-01` all read as *present* — invisible in these figures.
- Run `value_counts()` before trusting any 0.0% figure.

- Profiler counts only `""`, `NA`, `N/A`, `NULL`, `null`, `None`, `NaN`, `.` as missing.
- On a REDCap case report form, coded "not assessed" / "not applicable" values are
  conventional — every one would be counted as *present*. Higher risk here than on most pages.
- Run `value_counts()` before trusting any 0.0% figure.

### Overlap

**Primary identifier:** **Not yet established.** The patient ID column is the primary
identifier for every dataset in this catalogue, but no patient column has been found among the
~65 transcribed so far. `RECORD_ID` is REDCap's study record key, not a patient identifier —
do not substitute it. Whether a patient column exists further into the 575 is an outstanding
transcription task, not an exception to the convention; contrast
[Laboratory Dim](singcloud-laboratory-dim.md), where the object genuinely has no patient
column at all.

**If no patient identifier exists in this export, that is itself an important finding** —
it would mean the dataset cannot be linked to any other family in the catalogue.

**Identifier family:** Unknown — to confirm with data owner.

**Secondary keys:** Unknown.

**Coding standards:** Unknown — to confirm with data owner.

| Links to | On | Granularity | Cardinality | Overlap tested? | Notes |
|---|---|---|---|---|---|
| Unknown | Unknown | Unknown | Unknown | **no join tested** | No linkage established. Nothing can be proposed until the column list is transcribed |

**Known linkage pitfalls:** None recorded — no linkage has been attempted. An empty list, not
a clean bill of health.

### Bias

- **Coverage / selection:** Unknown — to confirm with data owner. For a dataset of this shape
  and size, who gets in is the first question.
- **Recording practice:** Unknown — to confirm with data owner.
- **Changes over time:** **Partly visible.** The schema changed between the July and October
  extracts. Any analysis spanning both must account for three columns that did not exist in
  the earlier one.
- **Ascertainment:** Unknown — to confirm with data owner.

### Other limitations

- **Duplicates:** **Confirmed at object level.** Two near-identical October copies and an
  earlier July copy. Row-level duplication within any single copy has not been checked.
- **Schema drift:** 572 columns against 575 between extracts.
- **Value-range anomalies:** Not checked.
- **Encoding:** Unknown. The profiler attempts UTF-8 and falls back to latin-1 with
  `errors="replace"` silently. The 52 MB size gap between two otherwise-identical copies makes
  encoding a live question here rather than a formality.
- **Damaged source screenshot:** the block that should carry this family's header sits at a
  stitch seam in `section_04.png`. See *Key Variables*.
- **Column names outstanding:** all 575. This is the largest single transcription job left in
  the catalogue.
- **Fitness for purpose:** **Cannot be assessed yet.**

---

## Ownership & Governance

| | |
|---|---|
| **Data owner** | Unknown — to confirm with data owner |
| **Steward / contact** | Unknown — to confirm with data owner |
| **Access restrictions** | Unknown — to confirm with data owner |
| **Approval requirements** | Unknown — to confirm with data owner |
| **Typical lead time** | Unknown — to confirm with data owner |
| **Permitted use / conditions** | Unknown — to confirm with data owner |
| **Sensitivity classification** | Unknown — to confirm with data owner |
| **Free-text / PII exposure** | **Not assessed, and not assessable yet** — no column of this family has been transcribed, so there is nothing to classify. Two structural facts still bear on it: the dataset is small (47,805 rows) and very wide (575 columns), and a cohort of that shape carries higher re-identification risk than a million-row transactional table, because a combination of a few dozen attributes is close to unique. And it exists in three copies under three prefixes, so any access control applied to one location does not necessarily cover the others. Absence of a classification here is an outstanding task, **not** a finding that the dataset carries no PII |
| **Attribution / citation** | Unknown — to confirm with data owner |

**Open questions for the data owner:**

1. **Which of the three copies is authoritative?** Two share an extract date and differ by four
   rows and 52 MB.
2. **Why do the two `30-10-2024` copies differ by four rows?** Which four, and why?
3. Why is one copy 111.97 MB and the other 59.57 MB with the same shape? Different encoding,
   quoting or line endings?
4. What are the `Updated_HFSI/` and `PriorityTables-B1/` prefixes for? Does
   `PriorityTables-B1/` hold copies rather than originals — it contains only this object and
   `VW_SCDB_HF_F`, and both are duplicated elsewhere.
5. Do the access conditions differ by prefix? If one copy is more restricted than another,
   that needs stating.
6. **What do `NUHS` and `HFSI` stand for?**
7. **Which three columns were added between the July and October extracts?**
8. **Is there a patient identifier column anywhere in the 575?** `RECORD_ID` is REDCap's
   record key, not a patient ID. If none exists, this dataset cannot be linked to any other
   family — which needs stating prominently.
9. Is the table longitudinal — one row per record per `REDCAP_EVENT_NAME` — so that
   `RECORD_ID` repeats?
10. What does `REDCAP_DATA_ACCESS_GROUP` contain, and do its values correspond to sites or
    teams with different permissions?
11. Can the REDCap data dictionary for this instrument be supplied? It would document all 575
    columns at once, including which are checkbox expansions.
12. What is the unit of observation?
9. Which population is included, and who is excluded by what mechanism?
10. Is there a data dictionary? All 575 columns are undescribed, and at this width a page
    cannot be completed without one.
11. Which column is the patient identifier?
12. Is the data hand-entered on a case report form? If so, what completeness rules apply?
13. Does the block of `_SAT` and `*LAB` columns following Laboratory Item FIL in the report
    belong to this family? Its header was lost to a damaged screenshot.
14. What is the refresh cadence? Two extracts three months apart are visible.
15. What is the delimiter and file encoding for each copy?
16. Who is the data owner and steward role, what is the approval route, and what lead time
    should a study plan for?

---

## Appendix A — Full column profile

**Roughly 65 of 575 columns transcribed** — the header block and a study-instrument fragment,
both in *Key Variables*. The report block for a single copy runs some 15,000 pixels, more than
one full screenshot section, so completing it is the largest remaining transcription job in
the catalogue.

**The REDCap data dictionary would be a shortcut.** This is a REDCap export, so the instrument
definition already documents every column — name, type, and the checkbox expansions that
account for much of the width. Obtaining it would complete this appendix in one step and would
do it better than transcription, since it also supplies descriptions.

## Appendix B — Change log

| Date | Change | By |
|---|---|---|
| 2026-07-31 | Page created against `template.md` from the profiler run of 2026-07-23. Three objects inventoried with object-level figures; identified as three copies of one dataset rather than three partitions, with a schema change between the July and October extracts. Header block and a ~60-column study fragment transcribed; identified as a REDCap export. An earlier tentative attribution of a cardiac-catheterisation column block to this family was checked and **retracted** — see *Key Variables*. Category from the dataset name. Primary identifier not yet nameable. | CCJX |

## Appendix C — Sources

- **Profiler run 2026-07-23** — object-level figures for all three objects. The header block
  of the July copy and the study-instrument column fragment were read from
  `source_material/screenshots/mass_columns_screenshots/section_25.png`.
- **`section_04.png` carries a stitch seam** where two scrolled captures were joined,
  swallowing the separator, path, size and column-header lines of the object following
  `VW_LABORATORY_ITEM_FIL_F_Export_28-07-2024_P2.csv`. That block was briefly considered as a
  candidate for this family and has since been ruled out. It remains unidentified, and is
  probably one of the ~68 objects the reconstruction index does not cover. This is the second
  seam found in the screenshot set; the first is in `section_17.png` and affects
  [MED Billing](singcloud-med-billing.md). A clean re-capture of both regions would resolve
  them.
- `tools/s3_data_catalog.py` — cited only for the profiler's documented behaviour, never for
  any property of this dataset.
- **Not used for column names:** `source_material/imported/profiler_report_full.txt` and
  `column_summary.csv`. For this family the reconstruction is at its least reliable — of 556
  names it recovers, only 40 achieve a majority across the three copies, so it cannot supply
  even a provisional column list.
- **Data owner correspondence — none.** Every governance field on this page is unconfirmed.

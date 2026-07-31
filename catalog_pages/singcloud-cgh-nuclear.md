# SingCLOUD — CGH Nuclear

| | |
|---|---|
| **Status** | ⚪ Stub |
| **Profiled on** | 2026-07-23 |
| **Last reviewed** | *not yet reviewed* |

**Objects included in this page**

| # | Object |
|---:|---|
| 1 | `VW_CGH_NUCLEAR_F_Export_22-07-2024.csv` |

Under the prefix `common-data/SingCLoud/FreeText_FTA/`. One object, 4,387 rows, 12 columns.

**This is the smallest object in the run and it is not partitioned** — there is no `_P{n}`
suffix, so the single file is the whole of what was profiled.

---

## Read this first

| | Issue | What to do |
|---|---|---|
| 🔴 | **Every column reports 0.0% missing.** That is also what a sentinel-filled extract looks like | Run `value_counts()` before treating this as complete data |
| 🔴 | **Quasi-identifiers at small N** — `Gender`, `Race`, `Date_of_Birth_X` in only 4,387 rows | Re-identification risk is structurally higher here than in the million-row families. Confirm release conditions first |
| 🟡 | **Column names are mixed-case** (`Gender`, `Order_Id`, `Text`), unlike every other family | Copy character for character; an upper-case query will not match |
| 🟡 | **Patient column is `PATIENT_ID_X`**, not `PATIENT_ID_EXTN_X` as elsewhere | Do not assume it is the same identifier space |
| 🟡 | **`Text` profiles as `id_like`** — over half its values hold >7 digits | Not what a column named `Text` should contain. Inspect early |

---

## Dataset Overview

**Category:** CGH nuclear — taken from the dataset name. Not yet confirmed against a data
dictionary or the data owner. What `CGH` and `nuclear` denote here is unconfirmed.

**Description:** Unknown — to be filled in.

**Data source:** Unknown — to confirm with data owner.

**Population:** Unknown — to confirm with data owner. At 4,387 rows this is four orders of
magnitude smaller than the billing and laboratory families, which makes the inclusion
criterion the single most useful thing to establish about it.

**Institutional / geographic coverage:** Unknown — to confirm with data owner.

**Unit of observation:** **Unknown — to confirm with data owner.**

**Rows vs people:** 4,387 rows (profiler, 2026-07-23, single object); distinct patients **not
counted**.

**What is *not* in it:** Unknown — to be filled in. The 12 column names in *Key Variables* are
the complete column list.

### Access

| | |
|---|---|
| **Catalogue alias(es)** | Unknown — to be filled in |
| **Source object(s)** | `common-data/SingCLoud/FreeText_FTA/VW_CGH_NUCLEAR_F_Export_22-07-2024.csv` |
| **Partitions** | 1 object, unpartitioned |
| **Format** | CSV by file extension. Delimiter and encoding unknown |
| **Extract date** | Unknown. The object name contains `_Export_22-07-2024` |
| **Refresh cadence** | Unknown — to confirm with data owner |
| **Free-text content** | Unknown. The object sits under a path segment named `FreeText_FTA`, and one column is named `Text` |

---

## Key Variables

All 12 columns, in the order printed in the report. Row count matches Appendix A.

**Type** is the profiler's label and is provisional until pass 2.

**Outstanding until pass 2, for every column:** Description, Class, Coding / units,
Sensitivity. Every column here is unclassified.

**Note the casing.** Unlike every other SingCLOUD family in this run, this object's column
names are mixed-case (`Gender`, `Race`, `Date_of_Birth_X`, `Order_Id`, `Case_No`,
`Order_Name`, `Result_Name`, `Text`) rather than upper-case. Copy them character for
character; a query written in upper case will not match.

| # | Variable | Type | Missing % | Description | Class | Coding / units | Sensitivity |
|---:|---|---|---:|---|---|---|---|
| 1 | `DATA_SOURCE` | categorical | 0.0 | | | | |
| 2 | `PATIENT_ID_X` | id_like | 0.0 | | | | |
| 3 | `Gender` | categorical | 0.0 | | | | |
| 4 | `Race` | categorical | 0.0 | | | | |
| 5 | `Date_of_Birth_X` | date | 0.0 | | | | |
| 6 | `Order_Id` | categorical | 0.0 | | | | |
| 7 | `Case_No` | id_like | 0.0 | | | | |
| 8 | `Result_Created_DateTime_X` | date | 0.0 | | | | |
| 9 | `Result_Created_DateTime_Z` | date | 0.0 | | | | |
| 10 | `Order_Name` | categorical | 0.0 | | | | |
| 11 | `Result_Name` | categorical | 0.0 | | | | |
| 12 | `Text` | id_like | 0.0 | | | | |

*(profiler, 2026-07-23)*

**Every column is reported 0.0% missing**, and the object's overall missing figure is 0.0%.
Read that with the disguised-missing caveat below before treating it as a complete dataset.

> **Value strings drift between extracts** (`SINGAPORE PINK IC` vs `SINGAPORE PINK NRIC`).
> This page lists no values for any column. Enumerate the distinct values in your own extract
> before filtering, and re-check them against each new extract — a value string that has
> drifted returns zero rows without raising an error.

---

## Time Coverage

| Date column | Start | End | Source |
|---|---|---|---|
| `Date_of_Birth_X` | Unknown | Unknown | — |
| `Result_Created_DateTime_X` | Unknown | Unknown | — |
| `Result_Created_DateTime_Z` | Unknown | Unknown | — |

No date range is established and no principal date column is identified.

**Date format:** Unknown. The profiler parses with `dayfirst=True`, so `01/02/2021` reads as
1 February. If any column is month-first, every date derived from it is wrong and nothing
raises.

**Completeness over the period:** Unknown — depends on the date range above.

**Variable availability over time:** Unknown.

| Variable | Usable from | Evidence |
|---|---|---|
| | | |

---

## Dataset Information

*Transcribed from the condensed profiler summary, run 2026-07-23.*

| Object | Size (MB) | Rows | Cols | Overall missing % |
|---|---:|---:|---:|---:|
| `VW_CGH_NUCLEAR_F_Export_22-07-2024.csv` | 5.80 | 4,387 | 12 | 0.0 |
| **Family total** | **5.80** | **4,387** | 12 | 0.0 |

*The row count above is a lower bound: the profiler reads with `on_bad_lines="skip"`
([tools/s3_data_catalog.py](../tools/s3_data_catalog.py)), so unparseable lines are dropped
silently and never counted. On a 4,387-row object a handful of skipped lines is a materially
larger share than on the million-row families.*

| Metric | Value |
|---|---|
| Sample size (distinct patients) | **not counted** — the profiler does not compute it |
| Schema consistent across partitions | n/a — single object |

---

## Provenance & Processing

Every field here is owner-only, and none is inferred from column naming.

**Collection mechanism:** Unknown — to confirm with data owner.

**Who enters it, and under what incentive:** Unknown — to confirm with data owner.

**Extract pipeline:** Unknown — to confirm with data owner. The object name begins `VW_`; what
that prefix denotes is not documented in any source available here.

**Processing applied:** Unknown — to confirm with data owner.

**Standardisation mappings:** n/a — no column name on this page carries a `_STD` suffix.

**Transformations at load:** Unknown. Inspect `df.columns` after loading — this object's
mixed-case names are the ones most likely to be altered by a loader that normalises case.

**Raw vs interpreted — what is lost:** Unknown. Needs the Class determination this page cannot
yet make. `Result_Created_DateTime_X` / `_Z` form an apparent pair; no relationship between
them has been established.

**Identifier handling:** Unknown — to confirm with data owner. Note that this object's patient
column is named `PATIENT_ID_X`, not `PATIENT_ID_EXTN_X` as in the larger SingCLOUD families.
Whether these are the same identifier space is unknown.

---

## Data Quality

### Missingness

| Metric | Value |
|---|---|
| Overall missing (share of all cells) | 0.0% (profiler, 2026-07-23) |
| Columns >50% missing | 0 of 12 |
| Columns 100% missing | 0 of 12 |

**Columns that matter:** Unknown — ranking columns by consequence needs their descriptions.

| Variable | Missing % | Consequence if unusable |
|---|---:|---|
| | | |
**Disguised missing:** **Not checked, and this is the page where it matters most.**

- Profiler counts only `""`, `NA`, `N/A`, `NULL`, `null`, `None`, `NaN`, `.` as missing.
- `UNKNOWN`, `NIL`, `9`, `999`, `1900-01-01` all read as *present* — invisible in these figures.
- Run `value_counts()` before trusting any 0.0% figure.

### Overlap

**Primary identifier:** `PATIENT_ID_X`. The patient ID column is the primary identifier for
every dataset in this catalogue. Its dtype as read, leading zeros, casing and padding are
unknown — read it as `str` and inspect before joining.

**Identifier family:** Unknown — to confirm with data owner. The name differs from the
`PATIENT_ID_EXTN_X` used by the larger SingCLOUD families, which is a reason to check rather
than assume; **no join has been tested**.

**Secondary keys:** Unknown. `Case_No` and `Text` are the other columns the profiler typed
`id_like`. `Text` receiving that label is worth a look on its own: it means more than half its
sampled values held over seven digits, which is not what a column named `Text` would be
expected to contain.

**Coding standards:** Unknown — to confirm with data owner.

| Links to | On | Granularity | Cardinality | Overlap tested? | Notes |
|---|---|---|---|---|---|
| Unknown | Unknown | Unknown | Unknown | **no join tested** | No linkage established |

**Known linkage pitfalls:** None recorded — no linkage has been attempted. An empty list, not
a clean bill of health.

### Bias

- **Coverage / selection:** Unknown — to confirm with data owner.
- **Recording practice:** Unknown — to confirm with data owner.
- **Changes over time:** Unknown — to confirm with data owner.
- **Ascertainment:** Unknown — to confirm with data owner.

### Other limitations

- **Duplicates:** Not checked.
- **Schema drift across partitions:** n/a — single object.
- **Value-range anomalies:** Not checked.
- **Encoding:** Unknown. The profiler attempts UTF-8 and falls back to latin-1 with
  `errors="replace"` silently.
- **Fitness for purpose:** **Cannot be assessed yet.** This page establishes neither what the
  dataset is nor what one row represents.

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
| **Free-text / PII exposure** | **Not assessed.** No column is classified Direct ID, Quasi-ID or Free text yet. The profiler typed `PATIENT_ID_X`, `Case_No` and `Text` as `id_like`. This object also carries `Gender`, `Race` and `Date_of_Birth_X` — three fields that are quasi-identifiers on their face — in a file of only 4,387 rows, where re-identification risk is structurally higher than in the million-row families. Treat this as a priority for pass 2, and note that absence of a classification here is an outstanding task, **not** a finding that the dataset carries no PII |
| **Attribution / citation** | Unknown — to confirm with data owner |

**Open questions for the data owner:**

1. What is the unit of observation — what does one row represent?
2. What is this dataset, in one paragraph? What do `CGH` and `nuclear` refer to?
3. Why is it only 4,387 rows — what is the inclusion criterion?
4. What is the source system, and what does the `VW_` prefix denote?
5. Is there a data dictionary? All 12 columns are currently undescribed and unclassified.
6. Is `PATIENT_ID_X` the same identifier space as `PATIENT_ID_EXTN_X` in the other SingCLOUD
   families? Does a crosswalk exist?
7. What does the `Text` column contain, and why does it profile as `id_like`?
8. Are `Gender`, `Race` and `Date_of_Birth_X` permitted for release at this row count, and
   under what conditions?
9. Is the 0.0% missing figure genuine, or does the object use sentinel values?
10. What is the relationship between `Result_Created_DateTime_X` and `_Z`?
11. Why are this object's column names mixed-case when every other family is upper-case?
12. What is the delimiter and file encoding?
13. What date does `22-07-2024` in the object name refer to?
14. Who is the data owner and steward role, what is the approval route, and what lead time
    should a study plan for?

---

## Appendix A — Full column profile

The per-column profile is the *Key Variables* table above and is not repeated here: with
Description, Class, Coding and Sensitivity still outstanding, the two tables would be
identical. Both carry 12 rows, matching the 12 columns declared.

## Appendix B — Change log

| Date | Change | By |
|---|---|---|
| 2026-07-31 | Page created against `template.md` from the profiler run of 2026-07-23. One object, 4,387 rows, 12 columns, all figures transcribed from the screenshots. Category from the dataset name and `PATIENT_ID_X` as primary identifier, both by catalogue convention. | CCJX |

## Appendix C — Sources

- **Profiler run 2026-07-23** — the complete object block, read from
  `source_material/screenshots/mass_columns_screenshots/section_01.png`. This is the first
  object in the report, immediately below the run header.
- `tools/s3_data_catalog.py` — cited only for the profiler's documented behaviour, never for
  any property of this dataset.
- **Not used for column names:** `source_material/imported/profiler_report_full.txt` and
  `column_summary.csv`, which are OCR reconstructions that corrupt column names. For this
  object the reconstruction happens to agree with the screenshot, but agreement was checked,
  not assumed.
- **Data owner correspondence — none.** Every governance field on this page is unconfirmed.

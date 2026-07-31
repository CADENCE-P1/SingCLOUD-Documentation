# SingCLOUD — Dispensed Medication

| | |
|---|---|
| **Status** | ⚪ Stub |
| **Profiled on** | 2026-07-23 |
| **Last reviewed** | *not yet reviewed* |

**Objects included in this page**

| # | Object |
|---:|---|
| 1 | `VW_DISPENSED_MEDICATION_F_Export_22-07-2024_PART_1.csv` |
| 2 | `VW_DISPENSED_MEDICATION_F_Export_24-07-2024_PART2.csv` |
| 3 | `VW_DISPENSED_MEDICATION_F_Export_24-07-2024_PART3.csv` |

All sit under the prefix `common-data/SingCLoud/FreeText_FTA/`. Three objects, 13,288,910
rows, 11 columns each.

---

## Read this first

| | Issue | What to do |
|---|---|---|
| 🔴 | **Object names are inconsistent** — `PART_1` with underscore, `PART2`/`PART3` without | A `*_PART_*` glob matches only one of three. List files explicitly |
| 🟡 | **Two extract dates** — `22-07-2024` and `24-07-2024` | Confirm all three are parts of one extract before pooling; rows may overlap otherwise |
| 🟡 | **Overall missing is 0.08–0.10%** — the most complete family in the catalogue | Suspiciously clean. Check for sentinels before trusting it |
| 🟡 | **No drug detail here** — no name, code, dose, quantity or route | Those live in Dispensed Medication Item. The link between the two is untested |
| 📋 | PART3 not column-transcribed | Verify its schema matches PART_1 and PART2 |

---

## Dataset Overview

**Category:** Dispensed medication — taken from the dataset name. Not yet confirmed against a
data dictionary or the data owner.

**Description:** Unknown — to be filled in.

**Data source:** Unknown — to confirm with data owner.

**Population:** Unknown — to confirm with data owner.

**Institutional / geographic coverage:** Unknown — to confirm with data owner.
`INSTITUTION_CODE` is present and 0.0% missing, so the answer is in the data, but it has not
been enumerated here.

**Unit of observation:** **Unknown — to confirm with data owner.** What one row represents,
and what causes rows to multiply, are not established.

**Rows vs people:** 13,288,910 rows (profiler, 2026-07-23, three objects summed); distinct
patients **not counted**.

**What is *not* in it:** Unknown — to be filled in. The 11 column names in *Key Variables*
are the complete column list for the partitions read. Note what is *not* among them: no drug
name, code, dose, quantity or route. Those appear in
[Dispensed Medication Item](singcloud-dispensed-medication-item.md) — but whether the two
families are related, and how, is unknown.

### Access

| | |
|---|---|
| **Catalogue alias(es)** | Unknown — to be filled in |
| **Source object(s)** | `common-data/SingCLoud/FreeText_FTA/VW_DISPENSED_MEDICATION_F_Export_{date}_PART{n}.csv` |
| **Partitions** | 3 objects — see the naming caveat above |
| **Format** | CSV by file extension. Delimiter and encoding unknown |
| **Extract date** | Two dates in the object names: `22-07-2024` and `24-07-2024` |
| **Refresh cadence** | Unknown — to confirm with data owner |
| **Free-text content** | Unknown. The objects sit under a path segment named `FreeText_FTA` |

---

## Key Variables

All 11 columns, in the order printed in the report. Names, order and types verified
**identical in PART_1 and PART2**, which carry different extract dates.

**Type** is the profiler's label and is provisional until pass 2.

**Outstanding until pass 2, for every column:** Description, Class, Coding / units,
Sensitivity. Every column here is unclassified.

| # | Variable | Type | PART_1 | PART2 | Description | Class | Coding / units | Sensitivity |
|---:|---|---|---:|---:|---|---|---|---|
| 1 | `DATA_SOURCE` | categorical | 0.0 | 0.0 | | | | |
| 2 | `MED_TYPE` | categorical | 0.0 | 0.0 | | | | |
| 3 | `COMBINED_ORDER_ID` | numeric | 0.0 | 0.0 | | | | |
| 4 | `COMBINED_ORDER_VER_NUM` | numeric | 0.0 | 0.0 | | | | |
| 5 | `COMBINED_ID_ROOT` | id_like | 0.0 | 0.0 | | | | |
| 6 | `PATIENT_ID_EXTN_X` | id_like | 0.0 | 0.0 | | | | |
| 7 | `DISPLAY_DATE_X` | date | 0.0 | 0.0 | | | | |
| 8 | `DISPLAY_DATE_Z` | date | 0.0 | 0.0 | | | | |
| 9 | `INSTITUTION_CODE` | categorical | 0.0 | 0.0 | | | | |
| 10 | `COMBINED_ID_EXTN` | id_like | 0.0 | 0.0 | | | | |
| 11 | `EVENT_EXT` | id_like | 1.13 | 1.1 | | | | |

*(PART_1 and PART2 are missing %; profiler, 2026-07-23)*

**This is the most complete family in the catalogue** — ten of eleven columns are 0.0% missing
in both partitions read, and the eleventh is ~1.1%. Read that alongside the disguised-missing
caveat below before treating it as fully populated.

> **Value strings drift between extracts** (`SINGAPORE PINK IC` vs `SINGAPORE PINK NRIC`).
> This page lists no values for any column. Enumerate the distinct values in your own extract
> before filtering, and re-check them against each new extract — a value string that has
> drifted returns zero rows without raising an error.

---

## Time Coverage

| Date column | Start | End | Source |
|---|---|---|---|
| `DISPLAY_DATE_X` | Unknown | Unknown | — |
| `DISPLAY_DATE_Z` | Unknown | Unknown | — |

Two date columns, both fully populated in the partitions read. No range is established.

**Date format:** Unknown. The profiler parses with `dayfirst=True`, so `01/02/2021` reads as
1 February. If either column is month-first, every date derived from it is wrong and nothing
raises.

**Completeness over the period:** Unknown — depends on the date range above.

**Variable availability over time:** Unknown. The `PART` split is not established as temporal,
so per-partition figures are not a time series.

| Variable | Usable from | Evidence |
|---|---|---|
| | | |

---

## Dataset Information

*Transcribed from the condensed profiler summary, run 2026-07-23.*

| Object | Size (MB) | Rows | Cols | Overall missing % |
|---|---:|---:|---:|---:|
| `…_22-07-2024_PART_1.csv` | 1,092.68 | 5,320,492 | 11 | 0.10 |
| `…_24-07-2024_PART2.csv` | 559.40 | 2,741,908 | 11 | 0.10 |
| `…_24-07-2024_PART3.csv` | 1,077.99 | 5,226,510 | 11 | 0.08 |
| **Family total** | **2,730.07** | **13,288,910** | 11 | — |

*Every row count above is a lower bound: the profiler reads with `on_bad_lines="skip"`
([tools/s3_data_catalog.py](../tools/s3_data_catalog.py)), so unparseable lines are dropped
silently and never counted.*

Family size and rows are sums of the three reported figures. Family missing % is left blank
deliberately: the per-object percentages are shares of three different denominators and cannot
be averaged.

| Metric | Value |
|---|---|
| Sample size (distinct patients) | **not counted** — the profiler does not compute it |
| Schema consistent across partitions | 11 columns in every object; names, order and types verified identical in PART_1 and PART2. PART3 is not yet checked column by column |

---

## Provenance & Processing

Every field here is owner-only, and none is inferred from column naming.

**Collection mechanism:** Unknown — to confirm with data owner.

**Who enters it, and under what incentive:** Unknown — to confirm with data owner.

**Extract pipeline:** Unknown — to confirm with data owner. The object name begins `VW_`; what
that prefix denotes is not documented in any source available here.

**Processing applied:** Unknown — to confirm with data owner.

**Standardisation mappings:** n/a — no column name on this page carries a `_STD` suffix.

**Transformations at load:** Unknown. Inspect `df.columns` after loading.

**Raw vs interpreted — what is lost:** Unknown. Needs the Class determination this page cannot
yet make. `DISPLAY_DATE_X` / `_Z` form an apparent pair; no relationship between them has been
established.

**Identifier handling:** Unknown — to confirm with data owner.

---

## Data Quality

### Missingness

| Metric | Value |
|---|---|
| Overall missing (share of all cells) | 0.08–0.10% across the three objects (profiler, 2026-07-23) |
| Columns >50% missing | 0 of 11 |
| Columns 100% missing | 0 of 11 |

The lowest overall missing figure of any multi-object family in the catalogue.

**Columns that matter:** Unknown — ranking columns by consequence needs their descriptions.

| Variable | Missing % | Consequence if unusable |
|---|---:|---|
| | | |
**Disguised missing:** **Not checked, and this page is one where it matters most.** Ten of eleven columns report 0.0% missing, which is exactly the pattern a sentinel-filled extract produces: the profiler counts only `""`, `NA`, `N/A`, `NULL`, `null`, `None`, `NaN` and `.` as missing, so `UNKNOWN`, `NIL`, `9`, `999` and `1900-01-01` are all counted as *present*. **Do not read "0.08% missing overall" as "this family is complete"** until someone has run `value_counts()` against it.

- Profiler counts only `""`, `NA`, `N/A`, `NULL`, `null`, `None`, `NaN`, `.` as missing.
- `UNKNOWN`, `NIL`, `9`, `999`, `1900-01-01` all read as *present* — invisible in these figures.
- Run `value_counts()` before trusting any 0.0% figure.

### Overlap

**Primary identifier:** `PATIENT_ID_EXTN_X`. The patient ID column is the primary identifier
for every dataset in this catalogue. Its dtype as read, leading zeros, casing and padding are
unknown — read it as `str` and inspect before joining.

**Identifier family:** Unknown — to confirm with data owner. The name matches the identifier
column in [Event Diagnosis](singcloud-event-diagnosis.md),
[Laboratory](singcloud-laboratory.md) and
[Dispensed Medication Item](singcloud-dispensed-medication-item.md), but **no join has been
tested** and a shared column name is not evidence of a shared identifier space.

**Secondary keys:** Unknown. `COMBINED_ID_ROOT`, `COMBINED_ID_EXTN` and `EVENT_EXT` also
profile as `id_like`.

**Coding standards:** Unknown — to confirm with data owner.

| Links to | On | Granularity | Cardinality | Overlap tested? | Notes |
|---|---|---|---|---|---|
| [Dispensed Medication Item](singcloud-dispensed-medication-item.md) | Unknown | Unknown | Unknown | **no join tested** | The two families share four column names — `COMBINED_ID_ROOT`, `COMBINED_ID_EXTN`, `PATIENT_ID_EXTN_X`, `INSTITUTION_CODE` — and the naming suggests an order-to-item relationship. **Nothing establishes that.** Listed so it can be checked |
| [Laboratory](singcloud-laboratory.md) | Unknown | Unknown | Unknown | **no join tested** | Both carry an `EVENT_EXT` column typed `id_like` |

**Known linkage pitfalls:** None recorded — no linkage has been attempted. An empty list, not
a clean bill of health.

### Bias

- **Coverage / selection:** Unknown — to confirm with data owner.
- **Recording practice:** Unknown — to confirm with data owner.
- **Changes over time:** Unknown — to confirm with data owner.
- **Ascertainment:** Unknown — to confirm with data owner.

### Other limitations

- **Duplicates:** Not checked. The two extract dates make this worth checking: if `22-07-2024`
  and `24-07-2024` are separate extracts rather than parts of one, rows may appear in both.
- **Schema drift across partitions:** All three objects report 11 columns. PART_1 and PART2
  verified identical; PART3 not yet checked.
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
| **Free-text / PII exposure** | **Not assessed.** No column is classified Direct ID, Quasi-ID or Free text yet. The profiler typed `COMBINED_ID_ROOT`, `PATIENT_ID_EXTN_X`, `COMBINED_ID_EXTN` and `EVENT_EXT` as `id_like` — four of eleven columns are digit-heavy and worth inspecting first. Absence of a classification here is an outstanding task, **not** a finding that the dataset carries no PII |
| **Attribution / citation** | Unknown — to confirm with data owner |

**Open questions for the data owner:**

1. What is the unit of observation — one row per dispensing order?
2. **What is the relationship between this family and `VW_DISPENSED_MEDICATION_ITEM_F`?** Do
   `COMBINED_ID_ROOT` and `COMBINED_ID_EXTN` join them, and at what cardinality?
3. What is this dataset, in one paragraph?
4. Why do the object names mix `PART_1` with `PART2` and `PART3`, and why two extract dates?
   Are all three parts of one extract?
5. Which population is included, and who is excluded by what mechanism?
6. Is there a data dictionary? All 11 columns are currently undescribed and unclassified.
7. What are the possible values of `MED_TYPE`?
8. Is the 0.08–0.10% missing figure genuine, or does the family use sentinel values?
9. What is `EVENT_EXT`, and what does it join to? Laboratory carries a column of the same name.
10. What is the relationship between `DISPLAY_DATE_X` and `_Z`, and which should be preferred?
11. Is `PATIENT_ID_EXTN_X` a pseudonym, and is it stable across datasets and across successive
    extracts of this one?
12. What is the delimiter and file encoding, and are all three objects the same?
13. Who is the data owner and steward role, what is the approval route, and what lead time
    should a study plan for?

---

## Appendix A — Full column profile

The per-column profile is the *Key Variables* table above and is not repeated here: with
Description, Class, Coding and Sensitivity still outstanding, the two tables would be
identical. Both carry 11 rows, matching the 11 columns declared for every object.

## Appendix B — Change log

| Date | Change | By |
|---|---|---|
| 2026-07-31 | Page created against `template.md` from the profiler run of 2026-07-23. Three objects, 13,288,910 rows, 11 columns. Column names, types and missing % transcribed from the screenshots for PART_1 and PART2; object-level figures for all three. Category from the dataset name and `PATIENT_ID_EXTN_X` as primary identifier, both by catalogue convention. | CCJX |

## Appendix C — Sources

- **Profiler run 2026-07-23** — the complete PART_1 and PART2 blocks, read from
  `source_material/screenshots/mass_columns_screenshots/section_01.png`. Object-level figures
  for PART3 from the same run.
- `tools/s3_data_catalog.py` — cited only for the profiler's documented behaviour, never for
  any property of this dataset.
- **Not used for column names:** `source_material/imported/profiler_report_full.txt` and
  `column_summary.csv`, which are OCR reconstructions that corrupt column names.
- **Data owner correspondence — none.** Every governance field on this page is unconfirmed.

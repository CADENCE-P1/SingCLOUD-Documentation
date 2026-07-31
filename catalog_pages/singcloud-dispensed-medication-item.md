# SingCLOUD — Dispensed Medication Item

| | |
|---|---|
| **Status** | ⚪ Stub |
| **Profiled on** | 2026-07-23 |
| **Last reviewed** | *not yet reviewed* |

**Objects included in this page**

`VW_DISPENSED_MEDICATION_ITEM_F_Export_24-07-2024_P{n}.csv` for the 27 values of *n* listed
below, all under the prefix `common-data/SingCLoud/FreeText_FTA/`:

| # | Object | # | Object |
|---:|---|---:|---|
| 1 | `…_P2.csv` | 15 | `…_P17.csv` |
| 2 | `…_P3.csv` | 16 | `…_P18.csv` |
| 3 | `…_P4.csv` | 17 | `…_P19.csv` |
| 4 | `…_P5.csv` | 18 | `…_P20.csv` |
| 5 | `…_P6.csv` | 19 | `…_P21.csv` |
| 6 | `…_P7.csv` | 20 | `…_P22.csv` |
| 7 | `…_P8.csv` | 21 | `…_P23.csv` |
| 8 | `…_P9.csv` | 22 | `…_P24.csv` |
| 9 | `…_P11.csv` | 23 | `…_P25.csv` |
| 10 | `…_P12.csv` | 24 | `…_P26.csv` |
| 11 | `…_P13.csv` | 25 | `…_P27.csv` |
| 12 | `…_P14.csv` | 26 | `…_P28.csv` |
| 13 | `…_P15.csv` | 27 | `…_P29.csv` |
| 14 | `…_P16.csv` | | |

Twenty-seven objects, 118,121,782 rows, 30 columns each.

---

## Read this first

| | Issue | What to do |
|---|---|---|
| 🔴 | **P1 and P10 are absent** — numbering runs P2–P9 then P11–P29 | Confirm whether they exist before treating 27 objects as the whole family |
| 🟡 | **`HIGH_DOSAGE_QTY` and `HIGH_DOSAGE_QTY_UOM` are 100% empty** in all four partitions read | No data at all in those objects |
| 🟡 | **`ITEM_NAME_ETS_ID` profiles as `id_like` in P29 but `categorical` elsewhere** | pandas infers per file too. Read it as `str` explicitly or joins may fail silently |
| 🟡 | **`ROUTE_OF_ADMIN_ORI_TXT` is 100% empty in P3 and P4** but 75–97% elsewhere | Varies sharply by partition |
| 📋 | 23 of 27 partitions have object-level figures only | Transcribe, or confirm schema uniformity |

---

## Dataset Overview

**Category:** Dispensed medication item — taken from the dataset name. Not yet confirmed
against a data dictionary or the data owner.

**Description:** Unknown — to be filled in.

**Data source:** Unknown — to confirm with data owner.

**Population:** Unknown — to confirm with data owner.

**Institutional / geographic coverage:** Unknown — to confirm with data owner.

**Unit of observation:** **Unknown — to confirm with data owner.** What one row represents,
and what causes rows to multiply, are not established.

**Rows vs people:** 118,121,782 rows (profiler, 2026-07-23, 27 objects summed); distinct
patients **not counted**.

**What is *not* in it:** Unknown — to be filled in. The 30 column names in *Key Variables*
are the complete column list for all 27 objects.

### Access

| | |
|---|---|
| **Catalogue alias(es)** | Unknown — to be filled in |
| **Source object(s)** | `common-data/SingCLoud/FreeText_FTA/VW_DISPENSED_MEDICATION_ITEM_F_Export_24-07-2024_P{n}.csv` |
| **Partitions** | 27 objects, P2–P9 and P11–P29 |
| **Format** | CSV by file extension. Delimiter and encoding unknown |
| **Extract date** | Unknown. The object name contains `_Export_24-07-2024_` |
| **Refresh cadence** | Unknown — to confirm with data owner |
| **Free-text content** | Unknown. The objects sit under a path segment named `FreeText_FTA` |

---

## Key Variables

All 30 columns, in the order printed in the report, identical in name and order across the
partitions read. Row count matches Appendix A.

**Type** is the profiler's label and is provisional until pass 2. `ITEM_NAME_ETS_ID` was typed
`id_like` in P29 and `categorical` in P3, P4 and P9; both readings are kept.

**Outstanding until pass 2, for every column:** Description, Class, Coding / units,
Sensitivity. Class cannot be read off a suffix such as `_ORI_TXT`, `_UOM`, `_X` or `_ETS_ID`,
so every column here is unclassified.

Missing percentages are given for **P3, P4, P9 and P29 only** — the four partitions
transcribed in full from the screenshots. The other 23 partitions have object-level figures in
*Dataset Information* but their per-column figures are not yet transcribed.

| # | Variable | Type | P3 | P4 | P9 | P29 | Description | Class | Coding / units | Sensitivity |
|---:|---|---|---:|---:|---:|---:|---|---|---|---|
| 1 | `DATA_SOURCE` | categorical | 0.0 | 0.0 | 0.0 | 0.0 | | | | |
| 2 | `COMBINED_ID_ROOT` | id_like | 0.0 | 0.0 | 0.0 | 0.0 | | | | |
| 3 | `COMBINED_ID_EXTN` | id_like | 0.0 | 0.0 | 0.0 | 0.0 | | | | |
| 4 | `SOURCE_ID_EXTN` | categorical | 0.0 | 0.0 | 0.0 | 0.0 | | | | |
| 5 | `PATIENT_ID_EXTN_X` | id_like | 0.0 | 0.0 | 0.0 | 0.0 | | | | |
| 6 | `MED_ITM_COMBINED_ORDER_ID` | numeric | 0.0 | 0.0 | 0.0 | 0.0 | | | | |
| 7 | `MED_ITM_COMBINED_ORDER_VER_NUM` | numeric | 0.0 | 0.0 | 0.0 | 0.0 | | | | |
| 8 | `ORD_DISP_LOC_TXT` | categorical | 52.43 | 53.06 | 70.62 | 27.96 | | | | |
| 9 | `DISP_ORD_FACILITY_EXTN` | categorical | 100.0 | 97.43 | 94.56 | 72.51 | | | | |
| 10 | `MEDITEM_DATE_X` | date | 0.0 | 0.0 | 0.0 | 0.0 | | | | |
| 11 | `MEDITEM_DATE_Z` | date | 0.0 | 0.0 | 0.0 | 0.0 | | | | |
| 12 | `DURATION_ORI_TXT` | categorical | 6.46 | 9.2 | 21.7 | 4.48 | | | | |
| 13 | `DURATION_UNIT` | categorical | 52.14 | 54.09 | 60.28 | 16.54 | | | | |
| 14 | `LOW_DOSAGE_QTY` | numeric | 51.22 | 53.23 | 69.63 | 53.75 | | | | |
| 15 | `LOW_DOSAGE_QTY_UOM` | categorical | 3.5 | 7.08 | 42.99 | 53.74 | | | | |
| 16 | `HIGH_DOSAGE_QTY` | categorical | 100.0 | 100.0 | 100.0 | 100.0 | | | | |
| 17 | `HIGH_DOSAGE_QTY_UOM` | categorical | 100.0 | 100.0 | 100.0 | 100.0 | | | | |
| 18 | `DOSAGE_FREQ_ETS_ID` | categorical | 2.4 | 4.97 | 17.3 | 53.56 | | | | |
| 19 | `ROUTE_OF_ADMIN_ORI_TXT` | categorical | 100.0 | 100.0 | 97.08 | 75.6 | | | | |
| 20 | `DOSAGE_FREQ_ORI_TXT` | categorical | 2.45 | 5.02 | 17.31 | 53.56 | | | | |
| 21 | `ITEM_NAME_ETS_ID` | **categorical P3–P9; id_like P29** | 0.0 | 0.0 | 0.0 | 0.0 | | | | |
| 22 | `ITEM_STATUS_ETS_ID` | categorical | 0.0 | 0.0 | 0.0 | 0.0 | | | | |
| 23 | `ITEM_STATUS_ORI_TXT` | categorical | 98.82 | 95.12 | 55.39 | 22.77 | | | | |
| 24 | `ORD_DISP_QTY` | numeric | 89.57 | 86.05 | 52.56 | 44.41 | | | | |
| 25 | `ORD_DISP_QTY_UOM` | categorical | 89.57 | 86.05 | 52.68 | 44.41 | | | | |
| 26 | `MED_STRENGTH` | categorical | 79.33 | 78.84 | 55.08 | 91.42 | | | | |
| 27 | `DOSE_FORM_ORI_TXT` | categorical | 47.86 | 46.17 | 30.77 | 60.86 | | | | |
| 28 | `ORD_DISP_BY_EXTENSION_TXT_X` | categorical | 48.81 | 47.14 | 30.22 | 47.43 | | | | |
| 29 | `INSTITUTION_CODE` | categorical | 0.0 | 0.0 | 0.0 | 0.0 | | | | |
| 30 | `ITEM_NAME_ORI_TXT` | categorical | 0.0 | 0.0 | 0.0 | 0.0 | | | | |

*(P3, P4, P9 and P29 are missing %; profiler, 2026-07-23)*

**`HIGH_DOSAGE_QTY` and `HIGH_DOSAGE_QTY_UOM` are 100% empty in all four partitions read** —
they hold no data at all in those objects. Whether that is true of the other 23 is not yet
transcribed.

> **Value strings drift between extracts** (`SINGAPORE PINK IC` vs `SINGAPORE PINK NRIC`).
> This page lists no values for any column. Enumerate the distinct values in your own extract
> before filtering, and re-check them against each new extract — a value string that has
> drifted returns zero rows without raising an error.

---

## Time Coverage

| Date column | Start | End | Source |
|---|---|---|---|
| `MEDITEM_DATE_X` | Unknown | Unknown | — |
| `MEDITEM_DATE_Z` | Unknown | Unknown | — |

Two date columns, both fully populated in every partition read. No range is established.

**Date format:** Unknown. The profiler parses with `dayfirst=True`, so `01/02/2021` reads as
1 February. If either column is month-first, every date derived from it is wrong and nothing
raises.

**Completeness over the period:** Unknown — depends on the date range above.

**Variable availability over time:** Unknown. The `_P{n}` split is not established as
temporal, so per-partition figures are not a time series.

| Variable | Usable from | Evidence |
|---|---|---|
| | | |

---

## Dataset Information

*Transcribed from the condensed profiler summary, run 2026-07-23.*

| Object | Size (MB) | Rows | Cols | Overall missing % |
|---|---:|---:|---:|---:|
| `…_P2.csv` | 1,838.42 | 6,050,215 | 30 | 35.72 |
| `…_P3.csv` | 980.24 | 3,124,838 | 30 | 34.15 |
| `…_P4.csv` | 1,052.00 | 3,324,622 | 30 | 34.11 |
| `…_P5.csv` | 1,085.03 | 3,426,473 | 30 | 34.49 |
| `…_P6.csv` | 1,112.33 | 3,513,500 | 30 | 34.64 |
| `…_P7.csv` | 1,485.77 | 4,644,736 | 30 | 33.44 |
| `…_P8.csv` | 909.10 | 2,787,367 | 30 | 32.43 |
| `…_P9.csv` | 951.61 | 2,910,038 | 30 | 32.27 |
| `…_P11.csv` | 1,493.64 | 4,620,997 | 30 | 33.61 |
| `…_P12.csv` | 1,451.65 | 4,522,782 | 30 | 34.51 |
| `…_P13.csv` | 1,491.43 | 4,637,969 | 30 | 34.51 |
| `…_P14.csv` | 1,538.16 | 4,780,503 | 30 | 34.51 |
| `…_P15.csv` | 1,502.27 | 4,663,315 | 30 | 34.53 |
| `…_P16.csv` | 983.81 | 3,049,918 | 30 | 34.48 |
| `…_P17.csv` | 1,567.13 | 4,835,134 | 30 | 34.36 |
| `…_P18.csv` | 1,572.57 | 4,836,597 | 30 | 34.18 |
| `…_P19.csv` | 1,598.02 | 4,947,856 | 30 | 33.73 |
| `…_P20.csv` | 1,626.29 | 4,987,026 | 30 | 34.33 |
| `…_P21.csv` | 1,563.93 | 4,797,258 | 30 | 34.30 |
| `…_P22.csv` | 1,527.05 | 4,682,880 | 30 | 34.33 |
| `…_P23.csv` | 1,605.32 | 4,920,167 | 30 | 34.01 |
| `…_P24.csv` | 1,611.13 | 4,929,227 | 30 | 33.37 |
| `…_P25.csv` | 1,528.63 | 4,667,974 | 30 | 32.30 |
| `…_P26.csv` | 1,511.70 | 4,616,707 | 30 | 32.27 |
| `…_P27.csv` | 1,531.07 | 4,683,142 | 30 | 31.89 |
| `…_P28.csv` | 1,495.35 | 4,584,849 | 30 | 31.32 |
| `…_P29.csv` | 1,494.61 | 4,575,692 | 30 | 30.77 |
| **Family total** | **38,108.26** | **118,121,782** | 30 | — |

*Every row count above is a lower bound: the profiler reads with `on_bad_lines="skip"`
([tools/s3_data_catalog.py](../tools/s3_data_catalog.py)), so unparseable lines are dropped
silently and never counted.*

Family size and rows are sums of the 27 reported figures. Family missing % is left blank
deliberately: the per-object percentages are shares of 27 different denominators and cannot be
averaged.

| Metric | Value |
|---|---|
| Sample size (distinct patients) | **not counted** — the profiler does not compute it |
| Schema consistent across partitions | 30 columns in every object; names and order identical in the four partitions read. The remaining 23 are not yet checked column by column |

---

## Provenance & Processing

Every field here is owner-only, and none is inferred from column naming.

**Collection mechanism:** Unknown — to confirm with data owner.

**Who enters it, and under what incentive:** Unknown — to confirm with data owner.

**Extract pipeline:** Unknown — to confirm with data owner. The object name begins `VW_`; what
that prefix denotes is not documented in any source available here.

**Processing applied:** Unknown — to confirm with data owner.

**Standardisation mappings:** Unknown — to confirm with data owner. No column name on this
page ends in `_STD`, but several end in `_ETS_ID` and `_ORI_TXT`; what either suffix denotes,
and whether the two encode the same information, is unconfirmed.

**Transformations at load:** Unknown. Inspect `df.columns` after loading.

**Raw vs interpreted — what is lost:** Unknown. Needs the Class determination this page cannot
yet make. `DOSAGE_FREQ_ETS_ID` / `DOSAGE_FREQ_ORI_TXT` and `ITEM_NAME_ETS_ID` /
`ITEM_NAME_ORI_TXT` form apparent pairs; no relationship between either pair has been
established.

**Identifier handling:** Unknown — to confirm with data owner.

---

## Data Quality

### Missingness

| Metric | Value |
|---|---|
| Overall missing (share of all cells) | 30.77–35.72% across the 27 objects (profiler, 2026-07-23) |
| Columns >50% missing | Varies by partition — 13 of 30 in P3, 13 in P4, 11 in P9, 9 in P29 |
| Columns 100% missing | 2 in every partition read (`HIGH_DOSAGE_QTY`, `HIGH_DOSAGE_QTY_UOM`); `DISP_ORD_FACILITY_EXTN` and `ROUTE_OF_ADMIN_ORI_TXT` also reach 100.0 in P3 |

No interpretation of the missingness is offered here.

**Columns that matter:** Unknown — ranking columns by consequence needs their descriptions.

| Variable | Missing % | Consequence if unusable |
|---|---:|---|
| | | |
**Disguised missing:** **Not checked.**

- Profiler counts only `""`, `NA`, `N/A`, `NULL`, `null`, `None`, `NaN`, `.` as missing.
- `UNKNOWN`, `NIL`, `9`, `999`, `1900-01-01` all read as *present* — invisible in these figures.
- **Do not read "0.0% missing" as "0.0% unusable"** — eleven columns are reported 0.0% missing in all four partitions read and the check is outstanding for every one of them.
- Run `value_counts()` before trusting any 0.0% figure.

### Overlap

**Primary identifier:** `PATIENT_ID_EXTN_X`. The patient ID column is the primary identifier
for every dataset in this catalogue. Its dtype as read, leading zeros, casing and padding are
unknown — read it as `str` and inspect before joining.

**Identifier family:** Unknown — to confirm with data owner. The name matches the identifier
column in [singcloud-event-diagnosis.md](singcloud-event-diagnosis.md) and
[singcloud-laboratory.md](singcloud-laboratory.md), but **no join has been tested** and a
shared column name is not evidence of a shared identifier space.

**Secondary keys:** Unknown. `COMBINED_ID_ROOT` and `COMBINED_ID_EXTN` are the other columns
the profiler typed `id_like` in every partition read.

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
- **Schema drift across partitions:** All 27 objects report 30 columns. Names and order
  verified identical in P3, P4, P9 and P29. One type differs: `ITEM_NAME_ETS_ID` is `id_like`
  in P29 and `categorical` in the other three. The cause is unknown. **One consequence follows
  regardless of cause:** pandas performs its own per-file type inference, so this column may
  load as a different dtype from different partitions. Read it as `str` explicitly.
- **Value-range anomalies:** Not checked.
- **Encoding:** Unknown. The profiler attempts UTF-8 and falls back to latin-1 with
  `errors="replace"` silently.
- **Missing partitions:** P1 and P10 are absent from the run.
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
| **Free-text / PII exposure** | **Not assessed.** No column is classified Direct ID, Quasi-ID or Free text yet. The profiler typed `COMBINED_ID_ROOT`, `COMBINED_ID_EXTN` and `PATIENT_ID_EXTN_X` as `id_like` in every partition read, plus `ITEM_NAME_ETS_ID` in P29 — digit-heavy values worth inspecting first. Absence of a classification here is an outstanding task, **not** a finding that the dataset carries no PII |
| **Attribution / citation** | Unknown — to confirm with data owner |

**Open questions for the data owner:**

1. What is the unit of observation — what does one row represent, and what causes rows to
   multiply?
2. What is this dataset, in one paragraph, and how does it relate to `VW_DISPENSED_MEDICATION_F`?
3. What is the source system, and what does the `VW_` prefix denote?
4. Which population is included, and who is excluded by what mechanism?
5. **Do partitions P1 and P10 exist?** If so, why were they not profiled?
6. Is there a data dictionary? All 30 columns are currently undescribed and unclassified.
7. For each column: is it a source value, a mapped value, or a computed/interpreted one?
8. What do the `_ETS_ID` and `_ORI_TXT` suffixes denote, and which of a pair should be
   preferred?
9. `HIGH_DOSAGE_QTY` and `HIGH_DOSAGE_QTY_UOM` are 100% empty in every partition read — are
   they deprecated, or populated in a source not delivered here?
10. `ROUTE_OF_ADMIN_ORI_TXT` is 100% empty in P3 and P4 but 75–97% empty elsewhere. Why?
11. Why does `ITEM_NAME_ETS_ID` profile as `id_like` in P29 but `categorical` elsewhere?
12. What determines the `_P{n}` split, and are the partitions ordered in any way?
13. Is `PATIENT_ID_EXTN_X` a pseudonym, and is it stable across datasets and across successive
    extracts of this one?
14. What are `COMBINED_ID_ROOT` and `COMBINED_ID_EXTN`, and what do they join to?
15. What is the delimiter and file encoding, and are all 27 objects the same?
16. What date does `24-07-2024` in the object name refer to?
17. Who is the data owner and steward role, what is the approval route, and what lead time
    should a study plan for?

---

## Appendix A — Full column profile

The per-column profile is the *Key Variables* table above and is not repeated here: with
Description, Class, Coding and Sensitivity still outstanding, the two tables would be
identical. Both carry 30 rows, matching the 30 columns declared for every object.

## Appendix B — Change log

| Date | Change | By |
|---|---|---|
| 2026-07-31 | Page created against `template.md` from the profiler run of 2026-07-23. Twenty-seven objects, 118,121,782 rows, 30 columns. Column names and types transcribed from the screenshots for P3, P4, P9 and P29; object-level figures for all 27. Category from the dataset name and `PATIENT_ID_EXTN_X` as primary identifier, both by catalogue convention. | CCJX |

## Appendix C — Sources

- **Profiler run 2026-07-23** — column names, types and per-column missing % read from
  `source_material/screenshots/mass_columns_screenshots/section_03.png` (objects P29, P3, P4
  and P9). Object-level figures for the remaining 23 objects from the same run.
- `tools/s3_data_catalog.py` — cited only for the profiler's documented behaviour, never for
  any property of this dataset.
- **Not used for column names:** `source_material/imported/profiler_report_full.txt` and
  `column_summary.csv`. These are OCR reconstructions that corrupt column names. For this
  family specifically, the reconstruction renders column 18 as `DOSAGE_FREQLETS_ID` in 18 of
  27 partitions; the screenshots show `DOSAGE_FREQ_ETS_ID`. The error is consistent enough to
  survive a majority vote, which is why no name on this page comes from that source.
- **Data owner correspondence — none.** Every governance field on this page is unconfirmed.

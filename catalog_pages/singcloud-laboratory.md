# SingCLOUD — Laboratory

| | |
|---|---|
| **Status** | ⚪ Stub |
| **Profiled on** | 2026-07-23 |
| **Last reviewed** | *not yet reviewed* |

**Objects included in this page**

| # | Object |
|---:|---|
| 1 | `VW_LABORATORY_F_Export_26-07-2024_P1.csv` |
| 2 | `VW_LABORATORY_F_Export_26-07-2024_P2.csv` |
| 3 | `VW_LABORATORY_F_Export_26-07-2024_P4.csv` |
| 4 | `VW_LABORATORY_F_Export_26-07-2024_P7.csv` |
| 5 | `VW_LABORATORY_F_Export_26-07-2024_P10.csv` |
| 6 | `VW_LABORATORY_F_Export_26-07-2024_P11.csv` |
| 7 | `VW_LABORATORY_F_Export_26-07-2024_P12.csv` |
| 8 | `VW_LABORATORY_F_Export_26-07-2024_P18.csv` |
| 9 | `VW_LABORATORY_F_Export_26-07-2024_P19.csv` |
| 10 | `VW_LABORATORY_F_Export_26-07-2024_P21.csv` |
| 11 | `VW_LABORATORY_F_Export_26-07-2024_P22.csv` |

All sit under the prefix `common-data/SingCLoud/FreeText_FTA/`. Eleven objects, 49,620,429
rows, 23 columns each.

---

## Read this first

| | Issue | What to do |
|---|---|---|
| 🔴 | **Partition numbers are non-contiguous** — 11 profiled; P3, P5, P6, P8, P9, P13–P17, P20 absent | Any count here is over an incomplete family. Ask whether the missing partitions exist |
| 🟡 | **Specimen and order dates are 89–97% empty**; `DISPLAY_DATE_X`/`_Z` are fully populated | Pick the date column deliberately — the obvious ones lose most rows |
| 🟡 | **`BATTERY_ID_EXT`** here vs **`BATTERY_ID_EXTN`** in Laboratory Item FIL | One letter apart on the likely join key. Confirm before joining |
| 📋 | Only P1 and P10 column-transcribed; 9 partitions have object-level figures only | Transcribe the rest, or confirm the schema is uniform |

---

## Dataset Overview

**Category:** Laboratory — taken from the dataset name. Not yet confirmed against a data
dictionary or the data owner.

**Description:** Unknown — to be filled in.

**Data source:** Unknown — to confirm with data owner.

**Population:** Unknown — to confirm with data owner.

**Institutional / geographic coverage:** Unknown — to confirm with data owner.

**Unit of observation:** **Unknown — to confirm with data owner.** What one row represents,
and what causes rows to multiply, are not established.

**Rows vs people:** 49,620,429 rows (profiler, 2026-07-23, eleven objects summed); distinct
patients **not counted**.

**What is *not* in it:** Unknown — to be filled in. The 23 column names in *Key Variables*
are the complete column list for all eleven objects.

### Access

| | |
|---|---|
| **Catalogue alias(es)** | Unknown — to be filled in |
| **Source object(s)** | `common-data/SingCLoud/FreeText_FTA/VW_LABORATORY_F_Export_26-07-2024_P{n}.csv` |
| **Partitions** | 11 objects, non-contiguous — see above |
| **Format** | CSV by file extension. Delimiter and encoding unknown |
| **Extract date** | Unknown. The object name contains `_Export_26-07-2024_` |
| **Refresh cadence** | Unknown — to confirm with data owner |
| **Free-text content** | Unknown. The objects sit under a path segment named `FreeText_FTA` |

---

## Key Variables

All 23 columns, in the order printed in the report, identical in name and order across the
partitions read. Row count matches Appendix A.

**Type** is the profiler's label and is provisional until pass 2.

**Outstanding until pass 2, for every column:** Description, Class, Coding / units,
Sensitivity. Class cannot be read off a suffix such as `_STD`, `_TXT`, `_X` or `_Z`, so every
column here is unclassified.

Missing percentages are given for **P1 and P10 only** — the two partitions transcribed from
the screenshots. The other nine partitions have object-level figures in *Dataset Information*
but their per-column figures are not yet transcribed.

| # | Variable | Type | P1 | P10 | Description | Class | Coding / units | Sensitivity |
|---:|---|---|---:|---:|---|---|---|---|
| 1 | `DATA_SOURCE` | categorical | 0.0 | 0.0 | | | | |
| 2 | `BATTERY_ACT_ID` | numeric | 0.0 | 0.0 | | | | |
| 3 | `BATTERY_VER_NUM` | numeric | 0.0 | 0.0 | | | | |
| 4 | `BATTERY_ID_ROOT` | id_like | 0.0 | 0.0 | | | | |
| 5 | `INVESTIGATION_NAME_ETS_ID` | categorical | 0.0 | 0.0 | | | | |
| 6 | `INVESTIGATION_NAME_ORI_TXT` | categorical | 0.0 | 0.0 | | | | |
| 7 | `INVESTIGATION_NAME_ORI_TXT_STD` | categorical | 52.54 | 51.48 | | | | |
| 8 | `PATIENT_ID_EXTN_X` | id_like | 0.0 | 0.0 | | | | |
| 9 | `SOURCE_EXTN_TEXT` | categorical | 0.0 | 0.0 | | | | |
| 10 | `FACILITY_EXTN` | categorical | 0.0 | 0.0 | | | | |
| 11 | `INV_RESULT_STATUS_ETS_ID` | categorical | 0.0 | 0.0 | | | | |
| 12 | `INV_TYPE_NAME_ETS_ID` | categorical | 0.0 | 0.0 | | | | |
| 13 | `INV_SUBTYPE_NAME_ETS_ID` | categorical | 0.0 | 0.0 | | | | |
| 14 | `SPECIMEN_COLLECTED_DATE_X` | date | 96.45 | 89.61 | | | | |
| 15 | `SPECIMEN_COLLECTED_DATE_Z` | date | 96.45 | 89.61 | | | | |
| 16 | `SPECIMEN_RECEIVED_DATE_X` | date | 41.22 | 42.32 | | | | |
| 17 | `SPECIMEN_RECEIVED_DATE_Z` | date | 41.22 | 42.32 | | | | |
| 18 | `ORDER_DATE_X` | date | 96.5 | 89.86 | | | | |
| 19 | `ORDER_DATE_Z` | date | 96.5 | 89.86 | | | | |
| 20 | `DISPLAY_DATE_X` | date | 0.0 | 0.0 | | | | |
| 21 | `DISPLAY_DATE_Z` | date | 0.0 | 0.0 | | | | |
| 22 | `BATTERY_ID_EXT` | id_like | 0.0 | 0.0 | | | | |
| 23 | `EVENT_EXT` | id_like | 0.01 | 0.06 | | | | |

*(P1 and P10 are missing %; profiler, 2026-07-23)*

> **Value strings drift between extracts** (`SINGAPORE PINK IC` vs `SINGAPORE PINK NRIC`).
> This page lists no values for any column. Enumerate the distinct values in your own extract
> before filtering, and re-check them against each new extract — a value string that has
> drifted returns zero rows without raising an error.

---

## Time Coverage

| Date column | Start | End | Source |
|---|---|---|---|
| `SPECIMEN_COLLECTED_DATE_X` | Unknown | Unknown | — |
| `SPECIMEN_COLLECTED_DATE_Z` | Unknown | Unknown | — |
| `SPECIMEN_RECEIVED_DATE_X` | Unknown | Unknown | — |
| `SPECIMEN_RECEIVED_DATE_Z` | Unknown | Unknown | — |
| `ORDER_DATE_X` | Unknown | Unknown | — |
| `ORDER_DATE_Z` | Unknown | Unknown | — |
| `DISPLAY_DATE_X` | Unknown | Unknown | — |
| `DISPLAY_DATE_Z` | Unknown | Unknown | — |

No date range is established and no principal date column is identified. Note that
`DISPLAY_DATE_X` / `_Z` are the only date columns populated in every row of both partitions
read; the other six are 41–97% empty.

**Date format:** Unknown. The profiler parses with `dayfirst=True`, so `01/02/2021` reads as
1 February. If any column is month-first, every date derived from it is wrong and nothing
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
| `…_P1.csv` | 1,539.97 | 5,008,403 | 23 | 22.65 |
| `…_P2.csv` | 1,791.80 | 5,862,470 | 23 | 23.54 |
| `…_P4.csv` | 1,141.30 | 3,725,410 | 23 | 22.93 |
| `…_P7.csv` | 1,287.94 | 4,181,669 | 23 | 22.71 |
| `…_P10.csv` | 1,359.36 | 4,386,097 | 23 | 21.53 |
| `…_P11.csv` | 1,344.42 | 4,341,298 | 23 | 21.72 |
| `…_P12.csv` | 1,362.31 | 4,398,438 | 23 | 21.67 |
| `…_P18.csv` | 1,478.55 | 4,691,646 | 23 | 20.40 |
| `…_P19.csv` | 1,463.34 | 4,569,232 | 23 | 18.71 |
| `…_P21.csv` | 1,410.64 | 4,396,862 | 23 | 18.88 |
| `…_P22.csv` | 1,320.96 | 4,058,904 | 23 | 18.19 |
| **Family total** | **15,500.59** | **49,620,429** | 23 | — |

*Every row count above is a lower bound: the profiler reads with `on_bad_lines="skip"`
([tools/s3_data_catalog.py](../tools/s3_data_catalog.py)), so unparseable lines are dropped
silently and never counted.*

Family size and rows are sums of the eleven reported figures. Family missing % is left blank
deliberately: the per-object percentages are shares of eleven different denominators and
cannot be averaged.

| Metric | Value |
|---|---|
| Sample size (distinct patients) | **not counted** — the profiler does not compute it |
| Schema consistent across partitions | 23 columns in every object; names and order identical in the two partitions read. The remaining nine are not yet checked column by column |

---

## Provenance & Processing

Every field here is owner-only, and none is inferred from column naming.

**Collection mechanism:** Unknown — to confirm with data owner.

**Who enters it, and under what incentive:** Unknown — to confirm with data owner.

**Extract pipeline:** Unknown — to confirm with data owner. The object name begins `VW_`; what
that prefix denotes is not documented in any source available here.

**Processing applied:** Unknown — to confirm with data owner.

**Standardisation mappings:** Unknown — to confirm with data owner. One column name ends in
`_STD` (`INVESTIGATION_NAME_ORI_TXT_STD`); its vocabulary, version, mapping rule and
failed-match behaviour are unrecorded, and whether the suffix denotes standardisation at all
is unconfirmed.

**Transformations at load:** Unknown. Inspect `df.columns` after loading.

**Raw vs interpreted — what is lost:** Unknown. Needs the Class determination this page cannot
yet make. Column names form apparent pairs (`_X`/`_Z`, `_ORI_TXT`/`_ORI_TXT_STD`); no
relationship between any pair has been established.

**Identifier handling:** Unknown — to confirm with data owner.

---

## Data Quality

### Missingness

| Metric | Value |
|---|---|
| Overall missing (share of all cells) | 18.19–23.54% across the eleven objects (profiler, 2026-07-23) |
| Columns >50% missing | 4 of 23 in both partitions read (`SPECIMEN_COLLECTED_DATE_X`/`_Z`, `ORDER_DATE_X`/`_Z`); `INVESTIGATION_NAME_ORI_TXT_STD` sits just above 50% in both |
| Columns 100% missing | 0 in both partitions read |

No interpretation of the missingness is offered here.

**Columns that matter:** Unknown — ranking columns by consequence needs their descriptions.

| Variable | Missing % | Consequence if unusable |
|---|---:|---|
| | | |
**Disguised missing:** **Not checked.**

- Profiler counts only `""`, `NA`, `N/A`, `NULL`, `null`, `None`, `NaN`, `.` as missing.
- `UNKNOWN`, `NIL`, `9`, `999`, `1900-01-01` all read as *present* — invisible in these figures.
- **Do not read "0.0% missing" as "0.0% unusable"** — sixteen of the 23 columns are reported 0.0% missing in both partitions read and the check is outstanding for every one of them.
- Run `value_counts()` before trusting any 0.0% figure.

### Overlap

**Primary identifier:** `PATIENT_ID_EXTN_X`. The patient ID column is the primary identifier
for every dataset in this catalogue. Its dtype as read, leading zeros, casing and padding are
unknown — read it as `str` and inspect before joining.

**Identifier family:** Unknown — to confirm with data owner. The name matches the identifier
column in [singcloud-event-diagnosis.md](singcloud-event-diagnosis.md) and
[singcloud-dispensed-medication-item.md](singcloud-dispensed-medication-item.md), but **no
join has been tested** and a shared column name is not evidence of a shared identifier space.

**Secondary keys:** Unknown. `BATTERY_ID_ROOT`, `BATTERY_ID_EXT` and `EVENT_EXT` are the other
columns the profiler typed `id_like`.

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
- **Schema drift across partitions:** All eleven objects report 23 columns. Names, order and
  types verified identical in P1 and P10; the other nine are not yet checked.
- **Value-range anomalies:** Not checked.
- **Encoding:** Unknown. The profiler attempts UTF-8 and falls back to latin-1 with
  `errors="replace"` silently, so an object that needed the fallback is indistinguishable
  from one that did not.
- **Missing partitions:** Eleven of at least twenty-two partition numbers are present. This is
  the most consequential open item on the page — any count computed here is a count over an
  incomplete family.
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
| **Free-text / PII exposure** | **Not assessed.** No column is classified Direct ID, Quasi-ID or Free text yet. The profiler typed `BATTERY_ID_ROOT`, `PATIENT_ID_EXTN_X`, `BATTERY_ID_EXT` and `EVENT_EXT` as `id_like` — digit-heavy values worth inspecting first. Absence of a classification here is an outstanding task, **not** a finding that the dataset carries no PII |
| **Attribution / citation** | Unknown — to confirm with data owner |

**Open questions for the data owner:**

1. What is the unit of observation — what does one row represent, and what causes rows to
   multiply?
2. What is this dataset, in one paragraph?
3. What is the source system, and what does the `VW_` prefix denote?
4. Which population is included, and who is excluded by what mechanism?
5. **Do partitions P3, P5, P6, P8, P9, P13–P17 and P20 exist?** If so, why were they not
   profiled, and where are they?
6. Is there a data dictionary? All 23 columns are currently undescribed and unclassified.
7. For each column: is it a source value, a mapped value, or a computed/interpreted one?
8. `INVESTIGATION_NAME_ORI_TXT_STD` — what vocabulary, what version, what mapping rule, and
   what happens on a failed match?
9. What is the relationship between the `_X` / `_Z` pairs, and which should be preferred?
10. Why are `SPECIMEN_COLLECTED_DATE` and `ORDER_DATE` 89–97% empty while `DISPLAY_DATE` is
    fully populated? Which is the reliable event date?
11. Is `PATIENT_ID_EXTN_X` a pseudonym, and is it stable across datasets and across successive
    extracts of this one?
12. Is `PATIENT_ID_EXTN_X` here the same identifier space as in Event Diagnosis and Dispensed
    Medication Item?
13. What are `BATTERY_ID_ROOT`, `BATTERY_ID_EXT` and `EVENT_EXT`, and what do they join to?
14. What is the delimiter and file encoding, and are all eleven objects the same?
15. What date does `26-07-2024` in the object name refer to?
16. Who is the data owner and steward role, what is the approval route, and what lead time
    should a study plan for?

---

## Appendix A — Full column profile

The per-column profile is the *Key Variables* table above and is not repeated here: with
Description, Class, Coding and Sensitivity still outstanding, the two tables would be
identical. Both carry 23 rows, matching the 23 columns declared for every object.

## Appendix B — Change log

| Date | Change | By |
|---|---|---|
| 2026-07-31 | Page created against `template.md` from the profiler run of 2026-07-23. Eleven objects, 49,620,429 rows, 23 columns. Column names and types transcribed from the screenshots for P1 and P10; object-level figures for all eleven. Category from the dataset name and `PATIENT_ID_EXTN_X` as primary identifier, both by catalogue convention. | CCJX |

## Appendix C — Sources

- **Profiler run 2026-07-23** — column names, types and per-column missing % read from
  `source_material/screenshots/mass_columns_screenshots/section_04.png` (objects P1 and P10).
  Object-level figures for the remaining nine objects from the same run.
- `tools/s3_data_catalog.py` — cited only for the profiler's documented behaviour, never for
  any property of this dataset.
- **Not used for column names:** `source_material/imported/profiler_report_full.txt` and
  `column_summary.csv`. These are OCR reconstructions that corrupt column names — verified
  against the screenshots, they invent characters (`EVN_FACILITY._EXTN`) and inject columns
  that do not exist. Numeric fields in them matched the screenshots exactly, but no name on
  this page comes from them.
- **Data owner correspondence — none.** Every governance field on this page is unconfirmed.

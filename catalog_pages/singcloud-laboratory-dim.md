# SingCLOUD — Laboratory Dim

| | |
|---|---|
| **Status** | ⚪ Stub |
| **Profiled on** | 2026-07-23 |
| **Last reviewed** | *not yet reviewed* |

**Objects included in this page**

| # | Object |
|---:|---|
| 1 | `VW_LABORATORY_DIM_F_Export_22-07-2024.csv` |

Under the prefix `common-data/SingCLoud/NonFreeText_Files/`. One object, 315,624 rows, 6
columns, unpartitioned.

---

## Read this first

| | Issue | What to do |
|---|---|---|
| 🔴 | **No patient column** — the only page where the patient-ID-is-primary-key rule cannot apply | Primary identifier is marked n/a deliberately. Candidate keys are `LAB_NAME_ETS_ID` and `LAB_CSN_ID`, neither tested for uniqueness |
| 🔴 | **The join key to the Laboratory families is not obvious** — neither carries any `LAB_*` column | Do not assume a join exists. Ask what links them |
| 🟡 | **No date column** | A code cannot be resolved as it stood at the time of a historical result |
| 🟡 | **315,624 rows is a lot for a laboratory lookup** | Check for duplicate keys before using it as one |
| 🟡 | Named `_F` but shaped like a `_D` dimension table | Files with the fact families by suffix, with the reference tables by structure |

---

## Dataset Overview

**Category:** Laboratory dim — taken from the dataset name. Not yet confirmed against a data
dictionary or the data owner.

**Description:** Unknown — to be filled in.

**Data source:** Unknown — to confirm with data owner.

**Population:** n/a — this object has no patient column, so it does not describe a population
of people. What population of *laboratories* or *lab names* it covers is unknown — to confirm
with data owner.

**Institutional / geographic coverage:** Unknown — to confirm with data owner.

**Unit of observation:** **Unknown — to confirm with data owner.** With 315,624 rows and a
column named `LAB_NAME`, one row per distinct laboratory would be implausibly many for a
single health system — so either the rows are not distinct laboratories, or the object carries
history or per-institution variants. Nothing here establishes which.

**Rows vs people:** 315,624 rows (profiler, 2026-07-23). **Distinct patients: n/a** — there is
no patient column in this object.

**What is *not* in it:** Unknown — to be filled in. What *can* be said exactly: there is no
patient identifier, no date column and no result value. The 6 column names in *Key Variables*
are the complete list.

### Access

| | |
|---|---|
| **Catalogue alias(es)** | Unknown — to be filled in |
| **Source object(s)** | `common-data/SingCLoud/NonFreeText_Files/VW_LABORATORY_DIM_F_Export_22-07-2024.csv` |
| **Partitions** | 1 object, unpartitioned |
| **Format** | CSV by file extension. Delimiter and encoding unknown |
| **Extract date** | Unknown. The object name contains `_Export_22-07-2024` |
| **Refresh cadence** | Unknown — to confirm with data owner |
| **Free-text content** | Unknown. This object sits under `NonFreeText_Files/` |

---

## Key Variables

All 6 columns, in the order printed in the report.

**Type** is the profiler's label and is provisional until pass 2.

**Outstanding until pass 2, for every column:** Description, Class, Coding / units,
Sensitivity. Every column here is unclassified.

| # | Variable | Type | Missing % | Description | Class | Coding / units | Sensitivity |
|---:|---|---|---:|---|---|---|---|
| 1 | `DATA_SOURCE` | categorical | 0.0 | | | | |
| 2 | `LAB_NAME_ETS_ID` | id_like | 0.0 | | | | |
| 3 | `LAB_NAME` | categorical | 0.06 | | | | |
| 4 | `LAB_CODE` | categorical | 0.0 | | | | |
| 5 | `LAB_CSN_ID` | id_like | 0.0 | | | | |
| 6 | `LAB_CSN` | categorical | 0.0 | | | | |

*(profiler, 2026-07-23)*

**`LAB_NAME` is 0.06% empty — the only gap in the object.** Roughly 190 of 315,624 rows carry
a code and a CSN but no name. On a lookup table that is the kind of gap that produces silent
nulls in a joined result.

> **Value strings drift between extracts** (`SINGAPORE PINK IC` vs `SINGAPORE PINK NRIC`).
> This page lists no values for any column. Enumerate the distinct values in your own extract
> before filtering, and re-check them against each new extract — a value string that has
> drifted returns zero rows without raising an error. This caution applies with particular
> force to a lookup table, whose whole purpose is to supply values other queries filter on.

---

## Time Coverage

n/a — this object has no date column. Whether that means it is a current-state snapshot with
no history, or that effective dates exist upstream and were not carried through, is unknown —
to confirm with data owner. It matters: a lookup table without effective dates cannot be
used to resolve a code as it stood at the time of a historical record.

**Date format:** n/a — no date columns.

**Completeness over the period:** n/a — no date columns.

**Variable availability over time:** Unknown.

| Variable | Usable from | Evidence |
|---|---|---|
| | | |

---

## Dataset Information

*Transcribed from the condensed profiler summary, run 2026-07-23.*

| Object | Size (MB) | Rows | Cols | Overall missing % |
|---|---:|---:|---:|---:|
| `VW_LABORATORY_DIM_F_Export_22-07-2024.csv` | 34.92 | 315,624 | 6 | 0.01 |
| **Family total** | **34.92** | **315,624** | 6 | 0.01 |

*The row count above is a lower bound: the profiler reads with `on_bad_lines="skip"`
([tools/s3_data_catalog.py](../tools/s3_data_catalog.py)), so unparseable lines are dropped
silently and never counted.*

| Metric | Value |
|---|---|
| Sample size (distinct patients) | **n/a** — no patient column in this object |
| Schema consistent across partitions | n/a — single object |

---

## Provenance & Processing

Every field here is owner-only, and none is inferred from column naming.

**Collection mechanism:** Unknown — to confirm with data owner.

**Who enters it, and under what incentive:** Unknown — to confirm with data owner.

**Extract pipeline:** Unknown — to confirm with data owner. The object name begins `VW_`; what
that prefix denotes is not documented in any source available here.

**Processing applied:** Unknown — to confirm with data owner.

**Standardisation mappings:** Unknown. No column carries a `_STD` suffix, but a lookup table
is itself the mechanism by which a code becomes a name — so what vocabulary `LAB_CODE` belongs
to is the central provenance question here.

**Transformations at load:** Unknown. Inspect `df.columns` after loading.

**Raw vs interpreted — what is lost:** Unknown. Needs the Class determination this page cannot
yet make.

**Identifier handling:** n/a for patients — no patient column. Whether `LAB_NAME_ETS_ID` and
`LAB_CSN_ID` are stable across extracts is unknown, and matters: if either is re-minted per
extract, a join written against one extract silently breaks against the next.

---

## Data Quality

### Missingness

| Metric | Value |
|---|---|
| Overall missing (share of all cells) | 0.01% (profiler, 2026-07-23) |
| Columns >50% missing | 0 of 6 |
| Columns 100% missing | 0 of 6 |

**Columns that matter:** Unknown — ranking columns by consequence needs their descriptions.
`LAB_NAME` at 0.06% empty is the only column with any gap at all.

| Variable | Missing % | Consequence if unusable |
|---|---:|---|
| | | |
**Disguised missing:** **Not checked.**

- Profiler counts only `""`, `NA`, `N/A`, `NULL`, `null`, `None`, `NaN`, `.` as missing.
- `UNKNOWN`, `NIL`, `9`, `999`, `1900-01-01` all read as *present* — invisible in these figures.
- Five of six columns report 0.0% missing and the check is outstanding for all of them. On a lookup table, a row whose name reads `UNKNOWN` is as useless as one whose name is null, and only the second is counted here.
- Run `value_counts()` before trusting any 0.0% figure.

### Overlap

**Primary identifier:** **n/a — this object has no patient column.** It is the first object in
the catalogue where the convention that the patient ID is the primary identifier cannot apply.
The candidate keys are `LAB_NAME_ETS_ID` and `LAB_CSN_ID`, both typed `id_like`, but which is
the primary key — and whether either is unique across the 315,624 rows — is unknown and has
not been tested.

**Identifier family:** n/a for patient identifiers.

**Secondary keys:** `LAB_CODE` and `LAB_CSN` are the other candidates; both profile as
`categorical`.

**Coding standards:** Unknown — to confirm with data owner. `LAB_CODE` implies a coding
scheme; which one, and what version, is not established.

| Links to | On | Granularity | Cardinality | Overlap tested? | Notes |
|---|---|---|---|---|---|
| [Laboratory](singcloud-laboratory.md) | Unknown | Unknown | Unknown | **no join tested** | The obvious candidate, but note that Laboratory's investigation columns are `INVESTIGATION_NAME_ETS_ID` and `INVESTIGATION_NAME_ORI_TXT` — **no column named `LAB_*` appears in Laboratory at all**, so the join key is not obvious from the names |
| [Laboratory Item FIL](singcloud-laboratory-item-fil.md) | Unknown | Unknown | Unknown | **no join tested** | Same caveat — that family uses `ITEM_NAME_ETS_ID`, not `LAB_*` |

**Known linkage pitfalls:** None recorded — no linkage has been attempted. An empty list, not
a clean bill of health. The absence of any matching `LAB_*` column in the two Laboratory
families is the first thing to resolve.

### Bias

- **Coverage / selection:** Unknown — to confirm with data owner.
- **Recording practice:** Unknown — to confirm with data owner.
- **Changes over time:** Unknown — to confirm with data owner.
- **Ascertainment:** Unknown — to confirm with data owner.

### Other limitations

- **Duplicates:** Not checked, and it is the key question for this object. 315,624 rows is a
  large number for a laboratory lookup; whether keys repeat has not been tested.
- **Schema drift across partitions:** n/a — single object.
- **Value-range anomalies:** Not checked.
- **Encoding:** Unknown. The profiler attempts UTF-8 and falls back to latin-1 with
  `errors="replace"` silently.
- **Fitness for purpose:** **Cannot be assessed yet.** This page establishes neither what the
  object is nor what one row represents.

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
| **Free-text / PII exposure** | **Not assessed, but the risk profile here is different from every other page in the catalogue: this object carries no patient column.** The profiler typed `LAB_NAME_ETS_ID` and `LAB_CSN_ID` as `id_like`, but they are digit-heavy identifiers of laboratories or tests, not people. Absence of a classification remains an outstanding task, **not** a finding that the object carries no PII — that conclusion needs someone to confirm the six columns hold what their names suggest |
| **Attribution / citation** | Unknown — to confirm with data owner |

**Open questions for the data owner:**

1. What is the unit of observation? Why does a laboratory lookup have 315,624 rows?
2. **What joins this object to `VW_LABORATORY_F` and `VW_LABORATORY_ITEM_FIL_F`?** Neither
   carries a `LAB_*` column, so the key is not apparent from the names.
3. Are `LAB_NAME_ETS_ID` and `LAB_CSN_ID` unique, and which is the primary key?
4. Are those identifiers stable across extracts, or re-minted each time?
5. Why is this object named `_F` when its shape matches the `_D` dimension tables?
6. What do `ETS` and `CSN` stand for? The same suffixes appear across the catalogue.
7. What coding scheme does `LAB_CODE` belong to, and what version?
8. **There is no date column.** Is this a current-state snapshot only? Can a code be resolved
   as it stood at the time of a historical result?
9. Roughly 190 rows have a `LAB_CODE` but no `LAB_NAME`. What are they?
10. Is the 0.01% missing figure genuine, or does the object use sentinel values such as
    `UNKNOWN`?
11. Are there duplicate keys?
12. What is the delimiter and file encoding?
13. Who is the data owner and steward role, what is the approval route, and what lead time
    should a study plan for?

---

## Appendix A — Full column profile

The per-column profile is the *Key Variables* table above and is not repeated here: with
Description, Class, Coding and Sensitivity still outstanding, the two tables would be
identical. Both carry 6 rows, matching the 6 columns declared.

## Appendix B — Change log

| Date | Change | By |
|---|---|---|
| 2026-07-31 | Page created against `template.md` from the profiler run of 2026-07-23. One object, 315,624 rows, 6 columns, all figures transcribed from the screenshots. Category from the dataset name. **Primary identifier marked n/a** — this object has no patient column, the first exception in the catalogue to the convention that the patient ID is always the primary identifier. | CCJX |

## Appendix C — Sources

- **Profiler run 2026-07-23** — the complete object block, read from
  `source_material/screenshots/mass_columns_screenshots/section_16.png`.
- `tools/s3_data_catalog.py` — cited only for the profiler's documented behaviour, never for
  any property of this object.
- **Not used for column names:** `source_material/imported/profiler_report_full.txt` and
  `column_summary.csv`, which are OCR reconstructions that corrupt column names.
- **Data owner correspondence — none.** Every governance field on this page is unconfirmed.

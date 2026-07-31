# SingCLOUD — MOH OB Operation

| | |
|---|---|
| **Status** | ⚪ Stub |
| **Profiled on** | 2026-07-23 |
| **Last reviewed** | *not yet reviewed* |

**Objects included in this page**

| # | Object |
|---:|---|
| 1 | `VW_MOH_OB_OPERATION_F_Export_31-07-2024_P1.csv` |
| 2 | `VW_MOH_OB_OPERATION_F_Export_31-07-2024_P2.csv` |
| 3 | `VW_MOH_OB_OPERATION_F_Export_31-07-2024_P3.csv` |

All sit under the prefix `common-data/SingCLoud/NonFreeText_Files/`. Three objects, 7,451,330
rows, 36 columns each.

---

## Read this first

| | Issue | What to do |
|---|---|---|
| 🔴 | **Patient column is `NRIC_X`** — a national identity number by name, not an obvious pseudonym | **Confirm whether it is pseudonymised before handling the data.** This gates everything else |
| 🔴 | **P3 is a strong outlier** — a tenth the size of P1/P2 and **91.67% missing** against their 14.21% and 9.14% | Do not pool P3 with the others without understanding why |
| 🟡 | **`surgeonsmc` and `anaessmc` may identify clinicians**, not patients | A separate disclosure question from patient PII |
| 🟡 | **`_merge_tosptable` and `_merge_tospclaimlimit`** look like join-indicator artefacts of the pipeline | Do not filter on them without confirmation |
| 🟡 | `date_X`, `date_Z`, `dt_tosp` are **100% empty** in P1 | Deprecated, or populated in a source not delivered? |
| 📋 | Only P1 column-transcribed | P3 makes checking P2 and P3 a priority, not a formality |

---

## Dataset Overview

**Category:** MOH OB operation — taken from the dataset name. Not yet confirmed against a data
dictionary or the data owner. What `MOH` and `OB` denote here is unconfirmed.

**Description:** Unknown — to be filled in.

**Data source:** Unknown — to confirm with data owner.

**Population:** Unknown — to confirm with data owner.

**Institutional / geographic coverage:** Unknown — to confirm with data owner.

**Unit of observation:** **Unknown — to confirm with data owner.** What one row represents,
and what causes rows to multiply, are not established. Note that `seq_no` exists alongside
`pataccno`, which is the shape a repeating sequence per account takes — but that reading is
not established and is not assumed here.

**Rows vs people:** 7,451,330 rows (profiler, 2026-07-23, three objects summed); distinct
patients **not counted**.

**What is *not* in it:** Unknown — to be filled in. The 36 column names in *Key Variables*
are the complete column list for the partition read.

### Access

| | |
|---|---|
| **Catalogue alias(es)** | Unknown — to be filled in |
| **Source object(s)** | `common-data/SingCLoud/NonFreeText_Files/VW_MOH_OB_OPERATION_F_Export_31-07-2024_P{1..3}.csv` |
| **Partitions** | 3 objects, P1–P3, contiguous |
| **Format** | CSV by file extension. Delimiter and encoding unknown |
| **Extract date** | Unknown. All three object names contain `_Export_31-07-2024_` |
| **Refresh cadence** | Unknown — to confirm with data owner |
| **Free-text content** | Unknown. These objects sit under `NonFreeText_Files/` |

---

## Key Variables

All 36 columns, in the order printed in the report. Transcribed in full from **P1**.

**Type** is the profiler's label and is provisional until pass 2.

**Outstanding until pass 2, for every column:** Description, Class, Coding / units,
Sensitivity. Every column here is unclassified.

**Note the casing.** This family mixes upper-case (`DATA_SOURCE`, `NRIC_X`) with lower-case
(`pataccno`, `seq_no`, `opfee_imp`) and two leading-underscore names (`_merge_tosptable`,
`_merge_tospclaimlimit`). Copy each character for character.

| # | Variable | Type | P1 | Description | Class | Coding / units | Sensitivity |
|---:|---|---|---:|---|---|---|---|
| 1 | `DATA_SOURCE` | categorical | 0.0 | | | | |
| 2 | `NRIC_X` | id_like | 0.0 | | | | |
| 3 | `pataccno` | categorical | 0.0 | | | | |
| 4 | `seq_no` | numeric | 0.0 | | | | |
| 5 | `patuintype` | categorical | 0.0 | | | | |
| 6 | `tospcode` | categorical | 0.0 | | | | |
| 7 | `date_X` | categorical | 100.0 | | | | |
| 8 | `date_Z` | categorical | 100.0 | | | | |
| 9 | `nature` | categorical | 0.0 | | | | |
| 10 | `surgeonsmc` | categorical | 0.0 | | | | |
| 11 | `surgeonfee` | numeric | 0.0 | | | | |
| 12 | `anaessmc` | categorical | 62.94 | | | | |
| 13 | `anaesfee` | numeric | 0.0 | | | | |
| 14 | `facilityfee` | numeric | 0.0 | | | | |
| 15 | `surgimplchrg` | numeric | 0.0 | | | | |
| 16 | `numofimplant` | numeric | 83.01 | | | | |
| 17 | `dt_tosp` | categorical | 100.0 | | | | |
| 18 | `date_tosp_X` | date | 0.0 | | | | |
| 19 | `date_tosp_Z` | date | 0.0 | | | | |
| 20 | `policy_effective_date` | date | 0.0 | | | | |
| 21 | `anatomicalsystem` | categorical | 7.93 | | | | |
| 22 | `tospdescription` | categorical | 7.93 | | | | |
| 23 | `tosptable` | categorical | 7.94 | | | | |
| 24 | `mshl2` | numeric | 8.43 | | | | |
| 25 | `_merge_tosptable` | categorical | 7.94 | | | | |
| 26 | `_merge_tospclaimlimit` | categorical | 0.01 | | | | |
| 27 | `wtosp` | numeric | 8.43 | | | | |
| 28 | `date_adm_X` | date | 0.01 | | | | |
| 29 | `date_adm_Z` | date | 0.01 | | | | |
| 30 | `date_dis_X` | date | 0.01 | | | | |
| 31 | `date_dis_Z` | date | 0.01 | | | | |
| 32 | `msvtosp` | numeric | 8.43 | | | | |
| 33 | `mshtosp` | numeric | 8.43 | | | | |
| 34 | `mshsurgimp` | numeric | 0.01 | | | | |
| 35 | `opfee` | numeric | 0.01 | | | | |
| 36 | `opfee_imp` | numeric | 0.01 | | | | |

*(P1 is missing %; profiler, 2026-07-23)*

**`date_X`, `date_Z` and `dt_tosp` are 100% empty in P1** and all three profile as
`categorical` rather than `date` — consistent with a column that is entirely empty, since the
profiler has no values to parse.

**Two columns begin with `_merge_`.** In some statistical tooling that is the conventional name
for a join-indicator variable produced during a merge. Whether that is what these are, and
whether they are meaningful to an analyst or an artefact of the extract pipeline, is unknown —
to confirm with data owner. Do not filter on them without an answer.

> **Value strings drift between extracts** (`SINGAPORE PINK IC` vs `SINGAPORE PINK NRIC`).
> This page lists no values for any column. Enumerate the distinct values in your own extract
> before filtering, and re-check them against each new extract — a value string that has
> drifted returns zero rows without raising an error.

---

## Time Coverage

| Date column | Start | End | Source |
|---|---|---|---|
| `date_tosp_X` | Unknown | Unknown | — |
| `date_tosp_Z` | Unknown | Unknown | — |
| `policy_effective_date` | Unknown | Unknown | — |
| `date_adm_X` | Unknown | Unknown | — |
| `date_adm_Z` | Unknown | Unknown | — |
| `date_dis_X` | Unknown | Unknown | — |
| `date_dis_Z` | Unknown | Unknown | — |
| `date_X` | Unknown | Unknown | — |
| `date_Z` | Unknown | Unknown | — |
| `dt_tosp` | Unknown | Unknown | — |

No date range is established and no principal date column is identified. The last three rows
are 100% empty in P1, so they can supply no range at all.

**Date format:** Unknown. The profiler parses with `dayfirst=True`, so `01/02/2021` reads as
1 February. If any column is month-first, every date derived from it is wrong and nothing
raises. `policy_effective_date` is the only date column with no `_X` / `_Z` suffix, which is
worth asking about.

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
| `…_P1.csv` | 1,295.65 | 3,446,325 | 36 | 14.21 |
| `…_P2.csv` | 1,273.37 | 3,298,973 | 36 | 9.14 |
| `…_P3.csv` | 125.91 | 706,032 | 36 | 91.67 |
| **Family total** | **2,694.93** | **7,451,330** | 36 | — |

*Every row count above is a lower bound: the profiler reads with `on_bad_lines="skip"`
([tools/s3_data_catalog.py](../tools/s3_data_catalog.py)), so unparseable lines are dropped
silently and never counted.*

Family size and rows are sums of the three reported figures. Family missing % is left blank
deliberately: the per-object percentages are shares of three different denominators and cannot
be averaged.

**P3 is a strong outlier and should be understood before use.** It is a tenth the size of P1
and P2 and reports **91.67% missing** against their 14.21% and 9.14%. A partition that is
overwhelmingly empty usually means one of three things — a truncated write, a different
schema populated differently, or a genuinely sparse tail — and which it is, is unknown. Do not
pool P3 with P1 and P2 without checking.

| Metric | Value |
|---|---|
| Sample size (distinct patients) | **not counted** — the profiler does not compute it |
| Schema consistent across partitions | 36 columns in every object. Names, order and types transcribed from P1 only; P2 and P3 are not yet checked column by column, and P3's missing profile suggests they should be |

---

## Provenance & Processing

Every field here is owner-only, and none is inferred from column naming.

**Collection mechanism:** Unknown — to confirm with data owner.

**Who enters it, and under what incentive:** Unknown — to confirm with data owner. The
presence of fee columns (`surgeonfee`, `anaesfee`, `facilityfee`, `opfee`) alongside clinical
ones (`nature`, `anatomicalsystem`, `tospdescription`) means this may be billing-entered,
clinically-entered, or both — and `template.md` notes those fail differently.

**Extract pipeline:** Unknown — to confirm with data owner. The object name begins `VW_`; what
that prefix denotes is not documented in any source available here. The two `_merge_` columns
suggest a join happened somewhere in the pipeline, but by what rule and against what is not
established.

**Processing applied:** Unknown — to confirm with data owner.

**Standardisation mappings:** n/a — no column name on this page carries a `_STD` suffix.

**Transformations at load:** Unknown. Inspect `df.columns` after loading — this family's mixed
casing and leading-underscore names are the ones most likely to be altered by a loader that
normalises case or strips punctuation.

**Raw vs interpreted — what is lost:** Unknown. Needs the Class determination this page cannot
yet make. `date_adm_X` / `_Z`, `date_dis_X` / `_Z` and `date_tosp_X` / `_Z` form apparent
pairs; no relationship between any pair has been established.

**Identifier handling:** Unknown — to confirm with data owner. This family's patient column is
`NRIC_X` — a name that on its face refers to a national identity number rather than a
project-minted pseudonym. **Whether it is pseudonymised is the single most important question
on this page** and must be answered before the data is handled.

---

## Data Quality

### Missingness

| Metric | Value |
|---|---|
| Overall missing (share of all cells) | 9.14–91.67% across the three objects (profiler, 2026-07-23) |
| Columns >50% missing | 4 of 36 in P1 (`date_X`, `date_Z`, `dt_tosp`, `numofimplant`), plus `anaessmc` at 62.94 |
| Columns 100% missing | 3 in P1 (`date_X`, `date_Z`, `dt_tosp`) |

No interpretation of the missingness is offered here.

**Columns that matter:** Unknown — ranking columns by consequence needs their descriptions.

| Variable | Missing % | Consequence if unusable |
|---|---:|---|
| | | |
**Disguised missing:** **Not checked.**

- Profiler counts only `""`, `NA`, `N/A`, `NULL`, `null`, `None`, `NaN`, `.` as missing.
- `UNKNOWN`, `NIL`, `9`, `999`, `1900-01-01` all read as *present* — invisible in these figures.
- **Do not read "0.0% missing" as "0.0% unusable"** — thirteen columns are reported 0.0% missing in P1 and the check is outstanding for every one of them. The fee columns are the place to start: a fee of `0` and a fee that was never recorded are different facts, and the profiler cannot tell them apart.
- Run `value_counts()` before trusting any 0.0% figure.

### Overlap

**Primary identifier:** `NRIC_X`. The patient ID column is the primary identifier for every
dataset in this catalogue. Its dtype as read, leading zeros, casing and padding are unknown —
read it as `str` and inspect before joining. Singapore NRIC values carry a trailing check
letter and leading zeros, both of which a numeric read would destroy.

**Identifier family:** Unknown — to confirm with data owner. `NRIC_X` differs in name from
both `PATIENT_ID_EXTN_X` (clinical families) and `FK_PATIENT_ID_X` (IP Billing); **no join has
been tested** between any of them.

**Secondary keys:** Unknown. `pataccno` and `seq_no` are candidates but neither profiles as
`id_like`. `NRIC_X` is the only column the profiler typed `id_like`.

**Coding standards:** Unknown — to confirm with data owner. `tospcode` and `tosptable` imply a
coded table of procedures, and `anatomicalsystem` implies a controlled list, but neither
vocabulary nor version is established.

| Links to | On | Granularity | Cardinality | Overlap tested? | Notes |
|---|---|---|---|---|---|
| Unknown | Unknown | Unknown | Unknown | **no join tested** | No linkage established. See also [singcloud-moh-ob-procedure](singcloud-moh-ob-procedure.md) when that page exists — the two families share a naming stem but no relationship has been checked |

**Known linkage pitfalls:** None recorded — no linkage has been attempted. An empty list, not
a clean bill of health.

### Bias

- **Coverage / selection:** Unknown — to confirm with data owner.
- **Recording practice:** Unknown — to confirm with data owner.
- **Changes over time:** Unknown — to confirm with data owner.
- **Ascertainment:** Unknown — to confirm with data owner.

### Other limitations

- **Duplicates:** Not checked.
- **Schema drift across partitions:** All three objects report 36 columns. Only P1 has been
  transcribed column by column; P3's 91.67% missing figure makes checking the other two a
  priority rather than a formality.
- **Value-range anomalies:** Not checked. The fee and charge columns are unbounded numerics
  with no stated units.
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
| **Free-text / PII exposure** | **Not assessed, and this page carries the strongest prima facie signal in the catalogue so far.** The patient column is named `NRIC_X` and profiles as `id_like`. If it holds NRIC values rather than a pseudonym, this is direct identifier data and the handling requirements differ sharply from the other families. `surgeonsmc` and `anaessmc` are also identifier-shaped names, and would identify *clinicians* rather than patients — a separate disclosure question. Absence of a classification here is an outstanding task, **not** a finding that the dataset carries no PII |
| **Attribution / citation** | Unknown — to confirm with data owner |

**Open questions for the data owner:**

1. **Is `NRIC_X` a pseudonym or a real NRIC?** This gates everything else on the page.
2. Do `surgeonsmc` and `anaessmc` identify individual clinicians, and is that permitted for
   release?
3. What is the unit of observation — what does one row represent, and what does `seq_no`
   sequence within?
4. What is this dataset, in one paragraph? What do `MOH`, `OB` and `tosp` stand for?
5. **Why is P3 91.67% missing** when P1 and P2 are 14.21% and 9.14%? Is it truncated?
6. Which population is included, and who is excluded by what mechanism?
7. Is there a data dictionary? All 36 columns are currently undescribed and unclassified.
8. `date_X`, `date_Z` and `dt_tosp` are 100% empty in P1 — deprecated, or populated in a
   source not delivered here?
9. What are `_merge_tosptable` and `_merge_tospclaimlimit`? Are they analytic artefacts of the
   extract pipeline?
10. What vocabulary do `tospcode`, `tosptable` and `anatomicalsystem` use, and what version?
11. What are the units of `surgeonfee`, `anaesfee`, `facilityfee`, `surgimplchrg`, `opfee` and
    `opfee_imp` — dollars or cents, and gross or net of subsidy?
12. What do `mshl2`, `wtosp`, `msvtosp`, `mshtosp` and `mshsurgimp` represent?
13. What is the relationship between the `_X` / `_Z` date pairs, and which should be preferred?
14. Is `NRIC_X` linkable to `PATIENT_ID_EXTN_X` or `FK_PATIENT_ID_X`? Does a crosswalk exist?
15. How does this family relate to `VW_MOH_OB_PROCEDURE_F` and `VW_MOH_OB_WO_SHI_F`?
16. What is the delimiter and file encoding, and are all three objects the same?
17. What date does `31-07-2024` in the object name refer to?
18. Who is the data owner and steward role, what is the approval route, and what lead time
    should a study plan for?

---

## Appendix A — Full column profile

The per-column profile is the *Key Variables* table above and is not repeated here: with
Description, Class, Coding and Sensitivity still outstanding, the two tables would be
identical. Both carry 36 rows, matching the 36 columns declared for every object.

## Appendix B — Change log

| Date | Change | By |
|---|---|---|
| 2026-07-31 | Page created against `template.md` from the profiler run of 2026-07-23. Three objects, 7,451,330 rows, 36 columns. Column names, types and missing % transcribed from the screenshots for P1; object-level figures for all three. Category from the dataset name and `NRIC_X` as primary identifier, both by catalogue convention. | CCJX |

## Appendix C — Sources

- **Profiler run 2026-07-23** — the complete P1 block, read from
  `source_material/screenshots/mass_columns_screenshots/section_17.png`. Object-level figures
  for P2 and P3 from the same run.
- `tools/s3_data_catalog.py` — cited only for the profiler's documented behaviour, never for
  any property of this dataset.
- **Not used for column names:** `source_material/imported/profiler_report_full.txt` and
  `column_summary.csv`, which are OCR reconstructions that corrupt column names.
- **Data owner correspondence — none.** Every governance field on this page is unconfirmed.

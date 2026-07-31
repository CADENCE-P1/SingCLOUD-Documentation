# SingCLOUD — MED Billing

| | |
|---|---|
| **Status** | ⚪ Stub |
| **Profiled on** | 2026-07-23 |
| **Last reviewed** | *not yet reviewed* |

**Objects included in this page**

`VW_MED_BILLING_F_Export_{date}_P{n}.csv`, under the prefix
`common-data/SingCLoud/NonFreeText_Files/VW_MED_BILLING_F/` — note the family has its own
subdirectory, unlike IP Billing.

| # | Object | # | Object |
|---:|---|---:|---|
| 1 | `…_19-08-2024_P1.csv` | 10 | `…_19-08-2024_P19.csv` |
| 2 | `…_19-08-2024_P5.csv` | 11 | `…_20-08-2024_P21.csv` |
| 3 | `…_19-08-2024_P6.csv` | 12 | `…_20-08-2024_P22.csv` |
| 4 | `…_19-08-2024_P8.csv` | 13 | `…_20-08-2024_P23.csv` |
| 5 | `…_19-08-2024_P10.csv` | 14 | `…_20-08-2024_P24.csv` |
| 6 | `…_19-08-2024_P11.csv` | 15 | `…_20-08-2024_P26.csv` |
| 7 | `…_19-08-2024_P14.csv` | 16 | `…_20-08-2024_P30.csv` |
| 8 | `…_19-08-2024_P15.csv` | 17 | `…_20-08-2024_P33.csv` |
| 9 | `…_19-08-2024_P16.csv` | | |

Seventeen objects, 93,302,155 rows, 23 columns each.

---

## Read this first

| | Issue | What to do |
|---|---|---|
| 🔴 | **The object list is incomplete** — numbering runs to at least P33 but only 17 are indexed | Totals are a lower bound, not a family total |
| 🔴 | **Two extract dates** — P1–P19 are `19-08-2024`, P21+ are `20-08-2024` | Check for cross-extract row duplication before pooling |
| 🟡 | **`ROUTE_OF_ADMINISTRATION` is 99.98–100% empty** in all three partitions read | Effectively no data |
| 🟡 | **`DRUG_CODE`/`DRUG_DESC` emptiness varies sharply by partition** — 66.42% in P1, 50.89% in P10 | Half to two thirds of rows carry no drug detail. What distinguishes them is unknown |
| ⚠ | **`section_17.png` is damaged** where this family appears there — a stitch seam swallowed one header | P1 and P10 came from the undamaged `section_16.png`, so nothing here rests on the seam. P33 stops at column 13 because of it |

---

## Dataset Overview

**Category:** MED billing — taken from the dataset name. Not yet confirmed against a data
dictionary or the data owner.

**Description:** Unknown — to be filled in.

**Data source:** Unknown — to confirm with data owner.

**Population:** Unknown — to confirm with data owner.

**Institutional / geographic coverage:** Unknown — to confirm with data owner.
`INSTITUTION_CODE` and `INSTITUTION_NAME` are present and 0.0% missing, so the answer is in
the data — but it has not been enumerated here.

**Unit of observation:** **Unknown — to confirm with data owner.** What one row represents,
and what causes rows to multiply, are not established.

**Rows vs people:** 93,302,155 rows across the seventeen indexed objects (profiler,
2026-07-23) — a lower bound, since the object list is incomplete. Distinct patients **not
counted**.

**What is *not* in it:** Unknown — to be filled in. The 23 column names in *Key Variables*
are the complete column list for the partitions read.

### Access

| | |
|---|---|
| **Catalogue alias(es)** | Unknown — to be filled in |
| **Source object(s)** | `common-data/SingCLoud/NonFreeText_Files/VW_MED_BILLING_F/VW_MED_BILLING_F_Export_{date}_P{n}.csv` |
| **Partitions** | 17 indexed, numbering runs to at least P33 — see above |
| **Format** | CSV by file extension. Delimiter and encoding unknown |
| **Extract date** | Two dates in the object names: `19-08-2024` and `20-08-2024` |
| **Refresh cadence** | Unknown — to confirm with data owner |
| **Free-text content** | Unknown. These objects sit under `NonFreeText_Files/` |

---

## Key Variables

All 23 columns, in the order printed in the report. Transcribed in full from **P1** and
**P10**, with **P33** confirming names and the first thirteen figures.

**Type** is the profiler's label and is provisional until pass 2.

**Outstanding until pass 2, for every column:** Description, Class, Coding / units,
Sensitivity. Every column here is unclassified.

| # | Variable | Type | P1 | P10 | P33 | Description | Class | Coding / units | Sensitivity |
|---:|---|---|---:|---:|---:|---|---|---|---|
| 1 | `DATA_SOURCE` | categorical | 0.0 | 0.0 | 0.0 | | | | |
| 2 | `PATIENT_CODE_X` | id_like | 0.0 | 0.0 | 0.0 | | | | |
| 3 | `CASE_NO` | id_like | 28.99 | 15.92 | 6.91 | | | | |
| 4 | `BILL_NO` | categorical | 47.94 | 38.97 | 58.8 | | | | |
| 5 | `ITEM_CODE` | id_like | 0.0 | 0.0 | 0.01 | | | | |
| 6 | `ITEM_DESC` | categorical | 0.0 | 0.0 | 0.0 | | | | |
| 7 | `DRUG_CODE` | categorical | 66.42 | 50.89 | 60.03 | | | | |
| 8 | `DRUG_DESC` | categorical | 66.42 | 50.89 | 60.03 | | | | |
| 9 | `DRUG_DOSE_FORM` | categorical | 11.28 | 16.66 | 0.42 | | | | |
| 10 | `DRUG_STRENGTH` | numeric | 11.26 | 14.07 | 14.59 | | | | |
| 11 | `BILLING_QTY` | numeric | 0.0 | 0.0 | 0.0 | | | | |
| 12 | `UOM` | categorical | 0.0 | 0.0 | 0.0 | | | | |
| 13 | `ROUTE_OF_ADMINISTRATION` | categorical | 99.98 | 100.0 | 100.0 | | | | |
| 14 | `INSTITUTION_CODE` | categorical | 0.0 | 0.0 | not read | | | | |
| 15 | `INSTITUTION_NAME` | categorical | 0.0 | 0.0 | not read | | | | |
| 16 | `BILLING_TRX_DATE_X` | date | 0.0 | 0.0 | not read | | | | |
| 17 | `BILLING_TRX_DATE_Z` | date | 0.0 | 0.0 | not read | | | | |
| 18 | `BILLING_FULL_AMOUNT` | numeric | 0.0 | not read | not read | | | | |
| 19 | `BILLING_PAYABLE_AMOUNT` | numeric | 0.0 | not read | not read | | | | |
| 20 | `BILLING_PAID_AMOUNT` | numeric | 0.0 | not read | not read | | | | |
| 21 | `BILLING_TAX_AMOUNT` | numeric | 0.0 | not read | not read | | | | |
| 22 | `BILLING_SUBSIDY_AMOUNT` | numeric | 0.0 | not read | not read | | | | |
| 23 | `BILLING_SURCHARGE_AMOUNT` | categorical | 66.23 | not read | not read | | | | |

*(missing %; profiler, 2026-07-23)*

**`ROUTE_OF_ADMINISTRATION` is 99.98–100% empty in all three partitions read** — effectively
no data at all.

**`DRUG_CODE` and `DRUG_DESC` share an identical missing percentage** within each partition —
66.42 in P1, 50.89 in P10, 60.03 in P33 — so between half and two thirds of rows carry
neither. What distinguishes a row with drug detail from one without is not established, and
the share varies substantially by partition.

> **Value strings drift between extracts** (`SINGAPORE PINK IC` vs `SINGAPORE PINK NRIC`).
> This page lists no values for any column. Enumerate the distinct values in your own extract
> before filtering, and re-check them against each new extract — a value string that has
> drifted returns zero rows without raising an error.

---

## Time Coverage

| Date column | Start | End | Source |
|---|---|---|---|
| `BILLING_TRX_DATE_X` | Unknown | Unknown | — |
| `BILLING_TRX_DATE_Z` | Unknown | Unknown | — |

Two date columns, both fully populated in the partition read. No range is established.

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

*Transcribed from the condensed profiler summary, run 2026-07-23. **Incomplete** — sixteen
partition numbers in the range are not indexed.*

| Object | Size (MB) | Rows | Overall missing % |
|---|---:|---:|---:|
| `…_19-08-2024_P1.csv` | 1,250.37 | 4,273,012 | 17.33 |
| `…_19-08-2024_P5.csv` | 1,164.70 | 3,934,358 | 14.97 |
| `…_19-08-2024_P6.csv` | 1,513.73 | 5,122,582 | 15.14 |
| `…_19-08-2024_P8.csv` | 1,569.81 | 5,317,646 | 15.23 |
| `…_19-08-2024_P10.csv` | 1,530.23 | 5,166,969 | 14.87 |
| `…_19-08-2024_P11.csv` | 1,569.60 | 5,303,565 | 14.91 |
| `…_19-08-2024_P14.csv` | 1,765.35 | 5,991,381 | 15.57 |
| `…_19-08-2024_P15.csv` | 1,916.33 | 6,530,611 | 15.97 |
| `…_19-08-2024_P16.csv` | 2,043.50 | 6,984,406 | 16.23 |
| `…_19-08-2024_P19.csv` | 1,127.73 | 3,875,659 | 16.44 |
| `…_20-08-2024_P21.csv` | 1,588.14 | 5,472,281 | 16.63 |
| `…_20-08-2024_P22.csv` | 1,646.30 | 5,651,953 | 16.06 |
| `…_20-08-2024_P23.csv` | 1,641.87 | 5,639,141 | 16.09 |
| `…_20-08-2024_P24.csv` | 1,737.43 | 5,978,376 | 16.17 |
| `…_20-08-2024_P26.csv` | 1,582.19 | 5,444,896 | 16.24 |
| `…_20-08-2024_P30.csv` | 1,838.15 | 6,316,180 | 15.88 |
| `…_20-08-2024_P33.csv` | 1,838.73 | 6,299,139 | 15.03 |
| **Sum over indexed objects** | **27,324.16** | **93,302,155** | — |

All objects report 23 columns.

*The sum is a **lower bound in two ways**: the object list above is incomplete, and every row
count is itself a lower bound because the profiler reads with `on_bad_lines="skip"`
([tools/s3_data_catalog.py](../tools/s3_data_catalog.py)), dropping unparseable lines
silently. It is not a family total.*

| Metric | Value |
|---|---|
| Sample size (distinct patients) | **not counted** — the profiler does not compute it |
| Schema consistent across partitions | 23 columns in every indexed object; names, order and types verified identical in P1 and P10, with P33 confirming the first thirteen. The remaining fourteen are not yet checked column by column |

---

## Provenance & Processing

Every field here is owner-only, and none is inferred from column naming.

**Collection mechanism:** Unknown — to confirm with data owner.

**Who enters it, and under what incentive:** Unknown — to confirm with data owner. This is a
billing dataset, and `template.md` notes that billing-entered and clinically-entered fields
fail differently.

**Extract pipeline:** Unknown — to confirm with data owner. The object name begins `VW_`; what
that prefix denotes is not documented in any source available here.

**Processing applied:** Unknown — to confirm with data owner.

**Standardisation mappings:** n/a — no column name on this page carries a `_STD` suffix.

**Transformations at load:** Unknown. Inspect `df.columns` after loading.

**Raw vs interpreted — what is lost:** Unknown. Needs the Class determination this page cannot
yet make. `BILLING_TRX_DATE_X` / `_Z` form an apparent pair, and `DRUG_CODE` / `DRUG_DESC` and
`INSTITUTION_CODE` / `INSTITUTION_NAME` look like code-and-label pairs; no relationship between
any pair has been established.

**Identifier handling:** Unknown — to confirm with data owner.

---

## Data Quality

### Missingness

| Metric | Value |
|---|---|
| Overall missing (share of all cells) | 14.87–17.33% across the seventeen indexed objects (profiler, 2026-07-23) |
| Columns >50% missing | 4 of 23 in P1 (`DRUG_CODE`, `DRUG_DESC`, `ROUTE_OF_ADMINISTRATION`, `BILLING_SURCHARGE_AMOUNT`); 2 in P10 (`DRUG_CODE`/`DRUG_DESC` fall to 50.89, `ROUTE_OF_ADMINISTRATION` stays at 100) |
| Columns 100% missing | 1 in P10 and P33 (`ROUTE_OF_ADMINISTRATION`); 99.98% in P1 |

No interpretation of the missingness is offered here.

**Columns that matter:** Unknown — ranking columns by consequence needs their descriptions.

| Variable | Missing % | Consequence if unusable |
|---|---:|---|
| | | |
**Disguised missing:** **Not checked, and the amount columns are the priority.**

- Profiler counts only `""`, `NA`, `N/A`, `NULL`, `null`, `None`, `NaN`, `.` as missing.
- `UNKNOWN`, `NIL`, `9`, `999`, `1900-01-01` all read as *present* — invisible in these figures.
- Six amount columns report 0.0% missing; on billing data a recorded `0` and a value that was never recorded are different facts, and the profiler cannot tell them apart. **Do not read "0.0% missing" as "0.0% unusable"** until someone has run `value_counts()`.
- Run `value_counts()` before trusting any 0.0% figure.

### Overlap

**Primary identifier:** `PATIENT_CODE_X`. The patient ID column is the primary identifier for
every dataset in this catalogue. Its dtype as read, leading zeros, casing and padding are
unknown — read it as `str` and inspect before joining.

**Identifier family:** Unknown — to confirm with data owner. `PATIENT_CODE_X` differs in name
from `FK_PATIENT_ID_X` (IP Billing), `PATIENT_ID_EXTN_X` (clinical families) and `NRIC_X`
(MOH OB Operation). **No join has been tested** between any of them. Four differently-named
patient columns across one catalogue is itself the finding worth chasing.

**Secondary keys:** Unknown. `CASE_NO` and `ITEM_CODE` also profile as `id_like`; `BILL_NO`
does not, despite the name.

**Coding standards:** Unknown — to confirm with data owner. `DRUG_CODE` implies a drug
vocabulary and a `VW_DRUG_D` dimension object exists in the same run, but no join has been
tested and the relationship is not established.

| Links to | On | Granularity | Cardinality | Overlap tested? | Notes |
|---|---|---|---|---|---|
| Unknown | Unknown | Unknown | Unknown | **no join tested** | `DRUG_CODE` and the same-run `VW_DRUG_D` object share naming, but no linkage has been established |

**Known linkage pitfalls:** None recorded — no linkage has been attempted. An empty list, not
a clean bill of health.

### Bias

- **Coverage / selection:** Unknown — to confirm with data owner.
- **Recording practice:** Unknown — to confirm with data owner.
- **Changes over time:** Unknown — to confirm with data owner.
- **Ascertainment:** Unknown — to confirm with data owner.

### Other limitations

- **Duplicates:** Not checked. The two extract dates make this more pressing than usual.
- **Schema drift across partitions:** All indexed objects report 23 columns. Only one partition
  has been transcribed in full.
- **Value-range anomalies:** Not checked. The amount columns are unbounded numerics with no
  stated units.
- **Encoding:** Unknown. The profiler attempts UTF-8 and falls back to latin-1 with
  `errors="replace"` silently.
- **Damaged source screenshot:** One block of this family sits across a stitch seam in
  `section_17.png`, where two scrolled captures were joined and a line was lost — which is why
  P33's columns 14–23 could not be read there. The family's P1 and P10 blocks appear
  undamaged in `section_16.png` and were transcribed in full from there, so nothing on this
  page now rests on the damaged region.
- **Incomplete object list:** Any count computed from the table above is a count over an
  unknown fraction of the family.
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
| **Free-text / PII exposure** | **Not assessed.** No column is classified Direct ID, Quasi-ID or Free text yet. The profiler typed `PATIENT_CODE_X`, `CASE_NO` and `ITEM_CODE` as `id_like`. This is patient-level medication and financial data together — what was dispensed, to whom, at what cost — which is a distinct sensitivity question from either the clinical or the billing families alone. Absence of a classification here is an outstanding task, **not** a finding that the dataset carries no PII |
| **Attribution / citation** | Unknown — to confirm with data owner |

**Open questions for the data owner:**

1. **How many partitions does this family have?** Numbering runs to at least P33 but only
   seventeen are indexed. A definitive file list is needed before any count from this page is
   used.
2. Are `_Export_19-08-2024_` and `_Export_20-08-2024_` two halves of one extract, or two
   separate extracts? If separate, can rows appear in both?
3. What is the unit of observation — one row per billed line item, per drug, per bill?
4. What is this dataset, in one paragraph, and how does it relate to IP, OP, TP and LIP
   Billing, and to `VW_DISPENSED_MEDICATION_ITEM_F`?
5. Which population is included, and who is excluded by what mechanism?
6. Is there a data dictionary? All 23 columns are currently undescribed and unclassified.
7. `ROUTE_OF_ADMINISTRATION` is 100% empty in both partitions read — deprecated, or populated
   in a source not delivered here?
8. Why do ~60% of rows carry no `DRUG_CODE` or `DRUG_DESC`? What are those rows?
9. What is the difference between `ITEM_CODE`/`ITEM_DESC` and `DRUG_CODE`/`DRUG_DESC`?
10. What are the units of the six amount columns, and how do FULL, PAYABLE, PAID, TAX,
    SUBSIDY and SURCHARGE relate arithmetically?
11. Is a `0` in an amount column a real zero or an unrecorded value?
12. Does `DRUG_CODE` join to `VW_DRUG_D`?
13. Is `PATIENT_CODE_X` the same identifier space as `FK_PATIENT_ID_X`, `PATIENT_ID_EXTN_X` or
    `NRIC_X`? Does a crosswalk exist?
14. What is `BILL_NO`, and why is it absent for ~57% of rows?
15. What is the delimiter and file encoding?
16. Who is the data owner and steward role, what is the approval route, and what lead time
    should a study plan for?

---

## Appendix A — Full column profile

The per-column profile is the *Key Variables* table above and is not repeated here: with
Description, Class, Coding and Sensitivity still outstanding, the two tables would be
identical. Both carry 23 rows, matching the 23 columns declared for every indexed object.

## Appendix B — Change log

| Date | Change | By |
|---|---|---|
| 2026-07-31 | Page created against `template.md` from the profiler run of 2026-07-23. Seventeen objects, 93,302,155 rows, 23 columns. Column names and types transcribed from the screenshots for one 20-08-2024 partition, first thirteen confirmed against P33; object-level figures for all seventeen. Object list flagged incomplete. Category from the dataset name and `PATIENT_CODE_X` as primary identifier, both by catalogue convention. | CCJX |

## Appendix C — Sources

- **Profiler run 2026-07-23** — the complete P1 and P10 blocks read from
  `source_material/screenshots/mass_columns_screenshots/section_16.png`; P33's first thirteen
  columns from `section_17.png`. Object-level figures for all seventeen indexed objects from
  the same run.
- **`section_17.png` is damaged where this family appears there.** It carries a stitch seam
  from two joined scroll captures: the `ROUTE_OF_ADMINISTRATION` line renders with doubled,
  overlapping strokes, and the separator and header lines of the following object were
  swallowed entirely. That is why P33 stops at column 13. The P1 and P10 blocks in
  `section_16.png` are undamaged and supply the full schema, so no figure on this page depends
  on the damaged region.
- `tools/s3_data_catalog.py` — cited only for the profiler's documented behaviour, never for
  any property of this dataset.
- **Not used for column names:** `source_material/imported/profiler_report_full.txt` and
  `column_summary.csv`, which are OCR reconstructions that corrupt column names. For this
  family the reconstruction is especially unreliable: it recovers 54 distinct names for a
  23-column object, having read across the damaged seam into a neighbouring block.
- **Data owner correspondence — none.** Every governance field on this page is unconfirmed.

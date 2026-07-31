# SingCLOUD — Dimension tables (`VW_*_D`) index

| | |
|---|---|
| **Status** | ⚪ Stub |
| **Profiled on** | 2026-07-23 |
| **Last reviewed** | *not yet reviewed* |

An index rather than a dataset page. It covers the **43 objects whose names end in `_D`** in
the profiler run of 2026-07-23 — 34,964,652 rows and 7,092.26 MB in total — so that none of
them is silently dropped while the fact families get individual pages.

**What this page carries:** object name, size, rows, columns and overall missing % for every
`_D` object. Those figures are object-level and reliable.

**What it does not carry:** column names, for all but the five objects noted below. Column
names have to be read from the screenshots one object at a time, because the OCR
reconstruction corrupts them. That work is outstanding for 38 of the 43.

---

## Read this first

| | Issue | What to do |
|---|---|---|
| 🔴 | **The `_D` suffix covers three different kinds of object** — small code lists, large reference tables, and patient-level data | Do not treat everything named `_D` as harmless reference data |
| 🔴 | **Group C is patient-level, not reference** — 10 objects carrying DOB, race, religion, nationality and occupation at individual level | A different sensitivity question entirely from the code lists they sit beside |
| 🔴 | **Ten Group C objects share ~849,308 rows.** If that is a patient count, it is the only denominator the catalogue has | Confirm with the owner — nothing else profiled supplies one |
| 🟡 | **Group C spans three extract dates** (22-07, 06-08, 11-09-2024) | Joining them into one patient record may mean mixing snapshots |
| 🟡 | **19 candidate joins listed, none tested** | They are there to be checked, not assumed |
| 📋 | Column names read for 5 of 43 objects | 38 outstanding |

---

## The `_D` suffix covers three different kinds of object

Grouped below by **observable shape** — row count and column count — not by any asserted
purpose. What each object actually contains is unknown until someone reads it or asks the
data owner. The grouping is a navigation aid, not a finding.

| Group | Objects | Shape | Rows |
|---|---:|---|---|
| **A — Small, narrow** | 16 | 2–11 columns | 3 – 9,727 |
| **B — Large, narrow** | 6 | 4–19 columns | 25,088 – 5,286,383 |
| **C — Patient-attribute** | 10 | 11–14 columns | ~849,000 – 1,050,317 |
| **D — Wide clinical** | 11 | 7–371 columns | 4,846 – 11,520,086 |

**Group C is the one to look at first, and it may not be a dimension table at all.** Ten
objects share almost exactly the same row count — 849,308 in seven of them, 849,164 and
849,012 in two more, and 1,050,317 in the tenth. A set of objects with one row per something,
all agreeing on the count, named `PATIENT_RACE`, `PATIENT_DOB`, `PATIENT_GENDER` and so on, is
not the shape of a code list. **What that shared count represents is unknown — to confirm with
data owner**, and it is the single most valuable question on this page: if it is a patient
count, it is the closest thing the catalogue has to a denominator, and nothing else profiled
so far supplies one.

These objects also carry date of birth, race, religion, nationality and occupation at
individual level, which is a different sensitivity question from the code lists they are
grouped with by suffix. **Do not treat everything named `_D` as non-sensitive reference data.**

---

## Group A — Small, narrow objects

| Object | Size (MB) | Rows | Cols | Missing % |
|---|---:|---:|---:|---:|
| `VW_MOV_CAT_D_Export_22-07-2024.csv` | 0.00 | 3 | 6 | 0.0 |
| `VW_PATIENT_TYPE_D_Export_22-07-2024.csv` | 0.00 | 4 | 6 | 0.0 |
| `VW_DIAGNOSIS_STATUS_D_Export_22-07-2024.csv` | 0.00 | 9 | 6 | 0.0 |
| `VW_INV_RESULT_STATUS_D_Export_22-07-2024.csv` | 0.00 | 32 | 6 | 0.0 |
| `VW_CASE_TYPE_D_Export_22-07-2024.csv` | 0.00 | 37 | 11 | 49.88 |
| `VW_DIAGNOSIS_TYPE_D_Export_22-07-2024.csv` | 0.00 | 47 | 6 | 0.35 |
| `VW_ITEM_STATUS_D_Export_22-07-2024.csv` | 0.01 | 125 | 6 | 0.13 |
| `VW_ADMIT_TYPE_D_Export_22-07-2024.csv` | 0.01 | 132 | 10 | 35.15 |
| `VW_INV_SUBTYPE_D_Export_22-07-2024.csv` | 0.01 | 160 | 6 | 0.0 |
| `VW_INV_TYPE_D_Export_22-07-2024.csv` | 0.02 | 177 | 6 | 0.09 |
| `VW_MOV_TYPE_D_Export_22-07-2024.csv` | 0.03 | 396 | 6 | 0.0 |
| `VW_DISCHARGE_DISPOSITION_D_Export_22-07-2024.csv` | 0.05 | 527 | 6 | 0.0 |
| `VW_SINGCLOUD_DIAGNOSIS_CODE_D_Export_22-07-2024.csv` | 0.04 | 859 | 2 | 0.0 |
| `VW_REFERRAL_FACILITY_D_Export_22-07-2024.csv` | 0.17 | 2,683 | 5 | 0.71 |
| `VW_DRG_D_Export_22-07-2024.csv` | 0.28 | 4,137 | 4 | 0.01 |
| `VW_INSTITUTION_D_Export_22-07-2024.csv` | 0.66 | 9,727 | 5 | 0.0 |

`VW_MOV_CAT_D` has **three rows**. `VW_PATIENT_TYPE_D` has four. These are the smallest
objects in the entire run.

**`VW_CASE_TYPE_D` (49.88%) and `VW_ADMIT_TYPE_D` (35.15%) are substantially empty**, and both
have more columns (11 and 10) than the six-column objects around them. Worth understanding
before either is used as a lookup.

## Group B — Large, narrow objects

| Object | Size (MB) | Rows | Cols | Missing % |
|---|---:|---:|---:|---:|
| `VW_SERVICE_SPECIALITY_D_Export_22-07-2024.csv` | 2.40 | 25,088 | 6 | 0.01 |
| `VW_ITEM_D_Export_22-07-2024.csv` | 6.71 | 81,721 | 8 | 12.27 |
| `VW_DRUG_D_Export_06-08-2024.csv` | 51.04 | 399,310 | 14 | 54.22 |
| `VW_SERVICE_CODE_D_Export_22-07-2024.csv` | 252.15 | 2,142,754 | 15 | 40.68 |
| `VW_DISPENSED_MEDICATION_CROSS_MAPS_MV2_D_Export_22-07-2024.csv` | 1,188.97 | 4,219,826 | 19 | 0.0 |
| `VW_DIAGNOSIS_CODE_D_Export_22-07-2024.csv` | 528.58 | 5,286,383 | 6 | 0.0 |

**`VW_DRUG_D` is 54.22% empty and `VW_SERVICE_CODE_D` 40.68%** — high for objects of this
shape. Both are candidates for a lookup join, so the emptiness matters.

**`VW_SERVICE_SPECIALITY_D` uses the British spelling** (`SPECIALITY`), matching IP Billing's
`FK_ADMIT_PATIENT_SPECIALITY_ID` but not the clinical families' `SPECIALTY`.

Note two objects with similar names in different places:
`VW_DIAGNOSIS_CODE_D` (5,286,383 rows, 6 columns) and `VW_SINGCLOUD_DIAGNOSIS_CODE_D` (859
rows, 2 columns) are different objects. Their relationship is unknown.

## Group C — Patient-attribute objects

| Object | Size (MB) | Rows | Cols | Missing % |
|---|---:|---:|---:|---:|
| `VW_PATIENT_MARITAL_STATUS_D_Export_11-09-2024.csv` | 153.34 | 849,012 | 11 | 13.51 |
| `VW_PATIENT_DOB_D_Export_22-07-2024.csv` | 163.67 | 849,164 | 12 | 9.01 |
| `VW_PATIENT_GENDER_D_Export_06-08-2024.csv` | 154.39 | 849,308 | 11 | 6.47 |
| `VW_PATIENT_LANGUAGE_D_Export_06-08-2024.csv` | 154.28 | 849,308 | 11 | 11.02 |
| `VW_PATIENT_NATIONALITY_D_Export_06-08-2024.csv` | 161.30 | 849,308 | 11 | 7.54 |
| `VW_PATIENT_OCCUPATION_D_Export_06-08-2024.csv` | 133.70 | 849,308 | 11 | 18.09 |
| `VW_PATIENT_RACE_D_Export_06-08-2024.csv` | 154.20 | 849,308 | 11 | 10.60 |
| `VW_PATIENT_RELIGION_D_Export_06-08-2024.csv` | 152.35 | 849,308 | 11 | 16.07 |
| `VW_PATIENT_RESIDENTIAL_STATUS_D_Export_06-08-2024.csv` | 153.90 | 849,308 | 11 | 12.27 |
| `VW_PATIENT_DEATH_IND_D_Export_06-08-2024.csv` | 216.72 | 1,050,317 | 14 | 22.68 |

**Three extract dates in this group** — `22-07-2024` for DOB, `06-08-2024` for seven objects,
and `11-09-2024` for marital status. The marital-status object is the latest-dated object in
the entire run and has 296 fewer rows than the `06-08-2024` set. If these are meant to be
joined into one patient record, they were not all cut from the same snapshot.

**`VW_PATIENT_DEATH_IND_D` has 1,050,317 rows — 201,009 more than the others** and 14 columns
rather than 11. Whether it covers a wider population, or holds more than one row per person,
is unknown.

## Group D — Wide clinical objects

| Object | Size (MB) | Rows | Cols | Missing % |
|---|---:|---:|---:|---:|
| `VW_SKH_CVIS_MIBI_D_Export_22-07-2024.csv` | 4.60 | 4,846 | 175 | 25.57 |
| `VW_NUH_CABG_09_21_D_Export_22-07-2024.csv` | 7.71 | 5,007 | 186 | 13.72 |
| `VW_CVIS_NUCLEAR_D_Export_22-07-2024.csv` | 33.89 | 54,449 | 169 | 18.39 |
| `VW_NUHCS_NUC_D_Export_22-07-2024.csv` | 161.13 | 63,656 | 191 | 14.87 |
| `VW_NUHCS_PCI_D_Export_22-07-2024.csv` | 823.10 | 230,968 | 286 | 39.34 |
| `VW_NUHCS_ECHO_D_Export_22-07-2024.csv` | 541.64 | 270,906 | 371 | 3.36 |
| `VW_NUHCS_PROC_D_Export_22-07-2024.csv` | 76.28 | 408,586 | 15 | 13.33 |
| `VW_CIIMS_RHYTHM_D_Export_22-07-2024.csv` | 21.80 | 148,278 | 8 | 5.35 |
| `VW_CIIMS_WALLMOTION_D_Export_22-07-2024.csv` | 53.39 | 259,487 | 26 | 4.09 |
| `VW_CIIMS_ECHO_FINDINGS_D_Export_22-07-2024.csv` | 208.76 | 1,130,597 | 10 | 16.56 |
| `VW_CIIMS_ECHO_MEASUREMENTS_D_Export_22-07-2024.csv` | 1,530.98 | 11,520,086 | 7 | 0.0 |

**These are not code lists.** `VW_NUHCS_ECHO_D` has 371 columns, `VW_NUHCS_PCI_D` 286.
`VW_CIIMS_ECHO_MEASUREMENTS_D` has 11.5 million rows — more than any single object outside the
billing families. Objects of this shape hold records, not reference values, and several
probably warrant their own catalogue page rather than an index row. Naming stems (`NUHCS_`,
`CIIMS_`, `CVIS_`, `SKH_`, `NUH_`) suggest institutional or system groupings, but nothing
establishes that and no reading is adopted here.

`VW_CGH_NUCLEAR_F` and `VW_CVIS_NUCLEAR_D` share the `NUCLEAR` stem across the `_F` / `_D`
divide; see [singcloud-cgh-nuclear.md](singcloud-cgh-nuclear.md). No relationship has been
established.

---

## Column names read so far

Five objects have had their columns transcribed from the screenshots. The rest have not.

**`VW_DRG_D`** — 4 columns: `DATA_SOURCE`, `PK_DRG_ID` (numeric), `DRG_CODE`, `DRG_DESC`.

**`VW_DISCHARGE_DISPOSITION_D`** — 6 columns: `DATA_SOURCE`,
`DISCHARGE_DISPOSITION_ETS_ID`, `DISCHARGE_DISPOSITION_CODE`, `DISCHARGE_DISPOSITION_DESC`,
`DISCHARGE_DISPOSITION_CSN_ID`, `DISCHARGE_DISPOSITION_CSN`. All 0.0% missing.

**`VW_DIAGNOSIS_TYPE_D`** — 6 columns in the same shape: `DATA_SOURCE`,
`DIAGNOSIS_TYPE_ETS_ID`, `DIAGNOSIS_TYPE_CODE`, `DIAGNOSIS_TYPE_DESC`,
`DIAGNOSIS_TYPE_CSN_ID`, `DIAGNOSIS_TYPE_CSN`.

Both six-column objects follow the pattern `DATA_SOURCE` + `<NAME>_ETS_ID` + `<NAME>_CODE` +
`<NAME>_DESC` + `<NAME>_CSN_ID` + `<NAME>_CSN`. **Whether the other nine six-column objects in
Group A share that shape is not established** — it is a reasonable guess and exactly the kind
of guess this catalogue does not publish. Read them before relying on it.

**`VW_DRUG_D`** — 14 columns, first nine read: `DATA_SOURCE`, `DRUG_NAME_ETS_ID` (numeric),
`DRUG_NAME`, `DRUG_CODE`, `DRUG_CSN_ID` (id_like, 16.17%), `DRUG_CSN` (16.17%), `DRUG_FORM`
(83.83%), `DRUG_STRENGTH` (92.8%), `EFFECTIVE_FROM_DATE_X` (date). The remaining five are not
yet read.

**`VW_DISPENSED_MEDICATION_CROSS_MAPS_MV2_D`** — 19 columns, all 0.0% missing:
`DATA_SOURCE`, `CONCEPT_ID`, `CONCEPT_CODE`, `STATUS_CODE`, `TERM_TXT`, `CODINGSCHEME_NAME`,
`CODINGSCHEME_OID`, `VERSION_NAME`, `VERSION_ID`, `VERSION_DEFAULT_FLAG`,
`EQUIVALENT_CODINGSCHEME_NAME`, `EQUIVALENT_CODINGSCHEME_OID`, `EQUIVALENT_VERSION_ID`,
`EQUIVALENT_VERSION_NAME`, `EQUIV_VERSION_DEFAULT_FLAG`, `EQUIVALENT_CONCEPT_ID`,
`EQUIVALENT_CONCEPT_CODE`, `EQUIVALENT_STATUS_CODE`, `EQUIVALENT_TERM_TXT`.

Note `EQUIV_VERSION_DEFAULT_FLAG` is abbreviated where its neighbours spell out `EQUIVALENT_`.
Copy it character for character.

---

## Candidate joins from the fact families — none tested

Several `FK_` columns on the billing pages carry names matching objects above. **No join has
been tested and none of these is established** — they are listed so someone can check them,
not as documented relationships.

| Fact column | Page | Candidate object |
|---|---|---|
| `FK_DRG_ID` | [IP Billing](singcloud-ip-billing.md), [OP Billing](singcloud-op-billing.md) | `VW_DRG_D` |
| `FK_SERVICE_CODE_ID` | IP Billing, OP Billing | `VW_SERVICE_CODE_D` |
| `FK_DISCHARGE_CASE_TYPE_ID` | IP Billing, OP Billing | `VW_CASE_TYPE_D` |
| `FK_REFERRAL_HCAR_FACILITY_ID` | OP Billing | `VW_REFERRAL_FACILITY_D` |
| `FK_ADMIT_TYPE_ID` | IP Billing | `VW_ADMIT_TYPE_D` |
| `FK_INST_ID` | IP Billing, OP Billing | `VW_INSTITUTION_D` |
| `FK_ADMIT_PATIENT_SPECIALITY_ID` | IP Billing | `VW_SERVICE_SPECIALITY_D` |
| `MOV_TYPE_ETS_ID` | [Event Diagnosis](singcloud-event-diagnosis.md) | `VW_MOV_TYPE_D` |
| `MOV_CAT_ETS_ID` | Event Diagnosis | `VW_MOV_CAT_D` |
| `DIAGNOSIS_TYPE_ETS_ID` | Event Diagnosis | `VW_DIAGNOSIS_TYPE_D` |
| `DIAG_STATUS_ETS_ID` | Event Diagnosis | `VW_DIAGNOSIS_STATUS_D` |
| `PATIENT_TYPE_ETS_ID` | Event Diagnosis | `VW_PATIENT_TYPE_D` |
| `DISCHARGE_DISPOSITION_ETS_ID` | Event Diagnosis | `VW_DISCHARGE_DISPOSITION_D` |
| `INV_RESULT_STATUS_ETS_ID` | [Laboratory](singcloud-laboratory.md) | `VW_INV_RESULT_STATUS_D` |
| `INV_TYPE_NAME_ETS_ID` | Laboratory | `VW_INV_TYPE_D` |
| `INV_SUBTYPE_NAME_ETS_ID` | Laboratory | `VW_INV_SUBTYPE_D` |
| `ITEM_STATUS_ETS_ID` | [Dispensed Medication Item](singcloud-dispensed-medication-item.md) | `VW_ITEM_STATUS_D` |
| `ITEM_NAME_ETS_ID` | Dispensed Medication Item | `VW_ITEM_D` |
| `DRUG_CODE` | [MED Billing](singcloud-med-billing.md) | `VW_DRUG_D` |

The `_ETS_ID` naming on the fact side and the `_ETS_ID` column inside `VW_DISCHARGE_DISPOSITION_D`
and `VW_DIAGNOSIS_TYPE_D` is the reason these are worth testing first.

---

## Open questions for the data owner

1. **What does the ~849,308 row count in Group C represent?** If it is a patient count, it is
   the catalogue's only denominator and should be recorded on every page.
2. Why does `VW_PATIENT_DEATH_IND_D` have 201,009 more rows than the rest of Group C?
3. Group C spans three extract dates (22-07, 06-08, 11-09-2024). Can these objects be joined
   into a single patient record, or are they inconsistent snapshots?
4. Are the Group C objects patient-level data rather than reference tables? If so, what are
   their access and sensitivity conditions, given they carry DOB, race, religion, nationality
   and occupation?
5. Which of the candidate joins above are real, and on which key?
6. Do the six-column Group A objects all share the
   `ETS_ID` / `CODE` / `DESC` / `CSN_ID` / `CSN` shape? What do `ETS` and `CSN` stand for?
7. Why are `VW_CASE_TYPE_D` (49.88%) and `VW_ADMIT_TYPE_D` (35.15%) so empty for lookup
   tables?
8. Why is `VW_DRUG_D` 54.22% empty and `VW_SERVICE_CODE_D` 40.68%?
9. What is the relationship between `VW_DIAGNOSIS_CODE_D` and `VW_SINGCLOUD_DIAGNOSIS_CODE_D`?
10. Should the Group D objects (`NUHCS_*`, `CIIMS_*`, `CVIS_*`, `SKH_*`, `NUH_CABG_*`) be
    treated as datasets in their own right rather than dimensions? Several are larger and
    wider than families that have their own pages.
11. What do the stems `NUHCS`, `CIIMS`, `CVIS`, `SKH` and `NUH` refer to?
12. Is the `_D` suffix meant to denote a dimension table, and if so why does it cover
    patient-level and clinical-record objects?

---

## Change log

| Date | Change | By |
|---|---|---|
| 2026-07-31 | Index created from the profiler run of 2026-07-23. All 43 `_D` objects listed with object-level figures. Column names transcribed from the screenshots for five objects; outstanding for 38. | CCJX |

## Sources

- **Profiler run 2026-07-23** — object-level figures for all 43 objects. Column names for
  `VW_DRG_D`, `VW_DISCHARGE_DISPOSITION_D`, `VW_DIAGNOSIS_TYPE_D`, `VW_DRUG_D` (partial) and
  `VW_DISPENSED_MEDICATION_CROSS_MAPS_MV2_D` read from
  `source_material/screenshots/mass_columns_screenshots/section_12.png`.
- `tools/s3_data_catalog.py` — cited only for the profiler's documented behaviour.
- **Not used for column names:** `source_material/imported/profiler_report_full.txt` and
  `column_summary.csv`, which are OCR reconstructions that corrupt column names. Its filename
  for `VW_PATIENT_OCCUPATION_D` reads `_Export:_06-08-2024`, with a spurious colon.
- **Data owner correspondence — none.** Every question above is unconfirmed.

# SingCLOUD — SCDB

| | |
|---|---|
| **Status** | ⚪ Stub |
| **Profiled on** | 2026-07-23 |
| **Last reviewed** | *not yet reviewed* |

**Objects included in this page**

Nineteen objects sharing the `VW_SCDB_` stem, all dated `22-07-2024`. Together they hold
2,967,005 rows, 1,304.80 MB and 3,324 columns — smaller in total than a single Laboratory
partition, which is why they are documented as one page rather than nineteen.

| # | Object | Prefix |
|---:|---|---|
| 1 | `VW_SCDB_EPS_F_Export_22-07-2024.csv` | `NonFreeText_Files/` |
| 2 | `VW_SCDB_EPS_DIM_F_Export_22-07-2024.csv` | `NonFreeText_Files/` |
| 3 | `VW_SCDB_HF_F_Export_22-07-2024.csv` | **`PriorityTables-B1/`** |
| 4 | `VW_SCDB_HF_F_Export_22-07-2024.csv` | **`FreeText_FTA/`** |
| 5 | `VW_SCDB_HF_DIM_F_Export_22-07-2024.csv` | `NonFreeText_Files/` |
| 6 | `VW_SCDB_ICD_F_Export_22-07-2024.csv` | `FreeText_FTA/` |
| 7 | `VW_SCDB_ICD_DIM_F_Export_22-07-2024.csv` | `NonFreeText_Files/` |
| 8 | `VW_SCDB_INTERVENTION_F_Export_22-07-2024.csv` | `FreeText_FTA/` |
| 9 | `VW_SCDB_INTERVENTION_DIM_F_Export_22-07-2024.csv` | `FreeText_FTA/` |
| 10 | `VW_SCDB_INTERVENTION_BEFORE_T1_F_Export_22-07-2024.csv` | `FreeText_FTA/` |
| 11 | `VW_SCDB_INTERVENTION_BEFORE_T2_F_Export_22-07-2024.csv` | `NonFreeText_Files/` |
| 12 | `VW_SCDB_PPM_F_Export_22-07-2024.csv` | `FreeText_FTA/` |
| 13 | `VW_SCDB_PPM_DIM_F_Export_22-07-2024.csv` | `FreeText_FTA/` |
| 14 | `VW_SCDB_SURGERY_F_Export_22-07-2024.csv` | `FreeText_FTA/` |
| 15 | `VW_SCDB_SURGERY_DIM_F_Export_22-07-2024.csv` | `NonFreeText_Files/` |
| 16 | `VW_SCDB_SURGERY_BEFORE_F_Export_22-07-2024.csv` | `NonFreeText_Files/` |
| 17 | `VW_SCDB_ZLMAUDITEPS_F_Export_22-07-2024.csv` | `NonFreeText_Files/` |
| 18 | `VW_SCDB_ZLMAUDITEPS_DIM_F_Export_22-07-2024.csv` | `NonFreeText_Files/` |
| 19 | `VW_SCDB_ZLMAUDITICD_F_Export_22-07-2024.csv` | `NonFreeText_Files/` |

All prefixes are relative to `common-data/SingCLoud/`.

> ⚠ **`VW_SCDB_HF_F` appears twice, in two different prefixes** — under `PriorityTables-B1/`
> at 57.11 MB and under `FreeText_FTA/` at 41.07 MB. Both report the same 48,629 rows, the
> same 174 columns and the same 24.44% overall missing, but differ in size by 16 MB. Whether
> these are one object copied to two locations, or two different cuts that agree on shape, is
> unknown — to confirm with data owner. **It is the only duplicate in the catalogue**, and
> anyone loading "the HF table" needs to know which one they have.
>
> `PriorityTables-B1/` is a prefix used by no other object in the run.

---

## Read this first

| | Issue | What to do |
|---|---|---|
| 🔴 | **`VW_SCDB_ICD_F` is about implantable cardioverter-defibrillators, not ICD-10 codes** — its columns are `PulseGenerator_Manuf`, `LV_LeadSerialNo`, `DFTTesting` | Reaching for it expecting diagnosis codes gets device records. The ICD-10 candidate is `VW_DIAGNOSIS_CODE_D` |
| 🔴 | **`VW_SCDB_HF_F` exists twice**, under `PriorityTables-B1/` and `FreeText_FTA/` — same rows and columns, 16 MB apart in size | Know which copy you have. Ask which is authoritative |
| 🔴 | **`VW_SCDB_PPM_DIM_F` names 40 of its 45 columns `Field1`…`FieldN`** | No amount of profiling recovers what they hold. A data dictionary is the only route |
| 🟡 | **An `S_` prefix pattern runs through the set**, and `S_` variants are consistently far emptier (2.79% vs 99.46%, for one) | Substituting one for the other silently changes row counts |
| 🟡 | **`INTERVENTION_BEFORE_T2_F` is 97.29% empty** across 779 columns — the emptiest object in the run | `BEFORE`, `T1` and `T2` are all undefined |
| 🟡 | **Device serial numbers** identify hardware and thereby a person, in cohorts of 1,716–1.6 M rows | Re-identification risk is higher than in the large families |
| 📋 | **~100 of 3,324 columns transcribed** | The largest documentation gap in the catalogue |

---

## Dataset Overview

**Category:** SCDB — taken from the dataset name. Not yet confirmed against a data dictionary
or the data owner. **What `SCDB` stands for is unknown.**

**Description:** Unknown — to be filled in. What *can* be said from the column names read so
far is narrower and is stated exactly: the columns transcribed below are cardiac-procedure
fields — pacing leads, pulse generators, PCI complications, CABG, LVEF. See
*What the sub-groups appear to cover* below for the evidence, and note that no expansion of
the acronym is adopted here.

**Data source:** Unknown — to confirm with data owner.

**Population:** Unknown — to confirm with data owner. Every object here is small by the
standards of this catalogue — the largest is 1.6 million rows against Laboratory's 49.6
million — which suggests a registry or a specialist cohort rather than a system-wide extract.
That is a guess and is not adopted.

**Institutional / geographic coverage:** Unknown — to confirm with data owner.
`HospitalName` appears in `VW_SCDB_PPM_DIM_F` and is 0.0% missing, so the answer is in the
data, but it has not been enumerated here.

**Unit of observation:** **Unknown for every one of the nineteen objects.**

**Rows vs people:** 2,967,005 rows across all nineteen objects (profiler, 2026-07-23);
distinct patients **not counted**. Note that summing across these objects is almost certainly
meaningless — they are not partitions of one table but nineteen different tables.

**What is *not* in it:** Unknown — to be filled in.

### Access

| | |
|---|---|
| **Catalogue alias(es)** | Unknown — to be filled in |
| **Source object(s)** | See the object table above — three different prefixes |
| **Partitions** | None. All nineteen objects are unpartitioned; there is no `_P{n}` anywhere in this set |
| **Format** | CSV by file extension. Delimiter and encoding unknown |
| **Extract date** | Unknown. Every object name contains `_Export_22-07-2024` |
| **Refresh cadence** | Unknown — to confirm with data owner |
| **Free-text content** | Unknown. Eight objects sit under `FreeText_FTA/`, ten under `NonFreeText_Files/` and one under `PriorityTables-B1/` — and the split does not follow the `_F` / `_DIM_F` pairing |

---

## Structure

### The `_F` / `_DIM_F` pairing

Seven stems appear in both a plain `_F` and a `_DIM_F` form. **In every pair the `_DIM_F`
object has more rows and fewer columns than its partner:**

| Stem | `_F` rows × cols | `_DIM_F` rows × cols |
|---|---|---|
| `EPS` | 6,220 × 96 | 51,379 × 41 |
| `HF` | 48,629 × 174 | 655,784 × 13 |
| `ICD` | 4,043 × 128 | 24,450 × 41 |
| `INTERVENTION` | 107,689 × 156 | 1,634,566 × 35 |
| `PPM` | 6,434 × 111 | 35,994 × 45 |
| `SURGERY` | 8,026 × 309 | 189,067 × 23 |
| `ZLMAUDITEPS` | 2,942 × 23 | 10,810 × 18 |

That is the shape of a wide record table alongside a long-format counterpart — but **nothing
establishes it**, and the ratios are not consistent (HF is 13× more rows, ZLMAUDITEPS only
3.7×). Do not assume one can be reconstructed from the other.

`VW_SCDB_ZLMAUDITICD_F` has no `_DIM_F` partner. `VW_SCDB_SURGERY_BEFORE_F` and the two
`INTERVENTION_BEFORE_*` objects sit outside the pairing entirely.

### The `BEFORE` objects are nearly empty

| Object | Rows | Cols | Missing % |
|---|---:|---:|---:|
| `VW_SCDB_INTERVENTION_BEFORE_T2_F` | 62,348 | **779** | **97.29** |
| `VW_SCDB_INTERVENTION_BEFORE_T1_F` | 62,342 | **697** | 82.37 |
| `VW_SCDB_SURGERY_BEFORE_F` | 5,937 | 367 | 62.36 |

`INTERVENTION_BEFORE_T2_F` is **the emptiest object in the entire profiler run** — 97.29% of
its cells are null across 779 columns. Its T1 sibling has six fewer rows (62,342 against
62,348) and 82 fewer columns. What `BEFORE` denotes, and what distinguishes T1 from T2, is
unknown — to confirm with data owner.

### What the sub-groups appear to cover

Stated as an observation about column names, not as a finding about the data.

**`VW_SCDB_ICD_F` is not about ICD diagnosis codes.** Its columns are implantable cardiac
device fields — `PulseGenerator_Manuf`, `PulseGenerator_Model`, `PulseGenerator_Serial`,
`LV_LeadModelNo`, `LV_LeadSerialNo`, `RV_DevicePacingThreshold`, `DFTTesting`,
`Lead_Explanted`, `ExplantGenerator_Reason`. **Anyone reaching for this object expecting
ICD-10 codes will get device records.** The ICD-10 candidate elsewhere in the catalogue is
`VW_DIAGNOSIS_CODE_D` — see
[the dimension index](singcloud-dimension-tables-index.md). Confirm with the data owner before
relying on either reading.

`VW_SCDB_PPM_F` carries the same device vocabulary. `VW_SCDB_INTERVENTION_F` carries
percutaneous-intervention fields — `PROCEDURALSUCCESS`, `NOOFLESIONSUCCESSFUL`,
`MYOCARDIALINFARCTION`, `CABGINDICATION`, `LASTLVEF`, `RETROPERITONEALBLEEDING`.

---

## Key Variables

**Column names are outstanding for most of this set.** Across nineteen objects there are 3,324
columns, and they have to be read from the screenshots one block at a time because the OCR
reconstruction corrupts names. Fragments transcribed so far are below; everything else is
not yet read.

**Type** is the profiler's label and is provisional throughout.

**Outstanding for every column in every object:** Description, Class, Coding / units,
Sensitivity.

### `VW_SCDB_PPM_DIM_F` — first 9 of 45 columns

| # | Variable | Type | Missing % | Description | Class | Coding / units | Sensitivity |
|---:|---|---|---:|---|---|---|---|
| 1 | `ID` | numeric | 0.0 | | | | |
| 2 | `NRIC_X` | id_like | 0.0 | | | | |
| 3 | `ImplantDate_X` | date | 0.0 | | | | |
| 4 | `ImplantDate_Z` | date | 0.0 | | | | |
| 5 | `HospitalName` | categorical | 0.0 | | | | |
| 6 | `Field1` | categorical | 17.54 | | | | |
| 7 | `Field2` | categorical | 99.07 | | | | |
| 8 | `Field3` | categorical | 66.60 | | | | |
| 9 | `Field4` | categorical | 65.91 | | | | |

**From column 6 onward the names are generic placeholders — `Field1`, `Field2`, `Field3`,
`Field4`.** Whatever those 40 columns hold, the object does not say. This is the strongest
argument in the catalogue for obtaining a data dictionary: no amount of profiling will
recover what `Field2` means, and it is 99.07% empty besides.

### `VW_SCDB_ICD_F` — 45-column fragment from the tail

Device and lead fields, transcribed in report order:
`LV_S_LeadInsertion` (99.28), `LV_LeadManufacturer` (74.18), `LV_S_LeadManufacturer` (99.11),
`LV_LeadLocation_RAO` (84.05), `LV_LeadLocation_LAO` (84.0), `LV_LeadModelNo` (73.61),
`LV_LeadSerialNo` (73.61), `LV_Amplitude` (80.46), `LV_SlewRate` (89.51),
`LV_PacingThreshold` (75.09), `LV_Resistance` (75.83), `RV_DeviceSlewRate` (99.58),
`RV_DevicePacingThreshold` (50.38), `RV_DevicePacingImp` (51.13), `LV_DeviceSlewRate` (99.95),
`LV_DevicePacingThreshold` (85.6), `LV_DevicePacingImp` (85.93), `RA_DeviceSlewRate` (99.85),
`RA_DevicePacingThreshold` (82.32), `RA_DevicePacingImp` (82.34),
`PulseGenerator_Manuf` (2.79), `S_PulseGenerator_Manuf` (99.46),
`PulseGenerator_Model` (1.98), `PulseGenerator_Serial` (2.1), `PulseGenerator_Site` (3.07),
`S_PulseGenerator_Site` (96.34), `DFTTesting` (5.61), `S_DETTesting` (82.22),
`ProcedureTime` (0.69), `FluoroscopyTime` (1.88), `S_Complications` (99.21),
`FirstImplantDate_X` (75.83), `FirstImplantDate_Z` (75.83),
`PreGeneratorChangeDate_X` (94.83), `PreGeneratorChangeDate_Z` (94.83),
`ExplantGenerator_Manuf` (76.48), `S_ExplantGenerator_Manuf` (98.17),
`ExplantGenerator_ModelNo` (76.13), `ExplantGenerator_SerialNo` (76.26),
`ExplantGenerator_Site` (76.21), `ExplantGenerator_Reason` (76.33),
`S_ExplantGenerator_Reason` (94.68), `Lead_Explanted` (79.1),
`LeadImplantedDate_X` (80.86), `LeadImplantedDate_Z` (80.86).

Note `S_DETTesting` sits beside `DFTTesting` — `DET` against `DFT`. One of the two is probably
a typo, in the source or in the capture; it has not been resolved.

### `VW_SCDB_INTERVENTION_F` — 45-column fragment from the tail

`NOOFLESIONSUCCESSFUL` (35.27), `PROCEDURALSUCCESS` (45.54), `NOINTRAPOSTPROCEDURE` (0.07),
`MYOCARDIALINFARCTION` (0.01), `POSTCARDIOGENICSHOCK` (0.0), `HEARTFAILURE` (0.0),
`CVA_STROKE` (0.0), `HEMORRHAGICSTROKE` (99.65), `TAMPONADE` (0.12),
`DIALYSISNEWREQUIREMENT` (0.02), `OTHERCOMPLICATIONS` (0.0), `RBCTRANSFUSION` (0.0),
`HOMOGLOBINPRIORTRANSFUSION` (99.41), `BLEEDINGIN72HRS` (0.12), `BLEEDINGACCESSSITE` (99.22),
`BLEEDINGSIZE` (99.57), `RETROPERITONEALBLEEDING` (99.43), `GIBLEED` (99.41),
`GUBLEED` (99.43), `OTHERBLEED` (99.42), `VT_DCSHOCK` (0.14), `HEARTBLOCK_PACING` (0.03),
`CABG` (0.0), `CABGINDICATION` (88.06), `S_CABGINDICATION` (89.92), `CABGLOCATION` (88.71),
`CABGDTM_X` (98.71), `CABGDTM_Z` (98.71), `OTHERMAJORSURGERY` (0.14), `LASTLVEF` (40.92),
`LVEFASSESSED` (7.08), `DISCHARGEDATE_X` (4.26), `DISCHARGEDATE_Z` (4.26),
`DISCHARGESTATUS` (4.31), `DEATHINLAB` (94.18), `DEATHPRIMARYCAUSE` (88.48),
`INTRAVASCULARLITHOTRIPSY` (0.14), `S_FINALDIAGNOSIS` (98.83), `S_OTHERS` (90.77),
`S_REASONFORDELAY` (99.49), `CATHNO` (0.03), `CASENO` (id_like, 75.96),
`S_PCI_INDICATION` (98.09).

`HOMOGLOBINPRIORTRANSFUSION` is spelled with an O where *haemoglobin* would have an AE — copy
it as written.

### The `S_` prefix pattern

Several columns appear in both a plain and an `S_`-prefixed form, and **in every observed case
the `S_` variant is far emptier**:

| Plain | Missing % | `S_` variant | Missing % |
|---|---:|---|---:|
| `PulseGenerator_Manuf` | 2.79 | `S_PulseGenerator_Manuf` | 99.46 |
| `PulseGenerator_Site` | 3.07 | `S_PulseGenerator_Site` | 96.34 |
| `ExplantGenerator_Manuf` | 76.48 | `S_ExplantGenerator_Manuf` | 98.17 |
| `ExplantGenerator_Reason` | 76.33 | `S_ExplantGenerator_Reason` | 94.68 |
| `CABGINDICATION` | 88.06 | `S_CABGINDICATION` | 89.92 |

What `S_` denotes is unknown — to confirm with data owner. The pattern is consistent enough to
be deliberate, and it matters: substituting one for the other would silently change how many
rows a query returns.

> **Value strings drift between extracts** (`SINGAPORE PINK IC` vs `SINGAPORE PINK NRIC`).
> This page lists no values for any column. Enumerate the distinct values in your own extract
> before filtering, and re-check them against each new extract — a value string that has
> drifted returns zero rows without raising an error.

---

## Time Coverage

**Unknown for every object.** No date range is established anywhere in this set.

Date columns observed so far: `ImplantDate_X` / `_Z` (`PPM_DIM_F`), `FirstImplantDate_X` /
`_Z`, `PreGeneratorChangeDate_X` / `_Z`, `LeadImplantedDate_X` / `_Z` (`ICD_F`),
`CABGDTM_X` / `_Z`, `DISCHARGEDATE_X` / `_Z` (`INTERVENTION_F`). The `_X` / `_Z` pairing runs
through the whole catalogue; no relationship between a pair has been established anywhere.

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
| `VW_SCDB_ZLMAUDITEPS_F` | 0.92 | 2,942 | 23 | 4.36 |
| `VW_SCDB_ZLMAUDITICD_F` | 1.10 | 1,716 | 94 | 46.80 |
| `VW_SCDB_ICD_F` | 2.84 | 4,043 | 128 | 47.50 |
| `VW_SCDB_ZLMAUDITEPS_DIM_F` | 3.03 | 10,810 | 18 | 50.73 |
| `VW_SCDB_EPS_F` | 4.02 | 6,220 | 96 | 34.43 |
| `VW_SCDB_PPM_F` | 4.26 | 6,434 | 111 | 42.69 |
| `VW_SCDB_SURGERY_F` | 9.61 | 8,026 | 309 | 40.54 |
| `VW_SCDB_SURGERY_BEFORE_F` | 9.70 | 5,937 | 367 | 62.36 |
| `VW_SCDB_ICD_DIM_F` | 12.84 | 24,450 | 41 | 69.50 |
| `VW_SCDB_PPM_DIM_F` | 17.92 | 35,994 | 45 | 71.29 |
| `VW_SCDB_EPS_DIM_F` | 23.81 | 51,379 | 41 | 72.43 |
| `VW_SCDB_HF_F` *(FreeText_FTA)* | 41.07 | 48,629 | 174 | 24.44 |
| `VW_SCDB_SURGERY_DIM_F` | 54.65 | 189,067 | 23 | 42.18 |
| `VW_SCDB_HF_F` *(PriorityTables-B1)* | 57.11 | 48,629 | 174 | 24.44 |
| `VW_SCDB_INTERVENTION_F` | 59.74 | 107,689 | 156 | 36.90 |
| `VW_SCDB_INTERVENTION_BEFORE_T1_F` | 84.22 | 62,342 | 697 | 82.37 |
| `VW_SCDB_HF_DIM_F` | 152.29 | 655,784 | 13 | 12.05 |
| `VW_SCDB_INTERVENTION_BEFORE_T2_F` | 210.54 | 62,348 | 779 | 97.29 |
| `VW_SCDB_INTERVENTION_DIM_F` | 555.13 | 1,634,566 | 35 | 62.00 |
| **Total across all objects** | **1,304.80** | **2,967,005** | **3,324** | — |

*Every row count above is a lower bound: the profiler reads with `on_bad_lines="skip"`
([tools/s3_data_catalog.py](../tools/s3_data_catalog.py)), so unparseable lines are dropped
silently and never counted. On objects of 1,716 and 2,942 rows a handful of skipped lines is a
materially larger share than on the million-row families.*

**The total is presented for scale only.** These are nineteen different tables, not partitions
of one, so the row and column sums are not meaningful quantities — do not cite them as a
dataset size.

| Metric | Value |
|---|---|
| Sample size (distinct patients) | **not counted** — the profiler does not compute it |
| Schema consistent across partitions | n/a — no object here is partitioned |

---

## Provenance & Processing

Every field here is owner-only, and none is inferred from column naming.

**Collection mechanism:** Unknown — to confirm with data owner.

**Who enters it, and under what incentive:** Unknown — to confirm with data owner. Three
objects carry `ZLMAUDIT` in their names, which suggests audit records of some kind, but that
is not established.

**Extract pipeline:** Unknown — to confirm with data owner. Every object name begins `VW_`;
what that prefix denotes is not documented in any source available here. The scattering of one
logical set across three prefixes — including `PriorityTables-B1/`, used by nothing else in
the run — is itself a pipeline question.

**Processing applied:** Unknown — to confirm with data owner.

**Standardisation mappings:** Unknown. No column read so far carries a `_STD` suffix, but the
`S_` prefix pattern described above is unexplained and may indicate a second encoding of the
same field.

**Transformations at load:** Unknown. Inspect `df.columns` after loading — this set mixes
upper-case (`PROCEDURALSUCCESS`), mixed-case (`PulseGenerator_Manuf`, `ImplantDate_X`) and
generic (`Field1`) naming, so a loader that normalises case will change most of it.

**Raw vs interpreted — what is lost:** Unknown. Needs the Class determination this page cannot
yet make. Fields such as `PROCEDURALSUCCESS` and `DEATHPRIMARYCAUSE` are judgements rather
than measurements, so the Raw / Derived distinction will matter here.

**Identifier handling:** Unknown — to confirm with data owner. `VW_SCDB_PPM_DIM_F` uses
`NRIC_X`, as the MOH OB families do. **Whether it is pseudonymised must be answered before the
data is handled.**

---

## Data Quality

### Missingness

| Metric | Value |
|---|---|
| Overall missing | **4.36% to 97.29%** across the nineteen objects (profiler, 2026-07-23) |
| Emptiest | `VW_SCDB_INTERVENTION_BEFORE_T2_F` at 97.29% — the emptiest object in the run |
| Fullest | `VW_SCDB_ZLMAUDITEPS_F` at 4.36% |

The spread is far wider than in any partitioned family, because these are unrelated tables
rather than slices of one.

**Columns that matter:** Unknown — ranking columns by consequence needs their descriptions.

| Variable | Missing % | Consequence if unusable |
|---|---:|---|
| | | |
**Disguised missing:** **Not checked anywhere in this set.**

- Profiler counts only `""`, `NA`, `N/A`, `NULL`, `null`, `None`, `NaN`, `.` as missing.
- `UNKNOWN`, `NIL`, `9`, `999`, `1900-01-01` all read as *present* — invisible in these figures.
- This set is full of clinical yes/no fields — `HEARTFAILURE`, `CVA_STROKE`, `RBCTRANSFUSION`, `CABG` — several reported 0.0% missing. On a complication flag, a recorded "no" and an unrecorded value are entirely different facts, and the profiler cannot tell them apart. **Do not read "0.0% missing" as "0.0% unusable"** until someone has run `value_counts()`.
- Run `value_counts()` before trusting any 0.0% figure.

### Overlap

**Primary identifier:** `NRIC_X`, confirmed in `VW_SCDB_PPM_DIM_F`. The patient ID column is
the primary identifier for every dataset in this catalogue. **The identifier column has not
been read for the other eighteen objects** and is not assumed to be `NRIC_X` throughout.
Dtype as read, leading zeros, casing and padding are unknown — read it as `str` and inspect
before joining. Singapore NRIC values carry a trailing check letter and leading zeros, both of
which a numeric read would destroy.

**Identifier family:** Unknown — to confirm with data owner. `NRIC_X` matches
[MOH OB Operation](singcloud-moh-ob-operation.md) and
[MOH OB Procedure](singcloud-moh-ob-procedure.md) but differs from every other family;
**no join has been tested**.

**Secondary keys:** Unknown. `CASENO` in `VW_SCDB_INTERVENTION_F` profiles as `id_like` and is
75.96% empty. `ID` and `CATHNO` are other candidates but profile as `numeric` and
`categorical`.

**Coding standards:** Unknown — to confirm with data owner.

| Links to | On | Granularity | Cardinality | Overlap tested? | Notes |
|---|---|---|---|---|---|
| Between the `_F` / `_DIM_F` pairs | Unknown | Unknown | Unknown | **no join tested** | The row/column shapes suggest a wide-to-long relationship. Nothing establishes it |
| MOH OB families | `NRIC_X` | Unknown | Unknown | **no join tested** | Shared column name only |

**Known linkage pitfalls:** None recorded — no linkage has been attempted. An empty list, not
a clean bill of health.

### Bias

- **Coverage / selection:** Unknown — to confirm with data owner. Given how small these
  objects are relative to the rest of the catalogue, who gets into them is the first question.
- **Recording practice:** Unknown — to confirm with data owner.
- **Changes over time:** Unknown — to confirm with data owner.
- **Ascertainment:** Unknown — to confirm with data owner.

### Other limitations

- **Duplicates:** **One confirmed at object level** — `VW_SCDB_HF_F` exists in two prefixes.
  Row-level duplication has not been checked in any object.
- **Schema drift across partitions:** n/a — nothing here is partitioned.
- **Value-range anomalies:** Not checked.
- **Encoding:** Unknown. The profiler attempts UTF-8 and falls back to latin-1 with
  `errors="replace"` silently.
- **Column names outstanding:** 3,324 columns across nineteen objects, of which roughly 100
  have been read. This is the largest documentation gap in the catalogue.
- **Fitness for purpose:** **Cannot be assessed yet** for any object in this set.

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
| **Free-text / PII exposure** | **Not assessed, and two signals stand out.** The identifier column read so far is `NRIC_X`, profiling as `id_like` — if it holds NRIC values rather than a pseudonym, this is direct identifier data. And the device columns (`PulseGenerator_Serial`, `LV_LeadSerialNo`, `ExplantGenerator_SerialNo`) hold serial numbers of implanted hardware, which identify a device and thereby a person in a small cohort. These objects are small — 1,716 to 1.6 million rows — so re-identification risk is structurally higher than in the million-row families. Absence of a classification here is an outstanding task, **not** a finding that this set carries no PII |
| **Attribution / citation** | Unknown — to confirm with data owner |

**Open questions for the data owner:**

1. **What does `SCDB` stand for?**
2. **Is `NRIC_X` a pseudonym or a real NRIC?** This gates everything else.
3. **Why does `VW_SCDB_HF_F` exist twice**, under `PriorityTables-B1/` and `FreeText_FTA/`,
   with the same row and column counts but a 16 MB size difference? Which is authoritative?
4. What is `PriorityTables-B1/`, and why does only this one object use it?
5. **Is there a data dictionary?** `VW_SCDB_PPM_DIM_F` names 40 of its 45 columns `Field1`
   through `Field40`-ish. No amount of profiling will recover what those hold.
6. What is the relationship between each `X_F` and its `X_DIM_F` partner? Is one derived from
   the other, and on what key?
7. What do `BEFORE`, `T1` and `T2` denote? Why is `INTERVENTION_BEFORE_T2_F` 97.29% empty?
8. **Does `VW_SCDB_ICD_F` hold implantable cardioverter-defibrillator records rather than
   ICD-10 diagnosis codes?** The column names say device; the name says ICD.
9. What does the `S_` prefix denote, and why are `S_` columns consistently far emptier than
   their plain counterparts?
10. What does `ZLMAUDIT` denote in the three audit-named objects?
11. Is `DFTTesting` / `S_DETTesting` a typo in the source, and which spelling is correct?
12. Which population is included in each object, and who is excluded by what mechanism?
13. Are the clinical flag columns (`HEARTFAILURE`, `CVA_STROKE`, `CABG`) genuinely complete,
    or do they use sentinel values for "not recorded"?
14. Are device serial numbers permitted for release, given the cohort sizes here?
15. Is `NRIC_X` linkable to the patient columns in the other families? Does a crosswalk exist?
16. Why is this set split across three prefixes, and does the split mean anything?
17. What is the delimiter and file encoding, and is it the same for all nineteen objects?
18. Who is the data owner and steward role, what is the approval route, and what lead time
    should a study plan for?

---

## Appendix A — Full column profile

**Outstanding.** Roughly 100 of 3,324 columns have been transcribed, and they appear in
*Key Variables* above. Completing this needs the screenshot blocks for all nineteen objects
read end to end — the largest remaining transcription job in the catalogue, and the wide
objects (779, 697 and 367 columns) are the bulk of it.

## Appendix B — Change log

| Date | Change | By |
|---|---|---|
| 2026-07-31 | Page created against `template.md` from the profiler run of 2026-07-23. All nineteen `VW_SCDB_*` objects inventoried with object-level figures. Column fragments transcribed from the screenshots for `VW_SCDB_PPM_DIM_F`, `VW_SCDB_ICD_F` and `VW_SCDB_INTERVENTION_F`. Documented as one page rather than nineteen because the `_F` / `_DIM_F` pairing and the duplicate `HF_F` are only visible side by side. Category from the dataset name and `NRIC_X` as primary identifier, both by catalogue convention. | CCJX |

## Appendix C — Sources

- **Profiler run 2026-07-23** — object-level figures for all nineteen objects. Column
  fragments read from `source_material/screenshots/mass_columns_screenshots/section_09.png`
  (`VW_SCDB_ICD_F` tail, `VW_SCDB_INTERVENTION_BEFORE_T1_F` header) and `section_11.png`
  (`VW_SCDB_INTERVENTION_F` tail, `VW_SCDB_PPM_DIM_F` header).
- `tools/s3_data_catalog.py` — cited only for the profiler's documented behaviour, never for
  any property of these datasets.
- **Not used for column names:** `source_material/imported/profiler_report_full.txt` and
  `column_summary.csv`, which are OCR reconstructions that corrupt column names.
- **Data owner correspondence — none.** Every governance field on this page is unconfirmed.

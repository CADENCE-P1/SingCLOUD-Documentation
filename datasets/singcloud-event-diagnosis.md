# SingCLOUD — Event Diagnosis

| | |
|---|---|
| **Status** | 🟡 Draft |
| **Catalogue alias(es)** | `Event_Diagnosis_P1` … `Event_Diagnosis_P8` |
| **Partitions** | 8 — source files `VW_EVENT_DIAGNOSIS_F_Export_31-07-2024_P{1..8}.csv` |
| **Format** | CSV, delimiter `,` |
| **Last reviewed** | *from the 2024-07-31 extract; not owner-confirmed* |

---

## 1. Content & Scope

**Information type:** Clinical data — diagnoses recorded during encounters, with admission
and discharge context

**Unit of observation:** One row per **diagnosis recorded within an encounter**. A single
encounter yields several rows if several diagnoses were recorded.

**Population represented:** Patients with encounters at participating SingCLOUD
institutions. Unlike MediClaims, inclusion does not depend on a claim being generated —
making this a clinically-driven rather than billing-driven record. Exact institutional
coverage: unknown — to confirm with data owner.

**Period covered:** Unknown — to confirm. Derive empirically from `VISIT_ADMIN_DATE_Z`.

**Variable availability over time:** Unknown — to confirm with data owner. The `_STD`
standardised-text fields are the most likely candidates for later introduction, since they
depend on a standardisation pipeline; check their missingness by year before using them in
a longitudinal design.

### Variables

| Column | Description | Class | Notes |
|---|---|---|---|
| `DATA_SOURCE` | Source system of the record | Raw | Useful for assessing cross-institution consistency |
| `EVN_ID_EXTN` | External event ID | Raw | Encounter key |
| **`PATIENT_ID_EXTN_X`** | **Primary patient ID** | Raw | SingCLOUD identifier family |
| `VISIT_ADMIN_DATE_X` | Admission date (format X) | Raw | |
| **`VISIT_ADMIN_DATE_Z`** | **Admission date, standardised** | Standardised | `YYYY-MM-DD HH:MM:SS` — prefer this |
| `DISCHARGE_DATE_X` | Discharge date (format X) | Raw | |
| **`DISCHARGE_DATE_Z`** | **Discharge date, standardised** | Standardised | `YYYY-MM-DD HH:MM:SS` |
| `PATIENT_TYPE_ETS_ID` | Patient type identifier | Standardised | |
| `EVN_FACILITY_EXTN` | Event facility (hospital) | Raw | |
| `EVN_SERVICE_SPECIALTY_ETS_ID` | Event service specialty ID | Standardised | |
| `EVN_SERVICE_SPECIALTY_TXT` | Event service specialty text | Raw | |
| `EVN_SERVICE_SPECIALTY_TXT_STD` | Event service specialty, standardised | Standardised | |
| `MOV_TYPE_ETS_ID` | Movement type | Standardised | |
| `MOV_CAT_ETS_ID` | Movement category | Standardised | |
| `DISCHARGE_OUTCOME` | Discharge outcome | Standardised | |
| `DISCHARGE_DISPOSITION_ETS_ID` | Discharge disposition | Standardised | |
| `DOC_TYPE_CODE` | Document type code | Standardised | |
| `DOC_TYPE_ETS_ID` | Document type identifier | Standardised | |
| `DIAG_SERVICE_SPECIALTY_ETS_ID` | Diagnosis service specialty ID | Standardised | |
| `DIAG_SERVICE_SPECIALTY_TXT` | Diagnosis service specialty text | Raw | |
| `DIAG_SERVICE_SPECIALTY_TXT_STD` | Diagnosis service specialty, standardised | Standardised | |
| `DIAGNOSIS_NAME_ETS_ID` | Standardised diagnosis name identifier | Standardised | Functions as the diagnosis code in this dataset |
| `DIAGNOSIS_TYPE_ETS_ID` | Diagnosis type identifier | Standardised | |
| `DIAGNOSIS_TYPE_TXT` | Diagnosis type text | Raw | |
| `DIAG_STATUS_ETS_ID` | Diagnosis status | Standardised | |
| `DIAG_ONSET_DATE_X` / `_Z` | Diagnosis onset date | Raw / Standardised | |
| `DIAG_OCCURENCE_DATE_X` / `_Z` | Diagnosis occurrence date | Raw / Standardised | Spelling of "OCCURENCE" is as-is in the source |
| `ICD_CODE_PMH_STD` | Standardised past-medical-history ICD code | Standardised | |
| `ICD_CODE_OUTCOME_STD` | Standardised outcome ICD code | Standardised | |
| **`DIAGNOSIS_NAME_TXT`** | **Raw diagnosis text** | Raw | As entered |
| **`DIAGNOSIS_NAME_TXT_STD`** | **Standardised diagnosis text** | Standardised | Mapped to a controlled description |

---

## 2. Provenance & Processing

**Collection mechanism:** Clinician / clinical-system entry at point of care, aggregated
across participating institutions into a common SingCLOUD view.

**Processing applied:** The `_X` / `_Z` and `_TXT` / `_TXT_STD` column pairs are the visible
trace of a standardisation layer: for several fields the platform retains both the source
value and a normalised counterpart. This is unusually good for provenance — most datasets
in this catalogue keep only one.

**Raw vs interpreted:**
- `DIAGNOSIS_NAME_TXT` is what was entered. `DIAGNOSIS_NAME_TXT_STD` is the result of a
  mapping step. They are **not** interchangeable: the standardised value may collapse
  distinctions present in the raw text, and the mapping may fail or mis-assign for unusual
  entries. Studies that depend on diagnostic nuance should work from the raw text and
  report their own mapping; studies that need consistent cohort selection should use the
  standardised text and acknowledge the mapping as a dependency.
- **The mapping rules behind the `_STD` fields are not documented here.** Unknown — to
  confirm with data owner. This is a material gap for anyone whose results depend on them.
- `DATA_SOURCE` and `EVN_FACILITY_EXTN` exist because recording practice differs by
  institution. Cross-institution comparisons should check for source-driven variation
  before attributing differences to clinical factors.

---

## 3. Feasibility & Quality

**Primary identifier:** `PATIENT_ID_EXTN_X`

**Linkage keys:**

| Links to | On | Granularity | Notes |
|---|---|---|---|
| [Laboratory items](singcloud-laboratory-items.md) | `PATIENT_ID_EXTN_X` | Diagnosis → result | Same identifier family |
| Other SingCLOUD `VW_*` views | `PATIENT_ID_EXTN_X` | | Same identifier family |
| MediClaims / COVID datasets | — | — | **Different identifier family** (`uin`); crosswalk not confirmed |

**Coding standards:** Primarily **free text and standardised text**, not ICD. ICD codes
appear only in `ICD_CODE_PMH_STD` and `ICD_CODE_OUTCOME_STD`, which serve specific purposes
(past medical history, outcome) and are not a general diagnosis coding for the row.

This is the single most consequential fact about the dataset: **case-finding here is a text
matching exercise, not a code lookup.** A study that ascertains a condition by ICD code in
MediClaims and by text in Event Diagnosis will produce two non-identical patient sets, and
must state how it combines them.

**Known linkage pitfalls:**
- Multiple rows per encounter, multiple encounters per patient — reduce before merging.
- Data spans 8 partitions with no guarantee a patient's records fall in one file. A
  patient-level operation must scan all 8.
- Cross-family linkage to MediClaims is unresolved.

**Scale:** 8 partitions. `Event_Diagnosis_P1` alone holds **5,084,554 rows** *(observed in
the 2024-07-31 extract)*. If the partitions are comparable in size the family is on the
order of 40 million rows — profile the remaining seven to confirm rather than extrapolating.

**Missingness:** Not yet profiled. Priority columns to profile: `DIAGNOSIS_NAME_TXT_STD`,
`ICD_CODE_PMH_STD`, `DIAG_ONSET_DATE_Z`.

**Known biases:**
- Institutional coverage is partial — absence of a diagnosis does not mean absence of the
  condition, only absence from participating institutions' records.
- Free-text entry means ascertainment depends on the keyword list used, which varies
  between researchers. Any curated keyword list should be published with the study.

---

## 4. Ownership & Governance

| | |
|---|---|
| **Data owner** | Unknown — to confirm with data owner |
| **Steward / contact** | Unknown — to confirm with data owner |
| **Access restrictions** | Unknown — to confirm with data owner |
| **Approval requirements** | Unknown — to confirm with data owner. Free-text clinical fields may attract additional conditions |
| **Typical lead time** | Unknown — to confirm with data owner |
| **Permitted use / conditions** | Unknown — to confirm with data owner |

---

## 5. Notes for analysts

- Prefer the `_Z` date columns (`YYYY-MM-DD HH:MM:SS`) over `_X`.
- Process partitions one at a time and accumulate; do not concatenate all 8 in memory.
- Build and version your diagnosis keyword list as a separate artefact — it determines your
  cohort.

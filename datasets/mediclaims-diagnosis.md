# MediClaims — Diagnosis Records

| | |
|---|---|
| **Status** | 🟡 Draft |
| **Catalogue alias(es)** | `mediclaims_diag_{year}` |
| **Partitions** | One file per year, 2015–2023 (9 files) |
| **Format** | CSV |
| **Last reviewed** | *from 2024 working notes; not owner-confirmed* |

---

## 1. Content & Scope

**Information type:** Billing / claims data, carrying clinical diagnosis codes

**Unit of observation:** One row per **diagnosis event** — a patient appears many times

**Population represented:**
Patients whose care generated a national health insurance claim. This is **not a
whole-population record**. Care that produced no claim does not appear, which is a
selection effect that must be stated in any study design using this dataset as a
denominator or as a case-finding source.

**Period covered:** 2015–2023, one file per year

**Variable availability over time:** Unknown — to confirm with data owner. Column stability
across the nine annual files has not been formally verified; column presence and naming
should be checked per year rather than assumed from any single year.

### Variables

| Column | Description | Class | Notes |
|---|---|---|---|
| `uin` / `PATIENT_ID` | Patient identifier | Raw | Naming has been observed to vary; normalise on load |
| `diagcode` | ICD-10 diagnosis code | Standardised | **Appears both with and without the decimal point** — see below |
| `diagdesc` | Diagnosis description | Raw (free text) | Operator-entered |
| `dischargedate` | Discharge date | Raw | Parse explicitly; format varies |

> The variable list above covers the columns used in practice, not necessarily the full
> column manifest. A complete manifest should be generated with
> [`tools/s3_data_catalog.py`](../tools/s3_data_catalog.py) and pasted in.

---

## 2. Provenance & Processing

**Collection mechanism:** Submitted as part of national health insurance claims processing.
Diagnosis codes are assigned for reimbursement purposes.

**Processing applied:** Patient identifiers are pseudonymised. Files are split by calendar
year.

**Raw vs interpreted:** `diagcode` is a coded, administratively-assigned representation of
a clinical event, not a direct clinical record. Claims coding is subject to reimbursement
incentives and coder practice, and the code assigned may differ from what a clinician would
record in a clinical system for the same encounter. For research needing the clinical
record rather than the billed representation, the
[SingCLOUD Event Diagnosis](singcloud-event-diagnosis.md) dataset is the closer source.

---

## 3. Feasibility & Quality

**Primary identifier:** `uin` — read as string to preserve format

**Linkage keys:**

| Links to | On | Granularity | Notes |
|---|---|---|---|
| [MediClaims episodes](mediclaims-episodes.md) | `uin` | Event → episode | Same identifier family |
| [COVID case registry](covid-confirmed-case-registry.md) | `uin` | Event → case | Same identifier family |
| [Death registry](death-registry.md) | `uin` | Event → person | Same identifier family |
| SingCLOUD clinical views | — | — | **Different identifier family** (`PATIENT_ID_EXTN_X`); crosswalk not confirmed |

**Coding standards:** ICD-10

**Known linkage pitfalls:**
- **ICD-10 dot inconsistency.** Codes occur as both `I21.0` and `I210` within the same
  dataset. A pattern matching only one form silently drops true cases. Every regex and
  lookup must accept both.
- Identifier column naming varies across years and against other datasets.

**Scale:** Millions of rows per year

**Missingness:** Not yet profiled — run the profiler and record per-column figures here.

**Known biases:**
- **Claims-generating care only** — see population note above.
- Diagnosis coding reflects billing practice, which may change over the 2015–2023 span
  independently of any change in underlying disease incidence. Studies looking at trends
  over time should treat coding-practice change as a competing explanation.

---

## 4. Ownership & Governance

| | |
|---|---|
| **Data owner** | Unknown — to confirm with data owner |
| **Steward / contact** | Unknown — to confirm with data owner |
| **Access restrictions** | Unknown — to confirm with data owner |
| **Approval requirements** | Unknown — to confirm with data owner |
| **Typical lead time** | Unknown — to confirm with data owner |
| **Permitted use / conditions** | Unknown — to confirm with data owner |

---

## 5. Notes for analysts

- **Load one year at a time.** The full 2015–2023 span will not fit comfortably in memory.
- Read identifier columns with `dtype=str` to avoid losing leading zeros.
- Parse dates explicitly; do not rely on inference. Use `dayfirst=True` where the format is
  ambiguous.
- De-duplicate to patient level before any patient-level analysis, using an explicit rule
  (typically first qualifying event).

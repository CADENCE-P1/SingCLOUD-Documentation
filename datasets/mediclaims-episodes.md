# MediClaims — Episodes

| | |
|---|---|
| **Status** | 🟡 Draft |
| **Catalogue alias(es)** | `mediclaims_epi_{year}` |
| **Partitions** | One file per year, 2017–2023 (7 files) |
| **Format** | CSV, delimiter `,` |
| **Last reviewed** | *from 2024 working notes; not owner-confirmed* |

---

## 1. Content & Scope

**Information type:** Billing / claims data with admission, length-of-stay and cost fields

**Unit of observation:** One row per **inpatient episode**

**Population represented:**
Patients with a claims-generating inpatient episode. Carries a `resident_type` field, which
makes this the practical source for restricting a cohort to Singapore residents within the
MediClaims family.

**Period covered:** 2017–2023

**Variable availability over time:** This dataset starts in **2017**, two years later than
[MediClaims diagnosis](mediclaims-diagnosis.md) (2015). Any study needing `admission_date`,
`resident_type`, length of stay or billing for 2015–2016 cannot get them from here. This is
a concrete instance of the "earlier records may not contain certain variables" problem — at
the dataset level rather than the column level.

### Variables

| Column | Description | Class | Notes |
|---|---|---|---|
| `uin` | Unique identification number (patient ID) | Raw | Primary key |
| `pataccno` | Patient account number | Raw | Episode-level account reference |
| `resident_type` | Residency status | Standardised | 8 distinct values — see below |
| `case_type` | Type of medical case | Standardised | |
| `sector` | Healthcare sector classification | Standardised | |
| `hospital` | Treating hospital / institution | Standardised | |
| `admission_date` | Date of admission | Raw | Not available before 2017 |
| `discharge_date` | Date of discharge | Raw | |
| `los` | Total length of stay (days) | Derived | Computed from admission/discharge |
| `icu_los` | ICU length of stay (days) | Derived | |
| `finaldiagcode` | Final diagnosis code | Standardised | One final diagnosis per episode — **not** a full problem list |
| `finaldiagdesc` | Final diagnosis description | Raw (free text) | |
| `tot_bill` | Total bill amount | Raw | |
| `tot_bill_bmt` | Total bill amount (BMT-specific) | Raw | |
| `facil_type` | Facility type | Standardised | |

### `resident_type` values

Observed distribution across the extract
([evidence](../source_material/screenshots/mediclaims_epi__resident_type_values.png)):

| Value | Count |
|---|---:|
| `SINGAPORE PINK NRIC` | 4,615,976 |
| `SINGAPORE BLUE NRIC` | 282,258 |
| `OTHER TYPES OF UNIQUE IDENTIFICATION` | 151,245 |
| `CPF ACCOUNT NUMBER` | 36,400 |
| `LONG TERM VISIT PASS` | 4,068 |
| `MALAYSIAN IC` | 1,256 |
| `UIN (APPLICABLE ONLY FOR NON-IC HOLDER)` | 775 |
| *(missing)* | 2 |

`SINGAPORE PINK NRIC` (citizens) and `SINGAPORE BLUE NRIC` (permanent residents) together
account for ~96% of rows. The remaining categories are non-resident or non-standard
identification types.

Two cautions. First, the strings are exact and unforgiving — earlier working notes recorded
these as `SINGAPORE PINK IC` / `SINGAPORE BLUE IC` (no `NRIC`), and filtering on that
version returns **zero rows without raising an error**. Second, this distribution is from
one extract; run `value_counts()` on your own before filtering rather than trusting this
table.

---

## 2. Provenance & Processing

**Collection mechanism:** Claims submission for inpatient episodes.

**Processing applied:** Pseudonymised identifiers; split by calendar year.

**Raw vs interpreted:**
- `los` and `icu_los` are **derived** from admission and discharge timestamps. Where the
  exact derivation matters (part-days, transfers, same-day discharge), recompute from
  `admission_date` / `discharge_date` rather than trusting the field.
- `finaldiagcode` is a single administrative summary of an episode that may have involved
  several conditions. It is not equivalent to the set of diagnoses recorded during the
  episode, and using it as a case-finding source will under-ascertain secondary conditions.

---

## 3. Feasibility & Quality

**Primary identifier:** `uin`

**Linkage keys:**

| Links to | On | Granularity | Notes |
|---|---|---|---|
| [MediClaims diagnosis](mediclaims-diagnosis.md) | `uin` | Episode ↔ event | Many-to-many; reduce to patient level first |
| [COVID case registry](covid-confirmed-case-registry.md) | `uin` | Episode → case | |
| [Death registry](death-registry.md) | `uin` | Episode → person | |

**Coding standards:** ICD-10 in `finaldiagcode`; free text in `finaldiagdesc`

**Known linkage pitfalls:**
- A patient has multiple episodes. Merging without prior reduction multiplies rows.
- `resident_type` value strings vary between extracts. Filtering on a hard-coded list taken
  from documentation — including this page — risks silently dropping the entire cohort.
  Always run `df['resident_type'].value_counts()` first.

**Scale:** Not yet profiled

**Missingness:** Not yet profiled

**Known biases:**
- Inpatient episodes only — outpatient and primary care activity is absent.
- Claims-generating care only.
- Coverage begins 2017, so any pre-2017 comparison period is unavailable.

---

## 4. Ownership & Governance

| | |
|---|---|
| **Data owner** | Unknown — to confirm with data owner |
| **Steward / contact** | Unknown — to confirm with data owner |
| **Access restrictions** | Unknown — to confirm with data owner |
| **Approval requirements** | Unknown — to confirm with data owner. Note this dataset carries **billing amounts**, which may attract restrictions beyond the clinical datasets |
| **Typical lead time** | Unknown — to confirm with data owner |
| **Permitted use / conditions** | Unknown — to confirm with data owner |

---

## 5. Notes for analysts

- This is the MediClaims dataset that carries `admission_date` and `resident_type`; the
  diagnosis dataset does not.
- Load year by year.
- Verify `resident_type` categories empirically before filtering.

# SingCLOUD — Medication Items

| | |
|---|---|
| **Status** | 🟡 Draft |
| **Catalogue alias(es)** | `SingCLOUD_medication_items{n}`, n = 1…29 |
| **Partitions** | 29 |
| **Format** | CSV |
| **Last reviewed** | *from 2024 working notes; not owner-confirmed* |

---

## 1. Content & Scope

**Information type:** Medication dispensing records

**Unit of observation:** One row per **dispensed medication**

**Population represented:** Patients dispensed medication at participating institutions.
Dispensing is not the same as prescribing, and neither is the same as *taking* the
medication — see §2.

**Period covered:** Unknown — to confirm. Derive empirically from the dispense date column.

**Variable availability over time:** Unknown — to confirm with data owner.

### Variables

| Column | Description | Class | Notes |
|---|---|---|---|
| `PATIENT_ID` | Patient identifier | Raw | **Exact column name not verified** — confirm against the extract before use |
| `MEDICATION_NAME` / `DRUG_NAME` | Medication name | Raw (free text) | Naming observed to vary; requires keyword matching |
| `DISPENSE_DATE` | Date dispensed | Raw | |

> ⚠️ The variable list for this dataset is **incomplete and partially unverified** — it
> records only the columns used in one analysis, with column names that varied across
> extracts. A full manifest should be generated with
> [`tools/s3_data_catalog.py`](../tools/s3_data_catalog.py) before this page is relied on.
> Fields likely present but undocumented: dose, quantity, duration, route, prescriber and
> facility.

---

## 2. Provenance & Processing

**Collection mechanism:** Pharmacy dispensing systems at participating institutions.

**Processing applied:** Partitioned into 29 files — the largest partition count in the
catalogue, indicating a very large dataset.

**Raw vs interpreted:** Medication names are free text with no standard vocabulary (no ATC,
RxNorm or equivalent observed). Grouping into drug classes is therefore **an interpretation
the researcher performs**, not a property of the data.

A dispensing record evidences that medication left the pharmacy. It does not evidence
adherence. Studies treating a dispensing record as "patient was on drug X during period Y"
are making an assumption that should be stated, and exposure windows must be constructed
explicitly — the dataset provides dispensing events, not exposure periods.

---

## 3. Feasibility & Quality

**Primary identifier:** `PATIENT_ID` (confirm exact name and identifier family — it is not
established here whether this dataset uses `PATIENT_ID_EXTN_X` or a different form)

**Linkage keys:** Determined by which identifier family applies. **Confirm before scoping
any study that depends on linking medications to other datasets.**

**Coding standards:** None observed — free-text drug names.

Illustrative keyword sets used in practice, offered as a starting point only:

| Class | Keywords |
|---|---|
| Statin | `statin` |
| Antiplatelet | `aspirin`, `clopidogrel`, `ticagrelor`, `prasugrel`, `dipyridamole`, `cilostazol` |
| Antihypertensive | `pril`, `sartan`, `olol`, `dipine`, `furosemide`, `hydrochlorothiazide` |

Stem-based matching of this kind (`pril`, `olol`, `dipine`) is convenient but imprecise:
stems match unintended drugs and miss agents that do not carry the stem. Any class
definition should be validated against the actual distinct values in the extract, and
published with the study.

**Known linkage pitfalls:**
- 29 partitions with no guarantee of patient locality.
- Many dispensing events per patient — reduce to patient level with an explicit rule.

**Scale:** 29 partitions; not yet profiled. Expect this to be memory-critical.

**Missingness:** Not yet profiled.

**Known biases:**
- Institutional coverage is partial; medication obtained elsewhere is absent.
- Dispensing ≠ adherence.

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

- Filter to your drug classes while streaming each of the 29 partitions.
- Inspect `df.columns` per partition — column naming has been observed to vary.
- Lowercase drug names before keyword matching.

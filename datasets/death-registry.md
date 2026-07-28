# Death Registry

| | |
|---|---|
| **Status** | 🟡 Draft |
| **Catalogue alias(es)** | `death_registry` |
| **Partitions** | 1 |
| **Format** | CSV |
| **Last reviewed** | *from 2024 working notes; not owner-confirmed* |

---

## 1. Content & Scope

**Information type:** Vital statistics registry

**Unit of observation:** One row per **death event**

**Population represented:** Registered deaths. As a statutory registry this is expected to
be near-complete for the resident population — making it the most reliable outcome source
in the catalogue, and the only true whole-population one.

**Period covered:** Unknown — to confirm. Derive from `DATE_OF_DEATH`.

**Variable availability over time:** Unknown — to confirm with data owner.

### Variables

| Column | Description | Class | Notes |
|---|---|---|---|
| `PATIENT_ID` / `uin` | Patient identifier | Raw | **Naming has been observed to vary** — confirm against the extract |
| `DATE_OF_DEATH` | Date of death | Raw | |
| `CAUSE_OF_DEATH` | Cause of death, ICD-10 | Standardised | An interpretation — see §2 |

> Manifest covers observed columns only. Fields likely present but undocumented: place of
> death, underlying vs contributing cause, certifier type.

---

## 2. Provenance & Processing

**Collection mechanism:** Statutory death registration.

**Processing applied:** Pseudonymised identifiers.

**Raw vs interpreted:** The two fields differ sharply in reliability, and it matters:

- `DATE_OF_DEATH` is a **fact**, recorded administratively. Highly reliable.
- `CAUSE_OF_DEATH` is a **certified clinical judgement**, coded to ICD-10. It reflects the
  certifying practitioner's assessment and the coding conventions in force. Cause-of-death
  coding is known to vary by certifier, by era, and by whether a post-mortem was performed.

The practical consequence: **all-cause mortality is a far more robust outcome than
cause-specific mortality** in this dataset. Studies using cause-specific death as a primary
endpoint should treat certification practice as a source of misclassification and, where
possible, report all-cause mortality alongside it.

---

## 3. Feasibility & Quality

**Primary identifier:** `PATIENT_ID` / `uin` — confirm exact name

**Linkage keys:**

| Links to | On | Granularity | Notes |
|---|---|---|---|
| [MediClaims](mediclaims-diagnosis.md) | `uin` | Person → event | Same identifier family |
| [COVID case registry](covid-confirmed-case-registry.md) | `uin` | Person → case | |
| SingCLOUD clinical views | — | — | **Different identifier family**; crosswalk not confirmed |

**Coding standards:** ICD-10 for cause of death. Check for the same dot/no-dot inconsistency
documented for [MediClaims](mediclaims-diagnosis.md) before pattern-matching codes.

**Known linkage pitfalls:**
- Identifier column naming varies.
- One row per death makes this a clean patient-level merge.
- **Absence of a row means "not recorded as died", which is not the same as "alive".** For
  survival analysis, establish the registry's complete-through date and censor at it —
  otherwise recent deaths not yet registered appear as survivors.

**Scale:** Not yet profiled.

**Missingness:** Not yet profiled. `CAUSE_OF_DEATH` completeness is the priority figure.

**Known biases:**
- Cause-of-death misclassification, as above.
- Registration lag at the end of the coverage period.

---

## 4. Ownership & Governance

| | |
|---|---|
| **Data owner** | Unknown — to confirm with data owner |
| **Steward / contact** | Unknown — to confirm with data owner |
| **Access restrictions** | Unknown — to confirm with data owner. Vital statistics commonly carry restrictions beyond baseline access |
| **Approval requirements** | Unknown — to confirm with data owner |
| **Typical lead time** | Unknown — to confirm with data owner |
| **Permitted use / conditions** | Unknown — to confirm with data owner |

---

## 5. Notes for analysts

- Establish the registry's complete-through date and censor survival analyses there.
- Prefer all-cause mortality where the research question allows.

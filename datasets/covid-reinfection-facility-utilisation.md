# Facility Utilisation / LOS — Subsequent Reinfections

| | |
|---|---|
| **Status** | 🟡 Draft |
| **Catalogue alias(es)** | `FacilityUtilizationLOSSubsequentRI` |
| **Partitions** | 1 |
| **Format** | CSV |
| **Last reviewed** | *from 2024 working notes; not owner-confirmed* |

---

## 1. Content & Scope

**Information type:** Administrative / facility utilisation

**Unit of observation:** One row per **reinfection episode**

**Population represented:** Confirmed reinfected COVID-19 patients who used managed
facilities. At ~2,319 rows this is by far the smallest dataset in the catalogue — roughly
1.8% of the [COVID reinfections](covid-reinfections.md) dataset. **The reason for that gap
is not documented** and should be established before either file is treated as complete:
it may reflect a facility-use requirement, a date window, or a different case definition.

**Period covered:** Derive from `notificationdate`.

**Variable availability over time:** Vaccination columns structurally empty pre-rollout.

### Variables

| Column | Description | Class | Notes |
|---|---|---|---|
| `uin` | Patient identifier | Raw | |
| `notificationdate` | Notification date | Raw | |
| `Age`, `Gender` | Demographics | Standardised / Derived | **Capitalised here** — a third naming convention across the COVID datasets |
| `reinfection_type` | Type of reinfection | Derived | |
| `reinfno` | Reinfection number | Derived | Which reinfection this is for the patient |
| `prev_reinf_notif` | Previous reinfection notification date | Raw | Enables interval calculation |
| `NRDate` | Date field, meaning undocumented | Unknown | **Confirm with data owner** |
| `DaysAtPHI`, `DaysAtCTF`, `DaysAtCIF`, `DaysAtCIFM` | Days at facility types | Derived | Four types here vs six in the reinfections dataset — **confirm whether the definitions match** |
| `DaysInICU`, `DaysO2` | ICU and oxygen days | Derived | |
| `vacc_date1`–`vacc_date5` | Vaccination dates | Raw | 5 doses |
| `vaccbrand1`–`vaccbrand5` | Vaccine brands | Standardised | |

**Approximate rows:** ~2,319 *(observed)*

---

## 2. Provenance & Processing

**Collection mechanism:** Facility management records restricted to reinfection episodes.

**Processing applied:** Appears to be a targeted extract rather than a full registry view.

**Raw vs interpreted:** `reinfno` and the `DaysAt*` fields are derived. This file carries
**four** facility-type day columns where [COVID reinfections](covid-reinfections.md) carries
**six**; whether the four are the same four, a subset, or differently defined is unknown.
Combining or comparing the two without confirming this will produce durations that look
comparable and are not.

---

## 3. Feasibility & Quality

**Primary identifier:** `uin`

**Linkage keys:**

| Links to | On | Granularity | Notes |
|---|---|---|---|
| [COVID reinfections](covid-reinfections.md) | `uin` | Overlapping scope | Relationship between the two files is unresolved |
| [COVID case registry](covid-confirmed-case-registry.md) | `uin` | Episode → case | |

**Coding standards:** Category labels.

**Known linkage pitfalls:**
- **Third demographic naming convention** in this dataset family: `Age`/`Gender`
  (capitalised) here, `age`/`gender` in COVIDFACILLOS, `age`/`cat_gender` in COVID
  Reinfections. Normalise column names before any cross-dataset work.
- The small size means merges will look "successful" while contributing almost nothing;
  always report the match count, not just that the merge ran.

**Scale:** ~2,319 rows *(observed)* — **too small to support subgroup analysis.** Treat as a
supplementary flag source, not an analytic dataset.

**Missingness:** Not yet profiled.

**Known biases:**
- Facility users among reinfected patients only — a severity-selected subset of a
  detection-selected subset.

---

## 4. Ownership & Governance

| | |
|---|---|
| **Data owner** | Unknown — to confirm with data owner |
| **Steward / contact** | Unknown — to confirm with data owner |
| **Access restrictions** | Unknown — to confirm with data owner |
| **Approval requirements** | Unknown — to confirm with data owner |
| **Typical lead time** | Unknown — to confirm with data owner |
| **Permitted use / conditions** | Unknown — to confirm with data owner. **Small cell counts** make this dataset a disclosure risk; expect suppression requirements on any published breakdown |

---

## 5. Notes for analysts

- Do not power a study on this dataset. Use it as a supplementary reinfection flag.
- Normalise `Age`/`Gender` casing when combining with sibling COVID datasets.

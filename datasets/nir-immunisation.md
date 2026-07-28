# NIR — National Immunisation Registry (truncated list)

| | |
|---|---|
| **Status** | 🟡 Draft |
| **Catalogue alias(es)** | `NIRListtruncated` |
| **Partitions** | 1 |
| **Format** | CSV |
| **Last reviewed** | *from 2024 working notes; not owner-confirmed* |

---

## 1. Content & Scope

**Information type:** Immunisation registry

**Unit of observation:** One row per **person** — genuinely patient-level, unlike most
datasets in this catalogue

**Population represented:** **All residents**, not only those with a COVID episode. This
makes it the most complete vaccination source available and the correct choice for any
analysis needing vaccination status for a general cohort.

**Period covered:** From the start of COVID-19 vaccination rollout. Derive bounds
empirically from `vacc_date1`.

**Variable availability over time:** Vaccination records begin when the programme begins;
dose 5 and 6 columns populate only from the later booster campaigns.

### Variables

| Column | Description | Class | Notes |
|---|---|---|---|
| `uin` | Patient identifier | Raw | |
| `vacc_date1`–`vacc_date6` | Dates of doses 1–6 | Raw | Wide format; **6 doses**, more than COVIDFACILLOS' 5 |
| `vaccbrand1`–`vaccbrand6` | Vaccine brand per dose | Standardised | |

**Approximate rows:** ~6,174,098 *(observed)*

> The alias contains "truncated" — **what was truncated is unknown and should be confirmed
> with the data owner.** It may refer to a column subset, a date cut-off, or a population
> restriction. This matters for any completeness claim made about the dataset, and it is
> the first question to ask about it.

---

## 2. Provenance & Processing

**Collection mechanism:** National Immunisation Registry — administrative recording of
administered vaccinations.

**Processing applied:** Denormalised into wide dose columns. Some form of truncation, per
the alias.

**Raw vs interpreted:** Dose dates and brands are recorded administrative facts. Everything
downstream is derived by the researcher:

- **"Doses before date D"** is not a column. It requires a row-wise scan across
  `vacc_date1`–`vacc_date6`.
- **"Fully vaccinated"** is a definition, not a field, and its meaning changed over the
  pandemic (two doses, then three, then bivalent boosters). Any study using the term must
  state which definition and at which reference date.

---

## 3. Feasibility & Quality

**Primary identifier:** `uin`

**Linkage keys:**

| Links to | On | Granularity | Notes |
|---|---|---|---|
| [COVID case registry](covid-confirmed-case-registry.md) | `uin` | Person → case | Same identifier family |
| [COVIDFACILLOS](covid-facility-los.md) | `uin` | Person → episode | |
| [MediClaims](mediclaims-diagnosis.md) | `uin` | Person → event | |

**Coding standards:** Vaccine brand as category labels — enumerate values in your extract.

**Known linkage pitfalls:**
- **Dose column count differs between sources** (6 here, 5 in COVIDFACILLOS and the
  reinfection extracts). Code written against 5 silently ignores dose 6.
- One row per person makes this the cleanest merge in the catalogue — no prior reduction
  needed.

**Scale:** ~6,174,098 rows *(observed)*

**Missingness:** Not yet profiled. Late-dose columns will be structurally sparse.

**Known biases:**
- Records administered doses. Vaccination received overseas may be absent or
  inconsistently recorded.
- Unclear truncation (see above) is an unquantified completeness risk.

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

- Prefer this over COVIDFACILLOS or the reinfection files for vaccination status: it covers
  6 doses and the whole resident population.
- Parse all six date columns before computing dose counts relative to an index date.
- State your "fully vaccinated" definition explicitly.

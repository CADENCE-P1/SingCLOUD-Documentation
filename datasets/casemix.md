# Casemix

| | |
|---|---|
| **Status** | ⚪ Stub |
| **Catalogue alias(es)** | `casemix_data_{fy}` — e.g. `casemix_data_2012_2013_df` |
| **Partitions** | One file per financial year |
| **Format** | CSV, delimiter `\|` *(pipe — not comma, unlike every other dataset in this catalogue)* |
| **Last reviewed** | *from a catalogue configuration entry only; contents not inspected* |

---

## 1. Content & Scope

**Information type:** Case-mix aggregate extract — administrative / costing

**Unit of observation:** One row per **inpatient spell**

**Population represented:** Inpatient spells within the covered financial years. Unknown —
to confirm with data owner.

**Period covered:** Financial-year files. The example entry covers **April 2012 – March
2013**, which if representative makes this **the earliest data in the catalogue** — three
years before MediClaims diagnosis (2015) and five before MediClaims episodes (2017). Any
study needing a pre-2015 baseline should investigate this dataset first.

**Full year coverage is unknown and should be established.**

**Variable availability over time:** Unknown — to confirm with data owner.

### Variables

Not yet documented. Run [`tools/s3_data_catalog.py`](../tools/s3_data_catalog.py) against
the casemix prefix and populate this section.

---

## 2. Provenance & Processing

**Collection mechanism:** Case-mix classification of inpatient spells, derived from
hospital administrative and clinical coding systems.

**Processing applied:** Pseudo-IDs are **encrypted** per the catalogue entry — note this is
described differently from the pseudonymisation used elsewhere, and the difference may
affect linkability. Confirm with the data owner.

**Raw vs interpreted:** Case-mix data is inherently **derived** — spells are assigned to
groups by a grouper algorithm applied to diagnosis and procedure codes. The grouper version
determines the assignment, and grouper versions change between years. Comparing case-mix
groups across years without accounting for grouper version compares two different
classification systems.

---

## 3. Feasibility & Quality

**Primary identifier:** Unknown — to confirm. **Whether the encrypted pseudo-IDs are
linkable to `uin` or `PATIENT_ID_EXTN_X` is the decisive question for this dataset** and is
unresolved. If they are not, casemix is usable only as a standalone aggregate resource.

**Linkage keys:** Unknown — see above.

**Coding standards:** Case-mix groups plus, presumably, underlying ICD codes. To confirm.

**Known linkage pitfalls:**
- **Pipe-delimited.** Reading it with a default comma delimiter yields a single-column
  DataFrame — a failure that is obvious once seen and puzzling until then.
- Encrypted identifiers may be non-linkable.

**Scale:** Not yet profiled.

**Missingness:** Not yet profiled.

**Known biases:**
- Inpatient spells only.
- Grouper version changes over time.

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

- Read with `sep='|'`.
- Establish identifier linkability before scoping any study that depends on joining casemix
  to other datasets.

---

> **Why this stub is here.** The rationale for this catalogue notes that stakeholders may
> "overlook datasets that can better meet their research objectives". Casemix is the live
> example: it is the earliest-covering dataset known to the catalogue and is currently the
> least documented. It is listed precisely so it is not overlooked.

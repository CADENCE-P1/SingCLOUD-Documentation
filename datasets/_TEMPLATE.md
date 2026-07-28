# <Dataset name>

| | |
|---|---|
| **Status** | ⚪ Stub |
| **Catalogue alias(es)** | `<exact alias string>` |
| **Partitions** | `<n>` files — pattern `<alias_P{1..n}>` |
| **Format** | CSV, delimiter `,` |
| **Last reviewed** | *not yet reviewed* |

---

## 1. Content & Scope

**Information type:** <clinical / lab / billing / administrative / registry / demographic>

**Unit of observation:** One row per <patient / encounter / event / result>

**Population represented:**
<Who is included. State explicitly who is excluded.>

**Period covered:** <earliest> to <latest> *(observed in <extract>)*

**Variable availability over time:**
<Fields not present or unusable in earlier records, and from roughly when they become
usable. Write "Unknown — to confirm with data owner" if not established.>

### Variables

| Column | Description | Class | Notes |
|---|---|---|---|
| `<COLUMN>` | | Raw / Standardised / Derived | |

---

## 2. Provenance & Processing

**Collection mechanism:**
<How the value reaches this dataset.>

**Processing applied:**
<De-identification, standardisation mappings, de-duplication, truncation.>

**Raw vs interpreted:**
<Which fields are interpretations rather than source values, and whether the source value
is obtainable elsewhere.>

---

## 3. Feasibility & Quality

**Primary identifier:** `<COLUMN>` — <type and format>

**Linkage keys:**

| Links to | On | Granularity | Notes |
|---|---|---|---|
| | | | |

**Coding standards:** <ICD-10 / SNOMED / local / free text>

**Known linkage pitfalls:**
- <…>

**Scale:** ~<n> rows, ~<n> distinct patients

**Missingness:**

| Column | Missing % | Notes |
|---|---|---|
| | | |

**Known biases:**
- <…>

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

<Practical gotchas: loading, memory, date parsing, encoding, chunking.>

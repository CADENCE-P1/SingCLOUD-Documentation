# Analyst dataset notes — index

Working notes on SingCLOUD datasets, written during an analysis project (a COVID-19 /
ischaemic heart disease cohort study) that used a **2024-07 extract** of the platform.
They are retained because they record analyst-observed detail — variable meanings,
Raw/Standardised/Derived classes, loading quirks — that the base catalog pages do not
yet carry.

> **Looking for the data catalog?** The canonical, platform-wide catalogue is
> [`catalog_pages/`](../catalog_pages/index.md) — 17 pages covering every object the
> profiler found (206 objects, 76 families). Start there. The notes below *supplement*
> the corresponding catalog pages and should be folded into them during pass 2.

**Status:** ✅ Verified (profiler-checked *and* owner-confirmed) · 🟡 Draft (analyst
knowledge, not owner-confirmed) · ⚪ Stub (known to exist, not documented)

---

## Notes pages

| Notes page | Alias pattern (2024-07 extract) | Unit of observation | Related catalog page(s) | Status |
|---|---|---|---|---|
| [SingCLOUD — Event Diagnosis](singcloud-event-diagnosis.md) | `Event_Diagnosis_P{1-8}` | Diagnosis within encounter | [Event Diagnosis](../catalog_pages/singcloud-event-diagnosis.md) | 🟡 |
| [SingCLOUD — Laboratory Items](singcloud-laboratory-items.md) | `VW_LABORATORY_ITEM_FIL_F_Export_{date}_P{1-22}` | Test result | [Laboratory Item FIL](../catalog_pages/singcloud-laboratory-item-fil.md), [Laboratory](../catalog_pages/singcloud-laboratory.md) | 🟡 |
| [SingCLOUD — Medication Items](singcloud-medications.md) | `SingCLOUD_medication_items{1-29}` | Dispensed medication | [Dispensed Medication Item](../catalog_pages/singcloud-dispensed-medication-item.md), [Dispensed Medication](../catalog_pages/singcloud-dispensed-medication.md) | 🟡 |
| [SingCLOUD — Demographics](singcloud-demographics.md) | `SingCLOUD_gender`, `SingCLOUD_DOB` | **Person** | [Dimension tables index](../catalog_pages/singcloud-dimension-tables-index.md) | 🟡 |

The partition counts and aliases above are as observed in the 2024-07 extract; the
profiler run of 2026-07-23 (see the catalog pages) reports different partition layouts
for some families. Reconciling the two is a pass-2 task.

> **Removed pages.** Notes on the non-SingCLOUD datasets used by the same study —
> MediClaims, Casemix, the COVID-19 registries, Death Registry, NIR and serology tests —
> were removed from this catalogue when its scope was narrowed to the SingCLOUD platform.
> They remain available in the git history.

---

## Known gaps

These apply to every notes page and are tracked here rather than repeated:

1. **Ownership and governance is undocumented.** No data owner, approval requirement or
   lead time is recorded anywhere. See
   [docs/02_access_and_governance.md](../docs/02_access_and_governance.md).
2. **Period covered is unconfirmed.** Derivable empirically from the date columns; not
   yet done.
3. **The `uin` ↔ `PATIENT_ID_EXTN_X` crosswalk is unresolved.** This determines whether
   external registry data can be joined to SingCLOUD clinical data at all. See
   [docs/03_linkage_guide.md](../docs/03_linkage_guide.md).
4. **Column manifests are partial** for medications and demographics — they record the
   fields used in one analysis, not the full schema. The catalog pages carry the full
   profiler column lists.
5. **Variable availability over time is undocumented** except where structurally
   obvious.

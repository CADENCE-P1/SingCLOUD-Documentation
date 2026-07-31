# SingCLOUD data catalog — page index

Which catalog page covers which object. Start here to find the page for a file you are
holding, or to check whether an object is documented at all.

| | |
|---|---|
| **Objects** | 206 |
| **Families** | 76 |
| **Catalog pages** | 17 |
| **Profiler run** | 2026-07-23 |
| **Object list verified** | 2026-07-31, by a full sweep of all 28 screenshot sections |

**Every object in the profiler report belongs to a page below.** Two have unresolved partition
identities — see *Unresolved* at the end — but both belong to families that are documented.

---

## Pages and their objects

| Data catalog page | Dataset objects in the page |
|---|---|
| [CGH Nuclear](singcloud-cgh-nuclear.md)<br>*1 object* | `VW_CGH_NUCLEAR_F_Export_22-07-2024.csv` |
| [Dimension tables (index)](singcloud-dimension-tables-index.md)<br>*43 objects* | `VW_ADMIT_TYPE_D`, `VW_CASE_TYPE_D`, `VW_CIIMS_ECHO_FINDINGS_D`, `VW_CIIMS_ECHO_MEASUREMENTS_D`, `VW_CIIMS_RHYTHM_D`, `VW_CIIMS_WALLMOTION_D`, `VW_CVIS_NUCLEAR_D`, `VW_DIAGNOSIS_CODE_D`, `VW_DIAGNOSIS_STATUS_D`, `VW_DIAGNOSIS_TYPE_D`, `VW_DISCHARGE_DISPOSITION_D`, `VW_DISPENSED_MEDICATION_CROSS_MAPS_MV2_D`, `VW_DRG_D`, `VW_DRUG_D`, `VW_INSTITUTION_D`, `VW_INV_RESULT_STATUS_D`, `VW_INV_SUBTYPE_D`, `VW_INV_TYPE_D`, `VW_ITEM_D`, `VW_ITEM_STATUS_D`, `VW_MOV_CAT_D`, `VW_MOV_TYPE_D`, `VW_NUHCS_ECHO_D`, `VW_NUHCS_NUC_D`, `VW_NUHCS_PCI_D`, `VW_NUHCS_PROC_D`, `VW_NUH_CABG_09_21_D`, `VW_PATIENT_DEATH_IND_D`, `VW_PATIENT_DOB_D`, `VW_PATIENT_GENDER_D`, `VW_PATIENT_LANGUAGE_D`, `VW_PATIENT_MARITAL_STATUS_D`, `VW_PATIENT_NATIONALITY_D`, `VW_PATIENT_OCCUPATION_D`, `VW_PATIENT_RACE_D`, `VW_PATIENT_RELIGION_D`, `VW_PATIENT_RESIDENTIAL_STATUS_D`, `VW_PATIENT_TYPE_D`, `VW_REFERRAL_FACILITY_D`, `VW_SERVICE_CODE_D`, `VW_SERVICE_SPECIALITY_D`, `VW_SINGCLOUD_DIAGNOSIS_CODE_D`, `VW_SKH_CVIS_MIBI_D`<br>*Dated `22-07-2024`, except `VW_DRUG_D`, `VW_PATIENT_DEATH_IND_D`, `VW_PATIENT_GENDER_D`, `VW_PATIENT_LANGUAGE_D`, `VW_PATIENT_NATIONALITY_D`, `VW_PATIENT_OCCUPATION_D`, `VW_PATIENT_RACE_D`, `VW_PATIENT_RELIGION_D`, `VW_PATIENT_RESIDENTIAL_STATUS_D` = `06-08-2024`; `VW_PATIENT_MARITAL_STATUS_D` = `11-09-2024`* |
| [Dispensed Medication](singcloud-dispensed-medication.md)<br>*3 objects* | `VW_DISPENSED_MEDICATION_F_Export_22-07-2024_PART_1.csv`<br>`VW_DISPENSED_MEDICATION_F_Export_24-07-2024_PART2.csv`<br>`VW_DISPENSED_MEDICATION_F_Export_24-07-2024_PART3.csv` |
| [Dispensed Medication Item](singcloud-dispensed-medication-item.md)<br>*27 objects (+1 unresolved)* | `VW_DISPENSED_MEDICATION_ITEM_F_Export_24-07-2024_P{n}.csv`<br>n = 2–9, 11–29<br>*P1 and P10 absent from the report* |
| [Event Diagnosis](singcloud-event-diagnosis.md)<br>*6 objects* | `VW_EVENT_DIAGNOSIS_F_Export_31-07-2024_P{n}.csv` — n = 1–6 |
| [IP Billing](singcloud-ip-billing.md)<br>*37 objects* | `VW_IP_BILLING_F_Export_05-08-2024_P{n}.csv` — n = 1–18<br>`VW_IP_BILLING_F_Export_06-08-2024_P{n}.csv` — n = 19–37<br>*Complete, no gaps. P9 failed to profile* |
| [Laboratory](singcloud-laboratory.md)<br>*11 objects* | `VW_LABORATORY_F_Export_26-07-2024_P{n}.csv`<br>n = 1, 2, 4, 7, 10, 11, 12, 18, 19, 21, 22<br>*Non-contiguous — P3, P5, P6, P8, P9, P13–P17, P20 absent* |
| [Laboratory Dim](singcloud-laboratory-dim.md)<br>*1 object* | `VW_LABORATORY_DIM_F_Export_22-07-2024.csv` |
| [Laboratory Item FIL](singcloud-laboratory-item-fil.md)<br>*2 objects* | `VW_LABORATORY_ITEM_FIL_F_Export_28-07-2024_P1.csv`<br>`VW_LABORATORY_ITEM_FIL_F_Export_28-07-2024_P2.csv` |
| [MED Billing](singcloud-med-billing.md)<br>*17 objects* | `VW_MED_BILLING_F_Export_19-08-2024_P{n}.csv` — n = 1, 5, 6, 8, 10, 11, 14, 15, 16, 19<br>`VW_MED_BILLING_F_Export_20-08-2024_P{n}.csv` — n = 21, 22, 23, 24, 26, 30, 33<br>*Numbering runs to at least P33; 16 numbers in range absent* |
| [MOH OB Operation](singcloud-moh-ob-operation.md)<br>*3 objects* | `VW_MOH_OB_OPERATION_F_Export_31-07-2024_P{1,2,3}.csv` |
| [MOH OB Procedure](singcloud-moh-ob-procedure.md)<br>*3 objects* | `VW_MOH_OB_PROCEDURE_F_Export_31-07-2024_P{1,2,3}.csv` |
| [MOH OB WO SHI](singcloud-moh-ob-wo-shi.md)<br>*1 object* | `VW_MOH_OB_WO_SHI_F_Export_31-07-2024.csv` |
| [NUHS HFSI](singcloud-nuhs-hfsi.md)<br>*3 objects — three copies of one dataset* | `VW_NUHS_HFSI_F_Export_22-07-2024.csv` — prefix `PriorityTables-B1/`<br>`VW_NUHS_HFSI_F_Export_30-10-2024.csv` — prefix `FreeText_FTA/`<br>`VW_NUHS_HFSI_F_Export_30-10-2024.csv` — prefix `Updated_HFSI/`<br>**Do not sum across these** — the two October copies differ by 4 rows and 52 MB |
| [OP Billing](singcloud-op-billing.md)<br>*28 objects* | `VW_OP_BILLING_F_Export_14-08-2024_P{n}.csv` — n = 1–18, 20–29<br>*P19 absent* |
| [Radiology](singcloud-radiology.md)<br>*1 object* | `VW_RADIOLOGY_F_Export_06-08-2024.csv` |
| [SCDB](singcloud-scdb.md)<br>*19 objects* | `VW_SCDB_EPS_F`, `VW_SCDB_EPS_DIM_F`, `VW_SCDB_HF_F` **(×2 — under `PriorityTables-B1/` and `FreeText_FTA/`)**, `VW_SCDB_HF_DIM_F`, `VW_SCDB_ICD_F`, `VW_SCDB_ICD_DIM_F`, `VW_SCDB_INTERVENTION_F`, `VW_SCDB_INTERVENTION_DIM_F`, `VW_SCDB_INTERVENTION_BEFORE_T1_F`, `VW_SCDB_INTERVENTION_BEFORE_T2_F`, `VW_SCDB_PPM_F`, `VW_SCDB_PPM_DIM_F`, `VW_SCDB_SURGERY_F`, `VW_SCDB_SURGERY_DIM_F`, `VW_SCDB_SURGERY_BEFORE_F`, `VW_SCDB_ZLMAUDITEPS_F`, `VW_SCDB_ZLMAUDITEPS_DIM_F`, `VW_SCDB_ZLMAUDITICD_F`<br>*All `_Export_22-07-2024.csv`* |

---

## Two names that are not datasets

The OCR-reconstructed index in `source_material/imported/` lists two families that **do not
exist**. Both are character-level misreadings of IP Billing partition names, and both carry
figures identical to the real partitions:

| Appears in the index as | Actually is | Identical figures |
|---|---|---|
| `VW_TP_BILLING_F_Export_05-08-2024_P5.csv`, prefix `NonFreeText_Flles` | `VW_IP_BILLING_F_..._P5.csv` | 1,023.58 MB, 3,157,211 rows, 37 cols |
| `VW_LIP_BILLING_F_Export_05-08-2024_P8.csv` | `VW_IP_BILLING_F_..._P8.csv` | 1,465.94 MB, 4,530,134 rows, 37 cols |

If you find either name in `profiler_report_full.txt`, `column_summary.csv`,
`dataset_summary.csv` or `datasets/full_inventory.md`, it is one of these. Do not create a
page for it.

## Unresolved

Two rows in the OCR index have unreadable filenames but valid figures. Both match a documented
family by column count — 37 columns occurs only in IP Billing, 30 only in Dispensed Medication
Item — so **neither is an undocumented dataset**, but the exact partition is not established.

| Size | Rows | Cols | Missing % | Belongs to | Likely |
|---:|---:|---:|---:|---|---|
| 1,943.75 MB | 6,036,342 | 37 | 19.00 | IP Billing | Probably P4 — the only partition confirmed present with no figures in the index, and 19.00% sits inside the family's 18.95–19.02% band. **Unconfirmed** |
| 1,406.55 MB | 4,297,867 | 30 | 32.44 | Dispensed Medication Item | Not matched to a partition number |

Also outstanding: `VW_IP_BILLING_F_Export_05-08-2024_P9.csv` exists but **failed to profile** —
the report prints a `ResponseStreamingError` where its figures should be. It contributes
nothing to any total and its schema is unverified.

---

## How this list was established

The OCR reconstructions in `source_material/imported/` cannot be trusted for object names —
they mangle filenames and invent datasets. This list was built from the screenshots instead:

1. Every object block in the profiler report opens with a dashed separator line. Those were
   detected by pixel across all 28 sections — a row with dark pixels beyond x=1000, which text
   never reaches.
2. The two header lines below each separator were cropped and composited into six sheets, and
   every object path read from them.
3. The result was reconciled against the index, which surfaced the two phantom families and
   the four IP Billing partitions the index had missed.

Re-run that process after any new profiler run. Figures per object come from the same
screenshots; see each page's *Sources* appendix for exactly which sections were read.

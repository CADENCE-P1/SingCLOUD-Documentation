# Imported: column manifests for three datasets

> **Working notes, not documentation.** Carried over verbatim from an analysis project that
> used SingCLOUD. This file holds the **most complete column manifests currently available**
> for Laboratory Items, SingCLOUD Event Diagnosis and MediClaims Episodes, which is why it
> is kept in full.
>
> Reviewed versions with provenance classification (Raw / Standardised / Derived), linkage
> notes and known biases are in `datasets/`:
> [Laboratory Items](../../datasets/singcloud-laboratory-items.md) ·
> [Event Diagnosis](../../datasets/singcloud-event-diagnosis.md) ·
> [MediClaims Episodes](../../datasets/mediclaims-episodes.md)
>
> Note the export date in the Laboratory Items base name (`28-07-2024`). Partitions P5–P22
> carry dates of 29-07-2024 and 30-07-2024; Event Diagnosis was exported 31-07-2024.
>
> Source: `HF_Diagnosis_Data_Context.md`.

---


# Data Catalog Documentation

This document outlines the schema, structure, and key attributes of the three primary datasets within the catalog: Laboratory Items, SingCLOUD Event Diagnosis, and Mediclaims Episodes.

## 1. Laboratory Items Dataset
This dataset contains detailed patient laboratory test results and associated metadata.

* **Dataset Base Name:** `VW_LABORATORY_ITEM_FIL_F_Export_28-07-2024`
* **Aliases / Partitions:** `VW_LABORATORY_ITEM_FIL_F_Export_28-07-2024_P1` through `VW_LABORATORY_ITEM_FIL_F_Export_28-07-2024_P22`
* **Total Parts:** 22
* **Format:** CSV
* **Delimiter:** `,`

### Key Identified Columns
* **Patient Identifier:** `PATIENT_ID_EXTN_X`
* **Lab Test Name:** `ITEM_NAME_ORI_TXT`
* **Test Value:** `ITEM_NUMERIC_VALUE`

### Full Column Manifest
| Column Name | Description / Notes |
| :--- | :--- |
| `DATA_SOURCE` | Source system of the data record |
| `BATTERY_ID_ROOT` | Root identifier for the lab battery |
| `FACILITY_EXTN` | External facility identifier |
| **`PATIENT_ID_EXTN_X`** | **Primary Patient ID** |
| `DISPLAY_DATE_X` | Lab display date (Format X) |
| `DISPLAY_DATE_Z` | Lab display date (Format Z) |
| `ITEM_SEQ_NO` | Sequence number of the lab item |
| `ITEM_NAME_ETS_ID` | Standardized ETS identifier for the item name |
| **`ITEM_NAME_ORI_TXT`** | **Original text of the lab test name** |
| **`ITEM_NUMERIC_VALUE`** | **Numeric result/value of the test** |
| `ITEM_NUMERIC_VALUE_UOM` | Unit of measure for the numeric value |
| `ITEM_REFERENCE_RANGE` | Normal reference range for the test |
| `ITEM_ABNORMAL_FLAG_ETS_ID` | Standardized ETS flag for abnormal results |
| `ITEM_ABNORMAL_FLAG_ORI_TXT` | Original text flag for abnormal results |
| `ITEM_STATUS_ETS_ID` | ETS identifier for the item status |
| `BATTERY_ID_EXTN` | External identifier for the lab battery |

---

## 2. SingCLOUD Event Diagnosis Dataset
This dataset captures patient diagnosis events, admission details, and discharge timings.

* **Dataset Base Name:** `SingCLOUD_Event_Diagnosis`
* **Aliases / Partitions:** `Event_Diagnosis_P1` through `Event_Diagnosis_P8`
* **Total Parts:** 8
* **Format:** CSV
* **Delimiter:** `,`

### Key Identified Columns
* **Patient Identifier:** `PATIENT_ID_EXTN_X`
* **Diagnosis Descriptions:** `DIAGNOSIS_NAME_TXT` and `DIAGNOSIS_NAME_TXT_STD`
* **Admission Date:** `VISIT_ADMIN_DATE_Z` *(Format: `YYYY-MM-DD HH:MM:SS`)*
* **Discharge Date:** `DISCHARGE_DATE_Z` *(Format: `YYYY-MM-DD HH:MM:SS`)*

### Full Column Manifest
| Column Name | Description / Notes |
| :--- | :--- |
| `DATA_SOURCE` | Source system of the data record |
| `EVN_ID_EXTN` | External Event ID |
| **`PATIENT_ID_EXTN_X`** | **Primary Patient ID** |
| `VISIT_ADMIN_DATE_X` | Admission date (Format X) |
| **`VISIT_ADMIN_DATE_Z`** | **Admission date (Standardized: YYYY-MM-DD HH:MM:SS)** |
| `DISCHARGE_DATE_X` | Discharge date (Format X) |
| **`DISCHARGE_DATE_Z`** | **Discharge date (Standardized: YYYY-MM-DD HH:MM:SS)** |
| `PATIENT_TYPE_ETS_ID` | Patient type identifier |
| `EVN_FACILITY_EXTN` | Event facility identifier |
| `EVN_SERVICE_SPECIALTY_ETS_ID` | Event service specialty identifier |
| `MOV_TYPE_ETS_ID` | Movement type identifier |
| `MOV_CAT_ETS_ID` | Movement category identifier |
| `DISCHARGE_OUTCOME` | Outcome of the discharge |
| `DISCHARGE_DISPOSITION_ETS_ID` | Discharge disposition identifier |
| `DOC_TYPE_CODE` | Document type code |
| `DOC_TYPE_ETS_ID` | Document type identifier |
| `DIAG_SERVICE_SPECIALTY_ETS_ID` | Diagnosis service specialty identifier |
| `DIAGNOSIS_NAME_ETS_ID` | Standardized diagnosis name identifier |
| `DIAGNOSIS_TYPE_ETS_ID` | Standardized diagnosis type identifier |
| `DIAGNOSIS_TYPE_TXT` | Text description of the diagnosis type |
| `DIAG_STATUS_ETS_ID` | Diagnosis status identifier |
| `DIAG_ONSET_DATE_X` | Diagnosis onset date (Format X) |
| `DIAG_ONSET_DATE_Z` | Diagnosis onset date (Format Z) |
| `DIAG_OCCURENCE_DATE_X` | Diagnosis occurrence date (Format X) |
| `DIAG_OCCURENCE_DATE_Z` | Diagnosis occurrence date (Format Z) |
| `EVN_SERVICE_SPECIALTY_TXT` | Event service specialty text |
| `DIAG_SERVICE_SPECIALTY_TXT` | Diagnosis service specialty text |
| `EVN_SERVICE_SPECIALTY_TXT_STD` | Standardized event service specialty text |
| `DIAG_SERVICE_SPECIALTY_TXT_STD` | Standardized diagnosis service specialty text |
| `ICD_CODE_PMH_STD` | Standardized PMH ICD code |
| `ICD_CODE_OUTCOME_STD` | Standardized outcome ICD code |
| **`DIAGNOSIS_NAME_TXT`** | **Raw text of the diagnosis** |
| **`DIAGNOSIS_NAME_TXT_STD`** | **Standardized text of the diagnosis** |

---

## 3. Mediclaims Episodes Dataset
This dataset tracks episodic medical claims, billing, and length of stay by year.

* **Dataset Base Name:** `mediclaims_epi`
* **Aliases / Partitions:** `mediclaims_epi_2017` through `mediclaims_epi_2023`
* **Total Parts:** 7 (One dedicated file per year)
* **Format:** CSV
* **Delimiter:** `,`

### Key Identified Columns
* **Patient Identifier:** `uin`
* **Admission Date:** `admission_date`
* **Discharge Date:** `discharge_date`
* **Diagnosis Description:** `finaldiagdesc`

### Full Column Manifest
| Column Name | Description / Notes |
| :--- | :--- |
| **`uin`** | **Unique Identification Number (Patient ID)** |
| `pataccno` | Patient account number |
| `resident_type` | Patient residency status |
| `case_type` | Type of medical case |
| `sector` | Healthcare sector classification |
| `hospital` | Treating hospital/institution |
| **`admission_date`** | **Date of admission** |
| **`discharge_date`** | **Date of discharge** |
| `los` | Total length of stay (days) |
| `icu_los` | ICU length of stay (days) |
| `finaldiagcode` | Final diagnosis code |
| **`finaldiagdesc`** | **Final diagnosis description** |
| `tot_bill` | Total bill amount |
| `tot_bill_bmt` | Total bill amount (BMT specific) |
| `facil_type` | Facility type |

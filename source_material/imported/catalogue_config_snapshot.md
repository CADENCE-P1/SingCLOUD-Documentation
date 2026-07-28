# Imported: catalogue alias snapshot

> **Working notes, not documentation.** The exact alias strings used to load SingCLOUD
> datasets, taken from the configuration of an analysis project that ran against the
> platform in 2024.
>
> Value: these are **verified-working strings**, not a specification. They loaded real data.
> Aliases with unusual formatting — a space, an inconsistent capital, a "truncated" suffix —
> are reproduced exactly, because that is what makes them useful.
>
> Caveat: alias strings are a property of the catalogue configuration, which is
> environment-specific and changes. Confirm against `cat.list_datasets()` in your own
> environment before relying on any of them. An alias present in a config file but absent
> from the live catalogue fails at load time, and that is a routine occurrence.
>
> Sources: analysis pipeline `config.yaml` and `catalog.yaml`. Bucket names and object paths
> redacted.

---

## Access pattern

Datasets are loaded by alias through a `DataCatalog` wrapper that resolves the alias to an
object-storage path via a YAML catalogue file:

```python
from catalog import DataCatalog

cat = DataCatalog("catalog.yaml")
df = cat.load("mediclaims_diag_2020")

# List what the environment actually exposes — do this first
print(cat.list_datasets())
```

Supported formats: CSV, XLSX, Parquet, JSONL. Access uses the environment's IAM role
(`s3fs.S3FileSystem(anon=False)`); no explicit credentials.

Catalogue entries carry: `path`, `type`, `delimiter` (CSV), `sheet_name` (XLSX),
`description`, and optionally `columns` (friendly → raw mapping), `required_columns`,
`date_column`, `date_format`, `date_min`, `date_max`, `n_rows`, `column_list`.

> The optional fields are worth noting: the catalogue format **already supports** row
> counts, date ranges and full column lists per dataset. Populating them would put a large
> part of this repo's §1 and §3 content directly into the platform's own catalogue. Most
> real entries leave them empty.

---

## Alias inventory

### MediClaims

| Pattern | Range |
|---|---|
| `mediclaims_diag_{year}` | 2015–2023 |
| `mediclaims_epi_{year}` | 2017–2023 |

### COVID-19 confirmed case registry

```
ConfirmedCaseHeadersForAgenciesCNo0to100000
ConfirmedCaseHeadersForAgenciesCNo100000to200000
ConfirmedCaseHeadersForAgenciesCNo200000to300000
ConfirmedCaseHeadersForAgenciesCNo300000to400000
ConfirmedCaseHeadersForAgenciesCNo400000to500000
ConfirmedCaseHeadersForAgencies1Dec2022
ConfirmedCaseHeadersForAgencies1Jan2023
```

### COVID-19 severity, vaccination, serology

| Alias | Observed rows | Content |
|---|---:|---|
| `COVIDFACILLOS` | ~2,349,112 | LOS, ICU, deceased, race, vaccination |
| `NIRListtruncated` | ~6,174,098 | National immunisation registry |
| `COVID Reinfections` | ~128,101 | Reinfection records — **note the space in the alias** |
| `Serology_Tests_COVID` | ~1,067,600 | Serology results |
| `FacilityUtilizationLOSSubsequentRI` | ~2,319 | Facility use, reinfected patients |

### SingCLOUD

| Alias / pattern | Parts |
|---|---|
| `SingCLOUD_gender` | 1 |
| `SingCLOUD_DOB` | 1 |
| `SingCLOUD_medication_items{n}` | 29 (n = 1…29) |
| `Event_Diagnosis_P{n}` | 8 (n = 1…8) |
| `VW_LABORATORY_ITEM_FIL_F_Export_{date}_P{n}` | 22 (n = 1…22; dates 28/29/30-07-2024) |

### Other

| Alias | Notes |
|---|---|
| `death_registry` | 1 file |
| `casemix_data_{fy}_df` | Per financial year; **pipe-delimited** |

---

## Storage layout

Objects sit under a `common-data/SingCLoud/` prefix in an S3 bucket, with `FreeText_FTA/`
and `NonFreeText_Files/` sub-prefixes — the split separates datasets containing free-text
clinical fields from those that do not, which is likely to be governance-relevant and
should be confirmed with the data owner.

Note the inconsistent capitalisation of the prefix itself (`SingCLoud` in some paths,
`SingCloud` in others). Object-storage prefixes are case-sensitive, so this is a real
source of "file not found" errors rather than a cosmetic issue.

Concrete bucket and prefix strings are omitted here — see
[docs/02_access_and_governance.md](../../docs/02_access_and_governance.md).

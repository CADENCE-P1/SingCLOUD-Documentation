# Access and governance

> ⚪ **Stub — this page is the largest known gap in the catalogue.**
>
> The rationale for this repo is explicit that stakeholders need "clear information on the
> owner of the data, access restrictions and approval requirements" to judge whether a
> dataset can be used *within their project timeline*. That information is not yet
> documented. Everything below is either structural (how access works technically) or a
> question to be answered by the platform and data owners.
>
> Until §2 and §3 are filled in, this catalogue supports the *suitability* and
> *feasibility* decisions but not the *governance* one.

---

## 1. Access model (technical)

Analysis is performed inside a managed analysis environment (SageMaker-based virtual
desktop). Data is not downloaded to analyst machines; it is read from object storage into
the environment.

- Datasets are stored as files (predominantly CSV) in an S3 bucket, organised under a
  `common-data/SingCLoud/` prefix, with `FreeText_FTA/` and `NonFreeText_Files/`
  sub-prefixes.
- Access is granted via the environment's IAM role rather than per-user credentials — code
  reads with `s3fs.S3FileSystem(anon=False)` or `boto3` and no explicit keys.
- Large datasets are **partitioned across many files** (see each dataset page). There is no
  single-file view; consumers must iterate over parts.

Concrete bucket and prefix names are deliberately not published in this repo. They are
available in the platform configuration to anyone who already has environment access, and
publishing them here would add no capability for legitimate users while exposing
infrastructure detail. See [`tools/README.md`](../tools/README.md).

### What this means for a stakeholder

| Implication | Detail |
|---|---|
| No data egress | Analysis happens in-environment; plan for outputs, not extracts |
| Compute-bound, not download-bound | Multi-GB partitioned CSVs must be streamed in chunks |
| Environment access is a prerequisite | Separate from, and additional to, dataset-level approval |

## 2. Ownership — to be documented

For each dataset the catalogue needs, and does not yet have:

- [ ] **Data owner** — the accountable agency or department
- [ ] **Data steward / contact point** — who answers questions
- [ ] Whether ownership differs by partition or by year for datasets assembled from
      multiple sources

Individual dataset pages carry an owner field; all are currently
*"Unknown — to confirm with data owner"*.

## 3. Approvals and restrictions — to be documented

- [ ] Baseline approval required for any SingCLOUD access
- [ ] Which datasets require **additional** dataset-specific approval beyond baseline
- [ ] Ethics / IRB requirements, and which body
- [ ] Whether a separate data-use agreement is required per study
- [ ] **Typical elapsed lead time** from request to access — the single number stakeholders
      most need for project planning
- [ ] Renewal, expiry and retention conditions

## 4. Output and publication conditions — to be documented

- [ ] Small-cell suppression threshold for published counts
- [ ] Output review process before results leave the environment
- [ ] Publication or acknowledgement requirements
- [ ] Restrictions on onward sharing of derived datasets

## 5. Standing rules for this repository

Regardless of what the sections above turn out to say:

- **No patient-level data** in this repository, in any form, including screenshots that
  show real record values.
- **No real identifiers** in examples. Use synthetic values.
- Screenshots contributed to `source_material/screenshots/` must show schema, column names
  and aggregate summaries only. Redact any visible record content before committing —
  a screenshot cannot be un-published once pushed.
- **No study results.** This catalogue documents datasets, not findings.

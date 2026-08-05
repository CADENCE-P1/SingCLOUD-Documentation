# SingCLOUD Documentation

A standardised data catalogue and documentation set for the datasets available through
**SingCLOUD**, written for stakeholders who need to decide *whether SingCLOUD is suitable
for their study* before committing to an access request.

**📖 Browse the catalogue as a website:**
<https://cadence-p1.github.io/SingCLOUD-Documentation/>

---

## The documentation site

The catalogue is published with [Astro Starlight](https://starlight.astro.build/) from
the [site/](site/) directory. The markdown in `docs/` and `datasets/` remains the single
source of truth — a sync step copies it into the site at build time, so **editing the
markdown here is all that is needed to update the site**. Pushing to `main` rebuilds and
deploys automatically via GitHub Actions.

To preview locally:

```sh
cd site
npm install
npm run dev     # http://localhost:4321/SingCLOUD-Documentation/
```

---

## Why this repo exists

Before deciding to use SingCLOUD, stakeholders must evaluate whether the datasets are
suitable for their needs. Doing that requires answers to four separate questions, and
today those answers are scattered across tribal knowledge, ad-hoc scripts and
screenshots.

| Question | What a stakeholder needs to know | Where it lives here |
|---|---|---|
| **What is in it?** | Type of information (clinical, lab, billing), the variables, the population represented, the period covered, and when each variable started being collected | `datasets/*.md` § 1 Content & Scope |
| **Where did it come from?** | How the data was collected and processed; whether a variable preserves the original source data or is an interpreted/derived value | `datasets/*.md` § 2 Provenance & Processing |
| **Can I actually use it?** | Linkage keys and identifiers, coding standards, sample size, missingness, known biases | `datasets/*.md` § 3 Feasibility & Quality, plus [docs/03_linkage_guide.md](docs/03_linkage_guide.md) |
| **Am I allowed to use it?** | Data owner, access restrictions, approval requirements, realistic lead time | `datasets/*.md` § 4 Ownership & Governance, plus [docs/02_access_and_governance.md](docs/02_access_and_governance.md) |

The full rationale is in [docs/00_rationale.md](docs/00_rationale.md).

The distinction in the second row matters more than it looks. A researcher building an AI
model on ECG waveforms needs the raw waveform, not a cardiologist's interpretation of it —
two fields that may sit next to each other in the same table and look equally usable from a
column list alone. Every dataset page therefore labels its fields **Raw**, **Standardised**
or **Derived**.

---

## Repo layout

```
docs/                     The documentation standard and cross-cutting guides
  00_rationale.md         Why standardised dataset documentation is needed
  01_documentation_standard.md   The required fields for every dataset page
  02_access_and_governance.md    Ownership, approvals, access model
  03_linkage_guide.md            Identifiers, coding standards, linkage pitfalls

catalog_pages/            The data catalog — one page per dataset family
  index.md                Page index: which catalog page covers which object
  template_intro.md       How to read a catalog page; the two-pass process
  template.md             Copy this to add a new catalog page
  singcloud-<family>.md   17 pages covering every object the profiler found

datasets/                 Analyst notes from the 2024-07 extract (supplement
  index.md                the catalog pages; to be folded in during pass 2)
  full_inventory.md       Superseded OCR inventory, kept for traceability
  singcloud-<dataset>.md

source_material/          Raw inputs the documentation is built from
  screenshots/            Dataset-summary screenshots (drop them here)
  imported/               Working notes carried over from analysis projects

tools/
  s3_data_catalog.py      Profiler that generates dataset/column summaries from S3

site/                     The Astro Starlight site that publishes all of the above
```

---

## Documentation status

The catalogue is being assembled incrementally. Every dataset page carries a status badge
so readers can tell verified documentation from a working draft:

| Status | Meaning |
|---|---|
| ✅ **Verified** | Reviewed against the profiler output *and* confirmed with the data owner |
| 🟡 **Draft** | Written from profiler output and/or analyst working knowledge; not owner-confirmed |
| ⚪ **Stub** | Dataset known to exist; contents not yet documented |

**Every object the profiler found belongs to a catalog page** — 17 pages covering 76
dataset families across 206 objects (profiler run 2026-07-23). See
[catalog_pages/index.md](catalog_pages/index.md) for the object-to-page mapping. Most
pages are currently ⚪ base pages: figures are sound, meaning is still being filled in.
The pages in [datasets/](datasets/index.md) are analyst notes from a 2024-07 extract
that supplement the corresponding catalog pages.

The catalogue's scope is the **SingCLOUD platform**. Notes on non-SingCLOUD datasets
(MediClaims, COVID-19 registries, Death Registry, NIR, serology) were removed when the
scope was narrowed; they remain in the git history.

---

## Provenance of the current content

The initial dataset pages were assembled from working documentation produced during an
analysis project that used SingCLOUD (a COVID-19 / ischaemic heart disease cohort study).
That means:

- Column lists and formats reflect **what an analyst actually observed on the platform**,
  which is a genuine strength — these are field-verified quirks, not a paper spec.
- They reflect the **extract those analysts received**, which may not be the full dataset,
  and reflect the platform as of the extract dates noted on each page.
- Row counts and date ranges are as observed in those extracts. Treat them as
  order-of-magnitude, not as an authoritative census.
- **No study results, cohort definitions or patient-level figures from that project are
  reproduced here.** Only dataset-descriptive metadata was carried over.

Anything in `source_material/imported/` is a working note, not documentation. It is kept
for traceability and should be superseded by proper `datasets/*.md` pages over time.

---

## Contributing

To add or update a dataset:

1. Copy [catalog_pages/template.md](catalog_pages/template.md) to
   `catalog_pages/singcloud-<family>.md`. Read
   [catalog_pages/template_intro.md](catalog_pages/template_intro.md) first.
2. Fill in the sections. Write "Unknown — to confirm with data owner" rather than
   leaving a section blank; a visible gap is useful, a silent one is not.
3. Add a row to [catalog_pages/index.md](catalog_pages/index.md).
4. Open a pull request.

Do not commit patient-level data, extracts, or any file containing real identifiers. See
[.gitignore](.gitignore).

# Data catalog pages

Each dataset in SingCLOUD has its own data catalog page, built to a common template so that
any two datasets can be compared field for field. A page answers four questions in order —
what is in it, where did it come from, can I actually use it, am I allowed to use it — through
the following sections.

**Objects included** — names every `.csv` the page was built from. The first thing to check:
does this page describe the files you are holding?

**Dataset Overview** — tells us what the dataset is, who is in it (and who is *not*), and
what one row represents. Also the practical facts needed to load it: alias, partitions,
format, extract date.

**Key Variables** — tells us which variables the dataset holds, what each one means, and
whether it is a raw source value, a standardised one, or somebody's interpretation.

**Time Coverage** — tells us which time range is *usable*: the date range covered, the format
each date is stored in, gaps within the range, and when each variable actually started being
collected.

**Dataset Information** — tells us the size, rows, columns and sample size. Machine-generated
from the profiler.

**Provenance & Processing** — tells us the origin of the data, how it was collected, and
which variables have been processed or transformed along the way.

**Data Quality** — tells us missingness, overlap with other datasets (linkage keys and
pitfalls), known biases, and other limitations.

**Ownership & Governance** — tells us who owns the data, who to ask about it, what approvals
are needed, and how long access typically takes. It ends with the open questions for the data
owner, written so the list can be sent as-is.

The page then carries **Appendices A–C** — full column profile, change log, and the sources
every figure came from.

---

## Pages are built in two passes

A page is useful after the first pass and is not expected to be complete.

**Pass 1 — the base page.** Everything the profiler establishes: the objects, their sizes,
row and column counts, and every column with its type and missingness. Two fields are filled
by catalogue convention rather than evidence — **Category**, read from the dataset name, and
**Primary identifier**, which is always the patient ID column. Every other field is present
and marked unknown.

**Pass 2 — the filled page.** Column descriptions, whether each column is raw or interpreted,
value domains, date ranges, linkage keys, bias, and the governance answers from the data
owner.

**The Status field in the header tells you which stage a page has reached**, and it is the
only completeness signal on the page:

| Status | Meaning | How much to trust it |
|---|---|---|
| ⚪ **Stub** | Pass 1 done — what the profiler establishes, and little else | The figures are sound; nearly everything about meaning is still unanswered |
| 🟡 **Draft** | Pass 2 under way — some fields filled from analysis or from the data owner | Read the individual fields; unknowns are still expected and are marked as such |
| ✅ **Verified** | Every field filled and confirmed with the data owner | Trust it, and check *Last reviewed* for how recently |

**An unknown is a real entry, not a blank.** It tells a reader what to ask and whom, which is
worth more than a plausible sentence someone inferred from a column name — the inference is
what a later reader will act on. Nothing on a base page is guessed.

---

A worked example of a pass-1 page is
[`singcloud-event-diagnosis.md`](singcloud-event-diagnosis.md).
Field-by-field guidance is in Appendix D of [`template.md`](template.md) itself. The reasoning
behind the structure is in [`docs/00_rationale.md`](../docs/00_rationale.md).

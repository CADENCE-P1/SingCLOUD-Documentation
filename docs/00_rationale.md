# Why standardised dataset documentation is needed

> This is the problem statement that motivates the catalogue. Each paragraph maps to a
> required section of the [documentation standard](01_documentation_standard.md).

---

## 1. Stakeholders cannot assess suitability without knowing the contents

Before deciding to use SingCLOUD, stakeholders must evaluate whether the datasets are
suitable for their needs. To do so, they would need to understand the contents of each
dataset, such as the type of information (e.g. clinical data, lab test data, billing data),
the variables in the dataset, and the population it represents.

They also need to determine whether the period covered by the dataset is suitable for their
study. For example, longitudinal studies will require historical data, while other studies
will only require more recent data. Furthermore, earlier records may not contain certain
variables, as data collection tools may not have been available yet in the past.

Details of how the data is collected and processed is also important, as some variables may
not preserve the original source data, and instead represent information that had undergone
interpretation or processing. For example, a researcher that wants to develop an AI model
would want to use raw data instead of an interpreted diagnosis of an ECG waveform.

Without this information, stakeholders may select datasets that are unsuitable for their
study, or overlook datasets that can better meet their research objectives.

**→ Documentation standard §1 (Content & Scope) and §2 (Provenance & Processing).**

## 2. Stakeholders cannot assess feasibility without knowing linkage and quality

Stakeholders must also consider the feasibility of using the datasets, as their analysis
may require the linkage of multiple datasets. However, differences in data collection
methods, coding standards or identifiers across datasets may prevent them from being linked
easily. For example, two hospitals may record the same diagnosis using different coding
systems.

The quality of the dataset — sample size, missingness, biasness — is another important
consideration, as it would affect the statistical power, validity and reliability of the
findings. Providing this information will allow stakeholders to assess whether the
available data meets their requirements.

**→ Documentation standard §3 (Feasibility & Quality), and the
[linkage guide](03_linkage_guide.md).**

## 3. Stakeholders cannot plan without knowing ownership and governance

Finally, stakeholders need to understand the ownership and governance of the datasets.
Providing clear information on the owner of the data, access restrictions and approval
requirements will allow stakeholders to determine if they will be able to use the dataset
within their project timeline, and used in compliance with governance requirements.

**→ Documentation standard §4 (Ownership & Governance), and the
[access and governance guide](02_access_and_governance.md).**

---

## Consequence

These considerations highlight the importance of standardised documentation that will allow
stakeholders to efficiently **evaluate, compare and select** datasets for their research
purposes.

The operative word is *standardised*. Documentation that exists but differs in structure
from dataset to dataset does not support comparison — a stakeholder cannot tell whether an
absent field means "not applicable", "not collected", or "nobody wrote it down". That is
why every page in `datasets/` uses the same four sections in the same order, and why
unknowns are recorded explicitly rather than omitted.

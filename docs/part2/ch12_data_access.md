# Getting Your Data: Access, Sources, and Compliance

:::{admonition} What You Will Learn
:class: tip

- How to evaluate whether a dataset is appropriate for your research question
- What compliance requirements apply before you access or share data
- When public datasets like Kaggle require — and do not require — IRB review
- Where to find data through University of Michigan resources
- Where to find publicly available datasets for prototyping and method development
:::

---

## The Pilot Data Problem

Imagine you are a biomedical researcher with a compelling hypothesis. You have done the background work, you have a clear question, and you want to apply for a small NIH grant — an R03 or R21 — to collect the pilot data that would let you build toward a larger R01. There is just one problem: to be competitive, your application needs preliminary data. And to get preliminary data, you need to run a study. And to run a study, you need funding.

This is one of the most frustrating loops in academic research, and it is more common than the grant literature tends to acknowledge. Experienced researchers navigate it by being creative about data sources: using existing cohorts, collaborating with groups who have relevant data, or — increasingly — turning to public repositories to find datasets that are close enough to their target population and measurement structure to generate credible feasibility results.

This is one of the most legitimate and underappreciated uses of public research data. A well-chosen publicly available dataset can let you estimate effect sizes, test analytical pipelines, identify methodological challenges, and demonstrate that your proposed approach is tractable — all before you have collected a single observation. That kind of preliminary work can be the difference between a fundable and an unfundable application.

This chapter is a practical guide to finding that data, understanding what you can actually do with it, and avoiding the compliance mistakes that researchers most commonly make in the process.

---

## Start with What You Need, Not What Is Available

The most common mistake in data acquisition is starting from availability rather than need. You find a large, well-documented dataset, and the temptation is to ask what question you could answer with it. That logic can work for exploratory or pilot work, but for a research project with a defined question, the sequence should run the other way: start from what your question requires, then look for data that fits.

A few things worth pinning down before you begin searching:

**Unit of analysis.** Are you studying individuals, clinical encounters, geographic areas, institutions, or something else? Data structured at the wrong unit of analysis can be adapted, but it is easier to start with data that matches.

**Time frame and coverage.** Does your question require longitudinal data, a specific historical window, or geographic coverage beyond a single site? Many repositories specialize by domain or era, and knowing your requirements early narrows the search considerably.

**Measurement specificity.** Generic population surveys rarely capture the specialized constructs that basic science or clinical research requires. If your question hinges on a particular biomarker, behavioral measure, or administrative code, that specificity should drive your source selection — not the other way around.

**Scale.** For feasibility testing and method development, small, clean, well-documented datasets are often more useful than large raw ones. It is usually better to validate your workflow on something manageable before scaling up.

---

## Compliance First

Data access decisions in research are never purely practical. Before you use any dataset — especially one involving human subjects — you need to understand the regulatory and institutional frameworks that apply.

### IRB and Data Use Agreements

Most human subjects research requires Institutional Review Board (IRB) review, even when data are not collected directly by the researcher. Using an existing dataset does not automatically exempt a project from review; the key question is whether the data contain identifiable information about living individuals. When in doubt, contact your institution's IRB office before proceeding.

Data use agreements (DUAs) are common when accessing restricted or licensed datasets. A DUA typically specifies permitted uses, storage requirements, publication restrictions, and the procedures for secure disposal of the data at the end of a project. Violating a DUA has serious professional and legal consequences, and DUAs sometimes run to many pages of technical requirements. Read them carefully and store a copy with your project documentation.

### HIPAA, FERPA, and GDPR

If your research involves health information about individuals in the United States, the Health Insurance Portability and Accountability Act (HIPAA) governs what data can be collected, stored, shared, and analyzed. HIPAA's Safe Harbor provision defines 18 categories of identifiers that must be removed for data to be considered deidentified; the presence of any one of them means the data are still protected health information {cite}`hhs_hipaa_deidentification`.

Educational records at U.S. institutions fall under the Family Educational Rights and Privacy Act (FERPA), which restricts access to student-level data and requires consent for most disclosures.

For research involving individuals in the European Union, the General Data Protection Regulation (GDPR) imposes substantial requirements on data collection, storage, transfer, and subject rights. If you are accessing European cohort data or collaborating with EU institutions, GDPR compliance is not optional.

```{admonition} If You're at U-M
:class: note

The University of Michigan maintains institutional policies on data classification and permissible use that apply regardless of external regulatory requirements. Sensitive data categories — including health information, financial records, and personally identifiable information — must be stored and processed on approved systems. Tools that involve uploading data to third-party platforms, including some AI systems, are subject to specific review. The U-M Safe Computing website and the Research Technology Stewardship program are the right starting points for questions about data classification and approved platforms.
```

### What About Kaggle, UCI, or Other Fully Public Datasets?

This is a question researchers often hesitate to ask out loud: if I am downloading a dataset that is already publicly available — something from Kaggle, the UCI repository, or a government open data portal — do I still need to worry about IRB approval, HIPAA, or a DUA?

The short answer is: usually not, but it depends on the data, not just the source.

Most datasets on platforms like Kaggle and UCI have been either fully deidentified, synthetically generated, or sourced from domains with no human subjects component at all — house prices, sensor readings, benchmark classification tasks. For those datasets, there is no IRB trigger and no HIPAA relevance. You are not dealing with protected health information, and the data carry no obligations beyond whatever license terms the repository specifies.

That said, a few situations still require attention even with public data:

**Licensing terms.** Every dataset on Kaggle and most other repositories carries a license — Creative Commons, CC BY-NC, custom terms of service, and so on. Some restrict commercial use, redistribution, or derivative works. For academic research publication these restrictions rarely apply, but you should confirm before including results in a paper or sharing derived datasets.

**Health-related public datasets.** Some publicly available datasets contain health information that was originally collected under HIPAA and released in a deidentified form. Using them for research purposes — particularly if your analysis could re-identify individuals, if you plan to link them with other datasets, or if your institution has specific policies on health data — may still require IRB review. PhysioNet, for instance, asks researchers to sign a credentialing agreement and a data use agreement even though the underlying data are openly hosted.

**Secondary analysis of survey or human behavior data.** If a public dataset contains responses from identifiable individuals — even without names — some IRBs consider secondary analysis of that data to require at minimum an exemption determination. It is worth checking with your IRB office rather than assuming.

The cleanest practical rule: if the data has no connection to human subjects, no health information, and a permissive license, you can usually treat it as you would any other publicly available resource. If any of those conditions is uncertain, spend ten minutes confirming before you invest weeks of analysis.

---

## Finding the Right Source

Not every dataset suits every purpose, and spending a few minutes thinking through what you actually need before browsing repositories will save you considerable time. Three questions are worth asking before you commit to a source.

First, does the data structure match your use case? If your research ultimately involves clinical time series, testing a pipeline on a tidy tabular benchmark will not surface the preprocessing or modeling issues that will actually matter. The closer the test dataset is to your real data in structure, the more useful the validation.

Second, is the ground truth well-understood? When you are checking whether a pipeline is working correctly rather than discovering something new, you want a dataset where the expected behavior is established. Sources with a long publication history and documented benchmarks give you that anchor.

Third, are the licensing terms compatible with your intended use? Some datasets that appear open carry restrictions on redistribution or derivative works. For academic research this rarely poses a problem, but confirming before you invest weeks of analysis is much easier than discovering a constraint afterward.

With those questions in mind, here is an overview of well-maintained sources across a range of domains.

```{admonition} If You're at U-M
:class: note

U-M maintains institutional policies on data classification and permissible use that apply regardless of external regulatory requirements. The U-M Safe Computing website and the Research Technology Stewardship program are good starting points for questions about data governance and approved platforms. For U-M-specific data repositories — including UM Library Data Services, ICPSR, Michigan Medicine synthetic datasets, and MIDAS curated datasets — see [AI Resources at the University of Michigan](../part4/ch27_um_resources.md).
```

---

## National and Global Public Sources

A number of well-maintained public repositories are worth knowing about. The sources below are widely used in research and teaching across disciplines, and most are freely accessible without institutional affiliation.


### Kaggle

Kaggle hosts a large collection of community-contributed datasets across domains including healthcare, finance, text, images, and time series {cite}`kaggle_datasets`. Many are lightweight and competition-oriented, which makes them well-suited for benchmarking and for testing AutoML workflows quickly. The quality varies considerably, so checking whether a dataset has active discussion threads and well-maintained documentation is worth your time before committing to it.

### Zenodo

Zenodo is an open-access repository operated by CERN that allows researchers to deposit and share datasets, software, preprints, and other research outputs {cite}`zenodo`. Unlike Kaggle, which is primarily competition-oriented, Zenodo is designed for scientific archival — datasets deposited here are assigned a DOI and are meant to be citable, stable, and reproducible. It is a particularly good place to look for datasets associated with published papers, since many journals now encourage or require data deposition at the time of publication.

### PhysioNet

PhysioNet offers freely accessible physiological and clinical time-series datasets, including ECG, EEG, ICU monitoring records, and wearable sensor data {cite}`physionet`. It is widely used for signal processing, time-series modeling, and benchmarking predictive models in health research. Access to some datasets requires signing a credentialing agreement and data use agreement, which PhysioNet manages through its online platform.

### OpenNeuro

OpenNeuro provides openly shared neuroimaging datasets — fMRI, EEG, MEG, and others — organized according to the Brain Imaging Data Structure (BIDS) standard {cite}`openneuro`. The standardized format makes it considerably easier to build preprocessing pipelines that work across datasets, which is useful if you are developing methods rather than studying a specific population.

### UCI Machine Learning Repository

The UCI repository is a long-standing collection of small to medium-sized datasets frequently used for teaching and method comparison {cite}`uci_ml_repo`. Its simplicity and standardized formats make it a reliable starting point for proof-of-concept work. For most modern machine learning tasks the datasets are too small to be representative, but for understanding a method's behavior in a controlled setting they remain useful.

### Hugging Face Datasets

Hugging Face hosts a large and actively maintained collection of datasets for natural language processing, computer vision, and multimodal research {cite}`huggingface_datasets`. Many can be loaded directly through a Python API, which makes iteration fast. The platform has grown quickly, so coverage across research domains is uneven, but for text-heavy research tasks it is often the most practical starting point.

### arXiv Metadata

The arXiv metadata dataset includes titles, abstracts, authorship, and subject classifications for millions of research papers {cite}`arxiv_kaggle`. It is well-suited for text mining, topic modeling, citation analysis, and testing language model workflows on scholarly content. The data are updated regularly and the schema is well-documented.

### U.S. Government Open Data

Several U.S. federal agencies maintain open data portals that are particularly useful for structured tabular analysis and policy-oriented research. Data.gov aggregates datasets from across the federal government {cite}`datagov`. NOAA provides climate, weather, and atmospheric data {cite}`noaa`. The U.S. Census Bureau publishes demographic, economic, and housing data at multiple geographic levels {cite}`uscensus`. These sources are generally stable, well-maintained, and carry permissive terms for research use.

---

## Try This

Pick a dataset from one of the sources listed in this chapter that is relevant to your research domain. Before you download or access it, work through these questions: What is the unit of analysis? What time period does it cover? What are the licensing and use restrictions? Does it require a data use agreement or IRB review before you can use it in a publication? Does the structure of the data match what your research question actually requires, or would you need to reshape it substantially?

That due-diligence habit — running through those questions before committing — is one of the most practical things you can build into your data workflow.

---

## References

```{bibliography}
:filter: docname in docnames
```

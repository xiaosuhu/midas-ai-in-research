# Getting Your Data: Access, Sources, and Compliance

:::{admonition} What You Will Learn
:class: tip

- How to evaluate whether a dataset is appropriate for your research question
- What compliance requirements apply before you access or share data
- Where to find data through University of Michigan resources
- Where to find publicly available datasets for prototyping and method development
:::

---

## Why Data Access Deserves Its Own Chapter

It is tempting to treat data access as a logistics problem — find the file, download it, get on with the analysis. In practice, it is often the phase where research projects stall or go wrong. Researchers discover mid-project that a dataset requires an institutional agreement they did not anticipate, that a public repository they planned to use prohibits their intended use case, or that the data they assumed were deidentified turn out to carry re-identification risk. These are not edge cases; they come up regularly.

This chapter is about getting ahead of those problems. Before you open a data portal or submit an access request, it helps to be clear about what you actually need, what rules govern the data you are considering, and which sources are genuinely well-suited to your situation. That groundwork pays off.

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

Data use agreements (DUAs) are common when accessing restricted or licensed datasets. A DUA typically specifies permitted uses, storage requirements, publication restrictions, and how data must be destroyed at the end of a project. Violating a DUA has serious professional and legal consequences, and DUAs sometimes run to many pages of technical requirements. Read them carefully and store a copy with your project documentation.

### HIPAA, FERPA, and GDPR

If your research involves health information about individuals in the United States, the Health Insurance Portability and Accountability Act (HIPAA) governs what data can be collected, stored, shared, and analyzed. HIPAA's Safe Harbor provision defines 18 categories of identifiers that must be removed for data to be considered deidentified; the presence of any one of them means the data are still protected health information {cite}`hhs_hipaa_deidentification`.

Educational records at U.S. institutions fall under the Family Educational Rights and Privacy Act (FERPA), which restricts access to student-level data and requires consent for most disclosures.

For research involving individuals in the European Union, the General Data Protection Regulation (GDPR) imposes substantial requirements on data collection, storage, transfer, and subject rights. If you are accessing European cohort data or collaborating with EU institutions, GDPR compliance is not optional.

### University of Michigan Specific Requirements

The University of Michigan maintains institutional policies on data classification and permissible use that apply regardless of external regulatory requirements. Sensitive data categories — including health information, financial records, and personally identifiable information — must be stored and processed on approved systems. Tools that involve uploading data to third-party platforms, including some AI systems, are subject to specific review. When working with sensitive research data, check whether the tools and platforms you plan to use are covered under a U-M institutional agreement.

The U-M Safe Computing website and the Research Technology Stewardship program are the right starting points for questions about data classification and approved platforms.

---

## University of Michigan Data Resources

### U-M Library Data Services

The University of Michigan Library maintains a searchable catalog of licensed and open datasets spanning social science, health, economics, education, and the humanities {cite}`umich_library_data`. Many datasets are directly accessible to U-M affiliates and come with documentation, codebooks, and subject librarian support. If you are not sure where to start for a particular domain, the Library's research data services team can point you toward appropriate sources and help you navigate access requirements.

### ICPSR

The Inter-university Consortium for Political and Social Research (ICPSR), headquartered at U-M, hosts thousands of curated social, behavioral, and health-related datasets, including longitudinal surveys, administrative records, and cross-national comparative studies {cite}`icpsr`. Data are typically accompanied by detailed codebooks and metadata, and many restricted-use datasets are accessible through a formal application process. ICPSR's data management practices make it one of the more reliable sources for reproducibility-focused work.

### Michigan Medicine

Michigan Medicine provides synthetic and simulated clinical datasets designed to resemble real electronic health record data without exposing protected health information {cite}`michigan_medicine`. These datasets are appropriate for testing analytical pipelines, exploring feature engineering strategies, and evaluating model deployment approaches without IRB constraints. They are particularly well-suited to researchers who want to develop clinical AI workflows before applying for access to real patient data.

### MIDAS

The Michigan Institute for Data and AI in Society (MIDAS) coordinates access to a growing collection of curated datasets used in pilot projects, training workshops, and AI Sandbox demonstrations {cite}`midas_umich`. These datasets are selected for pedagogical value and for quick experimentation, and they come with the practical advantage of local support — if you run into an issue, someone nearby has likely encountered it before.

---

## National and Global Public Sources

### Kaggle

Kaggle hosts a large collection of community-contributed datasets across domains including healthcare, finance, text, images, and time series {cite}`kaggle_datasets`. Many are lightweight and competition-oriented, which makes them well-suited for benchmarking and for testing AutoML workflows quickly. The quality varies considerably, so checking whether a dataset has active discussion threads and well-maintained documentation is worth your time before committing to it.

### PhysioNet

PhysioNet offers freely accessible physiological and clinical time-series datasets, including ECG, EEG, ICU monitoring records, and wearable sensor data {cite}`physionet`. It is widely used for signal processing, time-series modeling, and benchmarking predictive models in health research. Access to some datasets requires signing a data use agreement, which PhysioNet manages through its online platform.

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

## Choosing the Right Dataset for Quick Testing

When the goal is to test a method or validate a workflow before applying it to your actual research data, a few principles help narrow the choice.

Favor datasets where the ground truth is well-understood. If you are using a dataset to check whether your pipeline is working correctly, you want to be able to verify the output. Datasets with a long publication history and established benchmarks give you that anchor.

Match the data structure to your eventual use case. If your research ultimately involves clinical time series, testing on tabular survey data will not catch the preprocessing or modeling issues that will matter in production. The closer the test dataset is to your real data in structure, the more useful the test.

Check the licensing terms before you invest time. Some datasets that appear open carry restrictions on commercial use, redistribution, or derivative works. For academic research this rarely poses a problem, but it is worth confirming rather than discovering a constraint after the fact.

---

## Try This

Pick a dataset from one of the sources listed in this chapter that is relevant to your research domain. Before you download or access it, work through these questions: What is the unit of analysis? What time period does it cover? What are the licensing and use restrictions? Does it require a data use agreement or IRB review before you can use it in a publication? Does the structure of the data match what your research question actually requires, or would you need to reshape it substantially?

That due-diligence habit — running through those questions before committing — is one of the most practical things you can build into your data workflow.

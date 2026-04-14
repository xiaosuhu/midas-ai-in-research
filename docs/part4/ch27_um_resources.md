# Chapter 27: AI Resources at the University of Michigan

```{tip}
This chapter is a starting point, not a complete inventory. UM's AI landscape is moving fast, and new tools, services, and funding programs come online regularly. When something here looks out of date, check directly with MIDAS or ARC, or visit the links listed in each section.
```

## Overview

The University of Michigan supports AI-assisted research through a range of campus-hosted tools, high-performance computing systems, secure data environments, and expert consulting services. This chapter walks through the key resources available to UM researchers, organized in two parts: what MIDAS offers directly, followed by the broader set of U-M infrastructure and services.

---

## Data Sensitivity and Approved Computing Environments

Not all data can go everywhere, and choosing the wrong environment for sensitive research data is one of the more consequential mistakes a researcher can make. At U-M, tools and computing environments fall into three broad tiers based on what level of data protection they provide.

The first tier is public commercial tools on their free tiers — the default version of ChatGPT, Gemini, Claude, and similar products when accessed without a paid or enterprise account. Some providers may retain your inputs and use them to improve their models. Unpublished results, grant ideas, confidential collaborator information, and anything covered by HIPAA or other data governance regulations should not go into these tools.

The second tier is institutionally governed tools — UM-GPT, Maizey, Microsoft Azure OpenAI through U-M's enterprise agreement, and Google Gemini through U-M's institutional subscription. In these environments, your inputs are contractually not used for model training, and data is stored within enterprise-controlled infrastructure. This is the appropriate environment for most research-related AI use at U-M, including working with draft manuscripts, grant materials, and research ideas that are not yet public.

The third tier is local or self-hosted models — tools like Ollama running on your own machine, or on-premise LLMs deployed on secure institutional clusters like Armis2. Nothing leaves your machine or your institution's network. This is the right choice when working with genuinely sensitive data that cannot go anywhere outside a controlled environment, even in an enterprise system.

For choosing between U-M's HPC clusters specifically, the decision usually comes down to data sensitivity:

| Data Type | Appropriate Environment |
|-----------|------------------------|
| Public or synthetic data | Great Lakes, local machine, or Colab |
| Sensitive but not HIPAA-covered | Great Lakes (with data governance controls) |
| HIPAA-covered (e.g., EHR data) | Armis2 |
| Large-scale AI with big data storage needs | Turbo Research Storage |

If you are unsure where your data falls, the U-M Safe Computing website and the Research Technology Stewardship program are the right starting points. MIDAS and U-M Research Computing are also available for guidance.

**U-M Safe Computing:** https://safecomputing.umich.edu/

---

## Part 1: MIDAS Resources

MIDAS is the Michigan Institute for Data and AI in Society, and it is the home of this handbook. Beyond publishing resources like this one, MIDAS offers a range of direct services to U-M researchers, from hands-on workshops and consulting to grant support and pilot funding. If you are not sure where to start, MIDAS is usually the right first contact.

### MIDAS AI Sandbox

The AI Sandbox is MIDAS's weekly, drop-in learning space where researchers across campus can explore AI tools hands-on, without needing any prior experience. Each session focuses on a specific model or workflow, from image segmentation to text classification, and walks participants through running it live in a browser. Sessions are small by design so that everyone gets guided support, and you are welcome to bring your own data to explore alongside the example materials. Registration is required due to popular demand.

**Link:** https://midas.umich.edu/ai-sandbox/

---

### MIDAS Consulting

MIDAS provides free AI and data science consulting for UM researchers. Common topics include machine learning and deep learning, feature engineering, model selection, responsible AI practices, and designing AI-enabled research workflows. This is a good first call when you are not sure where to start with an analysis.

**Link:** https://midas.umich.edu/consulting/

---

### Faculty-Student Research Connection

MIDAS runs a formal program connecting faculty with graduate and undergraduate students who have data science and AI skills. The MIDAS Student Organizations Council represents more than 1,100 students across programs and student groups, many of whom are actively looking to contribute to faculty research projects. If you have a project ready for student involvement, whether standalone or part of a larger initiative, you can submit the details through MIDAS's Research Projects Collection Form. This is a genuinely underused resource that many faculty do not know exists ({cite}`midas_umich`).

**Link:** https://midas.umich.edu/research/research-resources/faculty-student-research-connection/

---

### MIDAS Grant Support

If you are preparing a grant proposal that involves AI or data science methods, MIDAS offers direct support that goes beyond a quick email exchange. The team can conduct red team reviews of your proposal, flagging methodological weak points and anticipating reviewer concerns before submission. They can also help you draft Letters of Support and connect you with data science collaborators on campus. If your proposal needs to describe MIDAS facilities or resources, you can request boilerplate language through a Google Form rather than writing it from scratch.

This is a genuinely underused service. If you are putting together an NSF, NIH, or foundation proposal with any computational or AI component, it is worth reaching out early, not just before the deadline ({cite}`midas_umich`).

**Link:** https://midas.umich.edu/research/

---

### MIDAS Workshops

MIDAS regularly hosts workshops covering topics such as introduction to machine learning, responsible AI, working with large language models, RAG and Maizey workflows, and using HPC for AI research.

**Link:** https://midas.umich.edu/workshops/

---

### MIDAS Generative AI Tutorial Series

MIDAS runs an ongoing monthly tutorial series for researchers who want to understand when, why, and how to bring generative AI into their work. The series is open to all UM researchers and requires no prior experience with generative AI. Recordings are made available for those who cannot attend in person ({cite}`midas_umich`).

**Link:** https://midas.umich.edu/research/research-resources/generative-ai-hub/generative-ai-tutorials/

---

### MIDAS Pilot Funding

MIDAS offers competitive pilot grants to support data science-driven interdisciplinary research at UM.

**Link:** https://midas.umich.edu/funding/

---

## Part 2: Other U-M Resources

Beyond MIDAS, the university offers a broad set of tools, computing infrastructure, data resources, and support services. This section covers the most relevant ones for researchers working with AI and data science methods.

### Campus AI Tools and Platforms

#### UMGPT

UMGPT is the university's secure, institution-hosted large language model service, available to all UM faculty, staff, and students. Because it runs within UM's infrastructure, it is appropriate for working with non-public research materials that you would not want to send to an external commercial service. Researchers use it for drafting and revising writing, summarizing literature, explaining concepts, generating and debugging code, and a range of other day-to-day tasks.

**Link:** https://its.umich.edu/computing/ai/umgpt

---

#### Maizey

Maizey allows researchers to upload documents and build custom Retrieval-Augmented Generation (RAG) systems without writing any code. This is particularly useful for literature review assistance, creating lab onboarding or SOP chatbots, building course material Q&A assistants, and summarizing large policy or documentation collections.

**Link:** https://maizey.ai.umich.edu/

---

#### Google Gemini (UM Institutional Access)

UM has an institutional subscription to Google Gemini, which gives researchers access to Gemini through their UM Google Workspace account. This provides a capable multimodal model, including text, image, and document understanding, within an enterprise agreement that offers additional data protections compared to consumer-tier access. Log in through your UM Google account to access it.

**Link:** https://gemini.google.com/ (sign in with your UM account)

---

#### NotebookLM (UM Google Workspace)

NotebookLM is Google's document-grounded research assistant. You upload your own sources — PDFs, Google Docs, URLs, or YouTube videos — and it answers questions grounded exclusively in those materials, with inline citations linking back to the original text. This makes it well suited for the synthesis stage of a literature review, for checking whether a draft argument is consistent with the papers you have read, or for getting a fast orientation to an unfamiliar set of documents.

Because NotebookLM is part of Google's product suite, UM researchers can access it directly through their institutional Google Workspace account. No separate sign-up is needed.

**Link:** https://notebooklm.google.com (sign in with your @umich.edu account)

---

### High-Performance Computing Resources

#### Great Lakes Cluster

Great Lakes is UM's primary HPC system for large-scale computing. It provides GPU and CPU nodes for ML training, a SLURM scheduler, and pre-installed software modules for PyTorch, TensorFlow, and JAX. It is well suited for AutoGluon training, deep learning experiments, and large simulations where a laptop or Colab session is not enough.

**Link:** https://arc.umich.edu/greatlakes/

---

#### Armis2 (HIPAA-Aligned Secure HPC)

Armis2 supports computation involving sensitive or clinical data, including electronic health records, restricted research datasets, and data subject to HIPAA or similar regulations. It includes GPU support for machine learning workflows and is the right environment when your data cannot leave a compliant infrastructure.

**Link:** https://arc.umich.edu/armis2/

---

#### Lighthouse (Researcher-Owned HPC Hardware)

Lighthouse is designed for researchers whose grants or funding sources require purchasing computing hardware. Rather than applying for allocations on a shared cluster, these researchers work with ARC to place their own hardware within the Slurm environment, with ARC handling the data center, networking, and staff support. That hardware is then for the exclusive use of the research group that purchased it. This makes Lighthouse a good fit when your grant mandates hardware acquisition, or when your workflow has requirements that Great Lakes and Armis2 cannot meet. Note that sensitive or HIPAA-covered data is not permitted on Lighthouse.

**Link:** https://its.umich.edu/advanced-research-computing/high-performance-computing/lighthouse

---

#### Turbo Research Storage

Turbo is ARC's high-capacity, high-performance network storage service for active research data. It is designed to integrate directly with all of ARC's HPC clusters, including Great Lakes, Armis2, and Lighthouse, making it a natural companion to cluster-based workflows. If your research generates large volumes of data that need to stay accessible during active analysis, such as neuroimaging datasets, high-density sensor streams, or multimodal corpora, Turbo is the right place to keep it. Basic Turbo storage is included in the UM Research Computing Package, and additional capacity is available at a per-terabyte rate. Sensitive data storage is supported; consult the ARC Sensitive Data Guide for specifics.

**Link:** https://its.umich.edu/advanced-research-computing/storage/turbo

---

### Data Access Resources

#### Deep Blue Data

Deep Blue Data is UM's institutional research data repository, hosted by the UM Library. Researchers can deposit and publish their datasets here to support open science and reproducibility, and can also discover datasets deposited by other UM researchers.

**Link:** https://deepblue.lib.umich.edu/data

---

#### UM Library Data Services

The UM Library offers a searchable data catalog, access to licensed datasets, and consultations covering metadata, data management planning, and reproducibility. This is a particularly valuable resource for researchers in the social sciences, public policy, and health-related fields.

**Link:** https://guides.lib.umich.edu/data

---

#### ICPSR

The Inter-university Consortium for Political and Social Research (ICPSR), headquartered at U-M, hosts thousands of curated social, behavioral, and health-related datasets, including longitudinal surveys, administrative records, and cross-national comparative studies {cite}`icpsr`. Data are typically accompanied by detailed codebooks and metadata, and many restricted-use datasets are accessible through a formal application process. ICPSR's data management practices make it one of the more reliable sources for reproducibility-focused work.

**Link:** https://www.icpsr.umich.edu/

---

#### Michigan Medicine Synthetic Datasets

Michigan Medicine provides synthetic and simulated clinical datasets designed to resemble real electronic health record data without exposing protected health information {cite}`michigan_medicine`. These datasets are appropriate for testing analytical pipelines, exploring feature engineering strategies, and evaluating model deployment approaches without IRB constraints. They are particularly well-suited to researchers who want to develop clinical AI workflows before applying for access to real patient data.

**Link:** https://www.michiganmedicine.org/

---

### ARC Consulting

Advanced Research Computing (ARC), a division of ITS, offers scientific computing and research consulting services to help implement machine learning and data driven workflows within their projects. These services include expert guidance on data science projects, identifying proper tools, and programming in support of implementing advanced data analytics, machine learning models, and computational techniques to enhance research projects. Researchers are not required to be users of ARC's HPC services to take advantage of the consulting service. This service is **not** for general guidance on the use of HPC resources ARC provides.

**Link:** https://its.umich.edu/advanced-research-computing/consulting

---

### UM Library Workshops

The UM Library's Technology Training Center offers workshops on reproducible research, data management, Python and R fundamentals, and data visualization and cleaning.

**Link:** https://ttc.iss.lsa.umich.edu/

---

### Other Funding Programs

#### OVPR Funding Programs

The Office of the Vice President for Research administers several funding programs, including the Research Catalyst and Innovation Fund, bridge support programs, and multidisciplinary research seed grants.

**Link:** https://research.umich.edu/funding/

---

#### Unit-Level Resources

Many UM units offer small grants, cloud compute credits through AWS, GCP, or Azure, and student support for data projects. Check with your departmental research office to find out what is available in your unit.

---

## Quick Reference Table

| Category | Resource | Description | Link |
|---------|----------|-------------|------|
| **MIDAS** | AI Sandbox | Weekly hands-on AI workshop for researchers | https://midas.umich.edu/ai-sandbox/ |
| **MIDAS** | MIDAS Consulting | AI and ML guidance | https://midas.umich.edu/consulting/ |
| **MIDAS** | Faculty-Student Connection | Match with student data scientists | https://midas.umich.edu/research/research-resources/faculty-student-research-connection/ |
| **MIDAS** | Grant Support | Red team reviews, Letters of Support, proposal boilerplate | https://midas.umich.edu/research/ |
| **MIDAS** | MIDAS Workshops | General AI and ML workshops | https://midas.umich.edu/workshops/ |
| **MIDAS** | GenAI Tutorial Series | Monthly GenAI tutorials for researchers | https://midas.umich.edu/research/research-resources/generative-ai-hub/generative-ai-tutorials/ |
| **MIDAS** | MIDAS Pilot Grants | Interdisciplinary research seed funding | https://midas.umich.edu/funding/ |
| AI Tools | UMGPT | Secure UM-hosted LLM service | https://its.umich.edu/computing/ai/umgpt |
| AI Tools | Maizey | Build custom RAG systems | https://maizey.ai.umich.edu/ |
| AI Tools | Google Gemini | Multimodal AI via UM institutional access | https://gemini.google.com/ |
| AI Tools | NotebookLM | Document-grounded research assistant via UM Google Workspace | https://notebooklm.google.com |
| HPC | Great Lakes | Large-scale compute for ML | https://arc.umich.edu/greatlakes/ |
| Secure HPC | Armis2 | HIPAA-aligned secure compute | https://arc.umich.edu/armis2/ |
| HPC | Lighthouse | Researcher-owned hardware in ARC Slurm environment | https://its.umich.edu/advanced-research-computing/high-performance-computing/lighthouse |
| Storage | Turbo Research Storage | High-capacity active storage integrated with ARC HPC clusters | https://its.umich.edu/advanced-research-computing/storage/turbo |
| Data Access | Deep Blue Data | UM research data repository | https://deepblue.lib.umich.edu/data |
| Data Access | ICPSR | Curated research datasets | https://www.icpsr.umich.edu/ |
| Data Access | Michigan Medicine | Synthetic clinical datasets | https://www.michiganmedicine.org/ |
| Data Access | UM Library | Data catalog and consultations | https://guides.lib.umich.edu/data |
| Consulting | ARC | Scientific computing and research consulting | https://its.umich.edu/advanced-research-computing/consulting |
| Training | UM Library Workshops | Data management and coding workshops | https://ttc.iss.lsa.umich.edu/ |
| Funding | OVPR Programs | UM research funding programs | https://research.umich.edu/funding/ |

---

```{bibliography}
:filter: docname in docnames
```

# Ethics, Privacy, and Compliance

## 1. Introduction

Artificial intelligence (AI) tools now participate in nearly every layer of academic research—from literature review and drafting to data analysis, modeling, and dissemination. As these tools become woven into research workflows, ethical and privacy considerations take on heightened importance. Responsible AI use is not only a matter of regulatory compliance; it is fundamental to *scientific reproducibility*, *public trust*, and *institutional accountability*.  

Using AI responsibly means understanding **what data we send into AI systems**, **how the model may store or process that data**, **what risks exist for research integrity**, and **what oversight structures guide ethical deployment** {cite}`NIST2023AI` {cite}`ISO42001`.

A particularly common concern among researchers is whether sharing research ideas, hypotheses, or unpublished text with an AI tool risks *intellectual leakage*. This chapter addresses that question directly and explains how different classes of AI systems handle user data, what protections exist, and how researchers can choose appropriate environments (e.g., U-M approved tools, on-premise LLMs, or air-gapped compute clusters).

---

## 2. Core Ethical Principles

### **Transparency**
Researchers should understand the capabilities and limits of AI tools, including how outputs are generated and whether citations, summaries, or analyses are explainable or verifiable. Transparent documentation of AI use is increasingly required by journals and funders.

### **Accountability**
Human researchers remain responsible for the scientific validity of all AI-assisted outputs. This includes verifying literature citations, checking analytical results, and ensuring that AI-generated content does not introduce bias or misinterpretation.

### **Fairness and Equity**
AI systems trained on incomplete or unrepresentative data may reinforce or amplify disparities. Fairness requires attention to whether datasets represent diverse populations and whether downstream outputs produce equitable benefits or burdens.

### **Beneficence and Non-maleficence**
AI should be used to enhance knowledge and societal good while minimizing risks of harm—to research participants, communities, or scientific credibility.

### **Human Oversight**
Automated decision-making without human review can lead to errors, privacy violations, or unethical interpretations. Best practice is to position AI as an assistive tool, not an autonomous decision-maker {cite}`NIST2023AI`.

---

## 3. Data Privacy and Security

### **Handling Sensitive Data**
Many research domains involve sensitive or regulated data—electronic health records (EHR), neuroimaging, genomic data, classroom information, or identifiable photos. When these data are used with AI systems, researchers must ensure compliance with HIPAA, FERPA, GDPR, and applicable U-M policy.

- **HIPAA** governs protected health information in clinical and research contexts. Uploading identifiable health data to a public AI model *violates HIPAA* unless a Business Associate Agreement exists.  
- **FERPA** restricts how student educational records can be processed or disclosed.  
- **GDPR** imposes strict requirements for data minimization, consent, and cross-border processing for EU persons.

### **UM Secure Computing Environments**
The University of Michigan provides secure, compliant infrastructures for AI-related work involving sensitive data:

- **Armis2** — HIPAA-aligned secure research cluster  
- **Lighthouse** — Michigan Medicine’s secure analytics environment  
- **Great Lakes** — HPC cluster for general research with data governance controls  

Researchers handling controlled data should use these environments or institutionally approved tools rather than public AI services.

### **Does AI “steal ideas” or share them with other users?**
This is one of the most frequent concerns raised by researchers.

There are *three categories* of AI tools, each with different privacy guarantees:

1. **Public commercial AI models (e.g., free-tier ChatGPT, Gemini, Claude)**  
   - Some providers may **retain user inputs to improve models** unless users opt out.  
   - They **do not intentionally share your content with other users**, but the data *can* be used for training unless a privacy policy explicitly forbids it.  
   - This means unpublished manuscripts, grant ideas, or confidential institutional information should *not* be entered.

2. **Enterprise or institutionally governed AI (e.g., U-M GPT, Maizey, Microsoft Azure OpenAI with enterprise contract)**  
   - Inputs are **not used for training**.  
   - Data are governed by institutional agreements and stored within enterprise-controlled infrastructure.  
   - This is the recommended environment for research-related writing or ideation.

3. **Local or self-hosted models (e.g., LM Studio, Ollama, on-premise LLMs on Armis2)**  
   - Inputs remain on the researcher’s machine or secure cluster.  
   - **Highest level of confidentiality**. Ideal for proprietary or sensitive research.

So the answer is: *AI does not “steal” ideas, but some systems may store your inputs unless you use an enterprise or local model.* Choosing the correct environment solves most of these concerns.

---

## 4. Bias, Fairness, and Representation

### **Sources of Bias**
Bias can enter AI workflows through:

- Skewed or unrepresentative training datasets  
- Historical inequities embedded in source data  
- Sampling biases in web-scale corpora  
- Annotation biases in crowdsourced labels {cite}`Mehrabi2021SurveyBias`

In biomedical and social research, such biases may lead to harmful misclassification, unequal model performance across demographic groups, or invalid scientific conclusions.

### **Auditing Outputs**
Best practices for fairness include:

- Checking model behavior on subgroups  
- Testing robustness to perturbed datasets  
- Comparing outputs against domain knowledge  
- Documenting model limitations

### **Equitable Dataset Design**
Whenever possible, research datasets should include diverse populations representative of the actual study context. FAIR principles (Findable, Accessible, Interoperable, Reusable) also help reduce structural biases by promoting transparency and documentation.

---

## 5. Research Governance and Institutional Oversight

### **IRB and Data Use Agreements**
Human subjects research involving AI may require:

- IRB review for analysis of identifiable or potentially identifiable data  
- Data Use Agreements (DUAs) when using external datasets  
- Explicit consent language if AI tools will handle participant data

### **AI Accountability Frameworks**
Several formal frameworks guide responsible AI research:

- **ISO/IEC 42001:2023**, the first international AI management system standard {cite}`ISO42001` 
- **NIST AI Risk Management Framework (AI RMF)**, emphasizing governance, monitoring, and stakeholder engagement {cite}`NIST2023AI`  
- [**U-M’s Research Integrity Program**](https://research-compliance.umich.edu/research-integrity) and [**ITS/HITS security offices**](https://safecomputing.umich.edu/dataguide), which provide guidance on secure data handling and compliance

These frameworks help researchers build workflows that are auditable, reproducible, and ethically defensible.

---

## 6. Case Studies

### **Case Study 1: Bias Propagation in Clinical Classification**
A widely discussed example is the racial bias discovered in clinical risk scores where AI systems underestimated the severity of illness in marginalized populations due to historical inequities embedded in EHR datasets {cite}`Obermeyer2019Bias`.  
This demonstrates how unbalanced training data can produce inequitable care recommendations, even when developers do not explicitly encode demographic variables.

### **Case Study 2: Privacy Leakage from LLM Training Corpora**
Large language models trained on public internet data have been shown to occasionally **memorize** snippets of personal information or copyrighted text {cite}`Carlini2021Extracting`.  
This highlights why regulated or unpublished research materials should never be uploaded to public training datasets and why enterprises now prohibit training on user content.

---

## 7. Practical Guidelines for Ethical AI Use

### **Checklist**
- [ ] Use institutionally governed or local models for research ideas, drafts, or unpublished data  
- [ ] Avoid entering identifiable human subject data into public AI tools  
- [ ] Maintain transparent documentation of AI-assisted steps  
- [ ] Audit model outputs for errors, hallucinations, or bias  
- [ ] Verify citations and factual claims  
- [ ] Use reproducible pipelines when integrating AI into data analysis  
- [ ] Seek IRB guidance when AI interacts with human subject data  
- [ ] Follow U-M data classification and storage policies  
- [ ] Provide attribution for AI tools used in writing or analysis  
- [ ] Retain human oversight for all research decisions

### **Documentation Templates**
To support transparency, reproducibility, and ethical AI use, this book provides a set of ready-to-use documentation templates. These include:

- AI usage statements
- Data provenance and preprocessing logs
- Model card summaries
- Ethics review checklists

For examples and copy-ready templates, see the {ref}`documentation-templates-examples` section in Part III of this book.

---

## 8. Reflection: The Role of Researchers in Responsible AI Adoption

Researchers occupy a unique position of responsibility. As early adopters of advanced AI tools, they shape not only the scientific outcomes but also the *social expectations* for how AI will be integrated into academic inquiry. Responsible use requires critical thinking, transparency, and respect for the people and communities whose data underpin AI research.  
By approaching AI with both enthusiasm and caution, researchers can model practices that enhance trust, preserve privacy, and advance ethical innovation.

---

## References

```{bibliography}
:filter: docname in docnames
```


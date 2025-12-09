# **Documentation Templates Examples**

## AI Usage Statement

**Purpose of AI use:**  
(Describe why AI tools were used — e.g., literature summarization, code generation, exploratory analysis, text revision.)

**AI tools used:**  
- Tool name(s): (e.g., U-M GPT, Maizey, ChatGPT Enterprise, LM Studio local model)  
- Version or model (if available):  
- Access environment:  
  - [ ] U-M enterprise tool  
  - [ ] Local/offline model  
  - [ ] Public commercial model (non-sensitive content only)

**Type of content generated or assisted:**  
(Check all that apply)  
- [ ] Drafting or editing text  
- [ ] Idea generation or brainstorming  
- [ ] Code suggestions or debugging  
- [ ] Data visualization suggestions  
- [ ] Statistical/modeling suggestions  
- [ ] Summary of publicly available literature  
- [ ] No unpublished or sensitive data were provided to the AI system  
- [ ] Other: ____________________________

**Human verification and oversight:**  
(Describe how generated content was checked, validated, and edited.)

**Data privacy considerations:**  
- No identifiable, proprietary, or regulated data (e.g., HIPAA/FERPA/GDPR) were entered into non–U-M AI tools.  
- Sensitive data, if used, were processed only within approved secure environments (Armis2, Lighthouse, Great Lakes, or local offline models).  

**Limitations and disclaimers:**  
(Describe known limitations of AI use and steps taken to mitigate errors or bias.)

---

## Data Provenance and Preprocessing Log

### 1. Dataset Overview
- Dataset name:  
- Version/date acquired:  
- Source (PI, repository, instrument):  
- Link or accession number (if public):  
- IRB or DUA reference (if applicable):

### 2. Data Structure
- Number of subjects/samples:  
- Variables/features included:  
- File formats (CSV, JSON, EDF, NIfTI, etc.):  
- Original storage location (secure cluster, server directory):

### 3. Preprocessing Steps
For each step, specify:
- Date  
- Tool/method used (AI, Python, R, manual)  
- Person responsible  
- Code or command (if applicable)  
- Output produced  
- Notes on data quality or anomalies

**Example format:**

| Date | Step | Tool/Method | Description | Output | Verified By |
|------|------|--------------|-------------|--------|-------------|
| 2025-01-10 | Motion filtering | Python script | Removed segments with >10 mm displacement | cleaned_data_v1.csv | X. Hu |
| 2025-01-12 | AI-assisted feature suggestions | U-M GPT (no data uploaded) | Identified candidate HRF regressors; manually evaluated | feature_notes.md | X. Hu |

### 4. Data Exclusion / Inclusion Criteria
(List rules for exclusions + rationale.)

### 5. Version Tracking
- Raw data filename:  
- Cleaned data filename:  
- Analysis-ready data filename:  
- Git commit tags or data version number:

### 6. Reproducibility Notes
(Assumptions, known issues, missing metadata, steps that require manual intervention.)

---

## Model Card Summary

### 1. Model Overview
- Model name:  
- Version:  
- Architecture (e.g., GRU, LSTM, ResNet, Transformer, LLM name):  
- Purpose of model (task):  

### 2. Intended Use
- Primary intended use cases:  
- Out-of-scope uses (important to prevent misuse):  

### 3. Training Data
- Source datasets:  
- Size (subjects, samples, tokens):  
- Data characteristics (e.g., demographic composition, imaging modality):  
- Preprocessing steps:  

### 4. Evaluation Metrics
- Metrics used (AUC, accuracy, F1, MAE, etc.):  
- Cross-validation strategy:  
- Baseline comparisons:  

### 5. Performance Summary
Provide a brief table:

| Subgroup | Metric | Notes |
|---------|--------|-------|
| Overall |        |       |
| Group A |        |       |
| Group B |        |       |

### 6. Ethical & Fairness Considerations
- Potential biases:  
- Known failure modes:  
- Mitigation strategies:  

### 7. Limitations
- Data limitations  
- Generalizability limits  
- Known sources of uncertainty  

### 8. Recommended Monitoring
- What should be monitored if deployed (drift, errors, inequity):  


---

## Ethics Review Checklist

### A. Data & Privacy
- [ ] Does the project involve human subjects?  
- [ ] Is IRB approval required?  
- [ ] Is a Data Use Agreement (DUA) required?  
- [ ] Have you classified the data under U-M’s Sensitive Data Guide?  
- [ ] Are sensitive data stored only on approved platforms (Armis2, Lighthouse, Great Lakes)?  
- [ ] Are all AI tools used appropriate for the data sensitivity level?

### B. AI Tool Use
- [ ] Has an AI usage statement been documented?  
- [ ] Were only enterprise or local AI systems used for unpublished or identifiable data?  
- [ ] Were model outputs independently verified by a human expert?  
- [ ] Were limitations or hallucinations noted and corrected?

### C. Bias & Fairness
- [ ] Have potential sources of dataset bias been identified?  
- [ ] Have subgroup performance metrics been evaluated?  
- [ ] Have steps been taken to avoid harm or inequitable outcomes?

### D. Reproducibility
- [ ] Is all preprocessing logged (with code, versions, and parameters)?  
- [ ] Are scripts, models, and data versioned?  
- [ ] Are all AI-assisted steps documented and reproducible?

### E. Compliance & Institutional Oversight
- [ ] Have U-M Research Integrity guidelines been followed?  
- [ ] Has sensitive data processing complied with HIPAA/FERPA/GDPR regulations?  
- [ ] Are export control considerations relevant (e.g., dual-use technology)?  
- [ ] Is the project aligned with NIST AI RMF and/or ISO 42001 principles?

### F. Dissemination
- [ ] Does the manuscript or report clearly state how AI tools were used?  
- [ ] Are citations and factual claims verified?  
- [ ] Is a model card or equivalent documentation included?


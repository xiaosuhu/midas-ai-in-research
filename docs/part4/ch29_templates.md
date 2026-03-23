# Chapter 29: Quick Reference Templates

```{important}
The templates in this chapter are starting points, not compliance checklists. What counts as adequate documentation varies by institution, journal, and funding agency. Before submitting work that involved AI tools or sensitive data, check the specific requirements from your journal, IRB, and department. When in doubt, document more rather than less.
```

The following templates are designed to be copied directly into your project documentation. They cover the four most common documentation needs that come up in AI-assisted research: stating how AI tools were used, logging data provenance and preprocessing decisions, summarizing a model for readers, and reviewing your project against a basic ethics checklist before submission.

---

## AI Usage Statement

**Purpose of AI use:**
(Describe why AI tools were used, for example: literature summarization, code generation, exploratory analysis, writing revision.)

**AI tools used:**
- Tool name(s): (e.g., UM-GPT, Maizey, Claude, Gemini via UM Workspace)
- Version or model (if available):
- Access environment:
  - [ ] UM enterprise tool
  - [ ] Local or offline model
  - [ ] Public commercial model (non-sensitive content only)

**Type of content generated or assisted:**
(Check all that apply)
- [ ] Drafting or editing text
- [ ] Idea generation or brainstorming
- [ ] Code suggestions or debugging
- [ ] Data visualization suggestions
- [ ] Statistical or modeling suggestions
- [ ] Summary of publicly available literature
- [ ] No unpublished or sensitive data were provided to the AI system
- [ ] Other: ____________________________

**Human verification and oversight:**
(Describe how generated content was checked, validated, and edited.)

**Data privacy considerations:**
- No identifiable, proprietary, or regulated data (e.g., HIPAA, FERPA, GDPR) were entered into non-UM AI tools.
- Sensitive data, if used, were processed only within approved secure environments (Armis2, Lighthouse, Great Lakes, or local offline models).

**Limitations and disclaimers:**
(Describe known limitations of AI use and steps taken to mitigate errors or bias.)

---

## Data Provenance and Preprocessing Log

### 1. Dataset Overview
- Dataset name:
- Version or date acquired:
- Source (PI, repository, instrument):
- Link or accession number (if public):
- IRB or DUA reference (if applicable):

### 2. Data Structure
- Number of subjects or samples:
- Variables and features included:
- File formats (CSV, JSON, Parquet, etc.):
- Original storage location:

### 3. Preprocessing Steps

For each step, document the date, the tool or method used, who was responsible, the relevant code or command, the output produced, and any notes on data quality or anomalies.

| Date | Step | Tool/Method | Description | Output | Verified By |
|------|------|-------------|-------------|--------|-------------|
| 2025-03-01 | Remove duplicate records | Python (pandas) | Dropped 47 exact duplicate rows based on respondent ID | cleaned_survey_v1.csv | J. Smith |
| 2025-03-03 | AI-assisted feature suggestions | UM-GPT (no data uploaded) | Prompted for candidate interaction terms based on theory; evaluated manually | feature_notes.md | J. Smith |

### 4. Data Exclusion and Inclusion Criteria
(List rules for exclusions and the rationale behind each.)

### 5. Version Tracking
- Raw data filename:
- Cleaned data filename:
- Analysis-ready data filename:
- Git commit tags or data version number:

### 6. Reproducibility Notes
(Any assumptions, known issues, missing metadata, or steps that require manual intervention.)

---

## Model Card Summary

### 1. Model Overview
- Model name:
- Version:
- Architecture (e.g., gradient boosting, LSTM, Transformer, fine-tuned LLM):
- Purpose of model (task):

### 2. Intended Use
- Primary intended use cases:
- Out-of-scope uses (important for preventing misuse):

### 3. Training Data
- Source datasets:
- Size (subjects, samples, tokens):
- Data characteristics (e.g., demographic composition, domain, time period):
- Preprocessing steps:

### 4. Evaluation Metrics
- Metrics used (AUC, accuracy, F1, MAE, etc.):
- Cross-validation strategy:
- Baseline comparisons:

### 5. Performance Summary

| Subgroup | Metric | Notes |
|---------|--------|-------|
| Overall | | |
| Group A | | |
| Group B | | |

### 6. Ethical and Fairness Considerations
- Potential biases:
- Known failure modes:
- Mitigation strategies:

### 7. Limitations
- Data limitations
- Generalizability limits
- Known sources of uncertainty

### 8. Recommended Monitoring
(What should be monitored if this model is deployed or reused: drift, error patterns, fairness over time.)

---

## Ethics Review Checklist

### A. Data and Privacy
- [ ] Does the project involve human subjects?
- [ ] Is IRB approval required?
- [ ] Is a Data Use Agreement (DUA) required?
- [ ] Have you classified the data under UM's Sensitive Data Guide?
- [ ] Are sensitive data stored only on approved platforms (Armis2, Lighthouse, Great Lakes)?
- [ ] Are all AI tools used appropriate for the data sensitivity level?

### B. AI Tool Use
- [ ] Has an AI usage statement been documented?
- [ ] Were only enterprise or local AI systems used for unpublished or identifiable data?
- [ ] Were model outputs independently verified by a human expert?
- [ ] Were limitations or hallucinations noted and corrected?

### C. Bias and Fairness
- [ ] Have potential sources of dataset bias been identified?
- [ ] Have subgroup performance metrics been evaluated?
- [ ] Have steps been taken to avoid harm or inequitable outcomes?

### D. Reproducibility
- [ ] Is all preprocessing logged with code, versions, and parameters?
- [ ] Are scripts, models, and data versioned?
- [ ] Are all AI-assisted steps documented and reproducible?

### E. Compliance and Institutional Oversight
- [ ] Have UM Research Integrity guidelines been followed?
- [ ] Has sensitive data processing complied with HIPAA, FERPA, or GDPR regulations as applicable?
- [ ] Are export control considerations relevant to this project?
- [ ] Is the project aligned with NIST AI RMF or ISO 42001 principles?

### F. Dissemination
- [ ] Does the manuscript or report clearly state how AI tools were used?
- [ ] Are all citations and factual claims verified independently?
- [ ] Is a model card or equivalent documentation included?

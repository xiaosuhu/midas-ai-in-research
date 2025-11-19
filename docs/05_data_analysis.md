# Data Analysis

AI-Enhanced Data Analysis for Research
1. Introduction

Why AI-based tools are transforming data analysis.

The idea of “analysis as conversation” — using AI to explore data, build models, and iterate quickly.

Positioning your MIDAS interface as a practical, low-barrier way for UM researchers to start.

2. Overview of the MIDAS Data Analysis Interface

What the interface does and what problems it solves.

Who it is designed for (researchers who don’t want to code from scratch / domain experts exploring models).

Workflow summary:
Upload data → explore → preprocess → model → evaluate → export results

2.1 Key Features

Support for tabular datasets (CSV, Excel).

Automatic preprocessing, missing value handling, and feature engineering.

Easy access to classical ML + AutoGluon deep learning models.

Integration with UM policy considerations (privacy, no PHI uploads).

Exportable results, plots, and reproducible scripts.

3. Public Data Resources

(This section becomes a major value-add for UM researchers.)

3.1 University of Michigan Sources

U-M Library data catalog

ICPSR

Michigan Medicine synthetic datasets

UM Open Datasets (e.g., MIDAS curated examples)

3.2 National / Global Public Datasets

Kaggle

NIH/NINDS/NIMH open neuroscience repositories (OpenNeuro)

PhysioNet

UCI Machine Learning Repository

HuggingFace datasets

Data.gov, NOAA, Census

arXiv metadata and scholarly datasets

fNIRS open datasets (if relevant to your domain)

3.3 Choosing the Right Dataset

Structured vs unstructured

Licensing considerations

Human-subjects considerations (deidentified vs synthetic)

4. Exploratory Data Analysis (EDA)
4.1 Uploading Data Into the MIDAS Interface

Supported file formats

Automatic type detection

First-pass diagnostics

4.2 Basic Data Cleaning

Missing data handling

Outlier detection

Standardization / normalization

Quick transformations

4.3 Visualization Tools

Automatic summary statistics

Correlation heatmaps

Distribution plots

5. AutoML With AutoGluon

(Your core topic — put real value here.)

5.1 Why AutoGluon?

Fast, strong baselines

Robust for small/medium datasets

Handles tabular data extremely well

Ensembling and model-stacking built in

Minimal code required

5.2 Supported Tasks

Classification

Regression

Time-series forecasting

Multimodal (if you want to include images or text)

5.3 Using AutoGluon Inside the MIDAS Interface

Default presets (quick start)

Advanced settings (hyperparameters, tuning)

Training logs & model leaderboard

Automatic feature importance

Exportable model artifacts

5.4 Practical Tips

Train/validation/test splits

Avoiding leakage

Interpretability (SHAP, feature importance)

When NOT to trust AutoML

6. Model Evaluation & Reporting
6.1 Metrics

Classification: accuracy, F1, ROC-AUC

Regression: RMSE, MAE

Time-series: MAPE, MASE

6.2 Interpretation Tools

Feature importance

Partial dependence plots

Error analysis

6.3 Exporting Outputs

Figures & plots

Model files

Summary reports

Reproducible scripts (Python notebook export)

7. Reproducibility and Good Practices

Keeping track of data sources, preprocessing steps

Auto-logging results (MLflow optional)

Documenting hyperparameters and random seeds

When to move from AutoML to custom modeling

8. Ethical & Policy Considerations

Do NOT upload PHI or restricted data

Using synthetic versions when possible

Data governance alignment with U-M policies

Reproducible open science

9. Case Studies (Optional, very helpful)

Example analysis using a Kaggle dataset

Example using a publicly available neuroscience dataset (e.g., OpenNeuro fNIRS/EEG)

Example using UM Library data

Show how the interface + AutoGluon accelerates discovery

10. Summary

AI-powered data analysis lowers barriers for researchers.

AutoGluon + a guided interface increases accessibility.

U-M’s ecosystem supports responsible, reproducible workflows.

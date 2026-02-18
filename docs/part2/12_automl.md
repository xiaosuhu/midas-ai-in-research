# AutoML with AutoGluon

AutoGluon is an open-source AutoML framework developed by Amazon that focuses on producing strong, practical machine learning baselines with minimal manual configuration. It is especially well-suited for researchers who want to move quickly from a dataset to a competitive model, without committing to extensive model engineering or hyperparameter tuning.

In the MIDAS AI Sandbox context, AutoGluon serves as a **rapid experimentation tool**: a way to test feasibility, benchmark performance, and identify promising directions before investing in custom modeling.

Reference: AutoGluon Documentation 

---

## 1. Why AutoGluon?

AutoGluon is designed around a simple principle: **strong performance by default**. Unlike many AutoML tools that require extensive configuration, AutoGluon emphasizes sensible defaults that work well across a wide range of research datasets.

Key strengths include:

- **Strong baseline models**  
  AutoGluon often outperforms hand-built “first-pass” models by combining multiple algorithms automatically.

- **Well-suited for small to medium tabular datasets**  
  Many academic datasets fall into this category, where AutoGluon excels without requiring massive compute resources.

- **Automatic stacking and ensembling**  
  Rather than relying on a single model, AutoGluon trains layered ensembles that improve robustness and generalization.

- **Minimal code and setup**  
  A complete training workflow can often be expressed in just a few lines of Python, lowering the barrier for non-ML experts.

For researchers, this means faster iteration, fewer implementation decisions, and more time spent interpreting results rather than tuning models.

---

## 2. Supported Tasks

AutoGluon supports several common research workflows out of the box:

- **Classification**  
  Binary and multi-class classification for structured (tabular) data, such as clinical labels, survey outcomes, or categorical annotations.

- **Regression**  
  Continuous outcome prediction, including behavioral scores, physiological measurements, or economic indicators.

- **Time-series forecasting**  
  Native support for forecasting tasks with temporal structure, including multiple time series and covariates.

- **Multimodal learning**  
  Combined modeling of text, images, and tabular data within a single framework, useful for richer datasets (e.g., clinical notes + structured fields).

This breadth allows AutoGluon to function as a single entry point for many applied research problems, rather than a narrowly scoped ML tool.

---

## 3. Using AutoGluon in the Interface

Within an AI-assisted analysis interface (such as the MIDAS AI Sandbox), AutoGluon typically exposes a small number of high-level controls rather than low-level model details.

Common interaction points include:

- **Presets**  
  Predefined configurations (e.g., “fast”, “medium”, “best quality”) that trade off runtime against performance. Presets are often sufficient for early-stage exploration.

- **Hyperparameter tuning**  
  Optional automated tuning that can be enabled when higher performance is needed, without manually specifying search spaces.

- **Leaderboard**  
  A ranked summary of trained models and ensembles, allowing users to compare performance transparently rather than treating AutoML as a black box.

- **Feature importance**  
  Built-in tools to estimate which features contribute most to predictions, supporting interpretability and hypothesis generation.

- **Model export**  
  Trained models can be saved and reused for inference, validation on new datasets, or downstream integration into pipelines.

The goal of the interface is not to expose every AutoGluon option, but to support **informed choice with minimal friction**.

---

## 4. Practical Tips

AutoML does not eliminate the need for good research practice. The following considerations are especially important when using AutoGluon:

- **Use proper data splits**  
  Ensure that training, validation, and test sets reflect the structure of the problem (e.g., subject-level splits for human data, time-aware splits for longitudinal data).

- **Avoid data leakage**  
  Features derived from future information, post-outcome variables, or aggregated labels can inflate performance unrealistically.

- **Balance performance with interpretability**  
  While ensemble models often perform best, simpler models may be preferable when explanation and transparency are primary goals.

- **Recognize when AutoML is insufficient**  
  AutoGluon is ideal for prototyping and benchmarking, but custom modeling may be required for:
  - Highly structured temporal or spatial data
  - Strong domain constraints
  - Mechanistic or theory-driven models

In practice, AutoGluon works best as a **starting point**, not an endpoint, in the research modeling lifecycle.

---

## References

 AutoGluon Documentation. https://auto.gluon.ai/stable/index.html

# Testing ML Feasibility with AutoGluon

Before committing significant time to building a custom machine learning pipeline, it helps to first ask a simpler question: is there a predictive signal in this data at all? AutoGluon is one of the most practical tools for answering that question quickly. It is an open-source AutoML framework developed by Amazon that trains and compares multiple models automatically, with almost no configuration required {cite}`erickson2020autogluon`.

In the context of research, AutoGluon is best understood as a rapid feasibility tool rather than a final modeling solution. The goal is to get a reliable performance baseline in minutes, so you can decide whether the problem is worth pursuing further, and if so, where to focus your attention {cite}`autogluon2024`.

---

## What AutoGluon Actually Does

When you call `TabularPredictor.fit()`, AutoGluon does several things in the background that would otherwise take considerable manual effort. It trains a range of model types (gradient boosting models like LightGBM and XGBoost, random forests, neural networks, and others), tunes hyperparameters automatically, and then combines the best-performing models into a stacked ensemble. The whole process is governed by a time budget you specify, so you stay in control of how much compute you spend.

The output is a ranked leaderboard showing how each model and ensemble performed on a held-out validation set. This transparency is one of the things that makes AutoGluon well-suited for research: you can see exactly what was tried and how each approach compared, rather than receiving a single number from an opaque process.

---

## Supported Problem Types

For the purposes of a feasibility test, AutoGluon handles three problem types that come up regularly in research.

Tabular prediction is the most common starting point. If your data is organized in rows and columns, such as clinical measurements, survey responses, administrative records, or experimental outcomes, AutoGluon can tackle classification (predicting categories) and regression (predicting continuous values) with the same interface. This is covered in depth in the tutorial below.

Time series forecasting is supported natively, including datasets with multiple series and external covariates. If your research involves longitudinal tracking, repeated measurements, or any data with a meaningful temporal structure, AutoGluon's `TimeSeriesPredictor` follows the same overall design pattern as the tabular interface.

Multimodal learning allows you to combine text fields, images, and structured columns in a single model. This is particularly relevant for clinical datasets that include both structured data and free-text notes, or social science datasets that combine survey responses with document content.

---

## Hands-On Tutorial: Predicting House Prices

The best way to understand what AutoGluon offers is to run through a complete example. The tutorial below uses a 500-row sample based on the California Housing dataset, originally from Pace and Barry (1997) {cite}`statlib_ca_housing`. Each row represents a census block group, and the task is to predict the median house value from neighborhood characteristics. This is a regression problem, but the workflow is identical for classification — you simply have a categorical label column instead of a continuous one.

You can run the full tutorial interactively in Google Colab by clicking the badge below. No local installation is needed, and everything runs in a free cloud environment.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/xiaosuhu/midas-ai-in-research/blob/v1.0-dev/docs/notebooks/autogluon_tabular_demo.ipynb)

---

### Setting Up

Start by installing AutoGluon. In Colab, this takes about 2 to 3 minutes:

```python
!pip install autogluon.tabular -q
```

Then load the dataset directly from the repository:

```python
import pandas as pd

DATA_URL = "https://raw.githubusercontent.com/xiaosuhu/midas-ai-in-research/v1.0-dev/docs/data/ca_housing_sample.csv"

df = pd.read_csv(DATA_URL)
print(f"Dataset shape: {df.shape}")
df.head()
```

The dataset has 500 rows and 9 columns. The first 8 are features (median income, house age, average rooms, average bedrooms, population, average occupancy, latitude, and longitude) and the last column `MedHouseVal` is the prediction target, representing median house value in hundreds of thousands of USD.

---

### Splitting the Data

A key principle in any feasibility test is holding back some data for final evaluation before training begins. AutoGluon does its own internal validation during training, but that internal split should not be confused with your test set. The test set must stay completely untouched until you are ready to report final performance:

```python
from sklearn.model_selection import train_test_split

train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

print(f"Training rows: {len(train_df)}")
print(f"Test rows:     {len(test_df)}")
```

For datasets where samples are not independent — for example, multiple measurements from the same research participant, or data collected over time — a simple random split like this is not appropriate. Chapter 14 covers validation strategies for these situations in more detail.

---

### Training the Model

This is the core of the workflow. We tell AutoGluon three things: which column is the target, what metric to optimize, and how much time it can use:

```python
from autogluon.tabular import TabularPredictor

predictor = TabularPredictor(
    label="MedHouseVal",
    eval_metric="rmse",
    path="autogluon_housing_model"
).fit(
    train_data=train_df,
    time_limit=120,
    presets="medium_quality"
)
```

The `time_limit=120` gives AutoGluon 2 minutes, which is usually enough for a first feasibility pass. The `presets` parameter lets you trade runtime for performance: `"medium_quality"` is a reasonable default, while `"best_quality"` enables more aggressive ensembling and hyperparameter search at the cost of longer training time.

One thing worth noting is that you do not need to specify the problem type. AutoGluon infers from the label column whether this is a regression or classification task. You also do not need to encode categorical features, handle missing values, or scale numeric columns, because those steps are handled internally.

---

### Reading the Leaderboard

Once training finishes, the leaderboard is one of the most informative artifacts to examine:

```python
leaderboard = predictor.leaderboard(test_df, silent=True)
leaderboard
```

The leaderboard ranks every model and ensemble that was trained, showing both validation performance (from AutoGluon's internal split) and test performance (from your held-out set). A few things to look for: check whether the ensemble models at the top outperform the best individual model (if the gap is small, a simpler model may be preferable for interpretability), look for models with good validation performance but poor test performance (a sign of overfitting), and note training times if compute cost matters for your use case.

---

### Evaluating on the Test Set

To get the final summary of performance on your held-out data:

```python
performance = predictor.evaluate(test_df)
print(performance)
```

For regression, the primary metric is RMSE. Since `MedHouseVal` is in hundreds of thousands of USD, an RMSE of 0.5 means predictions are off by about $50,000 on average. Whether that is acceptable depends entirely on your research question, not on any universal standard.

---

### Understanding Which Features Matter

For many research applications, the feature importance is more interesting than the prediction itself. It tells you which variables carry the most predictive information, which can help generate hypotheses, flag potential data leakage, or identify redundant measurements:

```python
importance = predictor.feature_importance(test_df)
importance
```

AutoGluon estimates importance using permutation: it shuffles each feature one at a time and measures how much model performance drops. A larger drop means the feature was doing more work. You can visualize this to make the ranking easier to read:

```python
import matplotlib.pyplot as plt

importance_sorted = importance["importance"].sort_values()

fig, ax = plt.subplots(figsize=(7, 5))
importance_sorted.plot(kind="barh", ax=ax, color="steelblue")
ax.set_xlabel("Permutation Importance")
ax.set_title("Feature Importance — AutoGluon Best Model")
ax.axvline(0, color="gray", linewidth=0.8)
plt.tight_layout()
plt.show()
```

In this dataset, median income and geographic location tend to dominate. If you ran this on your own research data and saw a variable you did not expect at the top of the list, that would be a reason to pause and investigate. It could be a meaningful finding, or it could indicate that a feature is inadvertently encoding the outcome.

---

### Saving and Reloading a Model

Reproducibility matters in research. If you want to reuse a trained model later — for validation on a new cohort, for sharing with collaborators, or for comparison in a future study — you can save and reload it:

```python
# The model is already saved to the path you specified in TabularPredictor()
# To reload it later:
reloaded_predictor = TabularPredictor.load("autogluon_housing_model")
predictions = reloaded_predictor.predict(test_df)
```

Saving the model alongside your data and notebook means someone else can reproduce your results without rerunning the full training process.

---

## Going Further: Time Series and Multimodal

If your research data has a temporal structure — repeated measurements, longitudinal follow-up, or any data indexed by time — AutoGluon's `TimeSeriesPredictor` follows the same overall design pattern with some additional arguments for the time column and forecast horizon. The [AutoGluon time series documentation](https://auto.gluon.ai/stable/tutorials/timeseries/index.html) provides a complete walkthrough.

For datasets that mix structured columns with text or images, `MultiModalPredictor` handles the combination automatically. This can be useful for datasets that include clinical notes alongside lab values, or survey instruments that combine rating scales with open-ended text responses. See the [multimodal tutorials](https://auto.gluon.ai/stable/tutorials/multimodal/index.html) in the AutoGluon documentation for examples.

In both cases, the core idea is the same as what you practiced above: define your target, set a time budget, and inspect the results before deciding whether deeper investment is warranted.

---

## Research Considerations

AutoML lowers the barrier to getting a model running, but it does not lower the bar for responsible research practice.

Data leakage is the most common pitfall. Features derived from future information, variables that are proxies for the outcome, or aggregations that inadvertently incorporate test data can all produce inflated performance estimates that do not hold up in practice. If your results look surprisingly good, leakage is the first thing to investigate.

The test set is a one-time measurement. Once you evaluate on the test set, any subsequent changes to your model or features should ideally trigger a fresh train/test split. Repeatedly evaluating on the same test set and adjusting based on those results is a form of overfitting, even if the decisions feel subjective.

AutoGluon is a starting point, not an endpoint. The feasibility test is meant to answer "is there signal here worth pursuing," not "what is my final model." If the results look promising, a custom pipeline with more careful feature engineering and domain-informed design will typically outperform AutoGluon's defaults on a specific problem.

On compute and data privacy: AutoGluon can be run locally, on the Great Lakes cluster, or in the MIDAS AI Sandbox. For any data covered by HIPAA or other data governance policies, make sure you are using an approved environment. Do not upload sensitive data to a public Colab notebook or a shared Binder instance. Chapter 8 covers data access policies and approved computing environments in more detail.

---

## References

```{bibliography}
:filter: docname in docnames
```

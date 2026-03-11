# AutoGluon Fundamentals: Tabular Prediction

:::{admonition} What you will learn
:class: tip

By the end of this chapter and its companion notebook, you will know how to quickly test whether there is a predictive signal in your tabular data, how `TabularPredictor` handles preprocessing and model selection automatically, how to read the leaderboard and evaluate model performance on a held-out test set, and how to use feature importance to interpret what the model is actually responding to.
:::

Before committing significant time to building a custom machine learning pipeline, it helps to first ask a simpler question: is there a predictive signal in this data at all? AutoGluon is one of the most practical tools for answering that question quickly. It is an open-source AutoML framework developed by Amazon that trains and compares multiple models automatically, with almost no configuration required {cite}`erickson2020autogluon`.

In the context of research, AutoGluon is best understood as a rapid feasibility tool rather than a final modeling solution. The goal is to get a reliable performance baseline in minutes, so you can decide whether the problem is worth pursuing further, and if so, where to focus your attention {cite}`autogluon2024`.

---

## What AutoGluon Actually Does

Regardless of which problem type you are working with, AutoGluon follows the same underlying approach. It starts with automated preprocessing — handling missing values, encoding categorical variables, and generating additional features where appropriate, so you do not need to do this manually before handing data over. It then searches across a range of model families (gradient boosting, random forests, neural networks, and others), tunes hyperparameters within each, and combines the best-performing results into a stacked ensemble. Everything runs within a time budget you control.

Each problem type has its own predictor class — `TabularPredictor` for row-and-column data, `TimeSeriesPredictor` for temporally indexed data, and `MultiModalPredictor` for mixed text, image, and tabular inputs — but the design pattern is the same across all three: specify your target, set a time limit, and inspect what came out.

The output is always a ranked leaderboard showing how each model and ensemble performed, rather than a single opaque number. This transparency is what makes AutoGluon particularly useful in a research context.

---

## Supported Problem Types

AutoGluon handles three problem types that come up regularly in research.

**Tabular prediction** is the most common starting point. If your data is organized in rows and columns — clinical measurements, survey responses, administrative records, experimental outcomes — AutoGluon can tackle both classification (predicting categories) and regression (predicting continuous values) with the same interface. This chapter's tutorial covers tabular prediction in depth.

**Time series forecasting** is supported natively, including datasets with multiple series and external covariates. If your research involves longitudinal tracking, repeated measurements, or any data with a meaningful temporal structure, `TimeSeriesPredictor` is the right entry point.

**Multimodal learning** allows you to combine text, images, and structured columns in a single model — useful for datasets that mix clinical notes with lab values, or survey instruments that include both rating scales and open-ended responses.

---

## Tutorial: Predicting House Prices

The tutorial uses a 500-row sample based on the California Housing dataset, originally from Pace and Barry (1997) {cite}`statlib_ca_housing`. Each row represents a census block group, and the task is to predict median house value from neighborhood characteristics — a regression problem. The workflow is identical for classification; only the label column and evaluation metric differ.

All code, explanatory notes, and hands-on exercises live in the Colab notebook. Clicking the badge opens a temporary session — click "Copy to Drive" inside Colab to save your own copy.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/xiaosuhu/midas-ai-in-research/blob/v1.0-dev/docs/notebooks/autogluon_tabular_demo.ipynb)

### The Core Call

The full training workflow comes down to a few lines. You tell AutoGluon which column is the target, what metric to optimize, and how much time it can use:

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

AutoGluon infers the problem type from the label column and handles all preprocessing internally. The `time_limit` is the single most important lever — two minutes is enough for a first feasibility pass, and you can increase it later if the results look promising.

### What the Leaderboard Shows

Once training finishes, the leaderboard ranks every model and ensemble that was trained, showing test and validation scores side by side. Here is an example of what you would typically see for a tabular regression task:

```{image} ../_static/autogluon_leaderboard_example.png
:alt: Example AutoGluon leaderboard for tabular regression, showing model rankings by RMSE score
:width: 100%
:align: center
```

AutoGluon reports RMSE as a negative number so that higher values always mean better performance — a convention it applies consistently across all metrics. The ensemble (`WeightedEnsemble_L2`) typically sits at the top. If a single model is close behind, that simpler model may be worth preferring when interpretability matters more than squeezing out the last bit of performance.

The notebook walks through each step in detail — data splits, metric selection, training, the leaderboard, evaluation, and feature importance — with explanatory notes and hands-on exercises at the end.

---

## What's Coming: Time Series and Multimodal Notebooks

This chapter focused on tabular prediction, which is the right starting point for most research datasets. Two additional notebooks are planned to extend the same feasibility-testing workflow to other data types.

The **time series notebook** will walk through `TimeSeriesPredictor` using a longitudinal research dataset, covering how to specify the time column and item ID, set a forecast horizon, and interpret the resulting metrics. It will also address how to handle irregular time intervals and missing observations, which are common in clinical and social science data.

The **multimodal notebook** will demonstrate `MultiModalPredictor` combining structured fields with text, using a dataset that pairs tabular features with short text descriptions. It will include a GPU-enabled example using MNIST image classification, taking advantage of the free GPU runtime available in Colab, to show how the same interface scales to image data with minimal code changes.

Both notebooks will follow the same structure as the tabular tutorial: load data, split, fit, inspect the leaderboard, evaluate, and check feature importance — so once you are comfortable with one, the others will feel familiar.

---

## Frequently Asked Questions

**Does AutoGluon support R?**
Not natively — AutoGluon is a Python-only framework. If your workflow is primarily in R, the most practical path is to run AutoGluon in Python for the modeling step, then export the predictions or feature importance as a CSV and continue your analysis in R. Technically, R users can call Python via the `reticulate` package, but this adds complexity and is not the recommended workflow.

**Can I rank models by two metrics at the same time?**
The leaderboard only ranks by the single `eval_metric` you set at training time. However, once you have the leaderboard as a DataFrame you can build a combined ranking yourself — normalize each metric to a 0-1 range and take a weighted average. The notebook's "Common Questions" section shows a working example of this.

**The ensemble always wins — how do I evaluate individual models?**
By default, `predictor.evaluate()` reports the performance of the best model (the ensemble). To evaluate any individual model, pass its name from the leaderboard using the `model` argument:

```python
predictor.evaluate(test_df, model="LightGBM_BAG_L1", auxiliary_metrics=True)
```

You can loop through all model names to build a full comparison table across multiple metrics, which lets you decide whether the ensemble's edge over a simpler model is worth the interpretability trade-off. The notebook walks through both approaches.

---

## Research Considerations

AutoML lowers the barrier to getting a model running, but it does not lower the bar for responsible research practice.

Data leakage is the most common pitfall. Features derived from future information, variables that are proxies for the outcome, or aggregations that inadvertently incorporate test data can all produce inflated performance estimates that do not hold up in practice. If your results look surprisingly good, leakage is the first thing to investigate.

The test set is a one-time measurement. Once you evaluate on it, any subsequent changes to your model or features should ideally trigger a fresh split. Repeatedly adjusting based on the same test results is a form of overfitting, even when the decisions feel subjective.

AutoGluon is a starting point, not an endpoint. The feasibility test answers "is there signal here worth pursuing," not "what is my final model." If the results look promising, a custom pipeline with careful feature engineering and domain-informed design will typically outperform AutoGluon's defaults on your specific problem.

On data privacy: for any data covered by HIPAA or other governance policies, use an approved environment — **the Armis2 HPC Cluster**, or a **local installation**. Do not upload sensitive data to a public Colab notebook. Chapter 8 covers approved computing environments in more detail.

---

## References

```{bibliography}
:filter: docname in docnames
```

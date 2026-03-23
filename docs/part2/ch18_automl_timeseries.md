# Chapter 18: Time Series Forecasting with AutoGluon

:::{admonition} What you will learn
:class: tip

By the end of this chapter and its companion notebook, you will be able to recognize when a research question is genuinely a forecasting problem, format longitudinal or panel data for `TimeSeriesPredictor`, set a forecast horizon and interpret quantile outputs with prediction intervals, and understand why temporal data leakage matters and how AutoGluon handles it for you.
:::

Some research datasets do not just describe a snapshot — they track how something changes over time. Repeated physiological measurements, weekly survey responses, yearly economic indicators, hourly sensor readings: all of these share a structure that tabular prediction is not designed for. When the goal is to predict future values based on past observations, the problem is called forecasting, and it calls for a different set of tools.

This chapter introduces `TimeSeriesPredictor`, AutoGluon's forecasting module, using the same feasibility-testing philosophy from the tabular chapter. The goal is not to build a production forecasting system. It is to quickly find out whether there is enough temporal signal in your data to justify investing further, and to understand what the output is actually telling you {cite}`autogluon_ts2023`.

---

## Is This a Forecasting Problem?

Not every dataset with a time column is a forecasting problem. This is worth pausing on before you write any code, because the answer shapes everything that follows.

A **forecasting problem** asks: given what I have observed up to now, what will the values look like at future time points? The output is a prediction over a future window.

But many research questions that involve time are not really asking that. A study comparing how two groups change over a six-week intervention period is usually asking a causal question, not a predictive one, and standard regression or mixed-effects models are the right tools. If your research question is "what will happen next" or "how much will we need," then forecasting is appropriate. If it is "does X cause Y" or "how do groups differ," forecasting is probably not the right frame.

If you decide forecasting is right for your problem, the next question is: over what horizon? That is a research decision, not a technical one. For a monthly health indicator, maybe you want a three-month-ahead forecast. For a sensor dataset, maybe 24 hours. `TimeSeriesPredictor` calls this `prediction_length`, and it is the first parameter you will set.

---

## How Time Series Differs from Tabular Prediction

In tabular prediction, each row is an independent observation and the order of rows does not matter. In time series forecasting, the opposite is true. Rows are ordered, and the order is the whole point. The value at time *t* depends on values at *t-1*, *t-2*, and beyond.

This has one major consequence for how you evaluate your model: **the train/test split must respect time**. You train on earlier data and test on later data, never the reverse. A random split would let the model see future observations during training, which makes performance look unrealistically good. This is called temporal data leakage, and it is the most common pitfall in time series modeling {cite}`hyndman2021forecasting`.

AutoGluon handles this correctly by default. You specify a forecast horizon, and it reserves the most recent `prediction_length` time steps of each series for validation. You do not need to manage the split yourself.

A second difference is the output format. Tabular prediction gives you a single predicted value per row. Time series forecasting gives you a **distribution** over future values at each step, specifically a set of quantiles (by default the 10th, 50th, and 90th percentiles). The 50th percentile is the point forecast; the others define a prediction interval. This is genuinely more useful for research because it forces you to communicate uncertainty rather than presenting a single number as ground truth.

---

## Data Format: Getting Your Data into Shape

`TimeSeriesPredictor` expects data in **long format**, with three required columns {cite}`autogluon_ts2023`:

| Column | Role | Example values |
|---|---|---|
| `item_id` | Unique identifier for each series | `"patient_01"`, `"site_A"` |
| `timestamp` | Timestamp of the observation | `2023-01-01`, `2023-01-08` |
| `target` | The value you want to forecast | `72.4`, `1320` |

The "item" concept is important to understand. AutoGluon is designed for **panel forecasting**, meaning multiple related series measured over time. Each unique `item_id` is one series. If you are studying 50 patients and measuring heart rate weekly, each patient is one item. If you have only one location measuring air quality, you still have one item. Single-series forecasting works, but some of the global deep learning models perform better when they can learn patterns across many series.

Most researchers store longitudinal data in **wide format**, where each row is a subject and each column is a time point. You will need to reshape this into long format before calling AutoGluon. The notebook shows how to do this with `pandas.melt()`.

Here is what the difference looks like:

**Wide format (what you might have):**

| subject_id | week_1 | week_2 | week_3 |
|---|---|---|---|
| patient_01 | 72 | 74 | 70 |
| patient_02 | 80 | 78 | 82 |

**Long format (what AutoGluon needs):**

| item_id | timestamp | target |
|---|---|---|
| patient_01 | 2023-01-01 | 72 |
| patient_01 | 2023-01-08 | 74 |
| patient_01 | 2023-01-15 | 70 |
| patient_02 | 2023-01-01 | 80 |
| ... | ... | ... |

Column names do not have to be exactly `item_id`, `timestamp`, and `target`. You tell AutoGluon which columns play which role. But the structure must be long format.

---

## What AutoGluon Tries: The Model Zoo

One of the strengths of `TimeSeriesPredictor` is that it runs a wide range of models and lets you compare them on your actual data. The models fall into four families {cite}`autogluon_ts2023`.

**Classical statistical models** (ETS, ARIMA, Theta, Naive, SeasonalNaive) are fast to run and interpretable. They are fit independently to each series, which makes them robust on small datasets. ETS models trend and seasonality explicitly; ARIMA captures autocorrelation structure. SeasonalNaive simply repeats the last observed seasonal cycle, which turns out to be a surprisingly strong baseline. If a sophisticated model barely beats SeasonalNaive, that tells you something important about how much learnable signal is in your data.

**Tree-based models** (DirectTabular, RecursiveTabular, built on LightGBM) treat forecasting as a tabular regression problem by creating lag features from the history. These are efficient and often competitive, especially when you have many series with relatively regular patterns.

**Deep learning models** (DeepAR, Temporal Fusion Transformer) learn global patterns across all series jointly. They can capture complex temporal dependencies and handle covariates, but they need more data and more training time to pay off. On a small dataset, they often do not beat the classical methods.

**Foundation model** (Chronos-2) is something qualitatively different. It is a pretrained model trained on hundreds of millions of real and synthetic time series observations, and it can produce forecasts for entirely new datasets without any training at all. This is called zero-shot forecasting {cite}`ansari2024chronos`. In practice, Chronos-2 often produces competitive results on research datasets even when the dataset is small, because it brings knowledge from pretraining rather than fitting from scratch.

The ensemble combines the best-performing models, weighting their forecasts to minimize the validation error. It usually sits at the top of the leaderboard, though the gap to individual models varies by dataset.

---

## Tutorial: Forecasting Monthly Time Series

The tutorial uses a 10-series subset of the M4 forecasting competition dataset, specifically a collection of monthly series {cite}`makridakis2020m4`. The M4 dataset is a widely used benchmark in the forecasting literature, covering series from domains including demographics, finance, industry, and economics. The figure below shows all ten series so you can see what you are working with before any code runs.

```{figure} ../_static/m4_sample_series.png
:alt: Ten M4-style monthly time series showing variety in scale, trend, seasonality, and length. Solid lines are the training history; dashed lines and gray shading mark the last 12 months held out for testing.
:width: 100%
:align: center

The ten series in the tutorial dataset. Notice how they differ in scale (M3 reaches into the tens of thousands while M6 stays below 70), trend direction (M9 grows rapidly, M4 declines), and seasonal amplitude (M8 is dominated by seasonality while M2 shows very little). This variety is intentional — it mirrors the kind of heterogeneity you would see in a real panel of research series, and it is why AutoGluon's multi-model approach is useful here.
```

All code, explanatory notes, and exercises live in the companion notebook. Click the badge to open a temporary Colab session, then click "Copy to Drive" to save your own copy.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/xiaosuhu/midas-ai-in-research/blob/v1.0-dev/docs/notebooks/autogluon_timeseries_demo.ipynb)

### The Core Call

The forecasting workflow is three steps: create the predictor, call `fit()`, call `predict()`.

```python
from autogluon.timeseries import TimeSeriesPredictor

predictor = TimeSeriesPredictor(
    prediction_length=12,
    target="target",
    eval_metric="MASE",
    path="autogluon_ts_model"
).fit(
    train_data,
    time_limit=120,
    presets="medium_quality"
)
```

`prediction_length=12` means you want forecasts 12 steps ahead. For monthly data, that is one year. `eval_metric="MASE"` tells AutoGluon which metric to optimize and rank models by. Two minutes is enough for a first feasibility pass.

### Reading the Leaderboard

The time series leaderboard looks similar to the tabular one. Every model that ran is ranked by the evaluation metric, with higher always meaning better (AutoGluon flips the sign on error metrics to enforce this convention). You will typically see a mix of classical models, tree-based models, and the ensemble near the top.

One pattern worth watching: if SeasonalNaive ranks near the top, your series may have strong seasonal structure but limited additional signal for complex models to capture. If deep learning models trail far behind the classical methods, you likely have too few observations for them to learn effectively. These are useful signals for your next modeling decision, not failures of the tool.

### Understanding MASE

MASE (Mean Absolute Scaled Error) is the default evaluation metric and the one used in most forecasting benchmarks {cite}`hyndman2021forecasting`. The key intuition is that it compares your model against a naive seasonal baseline, specifically a forecast that repeats the last observed seasonal value. A MASE of 1.0 means your model performs exactly as well as that naive baseline. Below 1.0 means you are beating it. Above 1.0 means the model has not learned much useful from the data.

Because MASE is scale-free, it does not depend on the units of your target variable, which makes it especially useful when you have multiple series with different scales.

AutoGluon reports it as a negative number in the leaderboard (so that higher is always better). A leaderboard value of `-0.82` corresponds to a MASE of `0.82`, meaning the model is 18% better than the seasonal naive baseline.

Other metrics worth knowing: SMAPE (symmetric mean absolute percentage error) if you want something easier to explain to collaborators, and WQL (weighted quantile loss) if you care about the accuracy of your uncertainty estimates rather than just the point forecast.

### What the Forecast Output Looks Like

Unlike tabular prediction, the output of `predict()` is a DataFrame with one row per time step per series, and multiple columns for different quantile levels. By default you get the 10th, 50th, and 90th percentiles:

```
                        0.1      0.5      0.9
item_id  timestamp
M1       2023-01-01    112.3    118.7    124.9
         2023-02-01    109.8    116.2    122.7
         ...
```

The 50th percentile is your point forecast. The range between the 10th and 90th percentiles is an 80% prediction interval: in a well-calibrated model, the true future value should fall within this range about 80% of the time. Visualizing this interval alongside the historical data is one of the most informative things you can do with a forecast. The width of the interval tells you how confident the model is and how that confidence changes over the forecast horizon.

---

## Practical Notes for Research Data

**Short series.** Most models need a history length meaningfully longer than the forecast horizon. A rough rule of thumb is that your history should be at least two to three times longer than `prediction_length`. If you have 15 monthly observations and want a 12-month forecast, deep learning models will struggle and classical methods are your best option.

**Missing observations.** AutoGluon handles missing values natively without requiring you to impute them first. If your series has gaps, you can pass the data in as-is.

**Irregular time intervals.** AutoGluon infers the frequency of your series automatically from the timestamps. If your timestamps are not evenly spaced, you will need to either regularize them or resample to a fixed frequency before passing data in.

**Single series.** If you have only one series, you can still use `TimeSeriesPredictor` by setting `item_id` to a constant value for all rows. Classical and Chronos models work well in this setting.

**Covariates.** If you have external variables that are known in advance for the forecast period, such as seasonal indicators, treatment assignments, or scheduled events, you can pass these as `known_covariates`. Models that support covariates (like Temporal Fusion Transformer) will incorporate them automatically. The notebook shows a basic example.

---

## Frequently Asked Questions

**How is this different from using the `forecast` package in R?**

The R `forecast` package gives you precise control over a single model, usually ETS or ARIMA, with rich diagnostic tools {cite}`hyndman2021forecasting`. AutoGluon trades that control for breadth: it runs many model families automatically and lets you compare them. The two approaches are complementary. AutoGluon is useful for a quick feasibility pass across many models; a dedicated tool like R's `forecast` package is better when you have chosen a direction and want to go deeper with one model.

**My dataset has hundreds of series. Will this take forever?**

With `time_limit=120` and `presets="medium_quality"`, two minutes is usually enough for a first pass even on moderate-sized panels. If you have a large panel and limited compute, try `presets="fast_training"` for a first run. It focuses on faster models and gives you a leaderboard quickly.

**Should I fine-tune Chronos rather than just using zero-shot?**

For a feasibility test, zero-shot Chronos is usually sufficient. If the results look promising and you want to squeeze more accuracy, AutoGluon supports fine-tuning Chronos on your specific dataset. Fine-tuning is most worthwhile when you have at least a few hundred observations and your series have patterns that differ from what general pretraining data covers {cite}`ansari2024chronos`.

**Can I use this to predict a binary event over time?**

`TimeSeriesPredictor` is designed for forecasting continuous values, not event prediction. If your outcome is binary, you would typically reformulate this as a survival analysis or a time-to-event model, which is outside AutoGluon's current scope.

---

## Research Considerations

The same cautions from the tabular chapter apply here, and time series adds a few of its own.

**Temporal leakage is easy to miss.** Beyond the train/test split, watch for features derived from the target across time. If you include a rolling average of your target as a covariate, and that average incorporates future observations, you have a leak. AutoGluon does not protect you from leakage in covariates you supply.

**Stationarity and structural breaks.** Classical models like ARIMA assume the statistical properties of the series are stable over time. If your data contains a regime change, such as a policy shift, an intervention, or an external shock, a model trained before the break may forecast poorly after it. Looking at your raw series before modeling is always worth the time.

**Forecasts are not causal.** A model that forecasts well does not tell you why the series behaves as it does. If the goal is to evaluate an intervention or understand a mechanism, forecasting tools alone are not sufficient.

**On data privacy.** For any data covered by HIPAA or other governance policies, run in an approved institutional environment or a local installation, and do not upload sensitive data to a public Colab notebook. [Chapter 13](ch13_computing_resources.md) covers computing options in more detail.

```{admonition} If You're at U-M
:class: note

Approved options include Great Lakes for general sensitive workloads and Armis2 for HIPAA-covered data. See [AI Resources at the University of Michigan](../part4/ch27_um_resources.md).
```

---

*Last reviewed: March 2026. Tool-specific content in this chapter refers to AutoGluon 1.x. If you notice outdated content, [open an issue on GitHub](https://github.com/xiaosuhu/midas-ai-in-research/issues).*

---

## References

```{bibliography}
:filter: docname in docnames
```

# Time Series Forecasting with AutoGluon

Many research datasets have a temporal dimension — repeated measurements over time, longitudinal patient follow-up, economic indicators tracked across quarters, or sensor readings collected at regular intervals. When the goal is to predict future values based on past observations, you are working with a forecasting problem, and standard tabular predictors are not the right tool. AutoGluon's `TimeSeriesPredictor` is designed specifically for this structure.

This chapter follows the same feasibility-testing philosophy as the tabular chapter. The goal is not to build a production forecasting system, but to quickly answer: is there enough temporal signal in this data to justify a deeper investment?

---

## How Time Series Differs from Tabular Prediction

In tabular prediction, each row is an independent observation. In time series forecasting, rows are ordered and the order matters — the value at time *t* depends on values at *t-1*, *t-2*, and so on. This means the train/test split must respect time: you always train on earlier data and test on later data, never the reverse. A random split would leak future information into training and produce misleadingly optimistic results.

AutoGluon handles this correctly by default. You specify a forecast horizon — how many steps ahead you want to predict — and AutoGluon reserves the most recent portion of each series for validation.

---

## Coming Soon

This chapter is under active development. The planned tutorial will walk through:

- Formatting your data for `TimeSeriesPredictor` (the required `item_id`, `timestamp`, and `target` columns)
- Setting a forecast horizon and choosing an evaluation metric (MASE, SMAPE, and others)
- Interpreting the time series leaderboard, which includes models like DeepAR, Temporal Fusion Transformer, and classical baselines like ETS and ARIMA
- Handling irregular time intervals and missing observations
- Comparing AutoGluon's ensemble forecast against simpler baselines

A companion Colab notebook with a longitudinal research dataset will be linked here when ready.

In the meantime, the [AutoGluon time series documentation](https://auto.gluon.ai/stable/tutorials/timeseries/index.html) provides a complete walkthrough of the API.

---

## References

```{bibliography}
:filter: docname in docnames
```

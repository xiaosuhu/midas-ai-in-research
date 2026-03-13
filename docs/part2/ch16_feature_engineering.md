# Feature Engineering for Research Data

:::{admonition} What You Will Learn
:class: tip

- What feature engineering is and why it still matters even when AutoML handles preprocessing
- How to transform numeric variables, encode categories, and build derived features for tabular data
- How raw text and images become model inputs, and when to do this manually versus leaning on pretrained models
- The specific feature engineering patterns that matter most for time series data
- How to decide when engineering features yourself is worth the effort versus letting AutoML take care of it
:::

---

## Where You Are in the Pipeline

You spent Chapter 11 learning what your data actually contains, column by column. Chapter 12 walked through the decisions that turned raw, messy data into something clean and trustworthy. Now the question is: what shape should that cleaned data be in before a model sees it?

That is what feature engineering is about. At its core, it is the process of transforming your cleaned variables into representations that are more useful for learning. Sometimes that means applying a mathematical transformation to a skewed distribution. Sometimes it means combining two columns into a single, more informative one. Sometimes it means converting raw text into a structured numeric representation. In each case, the idea is the same: you are helping the model see what you already know.

This chapter covers the most common patterns across four data types: tabular, text, time series, and images. It is not exhaustive, and it deliberately does not try to be. The goal is to give you a working vocabulary and a clear sense of when each technique is appropriate, so you can make informed decisions rather than applying transformations mechanically {cite}`zheng2018feature`.

---

## Does This Still Matter If You Are Using AutoML?

This is a fair question to ask before going further. Chapter 14 introduces AutoGluon, which handles quite a lot of preprocessing automatically. It encodes categorical variables, manages missing values, and in some cases generates additional features without any input from you. So why spend time on this chapter at all?

The short answer is that AutoML works with what you give it. It cannot know that a raw measurement in your dataset should be log-transformed because the underlying biological process is multiplicative, not additive. It does not know that two date columns in your clinical dataset together capture time since last hospitalization, which turns out to be more meaningful than either column alone. It does not know that "rural" and "suburban" should be collapsed into a single category for your research question, even though they appear distinct in the raw data.

This is where your domain knowledge makes a real difference. AutoML handles the mechanical layer well. Feature engineering at its best is about encoding the conceptual layer, the relationships and patterns you already understand about your field, into the structure of the data before a model ever touches it. That part does not get automated.

That said, not everything needs to be done manually. Part of becoming comfortable with this step is developing a sense of what the model will likely figure out on its own versus what genuinely benefits from your input. The last section of this chapter returns to that question directly.

---

## Tabular Data

Most researchers start with tabular data: rows and columns, one observation per row, one variable per column. This is the most common format across health sciences, social sciences, economics, ecology, and many other fields. The feature engineering patterns here are well established {cite}`hastie2009elements`.

### Numeric Transformations

Not all numeric variables are well-behaved for modeling purposes. The most common issue is skewness: a distribution with a long tail in one direction, where most values cluster near zero but a handful of extreme values stretch the scale. Income, population counts, gene expression levels, and hospital length of stay are common examples. Models that rely on distance or linear relationships tend to perform worse when variables are highly skewed, because the extreme values distort what the model learns.

The most common fix is a log transformation. If your variable is right-skewed and takes only positive values, `log(x)` or `log(x + 1)` usually brings the distribution closer to symmetric. The interpretation changes slightly (you are now working with log-dollars or log-counts), but the model often learns more meaningful patterns from the transformed version.

Standardization is a separate transformation with a different purpose. When you subtract the mean and divide by the standard deviation, you rescale a variable so it has a mean of zero and a standard deviation of one. This does not change the shape of the distribution. What it does is put variables on a common scale, which matters for any model that is sensitive to the magnitude of inputs, including most neural networks and regularized regression methods. Gradient boosting models like the ones AutoGluon uses by default are less sensitive to scale, but it is still good practice when you are mixing variables with very different units.

One thing to be careful about: if you are building a model you will eventually validate on held-out data, fit any scaling parameters (mean, standard deviation) on your training data only, and apply them to your test data. Fitting on the full dataset before splitting is a form of data leakage, and it leads to overly optimistic performance estimates.

### Encoding Categorical Variables

Models cannot take string values as input. A column containing "urban", "suburban", and "rural" needs to be converted into numbers. How you do that conversion matters.

The most common approach is one-hot encoding, where each category becomes its own binary column. A three-category variable becomes three columns, each containing 0 or 1. This is a natural choice when the categories have no meaningful order. One-hot encoding is safe and interpretable, but it can get unwieldy when a variable has many categories. A column with 50 possible values becomes 50 columns, which creates a sparse representation and can slow down training.

When categories do have a natural order, ordinal encoding is usually better. A variable like "low/medium/high" or "freshman/sophomore/junior/senior" has an inherent sequence, and mapping those to 1/2/3/4 preserves that information. One-hot encoding would throw it away.

Target encoding is worth knowing about for high-cardinality situations: you replace each category with the average value of the outcome variable for that category. This can be powerful, but it is also easy to overfit on, especially with small samples. If you use it, do so with care and validate the results.

### Derived Features from Domain Knowledge

This is where the real payoff often comes from. Derived features are new columns you create by combining or transforming existing ones based on what you know about the problem.

A few common patterns: computing ratios (body mass index from height and weight; revenue per employee from two financial columns), computing time differences (days between two date columns; years since a policy change), creating indicator variables for meaningful thresholds (a binary flag for whether a patient's value exceeded a clinical cutoff), and simplifying high-cardinality variables by grouping rare categories together.

The key with derived features is that they should mean something. The test is whether you can explain in one sentence why this new variable captures something the individual input columns do not. If you cannot, it is probably not worth adding.

As a practical note, when you are working with AI to generate these features, describing the research context is more valuable than describing the columns. "I have date of diagnosis and date of first treatment; I want to calculate days to treatment initiation" will get you further than "I have two date columns."

---

## Text Data

When a dataset includes free-text fields, survey responses, clinical notes, abstracts, or any other unstructured language, you need to convert that text into a numeric form before a model can use it.

The conceptual spectrum runs from simple to rich. On the simple end is bag-of-words: you count how many times each word appears in a document and use those counts as features. TF-IDF (term frequency-inverse document frequency) is a refinement that downweights words that appear everywhere (like "the" or "and") and upweights words that appear often in a specific document but rarely elsewhere. These approaches are computationally cheap, easy to interpret, and often surprisingly effective for classification tasks where the vocabulary itself is informative.

On the richer end are embeddings. These are dense vector representations, typically hundreds of numbers per word or document, that capture semantic relationships. Words with similar meanings end up with similar vectors. Documents on similar topics end up in similar regions of the vector space. These representations come from pretrained language models, and in most practical research applications you are using them rather than training them from scratch.

The practical implication is that for most text feature engineering tasks today, you are choosing a pretrained model and extracting its representations, not engineering raw features by hand. Chapter 15 covers this in much more detail, including how to use the AI Sandbox tools for text-based modeling tasks. What is worth understanding here is the conceptual distinction: simple count-based features are interpretable and fast; embedding-based features are richer but require more infrastructure and produce representations that are harder to inspect directly.

---

## Time Series Data

Time series data shows up across many research domains: longitudinal cohort studies, environmental monitoring, economic panels, repeated experimental measurements. The defining feature is that observations have a meaningful temporal order, and that order carries information.

The most important feature engineering patterns for time series are lag features and rolling aggregates.

A lag feature is simply the value of a variable at a previous time step. If you are trying to predict a patient outcome at time T, the patient's measurement at time T-1, T-2, and T-3 might all be informative. Creating these as explicit columns gives the model access to recent history. How many lags to include depends on your domain knowledge about how far back the relevant signal extends {cite}`hyndman2021forecasting`.

Rolling aggregates summarize a window of recent values. A 7-day rolling mean of daily temperature. A 30-day rolling maximum of hospital admissions. A 4-week rolling standard deviation of a sensor reading. These features smooth over noise and capture trends at different timescales. They are often more informative than raw lagged values, especially when the underlying signal is noisy.

There is one critical thing to get right when engineering time series features: the leakage boundary. Every feature you create for predicting time T should be built only from data that would have been available before time T. If you accidentally include information from the future in your features, your model will look impressive in development and fall apart on real data. This is easier to get wrong than it sounds, especially with rolling windows that span your train/test boundary. Always check your feature construction logic against your time splits before trusting a performance number.

---

## Image Data

Raw images are high-dimensional objects: a 224x224 pixel image has nearly 50,000 individual values. You almost never engineer features from raw pixels. The patterns that matter in images, edges, textures, shapes, objects, are hierarchical and spatially structured in ways that hand-crafted features struggle to capture.

The standard approach today is transfer learning: take a convolutional neural network that has already been trained on a large image dataset, feed your images through it, and use the learned representations as your features. These representations are much more compact and semantically meaningful than raw pixel values. The model has already learned to detect useful visual patterns; you are borrowing that knowledge for your specific task.

As with text embeddings, the practical question in most research contexts is which pretrained model to use and how to extract representations from it. Chapter 15 covers this in the context of the AI Sandbox, including worked examples for image-based tasks. What belongs here is the principle: resist the impulse to start with raw pixels, and resist the impulse to train a vision model from scratch unless you have a very large labeled dataset and a compelling reason.

---

## When to Engineer Manually versus Let AutoML Handle It

The honest answer is that the boundary shifts depending on your data and your question. But a few heuristics are worth keeping in mind.

Let AutoML handle it when the transformation is mechanical and domain-neutral. Standard scaling, one-hot encoding of low-cardinality variables, basic missing value imputation: AutoGluon does these things competently, and doing them yourself adds overhead without much return.

Engineer features yourself when the transformation requires domain knowledge. If you know from the literature that the relationship between your predictor and outcome is nonlinear in a specific way, encoding that directly is worth doing. If you know that two variables interact in a meaningful way in your domain, building the interaction term yourself is faster and more reliable than hoping the model discovers it. If a derived variable has a clear scientific interpretation, making it explicit improves not just performance but interpretability.

Be thoughtful when the transformation affects leakage risk. Any feature that involves aggregating over your full dataset, or that involves information from future time points, needs to be constructed carefully. AutoML will not automatically protect you from data leakage in your feature construction; that is your responsibility.

A practical workflow: start with clean data and let AutoGluon run first as a baseline. Then look at the feature importance output it gives you. If a derived feature you were considering is already being captured by combinations of existing variables, you may not need to add it explicitly. If there is a domain-specific variable you think matters but is not showing up as important, try adding it and re-running. Feature engineering is an iterative process, not a checklist to complete before modeling begins.

---

## Key Takeaways

- Feature engineering is about encoding domain knowledge into the structure of your data, which is something AutoML cannot do for you
- For tabular data, focus on correcting skewed distributions, choosing the right encoding for categorical variables, and building derived features that carry conceptual meaning
- For text and images, the most practical path in most research settings is using pretrained representations rather than building features from scratch; Chapter 15 covers the hands-on details
- For time series, lag features and rolling aggregates are the core tools; getting the leakage boundary right is more important than getting the window size perfect
- Start with a baseline AutoGluon run, then use the feature importance output to decide where manual engineering is worth the effort

---

## Try This

For a dataset you are currently working with or planning to use:

1. Pick one numeric variable with a skewed distribution. Apply a log transformation and compare the histogram before and after. Does the shape change in a way that makes sense for your domain?
2. Identify one categorical variable in your data. Decide whether one-hot encoding or ordinal encoding is more appropriate for it, and write a one-sentence justification.
3. Think of one derived feature that would require domain knowledge to construct. Describe it in plain language: what columns does it come from, what does it represent, and why might it be more informative than the raw inputs?

---

## Resources for Further Reading

A practical introduction to the full range of feature engineering techniques across data types, including more advanced methods not covered here, is available in Zheng and Casari's work on feature engineering for machine learning {cite}`zheng2018feature`. For time series feature engineering in particular, Hyndman and Athanasopoulos offer a thorough and freely available treatment of lag structures, rolling features, and decomposition methods {cite}`hyndman2021forecasting`.

---

## Related Chapters

- [Exploratory Data Analysis](ch14_exploratory_analysis.md) - Understanding your data before transforming it
- [Data Preparation](ch15_data_preparation.md) - Cleaning decisions that precede feature engineering
- [AutoML with AutoGluon](ch17_automl_tabular.md) - Baseline modeling that uses your engineered features
- [AI Sandbox](ch20_pretrained_text_vision.md) - Hands-on tools for text and image feature extraction

---

**Questions or feedback?** [Open an issue on GitHub](https://github.com/xiaosuhu/midas-ai-in-research/issues)

```{bibliography}
:filter: docname in docnames
```

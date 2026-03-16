# Multimodal Learning with AutoGluon

:::{admonition} What you will learn
:class: tip

By the end of this chapter and its companion notebook, you will understand how `MultiModalPredictor` handles text, images, and tabular data through the same interface, when combining data types actually improves your model, how to run all three use cases in a GPU-enabled Colab environment, and what to watch for when interpreting results from a multimodal model.
:::

Research data rarely comes in just one form. A psychology study might collect both numeric questionnaire scores and participants' written explanations of their answers. An ecology dataset might pair sensor readings with field photographs. A social science survey might combine Likert-scale items with open-ended responses that participants typed out themselves. In all of these cases, useful information sits across more than one data type at the same time, and the question is what to do with it.

The conventional approach is to handle each type separately: build one model on the numeric features, another on the text, maybe extract some hand-crafted features from the images, and then figure out how to combine the outputs. That works, but it is tedious and it throws away the relationships between modalities that might carry genuine predictive signal.

AutoGluon's `MultiModalPredictor` takes a different approach. You give it a DataFrame where some columns are numeric, some are text, and some contain image file paths, and it handles the rest. The same call works whether you are running a text-only task, an image-only task, or a fully mixed dataset. That is the organizing idea of this chapter: one tool, three uses {cite}`autogluon2024`.

---

## What MultiModalPredictor Handles

`MultiModalPredictor` works with three types of columns {cite}`autogluon2024`:

**Text columns** contain natural language strings. AutoGluon processes these through a pretrained language model, typically from the BERT family, which converts each string into a dense representation that captures semantic meaning {cite}`devlin2019bert`. You do not need to tokenize, vectorize, or otherwise preprocess your text. AutoGluon fine-tunes the language model on your prediction task as part of training.

**Image columns** contain file paths pointing to images on disk. AutoGluon processes these through a pretrained vision model, extracting features before fine-tuning on your labels. The images themselves stay on disk during training; AutoGluon reads and preprocesses them in batches.

**Tabular columns** are numeric or categorical variables. These are handled with a small neural network component that is trained jointly with the text and image encoders. AutoGluon detects column types automatically: short strings go to the categorical processor, longer strings go to the language model, and file-path-looking strings go to the image processor.

All of these representations are combined in a fusion layer and optimized together on your prediction task. The result is a single model that has learned from all data types simultaneously rather than treating them as separate problems.

---

## What Is Happening Under the Hood

For most purposes, you do not need to understand the architecture in detail. But it helps to know one thing: the backbone models (the language model and the vision model) are not trained from scratch. They are pretrained on large external datasets and then adapted to your task. This means `MultiModalPredictor` can produce useful results even on relatively small datasets, because most of the learning about language and visual features has already happened before your data enters the picture.

The trade-off is compute. Fine-tuning pretrained models requires a GPU to run in a reasonable amount of time. For text-only tasks with shorter inputs, a GPU is strongly recommended but not always strictly required. For image tasks, a GPU is essentially necessary. This is covered in more detail in the tutorial section below.

---

## Tutorial: One Tool, Three Ways

The companion notebook is organized into three standalone sections that each demonstrate a different use of `MultiModalPredictor`. You can run them independently or in sequence. The point of the three-section structure is to show that the core interface stays the same, so once you understand one section, the others are straightforward variations.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/xiaosuhu/midas-ai-in-research/blob/v1.0-dev/docs/notebooks/autogluon_multimodal_demo.ipynb)

Click the badge to open a temporary Colab session. Click "Copy to Drive" inside Colab to save your own copy before making changes.

### Enabling the GPU in Colab

Before running any cells in the notebook, make sure the GPU runtime is active. In Colab, go to **Runtime → Change runtime type** and select **T4 GPU**. The notebook includes a cell that checks your runtime and prints a warning if no GPU is detected. Image training in particular will be very slow on CPU.

### Section 1: Text-Only Classification

The first section uses a sample of product reviews from the Multilingual Amazon Reviews Corpus, where the task is to classify review sentiment from the review text alone {cite}`keung2020multilingual`. There are no numeric features and no images, just a column of text strings and a label. This is a good starting point because it isolates exactly what the language model component contributes.

The dataset is straightforward to load and split, and AutoGluon's text tokenization and batching happen automatically in the background. Training takes a few minutes on Colab's T4 GPU.

After training, you can inspect the predictions and look at cases where the model struggled. For sentiment classification, errors tend to cluster around reviews that are genuinely ambiguous, where the writer praises one aspect of a product while complaining about another. That pattern is meaningful: it suggests the model is doing something reasonable rather than just memorizing surface features.

### Section 2: Image-Only Classification

The second section uses Fashion-MNIST, a dataset of 70,000 grayscale images of clothing items across ten categories {cite}`xiao2017fashion`. The task is to classify each image into its correct category (t-shirt, trouser, pullover, and so on). Fashion-MNIST was designed as a direct drop-in replacement for the original MNIST handwritten digits dataset but with a harder classification problem, and it has become a standard benchmark for image classification.

The interface change from Section 1 is minimal. Instead of a text column, you have an image path column. The `MultiModalPredictor` call looks identical; AutoGluon figures out from the column type that it needs the vision encoder rather than the language model.

Fashion-MNIST is a clean pedagogical example for a few reasons: images are small (28x28 pixels), the categories are intuitive, and the classification task is hard enough to be interesting without being intractable. GPU training typically completes within a few minutes on Colab, and the leaderboard makes it easy to see how fine-tuning compares to simpler baselines.

### Section 3: Text and Tabular Combined

The third section uses a sample from the PetFinder.my Adoption Prediction dataset, a Kaggle competition dataset where the task is to predict how quickly a pet gets adopted based on its listing information {cite}`petfinder2019`. Each row represents a pet listing and includes both structured columns (species, age, breed, health status, adoption fee, and so on) and a free-text description written by the shelter or owner.

This section is the most research-realistic of the three. The combination of structured features with a text description is a pattern that appears regularly in social science surveys, grant applications, administrative records, and clinical notes. The question the section answers is whether the text column adds predictive value beyond what the structured features already capture.

To test this directly, the notebook fits two models: one on the tabular features only (`TabularPredictor`) and one on the full dataset including the description column (`MultiModalPredictor`). Comparing their leaderboard scores shows whether the text is actually helping.

### The Core Call

The main point of running the same code three times is to show how little changes. Here is what the call looks like across all three sections:

```python
from autogluon.multimodal import MultiModalPredictor

predictor = MultiModalPredictor(
    label="target_column",
    eval_metric="accuracy",
    path="autogluon_multimodal_model"
).fit(
    train_data=train_df,
    time_limit=300
)
```

In Section 1, `train_df` has a text column and a label. In Section 2, it has an image path column and a label. In Section 3, it has numeric columns, a text column, and a label. AutoGluon detects the column types and routes them to the appropriate encoder. You do not tell it which columns to treat as text or images; it infers this from the data.

The `time_limit` is in seconds. Five minutes is a reasonable starting point for text and image tasks. For the mixed tabular-plus-text section, three to five minutes is usually enough to get a meaningful leaderboard on a dataset of a few thousand rows.

---

## Reading the Output

`MultiModalPredictor` produces a leaderboard just like the tabular and time series predictors. The format is the same: models ranked by the evaluation metric, with higher values always meaning better performance. The model set is different, though. Rather than a wide ensemble of gradient boosting and random forest models, you will typically see a small set of fine-tuned pretrained models and a simple weighted ensemble on top.

```python
predictor.leaderboard(test_data=test_df, silent=True)
```

For classification tasks, accuracy is the default metric, though you can specify others at initialization. For the image and text tasks in the notebook, the leaderboard tends to be short because the model zoo for `MultiModalPredictor` is more focused than the tabular one. What matters is comparing the top model's performance against a simple baseline, such as a majority-class classifier, to make sure you are actually capturing signal.

Predictions are accessed the same way as always:

```python
predictions = predictor.predict(test_df)
probabilities = predictor.predict_proba(test_df)  # for classification
```

---

## Practical Notes for Research Data

**Does combining modalities always help?** Not necessarily. If your text descriptions are mostly boilerplate or do not vary meaningfully across observations, adding a text column may add noise rather than signal and slow down training considerably. The Section 3 comparison in the notebook (tabular-only versus tabular-plus-text) is specifically designed to let you check this on your own data.

**How much data do you need?** Pretrained models help considerably with small datasets because most of the feature learning is already done. In practice, a few hundred labeled examples per class can be enough to get a useful result from a fine-tuned language model, though more is always better. Image tasks typically need slightly more data to fine-tune reliably.

**File paths for images.** Image columns must contain valid paths to files that exist on disk at training time. In a Colab notebook, this means either downloading images into the session or mounting your Google Drive. If paths are broken, AutoGluon will raise an error immediately rather than silently using placeholder values.

**Processing time.** `MultiModalPredictor` is substantially slower to train than `TabularPredictor` on the same hardware. Fine-tuning a language model on a text column for five minutes on a GPU is roughly equivalent to running `TabularPredictor` for 15 to 20 minutes on a CPU. Budget accordingly, and use a GPU even for text-only tasks if you want results in reasonable time.

**Mixed text and images together.** The notebook does not include a section with all three modalities simultaneously, but `MultiModalPredictor` supports it. If you have a dataset with numeric features, text, and images in the same row, the same call works. The main practical constraint is that image-plus-text models are the slowest to train and most demanding on GPU memory.

---

## Frequently Asked Questions

**Can I use my own pretrained model instead of AutoGluon's default?**

Yes. You can specify the backbone model using the `hyperparameters` argument. For example, to use a different Hugging Face language model for the text encoder, you would pass `{"model.hf_text.checkpoint_name": "your-model-name"}`. The AutoGluon documentation covers the full list of supported backbones for each modality. For most research use cases, the defaults work well enough that swapping backbones is not necessary unless you have a specific reason, such as a domain-specific language model trained on scientific text.

**Is this the right tool if I just have text and no other features?**

`MultiModalPredictor` works for text-only tasks, but if you have only text and no other modalities, you might also look at AutoGluon's older `TextPredictor` interface or standard Hugging Face fine-tuning workflows. `MultiModalPredictor` is most useful when you want a single interface that scales from text-only to mixed data without rewriting your pipeline.

**How do I handle text that is very long, like clinical notes or full documents?**

Pretrained language models have a token limit, typically 512 tokens for BERT-family models. AutoGluon truncates text that exceeds this limit. If your documents are long and the important content could appear anywhere in them, truncation may hurt performance. For long documents, it is worth considering whether you should chunk or summarize them before passing them in, or use a model with a longer context window.

**Can I run this on a university HPC cluster instead of Colab?**

Yes, and for sensitive data you should. The process is essentially the same: request a GPU node, load your data from a secure storage location, and run the same code. [Chapter 13](ch13_computing_resources.md) covers how to get started with university HPC resources.

```{admonition} If You're at U-M
:class: note

Great Lakes provides GPU nodes well suited to multimodal training. For HIPAA-covered data, use Armis2 instead. See [AI Resources at the University of Michigan](../part4/ch27_um_resources.md) for access details.
```

---

## Research Considerations

The same cautions from the tabular chapter apply here, and multimodal modeling adds a few of its own.

**Baseline comparisons matter even more.** A multimodal model is harder to interpret than a tabular one, and it is tempting to assume that using more data types must be better. Always compare against a strong single-modality baseline. If a tabular-only model is nearly as good as the combined model, the added complexity of the multimodal pipeline is hard to justify, especially for a published result.

**Pretrained models carry assumptions.** Language models are trained on text from the internet and may perform differently on domain-specific text, such as scientific writing, medical terminology, or non-English language. If your text data is substantially different from the pretraining distribution, the default backbone may underperform, and a domain-adapted model could be a better choice.

**Images and text are not automatically clean.** `TabularPredictor` and `TimeSeriesPredictor` do a lot of preprocessing automatically. `MultiModalPredictor` also preprocesses internally, but the quality of its outputs depends heavily on the quality of your inputs. Inconsistent image resolutions, corrupted files, or noisy text fields will affect performance in ways that are harder to diagnose than a missing value in a numeric column.

**Interpretability is limited.** Feature importance from a tabular model is relatively straightforward to communicate. For a multimodal model that fuses a fine-tuned language model with tabular features, explaining which specific inputs drove a prediction is considerably harder. AutoGluon provides some gradient-based attribution tools, but these should be treated as exploratory rather than definitive.

**On data privacy.** For data covered by HIPAA, IRB restrictions, or other governance policies, do not use a public Colab notebook. This is especially important if your text columns contain clinical notes or any individually identifying content. Run in an approved institutional environment or a local installation instead. [Chapter 13](ch13_computing_resources.md) covers computing options in more detail.

---

## References

```{bibliography}
:filter: docname in docnames
```

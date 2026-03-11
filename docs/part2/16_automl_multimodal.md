# Multimodal Learning with AutoGluon

:::{admonition} What you will learn
:class: tip

By the end of this chapter and its companion notebook, you will understand how `MultiModalPredictor` handles text, images, and structured columns using the same calling interface, when combining data types adds genuine predictive value versus when separate models are simpler, and how to run three different use cases (text only, image only, text plus tabular) with minimal code changes.
:::

Research data is rarely just one thing. A clinical dataset might pair structured lab values with free-text physician notes. A social science survey might combine Likert-scale responses with open-ended text fields. An ecology study might attach tabular measurements to field photographs. When meaningful information lives across multiple data types simultaneously, training separate models on each type and combining them manually loses the relationships between them. AutoGluon's `MultiModalPredictor` is designed to handle this directly.

Like the tabular and time series chapters, the goal here is feasibility testing — a quick way to find out whether combining data types improves predictive signal before committing to a custom multimodal pipeline.

---

## What Multimodal Means in Practice

`MultiModalPredictor` can handle combinations of tabular columns, text fields, and images within a single model. AutoGluon detects the data types automatically: columns with short strings are treated as categorical, columns with longer text are processed through a pretrained language model (typically a BERT-family model), and image columns containing file paths are processed through a pretrained vision model. The representations from each modality are fused and fine-tuned together on your prediction task.

This means you do not need to manually engineer features from text or images — the pretrained models handle that. You do need a GPU for training in most cases, which is where Colab's free GPU runtime becomes particularly useful.

---

## Tutorial: One Tool, Three Uses

The companion notebook for this chapter demonstrates `MultiModalPredictor` across three different use cases in sequence: text only, images only, and text combined with tabular features. Each section uses a different Hugging Face dataset but calls the predictor in essentially the same way, which is the main point. The notebook is designed to follow naturally from the tabular tutorial in Chapter 14 — if you have worked through that one, the structure here will feel familiar.

All three sections, dataset loading, model training, evaluation, and a brief comparison between combined and single-modality versions are in the notebook. A GPU is recommended for the image section and will speed up the text sections as well. Instructions for enabling the free T4 GPU in Colab are at the top of the notebook.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/xiaosuhu/midas-ai-in-research/blob/v1.0-dev/docs/notebooks/autogluon_multimodal_demo.ipynb)

The three datasets used are:

- **Stanford Sentiment Treebank (SST-2)** for text-only sentiment classification {cite}`socher2013sst`
- **Fashion-MNIST** for image-only clothing category classification {cite}`xiao2017fashion`
- **Amazon Reviews Multilingual corpus (English subset)** for predicting star ratings from review text and product category {cite}`keung2020multilingual`

All datasets are loaded directly from Hugging Face with no manual downloads required.

---

## References

```{bibliography}
:filter: docname in docnames
```

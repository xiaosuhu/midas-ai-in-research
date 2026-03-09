# Multimodal Learning with AutoGluon

Research data is rarely just one thing. A clinical dataset might pair structured lab values with free-text physician notes. A social science survey might combine Likert-scale responses with open-ended text fields. An ecology study might attach tabular measurements to field photographs. When meaningful information lives across multiple data types simultaneously, training separate models on each type and combining them manually loses the relationships between them. AutoGluon's `MultiModalPredictor` is designed to handle this directly.

Like the tabular and time series chapters, the goal here is feasibility testing — a quick way to find out whether combining data types improves predictive signal before committing to a custom multimodal pipeline.

---

## What Multimodal Means in Practice

`MultiModalPredictor` can handle combinations of tabular columns, text fields, and images within a single model. AutoGluon detects the data types automatically: columns with short strings are treated as categorical, columns with longer text are processed through a pretrained language model (typically a BERT-family model), and image columns containing file paths are processed through a pretrained vision model. The representations from each modality are fused and fine-tuned together on your prediction task.

This means you do not need to manually engineer features from text or images — the pretrained models handle that. You do need a GPU for training in most cases, which is where Colab's free GPU runtime becomes particularly useful.

---

## Coming Soon

This chapter is under active development. The planned tutorial will include:

- A text-plus-tabular example combining structured features with short text descriptions
- An image classification example using the MNIST dataset, demonstrating GPU-accelerated training in Colab
- How to interpret `MultiModalPredictor` results and feature importance across modalities
- Practical guidance on when multimodal modeling is worth the added complexity versus separate models

A companion Colab notebook with GPU instructions will be linked here when ready.

In the meantime, the [AutoGluon multimodal documentation](https://auto.gluon.ai/stable/tutorials/multimodal/index.html) provides tutorials covering text, image, and combined modalities.

---

## References

```{bibliography}
:filter: docname in docnames
```

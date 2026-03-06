# External AI Resources for Research

```{tip}
This chapter focuses on carefully selected, high-value resources that are widely used, well maintained, and directly relevant to academic research. It is not meant to be exhaustive. New tools and platforms appear constantly, and the right question is always whether a resource is reliable and appropriate for your work, not simply whether it is popular.
```

## Overview

Beyond what UM provides, the broader AI community offers a wide range of open tools, datasets, and learning resources that can meaningfully accelerate research. The sections below organize these by purpose: learning and training, open datasets, modeling frameworks and tools, compute options, and software ecosystems.

---

## Learning and Training Resources

### DeepLearning.AI

Founded by Andrew Ng, DeepLearning.AI offers a well-regarded library of courses covering machine learning foundations, deep learning, large language models, prompt engineering, RAG, and applied topics in computer vision, NLP, and reinforcement learning. The courses are structured for learners who want both conceptual grounding and hands-on practice.

**Link:** https://www.deeplearning.ai/

---

### Kaggle Learn

Kaggle Learn provides short, practical micro-courses covering Python, pandas, machine learning, deep learning, computer vision, time series, and LLM applications. These are a good starting point for researchers who want to build hands-on fluency without a large time commitment.

**Link:** https://www.kaggle.com/learn

---

### The Turing Way

The Turing Way is an open-source, community-driven handbook covering reproducible research, project management and documentation, and ethics and open science. It is one of the direct inspirations for this handbook and remains an excellent reference for researchers building responsible, transparent workflows.

**Link:** https://the-turing-way.netlify.app/

---

### Fast.ai

Fast.ai offers free practical deep learning courses that start with working models and build conceptual understanding from there, rather than the other way around. Topics include NLP, vision, tabular learning, and model interpretation.

**Link:** https://www.fast.ai/

---

### Dive into Deep Learning (D2L)

D2L is a fully open-source deep learning textbook with runnable code in Jupyter notebooks. It is widely used in academic courses for combining mathematical foundations with hands-on, experiment-ready implementations in PyTorch. It is well suited for researchers who want both the theory and the code in one place.

**Link:** https://d2l.ai/

---

### Google Machine Learning Crash Course

A structured, freely available introduction to machine learning fundamentals from Google. It covers core concepts like gradient descent, overfitting, and classification, and is a reasonable starting point for researchers with no prior ML background.

**Link:** https://developers.google.com/machine-learning/crash-course

---

### Recommended Reading

If you want a grounded view of where generative AI actually stands in research contexts, this paper is worth the time: Reddy and Shojaee offer a broad and honest assessment of where generative AI is making a real difference in scientific discovery and where significant limitations remain ({cite}`reddy2025generative`).

---

## Open Datasets and Searchable Repositories

### Kaggle Datasets

Kaggle hosts one of the largest collections of queryable datasets across domains, including tabular, image, text, and time series data. Most datasets include metadata and community notebooks that let you start exploring immediately.

**Link:** https://www.kaggle.com/datasets

---

### HuggingFace Datasets

HuggingFace offers a massive ecosystem of machine learning-ready datasets with a standardized API, covering NLP, vision, audio, multimodal, and scientific domains.

**Link:** https://huggingface.co/datasets

---

### UCI Machine Learning Repository

The UCI repository hosts a large collection of classic and benchmark datasets commonly used for prototyping and evaluation across a wide range of tasks.

**Link:** https://archive.ics.uci.edu/

---

### PhysioNet

PhysioNet provides open access to biomedical and physiological datasets, including several synthetic and demo sets well suited for methods development without requiring IRB approval.

**Link:** https://physionet.org/

---

### OpenNeuro

OpenNeuro is a free platform for sharing and accessing neuroimaging datasets, including fMRI, EEG, MEG, and fNIRS data.

**Link:** https://openneuro.org/

---

## Modeling, Frameworks, and Tools

### HuggingFace Transformers

HuggingFace is the central open-source hub for pre-trained LLMs, vision models, audio models, multimodal architectures, and fine-tuning pipelines. If a published model has an open checkpoint available, it is almost certainly accessible through HuggingFace.

**Link:** https://huggingface.co/models

---

### Papers with Code

Papers with Code is a searchable collection of machine learning papers that link directly to their code implementations, datasets, and benchmark results. It is one of the most practical resources for seeing exactly how a method was implemented, not just described. MIDAS includes it as a recommended tool in their generative AI resource hub ({cite}`midas_umich`).

**Link:** https://paperswithcode.com/

---

### Stanford HELM

HELM (Holistic Evaluation of Language Models) is a living benchmark developed at Stanford that evaluates large language models across a wide range of scenarios in a transparent and systematic way. If you need to compare models for a specific task based on accuracy, fairness, calibration, or robustness, HELM provides a more principled basis for that comparison than relying on marketing claims ({cite}`liang2022helm`).

**Link:** https://crfm.stanford.edu/helm/

---

### AutoGluon

AutoGluon is the AutoML toolkit used throughout Part 2 of this handbook. It covers tabular prediction, NLP, vision, and multimodal learning, and is designed for rapid hypothesis testing without requiring you to write complex modeling code from scratch.

**Link:** https://auto.gluon.ai/

---

### Ollama

Ollama makes it straightforward to run open-source LLMs locally on your own machine, with no data sent to external servers. This is particularly useful for researchers working with sensitive or unpublished data who need LLM capabilities but cannot use a cloud-based service. It supports a growing range of models including Llama, Mistral, and Gemma.

**Link:** https://ollama.com/

---

### PyTorch

PyTorch is the dominant deep learning framework in academic research, widely used for building, training, and deploying custom neural network models.

**Link:** https://pytorch.org/

---

### TensorFlow and Keras

TensorFlow and its high-level interface Keras are widely used in both research and production settings, with a large community and extensive documentation.

**Link:** https://www.tensorflow.org/

---

### LangChain and LlamaIndex

LangChain and LlamaIndex are the two most commonly used frameworks for building retrieval-augmented generation pipelines, LLM agents, and data-connected chatbots.

**LangChain:** https://www.langchain.com/
**LlamaIndex:** https://www.llamaindex.ai/

---

## Cloud Compute and Low-Cost GPU Resources

### Google Colab

Colab provides free or low-cost Jupyter notebooks with GPU and TPU access. It is one of the most accessible ways to run ML experiments without any local hardware setup, and the notebooks used throughout this handbook are designed to run on Colab.

**Link:** https://colab.research.google.com/

---

### Kaggle Notebooks

Kaggle offers free GPU-enabled notebooks with zero configuration required. A useful fallback when Colab GPU availability is limited.

**Link:** https://www.kaggle.com/code

---

### Vast.ai

Vast.ai is a marketplace for renting GPU compute at relatively low cost, with a wide range of hardware configurations available. A practical option for larger training jobs that exceed what Colab or Kaggle provide.

**Link:** https://vast.ai/

---

### Lambda Labs

Lambda Labs provides cloud GPU infrastructure oriented toward research use, with options ranging from on-demand instances to reserved capacity.

**Link:** https://lambdalabs.com/

---

### RunPod

RunPod offers easy-to-configure GPU workspaces with ready-made templates for Jupyter notebooks, inference servers, and custom environments.

**Link:** https://runpod.io/

---

## Software and Notebook Ecosystems

### GitHub

GitHub is the standard platform for version control, open-source collaboration, and reproducibility in research software. This handbook's source is hosted there.

**Link:** https://github.com/

---

### VS Code

VS Code is a widely used editor for AI and data science workflows, with strong support for Python, Jupyter notebooks, and remote development.

**Link:** https://code.visualstudio.com/

---

### JupyterLab

JupyterLab is the standard interactive notebook environment for data exploration, ML prototyping, and visualization.

**Link:** https://jupyter.org/

---

## Quick Reference Table

| Category | Resource | Description | Link |
|---------|----------|-------------|------|
| Learning | DeepLearning.AI | High-quality AI courses | https://www.deeplearning.ai/ |
| Learning | Kaggle Learn | Practical micro-courses | https://www.kaggle.com/learn |
| Learning | Turing Way | Reproducible research handbook | https://the-turing-way.netlify.app/ |
| Learning | Fast.ai | Practical deep learning | https://www.fast.ai/ |
| Learning | D2L | Open-source deep learning textbook | https://d2l.ai/ |
| Datasets | Kaggle Datasets | Largest open dataset library | https://www.kaggle.com/datasets |
| Datasets | HuggingFace Datasets | ML-ready dataset hub | https://huggingface.co/datasets |
| Datasets | UCI Repository | Classic benchmark datasets | https://archive.ics.uci.edu/ |
| Datasets | PhysioNet | Biomedical and physiological datasets | https://physionet.org/ |
| Datasets | OpenNeuro | Open neuroimaging datasets | https://openneuro.org/ |
| Tools | HuggingFace Transformers | LLM and model hub | https://huggingface.co/models |
| Tools | Papers with Code | AI papers with code and benchmarks | https://paperswithcode.com/ |
| Tools | Stanford HELM | LLM evaluation benchmark | https://crfm.stanford.edu/helm/ |
| Tools | AutoGluon | AutoML for rapid experiments | https://auto.gluon.ai/ |
| Tools | Ollama | Run LLMs locally for sensitive data work | https://ollama.com/ |
| Compute | Colab | Free GPU notebooks | https://colab.research.google.com/ |
| Compute | Kaggle Notebooks | Free GPU compute | https://www.kaggle.com/code |
| Compute | Vast.ai | Low-cost GPU rental | https://vast.ai/ |
| Compute | Lambda Labs | Research-oriented GPU cloud | https://lambdalabs.com/ |
| Compute | RunPod | Easy GPU workspace setup | https://runpod.io/ |

---

```{bibliography}
:filter: docname in docnames
```

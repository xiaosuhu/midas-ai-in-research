# Chapter 30: AI Literacy Glossary

```{note}
This glossary covers terms as they appear in this handbook. It is intentionally scoped to the book rather than trying to cover the full breadth of the AI field. If you encounter a term in the text that is not defined here, the MIDAS AI Literacy Glossary at https://midas.umich.edu/ maintains a more comprehensive version.
```

---

## Foundational Terms

**Artificial Intelligence (AI)**
A broad field focused on creating systems that can perform tasks that usually require human intelligence, such as reasoning, learning, pattern recognition, and decision-making.

**Machine Learning (ML)**
A subset of AI where systems learn patterns from data rather than following explicit rules. Models improve their performance by adjusting internal parameters based on examples.

**Deep Learning (DL)**
A branch of machine learning that uses multilayer neural networks to learn complex patterns from images, text, audio, and other data types. Most state-of-the-art AI systems today are built on deep learning.

**Generative AI (GenAI)**
Models that can create new content, including text, images, audio, video, and code, based on patterns learned from large datasets. Large language models like GPT-4 and Claude are generative AI systems.

---

## Core Concepts and Techniques

**Neural Networks**
Computational structures composed of interconnected layers of units, often called neurons. Neural networks form the basis of most modern machine learning models.

**Attention Mechanism**
The core innovation in the Transformer architecture. For each position in the input, the attention mechanism computes a weighted relationship between that position and all others in the sequence, so the model learns which parts of the context are most relevant to each token. This allows models to capture long-range dependencies that earlier sequential approaches struggled with. Covered in depth in [Chapter 2](../part1/ch02_how_ai_works.md) and [Chapter 23](../part3/ch23_nlp_with_bert.md).

**Foundation Model**
A large model trained at substantial scale on broad data that can then be adapted to many different downstream tasks rather than being built from scratch for each one. BERT and GPT-3 are early examples. The term captures the idea that a single pretrained model serves as the starting point for a wide range of applications. Introduced in [Chapter 2](../part1/ch02_how_ai_works.md).

**Context Window**
The maximum amount of text a language model can consider at once when generating a response, measured in tokens. Content beyond this limit is invisible to the model, which is why very long conversations can produce responses that seem to ignore things said earlier in the session. Modern models have context windows ranging from a few thousand to hundreds of thousands of tokens. Covered in [Chapter 2](../part1/ch02_how_ai_works.md).

**Transfer Learning**
Using a model trained on one task or dataset as the starting point for a different but related task. Fine-tuning is the most common form of transfer learning in applied AI research. It works because representations learned during large-scale pretraining tend to be useful across a wide range of downstream problems. Relevant to [Chapters 16](../part2/ch16_feature_engineering.md), [19](../part2/ch19_automl_multimodal.md), and [20](../part2/ch20_pretrained_text_vision.md).

**Masked Language Modeling**
A pretraining objective in which some tokens in a sentence are hidden and the model is trained to predict them from surrounding context. BERT was trained this way, reading context from both directions around each masked token simultaneously. This produces rich, context-sensitive representations of language. Covered in [Chapter 23](../part3/ch23_nlp_with_bert.md).

**Downstream Task**
A specific applied problem that a pretrained model is adapted to solve, such as text classification, named entity recognition, or sentiment analysis. Fine-tuning is how a general pretrained model is adjusted to perform well on a downstream task. Covered in [Chapter 26](../part3/ch26_llm_eval_finetuning.md).

**Training Data**
The examples used to teach a model. Model quality depends heavily on the quantity, diversity, and accuracy of the training data.

**Training, Validation, and Test Sets**
The standard way to split a dataset for machine learning. The training set is used to fit the model, the validation set is used to tune settings and catch overfitting during development, and the test set is held out until the end to evaluate final performance. Keeping these splits separate is one of the most important practices in building reliable models.

**Overfitting and Underfitting**
Overfitting occurs when a model learns the training data too closely, including its noise and quirks, and fails to generalize to new examples. Underfitting occurs when a model is too simple to capture the actual patterns in the data. Both reduce how well a model performs in practice.

**Cross-Validation**
A technique for estimating model performance by repeatedly splitting the data into training and evaluation portions. K-fold cross-validation, the most common variant, divides the data into k subsets and trains k separate models, each evaluated on a different held-out fold. This gives a more reliable performance estimate than a single train/test split.

**Baseline Model**
A simple reference model used to set a performance floor. If a sophisticated model cannot beat a well-chosen baseline, that is a signal to revisit the problem setup before investing in more complexity.

**Fine-Tuning**
Adapting a pre-trained model to a specific dataset or task, rather than training a model from scratch. Fine-tuning is often much more efficient than full training and is widely used for adapting LLMs to specialized domains. [Chapter 26](../part3/ch26_llm_eval_finetuning.md) covers fine-tuning in depth, including parameter-efficient approaches.

**Embeddings**
Numeric vector representations of text, images, or other data that capture their semantic meaning. Two items with similar meanings end up close together in the embedding space, which is what makes search and retrieval systems work.

**Cosine Similarity**
A measure of the angle between two vectors, used to compare embeddings. A cosine similarity of 1 means the vectors point in the same direction (maximum similarity); 0 means they are perpendicular (no similarity). Because embeddings capture meaning as directions in a high-dimensional space, cosine similarity is a natural way to measure how close two texts are in meaning. Used throughout [Chapters 23](../part3/ch23_nlp_with_bert.md) and [24](../part3/ch24_rag.md).

**Inference**
The process of using a trained model to generate predictions or outputs on new data. Distinct from training, which adjusts the model's parameters.

**Hallucination**
When a language model produces confident-sounding but incorrect or fabricated information. Hallucinations are a well-documented limitation of LLMs and one of the main reasons that human review of AI-generated content remains important.

**Token**
A small unit of text that LLMs process, typically a word fragment or a punctuation mark. Computational cost and speed for LLM tasks both scale with token count.

**Reproducibility**
The ability of a research analysis to produce the same results when run again on the same data with the same code. Reproducibility depends on recording the software environment, pinning package versions, setting random seeds, and documenting every data transformation. It is distinct from replicability, which refers to obtaining consistent findings with new data. Covered in [Chapter 22](../part2/ch22_reproducibility.md).

---

## Data and Feature Concepts

**Tabular Data**
Data organized in rows and columns, where each row is an observation and each column is a variable or feature. Spreadsheets, databases, and most survey or sensor datasets are tabular. Tabular data remains the most common data format in research outside of vision and NLP.

**Exploratory Data Analysis (EDA)**
The practice of examining a dataset before modeling, using summary statistics, visualizations, and distribution checks to understand its structure, detect problems, and generate hypotheses. EDA is covered in [Chapter 14](../part2/ch14_exploratory_analysis.md).

**Feature Engineering**
The process of selecting, transforming, or constructing input variables to improve model performance. Good feature engineering encodes domain knowledge into a form the model can use. It is covered in depth in [Chapter 16](../part2/ch16_feature_engineering.md).

**Feature**
A single input variable used by a model. In a survey dataset, each question response might be a feature. In an image, pixel values or extracted descriptors might be features.

**Encoding**
Transforming categorical variables into a numeric format that a machine learning model can process. Common strategies include one-hot encoding, which creates a binary column for each category, and ordinal encoding, which assigns integer values to ordered categories.

**Imputation**
Filling in missing values in a dataset using a strategy such as the column mean, median, most frequent value, or a model-based estimate. How missing data is handled can have a significant effect on model results.

**Class Imbalance**
A situation where one category in the target variable is far more common than others, for example, a dataset where 95% of cases are negative and 5% are positive. Models trained on imbalanced data often default to predicting the majority class, which makes accuracy a misleading metric. Techniques like resampling, class weighting, and using metrics such as F1 or AUC are commonly used to address this.

**Target Variable**
The outcome a model is trained to predict. Also called the label or dependent variable.

**Train/Test Split**
The basic division of a dataset into a portion used for model training and a separate portion held out for evaluation. The test set should never influence any modeling decisions made during development.

**Data Leakage**
A situation in which information that would not be available at prediction time inadvertently influences model training, producing performance estimates that are unrealistically optimistic. Common forms include fitting a data scaler on the full dataset before splitting, including features derived from future observations, or using the test set to make modeling decisions. A persistent risk in AI-assisted research. Covered in [Chapters 15](../part2/ch15_data_preparation.md), [17](../part2/ch17_automl_tabular.md), [18](../part2/ch18_automl_timeseries.md), and [21](../part2/ch21_validation_interpretation.md).

**Forecasting**
Predicting future values of a variable based on its past observations. A forecasting problem differs from a general prediction problem in that the temporal order of observations matters and the output covers a future time window called the forecast horizon. Covered in [Chapter 18](../part2/ch18_automl_timeseries.md).

**Lag Feature**
A feature created by including the value of a variable at one or more previous time steps. Lag features give a model access to recent history when working with time series data, and how many lags to include depends on how far back the relevant signal extends in the domain. Covered in [Chapters 16](../part2/ch16_feature_engineering.md) and [18](../part2/ch18_automl_timeseries.md).

**Panel Data**
A dataset that tracks multiple subjects over time, also called longitudinal data. In time series forecasting with AutoGluon, each unique subject is called an item, and the full collection of items forms the panel. Covered in [Chapter 18](../part2/ch18_automl_timeseries.md).

**Confounding**
A variable that is associated with both the predictor and the outcome in a study, potentially creating a spurious or misleading relationship. Confounders are a risk in observational research and can make a model appear more predictive than it actually is if not accounted for in the analysis. Covered in [Chapter 21](../part2/ch21_validation_interpretation.md).

---

## Model Types and Architectures

**Large Language Models (LLMs)**
Models trained on large text corpora to understand and generate natural language. Examples include GPT-4, Llama 3, Claude, and Mistral.

**Transformers**
The neural network architecture that underlies most state-of-the-art NLP and vision models. Transformers use attention mechanisms to identify which parts of the input are most relevant to each output token.

**BERT (Bidirectional Encoder Representations from Transformers)**
A transformer-based language model introduced by Google in 2018 and trained using masked language modeling. BERT reads text bidirectionally, using context from both sides of each word simultaneously, which produces strong contextual representations. It became one of the first widely adopted foundation models for NLP tasks and is the basis for domain-adapted models such as BioBERT and SciBERT. Covered in [Chapters 20](../part2/ch20_pretrained_text_vision.md), [23](../part3/ch23_nlp_with_bert.md), and [26](../part3/ch26_llm_eval_finetuning.md).

**Vision Models**
Models trained to understand or generate visual data, including images and video. Examples include ResNet, Vision Transformer (ViT), and YOLO.

**Multimodal Models**
Models that process and connect multiple data types, such as text and images together. Examples include GPT-4o and Gemini.

**Gradient Boosting**
A supervised learning method that builds an ensemble of decision trees sequentially, with each tree correcting the errors of those before it. Gradient boosting methods, including LightGBM and XGBoost, are among the strongest performers on tabular data. AutoGluon uses gradient boosting as one of its core model families. Covered in [Chapter 17](../part2/ch17_automl_tabular.md).

**Random Forest**
A supervised learning method that trains many decision trees on random subsets of features and data and averages their predictions. Random forests are robust to overfitting and widely used as a strong baseline for tabular classification and regression. Covered in [Chapter 17](../part2/ch17_automl_tabular.md).

---

## Evaluation Metrics

**Accuracy**
The fraction of predictions a model gets correct. Accuracy is easy to interpret but can be misleading when class distributions are uneven. In a dataset where 95% of examples belong to one class, a model that always predicts that class achieves 95% accuracy without learning anything useful.

**Precision, Recall, and F1 Score**
Metrics for evaluating classifiers when class balance matters. Precision is the fraction of predicted positives that are actually positive. Recall is the fraction of actual positive cases that the model correctly identified. F1 score is the harmonic mean of precision and recall, summarizing the tradeoff between them. These metrics are more informative than accuracy alone when one class is much rarer than the other. Covered in [Chapters 21](../part2/ch21_validation_interpretation.md) and [26](../part3/ch26_llm_eval_finetuning.md).

**AUC-ROC**
Area under the receiver operating characteristic curve. A threshold-independent measure of how well a classifier separates the positive and negative classes across all possible decision thresholds. An AUC of 1.0 indicates perfect separation; 0.5 is equivalent to random guessing. Covered in [Chapter 21](../part2/ch21_validation_interpretation.md).

**MASE (Mean Absolute Scaled Error)**
The primary evaluation metric for time series forecasting in AutoGluon. MASE compares a model's forecast error against a naive seasonal baseline that simply repeats the last observed seasonal value. A MASE below 1.0 means the model is beating that baseline; above 1.0 means it is not. Because MASE is scale-free, it works well when comparing across series with different units or magnitudes. Covered in [Chapter 18](../part2/ch18_automl_timeseries.md).

**Prediction Interval**
A range within which a future observation is expected to fall with a stated probability. In time series forecasting, a prediction interval communicates uncertainty around a point forecast. An 80% prediction interval should contain the true value roughly 80% of the time in a well-calibrated model. Covered in [Chapter 18](../part2/ch18_automl_timeseries.md).

---

## AutoML and Automation

**AutoML**
Automated machine learning. Frameworks that automate parts of the model development pipeline, including model selection, hyperparameter tuning, and ensembling. AutoGluon, covered in [Chapter 17](../part2/ch17_automl_tabular.md), is an example.

**Hyperparameter**
A setting that controls how a model is trained, such as learning rate or the number of trees in a random forest. Hyperparameters are chosen by the researcher before training, not learned from the data.

**Hyperparameter Tuning**
The process of searching for the best combination of hyperparameters, either through grid search, random search, or more efficient methods like Bayesian optimization. AutoML frameworks handle this automatically.

**Ensemble**
A model that combines the predictions of multiple individual models, usually outperforming any single model on its own. Random forests and gradient boosting are both ensemble methods.

**Model Card**
A short document that describes a model's intended use, training data, performance characteristics, limitations, and ethical considerations. Model cards are a standard practice for responsible model sharing.

---

## NLP and Text Analysis

**Natural Language Processing (NLP)**
Methods that allow machines to understand and generate human language. Common tasks include summarization, translation, question answering, sentiment analysis, and named entity recognition.

**Named Entity Recognition (NER)**
An NLP task that identifies spans of text referring to named things and labels them by type, such as people, organizations, and locations. NER is used in research to extract entities from large document collections without reading them manually. Covered in [Chapters 20](../part2/ch20_pretrained_text_vision.md) and [23](../part3/ch23_nlp_with_bert.md).

**Semantic Search**
Retrieval based on meaning rather than exact keyword matching. A semantic search system converts both the query and the documents into embeddings and finds results based on conceptual closeness, even when the specific words differ. This is the core mechanism behind the retrieval step in RAG systems. Covered in [Chapters 5](../part1/ch05_literature_review.md) and [24](../part3/ch24_rag.md).

**Semantic Similarity**
A measure of how alike two pieces of text are in meaning, independent of whether they share the same words. Computed using embeddings: two texts are semantically similar when their vector representations are close together in the embedding space. Useful for grouping open-ended responses, deduplication, and document retrieval. Covered in [Chapter 23](../part3/ch23_nlp_with_bert.md).

**Zero-Shot Classification**
Applying a model to a classification task without providing any labeled training examples for the specific categories. The model uses its pretraining knowledge to assign texts to user-defined labels described in natural language. Useful when collecting labeled examples would be costly and the categories can be described clearly in plain text. Covered in [Chapters 20](../part2/ch20_pretrained_text_vision.md) and [23](../part3/ch23_nlp_with_bert.md).

**Chunking**
Splitting a document into smaller pieces before embedding and indexing them in a RAG system. Chunk boundaries affect what the retrieval step can find: a relevant passage that spans two chunks might only return half as context. Common strategies include splitting by character count, paragraph, or section header. Covered in [Chapter 24](../part3/ch24_rag.md).

**Vector Database**
A specialized storage system designed to efficiently index and search high-dimensional embedding vectors. Unlike a relational database that matches on exact field values, a vector database finds entries whose embeddings are closest to a query embedding. Common examples include ChromaDB and FAISS. Covered in [Chapter 24](../part3/ch24_rag.md).

---

## Computer Vision

**Computer Vision (CV)**
Methods that enable machines to interpret visual data. Common tasks include image classification, object detection, image segmentation, and image generation.

**Object Detection**
A computer vision task that locates specific objects within an image and draws bounding boxes around them. Unlike image classification, which assigns a single label to an entire image, object detection identifies both what is in the image and where each object is. Grounding DINO is an example of a zero-shot object detection model. Covered in [Chapter 20](../part2/ch20_pretrained_text_vision.md).

**Image Segmentation**
A computer vision task that identifies which pixels belong to which object, producing precise outlines rather than bounding boxes. Useful when exact object boundaries matter, such as cell segmentation in microscopy images. The Segment Anything Model (SAM) is a prominent example. Covered in [Chapter 20](../part2/ch20_pretrained_text_vision.md).

**Multimodal AI**
Models that work with more than one data type at the same time, such as text combined with images or text combined with audio. These models support tasks like visual question answering and document understanding.

---

## Prompting and LLM Interaction

**Prompting**
Crafting the text input that guides a language model's output. This includes simple instructions, system messages, structured formats, and chain-of-thought prompts. Covered in depth in [Chapter 3](../part1/ch03_prompt_engineering.md).

**Zero-Shot Prompting**
Giving a language model a task description with no examples and asking it to produce the output directly. Works well for tasks the model has encountered many variations of during training. Covered in [Chapter 3](../part1/ch03_prompt_engineering.md).

**Few-Shot Prompting**
Providing one or more examples of the desired output before asking the model to produce something similar. The examples serve as a template, showing the model the format, tone, and level of detail expected. Useful when the task is unusual or requires a specific style the model would not naturally produce without guidance. Covered in [Chapter 3](../part1/ch03_prompt_engineering.md).

**Chain-of-Thought Prompting**
A prompting technique that asks the model to reason through a problem step by step before giving its final answer. Intermediate steps become context for subsequent ones, which tends to produce more coherent reasoning and makes errors easier to spot. Covered in [Chapter 3](../part1/ch03_prompt_engineering.md).

**System Message**
An instruction provided to an LLM that sets its role, tone, or constraints for a conversation. Used to customize model behavior without being part of the user-facing conversation.

**Retrieval-Augmented Generation (RAG)**
A technique where an LLM retrieves relevant documents from a knowledge base before generating a response. RAG reduces hallucination and allows a model to work with information it was not trained on. Maizey, UM's document assistant, is a RAG system. Covered in depth in [Chapter 24](../part3/ch24_rag.md).

---

## Agents and Multi-Step Workflows

**AI Agent**
A system that can pursue a goal over multiple steps by planning, calling tools, and adjusting its approach based on what it observes. Unlike a single language model interaction, an agent can execute code, retrieve documents, and search the web, maintaining a record of what has already happened across a multi-step task. Covered in [Chapter 25](../part3/ch25_ai_agents.md).

**Context Engineering**
The practice of deliberately designing everything that goes into a model's context window at each step of a multi-step task. In agent workflows, context engineering involves deciding what task description, prior results, retrieved documents, and output format instructions to include at each point. The quality of context at each step is often more important than the sophistication of the framework used. Covered in [Chapter 25](../part3/ch25_ai_agents.md).

**Tool Use**
An agent's ability to call external functions or APIs as part of completing a task, such as searching the web, running code, reading files, or querying a database. Tool use is what gives agents the ability to act rather than just describe. Covered in [Chapter 25](../part3/ch25_ai_agents.md).

---

## Fine-Tuning and Adaptation

**LoRA (Low-Rank Adaptation)**
A parameter-efficient fine-tuning method that adds small trainable matrices alongside the frozen weights of a pretrained model rather than updating all parameters. LoRA typically trains less than one percent of a model's total parameters while achieving results competitive with full fine-tuning on many tasks, making it practical on limited hardware. Covered in [Chapter 26](../part3/ch26_llm_eval_finetuning.md).

**PEFT (Parameter-Efficient Fine-Tuning)**
A family of methods for adapting a pretrained model to a new task while updating only a small fraction of its parameters. LoRA is the most widely used approach in this family. PEFT makes fine-tuning practical on academic-scale hardware and produces compact adapters that can be stored and shared separately from the base model. Covered in [Chapter 26](../part3/ch26_llm_eval_finetuning.md).

---

## Research Compliance and Ethics

**IRB (Institutional Review Board)**
A committee that reviews research involving human subjects to ensure ethical treatment, privacy protection, and informed consent. IRB review may be required even when researchers are using existing datasets rather than collecting new data, if those datasets contain identifiable information about living individuals. Covered in [Chapters 10](../part1/ch10_ethics_privacy.md) and [12](../part2/ch12_data_access.md).

**Data Use Agreement (DUA)**
A legal agreement specifying how a dataset may be used, where it may be stored, who may access it, and what happens to it at the end of a project. Many restricted or licensed datasets require a signed DUA before access is granted. DUAs often predate large language models and may not explicitly address whether data can be processed through AI tools without additional approval. Covered in [Chapters 10](../part1/ch10_ethics_privacy.md) and [12](../part2/ch12_data_access.md).

**HIPAA**
The Health Insurance Portability and Accountability Act. A U.S. federal law governing the collection, storage, and use of protected health information. Research involving patient records, clinical data, or any health information that could be linked to an individual typically requires HIPAA compliance, including use of a computing environment specifically approved for that data type. Covered in [Chapters 10](../part1/ch10_ethics_privacy.md) and [12](../part2/ch12_data_access.md).

**Algorithmic Bias**
The tendency of AI models to produce systematically different outcomes for different demographic groups, often because training data reflects historical inequities or underrepresents certain populations. Bias can arise from data selection, proxy variables, or evaluation metrics that mask performance gaps across subgroups. Covered in [Chapter 10](../part1/ch10_ethics_privacy.md).


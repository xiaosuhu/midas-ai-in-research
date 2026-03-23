# AI Literacy Glossary

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

## High-Level Application Areas

**Natural Language Processing (NLP)**
Methods that allow machines to understand and generate human language. Common tasks include summarization, translation, question answering, and sentiment analysis.

**Computer Vision (CV)**
Methods that enable machines to interpret visual data. Common tasks include image classification, object detection, image segmentation, and image generation.

**Multimodal AI**
Models that work with more than one data type at the same time, such as text combined with images or text combined with audio. These models support tasks like visual question answering and document understanding.

---

## Core Concepts and Techniques

**Neural Networks**
Computational structures composed of interconnected layers of units, often called neurons. Neural networks form the basis of most modern machine learning models.

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
Adapting a pre-trained model to a specific dataset or task, rather than training a model from scratch. Fine-tuning is often much more efficient than full training and is widely used for adapting LLMs to specialized domains.

**Embeddings**
Numeric vector representations of text, images, or other data that capture their semantic meaning. Two items with similar meanings end up close together in the embedding space, which is what makes search and retrieval systems work.

**Inference**
The process of using a trained model to generate predictions or outputs on new data. Distinct from training, which adjusts the model's parameters.

**Hallucination**
When a language model produces confident-sounding but incorrect or fabricated information. Hallucinations are a well-documented limitation of LLMs and one of the main reasons that human review of AI-generated content remains important.

**Token**
A small unit of text that LLMs process, typically a word fragment or a punctuation mark. Computational cost and speed for LLM tasks both scale with token count.

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

---

## Model Types and Architectures

**Large Language Models (LLMs)**
Models trained on large text corpora to understand and generate natural language. Examples include GPT-4, Llama 3, Claude, and Mistral.

**Transformers**
The neural network architecture that underlies most state-of-the-art NLP and vision models. Transformers use attention mechanisms to identify which parts of the input are most relevant to each output token.

**Vision Models**
Models trained to understand or generate visual data, including images and video. Examples include ResNet, Vision Transformer (ViT), and YOLO.

**Multimodal Models**
Models that process and connect multiple data types, such as text and images together. Examples include GPT-4o and Gemini.

---

## AutoML and Model Evaluation

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

## Prompting and LLM-Specific Terms

**Prompting**
Crafting the text input that guides a language model's output. This includes simple instructions, system messages, structured formats, and chain-of-thought prompts.

**Retrieval-Augmented Generation (RAG)**
A technique where an LLM retrieves relevant documents from a knowledge base before generating a response. RAG reduces hallucination and allows a model to work with information it was not trained on. Maizey, UM's document assistant, is a RAG system.

**System Message**
An instruction provided to an LLM that sets its role, tone, or constraints for a conversation. Used to customize model behavior without being part of the user-facing conversation.

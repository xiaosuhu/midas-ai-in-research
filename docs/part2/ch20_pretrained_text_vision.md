# Chapter 20: Pre-trained Models for Text and Vision

The previous chapters focused on AutoML workflows where you bring your own labeled dataset and AutoGluon handles the modeling. Chapter 19 is a good example: you provide labeled rows, and AutoGluon fine-tunes a pretrained backbone on your prediction task. That approach makes sense when your goal is prediction and you have the labeled data to train on.

But a lot of research work does not look like that. Sometimes you have no labeled data at all. Sometimes your goal is not prediction but understanding: you want to make sense of interview transcripts, organize field photographs, or translate survey responses collected in three different languages. For these kinds of tasks, the most practical first question is not "how do I train a model?" but rather "is there already a model that does this?"

The answer is often yes. The machine learning community has produced a large ecosystem of pre-trained models, many of them freely available through [Hugging Face](https://huggingface.co). Hugging Face is a platform that hosts tens of thousands of open-source models, datasets, and interactive browser-based demos. You can browse models by task, read documentation, and in many cases test them directly in your browser before writing a single line of code. Think of it as a model library combined with a sandbox.

This chapter introduces a set of these models across two modalities: text and vision. The goal is partly to show you what is out there, and partly to build the habit of checking for a pre-trained solution before committing to building your own. That instinct will save you considerable time.

---

## Text Analysis with Pre-trained Models

### Background: The Transformer Paradigm

Most modern text AI models share a common architectural foundation called the transformer, introduced by Vaswani and colleagues in 2017 {cite}`ch20-vaswani2017attention`. The core innovation was an attention mechanism: rather than reading text word by word in sequence, the model learns which words are most relevant to each other across an entire sentence or passage. This allowed models to capture long-range dependencies in language far more effectively than earlier approaches.

Building on this foundation, Devlin and colleagues introduced BERT (Bidirectional Encoder Representations from Transformers) in 2019 {cite}`ch20-devlin2019bert`. What made BERT distinctive was that it reads text in both directions simultaneously, considering the full context around every word rather than only what comes before. BERT was pre-trained on a large amount of text using a masked prediction task, where the model learned to fill in randomly hidden words based on surrounding context. This produced a general-purpose language understanding model that could then be adapted to almost any text task with minimal additional training.

BERT became the blueprint for a generation of specialized models. The models you will encounter in this chapter, including BART for summarization and classification, RoBERTa for sentiment analysis, and embedding models for semantic similarity, are all built on the same transformer foundation that BERT helped establish. Chapter 23 goes deeper into how BERT works and how you can fine-tune it for your own research tasks.

### Model Overview

The table below summarizes the six pre-trained text models covered in this chapter, organized by the kind of task they are best suited for.

| Model | Task | What it does | Research uses |
|---|---|---|---|
| **EmbeddingGemma-300M** | Semantic similarity | Converts text into vectors that reflect meaning | Clustering open-ended responses; deduplication; similarity search |
| **BART-Large-MNLI** | Zero-shot classification | Assigns user-defined labels without any training data | Thematic coding; filtering interview excerpts; sorting policy documents |
| **Helsinki-NLP / OPUS-MT** | Machine translation | Translates between specific language pairs | Multilingual interviews; cross-regional comparative research |
| **BART-Large-CNN** | Summarization | Produces concise summaries of long documents | Triaging reports, interviews, and policy texts |
| **BERT Base Uncased** | General language understanding | Foundation model for sentence context and masked prediction | Named entity recognition; document classification; basis for fine-tuning |
| **CardiffNLP Twitter RoBERTa** | Sentiment analysis | Classifies sentiment in informal text including slang and emoji | Social media monitoring; public perception studies |

### Using These Models

**Semantic similarity and clustering.** When you have a large collection of open-ended responses and want to see how they group together conceptually, embedding models are the right starting point. EmbeddingGemma-300M converts each piece of text into a numerical vector that positions similar ideas close together in a high-dimensional space. The model captures meaning beyond surface wording, so responses like "I felt overwhelmed by the workload" and "there was too much to handle" would land near each other even though they share almost no words. From there, you can apply clustering algorithms to identify natural groupings, or calculate how conceptually close any two documents are to each other. This kind of analysis is especially useful in early-stage qualitative work, before you have settled on a coding scheme.

**Zero-shot classification.** BART-Large-MNLI lets you assign labels to text without needing any labeled training data at all. You simply provide the categories you want, and the model decides which one fits best. A policy researcher might provide labels like "economic concerns," "housing access," or "climate policy" and apply them to hundreds of interview excerpts in minutes. The model uses natural-language inference internally, comparing each piece of text against each candidate label to determine the best match. The main thing to watch out for is label phrasing: vague or overlapping labels tend to produce inconsistent results, so it helps to test a few phrasings before running across a full dataset.

**Machine translation.** The Helsinki-NLP OPUS-MT models are trained on public multilingual corpora and optimized for specific language pairs, with separate models available for hundreds of combinations. For researchers working with multilingual data, these models offer a transparent, open-source alternative to commercial translation APIs. They are particularly well-suited to translating interviews, field notes, or survey responses into a shared analysis language while preserving a clear record of what was translated and how.

**Summarization.** BART-Large-CNN is an abstractive summarization model, meaning it generates a new condensed version of a document rather than extracting sentences verbatim. This is useful for quickly determining whether a long report or interview is relevant to your research question before reading it in full. Summarization also works well as a preprocessing step: generating summaries first and then applying classification or clustering to the summaries rather than the full documents can significantly speed up analysis of large corpora.

**Sentiment analysis.** CardiffNLP Twitter RoBERTa is a fine-tuned version of RoBERTa, trained specifically on tweet data to handle informal writing, slang, emojis, and sarcasm that standard sentiment models tend to misclassify. For researchers studying public attitudes at scale, whether through social media, online reviews, or open survey responses, this model provides a fast baseline for understanding the emotional tone of text before moving into deeper qualitative analysis.

---

## Computer Vision with Pre-trained Models

### Background

Computer vision tasks are not all the same kind of problem, and it helps to understand the distinctions before choosing a model. The four main task types represented in this chapter are image classification (what category does this image belong to?), object detection (where are specific objects located within the image?), image segmentation (which pixels belong to which object?), and visual question answering (what can you infer from the content of this image?). Each type produces a different kind of output and suits different research scenarios. The sections below introduce one representative model for each task type.

### Image Classification: Vision Transformer (ViT)

Image classification assigns a single label to an entire image. The Vision Transformer (ViT) applies the same attention mechanism from the text transformer architecture to images by breaking a photograph into fixed-size patches and analyzing them jointly. This gives ViT strong generalization across diverse image types without requiring specialized preprocessing.

For research purposes, ViT is a good starting point when you have a large collection of images that need to be sorted or labeled quickly and you are not yet sure whether a custom model is necessary. You can test it directly in your browser via the [Hugging Face model page](https://huggingface.co/google/vit-base-patch16-224). The main constraint is that the model produces a single category label per image and cannot tell you where within the image something appears or how many instances there are.

**Example.** A field ecologist working with thousands of camera trap photographs can use ViT to quickly separate images into broad categories such as animal present, empty frame, or camera malfunction, before moving into species-level analysis.

### Object Detection: Grounding DINO

Object detection goes further than classification by locating specific objects within an image and drawing bounding boxes around them. Grounding DINO is a zero-shot detection model, meaning you describe what you are looking for in plain language and the model finds it without needing any labeled training examples. You might ask it to locate "solar panels" in a satellite image, or "protective equipment" in a set of workplace photographs, and it will return bounding boxes around the matching regions. You can try it at the [Hugging Face demo](https://huggingface.co/spaces/merve/Grounding_DINO_demo).

The key strength here is flexibility. Because the model accepts free-form natural language descriptions rather than fixed class lists, you can adapt it to unusual object types or domain-specific terminology that a standard detection model might not recognize. The trade-off is speed: Grounding DINO is slower than specialized detectors trained for a narrow task.

**Example.** Environmental scientists monitoring land use change can use Grounding DINO to locate wind turbines or solar installations across large satellite image archives, without building a custom training dataset from scratch.

### Image Segmentation: Segment Anything (SAM)

Segmentation goes beyond bounding boxes to identify which individual pixels belong to a given object, producing precise outlines rather than rectangular regions. The Segment Anything Model (SAM), developed by Meta AI, can segment objects across essentially any image domain without retraining. You can interact with it through clicks, bounding boxes, or by asking it to automatically propose segments for an entire image. A browser demo is available at [segment-anything.com](https://segment-anything.com/demo).

The important limitation to keep in mind is that SAM identifies and outlines objects without naming them. It can tell you where things are, but not what they are. In practice this is often used as a first step, with a classification model applied afterward to label each segmented region.

**Example.** Microbiologists use SAM to automatically outline individual cells in microscopy images, replacing hours of manual tracing and making much larger sample sizes practical.

### Visual Question Answering: Qwen-VL

Visual question answering models can read an image and respond to open-ended questions about its content. Qwen-VL (part of the Qwen3 model family) takes both an image and a natural-language question as input and generates a descriptive answer. You can ask it things like "What kind of vegetation is in this photograph?" or "Is the person in this image wearing protective equipment?" and receive a text response. A browser demo is available on [Hugging Face Spaces](https://huggingface.co/spaces/Qwen/Qwen3-VL-Demo).

This kind of model is useful for exploratory analysis of visual materials, rapid documentation of image collections, and generating structured descriptions at scale. The main caveat is that accuracy varies depending on image quality and how familiar the content is to the model, so results should be spot-checked rather than taken at face value.

**Example.** Researchers working with historical photograph archives can use Qwen-VL to generate preliminary descriptive metadata for large collections, then review and correct the outputs manually.

### Vision Model Comparison

| Model | Task type | Output | Strengths | Limitations | Research uses |
|---|---|---|---|---|---|
| **ViT** | Classification | Single label per image | Strong baseline; efficient; generalizes well | No localization or segmentation | Sorting large image collections; rapid labeling |
| **Grounding DINO** | Object detection | Bounding boxes | Zero-shot; accepts natural language | Slower than specialized detectors | Mapping objects in satellite images; locating domain-specific items |
| **SAM** | Segmentation | Pixel-level masks | Precise outlines; domain-agnostic; no training required | Does not label objects | Cell segmentation; region identification in scientific images |
| **Qwen-VL** | Visual Q&A | Text response | Open-ended; flexible; integrates vision and language | Variable accuracy; higher compute needs | Documentation; exploratory analysis; metadata generation |

---

*Last reviewed: March 2026. Tool-specific content in this chapter refers to the Hugging Face Transformers ecosystem. Model availability and browser interfaces on platforms like Hugging Face Spaces change frequently. If you notice outdated content, [open an issue on GitHub](https://github.com/xiaosuhu/midas-ai-in-research/issues).*

```{bibliography}
:filter: docname in docnames
:keyprefix: ch20-
```

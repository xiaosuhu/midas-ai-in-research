# Chapter 20: Pre-trained Models for Text, Vision, and Audio

:::{admonition} What you will learn
:class: tip

By the end of this chapter, you will be able to:

- Recognize when an existing pre-trained model is the right starting point, rather than building or training your own
- Navigate Hugging Face to find, evaluate, and test models directly in your browser before writing any code
- Match common text analysis tasks (semantic similarity, zero-shot classification, translation, summarization, and sentiment analysis) to appropriate pre-trained models
- Match common computer vision tasks (image classification, object detection, segmentation, and visual question answering) to appropriate pre-trained models
- Use CLIP and BioCLIP for zero-shot image classification when labeled training data is not available
- Transcribe audio recordings with Whisper and recognize where its output needs human review before research use
- Distinguish between analytical models, which extract information from existing data, and generative models, which produce new content, and choose accordingly for your research task
:::

The previous chapters focused on AutoML workflows where you bring your own labeled dataset and AutoGluon handles the modeling. Chapter 19 is a good example: you provide labeled rows, and AutoGluon fine-tunes a pretrained backbone on your prediction task. That approach makes sense when your goal is prediction and you have the labeled data to train on.

But a lot of research work does not look like that. Sometimes you have no labeled data at all. Sometimes your goal is not prediction but understanding: you want to make sense of interview transcripts, organize field photographs, or translate survey responses collected in three different languages. For these kinds of tasks, the most practical first question is not "how do I train a model?" but rather "is there already a model that does this?"

The answer is often yes. The machine learning community has produced a large ecosystem of pre-trained models, many of them freely available through [Hugging Face](https://huggingface.co). Hugging Face is a platform that hosts tens of thousands of open-source models, datasets, and interactive browser-based demos. You can browse models by task, read documentation, and in many cases test them directly in your browser before writing a single line of code. Think of it as a model library combined with a sandbox.

This chapter introduces a set of these models across text, vision, and audio. The goal is partly to show you what is out there, and partly to build the habit of checking for a pre-trained solution before committing to building your own. That instinct will save you considerable time.

One distinction worth keeping in mind as you read: the models here fall into two broad categories. Most of them are analytical, meaning they take existing data and extract information from it. A smaller set are generative, meaning they produce new content such as synthesized images or spoken audio. The two types serve different research purposes and come with different considerations around validation and appropriate use. The chapter flags this distinction as it comes up.

---

## Text Analysis with Pre-trained Models

### Background: The Transformer Paradigm

Most modern text AI models share a common architectural foundation called the transformer, introduced by Vaswani and colleagues in 2017 {cite}`ch20-vaswani2017attention`. The core innovation was an attention mechanism: rather than reading text word by word in sequence, the model learns which words are most relevant to each other across an entire sentence or passage. This allowed models to capture long-range dependencies in language far more effectively than earlier approaches.

Building on this foundation, Devlin and colleagues introduced BERT (Bidirectional Encoder Representations from Transformers) in 2019 {cite}`ch20-devlin2019bert`. What made BERT distinctive was that it reads text in both directions simultaneously, considering the full context around every word rather than only what comes before. BERT was pre-trained on a large amount of text using a masked prediction task, where the model learned to fill in randomly hidden words based on surrounding context. This produced a general-purpose language understanding model that could then be adapted to almost any text task with minimal additional training.

BERT became the blueprint for a generation of specialized models. The models you will encounter in this chapter, including BART for summarization and classification {cite}`ch20-lewis2020bart`, RoBERTa for sentiment analysis {cite}`ch20-liu2019roberta`, and embedding models for semantic similarity, are all built on the same transformer foundation that BERT helped establish. Chapter 23 goes deeper into how BERT works and how you can fine-tune it for your own research tasks.

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

**Semantic similarity and clustering.** When you have a large collection of open-ended responses and want to see how they group together conceptually, embedding models are the right starting point. EmbeddingGemma-300M {cite}`ch20-embedding_gemma_2025` converts each piece of text into a numerical vector that positions similar ideas close together in a high-dimensional space. The model captures meaning beyond surface wording, so responses like "I felt overwhelmed by the workload" and "there was too much to handle" would land near each other even though they share almost no words. From there, you can apply clustering algorithms to identify natural groupings, or calculate how conceptually close any two documents are to each other. This kind of analysis is especially useful in early-stage qualitative work, before you have settled on a coding scheme.

**Zero-shot classification.** BART-Large-MNLI lets you assign labels to text without needing any labeled training data at all. You simply provide the categories you want, and the model decides which one fits best. A policy researcher might provide labels like "economic concerns," "housing access," or "climate policy" and apply them to hundreds of interview excerpts in minutes. The model uses natural-language inference internally, comparing each piece of text against each candidate label to determine the best match. The main thing to watch out for is label phrasing: vague or overlapping labels tend to produce inconsistent results, so it helps to test a few phrasings before running across a full dataset.

**Machine translation.** The Helsinki-NLP OPUS-MT models are trained on public multilingual corpora and optimized for specific language pairs, with separate models available for hundreds of combinations {cite}`ch20-tiedemann2020opusmt`. For researchers working with multilingual data, these models offer a transparent, open-source alternative to commercial translation APIs. They are particularly well-suited to translating interviews, field notes, or survey responses into a shared analysis language while preserving a clear record of what was translated and how.

**Summarization.** BART-Large-CNN is an abstractive summarization model, meaning it generates a new condensed version of a document rather than extracting sentences verbatim. This is useful for quickly determining whether a long report or interview is relevant to your research question before reading it in full. Summarization also works well as a preprocessing step: generating summaries first and then applying classification or clustering to the summaries rather than the full documents can significantly speed up analysis of large corpora.

**Sentiment analysis.** CardiffNLP Twitter RoBERTa is a fine-tuned version of RoBERTa {cite}`ch20-liu2019roberta`, trained specifically on tweet data to handle informal writing, slang, emojis, and sarcasm that standard sentiment models tend to misclassify {cite}`ch20-barbieri2020tweeteval`. For researchers studying public attitudes at scale, whether through social media, online reviews, or open survey responses, this model provides a fast baseline for understanding the emotional tone of text before moving into deeper qualitative analysis.

---

## Computer Vision with Pre-trained Models

### Background

Computer vision tasks are not all the same kind of problem, and it helps to understand the distinctions before choosing a model. The four main task types represented in this chapter are image classification (what category does this image belong to?), object detection (where are specific objects located within the image?), image segmentation (which pixels belong to which object?), and visual question answering (what can you infer from the content of this image?). Each type produces a different kind of output and suits different research scenarios. The sections below introduce one representative model for each task type.

### Image Classification: Vision Transformer (ViT)

Image classification assigns a single label to an entire image. The Vision Transformer (ViT) applies the same attention mechanism from the text transformer architecture to images by breaking a photograph into fixed-size patches and analyzing them jointly {cite}`ch20-dosovitskiy2021vit`. This gives ViT strong generalization across diverse image types without requiring specialized preprocessing.

For research purposes, ViT is a good starting point when you have a large collection of images that need to be sorted or labeled quickly and you are not yet sure whether a custom model is necessary. You can test it directly in your browser via the [Hugging Face model page](https://huggingface.co/google/vit-base-patch16-224). The main constraint is that the model produces a single category label per image and cannot tell you where within the image something appears or how many instances there are.

**Example.** A field ecologist working with thousands of camera trap photographs can use ViT to quickly separate images into broad categories such as animal present, empty frame, or camera malfunction, before moving into species-level analysis.

### Zero-Shot Image Classification: CLIP and BioCLIP

ViT requires labeled training examples to classify images into your categories. CLIP (Contrastive Language-Image Pretraining), developed by OpenAI, takes a different approach {cite}`ch20-radford2021clip`. Instead of learning fixed categories, CLIP learns a shared embedding space where images and text descriptions are aligned. This means you can classify images using natural language prompts without any retraining. You write out candidate labels as short descriptions, such as "a photograph of dense forest" or "an aerial view of urban development," and CLIP ranks each image against those descriptions based on similarity.

This zero-shot capability is particularly useful when your categories are still evolving, when labeled training data is hard to collect, or when you are doing exploratory work and want to test several classification schemes before committing to one. A browser demo is available through [OpenCLIP on Hugging Face](https://huggingface.co/spaces/mlunar/open-clip-explorer).

For ecological and biodiversity research, BioCLIP offers a domain-specific alternative {cite}`ch20-stevens2024bioclip`. It is fine-tuned on a large collection of biological specimen images spanning hundreds of thousands of taxa, which gives it a significant advantage over general CLIP for species-level identification. Researchers working with camera trap images, herbarium specimens, or field photographs can apply BioCLIP to species identification tasks where general-purpose models tend to struggle with fine-grained visual distinctions within a taxon. A demo is available on [Hugging Face](https://huggingface.co/imageomics/bioclip).

The practical choice between ViT and CLIP comes down to whether you have labeled data. When labeled examples exist and categories are well-defined, a fine-tuned ViT will usually perform better. When you are exploring or when your categories are unusual, CLIP gets you started immediately without any labeling effort.

**Example.** A researcher studying urban green space could classify satellite image patches into categories such as tree canopy, grass, impervious surface, and water by writing those descriptions as text prompts, with no need to collect labeled training images.

### Object Detection: Grounding DINO

Object detection goes further than classification by locating specific objects within an image and drawing bounding boxes around them. Grounding DINO is a zero-shot detection model, meaning you describe what you are looking for in plain language and the model finds it without needing any labeled training examples {cite}`ch20-liu2023groundingdino`. You might ask it to locate "solar panels" in a satellite image, or "protective equipment" in a set of workplace photographs, and it will return bounding boxes around the matching regions. You can try it at the [Hugging Face demo](https://huggingface.co/spaces/merve/Grounding_DINO_demo).

The key strength here is flexibility. Because the model accepts free-form natural language descriptions rather than fixed class lists, you can adapt it to unusual object types or domain-specific terminology that a standard detection model might not recognize. The trade-off is speed: Grounding DINO is slower than specialized detectors trained for a narrow task.

**Example.** Environmental scientists monitoring land use change can use Grounding DINO to locate wind turbines or solar installations across large satellite image archives, without building a custom training dataset from scratch.

### Image Segmentation: Segment Anything (SAM)

Segmentation goes beyond bounding boxes to identify which individual pixels belong to a given object, producing precise outlines rather than rectangular regions. The Segment Anything Model (SAM), developed by Meta AI, can segment objects across essentially any image domain without retraining {cite}`ch20-kirillov2023sam`. You can interact with it through clicks, bounding boxes, or by asking it to automatically propose segments for an entire image. A browser demo is available at [segment-anything.com](https://segment-anything.com/demo).

The important limitation to keep in mind is that SAM identifies and outlines objects without naming them. It can tell you where things are, but not what they are. In practice this is often used as a first step, with a classification model applied afterward to label each segmented region.

**Example.** Microbiologists use SAM to automatically outline individual cells in microscopy images, replacing hours of manual tracing and making much larger sample sizes practical.

### Visual Question Answering: Qwen3-VL

Visual question answering models can read an image and respond to open-ended questions about its content. Qwen3-VL, the latest generation of Alibaba's Qwen vision-language series {cite}`ch20-wang2024qwenvl`, takes both an image and a natural-language question as input and generates a descriptive answer. You can ask it things like "What kind of vegetation is in this photograph?" or "Is the person in this image wearing protective equipment?" and receive a text response. A browser demo is available on [Hugging Face Spaces](https://huggingface.co/spaces/Qwen/Qwen3-VL-Demo).

This kind of model is useful for exploratory analysis of visual materials, rapid documentation of image collections, and generating structured descriptions at scale. The main caveat is that accuracy varies depending on image quality and how familiar the content is to the model, so results should be spot-checked rather than taken at face value.

**Example.** Researchers working with historical photograph archives can use Qwen3-VL to generate preliminary descriptive metadata for large collections, then review and correct the outputs manually.

### Image Captioning: BLIP

The models above either assign predefined categories to images or answer specific questions about them. BLIP (Bootstrapping Language-Image Pre-training) serves a different purpose: it generates free-text descriptions of image content without requiring a prompt {cite}`ch20-li2022blip`. Given an image, BLIP produces a sentence or two describing what it sees, which makes it practical for generating descriptive metadata at scale, creating alt-text for figures, or producing text that downstream NLP tools can then process and analyze.

For researchers managing large archives of photographs, microscopy images, or field images, this captioning capability offers a way to make visual material searchable and summarizable without writing descriptions by hand. BLIP also supports visual question answering, but where Qwen3-VL handles open-ended and complex reasoning tasks, BLIP is generally more efficient for straightforward captioning workflows where you want a description of image content rather than an answer to a specific question. A browser demo is available at [Hugging Face Spaces](https://huggingface.co/spaces/Salesforce/BLIP).

**Example.** A researcher archiving a large collection of field survey photographs could use BLIP to generate draft descriptions for each image, then review and correct the outputs rather than composing them from scratch.

### Vision Model Comparison

| Model | Task type | Output | Strengths | Limitations | Research uses |
|---|---|---|---|---|---|
| **ViT** | Classification | Single label per image | Strong baseline; efficient; generalizes well | Requires labeled data for fine-tuning | Sorting large image collections; rapid labeling |
| **CLIP / BioCLIP** | Zero-shot classification | Label + similarity score | No labeled data needed; flexible text prompts; BioCLIP specialized for species | Weaker than fine-tuned models on narrow tasks | Exploratory labeling; biodiversity identification |
| **Grounding DINO** | Object detection | Bounding boxes | Zero-shot; accepts natural language | Slower than specialized detectors | Mapping objects in satellite images; locating domain-specific items |
| **SAM** | Segmentation | Pixel-level masks | Precise outlines; domain-agnostic; no training required | Does not label objects | Cell segmentation; region identification in scientific images |
| **BLIP** | Image captioning | Descriptive text | Generates natural descriptions without prompting | Less capable than Qwen3-VL for complex reasoning | Metadata generation; making image archives searchable |
| **Qwen3-VL** | Visual Q&A | Text response | Open-ended; flexible; integrates vision and language | Variable accuracy; higher compute needs | Documentation; exploratory analysis; metadata generation |

---

## Audio: Transcription and Speech

Many researchers work with audio and never think of it as something a pre-trained model could handle. Recorded interviews, focus group sessions, conference presentations, and oral history archives all contain information that typically requires manual transcription before it can be analyzed. Whisper, developed by OpenAI, changes that considerably {cite}`ch20-radford2023whisper`.

Whisper is a speech recognition model trained on a large and diverse corpus of audio from the web, covering many languages and acoustic conditions. It converts spoken audio into text with accuracy strong enough for most research transcription tasks, and it handles background noise, varied accents, and technical vocabulary better than earlier automatic systems. Because the model is open and can be run locally, it is suitable for sensitive research contexts where recordings should not leave your institution's infrastructure. You can access it through the [Hugging Face model page](https://huggingface.co/openai/whisper-large-v3), and Chapter 13 covers the compute options for running it on Great Lakes or a local GPU.

The main limitation worth knowing about is overlapping speakers. Whisper transcribes what it hears but does not automatically separate multiple voices, which means focus group recordings or panel discussions may need post-processing to attribute speech to individual participants. For single-speaker recordings such as individual interviews or lectures, accuracy is generally strong enough to use directly in qualitative analysis, with a round of human review to catch errors in domain-specific terminology.

Beyond transcription, text-to-speech models can convert written text back into natural-sounding audio. This has practical applications in research communication: generating narration for video presentations, producing accessible audio versions of written materials, or creating spoken instructions for experiments. Tools like Bark (open-source) and ElevenLabs (commercial) offer this capability through simple interfaces. For most research workflows this is a secondary application, but the option is there when you need it.

---

## Image Generation: Stable Diffusion

The models covered so far in this chapter are all analytical: they take existing data and extract information from it. Stable Diffusion works differently. It is a generative model that produces new images from text descriptions {cite}`ch20-rombach2022ldm`, which puts it in the same broad category as large language models, just for visual content rather than text.

The underlying mechanism is a diffusion process: the model starts from random noise and iteratively refines it, guided by the meaning of your prompt, until a coherent image emerges. Stable Diffusion is open-source and can run on consumer hardware with a modest GPU, which makes it more accessible than many proprietary image generation systems.

For researchers, the most useful applications are not about generating photorealistic images as evidence, but rather about producing visual communication materials faster than traditional illustration workflows would allow. An ecologist explaining habitat fragmentation, a social scientist visualizing a theoretical concept, or an educator building teaching slides can all use image generation to produce conceptual diagrams and placeholder figures without commissioning custom illustrations or spending hours in design software. The model is also used in computer vision research to generate synthetic training data for scenarios that are difficult to photograph in the real world, though results should always be validated against real images before drawing conclusions.

Because Stable Diffusion can run locally, it is appropriate for research settings where visual materials involve sensitive topics or proprietary content that should not be sent to external services. Graphical interfaces like Automatic1111 and ComfyUI make it usable without writing code. A cloud-based option is available through [Hugging Face Spaces](https://huggingface.co/spaces/stabilityai/stable-diffusion).

One boundary that matters for research use: generated images should not be presented as photographs or data. They are production tools for communication and experimentation. Journals and conferences increasingly have explicit policies about AI-generated figures, and the right practice is always to disclose when generated imagery appears in a submission. Chapter 7 discusses this in the context of research writing and communication.

---

*Last reviewed: May 2026. Tool-specific content in this chapter refers to the Hugging Face Transformers ecosystem. Model availability and browser interfaces on platforms like Hugging Face Spaces change frequently. If you notice outdated content, [open an issue on GitHub](https://github.com/xiaosuhu/midas-ai-in-research/issues).*

```{bibliography}
:filter: docname in docnames
:keyprefix: ch20-
```

# MIDAS AI Sandbox
*Author: Dr. Nathan Fox*

This chapter presents two applied AI Sandbox modules used at the University of Michigan: one focused on **text analysis** and one focused on **computer vision**. These modules introduce researchers to practical, domain-agnostic AI tools that accelerate exploratory analysis, help organize large datasets, and lower the barrier to experimenting with modern machine-learning workflows.

---

## Part 1: AI Sandbox for Text Analysis

### 1. Introduction

Researchers across education, health, policy, humanities, and social sciences routinely work with large amounts of unstructured text: interviews, survey responses, reports, patient narratives, archival material, or multilingual documents. Manually reviewing such data is time-consuming due to volume, not conceptual difficulty.

Modern AI language models can support—though not replace—expert interpretation by helping researchers:

- Organize and compare text  
- Assign custom labels  
- Translate multilingual materials  
- Summarize long documents  

This module introduces four foundational model types:

- **EmbeddingGemma-300M** – semantic similarity & clustering  
- **BART-Large-MNLI** – zero-shot classification into custom thematic labels  
- **Helsinki-NLP / OPUS-MT** – open multilingual machine translation  
- **BART-Large-CNN** – abstractive summarization  

These tools offer fast, flexible entry points into early-stage qualitative analysis.

---

### 2. EmbeddingGemma-300M: Measuring Semantic Similarity

**Model type:** Text embedding model  
**Purpose:** Converts text into vectors that reflect meaning.

EmbeddingGemma-300M maps sentences and documents into a high-dimensional embedding space where similar ideas cluster together. Because embeddings capture meaning beyond surface wording, they are ideal for:

- Clustering open-ended responses  
- Detecting duplicates  
- Exploring thematic structure  
- Measuring conceptual distance  

**Example:**  
In education research, embeddings can automatically group thousands of student reflections into clusters such as “motivation,” “barriers,” or “learning environment,” allowing faster qualitative review.

---

### 3. BART-Large-MNLI: Zero-Shot Text Classification

**Model type:** Zero-shot classifier  
**Purpose:** Assigns user-defined labels without training.

BART-Large-MNLI uses natural-language inference to match text with categories you provide (e.g., “economic concerns,” “climate policy,” “mental health”). It is flexible, fast, and requires no annotated dataset.

**Strengths:**  
- Works immediately with any label set  
- Handles varied writing styles  
- Useful for qualitative coding and filtering

**Limitations:**  
- Sensitive to how labels are phrased  
- May oversimplify nuanced content

**Example:**  
Policy researchers can sort hundreds of interview excerpts into themes to guide deeper qualitative coding.

---

### 4. Helsinki-NLP / OPUS-MT: Machine Translation

**Model type:** Open-access machine translation  
**Purpose:** Cross-lingual research workflows.

OPUS-MT models are trained entirely on public multilingual corpora and optimized for specific language pairs (e.g., English ↔ Finnish; English ↔ Swahili). This makes them ideal for:

- Normalizing multilingual datasets  
- Translating interviews or field-site documents  
- Supporting cross-regional comparative research  
- Adapting translation systems to domain-specific terminology  

**Example:**  
Migration researchers can translate interviews collected across countries into a shared analysis language while maintaining transparency around data sources.

---

### 5. BART-Large-CNN: Summarizing Long Documents

**Model type:** Abstractive summarization  
**Purpose:** Produces concise, readable overviews.

BART-Large-CNN helps researchers quickly determine relevance when reviewing lengthy material such as:

- Public health reports  
- Long interviews  
- Meeting notes  
- Policy documents  

Summarization is often used before clustering or classification to accelerate interpretation.

**Example:**  
A research team can generate summaries of hundreds of interview transcripts, then cluster or label the summaries to identify thematic patterns.

---

### 6. Additional Text Models

#### BERT Base Uncased
A bidirectional masked-language model used for understanding sentence context, predicting masked words, and forming a foundation for tasks such as sentiment analysis, named entity recognition, or document classification.

#### CardiffNLP Twitter RoBERTa (Sentiment Analysis)
A sentiment model trained on millions of tweets to handle informal language, slang, emojis, and sarcasm. Ideal for public-perception studies and large-scale social-media monitoring.

---

### 7. Text Model Comparison Table

| Model | Primary Function | Strengths | Limitations | Research Uses |
|------|------------------|-----------|-------------|----------------|
| **EmbeddingGemma** | Semantic similarity | Captures meaning beyond wording; great for clustering | No labels or summaries; requires metrics | Grouping responses; deduplication; similarity mapping |
| **BART-MNLI** | Zero-shot classification | Flexible labels; no training needed | Sensitive to label phrasing | Sorting interviews; thematic coding; filtering |
| **OPUS-MT** | Translation | Open data; strong for specific language pairs | One model per language pair | Translating multilingual interviews; cross-lingual analysis |
| **BART-CNN** | Summarization | Clear summaries; fast document triage | May miss nuance | Summaries of interviews, reports, articles |

---

## Part 2: AI Sandbox for Computer Vision

### 1. Introduction

This module introduces how AI “sees” and interprets images. You will explore four models that represent a progression from **recognition → localization → segmentation → reasoning**:

- **Segment Anything (SAM)** – outlines objects  
- **Grounding DINO** – finds objects using text prompts  
- **Vision Transformer (ViT)** – classifies what an image contains  
- **Qwen-VL (Qwen3)** – answers questions about images  

These tools support research across biology, medicine, environmental science, cultural heritage, and more.

---

### 2. Segment Anything (SAM)

**Model type:** Segmentation (object outlining)  
**Demo:** https://segment-anything.com/demo

SAM identifies and outlines objects even without knowing their category. It works via:

- Clicks  
- Boxes  
- Automatic mask generation  

**Strengths:**  
- Works on any domain (microscopy, satellite, everyday images)  
- Produces precise object masks  
- No retraining required  

**Limitations:**  
- Does not name the object  
- Can over-segment complex textures  

**Example:**  
Microbiologists use SAM to automatically outline cells, replacing hours of manual tracing.

---

### 3. Grounding DINO

**Model type:** Text-guided object detection  
**Demo:** https://huggingface.co/spaces/merve/Grounding_DINO_demo

Grounding DINO connects **language ↔ vision**: you describe an object (“find solar panels”) and it locates it in the image.

**Strengths:**  
- Accepts free-form natural language  
- Detects unseen objects (zero-shot)  
- Highly flexible  

**Limitations:**  
- Requires clear wording  
- Slower than specialized detectors  

**Example:**  
Environmental scientists use it to detect solar farms or wind turbines in satellite images.

---

### 4. Vision Transformer (ViT)

**Model type:** Image classification  
**Demo:** https://huggingface.co/google/vit-base-patch16-224?maximized=true

ViT breaks an image into patches and analyzes them jointly, offering:

- Strong baseline performance  
- Good generalization across image types  
- Quick labeling of large datasets  

**Limitations:**  
- Produces one main label (no segmentation or localization)

**Example:**  
Researchers rapidly categorize large sets of lab or field images before deeper model development.

---

### 5. Qwen-VL (Qwen3)

**Model type:** Vision–language reasoning  
**Demo:** https://huggingface.co/spaces/Qwen/Qwen3-VL-Demo

Qwen-VL can describe images, answer questions, and explain relationships (“Which buildings look like temples?” “Is the person wearing protective equipment?”).

**Strengths:**  
- Open-ended question answering  
- Integrates vision and natural-language reasoning  
- Useful for research documentation and exploratory analysis  

**Limitations:**  
- Accuracy varies  
- Requires more computing resources  

**Example:**  
Museum researchers use it to analyze historical photographs quickly.

---

### 6. Vision Model Comparison Table

| Model | Primary Function | Strengths | Limitations | Research Uses |
|------|------------------|-----------|-------------|----------------|
| **SAM** | Object segmentation | Precise masks; no training; domain-agnostic | Does not label objects | Segmenting cells; identifying regions in satellite images |
| **Grounding DINO** | Text-guided detection | Understands natural language; zero-shot | Needs clear prompts | Mapping solar panels; locating wildlife; historical analysis |
| **ViT** | Image classification | Strong baseline; efficient | Only single-label | Rapid labeling of large image datasets |
| **Qwen-VL** | Visual Q&A | Explains image content; flexible | Variable accuracy | Documentation, cultural heritage research, interactive assistants |

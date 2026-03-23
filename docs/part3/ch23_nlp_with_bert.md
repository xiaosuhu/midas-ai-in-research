# NLP with Pre-trained Language Models

:::{admonition} What you will learn
:class: tip

By the end of this chapter and its companion notebook, you will be able to:

- Explain what makes BERT different from earlier language models
- Use the Hugging Face `transformers` library to apply pre-trained models to your own text
- Extract named entities from a document collection
- Measure semantic similarity between passages
- Reason about model selection and validation before applying these tools to your research data
:::

Imagine you are studying how regional newspapers covered air quality regulations over a fifteen-year period. You have collected about 3,000 articles, which is far too many to read systematically, but not so many that you can afford to ignore what is actually in them. What you really want to know is which government agencies and companies appear most often, how the language shifts before and after specific legislative events, and which articles are genuinely about regulatory enforcement versus those that merely mention it in passing.

Until recently, answering any one of those questions computationally would have required a separate model, a substantial labeled training dataset, and weeks of engineering time. The situation is quite different now. You can address all of them in a single afternoon using pre-trained language models and about fifty lines of Python, running free in a Colab notebook with a GPU.

Chapter 20 showed you these same model families through the browser, with no code at all. This chapter goes one level deeper. You will write the Python yourself, understand what the model is doing at each step, and see how to interpret the outputs in a way that is actually useful for research.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/xiaosuhu/midas-ai-in-research/blob/v1.0-dev/docs/notebooks/bert_nlp_demo.ipynb)

---

## The Idea Behind BERT

BERT stands for Bidirectional Encoder Representations from Transformers. The key word is bidirectional, and understanding what it means helps explain why BERT became such a significant landmark in natural language processing {cite}`devlin2019bert`.

Earlier language models read text in one direction, word by word from left to right. When the model processes any given word, it only has access to the words that came before it in the sentence. That works reasonably well for some tasks, but it is a genuine limitation for understanding meaning, because the meaning of a word often depends heavily on what comes after it.

Consider the word "bank" in two sentences: "I walked to the bank to deposit a check" and "we sat on the bank of the river to eat lunch." A model reading left to right would have processed "bank" before it reaches "deposit" in the first sentence or "river" in the second, so it would need to rely heavily on what came before to make the right interpretation. BERT sees both sentences in full from the start, which means it can use context from both directions simultaneously.

BERT learned this bidirectional reading through a training procedure called masked language modeling. During pretraining, roughly fifteen percent of the tokens in each training sentence were replaced with a special [MASK] token, and the model was trained to predict what the masked words were {cite}`devlin2019bert`. Because the missing words could appear anywhere in the sentence, the model was forced to attend to context from the left and the right at the same time. After training on enormous amounts of text using this approach, BERT developed representations that capture meaning in a remarkably context-sensitive way.

The practical output of all this pretraining is a model that produces **contextual embeddings**: dense numerical vectors where each word is represented not by a single fixed vector, but by a vector that changes based on surrounding context. "Bank" in a financial passage gets a different embedding from "bank" in a geographical passage, and that distinction is encoded in the representation itself. This is what makes BERT such a strong foundation for downstream research tasks.

The architecture that makes all of this possible is the Transformer, introduced in a 2017 paper by Vaswani and colleagues {cite}`vaswani2017attention`. If you want a fuller picture of how the Transformer works, including attention mechanisms and token representations, [Chapter 2](../part1/ch02_how_ai_works.md) walks through those ideas in detail. For now, the key intuition is that attention allows the model to relate every word to every other word in the sequence simultaneously, which is what bidirectionality really means in practice.

BERT is also one of the earliest examples of what researchers now call a foundation model: a large model pretrained at scale on broad data that can then be adapted to many different downstream tasks with relatively little additional effort. [Chapter 2](../part1/ch02_how_ai_works.md) introduces this concept if you want to understand the broader landscape before diving into the code here.

---

## From Understanding to Doing: The Transformers Library

The practical starting point for working with BERT is the Hugging Face `transformers` library {cite}`wolf2020transformers`. It provides a consistent Python interface to thousands of pre-trained models, all downloadable from the Hugging Face Model Hub. The library is designed around the idea that you should be able to go from "I need to run named entity recognition (NER) on my text" to working code in just a few lines.

The simplest interface is the `pipeline`. You specify the task, optionally name a specific model, and the library handles tokenization, the forward pass, and post-processing of the output:

```python
from transformers import pipeline

ner = pipeline("ner", model="dslim/bert-base-NER", aggregation_strategy="simple")
results = ner("The EPA released a report from its Chicago field office last week.")
```

Behind the scenes, the library downloads and caches the model weights on first use, tokenizes your input using the model's associated tokenizer, runs the text through the network, and decodes the outputs into a readable format. The model hub page for each model includes a model card explaining what data it was trained on, what tasks it supports, and any known limitations. Reading the model card before you use a model in research is good practice.

For tasks involving semantic similarity, a companion library called `sentence-transformers` provides models specifically optimized for producing embeddings at the sentence level {cite}`reimers2019sentence`. Standard BERT embeddings are token-level representations, and simply averaging them to get a sentence vector does not work as well as you might expect. Sentence transformer models are trained with a different objective that makes their sentence-level embeddings directly useful for comparison.

---

## Task 1: Named Entity Recognition

Named entity recognition is the task of identifying spans of text that refer to named things and labeling them by type. People, organizations, locations, and miscellaneous proper names like events or nationalities are the standard categories. For researchers, NER is useful any time you need to know who or what appears in a large collection of text without reading it manually.

A political scientist might use NER to track which advocacy organizations appear most frequently in congressional testimony over time. An economist might pull references to specific countries and industries from a corpus of regulatory filings. A historian might extract names of individuals mentioned in archival correspondence and then trace their co-occurrence patterns across documents.

The model in the companion notebook is `dslim/bert-base-NER`, which is BERT fine-tuned on the CoNLL-2003 named entity recognition benchmark {cite}`sang2003conll`. CoNLL-2003 contains annotated news text in English and German; the English portion covers four entity types:

- **PER** — person names
- **ORG** — organizations, companies, agencies, institutions
- **LOC** — locations: countries, cities, regions, geographic features
- **MISC** — miscellaneous named entities including nationalities, event names, and product names

One practical detail worth understanding is the `aggregation_strategy` parameter. BERT operates at the subword level: longer or unusual words get split into fragments during tokenization. A multi-word name like "Environmental Protection Agency" might be represented as a sequence of several subword tokens, and the NER model produces a prediction for each one separately. The `aggregation_strategy` controls how those token-level predictions get reassembled into entity spans. Setting it to `"simple"` merges consecutive tokens with the same entity label into a single span, which is usually what you want.

Here is an example of what the output looks like:

```python
[
    {"word": "EPA",       "entity_group": "ORG",  "score": 0.997, "start": 4,  "end": 7},
    {"word": "Chicago",   "entity_group": "LOC",  "score": 0.993, "start": 42, "end": 49}
]
```

Each result includes the entity text, its type, a confidence score between 0 and 1, and character offsets that let you locate the span in the original string. The character offsets are useful when you want to extract the surrounding sentence for further analysis or display.

The companion notebook works through applying NER to a set of short news excerpts from different domains, filtering results by entity type, and building a frequency table of the most commonly mentioned organizations and locations across the corpus.

---

## Task 2: Semantic Similarity

Semantic similarity is a measure of how alike two pieces of text are in meaning, independent of whether they share the same words. Two sentences can be worded completely differently and still express essentially the same idea, and two sentences can share many of the same words while meaning something quite different. Measuring this kind of meaning-level similarity is useful for finding documents on the same topic, detecting duplicate or near-duplicate survey responses, grouping open-ended answers into themes, and retrieving relevant passages from a large collection.

The tool for this is the `sentence-transformers` library, which provides models trained explicitly to produce sentence embeddings that are useful for comparison {cite}`reimers2019sentence`. The model we use in the notebook is `all-MiniLM-L6-v2`, a compact and fast sentence transformer that performs well across a range of tasks. The core operation is: encode your texts into vectors, then compute cosine similarity between pairs.

```python
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

passages = [
    "Carbon emissions near the industrial district increased substantially last year.",
    "Air pollution levels around the manufacturing zone rose sharply over the past twelve months.",
    "The company posted its strongest quarterly revenue figures in five years."
]

embeddings = model.encode(passages)
similarity = util.cos_sim(embeddings, embeddings)
```

Cosine similarity produces a value between 0 and 1. In the example above, the first two passages would score high (both describe rising pollution near industry), while either of them paired with the third would score low (a different topic entirely). The full pairwise similarity matrix gives you a compact picture of the thematic relationships across your document set.

The notebook works through applying this to a set of policy-related excerpts, visualizing the pairwise similarity matrix as a heatmap, and using the most similar pairs as a check on whether the model is behaving sensibly on your type of text.

**One important caveat: sentence similarity models measure semantic closeness, not factual agreement or sentiment alignment.** Two sentences expressing opposite positions on the same topic can still score moderately high because they share thematic vocabulary and conceptual focus. Whether this is useful or misleading depends on what you are trying to do. If you want to separate "supports the policy" from "opposes the policy," you need a classifier, not a similarity model. If you want to find all articles that are substantively about the policy regardless of stance, similarity is the right tool. Thinking through this distinction before you build a pipeline will save you a round of confusion later.

---

## Task 3: Text Classification with a Fine-Tuned Model

The third task demonstrates text classification using a model that was fine-tuned for a specific problem: sentiment analysis on short passages. The model is `distilbert-base-uncased-finetuned-sst-2-english`, a compact version of BERT fine-tuned on the Stanford Sentiment Treebank {cite}`socher2013sst`. DistilBERT retains about 97% of BERT's performance on most tasks while running approximately 60% faster, which makes it a practical choice when you are processing large volumes of text.

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

results = classifier([
    "The data collection process was frustrating and poorly documented.",
    "The training session was clear and well organized."
])
# [{'label': 'NEGATIVE', 'score': 0.998}, {'label': 'POSITIVE', 'score': 0.997}]
```

The reason to introduce a fine-tuned classifier here, alongside the zero-shot approach from Chapter 20, is to make the trade-off concrete. A fine-tuned model is generally more accurate for the specific task it was trained on. A zero-shot model is more flexible because you supply your own category labels without any retraining. When a pre-existing fine-tuned model matches your research question closely, it is almost always the better choice. When your classification problem is unusual or domain-specific, zero-shot is a reasonable first step, and you can collect a small set of hand-labeled examples to measure how well it actually performs.

The notebook includes a comparison exercise where you run the same short texts through both approaches and look at where they agree and where they diverge. That comparison is a quick way to build intuition for when each tool is appropriate.

---

## Running in Colab with a GPU

The companion notebook is set up for a free Colab GPU session. To enable the GPU, open the notebook, go to **Runtime**, click **Change runtime type**, and select **T4 GPU**. Most cells will work on CPU as well, but NER and embedding inference over longer texts or larger batches runs substantially faster on GPU.

Both `transformers` and `sentence-transformers` detect GPU availability automatically. You can also set it explicitly:

```python
# GPU (first device)
ner = pipeline("ner", model="dslim/bert-base-NER", device=0)

# CPU (if you are on a machine without GPU)
ner = pipeline("ner", model="dslim/bert-base-NER", device=-1)
```

The notebook includes a device detection cell at the top that sets the right value automatically, so you do not need to change anything by hand.

---

## Research Considerations

A few things are worth thinking through before you apply these models at scale.

**Domain fit.** BERT and its derivatives were pretrained primarily on news text and books. They work well on formal writing that resembles their training distribution. If your research uses clinical notes, legal documents, social media posts, historical texts, or scientific literature, the model may perform noticeably worse on domain-specific terminology and conventions. The Hugging Face hub hosts many domain-adapted variants, including BioBERT for biomedical text and LegalBERT for legal documents. It is worth checking whether a domain-specific model exists before defaulting to the general-purpose one.

**Confidence scores.** The scores returned by pipeline models are softmax outputs, which tend to be overconfident. A score of 0.99 does not mean the model is correct 99% of the time on your specific data. Before using model predictions as if they were ground truth, evaluate on a hand-labeled sample drawn from your actual corpus. Even fifty to one hundred labeled examples is enough to get a meaningful sense of precision and recall.

**Data privacy.** Running these models locally or in a private Colab notebook means your text stays on your machine. Third-party APIs are a different story. Do not send confidential or sensitive research data to any external service without confirming how they handle input data. For research covered by IRB protocols, HIPAA, or other governance requirements, use an approved institutional computing environment. Chapter 13 covers the options available at U-M and more broadly.

**Computational scale.** For a few hundred to a few thousand documents, Colab is perfectly adequate. For larger corpora, batching your inputs improves throughput substantially, and running overnight on Great Lakes with a GPU node becomes more practical than repeated Colab sessions. The notebook shows how to pass lists of texts to the pipeline rather than processing one at a time.

```{admonition} If You're at U-M
:class: note

For text corpora that are too large for Colab or that contain sensitive data, Great Lakes is the right environment. You can request GPU nodes through the Open OnDemand portal. For HIPAA-covered text, Armis2 is the approved option. See [AI Resources at the University of Michigan](../part4/ch27_um_resources.md) for details.
```

---

## Try This

Open the companion notebook and run the NER section on a short passage from your own research materials — a few paragraphs of a report, some interview excerpts, or a news article in your domain. Look carefully at what the model gets right, what it misses, and what it labels incorrectly. Then search the Hugging Face hub for a model fine-tuned closer to your domain (try search terms like "NER biomedical" or "NER legal") and compare its output on the same passage. The differences are often instructive.

Then try the semantic similarity section with a small set of documents you know well enough to evaluate by eye. Build the similarity matrix, find the highest-scoring pairs, and ask yourself whether those pairs are genuinely similar in meaning or whether the model is responding to shared vocabulary without shared meaning. That hands-on calibration is the most practical way to build intuition for where these tools are reliable and where they need backup from human judgment.

---

## Further Reading

Devlin et al. (2019) is the original BERT paper and is accessible even without a deep machine learning background {cite}`devlin2019bert`. The introduction and Section 3, which describes the pretraining and fine-tuning setup, are the most useful parts for a research context. The Hugging Face NLP course (huggingface.co/learn/nlp-course) provides a free, hands-on walkthrough of the transformers library with interactive notebooks covering all three tasks in this chapter. Reimers and Gurevych (2019) explain why standard BERT representations are not ideal for sentence-level similarity and how sentence transformers address that problem {cite}`reimers2019sentence`.

---

## Related Chapters

- [Pre-trained Models for Text and Vision](../part2/ch20_pretrained_text_vision.md) — browser-based exploration of the same model families without writing code
- [Computing Resources](../part2/ch13_computing_resources.md) — choosing where to run GPU workloads at scale
- [Validation and Interpretation](../part2/ch21_validation_interpretation.md) — checking model outputs before using them in research

*Last reviewed: March 2026. Tool-specific content in this chapter refers to Hugging Face Transformers (4.x). If you notice outdated content, [open an issue on GitHub](https://github.com/xiaosuhu/midas-ai-in-research/issues).*

```{bibliography}
:filter: docname in docnames
```

---

**Questions or feedback?** [Open an issue on GitHub](https://github.com/xiaosuhu/midas-ai-in-research/issues)

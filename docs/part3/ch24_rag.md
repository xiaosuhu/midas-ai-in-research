# Chapter 24: Building a Research Knowledge Base with RAG

:::{admonition} What you will learn
:class: tip

By the end of this chapter and its companion notebook, you will be able to:

- Explain what retrieval-augmented generation (RAG) is and why it matters for working with research documents
- Decide when an existing tool like NotebookLM is the right choice versus building your own pipeline
- Recognize the scenarios where a custom RAG pipeline is the only option
- Construct a simple local RAG system and run it on your own documents
- Identify retrieval quality as the most common point of failure in a RAG system
:::

Imagine you have just joined a research lab six months into a three-year project. Your advisor is generous with their time, but you feel guilty asking the same logistical questions every week. Where is the IRB-approved interview protocol? What does the lab's coding manual say about this edge case? How did the team decide to handle missing data in the second wave? The answers are almost certainly written down somewhere. The problem is that "somewhere" is spread across a shared drive with four years of folders, a Slack archive, a handful of PDFs, and a few Word documents nobody remembers naming.

Now imagine being able to type that question into a search box and get a direct answer, with a pointer to the exact document it came from.

That is the core promise of retrieval-augmented generation, usually called RAG. It combines two things: a retrieval system that finds the most relevant passages from a collection of documents, and a language model that uses those passages to compose an answer. The model does not make things up from memory. It reads what you give it and responds based on that {cite}`lewis2020retrieval`. For research contexts, where precision and traceability matter, that constraint turns out to be a feature, not a limitation.

---

## What RAG Actually Does

Before getting into the research applications, it helps to understand what is happening under the hood, at least at a high level.

A RAG system has two main stages. The first is **retrieval**. Every document in your collection gets converted into a numerical representation called an embedding, a dense vector of several hundred numbers that captures the meaning of the text in geometric space. When you ask a question, the question gets embedded the same way, and the system finds the documents whose embeddings are closest to your question's embedding. "Closest" here means semantically similar, not just lexically matching, which is why it can surface relevant passages even when the exact words differ {cite}`google2024embeddings`.

The second stage is **generation**. The top retrieved passages are passed to a language model as context, along with your original question. The model reads this context and produces a response grounded in what it found. Because the model is only working with the passages you give it, the answer can be traced back to specific source documents.

This is what distinguishes RAG from asking a general-purpose chatbot the same question. A general chatbot answers from its training data, which may be outdated, imprecise, or simply unaware of your specific documents. A RAG system answers from your documents, and can tell you exactly which ones.

---

## Four Reasons Researchers Use RAG

**Navigating large literature collections.** Researchers routinely accumulate hundreds of PDFs across a project lifetime. Keyword search helps when you know exactly what you are looking for, but fails when the relevant passage uses different terminology. Semantic retrieval finds conceptually related content even when the phrasing does not match, which means you spend less time reformulating search terms and more time reading what actually matters.

**Creating a shared lab knowledge base.** Protocols, coding manuals, onboarding guides, methodological decision logs: these documents encode institutional knowledge that is genuinely hard to transfer any other way. A RAG system built on these materials lets new team members ask questions and get grounded answers, rather than interrupting a senior colleague for the fourth time that week.

**Querying across many documents at once.** If you are doing qualitative research across a hundred interview transcripts, finding all the places participants mentioned a particular theme is slow and error-prone by hand. RAG lets you ask the question once and surface the relevant passages across the entire collection, treating the corpus as a searchable knowledge base rather than a pile of files.

**Keeping sensitive data local.** This is probably the most practically important reason for researchers. If your documents contain anything covered by an IRB protocol, a data use agreement, HIPAA, or a confidentiality commitment to participants, you generally cannot upload them to an external platform. A local RAG pipeline keeps everything on your own machine or on an approved institutional compute environment, so sensitive text never leaves the environment you control.

---

## Ready-Made Tools: Start Here

Before building anything yourself, it is worth knowing what already exists. For documents that are not sensitive, **NotebookLM** is the most accessible starting point. It is a Google product that lets you upload PDFs, Google Docs, websites, and other sources, then ask questions across all of them in a single interface. It handles embedding and retrieval automatically, cites its sources in the responses, and lets you generate structured summaries and briefing documents. The interface is easy to use and works well for literature reviews, project planning documents, and other collections of publicly available or non-sensitive material.

The one constraint that matters for researchers is that your documents are uploaded to Google's servers. That rules NotebookLM out for anything covered by an IRB protocol, a data use agreement, or a confidentiality commitment to participants. If your documents fall into that category, see the U-M note at the end of this chapter before deciding what to use.

Both tools are doing RAG under the hood. Understanding that connection matters because it helps you know what these tools are good at, where they will struggle, and why sometimes you need to build something yourself.

---

## When to Build Your Own

There is a point where existing tools are not enough. That point usually comes from one of two directions: data that cannot leave a specific environment, or a workflow that requires more control than a conversational interface allows.

**Data governance.** Consider a team studying housing instability who conducted 180 in-depth interviews with participants who were told their conversations would remain confidential. The IRB protocol is explicit: transcripts stay on approved institutional servers. Uploading them to any external platform, even one that promises not to train on user data, is not permitted under the terms of data collection. Or consider a clinical research group with five years of patient case notes, de-identified but still covered by a data use agreement that prohibits transmission to third-party services. In both cases, a local RAG pipeline is the answer. Everything, including embedding, retrieval, and generation, runs on your own machine or on an approved institutional environment, and nothing leaves.

**Pipeline integration and structured output.** The second reason to build your own is less obvious but equally important. Tools like NotebookLM are designed for conversation: you ask a question, you get an answer. That works well for exploration, but it is not designed for systematic, repeatable extraction across a large corpus.

Imagine a political scientist who wants to identify every mention of a specific fiscal policy position across 800 newspaper articles from five countries, and output the results as a structured dataset with article metadata, the retrieved passage, and a relevance score. She is not exploring; she is building a dataset. A custom RAG pipeline can loop through all 800 documents, embed and retrieve relevant chunks for each, write the results to a CSV, and run the same extraction again if the query needs refinement. NotebookLM has no way to do this automatically and no mechanism to produce machine-readable output for downstream analysis. The same applies to any workflow where RAG output needs to feed into a statistical model, a qualitative codebook, or any analysis step that expects structured data rather than a chat response.

This kind of automation is also where you gain control over the retrieval itself. You can experiment with chunk size, overlap, and embedding models. You can combine semantic retrieval with keyword filters, so that your search returns only passages from a specific date range or document type. And you can inspect the raw retrieval scores to audit why the pipeline surfaced what it did, rather than trusting a black-box interface.

---

## Two Research Scenarios in Practice

### A Lab Knowledge Base

A mixed-methods social science lab has accumulated four years of methodological documentation. There is a 40-page IRB protocol, a 25-page coding manual with definitions and decision rules for a content analysis project, a set of standard operating procedures for interview administration, and a running document of methodological decisions logged after each weekly lab meeting.

New graduate students spend their first weeks asking questions that are already answered somewhere in those documents. The senior students who get the questions are happy to help, but the interruptions add up. Building a RAG system on top of this documentation collection takes an afternoon. Once it is running, a student can type "how do we code mentions of indirect financial assistance" and get back the relevant section of the coding manual with a direct quote. They can ask "what does the IRB protocol say about audio recording consent" and get the answer in seconds.

This kind of lab knowledge base does not require a powerful model or sophisticated infrastructure. The documents are expert and precise. The questions are fairly specific. A small embedding model and a few hundred lines of Python are enough.

### IRB-Protected Interview Transcripts

A second scenario involves a public health researcher studying opioid use in rural communities. She has 95 interview transcripts, all covered by an IRB protocol that specifies data must remain on a university-approved server. She is in the writing phase and keeps needing to find passages where participants described their first interaction with the healthcare system, or passages where they mentioned family responses to their treatment.

Keyword search is inadequate. Participants describe these things in many different ways, and no single keyword captures the concept. What she needs is semantic retrieval: a system that understands what she is looking for, finds all the relevant passages across 95 documents, and returns them with enough context to judge their usability.

A local RAG pipeline running on Great Lakes gives her exactly that. She loads the transcripts, embeds them in chunks, and runs queries. The system finds conceptually relevant passages even when the specific words differ. Because everything runs on university infrastructure, the data governance question never comes up.

She is not using RAG to generate summaries of her interviews. She is using the retrieval component as a precision search tool. This is a completely valid use of the technology, and often the more appropriate one for qualitative research where the researcher's own interpretation of the data is the whole point.

---

## Tutorial: A Simple RAG Pipeline

The companion notebook walks through a complete, working RAG pipeline using public data and no proprietary services. It runs entirely in Google Colab and uses two libraries you have already encountered in this handbook: `sentence-transformers` for creating embeddings and `transformers` for the generation step.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/xiaosuhu/midas-ai-in-research/blob/v1.0-dev/docs/notebooks/rag_demo.ipynb)

The notebook uses a collection of short document excerpts drawn from publicly available research methodology descriptions across environmental science, economics, and public health. None of the demo documents are sensitive, and no external API calls are made during retrieval. The generation step uses a small open-weight model that runs on Colab's free CPU.

### The Core Pipeline

A RAG pipeline has three components that you will build in order in the notebook.

**Embedding and storage.** You load an embedding model and pass each chunk of text through it, storing the resulting vectors in a simple numpy array. This is the "indexing" step. For a few hundred documents it takes seconds; for tens of thousands of documents you would want a proper vector database.

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
chunk_embeddings = model.encode(chunks, show_progress_bar=True)
```

**Retrieval.** When a query comes in, you embed it the same way and compute cosine similarity between the query vector and all the stored chunk vectors. The highest-scoring chunks are returned as context.

```python
import numpy as np

def retrieve(query, top_k=3):
    query_vec = model.encode([query])
    scores = np.dot(chunk_embeddings, query_vec.T).flatten()
    top_indices = np.argsort(scores)[::-1][:top_k]
    return [(chunks[i], scores[i]) for i in top_indices]
```

**Generation.** The retrieved passages are formatted into a prompt and passed to a language model. The model reads the context and answers based on it rather than on general knowledge.

```python
prompt = f"""Answer the question using only the context below.

Context:
{context}

Question: {question}

Answer:"""
```

The notebook walks through each step with explanatory cells, common failure modes, and a final "try your own documents" section where you can drop in your own text and run the same pipeline.

### What the Notebook Does Not Cover

A production RAG system for a real research project involves a few additional decisions that are outside the scope of this tutorial. Chunking strategy matters more than it looks: how you split documents into pieces affects what the retrieval step can and cannot find. Document structure, optimal chunk size, and whether to use overlapping windows are all worth thinking through for your specific corpus. For large document collections, a vector database like ChromaDB or FAISS is more efficient than a numpy array, though the conceptual model is the same {cite}`google2024embeddings`. And for the generation step, a larger and more capable model will produce substantially better answers, though it will also require more compute.

---

## Research Considerations

**Retrieval quality determines answer quality.** The most common source of failure in a RAG system is not the language model. It is retrieval. If the wrong passages come back, the model answers based on the wrong information, and it will do so confidently. Before you trust the generated answers, evaluate the retrieval step independently. For a sample of representative questions, look at what the top three passages actually are and ask whether you would be satisfied with an answer based on them. A retrieval step that finds the right passages eight times out of ten is actually quite good; one that finds them four times out of ten is a problem no language model can fix.

**Chunk boundaries are a design decision.** Splitting a document into chunks by fixed character count is simple but loses context at boundaries. A coding manual definition that spans two chunks might return only the first half as a retrieved passage, producing a misleading answer. Splitting by paragraph or section headers often works better for structured documents. For transcripts with speaker turns, splitting at turn boundaries preserves conversational context. There is no universal answer, and it is worth experimenting on a subset of your documents before committing to a chunking strategy.

**Every answer should be traceable.** One of the practical advantages of RAG over a general chatbot is that you can build a system that always tells you which document a response came from. Build this into your pipeline from the start. Keeping metadata (filename, page number, participant ID) attached to each chunk costs almost nothing, and it makes the system far more useful for research purposes where you need to verify claims against primary sources.

**RAG is not an analysis tool.** A RAG system can find what is in your documents, but it cannot tell you what it means for your research. This is especially important for qualitative work. If you ask a RAG system "what do participants think about X" and it returns relevant passages, you still need to read those passages and interpret them through the lens of your theoretical framework and your understanding of the data. The system helps you navigate; the intellectual work remains yours.

```{admonition} If You're at U-M
:class: note

If your documents are sensitive but fall within U-M's data governance framework, **Maizey** is the first option to explore before writing any code {cite}`maizey2024`. It is U-M ITS's institutional RAG tool, available to students, staff, and faculty. It works similarly to NotebookLM: you build a knowledge base from uploaded documents and query it in natural language, but it operates within U-M's approved infrastructure rather than a commercial cloud. For many research use cases involving non-public or IRB-adjacent materials, Maizey is the right starting point.

When Maizey is not enough, whether because the data requires a stricter environment, the pipeline needs to be automated, or you need structured output for downstream analysis, Great Lakes is the right compute environment for building a custom pipeline. The Armis2 cluster is available for HIPAA-covered data. See [AI Resources at the University of Michigan](../part4/ch27_um_resources.md) for details on access and data classification.
```

---

## Try This

Open the companion notebook and run through the full pipeline on the provided sample documents. Once you have it working, try replacing the sample collection with three to five documents from your own work that are not sensitive, such as a literature review section, a methods chapter, or some field notes from a past project.

Ask yourself a question you would genuinely want answered, then look at what the retrieval step returned. Were those the passages you would have chosen yourself? If not, is the issue that the query was too vague, that the chunking broke a relevant passage across two chunks, or that the embedding model simply did not connect the query to the right content? Diagnosing retrieval failures by hand on a small document set is the fastest way to develop intuition for what RAG can and cannot do reliably before you build something larger.

---

## Further Reading

Lewis et al. (2020) is the paper that introduced and named retrieval-augmented generation as a formal architecture {cite}`lewis2020retrieval`. The introduction is accessible to readers without a deep NLP background and gives useful framing for why grounding generation in retrieved documents matters. Google's 5-Day Gen AI Intensive whitepaper on embeddings and vector stores provides a practical technical overview of how embeddings work, how vector stores are organized, and the engineering considerations for different retrieval strategies {cite}`google2024embeddings`. It is particularly useful if you want to go beyond the numpy-based approach in the companion notebook and think about production-grade retrieval systems. Reimers and Gurevych (2019) explains why sentence-level embeddings from models like `all-MiniLM-L6-v2` outperform averaged token embeddings for retrieval, and is the foundational paper behind the `sentence-transformers` library used throughout this chapter.

---

## Related Chapters

- [Chapter 23: NLP with Pre-trained Language Models](ch23_nlp_with_bert.md): embeddings and semantic similarity, which are the foundation of the retrieval step
- [Chapter 20: Pre-trained Models for Text and Vision](../part2/ch20_pretrained_text_vision.md): browser-based exploration of language models without writing code
- [Chapter 13: Computing Resources](../part2/ch13_computing_resources.md): where to run local pipelines for sensitive data at U-M
- [Chapter 21: Validation and Interpretation](../part2/ch21_validation_interpretation.md): evaluating outputs before using them in research

*Last reviewed: March 2026. Tool-specific content in this chapter refers to the sentence-transformers library and FAISS. The RAG tooling ecosystem evolves quickly. If you notice outdated content, [open an issue on GitHub](https://github.com/xiaosuhu/midas-ai-in-research/issues).*

```{bibliography}
:filter: docname in docnames
```

---

**Questions or feedback?** [Open an issue on GitHub](https://github.com/xiaosuhu/midas-ai-in-research/issues)

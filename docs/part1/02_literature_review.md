# Literature Review with AI

:::{admonition} What You'll Learn
:class: tip
- How deep research tools work and what capabilities they add beyond traditional search
- Why semantic search matters for literature discovery and when keyword matching falls short
- How to orchestrate a workflow combining human expertise, search databases, and AI tools
- What makes specialized tools like Asta different from general-purpose deep research systems
- Where human judgment remains irreplaceable in the review process
:::

## The Changing Landscape of Literature Review

Traditional literature review workflows—PubMed searches, keyword filtering, citation chaining, and expert judgment—remain essential in research. However, the volume and pace of scientific publishing have made manual review increasingly challenging. PubMed alone adds more than 100,000 new biomedical articles per month {cite}`NLM_PubMed_Stats`, creating a scale challenge for researchers who must stay current. Scientific output continues to grow exponentially, both in number of publications and the volume of cited references {cite}`bornmann2015growth`.

Systematic reviews often require 6 to 12 months due to manual screening and synthesis steps. Keyword based search also limits discovery: if researchers do not know the correct terminology, synonymous or cross disciplinary findings may be overlooked. Existing automation systems still face substantial methodological barriers {cite}`tsafnat2014automation`. This gap between what exists and what can be reasonably processed is where AI assisted literature review tools come in.

The real challenge is not that we lack information. It is that we have too much of it, and researchers must decide whether to spend months on a systematic review or accept the risk of missing relevant studies. AI tools offer a third path: accelerate the early exploration phase while preserving human judgment where it matters most.

---

## What Are Deep Research Tools and What Do They Add?

Deep research systems extend large language models with capabilities specifically designed for academic workflows. The major platforms include:

- **Ai2 Asta** (https://asta.allen.ai/): Precision academic search powered by Allen Institute's Semantic Scholar
- **OpenAI Deep Research** (https://openai.com/index/deep-research/): Multi step reasoning integrated into ChatGPT
- **Perplexity Research Mode** (https://www.perplexity.ai): Fast, transparent cited answers across web and academic sources
- **Consensus** (https://consensus.app): Evidence synthesis focused on peer reviewed studies
- **Google Gemini Deep Research** (https://gemini.google.com): Long form analytic reports with Google integration

What do they have in common? They all emulate the workflow of a skilled research assistant: search → screen → extract → synthesize → summarize. Instead of one keyword search, they perform multi step reasoning across sub questions. Instead of a list of links, they return citation backed responses with structured synthesis of themes, gaps, and contradictions. Many accept user provided PDFs, allowing you to ground the search in your own work.

Importantly, **they do not replace expert reading or judgment**. What they do is significantly accelerate early stage exploration and evidence mapping, freeing you to spend time on interpretation rather than initial discovery.

---

## Why Semantic Search Matters

PubMed and similar databases rely on exact keyword matches, metadata supplied by authors or journals, and MeSH term indexing. This approach has real limitations:

- Important papers are missed if you don't know the correct terminology
- Cross disciplinary studies use different vocabulary and may not appear in your results
- PubMed returns lists; it does not interpret or synthesize what it finds

Deep research tools use semantic retrieval, which identifies results by meaning rather than word matching. Semantic search approaches address these limitations by retrieving information based on conceptual meaning, a capability increasingly important in biomedical text mining {cite}`hunter2021semantic`.

Here is a concrete example. A query like:

> "What mechanisms link chronic pain and cognitive load in fNIRS studies?"

might surface literature from cognitive neuroscience, pain research, and optical imaging—something difficult with a single keyword query. Semantic search systems expand beyond exact matching by identifying relationships between concepts, allowing them to surface studies even when authors use different terminology or describe related mechanisms in domain specific language.

---

## A Practical Workflow: Combining Human, Keyword Search, and Deep Research

The best approach is not to choose one method over another, but to combine them strategically. Here is what that looks like:

**Stage 1: You Define the Question**

You start with a specific research question because deep research tools work best with clarity. Vague inputs produce vague outputs.

Poor: "Tell me about fNIRS and pain."

Better: "What fNIRS biomarkers have been associated with chronic pain modulation during mindfulness based interventions? Focus on studies published after 2018 and include citations."

**Stage 2: Parallel Searching with Multiple Tools**

You do not have to choose between PubMed and Deep Research. Run both in parallel:

- Use PubMed or Google Scholar to find the canonical papers in your field. These databases have decades of indexing and are trusted within disciplines. You learn what everyone already knows.

- Use a deep research tool like Asta or Perplexity to find related work and cross disciplinary connections. You discover what might be overlooked by standard search.

- If you have relevant papers, upload them to Gemini Deep Research to extract methods, find similar work, and build a network view.

**Stage 3: Human Synthesis and Validation**

Once you have candidate papers from multiple sources, you (the human) synthesize and verify:

- Does the citation correspond to a real paper?
- Does the quoted text actually appear in the original source?
- Is the relevance judgment fair, or has the tool overgeneralized beyond what the evidence supports?
- Which papers actually matter for your specific research question?

This is where rigor happens. The AI accelerates discovery, but you make the judgment calls.

---

## Deep Dive: Asta and Semantic Scholar Based Search

Since Asta appears frequently in research workflows, it deserves closer attention. Asta is built on the Allen Institute's Semantic Scholar, a production academic search engine that indexes over 215 million papers. Unlike general purpose LLMs, Asta is tuned specifically for academic discovery.

**Why Asta stands out:**

Asta retrieves papers from Semantic Scholar and grounds responses in real metadata rather than generating plausible sounding citations. It understands academic structure like methods, results, and citations. It also excels at finding papers that are cited together or that address similar research questions, even if they use different terminology. For researchers in well indexed fields like biomedicine, computer science, and engineering, Asta often catches papers that generic web search would miss.

**When Asta works well:**

You have a specific research question in a field with rich academic indexing. You want high confidence that returned papers actually exist and are correctly attributed. You need semantic rather than keyword based search.

**When Asta has limits:**

Asta cannot reason deeply about the PDF content of papers you upload. Its coverage depends on how well Semantic Scholar has indexed your specific subdomain. If you work in a very new field or at the intersection of multiple disciplines, you may need to supplement with broader tools like Perplexity.

---

## Comparison of Deep Research Tools

| System | Primary Strength | How It Works |
|--------|------------------|--------------|
| **Asta** | Precision scientific retrieval | Semantic Scholar based search; metadata driven retrieval; grounded in real papers |
| **OpenAI Deep Research** | Integrated multi step reasoning | Sequential searches plus synthesis; supports document uploads; works inside ChatGPT |
| **Perplexity** | Fast, transparent cited answers | Parallel searches across web and academic sources; aggregated results with linked sources |
| **Consensus** | Evidence synthesis from peer reviewed studies | Retrieves peer reviewed findings; produces summary cards with effect sizes and confidence |
| **Google Gemini** | Long form analytic reports | Multi source synthesis; integrates with Google Scholar; supports document uploads |

---

## When Human Expertise Remains Irreplaceable

**Deep research tools excel at breadth and speed. Humans excel at depth and judgment**. Here are scenarios where human expertise is essential:

**Systematic reviews and meta analyses.** If you are conducting a systematic review for publication or policy impact, you cannot delegate the screening to AI. Methodological rigor demands that you (or your team) read and evaluate every paper that meets your inclusion criteria. This is not just best practice; in many cases it is required by funders, institutions, or journal guidelines.

**Clinical or regulatory applications.** If your literature review supports a clinical decision, treatment guideline, or regulatory approval, certification and liability rest on human judgment. An AI tool might miss an important contraindication or misinterpret a study's population. The stakes justify the time investment.

**Novel or cross disciplinary work.** When your research sits at the intersection of multiple fields, AI tools may struggle to find relevant work because the terminology differs sharply across disciplines. A human expert with training in multiple areas can recognize connections that a general purpose tool might miss.

**Evaluating methodological quality.** Deep research tools can extract what a study claims to find, but they often cannot critically appraise the methods. Did the study have adequate statistical power? Were there biases in selection or reporting? A human expert can assess these questions; an AI tool summarizes what the paper says.

**Interpreting contradictions.** When studies disagree, understanding why requires domain expertise. One study might use a stricter inclusion criterion, another might measure a slightly different outcome, and a third might work with a different population. An AI tool can surface the disagreement; you must interpret what it means.

---

## Best Practices for Using Deep Research Tools

**Start with clarity.** Your research question should be specific enough to guide search but open enough to discover related work. Vague questions produce vague results.

**Ask for multi step reasoning.** Instead of a single query, ask the tool to first identify subtopics, then search each, then extract findings, then synthesize across. Most systems support this iterative approach.

**Validate sources immediately.** Before relying on a citation or quote, check the original paper. This takes minutes and saves you from propagating errors downstream.

**Upload PDFs when possible.** Gemini Deep Research becomes more accurate when you provide the papers you care about most. This grounds the search in your domain and reduces hallucination.

**Use iterative refinement.** Deep research is not a one shot activity. After seeing initial results, refine your query. Focus on specific populations, time periods, methodologies, or geographies. Treat the tool as an interactive collaborator, not an answer engine.

**Always combine with human verification.** This is the non negotiable step. AI can summarize and map the literature. Humans must interpret statistical validity, methodological quality, relevance to the research question, and ethical or contextual considerations.

---

## Going Deeper: Working with Papers You Already Have

There is a different kind of challenge that comes after the initial search. You have found a set of papers that seem relevant, but now you need to actually understand them — across methods, findings, and gaps — without spending days in close reading before you can form a view. This is where a different category of tool becomes useful.

[NotebookLM](https://notebooklm.google.com) is Google's document-grounded research assistant. Unlike the discovery tools described earlier, it does not go out and search the web. Instead, you upload your own sources — PDFs, Google Docs, URLs, even YouTube videos — and it works only within that set. Every response it gives you is grounded in those sources, with inline citations you can click to verify against the original text {cite}`NotebookLM2024`. This makes it a useful partner for the synthesis stage of a literature review, once you have already done the work of identifying which papers matter.

:::{admonition} University of Michigan Access
:class: tip
NotebookLM is available to all UM researchers through the university's Google Workspace subscription. No separate sign-up is needed — just log in with your @umich.edu account at [notebooklm.google.com](https://notebooklm.google.com). For a full list of UM-supported AI tools, see the [UM AI Resources](../part3/20_um_resources.md) chapter.
:::

**What NotebookLM does well**

The most practical use is asking cross-document questions: "What methods do these papers use to measure X?" or "Which of these studies report conflicting findings, and what might explain the discrepancy?" Rather than reading each paper looking for the answer, you get a synthesized response with pointers back to the exact passages that support it. You can then go verify those passages directly — which you should always do — but the initial orientation is much faster.

A second use case is getting feedback on your own draft. If you upload an early manuscript draft alongside a set of relevant papers, you can ask NotebookLM whether your argument is missing something the literature has already addressed, or whether you have accurately characterized the findings of a particular study. It is a useful sanity check before asking a colleague.

NotebookLM also offers an Audio Overview feature that generates a two-person conversational summary of your uploaded sources {cite}`NotebookLM2024`. This can be a reasonable way to get a first orientation to an unfamiliar set of papers, particularly if you absorb material better by listening. It is worth knowing about, though for detailed analytical work you will want the text-based question and answer interface instead.

**What to keep in mind**

NotebookLM works only with what you give it. If you upload five papers, its answers reflect those five papers. It has no way of knowing what you left out, and it will not tell you that a study you should have included exists. This means the quality of what you get is directly tied to the quality of your initial selection — which is why the discovery phase, using the tools described earlier in this chapter, still matters.

As with all AI tools in the research context, you should verify anything you plan to rely on. The citations NotebookLM provides make this easier than with tools that only cite at the level of a full document, but the verification step is still yours to do.

---

## Quick Reference: Which Tool to Use When?

| Your Situation | Best Tool(s) | Why |
|---|---|---|
| Rapidly scope an unfamiliar area | Perplexity or Google Gemini | Fast, transparent, and good at breadth. Results appear in minutes rather than hours. |
| Need precision scientific retrieval in a well indexed field | Asta | Built specifically for academic discovery and excels at finding papers that are thematically related but use different keywords. |
| Want to deeply understand a specific set of papers | NotebookLM | Upload your papers and ask cross-document questions. Responses are grounded in your sources with inline citations you can verify. |
| Synthesizing evidence for a clinical or policy decision | Consensus | Filters for peer reviewed studies and provides summary cards with effect sizes, reducing the risk of citing low evidence work. |
| Want everything integrated into your writing workflow | OpenAI Deep Research | Integrates with ChatGPT and supports document uploads, making it convenient for drafting alongside research. |

---

## Try This

Pick a topic you are actively working on or genuinely curious about. Something specific enough that you could explain it in a sentence, but where you have not done a thorough literature search yet.

Start with a keyword search in PubMed or Google Scholar to find the five or so papers that feel most central to the topic. These are your anchors — the work you already know or suspect is important.

Then take the same question to a deep research tool like Asta or Perplexity and ask it something more open-ended, such as "What are the key findings, debates, and open questions in research on [your topic]?" Compare what comes back to your keyword results. Notice what overlaps and, more importantly, what does not. Did the AI surface papers from adjacent fields you had not encountered? Did it frame any of the debates differently than you expected?

Finally, spend a few minutes writing down what you now understand about the landscape that you did not before you started. What are the genuine gaps? What questions seem underexplored? What would need to be true for a new study in this area to make a meaningful contribution?

That last step is not just a reflection exercise. It is the beginning of the next phase. Once you have a clear sense of what the literature does and does not cover, you are ready to move from understanding the field to deciding what you want to do in it — which is what the next chapter is about.

---

## Resources and Links

**Deep Research Tools**

- **Asta**: https://asta.allen.ai/
- **OpenAI Deep Research**: https://openai.com/index/deep-research/
- **Perplexity Research Mode**: https://www.perplexity.ai
- **Consensus**: https://consensus.app
- **Google Gemini Deep Research**: https://gemini.google.com

**Document Synthesis**

- **NotebookLM**: https://notebooklm.google.com (UM Google Workspace access)

**Reference Databases**

- **PubMed**: https://pubmed.ncbi.nlm.nih.gov/
- **Google Scholar**: https://scholar.google.com/
- **Semantic Scholar**: https://www.semanticscholar.org/

**Related Handbook Chapters**

- When to Use AI in Research
- Research Planning with AI
- Validation and Reproducibility

---

## References

```{bibliography}
:filter: docname in docnames
```

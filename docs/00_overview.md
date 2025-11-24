# Overview: Artificial Intelligence in Research

## Overview

### Purpose

This tutorial introduces the role of Artificial Intelligence (AI) in modern research — exploring _why_ researchers are adopting AI, _what_ it can (and can’t) do, and how this plays out in a large research-intensive university context (here, the University of Michigan). It is aimed at an audience of faculty, staff and students engaged in research and familiarizing themselves with AI-augmented workflows.

### Structure

1.  **What is "AI"**: Brief terminology clarification
2.  **Why AI in Research**: motivations and drivers.
3.  **Scope, Benefits & Limitations**: what AI brings, what it cannot replace, and caveats.
4.  **Should I trust AI**: Concerns about current AI
5.  **U-M Context**: how the University of Michigan positions and deploys AI in its research enterprise.

---
## What is "AI"

The conceptual landscape of artificial intelligence can be understood as a set of nested domains, each building on the previous one. At the broadest level, Artificial Intelligence (AI) encompasses computational approaches for tasks such as reasoning, perception, and language understanding, as broadly characterized in foundational textbooks on the field {cite}`Russell_Norvig_2021`. Within AI, Machine Learning (ML) focuses on algorithms that improve by learning patterns from data rather than following hand-crafted rules. A more specific subset of ML, Deep Learning (DL), uses multilayer neural networks to learn hierarchical representations of information—an approach that has driven major progress in computer vision, speech processing, and natural language systems {cite}`LeCun2015deep`.

Inside the deep-learning landscape, Generative AI refers to models capable of synthesizing new content—text, images, audio, or molecular structures—by learning the underlying probability distributions of existing data. Among these generative models, Large Language Models (LLMs) represent a particularly influential class: deep neural networks trained on massive text corpora to produce coherent, context-aware language. Early formulations of generative modeling, such as Generative Adversarial Networks {cite}`Goodfellow2014gan`, laid the foundation for today’s generative paradigm, while modern LLMs such as GPT-3 demonstrated unprecedented few-shot and generalization capabilities {cite}`Brown2020gpt3`. As illustrated in the figure, LLMs occupy the overlapping region where deep learning and generative modeling converge—reflecting both their architectural foundations and their emerging role as a central tool in scientific research and discovery (see also https://openai.com/research for further background).

A crucial turning point in the evolution of modern generative models was the introduction of the Transformer architecture by Vaswani et al. {cite}`vaswani2017attention`. Transformers were a major breakthrough because they can look at all parts of a sentence at the same time, instead of reading it slowly one word after another. This lets them understand long or complicated text much more effectively. Because they work in parallel, they can also learn from huge amounts of information very quickly, which is why modern AI models have become so powerful. Transformers became the foundation for today’s large language models because they can learn from huge amounts of text in a stable and efficient way. But an equally important part of the story is hardware. Modern GPUs and AI accelerators can perform billions of calculations at the same time, something that simply was not possible a decade ago [gpu-ai](https://blogs.nvidia.com/blog/why-gpus-are-great-for-ai/). The combination of a new architecture (Transformers) and powerful computing hardware made it finally realistic to train extremely large models. These two changes together explain why AI has advanced so quickly and why LLMs are now able to support scientific research, data analysis, and discovery in ways that were unimaginable before.


```{image} _static/overview/AI-terminology.png
:alt: AI-terminology
:width: 800px
:align: center
```
---
## Why AI in Research

Artificial intelligence is becoming an integral part of modern research practice, transforming how questions are asked, how data are analyzed, and how results are communicated.  
Several complementary motivations explain why researchers across disciplines are adopting AI:

**Scaling and accelerating discovery.**  
AI expands the pace and reach of scientific progress. Studies show that papers using AI-based methods often receive higher citation impact, and the presence of AI-driven work has grown sharply since around 2015 {cite}`hao2025artificialintelligencetoolsexpand`.  
By automating repetitive steps and exploring large hypothesis spaces, AI helps researchers move from concept to discovery much faster.

**Handling data complexity and volume.**  
Modern research produces vast, multimodal datasets—ranging from medical imaging and genomics to environmental sensors and social media streams.  
AI methods, including machine learning and deep learning, make it possible to identify hidden patterns, model nonlinear relationships, and extract insights that would be difficult to achieve using classical statistics alone.

**Expanding research questions and designs.**  
AI enables exploration beyond traditional experimental limits: simulating hypothetical conditions, designing adaptive experiments, and generating new hypotheses at scale [teaching_ai](https://www.techradar.com/ai-platforms-assistants/ai-is-redefining-university-research-heres-how).  
This capacity turns AI into a creative partner for the scientific process.

**Enhancing efficiency and reproducibility.**  
Tasks such as literature review, summarizing prior work, data wrangling, and even early drafting can be supported or semi-automated through AI-driven tools [oku_lib_ai_guides_2025](https://info.library.okstate.edu/AI/tools).  
These tools reduce manual errors and free up time for conceptual reasoning and interpretation.

**Interdisciplinary reach and democratization.**  
Because AI platforms are increasingly accessible, they allow scholars from diverse fields—humanities, social sciences, health, and engineering—to adopt computational reasoning.  
This accessibility has enabled collaborations that merge qualitative insight with quantitative modeling [umich_research_ai_2024](https://research.umich.edu/research-stories/going-all-in-on-ai/).

**Augmenting the researcher’s own capability.**  
AI can surface relationships or explanations that a researcher might not have considered, revealing blind spots or hidden patterns in data or literature.  
In this sense, AI acts as a cognitive amplifier, helping us learn things we didn’t know we didn’t know.

**Supporting writing and structure.**  
Language models can serve as real-time writing partners—helping outline an argument, organize sections, refine clarity, and maintain narrative flow.  
Used responsibly, this enhances coherence and productivity without diminishing scholarly ownership of ideas.

**Assisting with coding and computation.**  
AI-assisted coding tools help researchers write, debug, and optimize code across languages and frameworks.  
They accelerate prototyping and lower technical barriers, allowing investigators to focus more on research design and interpretation.

In short, AI in research is not about replacing human intelligence but about **amplifying it**—enabling new scales, speeds, and styles of inquiry that make discovery more efficient, creative, and inclusive.


---
## Scope, Benefits & Limitations

### Scope

“AI in research” encompasses a broad set of methods and tools. It includes machine learning (supervised, unsupervised, reinforcement), deep learning, generative models (text, image, code), natural language processing (NLP) for literature review, and AI-assisted experimentation. It applies across the research lifecycle: question framing, hypothesis generation, data acquisition/processing, modelling, interpretation, writing and dissemination.

### Benefits

Here are several of the commonly cited benefits:

*   Faster throughput: AI can support faster screening of literature or large datasets, accelerating time-to-insight. {cite}`smeds2023ai_manuscript_prep`
*   Improved discovery: AI may reveal patterns not obvious to humans, thereby enabling exploratory or “serendipitous” findings. {cite}`frança2023aiempoweringresearch10`
*   Efficiency gains: Automating repetitive tasks (e.g., data cleaning, extraction, formatting) allows researchers to spend more time on interpretation and creativity. [oku_lib_ai_guides_2025](https://info.library.okstate.edu/AI/tools)
*   Broadening access: With AI tools, smaller teams or less-resourced groups may leverage advanced analytics, potentially democratizing aspects of research.
*   Cross-discipline enablement: AI methods allow disciplines previously less quantitatively oriented (e.g., humanities, social sciences) to adopt computational/synthetic workflows, opening new hybrid research models.

### Limitations & Cautions

AI is not a panacea; significant limitations must be recognised. Some of the major ones:

*   **Accuracy and validity issues**: AI models may provide plausible-looking but incorrect outputs (“hallucinations”), mis-attribute citations, or generate biased or misleading results. [SJCD LibGuides+1](https://sjcd.libguides.com/c.php?g=1358464&p=10036323)
*   **Bias, fairness and representativeness**: Models trained on biased datasets may perpetuate or amplify disparities (e.g., underrepresentation of certain groups or domains). [library.cia.edu+1](https://library.cia.edu/AI/ethics?)
*   **Reproducibility and transparency**: Some AI workflows may lack adequate documentation, be irreproducible, or opaque (“black box” models), undermining rigorous scientific standards. [USC LibGuides+1](https://libguides.usc.edu/generative-AI/limitations?)
*   **Over-reliance and epistemic risk**: There is risk that researchers lean on AI output without sufficient critical reflection, possibly reducing depth of understanding. As one commentary notes: “There is a risk that scientists will use AI to produce more while understanding less.” [YaleNews](https://news.yale.edu/2024/03/07/doing-more-learning-less-risks-ai-research?utm_source=chatgpt.com)
*   **Data privacy, ethics and governance**: Use of AI often entails large datasets, potentially sensitive information, and raises concerns about consent, ownership, transparency, and misuse. [mariecuriealumni.eu+1](https://www.mariecuriealumni.eu/newsletters/35th-mcaa-newsletter/special-issue-proceed-caution-potential-negative-impact-ai?utm_source=chatgpt.com)
*   **Scope of expertise**: AI tools may require specialised expertise (data science, ML), and misuse without proper understanding may lead to flawed conclusions or mis-applied tools. [WIRED](https://www.wired.com/story/machine-learning-reproducibility-crisis?utm_source=chatgpt.com)
*   **Creativity and context limitations**: AI excels at identifying patterns from data it has seen, but may struggle with novel conceptual insights, creativity, or domain-specific nuance / common-sense reasoning. [Harvard Medical School CE+1](https://learn.hms.harvard.edu/insights/all-insights/ai-clinical-research-opportunities-limitations-and-what-comes-next?utm_source=chatgpt.com)

### Summary Table

| Category | Key Points |
| --- | --- |
| What AI does | Augments scale, speed, pattern detection, cross-discipline workflows |
| What AI cannot do | Replace human creativity/intuition, guarantee validity, ensure full ethical/social oversight |
| Critical caveats | Bias, transparency, reproducibility, privacy, over-reliance |


---
## Should I trust AI

As AI becomes more deeply integrated into scientific research, one of the most common concerns among researchers is whether using large language models might inadvertently “give away” their ideas. These worries are understandable—after all, scientific innovation depends on protecting emerging hypotheses, unpublished data, and grant-sensitive intellectual work. Fortunately, when used correctly, modern AI tools can be trusted in the same way we trust other research infrastructure. Reputable AI providers (e.g., OpenAI, Anthropic, Google) now offer clear assurances that user inputs are not used to train future models when operating through enterprise, API, or institution-managed environments e.g., [OpenAI Data Usage Policy](https://openai.com/policies/usage-policies
). Importantly, this means your ideas are not added to training corpora and are not surfaced to other users. From a technical standpoint, the training of frontier models is frozen at a specific cutoff date, and the model cannot “learn” from your conversation in real time {cite}`Russell_Norvig_2021`. Furthermore, privacy-preserving AI practices—such as on-premise deployment, sandboxed environments, and encryption—align with established standards for protecting sensitive research data {cite}`kethireddy2020privacy`.

Trusting AI does not mean abandoning caution; it means using the right tool in the right context. For exploratory ideation, literature review, or rapid prototyping, AI can accelerate insight without exposing confidential details. For sensitive content (e.g., unpublished datasets, human subjects information, proprietary algorithms), local or institution-approved models provide additional guarantees. As with any scientific method, the key is controlled usage, documented workflows, and awareness of the environment in which the tool is running. With these safeguards in place, AI becomes not a threat to research integrity but a powerful collaborator—one that expands the researcher’s analytical reach while respecting intellectual ownership and privacy.
---

## U-M Context

At the University of Michigan (U-M), AI is not treated as an optional add-on—it is treated as a strategic research enabler, supported institutionally across disciplines. Some highlights:

*   The U-M research office observes: “AI has already created many new opportunities for U-M researchers … [the university] is making deliberate investments in infrastructure, talent and collaboration to integrate AI across our entire research enterprise.” [U-M Research+1](https://research.umich.edu/research-stories/going-all-in-on-ai/?utm_source=chatgpt.com)
*   For example, within U-M’s health and medical research, AI methods are used to detect genetic mutations in brain tumours in under 90 seconds, illustrating high-impact, translational applications. [Michigan Medicine](https://www.michiganmedicine.org/health-lab-podcast/using-ai-combat-cancerous-brain-tumors?utm_source=chatgpt.com)
*   The AI Research Committee at U-M recommended establishing guidelines, expanding AI consulting services, and investing in AI-ready infrastructure and training. [U-M Research](https://research.umich.edu/wp-content/uploads/2024/11/AI-Report-2024.pdf?utm_source=chatgpt.com)
*   U-M also emphasises responsible, inclusive AI: “AI with, for and by everyone can help maximise its benefits.” [cse.engin.umich.edu](https://cse.engin.umich.edu/stories/ai-with-for-and-by-everyone-can-help-maximize-its-benefits?utm_source=chatgpt.com)

### Implications for You (as a researcher at U-M)

*   Capitalise on institutional resources: U-M has hubs, consulting services, and infrastructure for AI-based research.
*   Be aware of institutional expectations: U-M emphasizes ethics, reproducibility, transparency, and equitable access when deploying AI.
*   Recognise that responsible AI adoption involves more than tool use — it involves training, planning, reviewing bias/validity, and documenting workflows.

### Recommended U-M-specific Actions

1.  Before integrating AI in your work, consult U-M’s AI research policy documents and any unit-specific guidelines.
2.  Evaluate whether AI adds value beyond “doing the same things faster” — ask: does it enable _new_ insights or just speed the old?
3.  Document your AI workflow (data sources, pre-processing, model choice, evaluation, limitations) to support reproducibility.
4.  Consider cross-disciplinary collaborations (e.g., data science core + domain scientist) to maximise rigour and creative potential.
5.  Stay alert for bias, privacy or ethical issues especially when working with sensitive data (e.g., biomedical, behavioural, neuroimaging).

---

## Conclusion

AI offers a powerful lever for accelerating and expanding research—but it is not a magic bullet. In the context of U-M (and similarly research-intensive institutions), success lies in combining technological tools with human insight, ethical reflection, rigorous methodology, and institutional support. As you embark on using AI in your research workflow, keep asking: _What new questions does this enable? What new value? What new risks?_

---
## References

```{bibliography}
:filter: docname in docnames
```
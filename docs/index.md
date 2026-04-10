# MIDAS Handbook: Applying AI in Research

```{image} _static/MIDAS_ai_logo.png
:alt: MIDAS AI in Research logo
:width: 800px
:align: center
:target: https://midas.umich.edu
```

**Primary Author:** Xiao-Su Hu (Frank), Research Data Scientist, Michigan Institute for Data and AI in Society (MIDAS), University of Michigan

**Contributors:** Nathan Fox, AI Scientist, Michigan Institute for Data and AI in Society (MIDAS), University of Michigan (AI Sandbox materials, adapted for Chapter 20)

```{admonition} Not sure where to start?
:class: tip

This handbook is a practical map of where AI fits across the research workflow. Pick the chapter that matches where you are right now.

**By role or goal (for example):**
- **Faculty exploring AI for your research** — Ch. 1, 4, 7, 8
- **Grad student working with data** — Ch. 3, 14, 15, 17
- **Research administrator or compliance focus** — Ch. 4, 10, 11
- **Just want the big picture first** — Ch. 1, 4, 11

**Looking for something specific?**
- **AutoML and predictive modeling** — Ch. 17, 18
- **RAG, AI agents, and LLM applications** — Ch. 24, 25, 26
- **External AI learning resources and tools** — Ch. 28
- **MIDAS workshop recordings and tutorials** — Ch. 31
- **U-M AI resources and support** — Ch. 27

Every chapter stands on its own. Jump in anywhere.
```

```{admonition} Want to try the code yourself?
:class: note

Several chapters include a companion Colab notebook. Look for the Open in Colab badge inside the chapter, click it, and the notebook opens directly in your browser with no local setup needed.

The examples are built around simple working datasets to give you a runnable starting point. The real goal is to bring your own problem — swap in your own data and see what happens.

Chapters with companion notebooks:
- Ch. 17 — Tabular prediction with AutoGluon
- Ch. 18 — Time series forecasting with AutoGluon
- Ch. 19 — Multimodal learning with AutoGluon
- Ch. 23 — NLP with Pre-trained Language Models
- Ch. 24 — Building a Research Knowledge Base with RAG
- Ch. 25 — AI Agents: From Single Answers to Multi-Step Research Tasks
```

## A Practical Guide to AI-Augmented Research

This handbook grew out of a recurring observation at MIDAS: researchers across many disciplines were asking the same kinds of questions about AI, often starting from scratch each time. What tools are actually useful? Where does AI fit into my existing workflow? How do I know whether to trust what it gives me? This handbook is an attempt to answer those questions in one place, in a form that researchers can return to as their work evolves.

It is written for faculty, graduate students, and research staff who already have a research job to do and want to know how AI can help them do it better. You do not need a computer science background to use most of it. Where the material gets more technical, the handbook flags that clearly and explains what level of familiarity you will need.

A few things worth saying upfront. This handbook is not a course in machine learning, and it is not a substitute for understanding your own data, methods, and domain. It will not turn you into an AI developer. What it will do is help you make more informed decisions about where AI fits in your research, how to use it responsibly, and how to get reliable results when you do.

What sets this handbook apart is its human-centered approach. We put domain knowledge first. We emphasize validation, reproducibility, and transparency at every step, and we are honest about what AI cannot do.

## How the Handbook Is Organized

The handbook follows the research lifecycle, from the earliest stage of framing a research question through data work, analysis, and finally sharing your findings. **You do not need to read it from beginning to end**. Each chapter is designed to stand on its own, so you can jump to whatever is most relevant to you right now.

**Part I: AI Across the Research Lifecycle** (Chapters 1 through 11) covers the process side of things. It starts with a conceptual introduction to what AI is and how modern AI systems actually work, moves into practical topics like prompt engineering and deciding when to use AI at all, and then works through specific research tasks: literature review, research planning, writing, grant development, peer review, and ethics. The last chapter in this part focuses on validation, which connects to nearly everything else in the handbook.

**Part II: AI in Data Analysis** (Chapters 12 through 22) is the hands-on section. It covers how to access and work with research data, how to set up computing environments, and then walks through a full analysis workflow from exploratory analysis and data preparation through AutoML, pre-trained models, and interpretation. These chapters assume basic familiarity with Python but are written to be accessible even if you are not primarily a data scientist.

**Part III: Building with Modern AI** (Chapters 23 through 26) goes deeper into the tools and approaches behind more sophisticated AI applications in research. This includes working with pre-trained language models for NLP tasks, building retrieval-augmented generation systems, designing AI agents for multi-step workflows, and evaluating or fine-tuning language models. These chapters are more technical and build on the material in Part II.

**Part IV: Resources and Reference** (Chapters 27 through 31) is the reference section. It includes a guide to AI tools and support available at the University of Michigan, a curated list of external resources, reusable templates, a glossary of key terms, and a video index of recorded workshops and tutorials.

The examples throughout this handbook are drawn from a range of disciplines, including economics, environmental science, social science, ecology, and linguistics. AI methods are not specific to any one field, and the decision-making frameworks here are meant to travel across research contexts.

## The AI-Augmented Research Lifecycle

AI can play a useful role at many points in a research project, but knowing where and how to use it well requires some planning. The diagram below shows the nine phases of the research lifecycle as we think about it in this handbook. Each phase presents its own opportunities and its own considerations for working responsibly with AI.

```{image} _static/research_lifecycle.png
:alt: The AI-Augmented Research Lifecycle showing nine phases from Research Design through Knowledge Sharing
:width: 50%
:align: center
```

The lifecycle starts with research design, where you think carefully about what questions AI can help you address and where your own judgment is irreplaceable. It moves through data access, preparation, and compute decisions, then into analysis at increasing levels of sophistication. The final phases focus on making sure your outputs are reproducible and well-documented, and on sharing your work with the broader community. The circled arrow back to phase one is intentional: good research is iterative, and what you learn along the way often reshapes how you think about the original question.

This handbook is a living document. The field of AI moves quickly, and we update the content regularly to reflect new tools, emerging practices, and lessons learned from researchers using this material in their own work. If you are returning after some time away, it is worth checking back — there is a good chance something new has been added since your last visit.

```{toctree}
:maxdepth: 2
:caption: Part I — AI Across the Research Lifecycle
:hidden:

part1/ch01_introduction
part1/ch02_how_ai_works
part1/ch03_prompt_engineering
part1/ch04_when_to_use_ai
part1/ch05_literature_review
part1/ch06_research_planning
part1/ch07_writing_communication
part1/ch08_grant_writing
part1/ch09_reviewing_with_ai
part1/ch10_ethics_privacy
part1/ch11_validation
```
```{toctree}
:maxdepth: 2
:caption: Part II — AI in Data Analysis
:hidden:

part2/ch12_data_access
part2/ch13_computing_resources
part2/ch14_exploratory_analysis
part2/ch15_data_preparation
part2/ch16_feature_engineering
part2/ch17_automl_tabular
part2/ch18_automl_timeseries
part2/ch19_automl_multimodal
part2/ch20_pretrained_text_vision
part2/ch21_validation_interpretation
part2/ch22_reproducibility
```
```{toctree}
:maxdepth: 2
:caption: Part III — Building with Modern AI
:hidden:

part3/ch23_nlp_with_bert
part3/ch24_rag
part3/ch25_ai_agents
part3/ch26_llm_eval_finetuning
```
```{toctree}
:maxdepth: 2
:caption: Part IV — Resources & Reference
:hidden:

part4/ch27_um_resources
part4/ch28_external_resources
part4/ch29_templates
part4/ch30_glossary
part4/ch31_video_index
```

---

## Citation and Reuse

This handbook is published under a [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) license. You are welcome to share, adapt, and build on this material for any purpose, as long as you give appropriate credit. The suggested citation is:

> Hu, X. (2026). *MIDAS AI in Research Handbook*. Michigan Institute for Data and AI in Society, University of Michigan. Retrieved from https://midas-ai-in-research.readthedocs.io

---

## How This Handbook Was Written

This handbook was written using AI-assisted tools as part of its core workflow, and we want to be transparent about what that looked like.

**Purpose of AI use:** The author developed the structure, frameworks, and core arguments for each chapter, drawing on research experience and observations from MIDAS research consultations. AI tools were then used to assist with drafting and refining the language, and all content was reviewed and revised through multiple rounds of discussion between the author and the AI.

**Tools used:** The primary tool was Claude (Anthropic), which handled roughly 80% of the AI-assisted work. Google Gemini and OpenAI's ChatGPT contributed the remainder. Both public commercial interfaces and University of Michigan enterprise tools were used, depending on the task.

**Human oversight:** Every section went through multiple rounds of review. That review drew on the author's experience as a researcher and on direct observations from MIDAS research consultations, where the same questions and misconceptions come up repeatedly when researchers across disciplines are learning to work with AI. All framing decisions, judgment calls, and final wording were made by the author, not the AI.

**Limitations and feedback:** AI-generated content can contain errors, and no review process eliminates that risk entirely. All content has been carefully checked against the contributors' knowledge and experience, but this handbook will evolve as the field does and as readers point out things we missed. If you find something that looks wrong or incomplete, we welcome your feedback through the form at the bottom of each page.

---

## Resources

The resources below were selected to give you a broader picture of where AI in research stands today and where it is heading. They pair well with the themes in this handbook, from understanding the overall landscape to thinking through the risks.

[Stanford HAI AI Index Report (2025)](https://hai.stanford.edu/ai-index/2025-ai-index-report) is one of the most comprehensive annual overviews of AI progress, adoption, and societal impact. It is a good starting point if you want data-driven context for the conversations happening in your field.

[ExplanAItions 2025: The Evolution of AI in Research](https://www.wiley.com/en-us/about-us/ai-resources/ai-study/) is a recent study focused specifically on how researchers across disciplines are using AI today. It offers a grounded look at actual practices and what researchers say is working and what is not.

[University of Michigan: Going All-In on AI](https://research.umich.edu/research-stories/going-all-in-on-ai/) describes how U-M is approaching AI across its research enterprise. If you are working within the U-M ecosystem, this piece gives helpful context for the institutional direction and the kinds of support that are becoming available.

[Yale News: Doing More, Learning Less — The Risks of AI in Research](https://news.yale.edu/2024/03/07/doing-more-learning-less-risks-ai-research) offers a useful counterpoint. As AI tools make certain tasks faster and easier, there is a real question about whether researchers are developing the deeper understanding their work requires. This is worth reading alongside the more optimistic accounts.
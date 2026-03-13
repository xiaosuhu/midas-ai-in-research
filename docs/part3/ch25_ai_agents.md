# AI Agents: From Single Answers to Multi-Step Research Tasks

:::{admonition} What you will learn
:class: tip

By the end of this chapter, you will understand what distinguishes an AI agent from a plain language model, why that distinction matters for research workflows that require more than a single answer, what kinds of multi-step tasks agents are already being used for in academic research, and how to think about this space without getting lost in the rapidly changing tool landscape.

This chapter does not include a companion notebook or implementation tutorial. The goal is conceptual clarity, because the tools in this area change quickly enough that the most durable investment you can make right now is understanding what agents are and what they can do.
:::

Imagine you are conducting a systematic review of the literature on community-based interventions for food insecurity. You have a clear research question, a set of inclusion and exclusion criteria, and a list of databases to search. Now think about what the next several days actually look like. You run searches across PubMed, Scopus, and Google Scholar. You download a few hundred abstracts. You read through them manually to flag which ones meet your inclusion criteria. You pull the full texts of the ones that pass the first screen. You extract the relevant variables from each paper: study design, sample size, intervention type, outcome measures, and so on. You organize all of this into a spreadsheet. Then you check your own work because you know how easy it is to miss something when you are reading abstract number 217 at 11 at night.

Every step in that list is something you understand completely. None of it requires expert judgment that only you can provide. And yet the whole process takes weeks, and a great deal of that time is spent on tasks that feel more like logistics than scholarship.

This is exactly the kind of situation that AI agents are designed to help with.

---

## What Makes an Agent Different from a Language Model

When you ask a language model a question, what you get back is text. The model takes your prompt, processes it, and produces a response. That is the entire transaction. The model has no memory of what you asked before, it cannot take any action in the world, and it cannot go back and revise its answer based on new information it discovers. It reads your input and writes something back. For many tasks, that is exactly what you need.

An agent is something more than that {cite}`kaggle2024genai_agents`. At its core, an agent is a system that can pursue a goal over multiple steps, taking actions, observing results, and adjusting its approach as it goes. Think of the difference between asking a colleague a question in a hallway and asking a colleague to handle a project for you. In the first case, they answer from what they already know. In the second, they might do some research, send a few emails, check some databases, write a draft, revise it based on feedback, and report back to you when it is done. Same underlying competence, very different scope of operation.

Three things make an agent different from a plain language model:

**Planning.** An agent can break a goal into steps and decide what to do next based on what has already happened. It is not just completing a single prompt. It is managing a sequence of actions oriented toward a larger objective.

**Tool use.** An agent can call external tools, including web search, code execution, file access, and APIs. This is what gives it the ability to actually do things rather than just describe them. A language model can tell you how to search PubMed. An agent can search PubMed.

**Memory.** Within a session, an agent keeps track of what it has already done and found, so each subsequent action can build on what came before. Some agent architectures also support longer-term memory that persists across sessions, though this varies by implementation.

These three capabilities together are what allow an agent to work through a task like the systematic review example above, rather than stopping after a single answer {cite}`kaggle2025agents_day1`.

One more thing worth noting: agents are not autonomous in the sense of being unsupervised. The goal, the constraints, and the tools are all specified by you. A well-designed agent workflow has checkpoints where a human reviews what has been done before proceeding. Thinking of an agent as a capable research assistant who works on your behalf, rather than as a system that operates independently, is a more accurate and safer mental model.

---

## What Agents Can Do in Research Contexts

A few scenarios where agents are already being put to use in academic research illustrate both the current possibilities and where things are heading.

**Automated literature triage.** A researcher studying climate adaptation policy sets up an agent with access to a literature database, a set of inclusion criteria, and instructions to produce a structured summary for each paper that passes the screen. The agent searches the database, retrieves abstracts, applies the criteria, pulls full texts for qualifying papers, and returns a spreadsheet with standardized fields filled in. This does not replace the researcher's reading, but it compresses the triage phase from weeks to hours and reduces the chance that relevant papers are missed because of inconsistent keyword searches.

**Multi-source data assembly.** A labor economist is tracking how state-level minimum wage changes relate to employment outcomes over a twenty-year period. The data she needs lives across federal databases, state government websites, and several research archives, in different formats and with different update schedules. She sets up an agent to pull from each source on a schedule, standardize the formats, run a set of validation checks, and flag discrepancies for her to review. The agent handles the logistics. She handles the interpretation.

**Iterative analysis assistance.** A computational social scientist is working through a dataset of social media posts to develop a coding scheme. She asks an agent to apply a draft codebook to a sample of posts, run frequency counts, identify posts that seem inconsistent with the coding rules, and propose refinements to the codebook. The agent does not finalize the coding scheme. It accelerates the iteration cycles so she can arrive at a stable scheme faster.

**Research workflow automation.** More broadly, any workflow that involves the same sequence of steps applied repeatedly to changing inputs is a candidate for agent automation. Running the same preprocessing pipeline across a new batch of data, generating structured summaries of meeting notes or field observations, checking a manuscript draft against a citation style guide, or reformatting references between systems are all tasks where the work is well-defined, repetitive, and does not require the kind of disciplinary judgment that only you can exercise.

The common thread across these examples is that the researcher defines the task and reviews the output. The agent handles the repetitive middle section. This framing, agent as capable logistics layer rather than independent analyst, is important for setting realistic expectations and for using these tools responsibly.

---

## The Tool Landscape Right Now

If you search for AI agent frameworks today, you will find a long and growing list: LangChain, LlamaIndex, AutoGen, CrewAI, LangGraph, and others. They differ in architecture, design philosophy, and the kinds of workflows they handle best. They also change frequently, and a framework that is widely recommended today may look quite different a year from now, or may be superseded by something new.

This is an honest description of where the field is, not a criticism of any particular tool. The underlying concepts, planning, tool use, and memory, are stable enough that understanding them will serve you well regardless of which implementation eventually settles into common use. The specific APIs and configuration details are not worth memorizing right now. If you have a concrete use case in mind, the right approach is to look at what is currently well-maintained, well-documented, and used by people working on similar problems to yours, rather than trying to pick a long-term winner in an unsettled landscape.

For U-M researchers, the AI Sandbox sessions run by MIDAS cover emerging tools in this space as they mature, which is a more reliable way to stay current than trying to track the ecosystem on your own.

---

## Further Reading and Learning Resources

The most accessible entry point into this topic is the material produced by Google and Kaggle as part of their free intensive courses on generative AI and agents.

The 5-Day Gen AI Intensive course includes a Day 5 whitepaper on agents that gives a clear conceptual overview of how agent systems are structured and how they differ from standalone language model calls {cite}`kaggle2024genai_agents`. The full course is available at [kaggle.com/learn-guide/5-day-genai](https://www.kaggle.com/learn-guide/5-day-genai).

The 5-Day AI Agents Intensive, released in 2025, goes deeper and is specifically organized around the question of when and why you would use an agent instead of a direct language model prompt. The Day 1 whitepaper is particularly relevant for researchers who want to understand the decision logic behind agent design {cite}`kaggle2025agents_day1`. That course is available at [kaggle.com/learn-guide/5-day-genai-agents-2025](https://www.kaggle.com/learn-guide/5-day-genai-agents-2025).

Both are free, require no account to read, and are written for a technical but not specialist audience.

```{admonition} If You're at U-M
:class: note

The MIDAS AI Sandbox sessions include modules on agentic workflows as part of the ongoing series on applied AI in research. These sessions are updated as the tool landscape evolves and are a good way to see current implementations demonstrated on research-relevant tasks. See [AI Resources at the University of Michigan](../part4/ch27_um_resources.md) for details on how to access these sessions.
```

---

## Try This

Think about a recurring workflow in your research that involves more than one step and does not require expert judgment at every point. It could be something you do weekly, something you dread at the start of every new project, or something you currently hand off to a research assistant because it is time-consuming but conceptually straightforward.

Write it out as a sequence of steps. For each step, ask yourself three questions. First, does this step require knowledge that only I have, such as domain interpretation, ethical judgment, or contextual familiarity with this particular study? Second, is this step something that could be described clearly enough for someone unfamiliar with the project to carry it out, given detailed instructions? Third, does the output of this step need to be verified before the next step begins, and by whom?

The steps that fall in the second category, well-defined and describable but time-consuming, are the ones where an agent could plausibly take over the execution. The steps in the first category are where your expertise is irreplaceable. The steps in the third category are your checkpoints. A research workflow that is agent-ready has a clear picture of all three.

You do not need to build anything right now. The exercise is about developing the habit of looking at your own work and asking where the logistics end and the scholarship begins.

---

## Related Chapters

- [Building a Research Knowledge Base with RAG](ch24_rag.md): the retrieval layer that many agent workflows use to give a model access to a specific document collection
- [NLP with Pre-trained Language Models](ch23_nlp_with_bert.md): foundational understanding of how language models represent and process text
- [Pre-trained Models for Text and Vision](../part2/ch20_pretrained_text_vision.md): hands-on exploration of language and vision models without writing code
- [Validation and Interpretation](../part2/ch21_validation_interpretation.md): how to evaluate outputs you did not produce entirely yourself

```{bibliography}
:filter: docname in docnames
```

---

**Questions or feedback?** [Open an issue on GitHub](https://github.com/xiaosuhu/midas-ai-in-research/issues)

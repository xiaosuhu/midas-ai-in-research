# Chapter 25: AI Agents: From Single Answers to Multi-Step Research Tasks

:::{admonition} What you will learn
:class: tip

By the end of this chapter, you will be able to:

- Explain what distinguishes an AI agent from a plain language model interaction
- Describe what context engineering means and why it matters for agent design
- Recognize which kinds of multi-step research tasks are good candidates for agent automation
- Evaluate the current tool landscape without getting lost in rapidly changing frameworks
- Identify where human oversight is essential in any agent workflow
:::

Say you just picked up a new research thread, maybe a collaborator pulled you into it, maybe a grant call nudged you toward it, and you need to get oriented fast. What has already been done in this space? Where are the open questions? Who is publishing on this right now? You start pulling up papers across PubMed, Google Scholar, and a couple of field-specific databases. You skim abstracts, save the ones that look relevant, and start building a rough map in your head of who is arguing what. A week later you have forty tabs open, a messy folder of PDFs, and a nagging feeling that you are missing something published last month that would have changed your framing.

None of this requires the kind of judgment that only you can bring to the work. It is closer to reconnaissance than scholarship, and yet it can eat up the better part of a week before you write a single sentence of your own.

This is the kind of work AI agents are actually good at right now.

Worth being upfront about one thing: this is not the same as running a formal systematic review, or SR for short, the kind of literature review that follows a strict, pre-registered protocol so its methods can be checked and repeated by anyone. If you are working toward a PRISMA-style SR meant for publication, the search and screening stages still need a human in the lead, agents included. More on why later in this chapter.

A companion notebook for this chapter demonstrates the core agent loop in minimal Python, without any framework, so you can see exactly what is happening at each step. Rather than abstracting the mechanics behind a library, it shows how a model decides to call a tool, receives the result, and decides what to do next.

---

## What Makes an Agent Different from a Language Model

When you ask a language model a question, what you get back is text. The model takes your prompt, processes it, and produces a response. That is the entire transaction. The model has no memory of what you asked before, it cannot take any action in the world, and it cannot go back and revise its answer based on new information it discovers. It reads your input and writes something back. For many tasks, that is exactly what you need.

An agent is something more than that {cite}`wiesinger2024agents`. At its core, an agent is a system that can pursue a goal over multiple steps, taking actions, observing results, and adjusting its approach as it goes. Think of the difference between asking a colleague a question in a hallway and asking a colleague to handle a project for you. In the first case, they answer from what they already know. In the second, they might do some research, send a few emails, check some databases, write a draft, revise it based on feedback, and report back to you when it is done. Same underlying competence, very different scope of operation.

Three things make an agent different from a plain language model:

**Planning.** An agent can break a goal into steps and decide what to do next based on what has already happened. It is not just completing a single prompt. It is managing a sequence of actions oriented toward a larger objective.

**Tool use.** An agent can call external tools, including web search, code execution, file access, and APIs. This is what gives it the ability to actually do things rather than just describe them. A language model can tell you how to search PubMed. An agent can search PubMed.

**Memory.** Within a session, an agent keeps track of what it has already done and found, so each subsequent action can build on what came before. Some agent architectures also support longer-term memory that persists across sessions, though this varies by implementation.

These three capabilities together are what allow an agent to work through a task like the literature exploration example above, rather than stopping after a single answer {cite}`blount2025introagents`.

One more thing worth noting: agents are not autonomous in the sense of being unsupervised. The goal, the constraints, and the tools are all specified by you. A well-designed agent workflow has checkpoints where a human reviews what has been done before proceeding. Thinking of an agent as a capable research assistant who works on your behalf, rather than as a system that operates independently, is a more accurate and safer mental model.

---

## Context Engineering: Designing What the Model Sees

You have probably heard the phrase "prompt engineering" before, and you may have a sense that writing good prompts involves being clear and specific. That framing is useful for simple, one-off interactions. But for agent workflows, a more precise concept applies: context engineering.

Context engineering is the practice of deliberately designing everything that goes into the model's context window at each step of a multi-step task {cite}`milam2025contexteng`. In a single-turn chat, the context is essentially just your message. In an agent workflow, the context at any given step might include a system prompt defining the agent's role and constraints, the original task description, a summary of what has already been done, the results of tool calls made in previous steps, retrieved passages from a document collection, and instructions about what output format is expected next. Every one of these elements is a design decision that affects what the model can and cannot do.

The reason this matters in practice is that models have no memory between steps except what you explicitly give them. If step three of a workflow needs to know what was found in step one, that information has to be passed forward in the context. If it is not there, the model cannot use it. If the context becomes so long that early instructions get pushed out, the model may lose track of its original goal. And if the retrieved passages or tool results that the model is working from are irrelevant or poorly formatted, the model will generate answers based on the wrong information no matter how capable it is.

For researchers building or evaluating agent workflows, this means the most important question is often not "which framework should I use?" but rather "what information does the model actually need at each step, and is that information reliably getting there?" A well-designed context at each step, with the right task description, the right retrieved documents, and a clear summary of prior actions, will outperform a technically sophisticated framework with a poorly designed information flow.

---

## What Agents Can Do in Research Contexts

A few scenarios where agents are already being put to use in academic research illustrate both the current possibilities and where things are heading.

**Exploring a new literature.** A researcher picking up a new topic sets an agent loose across a couple of databases with a rough set of keywords and a short description of what counts as relevant. The agent pulls candidate papers, writes a one-paragraph summary of each, groups them by theme, and flags a handful that keep getting cited by the others. None of this replaces reading the papers that matter. It just means you start reading them a week earlier than you would have otherwise.

One caveat worth flagging here: this works well for open-ended exploration, but it is a different story once you are running a formal systematic review with inclusion criteria and a registered protocol. Recent work comparing AI search tools against manually conducted reviews found recall rates for the search stage as low as 18 percent, largely because tools like these only reach into a narrow slice of the literature and miss anything behind a paywall {cite}`moens2025aiteam`. If the review needs to hold up to PRISMA-level scrutiny, keep a person driving the search and the screening. For a current view of where the major systematic review methodology groups and journals stand on AI use, see the library guidance covered in [AI Resources at the University of Michigan](../part4/ch27_um_resources.md#ai-use-in-research-library-guidance).

**Multi-source data assembly.** A labor economist is tracking how state-level minimum wage changes relate to employment outcomes over a twenty-year period. The data she needs lives across federal databases, state government websites, and several research archives, in different formats and with different update schedules. She sets up an agent to pull from each source on a schedule, standardize the formats, run a set of validation checks, and flag discrepancies for her to review. The agent handles the logistics. She handles the interpretation.

**Iterative analysis assistance.** A computational social scientist is working through a dataset of social media posts to develop a coding scheme. She asks an agent to apply a draft codebook to a sample of posts, run frequency counts, identify posts that seem inconsistent with the coding rules, and propose refinements to the codebook. The agent does not finalize the coding scheme. It accelerates the iteration cycles so she can arrive at a stable scheme faster.

**Research workflow automation.** More broadly, any workflow that involves the same sequence of steps applied repeatedly to changing inputs is a candidate for agent automation. Running the same preprocessing pipeline across a new batch of data, generating structured summaries of meeting notes or field observations, checking a manuscript draft against a citation style guide, or reformatting references between systems are all tasks where the work is well-defined, repetitive, and does not require the kind of disciplinary judgment that only you can exercise.

The common thread across these examples is that the researcher defines the task and reviews the output. The agent handles the repetitive middle section. This framing, agent as capable logistics layer rather than independent analyst, is important for setting realistic expectations and for using these tools responsibly.

---

## The Tool Landscape Right Now

If you search for AI agent frameworks today, you will find a long and growing list: LangChain, LlamaIndex, AutoGen, CrewAI, LangGraph, and others. They differ in architecture, design philosophy, and the kinds of workflows they handle best. They also change frequently, and a framework that is widely recommended today may look quite different a year from now, or may be superseded by something new.

This is an honest description of where the field is, not a criticism of any particular tool. The underlying concepts, planning, tool use, and memory, are stable enough that understanding them will serve you well regardless of which implementation eventually settles into common use. The specific APIs and configuration details are not worth memorizing right now. If you have a concrete use case in mind, the right approach is to look at what is currently well-maintained, well-documented, and used by people working on similar problems to yours, rather than trying to pick a long-term winner in an unsettled landscape.

---

## Companion Notebook and Further Reading

The companion notebook for this chapter is a minimal, framework-free agent loop built with the Google Gemini API, which has a free tier that requires no payment to use. It defines a simple `search_documents` tool, shows how the model decides whether to call it, and walks through the full loop of a multi-step agent interaction. The notebook includes step-by-step instructions for getting a free API key and storing it securely in Colab. Because it uses direct API calls rather than a framework layer, the mechanics of each step are visible rather than abstracted away.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/xiaosuhu/midas-ai-in-research/blob/v1.0-dev/docs/notebooks/agent_loop_demo.ipynb)

:::{admonition} Prefer not to use a cloud API?
:class: tip
The notebook uses the Gemini API for convenience, but the agent loop itself does not depend on any particular model provider. If your data is sensitive or you would rather avoid sending prompts to an external service, the same loop can be adapted to run against a local model served through [LM Studio](https://lmstudio.ai) or [Ollama](https://ollama.com), both of which expose a local endpoint that the code can call with minimal changes. See the [Running AI Models Locally](../part2/ch13_computing_resources.md#running-ai-models-locally) section in Chapter 13 for hardware requirements and setup options.
:::

The most accessible entry point into the broader conceptual landscape is the material produced by Google and Kaggle as part of their free intensive courses on generative AI and agents. There are three of them, and the names are similar enough that they are easy to mix up.

The 5-Day Gen AI Intensive is the broad one. It ran live in November 2024 and again in spring 2025, and its Day 3 whitepaper on agents gives a conceptual overview of how agent systems are structured and how they differ from standalone language model calls {cite}`wiesinger2024agents`. The course is available at [kaggle.com/learn-guide/5-day-genai](https://www.kaggle.com/learn-guide/5-day-genai).

The 5-Day AI Agents Intensive, held in November 2025, goes deeper on agents themselves. Its Day 1 whitepaper lays out a taxonomy of agent capabilities and argues for a discipline it calls Agent Ops, aimed at keeping agents reliable and governable {cite}`blount2025introagents`. Day 3 covers sessions and memory, and its whitepaper goes further into the context engineering ideas covered earlier in this chapter {cite}`milam2025contexteng`. That course is available at [kaggle.com/learn-guide/5-day-agents](https://www.kaggle.com/learn-guide/5-day-agents).

Google and Kaggle ran a third course in June 2026, the 5-Day AI Agents: Intensive Vibe Coding Course. It keeps the agent themes but changes the question. Instead of asking how an agent works, it asks how you build software when you describe what you want in plain language and AI tools write much of the code {cite}`kaggle2026vibecoding_course`. If you want to see where agentic coding tools are heading, this is the one to look at. For what it means for research code specifically, including where it helps and where it can quietly turn into a methodological decision you did not mean to make, see the [vibe coding discussion in Chapter 15](../part2/ch15_data_preparation.md#vibe-coding-what-researchers-need-to-know). That course is available at [kaggle.com/learn-guide/5-day-agents-vibecoding](https://www.kaggle.com/learn-guide/5-day-agents-vibecoding).

All three are free. The hands-on codelabs ask for a free Kaggle account with a verified phone number, and the materials are written with developers in mind, so expect to do a little translating for research settings.

```{admonition} If You're at U-M
:class: note

The MIDAS AI Sandbox sessions include modules on agentic workflows as part of the ongoing series on applied AI in research. Because the agent tool landscape shifts quickly, these sessions are a more reliable way to stay current with what is actually being used in practice than trying to track the ecosystem on your own. Sessions are updated as the tools evolve and are open to researchers across disciplines. See [AI Resources at the University of Michigan](../part4/ch27_um_resources.md) for details on how to access these sessions and the broader MIDAS program.
```

---

## Try This

Think about a recurring workflow in your research that involves more than one step and does not require expert judgment at every point. It could be something you do weekly, something you dread at the start of every new project, or something you currently hand off to a research assistant because it is time-consuming but conceptually straightforward.

Write it out as a sequence of steps. For each step, ask yourself three questions. First, does this step require knowledge that only I have, such as domain interpretation, ethical judgment, or contextual familiarity with this particular study? Second, is this step something that could be described clearly enough for someone unfamiliar with the project to carry it out, given detailed instructions? Third, does the output of this step need to be verified before the next step begins, and by whom?

The steps that fall in the second category, well-defined and describable but time-consuming, are the ones where an agent could plausibly take over the execution. The steps in the first category are where your expertise is irreplaceable. The steps in the third category are your checkpoints. A research workflow that is agent-ready has a clear picture of all three.

You do not need to build anything right now. The exercise is about developing the habit of looking at your own work and asking where the logistics end and the scholarship begins.

---

## Related Chapters

- [Chapter 24: Building a Research Knowledge Base with RAG](ch24_rag.md): the retrieval layer that many agent workflows use to give a model access to a specific document collection
- [Chapter 23: NLP with Pre-trained Language Models](ch23_nlp_with_bert.md): foundational understanding of how language models represent and process text
- [Chapter 20: Pre-trained Models for Text and Vision](../part2/ch20_pretrained_text_vision.md): hands-on exploration of language and vision models without writing code
- [Chapter 21: Validation and Interpretation](../part2/ch21_validation_interpretation.md): how to evaluate outputs you did not produce entirely yourself

*Last reviewed: September 2026. The agent framework landscape changes quickly; specific tool recommendations in this chapter may have evolved since this review. If you notice outdated content, [open an issue on GitHub](https://github.com/xiaosuhu/midas-ai-in-research/issues).*

```{bibliography}
:filter: docname in docnames
```

---

**Questions or feedback?** [Open an issue on GitHub](https://github.com/xiaosuhu/midas-ai-in-research/issues)

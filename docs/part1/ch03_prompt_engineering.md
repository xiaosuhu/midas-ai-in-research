# Prompt Engineering: Talking to AI More Effectively

:::{admonition} What You Will Learn
:class: tip
- Why rephrasing the same question can produce dramatically different answers from the same AI tool
- What makes a prompt clear and useful rather than vague and generic
- The difference between zero-shot and few-shot prompting, and when each approach works best
- What chain-of-thought prompting is and why it helps with tasks that require reasoning
- How system prompts and user prompts work together behind the scenes
- A practical way to iterate from a weak first prompt to a stronger one
:::

## The Same Question, Two Very Different Answers

A researcher studying urban water quality submitted two requests to an AI assistant within the same hour. The first was short: "What are the main sources of water contamination in cities?" The model returned a textbook-style paragraph listing agricultural runoff, industrial discharge, aging infrastructure, and stormwater overflow. It was accurate, general, and not particularly useful for what she actually needed.

The second request went differently. She wrote: "I am an environmental engineer preparing a policy brief for a mid-sized Midwest city with aging lead service lines. Please summarize the three most important sources of contamination to address in the next five years, given that the city has limited capital funding and cannot replace all infrastructure at once. Format your response as a short list with one sentence of explanation for each item."

The model's response focused on lead leaching from corroding service lines, opportunistic bacterial growth in pipes due to reduced flow during periods of low water demand, and localized contamination near historically underserved neighborhoods with older industrial sites nearby. It grounded each point in the funding constraint she had specified. The two prompts took about thirty seconds apart to write. The outputs were not even close to being the same.

This chapter is about understanding why that gap exists and what you can do about it. Prompt engineering is not a mysterious art or a skill reserved for programmers. It is a transferable set of habits, and once you grasp a few underlying ideas, you can apply them across almost any AI tool you use in your research.

## What Is a Prompt, Really?

When you type something into an AI assistant, you are providing the starting context for a text completion process. As described in the previous chapter, language models work by predicting what text should come next given everything they have seen so far. Your prompt is everything they have seen so far.

This means a vague prompt does not lead the model to ask you for clarification the way a human colleague might. It leads the model to fill in whatever assumptions seem statistically reasonable given the limited context you provided. If you ask "What are the effects of migration?" without specifying what kind of migration, the model guesses. It might assume human migration, animal migration, or even data migration in a computing context, depending on subtle cues in your phrasing. Whatever it assumes, it proceeds as if those assumptions are correct.

A useful way to think about this: a good prompt reduces the space of reasonable interpretations. The more specific and well-scoped your prompt, the less the model needs to fill in on its own, and the more likely the output reflects what you actually needed.

## The Ingredients of a Clear Prompt

Good prompts tend to share a few qualities. They do not all need to be present at once, and some tasks are simple enough that a short prompt works well. But when you are not getting what you need, these are the places to look first.

**Role and context.** Telling the model who you are and what you are working on makes a real difference. "I am a second-year PhD student in computational linguistics preparing a conference paper on code-switching in bilingual social media communities" gives the model far more to work with than "I am a researcher." Context shapes tone, vocabulary, depth of explanation, and what the model treats as assumed background knowledge.

**A specific task.** Rather than asking the model to "tell me about X," specifying what you want from the response is almost always more productive. "Summarize the three main arguments," "identify the key methodological limitations," and "compare these two approaches in terms of computational cost" all tell the model what kind of output to produce. Vague requests tend to produce vague outputs.

**Format requirements.** If you need a bulleted list, say so. If you need a 200-word summary, say so. If you need output you can paste directly into a table, describe the structure. Language models do not have preferences about output format; they will match whatever pattern you give them. Leaving format unspecified means you get whatever the model considers a reasonable default, which may or may not match what you need.

**Constraints and scope.** The water quality example at the start of this chapter worked in part because the researcher specified a real constraint: limited capital funding. Constraints help the model understand what counts as a good answer for your specific situation rather than the general situation.

None of this requires that every prompt be long. A well-targeted three-sentence prompt often outperforms a meandering ten-sentence one. The goal is precision, not length.

## Zero-Shot and Few-Shot Prompting

The terms zero-shot and few-shot come from the research literature on how language models generalize to new tasks, but the ideas behind them are intuitive enough to apply without knowing the technical background.

Zero-shot prompting means giving the model a task with no examples. You describe what you want and ask it to produce the output directly. This works well for tasks the model has encountered many versions of during training, such as summarizing an abstract, translating a sentence, or suggesting synonyms for a word. For these everyday tasks, the model's prior experience covers a wide enough range of inputs that no examples are needed.

Few-shot prompting means providing one or more examples of the kind of output you want before asking the model to produce something similar. The examples serve as a template, showing the model the format, tone, and level of detail you are expecting. This is especially useful when you need something in a specific or unusual format that the model would not naturally produce without guidance.

Here is a practical illustration. Suppose you are a sociologist who needs to classify open-ended survey responses about household financial stress into three categories: high stress, moderate stress, and low stress. A zero-shot prompt would describe the categories and ask the model to apply them. A few-shot prompt would include two or three example responses alongside your classifications, showing the model exactly how you want it to apply the categories to the particular kind of language your respondents used.

The few-shot approach tends to be more consistent when the task requires judgment that is calibrated to your specific research context, your discipline's conventions, or the particular characteristics of your data. The tradeoff is that writing good examples takes time, and if your examples are not carefully chosen, they can push the model toward patterns that do not generalize well across your full dataset.

## Chain-of-Thought Prompting

For tasks that involve reasoning across multiple steps, there is a well-documented tendency for language models to perform better when they are asked to work through the problem explicitly rather than jump straight to an answer {cite}`wei2022chain`. This approach is often called chain-of-thought prompting, and it reflects something fairly intuitive: reasoning through intermediate steps tends to produce more coherent conclusions than producing the conclusion in one leap.

In practice, you can activate this in a few ways. The simplest is to add a phrase like "think through this step by step before giving your final answer." A more structured version is to explicitly frame the problem as a sequence: "First, identify the key variables at play. Then consider how they interact. Finally, draw a conclusion based on that analysis." When the model generates intermediate reasoning, each step becomes context for the next one, which tends to keep the logic more coherent and makes errors easier to spot when you review the output.

This matters for research tasks more than it might initially seem. If you ask a model to evaluate whether a proposed study design has confounding variables, a simple yes or no answer is much less useful than a step-by-step walkthrough of the design, the variables the model identifies as potentially confounding, and why each one might create problems. The latter gives you something you can actually read critically, agree with, or push back on.

Chain-of-thought prompting does not guarantee correct reasoning. The model can still make errors, and those errors can propagate through its own chain of steps in ways that are harder to catch than a single wrong answer. The value is in making the reasoning visible so that you, the researcher, can evaluate it.

## System Prompts and User Prompts

When you use an AI tool that has been built and deployed by a developer or institution, there are often two layers of instruction shaping what the model does. The user prompt is what you type. The system prompt is a set of instructions that the application's developer wrote in advance, and it typically tells the model how to behave across all conversations on that platform: what persona to adopt, what topics to focus on, what tone to use, and sometimes what sources to draw from or avoid.

If you are using a tool like UM-GPT or a custom institutional AI assistant, there is likely a system prompt behind the scenes that shapes behavior even before you type anything. You usually cannot read it, but you can often infer its effects from patterns in how the model responds. A model that consistently redirects certain questions to a human expert is probably instructed to do so. A model that always uses formal academic language is likely prompted to do that as well.

When you are using an API or a development environment directly, you have control over the system prompt yourself, and this is one of the more powerful tools available for building consistent workflows. A well-designed system prompt can establish a model as a specialized research assistant for a specific domain, provide background context that applies to every interaction, and set output conventions that remain stable across a whole session. If you find yourself typing the same preamble at the start of every conversation with a general-purpose model, that preamble is probably better placed in a system prompt.

For most researchers using consumer AI tools, the practical implication is narrower but still worth knowing: the tool's behavior is partly shaped by instructions you did not write. If a model seems to be avoiding a topic or responding in a constrained way, that is usually the system prompt at work rather than a capability limitation of the underlying model.

For researchers who move beyond single-turn interactions into more automated, multi-step workflows, the question of what the model sees at any given moment becomes considerably more complex. This is sometimes called context engineering: designing not just a single prompt but the full set of inputs the model receives across an entire workflow, including retrieved documents, conversation history, tool outputs, and injected memory. Beyond that, building reliable AI agents in production environments involves what practitioners now call harness engineering: structuring the constraints, feedback loops, and environment around the model so that it behaves consistently over many steps and interactions. These ideas are covered in depth in [Chapter 25: AI Agents and Multi-Step Research Workflows](ch25_ai_agents.md).

## Iterating Toward a Better Prompt

One of the more useful things to understand about prompting is that you rarely get the best version on the first try, and that is completely normal. Experienced practitioners treat prompt writing as an iterative process, not a one-shot task.

A practical starting sequence looks something like this. Write a rough version of what you need without overthinking it and note what the output gets right and what it misses. If the output is off in tone or register, add more specific context about who you are and what the output is for. If the content is too shallow or too broad, add explicit instructions about what to go deeper on and what to leave out. If the format is wrong, specify the format you want and provide an example. If the reasoning seems muddled or hard to evaluate, ask the model to reason through the task step by step before producing its final answer.

Each round of revision narrows the gap between what the model assumed you needed and what you actually need. Most prompts stabilize within two or three rounds of adjustment.

There is also value in keeping a small personal library of prompts that have worked well for recurring tasks in your research. A prompt that reliably produces useful draft methods sections, or one that works well for summarizing papers in your field, is worth saving. You can refine it over time and reuse it across different AI tools.

## Two Research Examples

The following examples show how these ideas apply across different disciplines. The point is not to copy these prompts directly but to see the pattern of adjustments in action.

**Environmental science.** A PhD student analyzing satellite imagery wants help understanding how to distinguish deforestation events from seasonal vegetation loss in time-series data. A bare-bones prompt might be: "Explain deforestation in Southeast Asia." A stronger version would be: "I am a PhD student in environmental science working with Landsat 8 time-series data covering three provinces in Myanmar from 2015 to 2023. I am trying to distinguish permanent deforestation from seasonal vegetation changes. What variables in the imagery metadata are most useful for telling these apart, and what patterns in pixel-level spectral signatures should I look for? Please focus on practical indicators rather than theoretical background. Assume I am familiar with basic remote sensing concepts but not with this specific distinction."

The second version provides role context, names the dataset and geographic scope, frames the specific interpretive problem, requests a particular type of guidance, and sets an explicit expertise assumption. It takes four or five sentences and eliminates the need for several rounds of follow-up clarification.

**Sociology.** A researcher studying intergenerational wealth transfer wants to use AI to help apply a coding scheme to a set of interview transcripts. She could start with: "Help me code these transcripts for financial secrecy." A more effective version would be: "I am a sociologist studying how financial information is communicated across generations in high-net-worth American families. I am doing thematic analysis of 40 semi-structured interviews. I need you to apply four codes to the excerpt below: explicit financial secrecy, implicit financial secrecy, financial transparency, and ambiguous or unclear. After applying each code, write one sentence explaining your reasoning." The instruction to explain the reasoning is a chain-of-thought element that keeps the model's judgment visible and makes it much easier for the researcher to catch cases where the coding does not match her own conceptual framework.

## Try This

Take a task from your current research that you would normally ask an AI assistant to help with. Write your first prompt without overthinking it, the same way you might dash off a question to a colleague. Review the output and identify two or three places where it fell short: wrong level of detail, wrong format, missing context, or reasoning that does not quite hold up.

Now revise the prompt, addressing each gap directly. Compare the two outputs side by side and note specifically what changed and why you think the revised prompt produced a different result.

If the second output still has problems, try one more iteration. This time, add an instruction asking the model to reason through the task before giving its final answer. Notice whether that changes the quality of the reasoning or just the visible structure of the response.

The goal is not to find the perfect prompt. It is to build a practical sense of which adjustments move the output in the right direction. That intuition transfers across tools and disciplines, which makes it one of the more durable skills you can develop as an AI-assisted researcher.

## References

```{bibliography}
:filter: docname in docnames
```

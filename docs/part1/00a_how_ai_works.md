# How Modern AI Works: A Conceptual Guide for Researchers

:::{admonition} What You Will Learn
:class: tip
- What tokens and embeddings are, and why they matter for understanding AI outputs
- How the 2017 Transformer paper changed everything about how language models are built
- Why large language models hallucinate, and what that tells you about how they actually work
- What a context window is and what happens when a conversation approaches its edges
- Why the way you phrase a prompt has a real, structural effect on what you get back
:::

## The Citation That Did Not Exist

A graduate student in sociology was using a language model to get a head start on her dissertation's literature review. She asked for five foundational papers on organizational inequality in the workplace. Within seconds the model returned five citations, each formatted neatly: author names, journal title, volume number, page range, year. They looked completely real. She spent the next two hours tracking them down. Three of the five did not exist anywhere. One belonged to a real scholar who had written on a related topic but had not published the paper attributed to her. Another pointed to a real journal and a plausible-sounding title, but no such article appeared in any issue.

This experience is not unusual, and it raises a question every researcher using AI tools needs to be able to answer: why does a system that sounds so knowledgeable make things up? The answer has everything to do with how these systems are built and what they are actually doing when they generate text. That is the goal of this chapter.

You do not need a mathematics or engineering background to follow along. The goal is to give you enough of a conceptual picture that you can reason about what AI is likely to do well, where it is likely to go wrong, and why.

## Before the Transformer: Why Language Was Hard

For most of the history of computational approaches to language, building systems that could understand and generate natural text was an exercise in tradeoffs. The methods researchers used before about 2017 worked reasonably well on short, well-structured text but struggled with the thing that makes language interesting: meaning depends on context, and that context can span long distances.

Consider this sentence: "The city council refused the demonstrators a permit because they feared violence." Who does "they" refer to? A human reader almost always resolves this correctly, drawing on a mix of world knowledge and syntactic cues. The approaches used before 2017 processed language sequentially, reading through a sentence word by word and trying to maintain a kind of running memory of what came before. That memory tended to decay over distance, which meant long-range dependencies in text were genuinely hard to handle {cite}`LeCun2015deep`.

In 2017, a team at Google published a paper titled "Attention Is All You Need" {cite}`vaswani2017attention`. The architecture they introduced, called the Transformer, side-stepped the sequential limitation entirely. Instead of reading through text from left to right, the Transformer looks at all positions in the input at once and computes, for each word-piece, how much attention to pay to every other word-piece. This turned out to make a very large difference, both in what the resulting models could do and in how efficiently they could be trained. Almost everything called a large language model today is built on this foundation.

## What Is a Token?

To understand how a Transformer processes language, you need to know what it is actually working with. The answer is tokens, which are neither full words nor individual letters but something in between.

When you type a prompt into a language model, the model does not read it as you wrote it. It first breaks your text into tokens using a vocabulary learned during training. Common English words often map to a single token. Less common words get split into smaller pieces. The word "unhappiness" might become three tokens. A technical term you coined for your own research area might get split into four or five fragments the model has to reconstruct. Punctuation, spaces, and capitalization can all affect how tokenization works.

This matters for a few reasons. If you rely on domain-specific jargon, unusual abbreviations, or proper nouns that are rare in general text, the model may be working from fragments that do not carry the same meaning as the complete term would. Token count is also the unit by which models measure the length of a conversation, and it determines what fits inside the context window, which we will come to shortly.

## What Is an Embedding?

Once text is broken into tokens, each token gets converted into a vector: a list of numbers. In practice these lists can be hundreds or thousands of numbers long, but the intuition behind them is simpler than it sounds. Think of an embedding as a point in a very high-dimensional space, where the position of that point encodes something about the meaning of the token.

What makes embeddings powerful is that tokens with related meanings end up positioned near each other in this space. The vector for "physician" ends up in the same neighborhood as the vector for "doctor." The vector for "Paris" ends up among other European capital cities. These positional relationships are not hand-coded by anyone. They emerge from training, from the model processing an enormous quantity of text and gradually learning which words appear in similar contexts {cite}`LeCun2015deep`.

The Transformer does not process raw text. It processes these numerical representations, and as a sequence passes through layer after layer of the model, each token's representation gets reshaped by the context around it. The word "bank" starts with a general meaning but accumulates a more specific one as the surrounding tokens make clear whether the sentence is about finance or a riverbank.

## How the Transformer Actually Processes Your Input

The key innovation in the Transformer is the attention mechanism {cite}`vaswani2017attention`. For each token in the input, the model asks: given everything else in this sequence, which other tokens are most relevant to understanding this one right now? It assigns attention weights, essentially numerical scores for how much to let each other token influence the current one's representation, and it does this at every layer of the model.

The important thing is that attention is flexible and context-sensitive. In one sentence, the word "bank" might attend strongly to "river" and weakly to everything financial. In another sentence, the same word flips. No rule in the program tells the model to do this. It learns which attention patterns are useful by being exposed to billions of examples of text.

Modern large language models are Transformers with many layers, each one refining the representations further. They are trained on text from books, websites, academic papers, code repositories, and much else. The training objective is simple: predict the next token given all the tokens that came before {cite}`Brown2020gpt3`. Through that process of massive repeated prediction, the model picks up an enormous amount of statistical structure about language and, as a byproduct, about the world as it is described in language.

## Why Hallucinations Happen

This is where the sociology student's missing citations come from, and where the conceptual picture becomes most important for researchers to understand.

A language model does not store facts the way a database does. It does not have a filing cabinet where "Vaswani et al., 2017" lives and can be retrieved on demand. What it has is a vast set of learned statistical patterns: knowledge of how text tends to flow, what kinds of words tend to follow other kinds of words, what a properly formatted academic citation looks like, what kinds of topics cluster together in a sociology literature review. When the model generates text, it is doing something closer to very sophisticated pattern completion than it is to memory retrieval {cite}`bender2021stochastic`.

When you ask for citations on organizational inequality, the model constructs a response that has the right shape and texture for that request. It produces plausible author names, real-sounding journal titles, plausible volume and page numbers. It does this not by looking anything up but by generating tokens that are statistically consistent with what a list of academic citations looks like. If a real paper happens to match what the model generates, that is a coincidence of overlap between the pattern and the actual literature. If no such paper exists, the model has no mechanism to notice the gap.

Research on this phenomenon, often called hallucination, has found that it occurs not because models are careless but because fluent generation and factual accuracy are separate things {cite}`ji2023hallucination`. The model is optimized to produce plausible continuations of text. Plausible and accurate overlap much of the time, which is why these tools are so useful, but they are not the same thing. This is not a bug that will eventually be fixed with a software patch. It is a structural feature of how these systems work, which is why source verification is a non-negotiable habit rather than an optional precaution.

## The Context Window

Every language model has a context window: a limit on how many tokens it can consider at once when generating a response. Early models had small limits, a few hundred tokens. Modern models have pushed this much further, with some accepting more than a hundred thousand tokens, roughly the length of a short novel. But every model has a limit, and understanding what happens near that limit matters for how you use these tools.

Within the context window, the model has access to everything included in the current session: your initial prompt, any background material you pasted in, the full conversation history, and the system instructions set by whoever built the application you are using. All of that takes up space, and all of it is what the model can actually attend to when generating its next response.

When a conversation grows long enough to push older content outside the context window, that content becomes unavailable to the model. It does not fade gradually the way human memory does. It simply disappears from scope. This is one reason why long conversations can produce responses that seem to contradict or ignore things you said earlier in the same session. The earlier content is no longer visible to the model, not because it forgot in any human sense but because it can no longer see those tokens at all {cite}`Brown2020gpt3`.

In practice, this means that if you are working on a complex, multi-turn task or processing a long document, you should be thoughtful about what you include and where you put it. Stating the most important context and constraints near the beginning of your prompt, and repeating key requirements when a session has grown long, helps keep the model oriented. Pasting in an entire book chapter and then asking a question at the end may mean the model devotes most of its attention to material that is less relevant than what you intended.

## Why Prompting Works

If you have experimented with language models at all, you have probably noticed that how you phrase a request makes a real difference in what you get back. A vague question tends to produce vague output. A carefully constructed prompt with relevant context and a specific request tends to produce something considerably more useful. This is not coincidence, and it is not magic.

Because a Transformer is trained to complete text in contextually appropriate ways, the tokens you provide at the start of a generation serve as a strong signal about what kind of completion the model should produce. When you describe your expertise level and the specific purpose of a task, you steer the model toward patterns it learned from similar contexts {cite}`Brown2020gpt3`. When you provide an example of the format or reasoning you want, you activate the model's capacity to recognize and extend patterns it has seen before. When you give no context at all, the model has to fill in from its own prior, which may not be well-matched to what you actually need.

This is what makes prompting a skill worth developing rather than something arbitrary. You are not changing what the model knows. You are changing which part of its learned statistical landscape you activate. A prompt that begins with the structure of a peer review report tends to draw on patterns the model learned from peer review reports. A prompt that includes a few sentences written in the register of a methods section tends to draw on patterns the model learned from methods sections. The model is not reading your mind; it is reading your prompt very carefully.

The same logic explains why very short or ambiguous prompts tend to underperform. With less context, the model has more of its prior to fill in, and the mismatch between that prior and your actual goal grows larger.

## Pulling It Together

The sociology student's hallucinated citations make complete sense in this frame. The model was not lying, and it was not drawing from a corrupted database. It was generating text that has the shape and texture of a valid citation list, using patterns learned from an enormous training corpus that included many real citation lists. There was no mechanism to check against reality, because the model does not hold a live connection to academic literature. Plausibility and truth came apart, and plausibility won.

The concepts in this chapter connect directly to practical guidance throughout this handbook. Hallucinations are why Chapter 8 puts source verification at the center of any AI-assisted research workflow. Context windows explain why session length and prompt structure matter for complex tasks. The pattern-completion nature of generation explains why careful prompting, relevant context, and explicit format guidance consistently pay off.

None of this makes large language models unreliable tools. It makes them tools with a specific and unusual kind of intelligence, one that is genuinely powerful for many research applications and genuinely limited in others. Knowing which is which starts with understanding what these systems are actually doing.

## Try This

Pick a topic you know well from your own research and ask a language model to provide four or five key citations on it. Check each citation against a real database such as Google Scholar or your discipline's main index. Note how many citations are accurate, how many are plausible-sounding but nonexistent, and how many belong to real authors but misattribute the paper's title or venue.

Then try the exercise again with a more specific prompt. Provide some context about what aspect of the topic you care about and ask the model to briefly explain why each paper is relevant before listing the citation. Compare the accuracy rates across your two attempts.

The goal is not to find a foolproof prompting formula. It is to get a direct, practical sense of how these systems behave under different conditions, so that you can calibrate your own validation effort accordingly. Understanding the failure mode firsthand is more useful than reading about it in the abstract.

## References

```{bibliography}
:filter: docname in docnames
```

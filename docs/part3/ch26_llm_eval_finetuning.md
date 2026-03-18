# LLM Evaluation and Fine-tuning

:::{admonition} What you will learn
:class: tip

By the end of this chapter and its companion notebook, you will be able to:

- Evaluate an out-of-the-box language model on a specific research task and interpret the results
- Recognize the patterns that indicate a model is not well-suited for your problem
- Explain what fine-tuning is for and when it is the right tool for a downstream task
- Describe the trade-offs between full fine-tuning and parameter-efficient approaches
- Apply Low-Rank Adaptation (LoRA) fine-tuning using Hugging Face's Parameter-Efficient Fine-Tuning (PEFT) library as a computationally practical alternative to full fine-tuning
:::

Imagine you are studying how different scientific communities adopted machine learning methods over the past two decades. You have assembled several thousand research abstracts from fields like economics, environmental science, and computational biology, and your goal is to sort them by primary research domain so you can trace how terminology and framing shifted over time. You try a general-purpose language model. For the bulk of the corpus it does reasonably well, but when you start checking outputs against your own judgment you notice consistent errors: the model conflates applied statistics with econometrics, splits what you consider one category into two, and places a cluster of environmental modeling papers under physics. The errors are not random. They follow a pattern, and the pattern is meaningful. The model's internal sense of disciplinary boundaries comes from contemporary usage, not from how these fields understood themselves ten or twenty years ago.

This is a common situation. The model is not broken. It was trained on text from a different context than the problem you are trying to solve. The question is what to do about it, and in what order.

This chapter is organized around a specific goal: adapting a pre-trained language model to perform well on a **downstream task** — a concrete, domain-specific problem that is different from what the model was originally trained on. Pre-trained models learn general representations of language from large text corpora. Fine-tuning is the process of taking those representations and adjusting them for your particular task, whether that is classifying research abstracts by discipline, labeling sentences in interview transcripts, or scoring the sentiment of open-ended survey responses. Understanding that fine-tuning is always in service of a downstream task — not an end in itself — shapes every decision in this chapter: what to evaluate, when prompting is enough, and when the effort of fine-tuning is actually justified.

---

## Evaluating Before You Commit to Anything

The first thing to do when a model is not performing as expected is to measure exactly how badly it is failing, and on what kinds of examples. Without that measurement, any decision about what to fix is a guess.

**Building a reference set.** You need a collection of examples where you already know the right answer. For a classification task, that means a set of texts you or a knowledgeable colleague have labeled by hand. A hundred examples is often enough to detect systematic problems. Five hundred or more will give you more stable per-category estimates. The labels do not need to be exhaustive, but they need to be honest. If you are uncertain about a particular case, set it aside rather than labeling it arbitrarily and contaminating your evaluation.

**Measuring performance on your task.** For classification, the core metrics are accuracy and per-class F1 score. Accuracy tells you the overall fraction of correct predictions. Per-class F1 breaks that down by category, which matters because a model can look acceptable in aggregate while being essentially useless on a minority class that is important to your research question. If your label distribution is uneven, macro-averaged F1 is more informative than raw accuracy. For a fuller explanation of these metrics, including the precision and recall they are built from, see the "Choosing the Right Metrics" section in [Chapter 21](../part2/ch21_validation_interpretation.md).

For generation tasks like summarization or question answering, common automated metrics include ROUGE for summarization and BLEU for translation {cite}`papineni2002bleu`. These measure textual overlap between a model's output and a human-written reference. They are useful for getting a rough picture at scale, but they are not reliable indicators of factual correctness. A sentence can score well on ROUGE while being subtly wrong in ways that matter for research.

Factual correctness is where the problem of hallucination becomes central. Hallucination refers to cases where a language model generates plausible-sounding text that is not supported by its input or that contradicts known facts. Detecting hallucination systematically is difficult. One practical approach is to pull the original source for a sample of outputs and manually verify whether the specific claims the model makes are actually supported by that source. This is tedious, but for high-stakes applications it is necessary. More automated approaches exist, including using a second model as a judge, but those have their own accuracy limitations and introduce new sources of error.

**The role of human evaluation.** For qualitative dimensions like domain appropriateness, coherence, or whether the model is capturing the right distinctions for your research question, automated metrics often miss what matters most. Human evaluation, even on a small sample, is frequently more informative than any automated score. The practical question is how much time it costs against how much confidence you gain. A useful middle ground is to use automated metrics to catch obvious failures quickly, then do targeted human review on examples where the automated score is low or where you already suspect a particular failure mode. An hour spent reviewing fifty borderline cases will tell you more than a confusion matrix alone.

Once you have a concrete picture of where the model is failing, you are in a position to make a more informed decision about what to do.

---

## Recognizing When the Out-of-the-Box Model Is Not Enough

Sometimes better prompting is the right first step. If the model is applying the wrong categories because your prompt is ambiguous, adding a few labeled examples through few-shot prompting often helps substantially. [Chapter 3](../part1/ch03_prompt_engineering.md) in this handbook covers prompt engineering in detail. If you have not tried systematic prompt improvement yet, it is worth doing before considering fine-tuning. The effort is much lower, and it often gets you most of the way there.

But prompting has limits, and there are situations where no amount of prompt crafting will close the gap. The most common ones in research contexts follow a few recognizable patterns.

**Highly specialized domain language.** A general-purpose model trained on web text and books has limited exposure to specialized terminologies in fields like genomics, archival history, materials science, or computational linguistics. It may know that a particular term belongs to a domain without being reliable about the specific distinctions that matter for your task. Models that were pretrained on domain-specific corpora, like BioBERT for biomedical text {cite}`lee2020biobert` or SciBERT for scientific literature {cite}`beltagy2019scibert`, often do substantially better in those settings. Before fine-tuning from scratch, it is always worth checking whether a domain-adapted model already exists for your field.

**A classification scheme defined by disciplinary convention.** Sometimes the distinctions you need to make are not recoverable from plain meaning alone. In the example above, the boundary between applied statistics and econometrics is not something a model can fully reconstruct from a text description of the categories. It reflects decades of disciplinary history and publishing practice that the model was not trained on. Prompts can guide a model toward a definition, but they cannot supply the underlying experience.

**Consistent systematic errors on a specific type of input.** If your evaluation reveals that the model makes the same kind of mistake repeatedly on a particular subgroup of your data, that is a sign the problem runs deeper than prompting. A model that reliably misclassifies passive-voice sentences in a particular way, or consistently fails on texts that contain a specific structural pattern, is showing you a distribution mismatch that a prompt adjustment is unlikely to overcome.

When you hit these walls, fine-tuning is worth thinking about seriously.

---

## What Fine-tuning Actually Costs

Fine-tuning a language model means continuing its training on a dataset specific to your task, adjusting the weights so the model performs better in your context. In principle it is just more gradient descent. In practice it comes with costs that are easy to underestimate.

**Data.** You need a labeled dataset large enough to teach the model something meaningful. For text classification, a few hundred to a few thousand examples per category is a reasonable target, depending on how difficult the distinctions are. Collecting and labeling that data is often the hardest part. If your domain requires expert annotators rather than general-purpose crowdworkers, the cost and coordination time increase accordingly. Data quality matters more than quantity: a hundred carefully labeled examples will outperform five hundred careless ones.

**Compute.** Full fine-tuning of a model like BERT, which has around 110 million parameters, on a single GPU is manageable. Full fine-tuning of anything in the current generation of large language models, which typically have several billion parameters, requires hardware that most researchers do not have ready access to. Training a seven-billion-parameter model for a few epochs requires multiple high-memory GPUs and several hours of wall time. On commercial cloud infrastructure that can easily reach hundreds of dollars for a single experiment, and if the first run has a bug in your data pipeline, you pay again.

**Maintenance.** A fine-tuned model is not a one-time solution. If the underlying task changes, if new vocabulary enters your domain, or if the base model is updated or deprecated, you may need to redo the fine-tuning. Every fine-tuned checkpoint is also a file you need to store, version, and document. A research project that produces multiple fine-tuned model checkpoints across several experimental iterations has quietly become a small software infrastructure project.

For most academic researchers working on individual or small-team projects, the overhead of full fine-tuning is prohibitive for routine use. It makes sense when you have a clearly justified need, a substantial labeled dataset, and access to institutional computing resources. It does not make sense as a first resort.

---

## LoRA: Getting Most of the Benefit at a Fraction of the Cost

The key insight behind parameter-efficient fine-tuning is that you probably do not need to update all of a model's weights to adapt it to a new downstream task. A large language model has already learned a great deal about language and structure during pretraining. What it needs for your specific task is a relatively small adjustment on top of that foundation — enough to shift its behavior toward the distinctions your task requires, without overwriting the general knowledge that makes it useful in the first place.

Low-Rank Adaptation (LoRA) is the most widely used approach in this family {cite}`hu2022lora`. The intuition is geometric. When you fine-tune a model on a downstream task, the changes to any given weight matrix tend to have low intrinsic dimensionality. Even though the matrix may be very large, the adjustments that are actually needed can be well-approximated by a much lower-dimensional structure.

LoRA takes advantage of this by not modifying the original weight matrices at all. Instead, it introduces pairs of small trainable matrices alongside the frozen original ones. One matrix is tall and narrow, the other is short and wide, and their product approximates the update that full fine-tuning would have learned. If an original weight matrix has dimensions 768 by 768 (about 590,000 values), a LoRA adapter with rank 16 represents that update with two matrices totaling roughly 25,000 values. You train those small matrices, and the original weights stay frozen.

The result is that LoRA typically trains less than one percent of a model's total parameters, while achieving performance that is competitive with full fine-tuning on many downstream tasks {cite}`hu2022lora`. The original model weights are never changed, which means you can save an adapter as a file of a few megabytes rather than a full model checkpoint of several gigabytes, and you can swap adapters in and out for different tasks without maintaining separate full copies of the model.

Hugging Face's Parameter-Efficient Fine-Tuning (PEFT) library makes this practical in a few lines of code {cite}`mangrulkar2022peft`. You define a `LoraConfig` specifying the rank and which layers to apply adapters to, wrap your model with the `get_peft_model` function, and train as you normally would. The training loop does not change. Only the parameter count does.

```python
from peft import LoraConfig, get_peft_model, TaskType

config = LoraConfig(
    task_type=TaskType.SEQ_CLS,
    r=16,
    lora_alpha=32,
    lora_dropout=0.1,
    target_modules=["q_lin", "v_lin"]
)

peft_model = get_peft_model(base_model, config)
peft_model.print_trainable_parameters()
# trainable params: 369,664 || all params: 66,955,778 || trainable%: 0.55
```

The `r` parameter is the rank of the low-rank matrices. Higher rank gives the adapter more expressive capacity at the cost of more trainable parameters. For most classification tasks, ranks between 8 and 32 work well. The `target_modules` argument specifies which layers receive adapters. For BERT-family models, the query and value projection matrices in the self-attention layers are the standard choice.

A few other parameter-efficient approaches are worth knowing about, even if LoRA is currently the most popular. Prefix tuning prepends a small set of trainable vectors to the input at each transformer layer instead of modifying the attention weights. Prompt tuning is a lighter variant that adds trainable tokens only at the embedding layer. Both can be useful when you want to minimize the number of parameters touched, but LoRA generally produces stronger results across a wider range of classification and generation tasks.

---

## Running in Colab with a GPU

The companion notebook walks through a complete workflow on Google Colab using a T4 GPU. Enable the GPU by going to **Runtime**, clicking **Change runtime type**, and selecting **T4 GPU**. The full training run takes under ten minutes on a T4.

The notebook uses arXiv abstract classification as its running example. The task is to assign a research abstract to one of several scientific subject areas based only on its text. This is a realistic problem: anyone building a literature monitoring tool, a topic tracker, or a search system for academic content faces some version of it. The dataset comes from the Hugging Face Hub and requires no preprocessing.

The four steps in the notebook follow the logic of this chapter.

**Step 1: Evaluate the out-of-the-box model.** A pretrained zero-shot classifier is applied to a sample of arXiv abstracts. The model makes reasonable guesses on obvious cases but struggles with abstracts that rely on domain conventions rather than plain-language cues. Accuracy and per-class F1 document exactly where it falls short.

**Step 2: Examine what full fine-tuning would require.** The parameter count of the base model is printed, and a rough estimate of what full fine-tuning would cost in time and compute is worked through. This is not hypothetical. The notebook shows the numbers for the specific hardware context you are running in.

**Step 3: Apply LoRA fine-tuning with PEFT.** A `LoraConfig` is defined, the base model is wrapped, and training runs on the labeled arXiv data. You can watch the training loss decrease as the adapter adjusts to the task.

**Step 4: Compare results.** The fine-tuned model is evaluated on the same held-out test set, and the metrics are compared side by side with the baseline. The improvement in accuracy and per-class F1 is the concrete payoff for the fine-tuning work.

```{admonition} If You're at U-M
:class: note

For larger fine-tuning experiments or datasets that do not fit comfortably in Colab, Great Lakes provides GPU nodes with more memory and no session time limits. See [AI Resources at the University of Michigan](../part4/ch27_um_resources.md) for access and allocation information.
```

---

## Research Considerations

A few things are worth keeping in mind before you fine-tune a model for research purposes.

**Your labeled data is a research artifact.** The dataset you create for fine-tuning documents something about how you interpret your domain. Describing how it was constructed, what the annotation guidelines were, and where annotators disagreed is part of responsible reporting. If you publish work that depends on a fine-tuned model, your methods section should include enough detail that someone else could replicate the dataset creation process.

**Small datasets can overfit.** LoRA reduces the risk of overfitting compared to full fine-tuning, because fewer parameters are being updated. But with fewer than a few hundred training examples per class, overfitting is still a real concern. Monitoring validation loss during training and using early stopping is a straightforward safeguard.

**The base model matters.** If your domain has a specialized pretrained model available, it is usually better to start from that than from a general-purpose one. Fine-tuning SciBERT with LoRA on scientific abstracts will typically outperform fine-tuning vanilla BERT with LoRA on the same data, because the starting point already has better representations for the domain {cite}`beltagy2019scibert`.

**Adapters are easy to version.** Because LoRA adapters are small, you can store a fine-tuned adapter alongside your code in a repository, which makes reproducibility much more tractable than managing full model checkpoints. Chapter 22 covers reproducibility practices in more detail.

---

## Try This

Open the companion notebook and run all four steps. When you reach Step 4, spend time on the per-class F1 scores rather than just the overall accuracy number. Find the category where the improvement from fine-tuning was largest and the one where it was smallest. For the category with the smallest improvement, look at some of the examples that are still being misclassified after fine-tuning. Are they cases where even a human expert might find the boundary ambiguous, or are they cases where the model is making a systematic error that more data would likely fix? Thinking through that question is the beginning of understanding what kind of investment in data collection would actually help versus what is a fundamental limit of the approach.

If you have a text classification problem from your own research, try adapting the notebook to your domain. The code changes are minor: you supply your own dataset and your own label names. The more interesting work is building a reference set to evaluate against and deciding whether the performance you see is adequate for your intended use.

---

## Further Reading

Hu et al. (2022) is the original LoRA paper and is readable without a deep machine learning background {cite}`hu2022lora`. The introduction and the experiments section are the most useful parts for a research context. The Hugging Face PEFT documentation at huggingface.co/docs/peft provides a practical guide to the library, including worked examples for several task types {cite}`mangrulkar2022peft`. Ji et al. (2023) survey hallucination in natural language generation at length if you want to go deeper on the evaluation side. For biomedical and scientific text specifically, Lee et al. (2020) on BioBERT and Beltagy et al. (2019) on SciBERT illustrate the kind of improvement that domain-adapted pretraining provides before any task-specific fine-tuning {cite}`lee2020biobert,beltagy2019scibert`.

---

## Related Chapters

- [NLP with Pre-trained Language Models](ch23_nlp_with_bert.md) — using pre-trained models out of the box, which this chapter builds from
- [Prompt Engineering](../part1/ch03_prompt_engineering.md) — often the right first step to try before considering fine-tuning
- [Validation and Interpretation](../part2/ch21_validation_interpretation.md) — evaluating model outputs more broadly across task types
- [Reproducibility](../part2/ch22_reproducibility.md) — versioning and documenting fine-tuned model adapters

*Last reviewed: March 2025. Tool-specific content in this chapter refers to Hugging Face Transformers (4.x) and PEFT. If you notice outdated content, [open an issue on GitHub](https://github.com/xiaosuhu/midas-ai-in-research/issues).*

```{bibliography}
:filter: docname in docnames
```

---

**Questions or feedback?** [Open an issue on GitHub](https://github.com/xiaosuhu/midas-ai-in-research/issues)

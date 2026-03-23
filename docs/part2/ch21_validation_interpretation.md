# Chapter 21: Validation and Interpretation of AI-Assisted Analysis

:::{admonition} What You'll Learn
:class: tip
- How to validate AI-assisted analysis across three layers: technical, statistical, and domain
- How to interpret machine learning results with appropriate skepticism
- Which evaluation metrics matter and when, beyond just accuracy
- How to report AI-assisted findings transparently
:::

## When the Numbers Look Fine but Something Is Off

Imagine you are running an fNIRS study on language development in children. The preprocessing pipeline runs cleanly, your signals look reasonable, and the analysis produces a clear result: the right hemisphere shows significantly stronger activation than the left during a language task. The numbers are there, the statistics pass, and the code ran without a single error.

And yet, if you know anything about psycholinguistics, that finding should make you pause. Language processing in most right-handed individuals is strongly left-lateralized, a pattern so well established across decades of neuroimaging research that a right-dominant result is not a discovery you stumble into by accident {cite}`Springer1999`. Before you start thinking you have overturned the literature, the more productive question is: what went wrong in the analysis?

This is what validation actually looks like in practice. It is not a formality you complete after the analysis. It is the habit of asking whether your results make sense at every layer, from whether the code executed correctly, to whether the statistics hold up, to whether the finding is even plausible given what the field already knows. Interpretation follows from that: once you are reasonably confident the analysis is correct, you then have to figure out what it actually means for your research question.

This chapter walks through both.

## Two Questions Worth Keeping Separate

Researchers often talk about validation and interpretation as if they are one task, but they are asking different things. Validation is asking: did this analysis work correctly? Interpretation is asking: what does the result mean?

It is worth keeping them separate because they can come apart. An analysis can be technically correct and still be meaningless for your question. And a finding can be substantively interesting and still rest on a methodological mistake. Working through them in order, validation first, interpretation second, keeps you from making sense of results that do not yet deserve to be made sense of.

## Validation: Three Layers

### Layer 1: Technical Validation

The first layer is the most basic: did the analysis actually do what you intended? This sounds obvious but it is easy to skip in practice, especially when AI-generated code looks clean and runs without errors. Running without errors is not the same as running correctly.

A few things worth checking at this layer. First, do the model assumptions hold? A linear model assumes a linear relationship; a time series model assumes stationarity. AI tools will generally not flag when those assumptions are violated unless you ask them to. Second, is there any data leakage? This is one of the more common and damaging mistakes in applied machine learning: information from your test set inadvertently influencing training, which makes the model look better than it actually is. It can happen in subtle ways, like fitting a scaler on the full dataset before splitting, or including a feature that is only available after the outcome is known. Third, do intermediate outputs make sense? Spot-checking a few predictions, looking at distributions before and after preprocessing, and confirming that sample sizes match what you expect can catch a surprising number of issues before they become problems.

Reproducibility, meaning whether someone else can run your analysis and get the same result, is closely related to technical validation but gets its own treatment in the next chapter.

### Layer 2: Statistical Validation

Once you are satisfied the analysis ran correctly, the next layer is whether the results are statistically sound.

Sample size is one of the first things to think about. A result can be statistically significant with a large enough sample even when the actual effect is tiny and practically irrelevant. The reverse is also true: a real effect can look non-significant in a small sample. It helps to think about effect sizes alongside p-values, because effect sizes tell you something about the magnitude of what you found, not just whether it crossed a threshold.

Multiple testing is another common place where things go wrong quietly. If you are running many comparisons across features, time points, or brain regions, some of them will look significant by chance. Corrections like Bonferroni or Benjamini-Hochberg exist for this reason, and it is worth being explicit about whether and how you applied them.

Confidence intervals deserve more attention than they usually get. A confidence interval tells you something about the precision of your estimate. A result that is statistically significant but carries a confidence interval spanning nearly the full plausible range of the effect should be interpreted with considerably more humility than one with a tight interval around a meaningful estimate.

### Layer 3: Domain Validation

This is where the fNIRS example fits. Domain validation is the step where you ask whether the result makes sense given what is already known in your field. It requires actual expertise, and it is the layer that AI tools are least equipped to help with on their own.

A few specific things to look for. Do the effect sizes land in a plausible range? If you are studying a subtle cognitive effect and your model is explaining 80% of the variance, that is a sign something may be off. Are there unexpected directions, like a positive relationship where theory predicts a negative one? Those cases call for investigation before they call for interpretation. Are there findings that seem to only emerge in one subgroup or under one set of conditions, in a way that does not have a theoretical explanation?

None of these are automatic disqualifiers. Sometimes you do find something surprising and it holds up. But the threshold for that claim is higher than for a result that fits neatly with existing knowledge, and domain validation is how you figure out which situation you are in.

## Interpretation: What Do the Results Actually Mean?

### Choosing the Right Metrics

If you ask an AI tool to evaluate a classifier and it returns an accuracy of 92%, that number needs context before it means anything. The first question is always: what is the baseline? If 92% of your samples belong to one class, a model that predicts that class every single time will also achieve 92% accuracy without learning anything.

This is why it is worth understanding what different evaluation metrics are actually measuring. Accuracy counts all correct predictions equally, which is a problem when classes are imbalanced. Precision asks: of all the cases the model flagged as positive, how many actually were? Recall asks: of all the actual positive cases, how many did the model catch? These two are often in tension with each other. A model tuned for high recall will catch more true positives, but at the cost of more false positives. A model tuned for high precision will be more conservative, missing some true positives to reduce false alarms. F1 score summarizes this tradeoff as the harmonic mean of precision and recall. AUC, the area under the ROC curve, gives you a threshold-independent view of how well the model separates the two classes overall.

Which metric matters most depends on your research context. In a study where missing a true positive has serious consequences, recall is usually the priority. In a setting where acting on a false positive is costly, precision matters more. Knowing this before you evaluate your model will help you interpret the results much more meaningfully than looking at accuracy alone.

### Feature Importance Is Not Causal

Machine learning models can tell you which features were most predictive in your dataset. What they cannot tell you is why. A feature being highly important means the model found it useful for making predictions, not that it has a causal role in the outcome. In many datasets, features that seem predictive are actually standing in for something else, a confound, a proxy, or a data artifact, and unpacking that requires domain reasoning, not just model output.

This distinction matters for how you frame findings in your writing. Saying a feature was "strongly associated with" the outcome is defensible. Saying it "drives" or "causes" the outcome is a stronger claim that requires more than feature importance scores to support.

### Common Pitfalls

A few patterns come up frequently enough in AI-assisted research to be worth naming directly.

Overfitting is when a model learns the training data too well, including its noise, and then performs poorly on new data. The fix is proper train/validation/test splits and, ideally, cross-validation so you have a more stable estimate of generalization.

Data leakage was mentioned above under technical validation, but it is worth repeating here because its effects show up as interpretation problems: results that look implausibly good are sometimes a sign that the model has access to information it should not.

P-hacking, or running many analyses until something crosses a significance threshold, is a real risk when AI tools make it easy to try many variations quickly. Pre-registering your analysis plan and correcting for multiple comparisons are the standard mitigations.

Confounding happens when a variable you did not account for is actually driving the relationship you observed. This is particularly hard to catch with automated analysis because the tools do not know which variables in your dataset are conceptually related. Domain knowledge is the main defense here.

Cherry-picking, reporting only the analyses that worked and leaving out the ones that did not, distorts the literature even when no single reported finding is technically false. A good habit is to document every analysis you ran, not just the ones you report.

## Reporting AI-Assisted Results

How you write up findings from AI-assisted analysis matters both for scientific integrity and for readers who need to evaluate your work.

In your methods section, describe which AI tools you used, including the name and version. Explain how you validated the outputs and what human decisions were made throughout the workflow. If prompts or code were central to the analysis, consider including them in supplementary materials.

In your results section, do not just report the final numbers. Show model diagnostics, report validation metrics alongside performance metrics, and include uncertainty estimates where relevant. A result with no uncertainty quantification is harder to evaluate than one that comes with confidence intervals or comparable information.

In your discussion, interpret the findings in the context of what is already known in your field. Be explicit about limitations: what the model cannot do, where it might generalize poorly, and what would be needed to replicate or extend the work. Suggesting that an independent team replicate the key findings is a reasonable standard for AI-assisted work, just as it would be for any computationally intensive analysis.

## Quick Reference Checklist

Before reporting AI-assisted analysis, it is worth running through these:

- [ ] Model assumptions are met and have been checked
- [ ] No data leakage in preprocessing or feature construction
- [ ] Sample size is adequate for the effect you are trying to detect
- [ ] Significance tests are appropriate for the data structure
- [ ] Multiple testing corrections applied where relevant
- [ ] Confidence intervals or uncertainty estimates are reported
- [ ] Results are consistent with domain knowledge, or surprising results have been investigated
- [ ] Effect sizes are in a plausible range
- [ ] Evaluation metrics match the research context (not just accuracy)
- [ ] Feature importance claims do not overstate causality
- [ ] All analyses attempted are documented, not just the ones that worked
- [ ] Limitations are stated explicitly

## Try This

Before you run your next AI-assisted analysis, write down what result you expect to see and why. After the analysis, compare what you got against that prior. If they match, great. If they do not, treat that as an invitation to dig in rather than a reason to either dismiss the result or immediately celebrate it. This habit of making predictions explicit before looking at outputs is one of the simplest ways to build validation into your workflow.

## Related Chapters

- [Chapter 11: Validation Modes and Study Design](../part1/ch11_validation.md) - General principles on validation from Part 1
- [Chapter 17: AutoML with AutoGluon](ch17_automl_tabular.md) - Validating automated modeling pipelines
- [Chapter 22: Reproducibility](ch22_reproducibility.md) - How to make your analysis reproducible

```{bibliography}
:filter: docname in docnames
```

---

**Questions or feedback?** [Open an issue on GitHub](https://github.com/xiaosuhu/midas-ai-in-research/issues)

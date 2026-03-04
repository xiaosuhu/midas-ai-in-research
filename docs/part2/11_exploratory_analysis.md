# Exploratory Data Analysis with AI

:::{admonition} What You'll Learn
:class: tip
- How to use AI to accelerate your first pass through data
- What questions to answer before you touch a single row
- Generating visualizations and summary statistics to understand what you're working with
- Identifying data quality issues that will guide your cleaning strategy
- The iterative nature of EDA: initial exploration before prep, deep exploration after
:::

## The Two-Pass Journey

You just received your dataset. Before you run a single model or write a cleaning script, you need to answer a few basic questions: What is each column? Which one are you trying to predict or explain? Where are the gaps, and are those gaps random or concentrated in a way that matters?

This is what EDA is really about. It is not just running `.describe()` and moving on. It is taking the time to build a mental model of your data, column by column, before you trust it with anything important.

This chapter covers the first pass, the initial exploration you do when the data is still unfamiliar. You will discover its shape, its gaps, its quirks, and its quality issues. These discoveries will guide your cleaning strategy in the next chapter.

After cleaning and preparing the data, you will return for a second, deeper exploration. That is when you investigate relationships, test assumptions about distributions, and look for patterns with confidence, because by then you will trust what you are working with.

## A Quick Example

Imagine a public health researcher who just received a dataset from a multi-site collaborative study. It has 8,000 rows and 42 columns, and they have never seen it before.

The first thing they do is ask an AI to generate a quick summary. Within 15 minutes, they know the row and column counts, the data types for each variable, and where missingness is concentrated. One critical variable is missing in about 12% of rows, and those rows turn out to be disproportionately from one study site. Dates are stored in three different formats across sites. Two columns have identical names but different scales.

None of this is catastrophic. But all of it would have caused silent errors if left unchecked. Now they know what to fix, and why.

That is the value of a careful first-pass EDA. It takes maybe an hour. It saves days.

## Starting With the Right Questions

Before generating a single plot, it helps to get grounded in what the data is supposed to represent. Some questions worth answering at the start:

**What does each column actually mean?** Column names are often abbreviations, legacy labels, or ambiguous shorthand. If you have a data dictionary, read it. If you do not, ask a collaborator or use AI to help you infer meaning from context. You should be able to describe every column in plain language before you start modeling.

**Which column is your outcome or target?** Whether you are doing supervised learning, regression, or just building summary statistics for a paper, you need to identify your dependent variable clearly. What are its values? Is it continuous or categorical? How is it distributed? How much missing data does it have?

**What are the known gaps, and do they matter?** Missing data is normal. But missing data that is correlated with your outcome, or with a particular subgroup, is a problem that no amount of imputation will fully solve. You want to flag this early.

**Are there columns you should exclude outright?** Some variables are leakage risks (information that would not be available at prediction time), near-duplicates, or simply too sparse to be useful. Better to identify those now than after you have built features from them.

## When AI Enhances EDA

AI is useful for generating visualization code quickly, computing summary statistics across many columns at once, suggesting relevant plots based on data types, and flagging potential outliers or anomalies. It is also good at writing the boilerplate you would otherwise copy from Stack Overflow: the missing value heatmap, the correlation matrix, the histogram grid.

Where AI falls short is interpretation. AI can tell you that 23% of a column is missing. It cannot tell you whether that is a problem for your research question, whether you should impute it, or whether the missingness is systematic in a way that undermines your design. That judgment requires your domain knowledge.

## Recommended First-Pass EDA Workflow

### Step 1: Get a Quick Data Overview

Ask AI to give you the big picture. What are the dimensions? What are the data types? Where are the obvious gaps?

You might prompt an AI like this: "I have a CSV file with patient data. Give me a high-level summary: how many rows and columns, what data types, how many missing values per column, and any obvious data quality issues."

AI can generate code to check basic statistics (count, mean, median, standard deviation, min, max), missing value patterns and percentages, data type information, value ranges and distributions, and duplicate records.

### Step 2: Understand What Each Column Is

Once you have the structural overview, go a level deeper. Review the column names against any available documentation. For columns where you are unsure, ask AI to help you interpret them from context. Make sure you can map every column to either a feature, a target variable, a metadata field, or something to exclude.

This step is easy to skip. Do not skip it.

### Step 3: Create Standard Visualizations

Use AI to quickly generate common plots that show you the shape of your data: distributions (histograms, density plots, box plots), missing value patterns (heatmaps showing which columns have gaps), categorical value counts, and outlier flags.

Do not aim for publication-quality graphics here. Aim for speed and coverage. You want to see everything at least once.

### Step 4: Flag Data Quality Issues

Based on what you see, list the issues that need addressing. Are dates formatted inconsistently? Are there impossible values like negative ages or future dates? Are categories misspelled or inconsistent? Are numbers stored as text? Are some columns mostly empty?

Write these down. This list becomes your cleaning to-do list for the next chapter.

### Step 5: Decide on Your Cleaning Strategy

Before you touch your data, think about what needs to be fixed and why. For each issue, jot down a quick decision: missing values (delete rows, impute, or flag?), inconsistent dates (standardize to one format?), outliers (investigate, cap, or remove?).

You do not need to decide everything perfectly now. You are planning ahead.

## After Cleaning: The Second Pass

Once you have cleaned and prepared your data, you come back for a deeper look. The second-pass EDA is where the real analysis begins. Now you can examine relationships between variables with confidence, build correlation matrices and scatter plots, test whether distributions match your assumptions, and explore subgroup differences.

In the first pass, you are asking "can I trust this data?" In the second pass, you are asking "what does this data tell me?" The separation matters because trying to do both at once usually means doing neither well.

It is also worth noting that EDA is not a one-time event. Plan to revisit your data after each major transformation. If you impute a large block of missing values or re-encode a categorical variable, take another look at the distributions before moving forward. Chapter 12 covers the cleaning and preparation steps, and Chapter 16 addresses validation, but each of those stages benefits from looping back to visualization before you commit to your final dataset.

## Common AI-Assisted EDA Tasks

### Generating an Initial Data Quality Report

AI can create a report showing missing values, duplicates, data types, and basic statistics. You review it and use it to inform your cleaning decisions.

Example prompt: "Generate a Python script that gives me a complete data quality report for my CSV file, including missing values, duplicates, data type mismatches, and summary statistics."

### Creating Distribution Plots

Ask AI to generate plots for each column or for a subset of key variables. Box plots for numeric variables, bar charts for categories, histograms for continuous values.

### Identifying Missing Value Patterns

AI can visualize which columns have missing data and whether missingness is random or concentrated in certain rows or time periods. This matters for deciding how to handle it.

### Spotting Outliers

AI can flag statistical outliers, but you decide whether they are errors or real phenomena that matter to your research.

## Validation Checklist: Before Moving to Data Prep

Before you write down your cleaning strategy:

✅ Have you reviewed a sample of raw data yourself (not just summaries)?
✅ Can you name and describe every column in plain language?
✅ Have you identified which column is your outcome or target variable?
✅ Do the summary statistics match what you expect?
✅ Have you identified all major data quality issues?
✅ Do you understand where missing values are concentrated?
✅ Have you caught any obviously incorrect values?

## Why This Matters

Rushing through initial EDA means you will miss important context. You might clean your data beautifully according to the wrong assumptions. By investing 30 minutes to an hour in this first pass, you will make smarter cleaning decisions. AI makes this fast.

## Key Takeaways

- 🎯 First-pass EDA is about getting your bearings, not deep analysis
- 🎯 Start by understanding what each column means and which is your target variable
- 🎯 AI accelerates summary statistics and visualization generation
- 🎯 Data quality issues you find here guide your cleaning strategy
- 🎯 You will return for a deeper second pass after cleaning
- 🎯 Speed matters here; perfection does not

## Try This

**For your next dataset:**
1. Before generating any plots, write a one-sentence description of each column
2. Ask AI to generate a complete data quality report
3. Spend 10 minutes reviewing the outputs
4. Create a list of 3 to 5 data quality issues that need fixing
5. For each issue, write a one-line plan (what you will do about it)
6. Move to Chapter 12 with your findings in hand

## Resources for Hands-On Learning

Kaggle Learn offers free micro-courses with practical examples that align well with this workflow. The courses on data cleaning and exploratory analysis include guided notebooks you can adapt to your own datasets. {cite}`kaggle_learn`

## Related Chapters

- [Data Access](09_data_access.md) - Getting your data ready
- [Data Preparation](12_data_preparation.md) - Cleaning data based on what you found
- [Validation](16_validation_interpretation.md) - Ensuring your findings are robust

---

**Questions or feedback?** [Open an issue on GitHub](https://github.com/xiaosuhu/midas-ai-in-research/issues)

```{bibliography}
:filter: docname in docnames
```

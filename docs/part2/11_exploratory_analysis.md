# Exploratory Data Analysis with AI

:::{admonition} What You'll Learn
:class: tip
- How to use AI to accelerate your first pass through data
- Generating visualizations and summary statistics to understand what you're working with
- Identifying data quality issues that will guide your cleaning strategy
- The iterative nature of EDA: initial exploration before prep, deep exploration after
:::

## The Two-Pass Journey

You just received your dataset. You haven't touched it yet, but you need to know what you're working with. This chapter covers the initial exploration, your first pass through the data. You'll discover its shape, its gaps, its quirks, and its quality issues. These discoveries will guide your cleaning strategy in the next chapter.

Here's the story: A researcher gets a dataset from a collaborative project. The first thing they do is ask an AI to generate a quick summary. Fifteen minutes later, they know there are 8,000 rows, 42 columns, and about 12% of one critical variable is missing. They also notice that dates are stored in three different formats. These findings are gold. They now know exactly what to fix.

After they clean and prepare the data based on these discoveries, they'll return for a deeper exploration. In that second pass, they can confidently investigate relationships, patterns, and distributions on data they trust.

## When AI Enhances EDA

**AI is particularly useful for:**
- Generating visualization code quickly
- Computing comprehensive summary statistics
- Suggesting relevant plots based on your data type
- Identifying potential outliers and anomalies
- Flagging data quality issues early

**Your expertise is essential for:**
- Interpreting what patterns mean
- Deciding which relationships matter for your research
- Avoiding spurious correlations
- Understanding whether something is a data error or a real phenomenon

## Recommended First-Pass EDA Workflow

### Step 1: Get a Quick Data Overview

Ask AI to give you the big picture. What are the dimensions? What are the data types? Where are the obvious gaps?

You might prompt an AI like this: "I have a CSV file with patient data. Give me a high-level summary: how many rows and columns, what data types, how many missing values, and any obvious data quality issues."

AI can generate code to check:
- Basic statistics (count, mean, median, standard deviation, min, max)
- Missing value patterns and percentages
- Data type information
- Value ranges and distributions
- Duplicate records

### Step 2: Create Standard Visualizations

Use AI to quickly generate common plots that show you the shape of your data:

- Distributions (histograms, density plots, box plots)
- Missing value patterns (heatmaps showing which columns have gaps)
- Data type consistency (categorical value counts)
- Outliers (values that sit far outside the typical range)

Don't aim for publication-quality graphics here. Aim for speed and coverage. You want to see everything at least once.

### Step 3: Flag Data Quality Issues

Based on what you see, list the issues that need addressing:
- Are dates formatted inconsistently?
- Are there impossible values (negative ages, future dates)?
- Are categories misspelled or inconsistent?
- Are numbers stored as text?
- Are some columns mostly empty?

Write these down. This list becomes your cleaning to-do list for the next chapter.

### Step 4: Decide on Your Cleaning Strategy

Before you touch your data, think about what needs to be fixed and why. For each issue, jot down a quick decision:
- Missing values: delete rows, impute, or flag?
- Inconsistent dates: standardize to one format?
- Outliers: investigate, cap, or remove?

You don't need to decide everything perfectly now. You're planning ahead.

## Common AI-Assisted EDA Tasks

### Generating an Initial Data Quality Report

AI can create a report showing missing values, duplicates, data types, and basic statistics. You review it and use it to inform your cleaning decisions.

Example prompt: "Generate a Python script that gives me a complete data quality report for my CSV file, including missing values, duplicates, data type mismatches, and summary statistics."

### Creating Distribution Plots

Ask AI to generate plots for each column or for a subset of key variables. Box plots for numeric variables, bar charts for categories, histograms for continuous values.

### Identifying Missing Value Patterns

AI can visualize which columns have missing data and whether missingness is random or concentrated in certain rows or time periods. This matters for deciding how to handle it.

### Spotting Outliers

AI can flag statistical outliers, but you decide whether they're errors or real phenomena that matter to your research.

## Validation Checklist: Before Moving to Data Prep

Before you write down your cleaning strategy:

✅ Have you reviewed a sample of raw data yourself (not just summaries)?  
✅ Do the summary statistics match what you expect?  
✅ Have you identified all major data quality issues?  
✅ Do you understand where missing values are concentrated?  
✅ Have you caught any obviously incorrect values?  

## Why This Matters

Rushing through initial EDA means you'll miss important context. You might clean your data beautifully according to the wrong assumptions. By investing 30 minutes to an hour in this first pass, you'll make smarter cleaning decisions. AI makes this fast.

## Key Takeaways

- 🎯 First-pass EDA is about getting your bearings, not deep analysis
- 🎯 AI accelerates summary statistics and visualization generation
- 🎯 Data quality issues you find here guide your cleaning strategy
- 🎯 You'll return for deeper exploration after cleaning
- 🎯 Speed matters here; perfection doesn't

## Try This

**For your next dataset:**
1. Ask AI to generate a complete data quality report
2. Spend 10 minutes reviewing the outputs
3. Create a list of 3-5 data quality issues that need fixing
4. For each issue, write a one-line plan (what you'll do about it)
5. Move to Chapter 12 with your findings in hand

## Resources for Hands-On Learning

Kaggle Learn offers free micro-courses with practical examples that align well with this workflow. The courses on data cleaning and exploratory analysis include guided notebooks you can adapt to your own datasets. {cite}`kaggle_learn`

## Related Chapters

- [Data Access](08_data_access.md) - Getting your data ready
- [Data Preparation](12_data_preparation.md) - Cleaning data based on what you found
- [Validation](16_validation_interpretation.md) - Ensuring your findings are robust

---

**Questions or feedback?** [Open an issue on GitHub](https://github.com/xiaosuhu/midas-ai-in-research/issues)

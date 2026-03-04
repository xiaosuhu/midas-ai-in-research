# Data Preparation with AI Assistance

:::{admonition} What You'll Learn
:class: tip
- How to make strategic decisions about data cleaning (not just how to code it)
- A three-way framework: discuss with AI, let AI handle simple tasks, collaborate on complex ones
- How to validate transformations without blindly trusting AI output
- The importance of documenting every cleaning decision
:::

## The Real Work Begins

You've completed your first pass through your data. You found issues: dates in three formats, missing values scattered across two columns, a few outliers that might be errors. Now comes the preparation phase. But here's the key insight: the hardest part isn't the coding. It's deciding *what to do* about each issue and *why*. That's where AI shines as a thinking partner, not just a code generator.

## The Three-Way Framework

Not all data cleaning tasks are created equal. Some require you to think carefully with AI as your guide. Others are straightforward and AI can do them with minimal oversight. A third group sits in the middle, where you and AI collaborate iteratively. Understanding which task falls into which category will save you time and protect your data integrity.

### Way 1: Discuss with AI (The Most Important)

These are decisions where the stakes are high or your domain knowledge is critical. You're not asking AI to code something. You're asking AI to help you reason through options.

**When to use this approach:**
- Deciding how to handle missing data
- Determining whether outliers are errors or real phenomena
- Choosing how to standardize or transform variables
- Deciding whether to merge, split, or create categories

**What a conversation looks like:**

You tell AI about your situation: "I have a clinical dataset with blood pressure readings. About 6% of the systolic BP values are missing. These come from patients who didn't have vital signs recorded at that visit. Should I delete those rows, impute the values, or create a 'missing' indicator?"

AI doesn't just code a solution. It explores the options with you: What are the trade-offs of each approach? How would deletion affect your sample size? What assumptions does imputation make? If you impute, which method is appropriate for your research design?

You then make the decision based on your domain knowledge and your research goals. AI is the thinking partner. You are the decision-maker.

**Examples of Way 1 conversations:**

- "I have categorical variables with lots of misspellings and variations (e.g., 'USA', 'United States', 'US'). How should I standardize these, and should I combine rare categories or keep them separate?"
- "My dataset has extreme outliers in income that are probably real but might be errors. What's a principled way to check if they're real?"
- "I have time series data with gaps. When should I fill gaps forward, when should I drop them, and when should I flag them for investigation?"

### Way 2: Let AI Do It (Simple, Low-Risk Tasks)

These are straightforward technical tasks where the risk of error is low and little judgment is required. You can give AI clear instructions and run the code with confidence.

**When to use this approach:**
- Converting data types (text to numeric, strings to dates)
- Standardizing date formats across a column
- Removing exact duplicate rows
- Splitting or combining columns mechanically
- Creating simple indicators or flags

**What this looks like:**

You give AI a clear instruction: "Write Python code to convert all dates in the 'visit_date' column from 'MM/DD/YYYY' format to 'YYYY-MM-DD' format. Handle any dates that don't match the expected format by flagging them in a new column."

AI generates the code. You review it quickly (make sure it's doing what you asked), run it on a sample, and deploy it.

**Examples of Way 2 tasks:**

- "Convert all values in this column to lowercase for consistency."
- "Remove leading and trailing whitespace from all text fields."
- "Create a new column that extracts the year from the date column."
- "Replace all instances of 'N/A', 'NA', and 'null' with a standard missing value indicator."

### Way 3: Collaborate Iteratively (Complex Tasks)

These tasks are more involved. They require some judgment, or the code needs to be tested and refined as you go. You and AI work together, with you validating each step.

**When to use this approach:**
- Creating derived variables (calculating BMI from height and weight, age from birthdate)
- Implementing domain-specific transformations
- Building a data validation script with multiple checks
- Combining or merging data from multiple sources
- Handling complex missing value patterns

**What this looks like:**

You describe your goal to AI: "I need to calculate BMI from height and weight columns. Height is in inches, weight is in pounds. I want to flag any calculated BMIs that seem implausible (below 10 or above 60), and I want to verify my calculation against a few manual examples."

AI generates code. You review it, check the logic, run it on a sample, and inspect some results. You might ask: "What if height is missing but weight isn't? Should we flag those?" Then AI adjusts the code. You test again. This iterative back-and-forth continues until you're confident the approach is correct.

**Examples of Way 3 tasks:**

- "I need to merge three datasets by patient ID, keeping only patients who appear in all three files. Create a script that does this and reports how many records are retained."
- "Create a script that checks for impossible value combinations (e.g., a person's discharge date before their admission date) and flags any inconsistencies."
- "I need to aggregate daily measurements into weekly summaries. How should missing days be handled, and what should my summary statistics include?"

## A Decision Flowchart

Unsure which approach to use? Ask yourself:

1. **Is this a strategic decision about your data?** (Way 1: Discuss)
2. **Is this a simple, mechanical task with no domain judgment?** (Way 2: Let AI do it)
3. **Is this more complex and requires testing as I go?** (Way 3: Collaborate)

## Recommended Data Prep Workflow

### Step 1: Start with Your First-Pass EDA Findings

Pull out the list you made in Chapter 11. What issues need fixing? In what order?

### Step 2: For Each Issue, Choose Your Approach

Go through your list one by one. For each issue, ask: Which of the three ways applies here?

- Missing values in a key variable? Way 1 (discuss your strategy).
- Dates in inconsistent formats? Way 2 (let AI standardize them).
- Complex transformation based on clinical logic? Way 3 (collaborate).

### Step 3: Execute and Validate

For Way 1, take time to think and decide.
For Way 2, review the code, test on a sample, deploy.
For Way 3, iterate with AI until you're confident, then test on the full dataset.

### Step 4: Document Every Decision

Before moving on, write down what you did and why. This becomes part of your data documentation and is essential for reproducibility.

## Validation is Non-Negotiable

Regardless of which approach you use, validation is critical.

**Essential validation steps:**
- Compare data distributions before and after cleaning. Did something unexpected change?
- Manually inspect a sample of transformed records. Does the output match your intention?
- Check for introduced biases. Did your cleaning process systematically exclude or alter certain groups?
- Verify that transformations are reproducible. Can you run the same code again and get identical results?
- Ensure no data leakage between train and test sets (relevant when preparing data for modeling).

## Validation Checklist

Before considering your data "clean":

✅ Have you reviewed the code (whether AI-generated or not)?  
✅ Have you tested on a sample before applying to the full dataset?  
✅ Do the before-and-after distributions make sense?  
✅ Have you manually spot-checked transformed records?  
✅ Have you documented the reason for every transformation?  
✅ Can you reproduce these transformations exactly?  

## Common Pitfalls

**Pitfall 1: Trusting AI without understanding the logic**

AI can generate code that looks right but makes wrong assumptions. Always understand the approach before running it on your full dataset.

**Pitfall 2: Over-cleaning**

Sometimes it's tempting to remove every unusual record or fill every gap. Resist this. Data is messy for a reason. Clean strategically, not obsessively.

**Pitfall 3: Forgetting to document**

Six months from now, you'll forget why you made certain decisions. Document them now.

**Pitfall 4: Not validating on a sample first**

Always test on a small subset before running code on your full dataset. This catches mistakes before they propagate.

## Key Takeaways

- 🎯 Use AI as a thinking partner (Way 1) for strategic decisions, not just a code generator
- 🎯 Leverage AI's speed on simple tasks (Way 2) where judgment isn't needed
- 🎯 Collaborate iteratively (Way 3) on complex transformations
- 🎯 Always validate before trusting the output
- 🎯 Document everything for reproducibility and integrity

## Try This

**For your next cleaning project:**
1. List the data quality issues you found in first-pass EDA
2. For each issue, decide: Way 1, Way 2, or Way 3?
3. Execute each approach using the framework above
4. Validate your results
5. Write a one-paragraph summary of what you cleaned and why

## Resources for Hands-On Learning

Kaggle Learn offers micro-courses on data cleaning with practical examples. The courses include guided notebooks where you can see the three-way framework in action: thinking through a strategy, executing simple transformations, and iteratively building complex validation scripts. {cite}`kaggle_learn`

## Related Chapters

- [Exploratory Data Analysis](11_exploratory_analysis.md) - Understanding your data before cleaning
- [Feature Engineering](13_feature_engineering.md) - Creating new variables from cleaned data
- [Validation](16_validation_interpretation.md) - Ensuring your results are robust

---

**Questions or feedback?** [Open an issue on GitHub](https://github.com/xiaosuhu/midas-ai-in-research/issues)

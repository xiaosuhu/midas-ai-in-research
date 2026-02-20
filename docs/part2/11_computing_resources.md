# Computing Resources for AI-Assisted Data Analysis

:::{admonition} What You'll Learn
:class: tip
- University of Michigan computing resources for AI research
- When to use local vs. cloud vs. HPC resources
- Setting up environments for AI tools
:::

## The Challenge

AI-assisted data analysis often requires more computational power than standard research workflows. Understanding available resources and choosing the right environment ensures efficient, reproducible work.

## UM Computing Resources Overview

### MIDAS AI Sandbox
**Best for:** Learning, prototyping, small-scale analyses  
**Specs:** Pre-configured AI environment with common tools  
**Access:** [Contact MIDAS](#)

### Great Lakes HPC Cluster
**Best for:** Large-scale data processing, computationally intensive models  
**Specs:** High-performance computing with GPU nodes available  
**Access:** [ARC-TS](https://arc.umich.edu/greatlakes/)

### UM-GPT and Google Gemini
**Best for:** Interactive AI assistance, code generation, text tasks  
**Specs:** University-licensed access with data privacy protections  
**Access:** Through your UM account

## Choosing the Right Resource

**Use your local machine when:**
- Dataset fits in memory (<8GB typically)
- Quick prototyping and exploration
- Interactive development with immediate feedback

**Use MIDAS AI Sandbox when:**
- Learning new AI tools
- Need pre-configured environments
- Collaborative development

**Use Great Lakes HPC when:**
- Large datasets (>50GB)
- Training machine learning models
- Parallel processing needs
- GPU-intensive computations

**Use UM-GPT/Gemini when:**
- Writing and documenting code
- Exploring analysis approaches
- Getting quick answers about methods

## Setting Up Your Environment

### Local Setup (Python)

```bash
# Create isolated environment
python -m venv ai_research_env
source ai_research_env/bin/activate  # On Windows: ai_research_env\Scripts\activate

# Install common AI tools
pip install pandas numpy scikit-learn jupyter
pip install openai anthropic  # For AI APIs
```

### Great Lakes Setup

```bash
# Connect to Great Lakes
ssh uniquename@greatlakes.arc-ts.umich.edu

# Load modules
module load python3.11
module load cuda  # If using GPUs

# Create environment
python -m venv ~/ai_env
source ~/ai_env/bin/activate
```

## Data Privacy Considerations

**Reminder:** Different resources have different data restrictions:

- ✅ **UM-GPT**: Can handle U-M data, HIPAA data NOT allowed
- ✅ **MIDAS Sandbox**: Suitable for research data, check with MIDAS for restrictions
- ✅ **Great Lakes**: Suitable for most research data, follow ARC-TS guidelines
- ❌ **Public AI services**: NO protected health information, no sensitive data

## Cost Considerations

| Resource | Cost | Best For |
|----------|------|----------|
| Local | Free (your hardware) | Small-scale work |
| UM-GPT | Free (UM subscription) | Interactive AI assistance |
| MIDAS Sandbox | Free for UM researchers | Learning & prototyping |
| Great Lakes | Free allocation + paid | Large-scale computation |

## Key Takeaways

- 🎯 Start small locally, scale up to HPC when needed
- 🎯 Match your computational needs to the right resource
- 🎯 Always consider data privacy when choosing platforms
- 🎯 Document your environment for reproducibility

## Try This

**For your current project:**
1. Estimate your data size and computational needs
2. Choose the appropriate resource from the list above
3. Set up a reproducible environment (save requirements.txt or environment.yml)
4. Test on a sample before running full analysis

## Related Chapters

- [Data Preparation](09_data_preparation.md) - Getting data ready for analysis
- [UM Resources](../part3/16_um_resources.md) - Detailed UM resource guide
- [Exploratory Analysis](11_exploratory_analysis.md) - Interactive data exploration

---

**Questions or feedback?** [Open an issue on GitHub](https://github.com/xiaosuhu/midas-ai-in-research/issues)

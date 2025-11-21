# MIDAS AI in Research Tutorial

[![Documentation Status](https://readthedocs.org/projects/midas-ai-tutorial/badge/?version=latest)](https://midas-ai-tutorial.readthedocs.io/)

A living tutorial on applying artificial intelligence in academic research, maintained by the Michigan Institute for Data Science (MIDAS) at the University of Michigan.

## About This Tutorial

This handbook began with a simple curiosity — how do our questions as researchers evolve in the era of artificial intelligence? Each advance in AI reshapes not only *how* we analyze data or write code, but *what* we ask, *why* we ask it, and *how* we validate answers.

Through this living tutorial, we aim to gather and organize the essential **questions and answers** that researchers across disciplines face when integrating AI into their work — from literature review and grant writing, to ethical practice, reproducibility, and responsible deployment.

Rather than a static guide, this is an evolving space to **collect insights, examples, and reflections** about using AI as a true collaborator in research.

## Citation System

We use a hybrid citation approach to balance academic rigor with practical usability:

### For Academic Papers
Use **BibTeX references** in `references.bib`:

```bibtex
@article{vaswani2017attention,
  title={Attention is all you need},
  author={Vaswani, Ashish and Shazeer, Noam and Parmar, Niki and others},
  journal={Advances in neural information processing systems},
  volume={30},
  year={2017}
}
```

### In content:

markdown
The transformer architecture [@vaswani2017attention] revolutionized NLP...
For Websites & Online Reports
Use direct links:

markdown
- [State of AI Report (2024)](https://www.stateof.ai/)
- [Stanford HAI AI Index Report (2025)](https://hai.stanford.edu/ai-index/2025-ai-index-report)

## How to Contribute
We welcome contributions from the research community!

Reporting Issues
Found a typo or error? Open an issue

Spot outdated information? Let us know

Have suggestions for new content? We'd love to hear

Content Contributions
Fork the repository (if public) or request collaborator access

Create a new branch for your changes

Follow our citation guidelines above

Submit a pull request with a clear description

Content Areas We're Looking For
Discipline-specific AI use cases

Ethical considerations in your field

Reproducibility best practices

Grant writing examples with AI

Data analysis workflows

Style Guidelines
Use clear, accessible language for interdisciplinary audiences

Include practical examples when possible

Balance technical depth with approachability

Follow the existing citation format (hybrid system)

Local Development
To build the documentation locally:

bash
# Install dependencies
pip install sphinx sphinx-rtd-theme myst-parser

# Build the documentation
make html

# Serve locally
cd _build/html && python -m http.server 8000
License
This tutorial is available under Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International.

Acknowledgments
This tutorial is maintained by the Michigan Institute for Data Science (MIDAS) at the University of Michigan.

Contact
For questions or suggestions about this tutorial:

Open an issue in this repository

Contact MIDAS at midas-contact@umich.edu

This is a living document — we welcome your insights and experiences to help this resource grow and evolve with the AI research landscape.
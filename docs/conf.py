# conf.py
import os

# Use Read the Docs output directory if available
if os.environ.get('READTHEDOCS') == 'True':
    html_dir = os.path.join(os.environ.get('READTHEDOCS_OUTPUT', ''), 'html')
else:
    html_dir = '_build/html'
    
# -- Project info -----------------------------------------------------
project = 'MIDAS AI in Research'
copyright = '2025, Michigan Institute for Data and AI in Society'
author = 'MIDAS Research Team'
version = '0.1'
release = '0.1'

# -- General config ---------------------------------------------------
extensions = [
    "myst_parser",
    "sphinxcontrib.bibtex",  # Bibliography support
]

# BibTeX configuration
bibtex_bibfiles = ['references.bib']
bibtex_default_style = 'unsrt'
bibtex_reference_style = 'label'  # or 'super'

myst_enable_extensions = [
    "colon_fence", "deflist", "substitution", "tasklist"
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output ------------------------------------------
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
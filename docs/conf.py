# conf.py
import os

# -- Read the Docs specific configuration ---
if os.environ.get('READTHEDOCS') == 'True':
    # This forces Sphinx to use the correct output directory
    html_context = {
        'output_path': os.path.join(os.environ.get('READTHEDOCS_OUTPUT', ''), 'html')
    }
    
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
    "sphinx_revealjs",
]

# BibTeX configuration
bibtex_bibfiles = ['references.bib']
bibtex_default_style = 'unsrt'
bibtex_reference_style = 'label'

myst_enable_extensions = [
    "colon_fence", "deflist", "substitution", "tasklist"
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output ------------------------------------------
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
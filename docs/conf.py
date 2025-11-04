# -- Project info -----------------------------------------------------
project = 'MIDAS AI in Research'
copyright = '2025, Frank Hu'
author = 'Frank Hu'
release = '0.1'

# -- General config ---------------------------------------------------
extensions = [
    "myst_parser",               # Markdown support (MyST)
    # "myst_nb",                 # <- use this instead of myst_parser if you want notebooks
    # "sphinxcontrib.bibtex",    # <- enable if you'll cite references
]

myst_enable_extensions = [
    "colon_fence", "deflist", "substitution", "tasklist"
]

templates_path = ["_templates"]
exclude_patterns = ["_build"]

# -- Options for HTML output ------------------------------------------
html_theme = "sphinx_rtd_theme"   # clean “book-like” theme (like Andy’s)
html_static_path = ["_static"]

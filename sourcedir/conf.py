# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os

# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "PyData Osaka"
copyright = "2021, PyData Osaka Community"
author = "PyData Osaka Community"

import pydata_sphinx_theme


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinxext.rediraffe",
    "sphinx.ext.viewcode",
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

# -- Internationalization ------------------------------------------------
# specifying the natural language populates some key tags
language = "ja"

# ReadTheDocs has its own way of generating sitemaps, etc.
if not os.environ.get("READTHEDOCS"):
    extensions += ["sphinx_sitemap"]

    # -- Sitemap -------------------------------------------------------------
    html_baseurl = os.environ.get("SITEMAP_URL_BASE", "http://127.0.0.1:8000/")
    sitemap_locales = [None]
    sitemap_url_scheme = "{link}"

autosummary_generate = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]

# -- Extension options -------------------------------------------------------

myst_enable_extensions = [
    # This allows us to use ::: to denote directives, useful for admonitions
    "colon_fence",
]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"
# html_logo = "_static/pandas.svg"  # For testing

html_theme_options = {
    "github_url": "https://github.com/pydataosaka",
    "twitter_url": "https://twitter.com/pydataosaka",
    "use_edit_page_button": True,
    "show_toc_level": 1,
    # "show_nav_level": 2,
    # "search_bar_position": "navbar",  # TODO: Deprecated - remove in future version
    # "navbar_align": "left",  # [left, content, right] For testing that the navbar items align properly
    # "navbar_start": ["navbar-logo", "navbar-version"],
    # "navbar_center": ["navbar-nav", "navbar-version"],  # Just for testing
    # "navbar_end": ["theme-switcher", "version-switcher", "navbar-icon-links"],
    # "left_sidebar_end": ["custom-template.html", "sidebar-ethical-ads.html"],
    # "footer_items": ["copyright", "sphinx-version", ""]
#     "switcher": {
#         "json_url": json_url,
#         "version_match": version_match,
#     },
}

html_sidebars = {
    "contribute/index": [
        "search-field",
        "sidebar-nav-bs",
        "custom-template",
    ],  # This ensures we test for custom sidebars
    "demo/no-sidebar": [],  # Test what page looks like with no sidebar items
}

myst_heading_anchors = 2

html_context = {
    "github_user": "pydataosaka",
    "github_repo": "pydataosaka.github.io",
    "github_version": "main",
    "doc_path": "docs",
}

# rediraffe_redirects = {
#     "contributing.rst": "contribute/index.rst",
# }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]


def setup(app):
    app.add_css_file("custom.css")

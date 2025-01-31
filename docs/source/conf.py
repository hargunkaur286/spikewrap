# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

import setuptools_scm

# Used when building API docs, put the dependencies
# of any class you are documenting here
autodoc_mock_imports = []

# Add the module path to sys.path here.
# If the directory is relative to the documentation root,
# use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath("../.."))

project = "spikewrap"
copyright = "2025, University College London"
author = "Joe Ziminski"

try:
    release = setuptools_scm.get_version(root="../..", relative_to=__file__)
    release = release.split("+")[0]  # remove git hash
except LookupError:
    # if git is not initialised, still allow local build
    # with a dummy version
    release = "0.0.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx.ext.githubpages",
    "sphinx_autodoc_typehints",
    "sphinx.ext.autosummary",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "myst_parser",
    "nbsphinx",
    "notfound.extension",
    "sphinx_design",
    "sphinx_gallery.gen_gallery",
    "sphinx_sitemap",
    "sphinx.ext.autosectionlabel",
]

# Configure the myst parser to enable cool markdown features
# See https://sphinx-design.readthedocs.io
myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
    "attrs_block",  # https://stackoverflow.com/questions/78183173/custom-styling-a-header-in-sphinx-website?noredirect=1#comment137843002_78183173
    "attrs_inline"
]
# Automatically add anchors to markdown headings
myst_heading_anchors = 4

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# Automatically generate stub pages for API
autosummary_generate = True
# autodoc_default_flags = ["members", "inherited-members"]
autodoc_member_order = 'bysource'

autodoc_default_options = {
    'members': True,             # Include all members (functions, methods, etc.)
    'undoc-members': False,      # Skip undocumented members
    'show-inheritance': True,    # Show class inheritance
}

# Prefix section labels with the document name
autosectionlabel_prefix_document = True

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    "**.ipynb_checkpoints",
    # to ensure that include files (partial pages) aren't built, exclude them
    # https://github.com/sphinx-doc/sphinx/issues/1965#issuecomment-124732907
    "**/includes/**",
    # exclude .py and .ipynb files in examples generated by sphinx-gallery
    # this is to prevent sphinx from complaining about duplicate source files
    "**/README.rst",
    "gallery_builds/tutorials/*.ipynb", "gallery_builds/get_started/*.ipynb", "gallery_builds/how_to/*.ipynb"  # TODO: rename if not using custom
]

import sphinx_gallery.sorting


# Configure Sphinx gallery
sphinx_gallery_conf = {
    "examples_dirs": ["galleries/tutorials", "galleries/get_started", "galleries/how_to"],
    "filename_pattern": "/*.py",  # which files to execute before inclusion
    "gallery_dirs": ["gallery_builds/tutorials", "gallery_builds/get_started", "gallery_builds/how_to"],  # output directory
    "run_stale_examples": True,  # re-run examples on each build
    # Integration with Binder, see https://sphinx-gallery.github.io/stable/configuration.html#generate-binder-links-for-gallery-notebooks-experimental
    "binder": {
        "org": "neuroinformatics-unit",
        "repo": "spikewrap",
        "branch": "gh-pages",
        "binderhub_url": "https://mybinder.org",
        "dependencies": ["environment.yml"],  ## TODO!!!!!!!!!!!!!!
    },
    "reference_url": {"spikewrap": None},
    "thumbnail_size": (1500, 1500),  # width, height in pixels
    'within_subsection_order': "FileNameSortKey",
    #  "default_thumb_file": "",  # default thumbnail image
 #   "remove_config_comments": True,
    # do not render config params set as # sphinx_gallery_config [= value]
}


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = "pydata_sphinx_theme"
html_title = "spikewrap"
html_show_sourcelink = False

# Customize the theme
html_theme_options = {
    "icon_links": [
        {
            # Label for this link
            "name": "GitHub",
            # URL where the link will redirect
            "url": "https://github.com/neuroinformatics-unit/spikewrap",
            # Icon class (if "type": "fontawesome"),
            # or path to local image (if "type": "local")
            "icon": "fa-brands fa-github",
            # The type of image to be used (see below for details)
            "type": "fontawesome",
        },
        {
            "name": "Zulip (chat)",
            "url": "https://neuroinformatics.zulipchat.com/#narrow/stream/406002-Spikewrap",
            "icon": "fa-solid fa-comments",
            "type": "fontawesome",
        },
    ],
    "logo": {
        "text": f"{project} v{release}",
    },
    "footer_start": ["footer_start"],
    "footer_end": ["footer_end"],
    "external_links": [],
    "show_toc_level": 2,  # sidebar levels that are expanded before scrolling, needed for API docs
}

# Redirect the webpage to another URL
# Sphinx will create the appropriate CNAME file in the build directory
# The default is the URL of the GitHub pages
# https://www.sphinx-doc.org/en/master/usage/extensions/githubpages.html
github_user = "neuroinformatics-unit"
html_baseurl = "https://spikewrap.neuroinformatics.dev"
sitemap_url_scheme = "{link}"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_css_files = [
    'css/custom.css',
]
html_favicon = "_static/light-logo-niu.png"

# The linkcheck builder will skip verifying that anchors exist when checking
# these URLs
linkcheck_anchors_ignore_for_url = [
    "https://neuroinformatics.zulipchat.com"
]
# A list of regular expressions that match URIs that should not be checked
linkcheck_ignore = [
]

intersphinx_mapping = {
    "scipy": ("https://docs.scipy.org/doc/scipy/", None),
    "pandas": ("https://pandas.pydata.org/pandas-docs/stable/", None),
}


# What to show on the 404 page
notfound_context = {
    "title": "Page Not Found",
    "body": """
<h1>Page Not Found</h1>

<p>Sorry, we couldn't find that page.</p>

<p>We occasionally restructure the spikewrap website, and some links may have broken.</p> 

<p>Try using the search box or go to the homepage.</p>
""",
}

# needed for GH pages (vs readthedocs),
# because we have no '/<language>/<version>/' in the URL
notfound_urls_prefix = None

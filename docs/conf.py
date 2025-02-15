# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import re
import sys

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('..'))
sys.path.append(os.path.abspath('extensions'))

project = 'pyvolt'
copyright = '2024, MCausc78'
author = 'MCausc78'


version = ''
with open('../pyvolt/__init__.py', 'r') as fp:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fp.read(), re.MULTILINE).group(1)  # type: ignore

# The full version, including alpha/beta/rc tags.
release = version

# This assumes a tag is available for final releases
branch = 'master' if version.endswith('a') else 'v' + version

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.extlinks',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinxcontrib_trio',
    'sphinx_inline_tabs',
    'exception_hierarchy',
    'attributetable',
    'resourcelinks',

]

autodoc_member_order = 'bysource'
autodoc_typehints = 'none'
# autodoc_typehints = 'description'
# autodoc_typehints_description_target = 'documented'


# maybe consider this?
# napoleon_attr_annotations = False

# Make tables in Raises section actually work
napoleon_custom_sections = [('Raises', 'returns_style')]

extlinks = {
    'issue': ('https://github.com/MCausc78/pyvolt/issues/%s', 'GH-%s'),
}

# Links used for cross-referencing stuff in other documentation
intersphinx_mapping = {
    'py': ('https://docs.python.org/3', None),
    'aio': ('https://docs.aiohttp.org/en/stable/', None),
    'req': ('https://requests.readthedocs.io/en/latest/', None),
    # unfortunately livekit does not use Sphinx, and therefore does not have objects.inv, so this will fail
    # 'livekit': ('https://docs.livekit.io/python/livekit/rtc/', None),
}

rst_prolog = """
.. |coro| replace:: This function is a |coroutine_link|_.
.. |maybecoro| replace:: This function *could be a* |coroutine_link|_.
.. |coroutine_link| replace:: *coroutine*
.. _coroutine_link: https://docs.python.org/3/library/asyncio-task.html#coroutine
"""

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = 'furo'
html_static_path = ['_static']


html_context = {
    'revolt_invite': 'https://rvlt.gg/ZZQb4sxx',
    'pyvolt_extensions': [
        ('pyvolt.ext.commands', 'ext/commands'),
    ],
}

resource_links = {
    'revolt': 'https://rvlt.gg/ZZQb4sxx',
    'issues': 'https://github.com/MCausc78/pyvolt/issues',
    'discussions': 'https://github.com/MCausc78/pyvolt/discussions',
    'examples': f'https://github.com/MCausc78/pyvolt/tree/{branch}/examples',
}

def setup(app):
    app.add_css_file('style.css')
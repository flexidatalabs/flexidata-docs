# Configuration file for the Sphinx documentation builder.
from docutils import nodes

# -- Project information

project = 'flexidata'
copyright = '2024, flexidatalabs'
author = 'flexidatalabs'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

def setup(app):
    app.add_role('red', colorize('red', 'span'))

def colorize(color_name, element_name):
    def callback(name, rawtext, text, lineno, inliner, options={}, content=[]):
        open_tag = '<{element} style="color: {color};">'.format(element=element_name, color=color_name)
        close_tag = '</{element}>'.format(element=element_name)
        return [nodes.raw('', open_tag + text + close_tag, format='html')], []
    return callback
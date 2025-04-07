# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
sys.path.insert(0, os.path.abspath('../..')) # Pfad zum Projekt-Root anpassen!

import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'join_backend.settings')
django.setup()

project = 'join_backend'
copyright = '2025, Philipp Lötzsch'
author = 'Philipp Lötzsch'
release = '2025'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',      # Haupt-Erweiterung zum Lesen von Docstrings
    'sphinx.ext.napoleon',     # Versteht Google & NumPy Style Docstrings
    'sphinx.ext.intersphinx',  # Für Links zu anderer Doku (Python, Django)
    'sphinx.ext.viewcode',     # Fügt Links zum Quellcode hinzu
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import sys
import os

project = 'django-project'
copyright = '2025, Klimova'
author = 'Klimova'
release = '1.0'

sys.path.insert(0, os.path.abspath('../dash'))
sys.path.insert(0, os.path.abspath('../djangotutorial'))
sys.path.insert(0, os.path.abspath('../pw'))

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',  # Автоматическая документация из docstring
    'sphinx.ext.viewcode',  # Добавляет ссылки на исходный код
    'sphinx.ext.napoleon',  # Поддержка Google- и NumPy-style docstrings
]

templates_path = ['_templates']
exclude_patterns = []

language = 'ru'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

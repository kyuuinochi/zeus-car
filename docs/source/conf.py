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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------
import sphinx_rtd_theme

project = 'SunFounder Robot HAT'
copyright = '2021, SunFounder'
author = 'www.sunfounder.com'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autosectionlabel', 
    'breathe',
]

breathe_projects_source = {
    "auto" : ( "../../Zeus_Car/", 
        [
         "Zeus_Car.h",    
         "Zeus_Car.ino",    
         "ai_camera.cpp",    
         "ai_camera.h",    
         "car_control.cpp",    
         "car_control.h",    
         "cmd_code_config.hpp",    
         "compass.cpp",    
         "compass.h",    
         "grayscale.cpp",    
         "grayscale.h",    
         "hc165.cpp",    
         "hc165.h",    
         "ir_obstacle.cpp",    
         "ir_obstacle.h",    
         "ir_remote.cpp",    
         "ir_remote.h",    
         "qmc6310.cpp",    
         "qmc6310.h",    
         "rgb.cpp",    
         "rgb.h",    
         "test.h",    
         "ultrasonic.cpp",    
         "ultrasonic.h",    
        ]
    ),
}


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]


# SunFounder logo

html_js_files = [
    'https://ezblock.cc/readDocFile/custom.js',
]
html_css_files = [
    'https://ezblock.cc/readDocFile/custom.css',
]

#### RTD+

# html_js_files = [
#     'https://ezblock.cc/readDocFile/readTheDoc/src/js/ace.js',
#     'https://ezblock.cc/readDocFile/readTheDoc/src/js/ext-language_tools.js',
#     'https://ezblock.cc/readDocFile/readTheDoc/src/js/theme-chrome.js',
#     'https://ezblock.cc/readDocFile/readTheDoc/src/js/mode-python.js',
#     'https://ezblock.cc/readDocFile/readTheDoc/src/js/mode-sh.js',
#     'https://ezblock.cc/readDocFile/readTheDoc/src/js/monokai.js',
#     'https://ezblock.cc/readDocFile/readTheDoc/src/js/xterm.js',
#     'https://ezblock.cc/readDocFile/readTheDoc/src/js/FitAddon.js',
#     'https://ezblock.cc/readDocFile/readTheDoc/src/js/readTheDocIndex.js',

# ]
# html_css_files = [
#     'https://ezblock.cc/readDocFile/readTheDoc/src/css/index.css',
#     'https://ezblock.cc/readDocFile/readTheDoc/src/css/xterm.css',
# ]



# Multi-language

language = 'en' # Before running make html, set the language.
locale_dirs = ['locale/'] # .po files for other languages are placed in the locale/ folder.

gettext_compact = False # Support for generating the contents of the folders inside source/ into other languages.
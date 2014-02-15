import sys
import os
import sphinxtrap 

extensions = ["sphinxtrap.ext.rawtoc"]
html_theme = 'sphinxtrap'
html_theme_path = [sphinxtrap.get_theme_dir()]
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'testprj'
copyright = u'2014, foo'
version = '0.1'
release = '0.1'
exclude_patterns = []
pygments_style = 'sphinx'
html_static_path = ['_static']
htmlhelp_basename = 'testprjdoc'

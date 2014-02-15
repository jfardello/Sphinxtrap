import os

__version__ = "0.2"
__release__ = "{0}.{1}".format(__version__, "1") 

_root_dir = os.path.abspath(os.path.dirname(__file__))

def get_theme_dir():
    return os.path.join(_root_dir, "themes")

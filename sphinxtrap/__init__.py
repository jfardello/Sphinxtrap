import os

__version__ = "0.1"
__release__ = __version__ + "a" 

_root_dir = os.path.abspath(os.path.dirname(__file__))

def get_theme_dir():
    return os.path.join(_root_dir, "themes")

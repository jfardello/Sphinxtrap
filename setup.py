#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,os
from os.path import abspath, join
root_path = abspath(join(__file__, ".."))
os.chdir(root_path)
lib_path = '.'

from setuptools import setup, find_packages

from sphinxtrap import __release__ as VERSION

setup(
    packages = find_packages(),
    package_data = { "sphinxtrap": ["themes/*/*.*", "themes/*/static/*.*",
        "themes/*/static/img/*"]},
    zip_safe=False,
    install_requires=[ "sphinx>=1.1"],
    name = "sphinxtrap",
    version = VERSION,
    author = "José Manuel Fardello",
    author_email = "jmfardello@gmail.com",
    description = "Yet another bootstrap sphinx theme.",
    long_description="""\
Small package containing a Sphinx theme named "sphinxtrap",
You can see an example at `<//http://jfardello.github.com/Dardrive/>`_.
    """,
    license = "MIT",
    keywords = "sphinx extension theme",
    url = "https://github.com/jfardello/Sphinxtrap",
    download_url = "http://pypi.python.org/pypi/sphinxtrap",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ]
)

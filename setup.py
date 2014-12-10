#!/usr/bin/env python
# encoding: utf-8

import os
import re
import glob
from setuptools import setup, find_packages


def rel_path(path):
    return os.path.join(os.path.dirname(__file__), path)


def get_version():
    with open(rel_path(os.path.join("astrorec", "__init__.py"))) as f:
        for line in f:
            if line.startswith("VERSION"):
                version = re.findall(r'\"(.+?)\"', line)[0]
                return version
    return "0.0.0.dev"


try:
    long_description = open(rel_path('README.rst'), 'rt').read()
except IOError:
    long_description = ''

setup(
    name='astrorec',
    version=get_version(),
    author="Adam Becker, Matthew Sofftie, Jonathan Sick, Bekkie Smethurst, "
           "Chris Lintott and .Astronomy",
    # author_email='jonathansick@mac.com',
    license='MIT',
    description='Recommendations for citations by analyzing paper sources',
    long_description=long_description,
    packages=find_packages(),
    scripts=glob.glob(os.path.join('scripts', '*.py')),
    # install_requires=['pytest', 'ads', 'bibtexparser'],
    url='https://github.com/jonathansick/astrorec',
    classifiers=['Development Status :: 3 - Alpha',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Environment :: Console'],
)

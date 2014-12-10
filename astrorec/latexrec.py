#!/usr/bin/env python
# encoding: utf-8
"""
Recommender based on a LaTeX file.
"""


class LaTeXRecommender(object):
    """Recommend papers to be cited in your LaTeX file."""
    def __init__(self, tex_filepath):
        super(LaTeXRecommender, self).__init__()
        self._filepath = tex_filepath

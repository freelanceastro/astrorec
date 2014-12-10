#!/usr/bin/env python
# encoding: utf-8
"""
Paper recommendations for an article on the arXiv (that we can grab via
out database dump).
"""


class ArXivRecommender(object):
    """Docstring for ArXivRecommender. """
    def __init__(self, arxiv_id):
        super(ArXivRecommender, self).__init__()
        self._arxiv_id = arxiv_id

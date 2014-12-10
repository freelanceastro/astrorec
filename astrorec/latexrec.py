#!/usr/bin/env python
# encoding: utf-8
"""
Recommender based on a LaTeX file.
"""

from paperweight.document import FilesystemTexDocument


class LaTeXRecommender(object):
    """Recommend papers to be cited in your LaTeX file."""
    def __init__(self, tex_filepath):
        super(LaTeXRecommender, self).__init__()
        self._filepath = tex_filepath
        self._doc = FilesystemTexDocument(tex_filepath)
        self._doc.inline_inputs()
        self._doc.remove_comments()
        rich_cites = self._doc.rich_bib_keys
        print rich_cites
        print type(rich_cites)
        # self._doc.bibtex_path  # we're using bibtex, right?

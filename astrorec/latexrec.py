#!/usr/bin/env python
# encoding: utf-8
"""
Recommender based on a LaTeX file.
"""

from paperweight.document import FilesystemTexDocument

from starlit.bib.bibtexdb import BibTexDB

from .mentionsrec import MentionsRecs


class LaTeXRecommender(object):
    """Recommend papers to be cited in your LaTeX file."""
    def __init__(self, tex_filepath, ads_cache=None):
        super(LaTeXRecommender, self).__init__()
        self._filepath = tex_filepath
        self._ads_cache = ads_cache
        self._doc = FilesystemTexDocument(tex_filepath)
        self._doc.inline_inputs()
        self._doc.remove_comments()
        rich_cites = self._doc.rich_bib_keys
        bib_path = self._doc.bib_path  # we're using bibtex, right?
        assert bib_path is not None, "You need to use BibTeX"
        # FIXME could also parse those bibitems
        bibdb = BibTexDB(bib_path, ads_cache=ads_cache)

        mention_recs = MentionsRecs(self._ads_cache)
        # Initialize with the set of ADS bibcodes we've already cited
        for bib_key in rich_cites:
            try:
                ref_pub = bibdb[bib_key]
            except:
                continue

            try:
                arxiv_id = ref_pub.arxiv_id
            except:
                continue
            if arxiv_id is None:
                continue

            n_mentions = len(rich_cites)
            mention_recs.append(ref_pub, n_mentions)

        mention_recs.analyze_secondary()
        # TODO get top *N* recommendations by score

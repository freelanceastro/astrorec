#!/usr/bin/env python
# encoding: utf-8
"""


2014-12-10 - Created by Jonathan Sick
"""

import numpy as np

from starlit.bib.adsdb import ADSBibDB


class MentionsRecs(object):
    """Citation recommendations based on mention frequency analysis."""
    def __init__(self, ads_cache):
        super(MentionsRecs, self).__init__()
        self._adsdb = ADSBibDB(cache=ads_cache)
        # List of B-level publications
        self._cited_pubs = []
        self._cited_bibcodes = []
        self._cited_mention_counts = []

    def add_cited_pub(self, pub, n_mentions):
        self._cited_pubs.append(pub)
        self._cited_bibcodes.append(pub.bibcode)
        self._cited_mention_counts.append(n_mentions)

    def analyze_secondary(self):
        """Build a secondary set of references to recommend from."""
        # First build the unique set of secondary-level publications.
        # that are not in the B-level (directly cited)
        secondary_bibcodes = []
        for cited_pub in self._cited_pubs:
            secondary_bibcodes += cited_pub.reference_bibcodes
        secondary_bibcodes = list(set(secondary_bibcodes)
                                  - set(self._cited_bibcodes))

        self._secondary_pubs = []
        cited_mentions = np.array(self._cited_mention_counts)
        for bibcode in secondary_bibcodes:
            spub = SecondaryPub(bibcode, self._adsdb, self._cited_bibcodes,
                                cited_mentions)
            self._secondary_pubs.append(spub)

        self._secondary_scores = []
        for spub in self._secondary_pubs:
            self._secondary_scores.append(spub.score)

        # TODO way to return top *n* publications


class SecondaryPub(object):
    """A publication at the seconary level that will be scored for relevance
    to the original paper via mentions to the tertiary papers
    """
    def __init__(self, bibcode, adsdb, cited_bibcodes, cited_mentions):
        super(SecondaryPub, self).__init__()
        self._bibcode = bibcode
        self._adsdb = adsdb
        self._cited_bibcodes = cited_bibcodes

        # Mentions vector for primary references
        self._cited_mentions = cited_mentions

        # Mentions vector for tertiary reference
        self._tertiary_mentions = np.zeros(self._cited_mentions.shape)

        # TODO read and build the rich citations for this publication

        # query ADS for this paper
        pub = adsdb[bibcode]

        # Analyze only quaternay references that appear in the orginal
        # paper too (and thus are likely to be relevant).
        for bibcode in pub.reference_bibcodes:
            if bibcode not in self._cited_bibcodes:
                continue
            # TODO combine bibcode to number of mentions to fill in
            # self._tertiary_mentions

    @property
    def score(self):
        """http://en.wikipedia.org/wiki/Cosine_similarity"""
        return np.sum(self._cited_mentions * self._tertiary_mentions) \
            / (np.hypot(self._cited_mentions)
               * np.hypot(self._tertiary_mentions))

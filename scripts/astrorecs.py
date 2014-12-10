#!/usr/bin/env python
# encoding: utf-8
"""
Astrorec paper recommendation engine
"""

import os
import argparse

from astrorec.latexrec import LaTeXRecommender
from astrorec.arxivrec import ArXivRecommender

from starlit.bib.adscache import ADSCacheDB
from starlit.bib.adsdb import ADSBibDB


def main():
    args = parse_args()

    cachedb = ADSCacheDB(host='localhost',
                         port=27017,
                         ads_db=ADSBibDB())

    if os.path.exists(args.input_token):
        # assume it's a latex file
        rec = LaTeXRecommender(args.input_token, ads_cache=cachedb)
    else:
        # assume it's an arXiv ID. Could also be a ADS bibcode eventually
        rec = ArXivRecommender(args.input_token)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_token',
                        help='arxiv ID or path to latex manuscript')
    return parser.parse_args()


if __name__ == '__main__':
    main()

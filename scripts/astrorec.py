#!/usr/bin/env python
# encoding: utf-8
"""
Astrorec paper recommendation engine
"""

import os
import argparse

from astrorec.latexrec import LaTeXRecommender
from astrorec.arxivrec import ArXivRecommender


def main():
    args = parse_args()

    if os.path.exists(args.input_token):
        # assume it's a latex file
        paper_rec = LaTeXRecommender(args.input_token)
    else:
        # assume it's an arXiv ID. Could also be a ADS bibcode eventually
        arxiv_rec = ArXivRecommender(args.input_token)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_token',
                        help='arxiv ID or path to latex manuscript')
    return parser.parse_args()


if __name__ == '__main__':
    main()

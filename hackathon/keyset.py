# -*- encoding:utf-8 -*-
from __future__ import print_function

from textrank4zh import TextRank4Keyword

tr4w = TextRank4Keyword()


def get_keyset(text):
    tr4w.analyze(text=text, lower=True, window=2)
    keyset = []
    for phrase in tr4w.get_keywords(word_min_len=2):
        keyset.append(phrase)
    return keyset

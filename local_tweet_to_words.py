#!/usr/bin/python
# -*- coding: utf-8 -*-
from MaltegoTransform import *
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
import sys, string

# Description:  Locally extract words from Tweets
# Installation: http://dev.paterva.com/developer/getting_started/building_your_own_local_transform.php
# Author:       Michael Henriksen (@michenriksen)

transform = MaltegoTransform()
transform.parseArguments(sys.argv)

tweet      = transform.getVar("content")
stemmer    = SnowballStemmer("english")
stop_words = stopwords.words("english")
with open("top100Kenglishwords.txt") as f:
    common_words = [x.strip().strip().lower().decode("unicode_escape").encode("ascii", "ignore") for x in f.readlines()]
words      = []

for word in tweet.split():
    if word.startswith('#') or word.startswith('@') or word.startswith('\\'):
	continue

    # Normalize word and strip out silliness
    word = word.strip().lower().decode("unicode_escape").encode("ascii", "ignore")
    word = ''.join(ch for ch in word if ch not in string.punctuation)

    if word == '' or word == 'rt' or word.startswith('http'):
        continue

    # Ignore stop-words and common words
    if word in stop_words or word in common_words:
        continue

    word = stemmer.stem(word)

    # Check word again after stemming
    if word in stop_words or word in common_words:
        continue

    words.append(word)

for word in words:
	transform.addEntity("maltego.Phrase", word)

transform.returnOutput()

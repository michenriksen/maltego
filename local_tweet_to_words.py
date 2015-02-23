#!/usr/bin/python
# -*- coding: utf-8 -*-
from MaltegoTransform import *
from nltk.corpus import stopwords
import sys, string

# Description:  Locally extract words from Tweets
# Installation: http://dev.paterva.com/developer/getting_started/building_your_own_local_transform.php
# Author:       Michael Henriksen (@michenriksen)

def normalizeWord(word):
	word = word.strip().lower().decode('unicode_escape').encode('ascii','ignore')
	return ''.join(ch for ch in word if ch not in string.punctuation)

transform = MaltegoTransform()
transform.parseArguments(sys.argv)

tweet      = transform.getVar("content")
stop_words = stopwords.words("english")
words      = []

for word in tweet.split():
	if word.startswith('#') or word.startswith('@') or word.startswith('\\'):
		continue

	word = normalizeWord(word)
	if word != '' and word != 'rt' and not word.startswith('http') and word not in stop_words:
		words.append(word)

for word in words:
	transform.addEntity("maltego.Phrase", word)

transform.returnOutput()

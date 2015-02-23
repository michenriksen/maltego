#!/usr/bin/python
# -*- coding: utf-8 -*-
from MaltegoTransform import *
from ttp import ttp
import sys

# Description:  Locally extract hashtags from Tweets
# Installation: http://dev.paterva.com/developer/getting_started/building_your_own_local_transform.php
# Author:       Michael Henriksen (@michenriksen)

transform = MaltegoTransform()
transform.parseArguments(sys.argv)

tweet        = transform.getVar("content").decode('utf-8')
parser       = ttp.Parser()
parsed_tweet = parser.parse(tweet)

for hashtag in parsed_tweet.tags:
    hashtag = "#" + hashtag
    transform.addEntity("maltego.hashtag", hashtag)

transform.returnOutput()

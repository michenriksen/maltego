#!/usr/bin/python
# -*- coding: utf-8 -*-

# Description:  Locally extract aliases/usernames from Tweets
# Installation: http://dev.paterva.com/developer/getting_started/building_your_own_local_transform.php
# Author:       Michael Henriksen (@michenriksen)

from MaltegoTransform import *
from ttp import ttp
import sys

transform = MaltegoTransform()
transform.parseArguments(sys.argv)

tweet        = transform.getVar("content").decode('utf-8')
parser       = ttp.Parser()
parsed_tweet = parser.parse(tweet)

for alias in parsed_tweet.users:
    transform.addEntity("maltego.Alias", alias)

transform.returnOutput()

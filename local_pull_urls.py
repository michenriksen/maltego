#!/usr/bin/python
# -*- coding: utf-8 -*-
from MaltegoTransform import *
from ttp import ttp
from urlparse import urlparse
import sys, httplib

# Description:  Locally extract URLs from Tweets
# Installation: http://dev.paterva.com/developer/getting_started/building_your_own_local_transform.php
# Author:       Michael Henriksen (@michenriksen)

transform = MaltegoTransform()
transform.parseArguments(sys.argv)

tweet        = transform.getVar("content").decode('utf-8')
parser       = ttp.Parser()
parsed_tweet = parser.parse(tweet)

for url in parsed_tweet.urls:
    parsed_url = urlparse(url)

    # Expand Twitter shortened URLs
    if parsed_url.hostname == "t.co":
        transform.addUIMessage("Expanding t.co URL: " + url, "Inform")

        # Perform a HEAD request on t.co via secure connection
        connection = httplib.HTTPSConnection(parsed_url.hostname)
        connection.request("HEAD", parsed_url.path)
        response = connection.getresponse()

        # Loop through each header until we find the Location header
        for header in response.getheaders():
            if header[0] == 'location':
                url = header[1]
                break

    ent = transform.addEntity("maltego.URL", url)
    ent.addAdditionalFields("url", "URL", True, url)

transform.returnOutput()

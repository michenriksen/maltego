#!/usr/bin/python
# -*- coding: utf-8 -*-
from MaltegoTransform import *
from urlparse import urlparse
import sys, httplib

# Description:  Follows HTTP redirects and returns the final URL.
# Installation: http://dev.paterva.com/developer/getting_started/building_your_own_local_transform.php
# Author:       Michael Henriksen (@michenriksen)

def follow_redirects(url, maximum_redirects = 15):
  parsed_url = urlparse(url)
  if parsed_url.scheme == 'https':
    connection = httplib.HTTPSConnection(parsed_url.hostname)
  else:
    connection = httplib.HTTPConnection(parsed_url.hostname)

  connection.request("HEAD", parsed_url.path)
  response = connection.getresponse()

  if response.status >= 300 and response.status <= 399:
    if maximum_redirects == 0:
      transform.addUIMessage("Too many redirects; giving up.", "FatalError")
      return url

    transform.addUIMessage("Got redirect response from " + parsed_url.hostname + "; following...", "Inform")
    for header in response.getheaders():
      if header[0] == 'location':
        return follow_redirects(header[1], maximum_redirects - 1)
    transform.addUIMessage("Location header was not found...", "PartialError")
    return url
  else:
    transform.addUIMessage("Got non-redirect response from " + parsed_url.hostname + ": " + str(response.status) + " " + response.reason, "Inform")
    return url

transform = MaltegoTransform()

url       = sys.argv[1]
final_url = follow_redirects(url)

if url != final_url:
    transform.addUIMessage(url + " redirected to: " + final_url, "Inform")

    ent = transform.addEntity("maltego.URL", urlparse(final_url).hostname)
    ent.addAdditionalFields("url", "URL", True, final_url)
else:
    transform.addUIMessage(url + " did not redirect.", "Inform")

transform.returnOutput()

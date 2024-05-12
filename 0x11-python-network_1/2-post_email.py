#!/usr/bin/python3
"""Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)"""

import sys
import urllib.parse
import urllib.request

if __name__ == "_main_":
    url = sys.argv[1]
    work = {"ëmail": sys.argv[2]}
    info = urllib.parse.urlencode(work).encode("ascii")

    req = urllib.request.Request(url, info)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))

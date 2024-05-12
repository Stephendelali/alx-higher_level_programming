#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.."""
import sys
import urllib.request
import urllib.parse


if __name__ == "_main_":
    url = sys.argv[1]
    
    request = urllib.request.Request(url)
    try :
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except urlib.error.HTTPError as e:
        print ("Error code:{} ".format (e.code))  

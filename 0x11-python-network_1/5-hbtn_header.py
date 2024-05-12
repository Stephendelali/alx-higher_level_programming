#!/usr/bin/python3
"""
Python script that fetches a url and prints a specific header value
"""


if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    info = requests.get(url)
    info = info.headers
    print(info.get("X-Request-Id"))

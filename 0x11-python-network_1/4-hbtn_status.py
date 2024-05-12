#!/usr/bin/python3
"""A Python script that fetches
https://alx-intranet.hbtn.io/status """

import requests

if __name__ == "_main_":
    info = requests.get("https://alx-intranet.hbtn.io/status")

    print("Body response:")
    print("\t- type: {}".format(type(info)))
    print ("\t- content:".format(info.text))

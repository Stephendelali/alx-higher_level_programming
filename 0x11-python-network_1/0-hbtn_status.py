#!/usr/bin/python3

""" Python script that fetches https://alx-intranet.hbtn.io/status """

import urllib.request
with urllib.request.urlopen ('https://alx-intranet.hbtn.io/status')as response:
    text = response.read()


    print('Body response:')
    print('\t- typp: {}'.format (type(text)))
    print('\t- content: {}'.format(text))
    print('t- utf8 content: {}'.format(text.decode('utf-8')))

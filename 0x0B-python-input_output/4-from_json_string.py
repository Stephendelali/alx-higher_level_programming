#!/usr/bin/python3
# 6-from_json_string.py
"""shows a JSON to object ."""
import json


def from_json_string(my_str):
    """Provide back a JSON string's object representation in Python."""
    return json.loads(my_str)

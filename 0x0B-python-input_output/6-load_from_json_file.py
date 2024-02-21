#!/usr/bin/python3
"""Shows JSON file-reading function."""
import json


def load_from_json_file(filename):
    """Creates an object using python from a JSON file."""
    with open(filename) as f:
        return json.load(f)

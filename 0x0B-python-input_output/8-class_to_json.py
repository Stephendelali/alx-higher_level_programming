#!/usr/bin/python3
"""outlines the Python class-to-JSON function."""


def class_to_json(obj):
    """provides the data dictionary form of a data structure."""
    return obj.__dict__

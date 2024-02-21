#!/usr/bin/python3
"""Creates a function that checks classes."""


def is_same_class(obj, a_class):
    if type(obj) == a_class:
        return True
    return False

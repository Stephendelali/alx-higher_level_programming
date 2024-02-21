#!/usr/bin/python3
"""defines a function for checking inheritance classes."""


def inherits_from(obj, a_class):
    """Checks for inheritance of a class

    Args:
        obj (any): The object .
        a_class (type): The class 
    Returns:
        True If obj is an inherited instance of a_class 
        false otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False

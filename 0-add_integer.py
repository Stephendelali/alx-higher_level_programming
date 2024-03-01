#!/usr/bin/python3
"""defines the addition function for integers."""


def add_integer(a, b=98):
    
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a = integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b = integer")
    return (int(a) + int(b))

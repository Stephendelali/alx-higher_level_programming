#!/usr/bin/python3
"""showes a file opening function"""


def append_write(filename="", text=""):
    """adds a string to a UTF8 text file's end.

    Args:
        filename (str): the file name 
        text (str): The end string.
    Returns:
        the characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

#!/usr/bin/python3
"""JSON file-writing function."""
import json

"""Write an object to a text file using JSON."""
def save_to_json_file(my_obj, filename): 
    with open(filename, "w") as f:
        json.dump(my_obj, f)

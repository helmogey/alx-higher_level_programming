#!/usr/bin/python3
""" function that writes an Object to a text file, using a JSON representation:"""
import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        The Python object represented by the JSON data in the file.
    """

    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

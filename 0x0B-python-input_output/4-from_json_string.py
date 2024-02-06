#!/usr/bin/python3
"""returns an object (Python data structure) represented by a JSON string"""
import json


def from_json_string(my_str):
    """
    Returns an object represented by a JSON string.

    Args:
        my_str: The JSON string to convert to an object.

    Returns:
        The Python object represented by the JSON string.
    """

    return json.loads(my_str)

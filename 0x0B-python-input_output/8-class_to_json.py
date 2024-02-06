#!/usr/bin/python3
"""  returns the dictionary description with simple data structure
(list, dictionary, string, integer and boolean) for JSON
serialization of an object:"""


def class_to_json(obj):
    """
    Returns a dictionary description of an object suitable for JSON serialization.

    Args:
        obj: An instance of a class.

    Returns:
        A dictionary containing the serializable attributes of the object.
    """

    data = {}

    for attr_name, attr_value in obj.__dict__.items():
        if not attr_name.startswith("__"):  # Skip private attributes and methods
            if isinstance(attr_value, (list, dict, str, int, bool)):
                data[attr_name] = attr_value
            else:
                data[attr_name] = "NOT SERIALIZABLE"  # Handle non-serializable types

    return data

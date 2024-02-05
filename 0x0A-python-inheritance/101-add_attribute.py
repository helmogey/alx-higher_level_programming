#!/usr/bin/python3
"""function that adds a new attribute to an object if it’s possible"""



def add_attribute(obj, name, value):
    """
    Adds a new attribute to an object if possible, raising a TypeError if not.

    Args:
        obj: The object to add the attribute to.
        name: The name of the new attribute.
        value: The value to assign to the new attribute.

    Raises:
        TypeError: If the object does not allow new attributes.
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(obj, name, value)

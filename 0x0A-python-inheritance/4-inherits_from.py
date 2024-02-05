#!/usr/bin/python3
"""returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False"""


def inherits_from(obj, a_class):
    """Check if an object is exactly an instance of a given class.

        Args:
            obj (any): The object to check.
            a_class (type): The class to match the type of obj to.
        eturns:
            returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False
        """
    return issubclass(type(obj), a_class) and type(obj) != a_class

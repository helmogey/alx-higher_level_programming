#!/usr/bin/python3
"""returns True if the object is exactly an instance of the specified class ; otherwise False"""


def is_kind_of_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.

        Args:
            obj (any): The object to check.
            a_class (type): The class to match the type of obj to.
        Returns:
            returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False
        """
    return isinstance(obj, a_class)

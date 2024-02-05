#!/usr/bin/python3
def lookup(obj):
    """
      Returns a list of available attributes and methods of an object.

      Args:
          obj: The object to inspect.

      Returns:
          A list of strings, where each string represents an attribute or method name.
      """
    return (dir(obj))

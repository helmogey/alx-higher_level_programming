#!/usr/bin/python3
def lookup(obj):
    """
      Returns a list of available attributes and methods of an object.

      Args:
          obj: The object to inspect.

      Returns:
          A list of strings, where each string represents an attribute or method name.
      """
    attributes = []
    methods = []

    # Get all attributes and methods of the object
    for name in dir(obj):
        # Filter out private and special methods
        if not name.startswith("__"):
            # Check if it's an attribute or method
            if hasattr(obj, name):
                attributes.append(name)
            else:
                methods.append(name)

    # Combine attributes and methods into a single list
    return attributes + methods

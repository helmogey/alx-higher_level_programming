#!/usr/bin/python3
"""contains the MyList class"""


class MyList(list):
  """
  A custom list class that inherits from the built-in list class and adds a method to print the list sorted.
  """

  def __init__(self):
      """initializes the object"""
      super().__init__()

  def print_sorted(self):
    """
    Prints the list in ascending order.
    """
    # Sort the list in ascending order
    sorted_list = sorted(self)  # Use the built-in sorted function for efficiency
    print(sorted_list)

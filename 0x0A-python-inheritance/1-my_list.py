#!/usr/bin/python3
class MyList(list):
  """
  A custom list class that inherits from the built-in list class and adds a method to print the list sorted.
  """

  def print_sorted(self):
    """
    Prints the list in ascending order.
    """
    # Sort the list in ascending order
    sorted_list = sorted(self)  # Use the built-in sorted function for efficiency
    print(sorted_list)

#!/usr/bin/python3
""" function that finds a peak in a list of unsorted integers. """

def find_peak(list_of_integers):
    """
    Finds a peak element in a list of unsorted integers.

    A peak element is an element that is greater than both its neighbors.
    If the list is empty or has only one element, None is returned.

    Args:
        list_of_integers: A list of unsorted integers.

    Returns:
        The peak element in the list, or None if the list is empty or has only one element.
    """

      # Handle empty list or single element case
    if len(list_of_integers) <= 1:
      return None

      # Iterate through the list, checking for elements greater than both neighbors
    for i in range(1, len(list_of_integers) - 1):
      if list_of_integers[i] > list_of_integers[i - 1] and list_of_integers[i] > list_of_integers[i + 1]:
        return list_of_integers[i]

      # No peak found in the list
    return None

print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))

#!/usr/bin/python3
"""append to UTF8 file"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF8) and returns the number of characters added.
    Creates the file if it doesn't exist.

    Args:
        filename (str): The name of the file to append to. Defaults to "".
        text (str): The text to append to the file. Defaults to "".

    Returns:
        int: The number of characters appended to the file.
    """

    with open(filename, "a", encoding="utf-8") as file:  # Open in append mode ("a")
        num_chars = file.write(text)
    return num_chars

#!/usr/bin/python3
"""write UTF8 file"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of characters written.

    Args:
        filename (str): The name of the file to write to. Defaults to "".
        text (str): The text to write to the file. Defaults to "".

    Returns:
        int: The number of characters written to the file.
    """

    with open(filename, "w", encoding="utf-8") as file:
        num_chars = file.write(text)
    return num_chars

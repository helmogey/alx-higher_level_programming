#!/usr/bin/python3
"""function that returns the list of available attributes and methods of an object"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its contents to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to "".
    """

    with open(filename, "r", encoding="utf-8") as file:
        contents = file.read()
        print(contents)

#!/usr/bin/python3
""" function that inserts a line of text to a file, after each
line containing a specific string """


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text (new_string) after each line containing a specific string (search_string) in a file.

    Args:
        filename (str): The name of the file to modify. Defaults to "".
        search_string (str): The string to search for in the file. Defaults to "".
        new_string (str): The string to insert after matching lines. Defaults to "".
    """

    with open(filename, "r+", encoding="utf-8") as file:
        lines = file.readlines()
        file.seek(0)  # Rewind to the beginning of the file

        for line in lines:
            file.write(line)  # Write the original line
            if search_string in line:
                file.write(new_string + "\n")  # Insert the new string after a match

        # Ensure the file ends with a newline (in case the last line didn't have one)
        file.write("\n")

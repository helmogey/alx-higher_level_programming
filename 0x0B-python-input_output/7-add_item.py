#!/usr/bin/python3
""" function that writes an Object to a text file, using a JSON representation:"""
import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


    filename = "add_item.json"

    try:
        # Load existing items from file, if any
        existing_items = load_from_json_file(filename)
    except FileNotFoundError:
        existing_items = []  # Create an empty list if the file doesn't exist

    # Combine existing items with new items
    all_items = existing_items + sys.argv[1:]

    # Save the updated list to the file
    save_to_json_file(all_items, filename)


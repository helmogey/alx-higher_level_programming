#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary:
        for key in a_dictionary:
            if a_dictionary[key] == value:
                a_dictionary.pop(key)
        return a_dictionary

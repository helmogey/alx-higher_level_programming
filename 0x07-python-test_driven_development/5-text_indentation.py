#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    k = ["." ,"?" ,":"]
    print(text.split(" "))
    for word in text.split(" "):
        if any(char in k for char in word):
            print(word)
            print()
        else:
            print(word, end=" ")
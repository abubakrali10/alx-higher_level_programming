#!/usr/bin/python3
def text_indentation(text):
    """Function that prints two lines after special characters (. : ?)
    Args:
        text (str): The text to check
    Raises:
        TypeError: If text is not a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    i = 0
    spec_char = [".", "?", ":"]
    while i < len(text):
        if text[i] in spec_char:
            print(text[i])
            print()
            i += 1
        else:
            print(text[i], end="")
        i += 1

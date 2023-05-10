#!/usr/bin/python3
def uppercase(str):
    full_str = ""
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            full_str += chr(ord(char) - 32)
        else:
            full_str += char
    print("{}".format(full_str))

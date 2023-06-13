#!/usr/bin/python3
""" adds all arguments to a Python list, and saving them to a file """
import sys
save_to_json = __import__('5-save_to_json_file').save_to_json_file
load_from_json = __import__('6-load_from_json_file').load_from_json_file


try:
    li = load_from_json("add_item.json")
except Exception:
    li = []

for arg in sys.argv[1:]:
    li.append(arg)
save_to_json(li, "add_item.json")

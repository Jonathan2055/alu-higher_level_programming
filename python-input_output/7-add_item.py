#!/usr/bin/python3
"""
This module provides a script that adds all command-line arguments
to a Python list and saves them to a JSON file. The list is stored
in 'add_item.json' and persists across multiple script executions.

Functions:
- Uses save_to_json_file() from 5-save_to_json_file.py to save data.
- Uses load_from_json_file() from 6-load_from_json_file.py to load data.
"""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []

    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")

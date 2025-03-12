#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys
import os


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    filename = "add_item.json"

    # Ensure the file exists before loading
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            f.write("[]")

    try:
        items = load_from_json_file(filename)
    except FileNotFoundError:
        items = []

    items.extend(sys.argv[1:])
    save_to_json_file(items, filename)

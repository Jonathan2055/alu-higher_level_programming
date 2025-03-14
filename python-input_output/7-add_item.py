#!/usr/bin/python3
"""
Script that adds all command-line arguments to a Python list 
and saves them to a file in JSON format.
"""

import sys  # Import sys to access command-line arguments
from 5-save_to_json_file import save_to_json_file  # Import function to save JSON
from 6-load_from_json_file import load_from_json_file  # Import function to load JSON

if __name__ == "__main__":  # Ensure the script runs only when executed directly
    filename = "add_item.json"  # Define the file where the list will be stored

    # Try to load the existing list from the file
    try:
        items = load_from_json_file(filename)  # Read the JSON file and load data as a list
    except FileNotFoundError:
        # If the file does not exist, initialize an empty list
        items = []

    # Extend the list with command-line arguments (excluding the script name)
    items.extend(sys.argv[1:])  # Append new arguments to the existing list

    # Save the updated list back to the file in JSON format
    save_to_json_file(items, filename)  # Write the modified list back to the JSON file

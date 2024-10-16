#  Write a Python program to read a random line from a file.

import random

def read_random_line(file_path):
    with open(file_path) as file:
        lines = file.readlines()
        return random.choice(lines).strip() if lines else "The file is empty."

# Example usage
file_path = 'your_file.txt'  # Replace with your file path
print(read_random_line(file_path))

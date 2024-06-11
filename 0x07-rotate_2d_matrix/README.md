Rotate 2D Matrix

This Python script implements a function to rotate a 2D matrix 90 degrees clockwise in-place.

Functionality

The provided function rotate_2d_matrix takes a 2D matrix represented as a list of lists and modifies it directly to achieve a 90-degree clockwise rotation.

How it Works

The function employs a two-step approach:

Transposition: It iterates through the upper triangle of the matrix, swapping elements to effectively transpose the rows and columns.
Row Reversal: After transposing, it reverses the elements in each row to complete the 90-degree clockwise rotation.
Example Usage

The script includes an example demonstrating how to use the rotate_2d_matrix function. It creates a sample matrix, rotates it, and prints the resulting rotated matrix.

Requirements

Python 3 (interpreter specified in the first line)
No external modules are imported
Running the Script

Save the code as 0-rotate_2d_matrix.py.
Ensure the file has execute permissions (e.g., chmod +x 0-rotate_2d_matrix.py).
Run the script from the command line: ./0-rotate_2d_matrix.py
The output will display the rotated matrix.

Additional Notes

The code adheres to the pycodestyle style guide for Python code formatting.

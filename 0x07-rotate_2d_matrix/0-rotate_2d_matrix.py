#!/usr/bin/python3

"""
Rotates a 2D matrix 90 degrees clockwise in-place.

Args:
    matrix: A list of lists representing a 2D matrix.

Returns:
    None (modifies the matrix in-place).
"""
def rotate_2d_matrix(matrix):
  n = len(matrix)

  # Transpose the matrix
  for i in range(n):
    for j in range(i, n):
      matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

  # Reverse each row of the transposed matrix
  for row in matrix:
    row.reverse()


# Example usage
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

rotate_2d_matrix(matrix)
print(matrix)

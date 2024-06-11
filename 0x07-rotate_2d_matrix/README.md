# Rotate 2D Matrix

This project contains a function to rotate a 2D matrix 90 degrees clockwise.

## Function Description

### `rotate_2d_matrix(matrix)`

This function takes a square 2D matrix as input and rotates it 90 degrees clockwise in place.

#### Parameters

- `matrix` (list of list of int): The 2D matrix to rotate. It should be a square matrix (NxN).

#### Returns

The function does not return any value. It modifies the input matrix in place.

## How the Function Works

The function uses nested loops to access each element of the matrix and swap its values with the elements located at the corresponding positions in the rotated matrix. The rotation is performed layer by layer, starting from the outermost layer and moving towards the innermost layer.

Here is a step-by-step explanation of the rotation process for a given element at position `(i, j)`:

1. Store the element at `(i, j)` in a temporary variable `temp`.
2. Move the element from the left to the top.
3. Move the element from the bottom to the left.
4. Move the element from the right to the bottom.
5. Move the temporary variable `temp` to the right.

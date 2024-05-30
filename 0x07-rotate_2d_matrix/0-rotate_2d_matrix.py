#!/usr/bin/python3
"""
2D matrix

This script defines a function to rotate a 2D matrix 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    ''' Rotates a 2d matrix 90° clockwise
    Returns: Nothing
    '''
    # Initialize the left and right pointers to the
    # first and last column indices of the matrix
    left, right = 0, len(matrix) - 1

    # Continue rotating layers until left pointer
    # is less than the right pointer
    while left < right:
        # Iterate over each element in the current layer (except the last one)
        for i in range(right - left):
            # Define the top and bottom pointers for the current layer
            top, bottom = left, right
            # Store the top left element in a temporary variable
            topLeft = matrix[top][left + i]
            # Move the bottom left element to the top left position
            matrix[top][left + i] = matrix[bottom - i][left]
            # Move the bottom right element to the bottom left position
            matrix[bottom - i][left] = matrix[bottom][right - i]
            # Move the top right element to the bottom right position
            matrix[bottom][right - i] = matrix[top + i][right]
            # Move the top left element (stored in the temporary variable)
            # to the top right position
            matrix[top + i][right] = topLeft
        # Move the pointers inward to the next layer
        right -= 1
        left += 1

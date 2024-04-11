#!/usr/bin/python3
"""Pascal Triangle Interview Challenge"""


def pascal_triangle(n):
    """
    Returns a list of lists representing the first n rows of Pascal's triangle.

    Pascal's triangle is a triangular array of the binomial coefficients.
    Each row starts and ends with the number 1, and each
    interior element is the sum of the
    two elements above it in the previous row.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list of lists: The first n rows of Pascal's triangle.
    """

    # Return an empty list if n is less than or equal to 0
    if n <= 0:
        return []

    # Initialize Pascal's triangle with the first row [1]
    triangle = [[1]]

    # Iterate from the 2nd row to the nth row
    for i in range(1, n):
        # Get the previous row
        prev_row = triangle[-1]

        # Create the current row starting with 1
        current_row = [1]

        # Calculate the inner values of the current row
        # Each ele is the sum of the two elements above it in the previous row
        for j in range(1, len(prev_row)):
            current_row.append(prev_row[j - 1] + prev_row[j])

        # End the current row with 1
        current_row.append(1)

        # Add the current row to the triangle
        triangle.append(current_row)

    # Return the completed Pascal's triangle
    return triangle

#!/usr/bin/python3
''' The minimum operations coding challenge.'''


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in
    exactly n H characters in the file.

    Parameters:
    n (int): The desired number of H characters.

    Returns:
    int: The fewest number of operations needed to achieve exactly n H
    characters.
    If n is impossible to achieve, return 0.
    """

    if n <= 1:
        return 0

    # Initialize the result with n itself since it's the maximum possible
    # operations
    result = n

    # Iterate over the factors of n
    for i in range(2, int(n**0.5) + 1):  # for i in range(2, n // 2 + 1)
        if n % i == 0:
            # If i is a factor of n, calculate the operations needed for
            # i copies and n//i pastes
            result = min(result, minOperations(n // i) + i)

    # Return the minimum number of operations
    return result

def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]  # First element of each row is always 1
        for j in range(1, i + 1):
            if j < len(triangle[i - 1]):
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            else:
                row.append(1)  # Last element of each row is always 1
        triangle.append(row)

    return triangle


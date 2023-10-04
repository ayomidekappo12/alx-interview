#!/usr/bin/python3

def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]  # The first element of each row is always 1
        if triangle:
            prev_row = triangle[-1]
            for j in range(1, len(prev_row)):
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)  # The last element of each row is always 1
        triangle.append(row)

    return triangle

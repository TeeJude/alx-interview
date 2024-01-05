#!/usr/bin/python3
"""
A module for working with Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Creates a list of lists of integers representing
    the Pascal's triangle of a given integer.
    """
    Pas_Tri = []
    if type(n) is not int or n <= 0:
        return Pas_Tri
    for i in range(n):
        line = []
        for j in range(i + 1):
            if j == 0 or j == i:
                line.append(1)
            elif i > 0 and j > 0:
                line.append(Pas_Tri[i - 1][j - 1] + Pas_Tri[i - 1][j])
        Pas_Tri.append(line)
    return Pas_Tri

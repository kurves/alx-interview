#!/usr/bin/python3
"""
This module defines the function island_perimeter that calculates
the perimeter of an island described in a grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island in grid.
    int: Perimeter of the island
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4

                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter

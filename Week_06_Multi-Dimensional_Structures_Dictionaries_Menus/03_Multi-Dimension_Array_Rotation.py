"""
TASK: 03 Multi-Dimension Array Rotation

# Rotate a 2D matrix 90 degrees clockwise manually
Good luck

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

import random

def initArray(rows, collumns):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(collumns):
            row.append(2*i + j)
        matrix.append(row)
    return(matrix)

def printGrid(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

def rotate(m, n, matrix):
    rotation = initArray(m,n)
    for i in range(n):
        for j in range(m):
            rotation[j][-i-1] = matrix[i][j]
    return(rotation)


if __name__ == "__main__":
    m = 5
    n = 5
    grid = initArray(m,n)
    print("Original grid:")
    printGrid(grid)
    rGrid = rotate(m,n,grid)
    print("Rotated grid:")
    printGrid(rGrid)


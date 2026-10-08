"""
TASK: 03 Grid Path Counter

# Grid Path Counter - https://bk2coady.medium.com/daily-coding-problem-62-bfe0e398247b
Given an NxM grid:
- Count paths using recursion
- Count paths using iteration
Movement allowed: RIGHT or DOWN only.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def initArray(rows, collumns):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(collumns):
            row.append("X")
        matrix.append(row)#
    return(matrix)

def rPath(row,col):
    if row <= 0 or col <= 0:
        return(0)
    if row == 1 or col == 1:
        return(1)
    return(rPath(row-1,col) + rPath(row,col-1))

def iPath(row,col):
    paths = [0] * col
    paths[0] = 1
    for i in range(row):
# paths[j] stores the number of paths to reach the current cell in the current row, i. 
# paths[0] stays as 1, since there's always only 1 way to reach the elements in the 1st collumn.
        for j in range(1, col):
            paths[j] += paths[j-1]
    return(paths[col-1])

if __name__ == "__main__":
    r = 5
    c = 5
    grid = initArray(r % 16, c % 16)
    print(grid)

print(rPath(r,c))
print(iPath(r,c))
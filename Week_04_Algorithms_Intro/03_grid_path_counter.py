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
    rFactorial = 1
    cFactorial = 1
    tFactorial = 1
    for i in range(row - 1):
        rFactorial *= (i + 1)
    for i in range(col - 1):
        cFactorial *= (i + 1)
    for i in range(row + col - 2):
        tFactorial *= (i + 1)
    return(tFactorial//(rFactorial*cFactorial))

if __name__ == "__main__":
    r = 12
    c = 12
    grid = initArray(r % 16, c % 16)
    print(grid)

print(rPath(r,c))
print(iPath(r,c))
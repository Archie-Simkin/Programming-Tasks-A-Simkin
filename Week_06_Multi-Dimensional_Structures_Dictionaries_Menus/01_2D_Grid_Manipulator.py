"""
TASK: 01 2D Grid Manipulator

# Create an NxM grid resolver - https://bk2coady.medium.com/daily-coding-problem-62-bfe0e398247b
- Initialises a grid filled with zeros
- Allows user to "paint" coordinates
- Displays updated grid each time

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def initArray(rows, collumns):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(collumns):
            row.append(0)
        matrix.append(row)
    return(matrix)

def printGrid(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

def paint(x, y, value, matrix):
    matrix[y - 1][x - 1] = value
    return(matrix)



if __name__ == "__main__":
    m = 8
    n = 8
    grid = initArray(m,n)
    printGrid(grid)
    while True:
        try:
            x = int(input("Enter collumn number of item you would like to edit. (1 to " + str(n) + ")\n"))
            y = int(input("Enter row number of item you would like to edit. (1 to " + str(n) + ")\n"))
        except:
            print("Input must be an integer.")
        else:
            grid = paint(x, y, input("Enter something into the grid.\n"), grid)
            printGrid(grid)


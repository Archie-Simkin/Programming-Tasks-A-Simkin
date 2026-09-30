"""
TASK: 03 2D Array Adder

# 2D Array Added
Create a 2D arraw and allow user to:
- Append new values in
- read all current values
- delete a chosen entry

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
            row.append(chr(random.randint(65,90)))
        matrix.append(row)#
    return(matrix)

def choose_action(action):
    while action.upper() != "NONE":
        if action.upper() == "VIEW":
            for i in range(0,r):
                print(matrix[i])
        elif action.upper() == "REPLACE":
            try:
                inRow = int(input("Enter the row of the item you would like to replace.\n")) - 1
                inCollumn = int(input("Enter the collumn of the item you would like to replace.\n")) - 1
                matrix[inRow][inCollumn] = input("Enter what you would like to replace it with.\n")

            except:
                print("Error, inputs must be an integer.")
        elif action.upper() == "DELETE":
            try:
                inRow = int(input("Enter the row of the item you would like to delete.\n")) - 1
                inCollumn = int(input("Enter the collumn of the item you would like to delete.\n")) - 1
                matrix[inRow][inCollumn] = ""
            except:
                print("Error, inputs must be an integer.")
        else:
            print("Action not recognised, please try again.")
        action = input("Choose an action: 'view', 'replace', 'delete' or 'none'.\n")


if __name__ == "__main__":
    r = 5
    c = 5
    matrix = initArray(r,c)
    choose_action(input("Choose an action: 'view', 'replace', 'delete' or 'none'.\n"))
"""
TASK: 01 Csv Writer

# Skills: CSV writing
CAsk the user for:
- Name
- age
- favourite colour
- anything you want
Append this to a CSV file (Extend: allow user to choose to edit the file and read the file)

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

import csv

def main(name, quest, colour):
    with open("csvFile.csv", "a") as file:
        file.write(name + " ")
        file.write(quest + " ")
        file.write(colour)
    with open("csvFile.csv", "r") as file:
        read = csv.reader(file, delimiter=' ', quotechar='|')
        for row in read:
            print(', '.join(row))

if __name__ == "__main__":
    with open("csvFile.csv", "w") as file:
        file.write("")
    main(input("What is your name?\n"),input("What is your quest?\n"),input("What is your favourite colour?\n"))

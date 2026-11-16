"""
TASK: 01 Grade Writer

# Purpose is to write a grade uploading program for csv files
Ask the user for student names and ages, with a keyword to stop.
Writes all entries to a .txt file and .csv file separately

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

import csv

def enterGrades():
    stop = False
    grades = []
    while stop != True:
        name = input("Enter student name.\n")
        while True:
            try:
                age = int(input("Enter student age.\n"))
                break
            except:
                print("Age must be an integer.")
        grade = input("Enter student grade.\n")
        grades.append(name + "," + str(age) + "," + grade)
        if input("Enter another grade? (Y/N)\n").upper() == "N":
            stop = True
    return(grades)

def txtWrite(filename, grades):
    with open(filename, "w") as file:
        for i in range(len(grades)):
            file.write(grades[i])

def csvWrite(filename, grades, newline='', encoding='utf-8'):
    with open(filename, "w") as file:
        writer = csv.writer(file)
        writer.writerow(["Name","Age","Grade"])
        for i in range(len(grades)):
            line = grades[i].split(",")
            writer.writerow(line)

if __name__ == "__main__":
    grades = enterGrades()
    txtWrite("week8_01.txt",grades)
    csvWrite("week8_01.csv",grades)
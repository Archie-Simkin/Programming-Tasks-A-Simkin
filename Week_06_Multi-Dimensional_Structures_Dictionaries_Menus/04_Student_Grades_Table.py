"""
TASK: 04 Student Grades Table

# Use a dictionary of lists e.g
grades = {
  "Alice": [80, 85, 90],
  "Ben": [70, 60, 75]
}
Add:
- Function to compute class averages
- Function to add student
- Function to remove student

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

import datetime

grades = {
    "Alice": [95, 42, 78],
    "Bob": [34, 88, 91],
    "Charlie": [99, 97, 93],
    "David": [12, 75, 56],
    "Emma": [92, 23, 96],
    "Frank": [77, 81, 19],
    "Grace": [48, 94, 90],
    "Harry": [65, 31, 73],
    "Isabella": [100, 85, 38],
    "Jack": [29, 83, 87]
}

def calcAverage(dict1, grades):
    totals = [0] * grades
    for i in dict1:
        results = dict1[i]
        for j in range(len(results)):
            totals[j] += results[j]
    for k in range(len(totals)):
        totals[k] /= len(dict1)
    return(totals)

def addStudent(dict1, grades):
    name = input("Enter name of student to add.\n")
    results = [0] * grades
    for i in range(grades):
        results[i] = int(input("Enter grade.\n"))
    dict1[name] = results
    return(dict1)

def removeStudent(dict1, grades):
    name = input("Enter name of student to remove.\n").lower()
    try:
        dict1.pop(name.capitalize())
    except:
        print("Student not found.")
    return(dict1)


print(removeStudent(grades, 3))
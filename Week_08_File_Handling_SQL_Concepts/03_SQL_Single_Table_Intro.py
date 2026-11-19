"""
TASK: 03 Sql Single Table Intro

# You will need to visit https://www.w3schools.com/python/ref_module_sqlite3.asp
Provide an SQLite database with one table- Tasks:
- Connect using Python sqlite3 import
- Run simple SELECT queries
- Insert new records
- Display table in formatted text output

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""
import sqlite3

def createTable():
    connect = sqlite3.connect(':memory:')
    cursor = connect.cursor()
    cursor.execute('CREATE TABLE mathsStudents (name TEXT, age INTEGER, grade TEXT)')
    connect.commit()
    return(connect, cursor)

def insertRecords(connect, cursor):
    while True:
        name = input("Enter student name.\n")
        while True:
            try:
                age = int(input("Enter student age.\n"))
                break
            except:
                print("Age must be an integer.")
        grade = input("Enter student grade.\n")
        sql = "INSERT INTO mathsStudents (name, age, grade) VALUES (?, ?, ?)"
        cursor.execute(sql, (name, age, grade))
        connect.commit
        if input("Add another student? Y/N\n").upper() == "N":
            break
    return(connect, cursor)

if __name__ == "__main__":
    connect, cursor = createTable()
    insertRecords(connect,cursor)
    cursor.execute('SELECT * FROM mathsStudents')
    for row in cursor.fetchall():
        print("Student: " + row[0] + ", " + str(row[1]) + "      Grade: " + row[2])
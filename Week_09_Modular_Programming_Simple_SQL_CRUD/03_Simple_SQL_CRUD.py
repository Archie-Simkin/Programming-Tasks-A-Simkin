"""
TASK: 03 Simple Sql Crud

# Create Read Update Delete all with SQL
Have an SQLite table: students(id, name, score)
Implement:
- INSERT
- UPDATE
- DELETE
- SELECT
using Python

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""
import sqlite3

def createTable():
    con = sqlite3.connect('week9_03.db')
    cursor = con.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS students (name TEXT, id TEXT, score INTEGER)')
    return(con, cursor)

def insertData(cursor, name, id, score):
    command = "INSERT INTO students (name, id, score) VALUES (?, ?, ?)"
    cursor.execute(command, (name, id, score))

def deleteData(cursor, id):
    command = "DELETE FROM students WHERE id = ?"
    cursor.execute(command, (id,))

def updateTable(con):
    con.commit()

def selectData(cursor, id):
    command = "SELECT * FROM students WHERE id = ?"
    cursor.execute(command, (id,))
    return(cursor.fetchall())

if __name__ == "__main__":
    con, cursor = createTable()
    print(selectData(cursor, "G18F"))

"""
TASK: 01 Inventory System

# This is all working around an SQLite database with a single table, all module relate to this function
Modules:
- input record module
- Caluclate averages module
- display data module
- file storage module (save as an excel file or new database)

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

import sqlite3
import csv

def createTable():
    con = sqlite3.connect('inventory.db')
    cursor = con.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS inventory (name TEXT, price FLOAT, stock INTEGER)')
    con.commit()
    return(con, cursor)

def insertRecord(con, cursor, name, price, stock):
    command = "INSERT INTO inventory (name, price, stock) VALUES (?, ?, ?)"
    cursor.execute(command, (name, price, stock))
    con.commit()

def calcAverage(cursor):
    totalPrice = 0
    totalStock = 0
    counter = 0
    for row in cursor.execute("SELECT * FROM inventory"):
        totalPrice += row[1]
        totalStock += row[2]
        counter += 1
    return(totalPrice/counter, totalStock/counter)

def displayData(cursor):
    for row in cursor.execute("SELECT * FROM inventory"):
        print(row)

def saveFile(cursor, filename):
    cursor.execute("SELECT * FROM inventory")
    data = cursor.fetchall()
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)

if __name__ == "__main__":
    con, cursor = createTable()
    displayData(cursor)
    print(calcAverage(cursor))
    saveFile(cursor, "week9_01.csv")

"""
TASK: 02 Library Item Inheritance

# This will require you understand how inheritance works
Base class: Item
Attributes: title, year
Subclasses:
- Book - add author attribute
- DVD - add director
Demonstrate polymorphism by iterating a list of mixed objects

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

class Item:
    def __init__(self,t,y):
        self._title = t
        self._year = y

class Book(Item):
    pass

    def details(self):
        print("Type - Book, Title - " + self._title + ", Year - " + self._year)

class DVD(Item):
    pass

    def details(self):
        print("Type - DVD, Title - " + self._title + ", Year - " + self._year)

def registerItems():
    newItem = input("Enter 'DVD', 'BOOK' or 'NONE' to register an item.\n")
    items = []
    while newItem.upper() != "NONE":
        if newItem.upper() == "DVD":
            title = input("Enter title.\n")
            year = input("Enter year.\n")
            items.append(DVD(title,year))
        elif newItem.upper() == "BOOK":
            title = input("Enter title.\n")
            year = input("Enter year.\n")
            items.append(Book(title,year))
        else:
            print("Action not recognised, please try again.")
        newItem = input("Enter 'DVD', 'BOOK' or 'NONE' to register an item.\n")
    return(items)

def readInfo(items):
    for i in range(len(items)):
        currentI = items[i]
        currentI.details()

if __name__ == "__main__":
    readInfo(registerItems())

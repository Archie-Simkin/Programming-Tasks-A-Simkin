"""
TASK: 02 File-Backed Address Book

# Storing contacts in a JSON file.
Supports:
- Add
- Delete
- Update
- Show all
Upload the JSON file to Git

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""
import json

filename = "week9_02_contacts.json"
with open(filename, "r") as file:
    contacts = json.load(file)

def addContact():
    while True:
        try:
            name = input("Enter name of person to add.\n")
            email = input("Enter email.\n")
            phoneNum = input("Enter phone number.\n")
            contacts[name] = {"email": email, "phoneNumber": phoneNum}
            break
        except:
            print("Error, please try again.")

def removeContact():
    name = input("Enter name of person to remove.\n")
    contacts.pop(name)

def updateJSON(filename):
    with open(filename, "w") as file:
        file.write(json.dumps(contacts, indent=4))

def showAll():
    for row in contacts:
        data = contacts[row]
        keys = list(contacts[row].keys())
        print(f"{row} - Email: {data[keys[0]]}    Phone Number: {data[keys[1]]}")

if __name__ == "__main__":
    addContact()
    updateJSON(filename)
    showAll()
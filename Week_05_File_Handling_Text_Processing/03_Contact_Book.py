"""
TASK: 03 Contact Book

# Store contacts in a text file, each line containing
name,phone,email
Program must allow:
- Add contact
- Search contact (sequential search)
- Display all

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def addContact(filename):
    name = input("Enter name.\n")
    phoneNum = input("Enter phone number.\n")
    email = input("Enter email.\n")
    with open(filename, "a") as file:
        file.write(name+","+phoneNum+","+email+"\n")

def viewContact(filename):
    with open(filename, "r") as file:
        content = file.read()
        return(content.strip("\n"))

def searchContact(filename, name):
    with open(filename, "r") as file:
        for line in file:
            details = line.split(",")
            details[2] = details[2].strip("\n")
            name = name.replace(" ", "")
            details[0] = details[0].replace(" ", "")
            if details[0].upper() == name.upper():
                return(details[1],details[2])
        return(-1, -1)


def menu(action):
    filename = "contacts.txt"
    while action.upper() != "NONE":
        if action.upper() == "ADD":
            print(addContact(filename))
        elif action.upper() == "VIEW":
            print(viewContact(filename))
        elif action.upper() == "SEARCH":
            phoneNum, email = searchContact(filename, input("Enter a name to search for.\n"))
            if phoneNum != -1:
                print("Phone number: " + phoneNum + "\nEmail: " + email)
            else:
                print("Not found")
        else:
            print("Action not recognised, please try again.")
        action = input("Choose an action: 'add', 'view', 'search' or 'none'.\n")

if __name__ == "__main__":
    menu(input("Choose an action: 'add', 'view', 'search' or 'none'.\n"))
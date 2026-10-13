"""
TASK: 02 Simple Logger System

# Create a script that appends time-stamped log entries to a file.
Menu:
- Add Log
- View Log
- Clear Log

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""
import datetime

def addLog(filename):
    with open(filename, "a") as file:
        timestamp = str(datetime.datetime.now())
        log = input("Enter log\n")
        log = timestamp[:16].replace("-", "/") + ": " + log + "\n"
        file.write(log)
        return(log)

def viewLog(filename):
    with open(filename, "r") as file:
        content = file.read()
        return(content.strip("\n"))

def clearLog(filename):
    with open(filename, "w") as file:
        file.write("")
        return("Cleared logs.")

def menu(action):
    filename = "logs.txt"
    while action.upper() != "NONE":
        if action.upper() == "ADD":
            print(addLog(filename))
        elif action.upper() == "VIEW":
            print(viewLog(filename))
        elif action.upper() == "CLEAR":
            print(clearLog(filename))
        else:
            print("Action not recognised, please try again.")
        action = input("Choose an action: 'add', 'view', 'clear' or 'none'.\n")

if __name__ == "__main__":
    menu(input("Choose an action: 'add', 'view', 'clear' or 'none'.\n"))
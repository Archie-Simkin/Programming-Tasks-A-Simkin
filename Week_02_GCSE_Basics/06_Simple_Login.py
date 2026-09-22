"""
TASK: 06 Simple Login

# Skills: Selection, string comparison
Start with a correct username/password (extend if saved in a text file separately):
- Ask for login
- Print "Welcome" or "Access Denied {number} attempts remaining"
Only allow 3 attempts and close the file

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

import os

def login(inputU, inputP):
    with open(file_path, "r") as f:
        f.seek(0)
        correctU = f.readline()
        correctP = f.readline()
        if inputU == correctU.strip("\n"):
            if inputP == correctP:
                return("C")
        else:
            return("W")

for i in range(0,3):
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, 'credentials.txt')
    response = login(input("Enter your username.\n"), input("Enter your password.\n"))
    if response == "W":
        if i < 2:
            print("Incorrect, please try again.")
        else:
            print("Incorrect, you are now locked out.")
    elif response == "C":
        print("Logging in...")
        break
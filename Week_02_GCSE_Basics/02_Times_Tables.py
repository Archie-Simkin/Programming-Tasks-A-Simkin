"""
TASK: 02 Times Tables

# Skills: Loops,input validation
Ask the user for a number, print the multiplication from 1 to 12 in a readable format:

Extend by using a function you can call for easy entry

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def times_tables(num):
    for i in range(1,13):
        print(str(num) + " × " + str(i) + " = " + str(num*i))



if __name__ == "__main__":
    try:
        times_tables(int(input("Enter an integer.\n")))
    except:
        print("Input must be an integer.")

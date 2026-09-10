"""
TASK: 03 Array Reversal

# Array Reversal
Create a program that:
- Generates a list of random integers.
- Reverses the list manually (no slicing or .reverse).
- Includes a function `reverse_list(values)` that returns a new reversed list.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

import random

def main(length):
    for j in range(length):
        v.append(random.randint(1,100))
    return(v)

def reverse_list(values):
    revList = []
    for i in range(len(values)-1,-1,-1):
        revList.append(values[i])
    return(revList)

if __name__ == "__main__":
    v = []
    v = main(int(input("How many items in list?\n")))
    print(v)
    print(reverse_list(v))
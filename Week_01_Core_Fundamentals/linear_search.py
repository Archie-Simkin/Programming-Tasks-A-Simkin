"""
TASK: 04 Linear Search

# Linear Search
Implement a linear search algorithm:
- Ask the user for a target value.
- Search a generated random list.
- Return the index or -1.
- Include `linear_search(values, target)`.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

import random

def linear_search(values, target):
    for i in range(0,len(values)):
        x = str(values[i])
        if x == target:
            return(i)
    return(-1)


def randomise(length):
    for j in range(length):
        v.append(random.randint(1,20))
    return(v)



if __name__ == "__main__":
    v = []
    v = randomise(int(input("How many items in list?\n")))
    print(v)
    print(linear_search(v,input("What is your target?\n")))
"""
TASK: 01 Bubble Sort

# Bubble Sort
Implement Bubble Sort on any size list:
- Do not use built-in sort()
- Count swaps
- Extend by

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""
import random

def initArray(items):
    matrix = []
    for i in range(items):
        matrix.append(random.randint(1,25))
    return(matrix)

def bubble(list):
    counter = len(list)
    for i in range(len(list)):
        for j in range(counter-1):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
        counter -= 1
    return(list)

if __name__ == "__main__":
    matrix = initArray(12)
    print(matrix)
    print(bubble(matrix))

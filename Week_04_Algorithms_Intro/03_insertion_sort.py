"""
TASK: 03 Insertion Sort

# Insertion Sort Tester
Generate an unsorted list (maybe use RNG). Implement:
- Insertion sort without using inbuild sorts
- Count number of comparions
Then benchmark them with random inputs.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""
import random

def initArray(items):
    uList = []
    sList = []
    for i in range(items):
        uList.append(random.randint(1,25))
        sList.append("")
    return(uList,sList)

def insertSort(uList,sList):
    for i in range(len(uList)):
        lower = 0
        pointer = 0
        for j in range(len(uList)):
            if uList[i] > uList[j]:
                lower += 1
        while sList[lower - pointer] != "":
            pointer += 1
        sList[lower - pointer] = uList[i]
    return(sList)

if __name__ == "__main__":
    u,s = initArray(12)
    print(u)
    print(insertSort(u, s))
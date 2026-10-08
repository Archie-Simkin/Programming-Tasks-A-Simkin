"""
TASK: 02 Binary Search Tester

# Binary Search Tester
Generate a sorted list. Implement:
- iterative binary search
- recursive binary search
Then benchmark them with random inputs.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""
import random

def initArray(items):
    matrix = []
    for i in range(items):
        matrix.append(random.randint(1,25))
    return(bubble(matrix))

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

def iSearch(list,value):
        high = len(list)-1
        low = 0
        while high >= low:
            mid = (high + low) // 2
            if list[mid] == value:
                return("Found")
            elif list[mid] < value:
                low = mid + 1
            elif list[mid] > value:
                high = mid - 1
        return("Value not found")

def rSearchInit(list,value):
        high = len(list)-1
        low = 0
        return(rSearch(list,value,high,low))

def rSearch(list,value,high,low):
    if low > high:
        return("Value not found")
    mid = (low + high) // 2
    if list[mid] == value:
        return("Found")
    elif list[mid] < value:
        return(rSearch(list,value,high,mid+1))
    elif list[mid] > value:
        return(rSearch(list,value,mid-1,low))

if __name__ == "__main__":
    list = initArray(12)
    print(list)
    value = int(input("Enter a value to search for\n"))
    print(iSearch(list,value))
    print(rSearchInit(list,value))



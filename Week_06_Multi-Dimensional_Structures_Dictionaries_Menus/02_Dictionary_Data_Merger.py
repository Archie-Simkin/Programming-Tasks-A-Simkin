"""
TASK: 02 Dictionary Data Merger

# Please refer to the python file with dictionaries in
Given two dictionaries:
- Merge them by summing matching keys
- Present them to the user

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

from Dictionary_File import furniture_stock
from Dictionary_File import supermarket_stock

def merge(dict1, dict2):
    return(dict1 | dict2)

def presentDict(dict1):
    for i in dict1:
        output = ""
        temp = dict1[i].copy()
        for j in temp:
            output = output + j.capitalize() + " : " + str(temp[j]) + ", "
        print(i + " - " + output.strip(", "))

if __name__ == "__main__":
    merged = merge(supermarket_stock, furniture_stock)
    presentDict(merged)
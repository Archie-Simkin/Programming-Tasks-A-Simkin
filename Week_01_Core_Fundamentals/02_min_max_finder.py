"""
TASK: 02 Min Max Finder

# Min/Max Finder
Write a program that:
- Accepts a list of integers.
- Manually finds the min and max (no built-in min/max).
- Includes a function `find_min_max(values)` returning `(min_value, max_value)`.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main(values):
    x = True
    while x == True:
        try:
            num = int(input())
        except:
            print("Input must be an integer")
        else:
            values.append(num)
            if input("Would you like to input another number? Y/N\n").upper() == "N":
                x = False
    return(values)

def find_values(values):
    minm = values[0]
    maxm = values[0]
    for i in range(0,len(values)):
        if values[i] > maxm:
            maxm = values[i]
        if values[i] < minm:
            minm = values[i]
    return(str(minm) + ', ' + str(maxm))

if __name__ == "__main__":
    v = []
    v = main(v)
    print(find_values(v))
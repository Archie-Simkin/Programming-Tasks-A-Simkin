"""
TASK: 01 Average Calculator

# Average Calculator
Write a Python program that:
- Prompts the user for a list of numbers.
- Stores them in a 1D list.
- Calculates the mean *without using built-in statistics libraries*.
- Includes input validation.
- Implements a reusable function: `calculate_average(values)`.

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


def calc_average(values):
    total = 0
    for i in range(0,len(values)):
        total = total + values[i]
    return(total/len(values))



if __name__ == "__main__":
    v = []
    coolList = main(v)
    print(calc_average(coolList))
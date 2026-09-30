"""
TASK: 02 Dice Roll

# Skills: RNG, Loops
Simulate rolling a six-sided die X number of times:
Print each roll, store all values in a list of updated totals for each number (56 ones for example):
Allow the user to print:
- Totals for each side
- average dice roll
- Counts for each of the 6 sides
- Extend (look up how to use mathplotlib and produce a bar graph for all of the statistics)

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

import random

def roll(trials):
    output = ""
    totals = [0, 0, 0, 0, 0, 0]
    average = 0
    for i in range(trials):
        currentRoll = random.randint(1,6)
        output += str(currentRoll) + ", "
        totals[currentRoll - 1] += 1
        average += currentRoll
    return(output.strip(", "),totals,(average/trials))


if __name__ == "__main__":
    error = True
    while error == True:
        try:
            allRolls,totals,average = roll(int(input("How many rolls?\n")))
        except:
            print("Error, input must be an integer.")
        else:
            error = False
            print("All rolls: " + allRolls)
            for i in range(0,6):
                print(str(i+1) + "s: " + str(totals[i]))
            for i in range(0,6):
                print("Total for " + str(i+1) + "s: " + str(totals[i]*(i+1)))
            print("Average roll: " + str(average))
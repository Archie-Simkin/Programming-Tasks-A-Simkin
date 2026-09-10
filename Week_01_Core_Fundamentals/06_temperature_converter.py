"""
TASK: 06 Temperature Converter

# Temperature Converter
Build a converter tool:
- Convert Celsius <-> Fahrenheit.
- Provide a looped menu.
- Validate user input.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def convertC(n):
    return((n-32)/1.8)

def convertF(n):
    return((n*1.8)+32)

def convertChoice(value):
    ch = input("Would you like to convert your value into Celsius or Farenheit? (C or F)\n")
    if ch.upper() == "C":
        return(str(convertC(value))+"°C")
    elif ch.upper() == "F":
            return(str(convertF(value))+"°F")
    else:
        print("Choice not understood, please try again.")

if __name__ == "__main__":
    x = True
    while x == True:
        try:
            num = float(input("What is your value?\n"))
        except:
            print("Input must be an number.")
        else:
            print(convertChoice(num))
            if input("Would you like to do another conversion? Y/N\n").upper() == "N":
                x = False
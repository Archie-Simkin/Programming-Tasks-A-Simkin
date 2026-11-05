"""
TASK: 05 Json Writer Reader

# Do some research into JSON
Prompt user for:
- Name
- Price
- Quantity
Store items into a JSON file with proper formatting
Then allow the user to open and convert to list of dictionaries and output the summary with averages.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

import json

fName = "json_week06.json"

def inputData(filename, dict1):
    while True:
        try:
            name = input("Enter name of item.\n")
            price = float(input("Enter price.\n"))
            quantity = int(input("Enter quantity.\n"))
            dict1[name] = {"price": price, "quantity": quantity}
            print(dict1)
            option = input("(A) Append to data more\nOR\n(B) Write to file\n")
            if option.upper() == "B":
                break
        except:
            print("Wrong data type, please re-enter.")
    content = json.dumps(dict1, indent=4)
    with open(filename, "w") as file:
        file.write(content)
        return(calcAverage(dict1))

def calcAverage(dict1):
    totalStock = 0
    totalPrice = 0
    for i in dict1:
        details = dict1[i]
        keys = list(dict1[i].keys())
        totalPrice = details[keys[0]]
        totalStock = details[keys[1]]
    return(totalStock / len(dict1), totalPrice / len(dict1))

def readJSON(filename):
    with open(filename, "r") as file:
        dict1 = json.load(file)
        return(dict1)


data = readJSON(fName)

avgStock, avgPrice = inputData(fName, data)
print("Average price: " + str(avgPrice) + "\nAverage stock: " + str(avgStock))
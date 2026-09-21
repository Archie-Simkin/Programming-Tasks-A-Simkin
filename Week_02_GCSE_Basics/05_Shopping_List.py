"""
TASK: 05 Shopping List

# Skills: Loops, lists
Allow the user to add itemds to a shopping list until they type DONE
When they type DONE, print the list and ask if they want to edit any item.
They should select an item by number and allow them to ammend the item.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def addItems(item,sList):
    while item.upper() != "DONE":
        item = input("What item would you like to add to the list?\nEnter 'DONE' if you would not like to add any more.\n")
        if item.upper() != "DONE":
            sList.append(item)
    return(sList)



if __name__ == "__main__":
    error = True
    while error == True:
        try:
            sList = addItems("",[])
            for i in range(0, len(sList)):
                print(str(i+1) + ": " + sList[i])
            choice = "Y"
            while choice.upper != "N":
                choice = input("Edit any items? (Y/N)\n")
                if choice.upper != "N":
                    index = int(input("Enter the number of the item you would like to edit.\n")) - 1
                    sList[index] = input("What would you like to change it to?\n")
                    for i in range(0, len(sList)):
                        print(str(i+1) + ": " + sList[i])

        except:
            print("An error occurred, try again.\n")
        else:
            error = False
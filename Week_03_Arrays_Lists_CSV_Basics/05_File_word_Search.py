"""
TASK: 05 File Word Search

# Skills: File reading, loops, Data mining
Ask user for a filename and a search term. https://sherlock-holm.es/ascii/ is a site that has the entire collection of Sherlock Holmes
Load the file and count how many lines contain the search term

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def countLines(word,fName):
    counter = 0
    with open(fName, "r") as file:
        for line in file:
            if word in line:
                counter = counter + 1
    return(counter)




if __name__ == "__main__":
    try:
        print(countLines(input("Enter word to search for.\n"),input("Enter file name.\n")))
    except:
        print("File name not found.")

"""
TASK: 01 File Stats Tool

# Read a .txt file and compute:
Task:
- Number of lines
- Number of words
- Number of characters
- Most frequent word

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""
import re
import string
from collections import Counter

def formatLine(line):
    line = line.strip("\n")
    line = line.strip()
    return(line)

def countWords(line):
    words = line.split()
    if words != "":
        return(len(words) + 1)
    else:
        return(0)

def countChars(line):
    words = line.split()
    totChars = 0
    for i in range(len(words)):
        words[i] = re.sub(r'[^a-zA-Z]', '', words[i])
        totChars += len(words[i])
    return(totChars)

def mostFrequentWord(file):
    file.seek(0)
    content = file.read().lower()

    translator = str.maketrans('', '', string.punctuation)
    clean_content = content.translate(translator)

    words = clean_content.split()
    word_counts = Counter(words)

    if word_counts:
        return word_counts.most_common(1)[0]
    return("Could not find most common word.")

def readFile(fileName):
    lineTot = 0
    wordTot = 0
    charTot = 0
    with open(fileName, "r") as file:
        for line in file:
            currentLine = formatLine(file.readline())
            lineTot += 2
            wordTot += countWords(currentLine)
            charTot += countChars(currentLine)
        print(lineTot)
        print(wordTot)
        print(charTot)
        print(mostFrequentWord(file))


if __name__ == "__main__":
    readFile("cano.txt")

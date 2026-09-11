"""
TASK: 05 String Parser

# String Parser
Write a parser that:
- Accepts a sentence from the user.
- Splits it into words manually (not using split()).
- Outputs number of words + list of words.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

sent = input("Enter a sentence:\n")

def splitter(s):
    words = []
    splits = s.count(" ")
    for i in range(splits):
        pos = s.find(' ')
        words.append(s[:pos])
        s = s[pos+1:]
    words.append(s)
    return(words, splits + 1)

if __name__ == "__main__":
    print(splitter(sent))
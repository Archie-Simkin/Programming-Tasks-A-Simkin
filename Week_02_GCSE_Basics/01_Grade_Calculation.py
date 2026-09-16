"""
TASK: 01 Grade Calculation

# Skills: Input, output, selection
Write a program that asks the user for a percentage grade and prints the corresponding letter grade:
- A: 80-100
- B: 60-79
- C: 40-59
- D: <40
Include a function def get_grade(score):

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def get_grade(score):
    if score >= 80 and score <= 100:
        return("A")
    elif score >= 60 and score < 80:
        return("B")
    elif score >= 40 and score < 60:
        return("C")
    elif score < 40:
        return("D")
    else:
        return("Grade must be a percentage out of 100.")




if __name__ == "__main__":
    try:
        print(get_grade(int(input("What is your percentage grade?\n"))))
    except:
        print("Grade must be a percentage out of 100.")

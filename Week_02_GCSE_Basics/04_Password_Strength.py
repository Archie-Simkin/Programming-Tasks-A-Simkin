"""
TASK: 04 Password Strength

# Skills: Strings, loops, selection
Ask the user to enter a password, and check that they meet these conditions:
- At least 8 characters
- Contains a number
- Contains a captial and lower cased letter
- Extend for one special character
Print a response of weak, medium or strong for how many they pass.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def test_strength(password):
    strength = 4
    if len(password) < 8:
        print("Password should be at least 8 characters long.")
        strength = strength - 1
    if password.lower() == password or password.upper() == password:
        print("Password should contain an uppercase and lowercase letter.")
        strength = strength - 1
    if password.isalnum() == True:
        if password.isalpha() == True:
            print("Password should contain a number.")
            strength = strength - 1
        print("Password should contain a special character.")
        strength = strength - 1
    return(strength)



if __name__ == "__main__":
    totalStrength = test_strength(input("Please enter a password.\n"))
    if totalStrength == 4:
        print("This password is strong.")
    elif totalStrength <= 1:
        print("This password is weak.")
    else:
        print("This password has medium strength.")

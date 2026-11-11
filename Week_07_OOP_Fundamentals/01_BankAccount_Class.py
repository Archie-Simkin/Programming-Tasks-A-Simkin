"""
TASK: 01 Bankaccount Class

# Skills - https://www.w3schools.com/python/python_oop.asp Highly recommend you visit this site.
Create class with the following attributes:
- Owner
- Balance
- Log
With the following methods:
- deposit()
- withdraw() with validation or an overdraft validation
- get_balance()
- get_log() of all transactions

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
        self.log = []

    def deposit(self):
        try:
            value = abs(float(input("How much would you like to deposit.\n")))
            self.balance += value
            self.log.append("Deposited £" + str(value) + " into account.")
        except:
            print("Input must be a number.")

    def withdraw(self):
        try:
            value = abs(float(input("How much would you like to withdraw?\n")))
            self.balance -= value
            self.log.append("Withdrew £" + str(value) + " from account.")
        except:
            print("Input must be a number.")

    def getBalance(self):
        print("Your balance is £" + str(self.balance))

    def getLog(self):
        print("Transaction log:")
        for i in range(len(self.log)):
            print(self.log[i])

def inputData():
    name = input("Enter name.\n")
    while True:
        try:
            balance = float(input("Enter balance.\n"))
            break
        except:
            print("Input must be a number.")
    account = BankAccount(name, balance)
    return(account)


def menu(account, action):
    while action.upper() != "NONE":
        if action.upper() == "DEPOSIT":
            account.deposit()
        elif action.upper() == "WITHDRAW":
            account.withdraw()
        elif action.upper() == "GET BALANCE":
            account.getBalance()
        elif action.upper() == "GET LOG":
            account.getLog()
        else:
            print("Action not recognised, please try again.")
        action = input("Choose an action: 'deposit', 'withdraw', 'get balance', 'get log' or 'none'.\n")


if __name__ == "__main__":
    menu(inputData(), input("Choose an action: 'deposit', 'withdraw', 'get balance', 'get log' or 'none'.\n"),)

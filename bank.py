import numpy as np
import random


class bank:
    def __init__(self, name, accountnum):
        self.balance = 0
        self.name = name
        self.accountnum = accountnum

    def deposit(self, money):
        if money >= 0:
            self.balance = self.balance + money
            return self.balance
        if money < 0:
            raise ValueError("can't deposite negative money")

    def withdraw(self, money):
        if money < 0:
            raise ValueError("can't withdraw negative money")
        elif self.balance - money < 0:
            print("too little money in account")
            return -1
        else:
            self.balance = self.balance - money
            return self.balance

    def printbal(self):
        print(self.balance)
        return self.balance

    def printname(self):
        print(self.name)
        return self.name
    
    def getaccountnum(self):
        return self.accountnum
    

    def gamble(self):
        while self.balance > 0:
            print("balance:" + str(self.balance))
            wager = int(input("how much are you betting? bet -1 to leave."))
            if wager == -1:
                break
            if wager > self.balance:
                print("stop trying to cheat ._.")
                break
            bet = int(input("bet your number between 1-33:"))
            if bet < 1 or bet > 33:
                print("number outside")
                break
            number = random.randint(1, 33)
            if number == bet:
                print("WINNN")
                self.balance = self.balance + 5 * wager
            elif number % 2 == bet % 2:
                print("win yay")
                self.balance = self.balance + wager
            else:
                print("rip")
                self.balance = self.balance - wager


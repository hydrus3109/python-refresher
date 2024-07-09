import numpy as np


class bank:
    def __init__(self, balance, name, accountnum):
        self.balance = balance
        self.name = name
        self.accountnum = accountnum

    def deposit(self, money):
        if money >= 0:
            self.balance = self.balance + money
            return self.balance
        if money < 0:
            print("can't deposite negative money")
            return "can't deposite negative money"

    def withdraw(self, money):
        if money < 0:
            print("can't withdraw negative money")
            return "can't withdraw negative money"
        elif self.balance - money < 0:
            print("too little money in account")
            return "too little money in account"
        else:
            self.balance = self.balance - money
            return self.balance

    def printbal(self):
        print(self.balance)
        return self.balance


def hello():
    print("Hello, world!")


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        raise ValueError("Can't divide by zero!")
    return a / b


# def sqrt(a):
#     return np.sqrt(a)


# def power(a, b):
#     return np.power(a, b)


# def log(a):
#     return np.log(a)


# def exp(a):
#     return np.exp(a)


def sin(a):
    return np.sin(a)


def cos(a):
    return np.cos(a)


# def tan(a):
#     return np.tan(a)


def cot(a):
    return 1 / np.tan(a)


def __main__():
    hello()


if __name__ == "__main__":
    __main__()

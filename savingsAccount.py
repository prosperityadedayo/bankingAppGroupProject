from account import Account

class SavingsAccount(Account):
    def __init__(self, balance):
        Account.__init__(self, balance)

    def withdraw(self, amount, limit = 1000):
        if amount < limit:
            super().withdraw(amount)
        else:
            print("Amount exeeds withdrawal limit")

    def deposit(self, amount):
        super().deposit(amount)

savings = SavingsAccount(10000)

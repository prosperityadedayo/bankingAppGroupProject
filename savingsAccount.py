from account import Account

class SavingsAccount(Account):
    def __init__(self, balance):
        Account.__init__(self, balance)

    def withdraw(self, amount, limit):
        if(amount < limit):
            super().withdraw(amount)
        else:
            print("Amount exeeds withdrawal limit")

    def deposit(self, amount):
        super().withdraw(amount)

savings = SavingsAccount(10000)
savings.withdraw(200, 1000)
print(savings.balance)
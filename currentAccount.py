from account import Account

class CurrentAccount(Account):
    def _init_(self, balance):
        Account.__init__(self, balance)

    def withdraw(self, amount):
            super().withdraw(amount)

    def deposit(self, amount):
            super().deposit(amount)

current = CurrentAccount(100000)

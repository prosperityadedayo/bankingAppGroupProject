from account import Account

class CurrentAccount(Account):
    def _init_(self, balance):
        Account._init_(self, balance)

    def withdraw(self, amount):
            super().withdraw(amount)

current = CurrentAccount(100000)
current.withdraw(0)
print(current.balance)
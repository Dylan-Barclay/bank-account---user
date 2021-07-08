from bank_account import BankAccount

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = .01, balance = 0)

    def make_deposit(self, amount):
        self.account.balance += amount
        return self

    def make_withdraw(self, amount):
        self.account.balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account}")
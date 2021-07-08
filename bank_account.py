class BankAccount():
    
    def __init__(self, int_rate = .01, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print('Decline')
            return self
        else:
            self.balance -= amount
            return self

    def display_account_info(self):
        print(self.balance)
        return self

    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return(f'New balance is {self.balance}') 

    def __str__(self):
        return f'{self.balance}'
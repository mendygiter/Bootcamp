class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        self.int_rate = int_rate
        self.balance = balance
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self


    def display_account_info(self):
        print (f'current_balance = {self.account_balance}')
        return self

    def yield_interest(self):
        self.balance += 
        return self


account1 = BankAccount('')
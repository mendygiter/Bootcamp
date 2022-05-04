class BankAccount:

    def __init__(self, int_rate = .01, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance <= 0:
            print('Insufficent funds: Charging a $5 fee')
            self.balance -= 5
            return self

        self.balance -= amount
        return self

    def display_account_info(self):
        print(f'balance: = {self.balance}')
        return self

    def yield_interest(self):
        if self.balance > 0:
            x = self.balance * self.int_rate
            self.balance += x
        return self





account1 = BankAccount()
account2 = BankAccount()


account1.deposit(100).deposit(10000).deposit(356124).yield_interest().display_account_info()
account2.deposit(1467463).deposit(1455625).withdraw(564).withdraw(55632).withdraw(563).withdraw(4525).yield_interest().display_account_info()












#     # don't forget to add some default values for these parameters!
#     def __init__(self, int_rate, balance): 
#         # your code here! (remember, instance attributes go here)
#         self.int_rate = int_rate
#         self.balance = balance
#         # don't worry about user info here; we'll involve the User class soon
#     def deposit(self, amount):
#         self.balance += amount
#         return self

#     def withdraw(self, amount):
#         self.balance -= amount
#         return self


#     def display_account_info(self):
#         print (f'current_balance = {self.account_balance}')
#         return self

#     def yield_interest(self):
#         self.balance += 
#         return self 


# account1 = BankAccount('')
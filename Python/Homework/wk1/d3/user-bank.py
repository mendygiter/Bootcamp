class user:
#attributes
    def __init__(self, name, email, account_balance):
        self.name = name
        self.email = email
        self.account = BankAccount(balance = 0)

#methods
    def make_withdrawal(self, number):
        self.account.balance -= number
        return self

    def user_balance (self):
        print (f'current_balance = {self.account.display_account_info}') 
        return self

    def make_deposit(self, amount):
        self.account.balance += amount
        return self





#instance
user1 = user("Mendy Giter", "mg@mg.com", 5000000)
user2 = user("Rochel Giter", "rg@rg.com", 1000000)
user3 = user("Ilana Giter", "il@il.com", 10000000)





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



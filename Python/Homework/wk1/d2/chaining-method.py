class user:
#attributes
    def __init__(self, name, email, account_balance):
        self.name = name
        self.email = email
        self.account_balance = account_balance

#methods
    def make_withdrawal(self, number):
        self.account_balance -= number
        return self
    def user_balance (self):
        print (f'current_balance = {self.account_balance}') 
        return self
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
#instance
user1 = user("Mendy Giter", "mg@mg.com", 5000000)
user2 = user("Rochel Giter", "rg@rg.com", 1000000)
user3 = user("Ilana Giter", "il@il.com", 10000000)

#doing thing with instance
#print (user1.account_balance) Doing it like this doesnt print our print statement on line 13 it just gets our account balance from our instance
user1.make_deposit(15463).make_deposit(6767345).make_deposit(4543).make_withdrawal(45678).user_balance()

user2.make_deposit(15463).make_deposit(6767345).make_withdrawal(4543).make_withdrawal(45678).user_balance()

user3.make_deposit(124567876).make_withdrawal(6767345).make_withdrawal(456543).make_withdrawal(45456678).user_balance()
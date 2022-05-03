class user:
#attributes
    def __init__(self, name, email, account_balance):
        self.name = name
        self.email = email
        self.account_balance = account_balance

#methods
    def make_withdrawal(self, number):
        self.account_balance -= number
        
    def user_balance (self):
        print (f'current_balance = {self.account_balance}') 

    def make_deposit(self, amount):
        self.account_balance += amount

#instance
user1 = user("Mendy Giter", "mg@mg.com", 5000000)
user2 = user("Rochel Giter", "rg@rg.com", 1000000)
user3 = user("Ilana Giter", "il@il.com", 10000000)

#doing thing with instance
#print (user1.account_balance) Doing it like this doesnt print our print statement on line 13 it just gets our account balance from our instance
user1.make_deposit(15463)
user1.make_deposit(6767345)
user1.make_deposit(4543)
user1.make_withdrawal(45678)
user1.user_balance()

user2.make_deposit(15463)
user2.make_deposit(6767345)
user2.make_withdrawal(4543)
user2.make_withdrawal(45678)
user2.user_balance()

user3.make_deposit(124567876)
user3.make_withdrawal(6767345)
user3.make_withdrawal(456543)
user3.make_withdrawal(45456678)
user3.user_balance()





# class Employee():

#     def __init__(self, first_name, last_name, salary, middle_name = None):
#         self.first_name = first_name
#         self.middle_name = middle_name
#         self.last_name = last_name
#         self.salary = salary

#     def full_name(self):
#         if self.middle_name == None:
#             return f"{self.first_name} {self.last_name}"
#         else:
#             return f"{self.first_name} {self.middle_name} {self.last_name}"

#     def change_salary(self, percent_increase):
        
#         if percent_increase > 10:
#             return None

#         new_salary = self.salary * (1 + (.01 * percent_increase))

#         if not new_salary < 40000:
#             self.salary = new_salary


# employee_1 = Employee("Alex", "Smith", 82000)
# employee_2 = Employee("Bradley", "Jones", 79000)
# employee_3 = Employee("Charlie", "Adams", 65000)
# employee_4 = Employee("Darla", "Smith", 85000, middle_name = "Allison")
# employee_5 = Employee("Eric", "Smith", 40000)

# employees = [employee_1, employee_2, employee_3, employee_4, employee_5]

# for employee in employees:
#     print(f"Full name: {employee.full_name()}, salary: {employee.salary}")

# for employee in employees:
#     employee.change_salary(-3)
#     # call method to change salary

# for employee in employees:
#     print(f"Full name: {employee.full_name()}, salary: {employee.salary}")
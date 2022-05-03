from unicodedata import name


class Employee():

    def _init_(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

employee_1 = Employee('Alex', 'Smith', 82000)


for employee in employees:
    print(f'First name: {employee.first_name}')
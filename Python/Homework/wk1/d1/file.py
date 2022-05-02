num1 = 42 # variable declaration
num2 = 2.3 # variable declaration
boolean = True #Boolean
string = 'Hello World' #Strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable declaration
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration
print(type(fruit)) #- log statement
print(pizza_toppings[1]) #log statement
pizza_toppings.append('Mushrooms') #add value
print(person['name']) #log statement
person['name'] = 'George' #variable declaration
person['eye_color'] = 'blue' #variable declaration
print(fruit[2]) #log statement

if num1 > 45: #if statement
    print("It's greater") #- log statement
else: #else
    print("It's lower") #log statement

if len(string) < 5:# conditional
    print("It's a short word!") # log statement
else if len(string) > 15: #conditionl
    print("It's a long word!")# log statement
else:# conditional
    print("Just right!") #log statement

for x in range(5): #for loop
    print(x) #log statement
for x in range(2,5): #for loop
    print(x) # log statement
for x in range(2,10,3): #for loop   
    print(x) #log statement
x = 0 # variable decleration
while(x < 5):# while loop
    print(x)# log statment
    x += 1 # var decleration

pizza_toppings.pop() #delete value
pizza_toppings.pop(1) #delete value

print(person) # log statement
person.pop('eye_color') #delete value
print(person) #log statement

for topping in pizza_toppings: #for loop
    if topping == 'Pepperoni': #conditional
        continue #forloop
    print('After 1st if statement') #log statment
    if topping == 'Olives': #for loop
        break #for loop

def print_hello_ten_times(): #function
    for num in range(10): #forloop
        print('Hello')#log statement

print_hello_ten_times() #logstatement

def print_hello_x_times(x) #functio 
    for num in range(x): #forloop
        print('Hello') # log statement

print_hello_x_times(4) #log statment

def print_hello_x_or_ten_times(x = 10): #function
    for num in range(x): #for loop
        print('Hello') #log statment

print_hello_x_or_ten_times() #function
print_hello_x_or_ten_times(4)#function


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)
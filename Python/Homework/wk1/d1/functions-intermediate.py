names = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]

names[0]['last_name']= 'Bryant'
print(names)


sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory ['soccer'] [0] = 'Andres'

print(sports_directory)

z = [{'x': 10, 'y': 20}]

z ('y' [1])  = 30
print(z)


# iterate trough list of functions
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


for student in students:
    print(student)


# iterate through a dictionary with list values
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


print(str(len(dojo['locations'])) + ' locations')

for x in range(len(dojo['locations'])):
    print(dojo['locations'][x])

print(str(len(dojo['instructors'])) + ' instructors')

for x in range(len(dojo['instructors'])):
    print(dojo['instructors'][x])
# Print all integers from 0 to 150.
for count in range(0,150):
    print(count)

#Print all the multiples of 5 from 5 to 1,000
for count in range(5,1000,5):
    print(count)

# Counting, the Dojo Way
for count in range(1,100):
    if count % 10  == 0:
        print('Coding Dojo')
    elif count % 5 == 0:
        print('Coding')

#countdown by fours
for count in range(2018,4,-4):
    print(count)

#woah suckers huge
sum = 0
for count in range(1,500000,2):
    if count % 2 != 0:
        sum += count
print (sum)

#flexible counter
lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum, highNum + 1):
    if(i % mult == 0):
        print(i)



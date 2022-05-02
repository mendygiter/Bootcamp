name = "zen"
print("My name is", name)

def sample_function_name(input_list):
    output_list = []

    for x in input_list:
        if x >= 0:
            output_list.append(x)
    return output_list

print(sample_function_name([1, -3, 9, -2, 7]))


from random import randint

def roll_dice(number, side):
    result = 0

    for i in range(0, number):
        result += randint(1, side)

    return result

print(roll_dice(2, 20))


fruits = ['apple', 'banana', 'orange', 'strawberry']
vegetables = ['lettuce', 'cucumber', 'carrots']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)
salad = 3 * vegetables
print(salad)


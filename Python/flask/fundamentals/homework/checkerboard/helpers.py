from unittest import result


def generate_checkerboard(x,y):
    result = []

    for j in range(0,y):
        temp = []
        for i in range (0,x):
            temp.append((i + j) % 2)
        result.append(temp)
    
    return result

result = generate_checkerboard(12, 12)

for row in result:
    print(row)
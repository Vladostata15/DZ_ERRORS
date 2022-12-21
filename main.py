result = []
def divider (a, b):
    if a < b:
        raise ValueError('The first number is the smallest then second!')
    if b > 100:
        raise IndexError('The second number is bigger then 100!')
    if b == 0:
        raise ZeroDivisionError('You can`t divide by 0!')

    return a/b

data = {10: 2,
        2: 5,
        123: 4,
        18: 0,
        8: 4}


for key in data:
    res = divider(key, data[key])
    result.append(res)

print(result)




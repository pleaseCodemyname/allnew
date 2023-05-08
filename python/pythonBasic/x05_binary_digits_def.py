import random

def bDigits(n):
    binary_digits = []
    while True:
        x = random.sample(range(4, 17), 1)[0]
        binary_digits.append\
            .(x % 2)
        if x // 2 == 0:
            break
        else:
            x = x // 2
    return list(reversed(binary_digits))

n = random.randint(4, 16)
result = bDigits(n)
print(f'{n} binaryDigits = {result}')

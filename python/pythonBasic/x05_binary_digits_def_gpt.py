#GPT
import random

def bDigits(n):
    binary_digits = []
    while n // 2 != 0:
        x = random.sample(range(4, 16), 1)[0]
        binary_digits.append(x % 2)
        n = n // 2
    binary_digits.append(n % 2)
    return binary_digits[::-1]

n = random.randint(4, 16)
result = bDigits(n)
print(f'{n} binary number is : {result}')
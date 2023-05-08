#GPT
import random

class BDigits(object):
    def __init__(self, n):
        self.n = n

    def bDigits(self):
        binary_digits = []
    while self.n // 2 != 0:
        n = random.sample(range(4, 16), 1)[0]
        binary_digits.append(n % 2)
        self.n = self.n // 2
        binary_digits.append(self.n % 2)
        return binary_digits[::-1]

n = random.randint(4, 16)
number = BDigits(n)
print(f'{n} binary number is : {number.bDigits()}')
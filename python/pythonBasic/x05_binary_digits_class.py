import random
# 제가 할
class BDigits(object):
    def __init__(self, n):
        self.n = n

#몫이 0이 될때까지 계속 나눠야하는게 맞음
    def bDigits(self):
        n = random.sample(range(4, 17), 1)[0]
        if self.n // 2 == 0:

        else:
            return n % 2

BDigits(n)
print(f'{n} binaryDigits = {bDigits()}')



class Calculate(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return 'add result : %d' % result

    def sub(self):
        result = self.first - self.second
        return 'sub result : %d' % result

    def mul(self):
        result = self.first * self.second
        return 'mult result : %d' % result

    def div(self):
        if self.second == 0:
            self.second = 5
        result = self.first / self.second
        return 'div result : %.3f' % result

calc = Calculate(14, 0)

print(calc.add()) # add result : 14
print(calc.sub()) # sub result : 14
print(calc.mul()) # multiply result : 0
print(calc.div()) # div result : 2.800

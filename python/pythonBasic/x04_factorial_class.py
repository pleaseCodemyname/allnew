class Factorial:
    def __init__(self, x):
        self.x = x
    def factorial(self):
        if self.x == 0:
            return 1
        else:
            return self.x * Factorial(self.x-1).factorial()
x = int(input("Input the number : "))

b = Factorial(x)
Factorial.factorial()

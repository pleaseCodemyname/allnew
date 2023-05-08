class Gcd(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def gcd(self):
        if self.a < self.b:
            self.a, self.b = self.b, self.a
        print("gcd", (self.a, self.b))
        while self.b !=0:
            self.r = self.a % self.b

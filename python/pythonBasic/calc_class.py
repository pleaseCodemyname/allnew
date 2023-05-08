class Calc(object):
    def __init__(self, a, b): ##a, b를 초기화함
        self.a = a
        self.b = b
    def add(self): #add 함수 생성
        return self.a + self.b
    def sub(self): #suib 함수 생성
        return self.a - self.b

add = Calc('a', 'b')
sub = Calc('a', 'b')

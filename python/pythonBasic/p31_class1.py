class Person(object):
    total = 10
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def getName(self):
        return self.name
    def getAge(self):
        return self.age

#클래스를 사용하는 이유? 클래스는 상속이 가능해서 상속의 속성을 사용해서 여러 용도로 Reuse하는게 목적
print(type(Person))
my = Person("Moon", 22)
print(my.name)
print(my.age)
print(my.getName())
print(my.getAge())
print(my.total)

you = Person("Kim", 20)
print(you.getName()) #method는 괄호 열고 닫고 함
print(you.getAge())
print(you.total)
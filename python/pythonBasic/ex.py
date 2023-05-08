class Person(object):
    total = 10
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

print(type(Person))
my = Person("yun", 22)
print(my.name)
print(my.age)
print(my.getName())
print(my.getAge())
print(my.total)

you = Person("Kim", 20)
print(you.getName())
print(you.getAge())
print(you.total)


class SmartPhone(object):
    def __init__(self, brand, details): #instance란
        self.brand = brand
        self.details = details
    def __str__(self):
        return f'str : {self.brand} - {self.details}'
    def __repr__(self):
        return f'repr : Instant name = SmartPhone({self.brand}, {self.details}'
    def __doc__(self):
        return f'This class is Smart Phone Class.'

SmartPhone1 = SmartPhone('IPhone', {'color' : 'White', 'price' : 10000}) #instance(클래스를 통해 생성한 객체)
SmartPhone2 = SmartPhone('Galaxy', {'color' : 'Black', 'price' : 8000})
SmartPhone3 = SmartPhone('Blackberry', {'color' : 'Silver', 'price' : 6000})

print(dir(SmartPhone))
print(SmartPhone1.__dict__) #SmartPhone1 인스턴스의 속성과 그 값이 담긴 딕셔너리가 반환됨
print(SmartPhone2.__dict__) #원래 Smartphone은 Galaxy인데 key/value 형식으로 나옴)
print(SmartPhone3.__dict__)

print(id(SmartPhone1)) #id 알아봄
print(id(SmartPhone2)) #id 알아봄
print(id(SmartPhone3)) #id 알아봄

print(SmartPhone1.brand == SmartPhone2.brand)
print(SmartPhone1 is SmartPhone2)
#
print(SmartPhone.__str__(SmartPhone1))
print(SmartPhone.__str__(SmartPhone2))
print(SmartPhone.__doc__) # none 호출한 적이 없음

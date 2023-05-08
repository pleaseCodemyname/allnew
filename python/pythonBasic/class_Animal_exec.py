from class_animal import *

dog = Dog('doggy')
print(dog.name)
dog.move() #instance
dog.speak() #instance

duck = Duck('donald')
print(duck.name)
duck.move() #instance
duck.speak() #instance

zoo = [Dog('marry'), Duck('dduck')]

for z in zoo:
    print(z.name) #instance가 아님 왜냐하면 class를 통해서 만들어진 객체가 아니기 때문이다
    z.speak() #instance
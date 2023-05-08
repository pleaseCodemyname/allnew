from class_rectangle import *

square1 = Rectangle.isSquare(5, 5)
print(square1)

rect1 = Rectangle(5, 5) #instance의 생성자를 만드는 방법
print('Area of rect1 is ', rect1.calcArea())
print(type(rect1)) #type = class (rectangle 의 상속된 class)
rect1.printCount()

rect2 = Rectangle(2, 5)
print('Area of rect2 is ', rect2.calcArea())
rect2.printCount()

rect3 = rect1 + rect2
print(type(rect3))
print('Area of rect3 is ', rect3.calcArea())

rect3.width = 6
rect3.height = 6
print('Area of rect3 is ', rect3.calcArea())
rect3.printCount()

rect4 = rect2.__add__(rect1)
print('Area of rect4 is ', rect4.calcArea()) ##rec1(5,5)와 rec(2,5) 더한 값 rec4 (7, 5)
rect3.printCount()

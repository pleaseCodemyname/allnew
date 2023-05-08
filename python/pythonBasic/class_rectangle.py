# class에서 method에 접근할때는 cls다
class Rectangle(object):
    count = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height
        Rectangle.count += 1

    def printCount(cls): #자기자신이 자기를 부를때 cls
        print(cls.count) #예를 실행 안해주면 rect1 밖에 실행이 안됨
    def calcArea(self):
        return self.width * self.height

    def isSquare(recwidth, recheight):
        return recwidth == recheight

    def __add__(self, other):
        return Rectangle(self.width + other.width, self.height + other.height)

    # 강사님 버전
    # class Rectangle(object):
    #     count = 0
    #
    #     def __init__(self, width, height):
    #         self.width = width
    #         self.height = height
    #         Rectangle.count += 1
    #
    # def calcArea(self):
    #     return self.width * self.height
    #
    # def isSquare(recwidth, recheight):
    #     return recwidth == recheight
    #
    # def __add__(self, other):
    #     obj = Rectangle(self.width + other.width, self.height + other.height)
    #     return obj
    #
    # def __add__(self, other):
    #     lol = Rectangle(self.width + other.width, self.height + other.height)
    #     return lol
    #
    # def printCount(cls):
    #     print(cls.count)

    #
    # #클래스를 할당받은 객체 = 인스턴스
    # issquare
    #

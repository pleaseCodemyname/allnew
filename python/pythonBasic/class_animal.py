class animal(object):
    def __init__(self, name):
        self.name = name
    def move(self):
        return print("move~")

class Dog(animal):
    def speak(self):
        return print("woof-woof")


class Duck(animal):
    def speak(self):
        return print("quack-quack")
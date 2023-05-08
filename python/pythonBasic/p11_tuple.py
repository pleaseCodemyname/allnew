#!/usr/bin/env python
#튜플은 소괄호, ##안에 있는 값을 변경 못함
person = ("Kim", 24, "male")
print(person)

a = ()
print(a)

b = (person, )
print(b)

name, age, gender = person
print("name : ", name )
print("age : ", age )
print("gender: ", gender )

n = 1
numbers = [1, 2]

print(type(person))  ##<class(type) 'tuple'>
print(type(n))  ##<class 'int'>
print(type(numbers)) ##<class 'list'>[1, 2]는 List

print(person[0]) #Kim
print(person[-1]) #male

fruits = ('apple', ('banana', 'cherry'), ('strawberry', 'watermelon')) #튜플안에 튜플이 가능함
print(fruits)
print(fruits[0])
print(fruits[1][0]) #banana
print(fruits[1][1]) #cherry
print(fruits[2][0]) #strawberry
print(fruits[2][1]) #watermelon
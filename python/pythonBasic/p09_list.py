#!/usr/bin/env python

numbers = [0 , 1, 2, 3]
names = ["Kim", "Lee", "Park", "Choi"]
print(numbers[0])
print(names[2:])
print(numbers[-1])
print(numbers + names)
empty=[]
print(empty)

# append 한개만 추가 가능
names.append("Moon")
print(names)

# insert
names.insert(1, "Gang")
print(names)

# delete (index에 의한 삭제)
del names [1]
print(names)

# remove (값에 의한 삭제)
names.remove("Moon")
print(names)

# pop
value = names.pop()
print(value)

# pop
value = names.pop(1)
print(value)

# extend
numbers.extend([4, 5, 6, 4, 4, 5, 6]) #여러개 추가하려면 extend
print(numbers)

# count
print(numbers.count(4))

# sort
numbers.sort()
print(numbers)

# reverse
numbers.reverse()
print(numbers)

# clear
numbers.clear()
print(numbers)


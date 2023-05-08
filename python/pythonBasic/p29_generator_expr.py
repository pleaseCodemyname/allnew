numbers = [1, 2, 3, 4, 5]
evens = (2 * i for i in numbers)

print(evens) #object type id가 나옴
print(evens.__next__()) #next를 해야만 멈춤
print(evens.__next__()) # 4
print(sum(evens)) # 3, 4, 5에 대한 sum 값 (이미 앞에서 2번 실행했기 때문에)

print(numbers) #[1, 2, 3, 4, 5]
numbers.reverse()
print(numbers) #[5, 4, 3, 2, 1]

evens = (2 * i for i in numbers)

print(evens) # 10 #id가 바뀜
print(evens.__next__())
print(evens.__next__()) #8
print(numbers) #[5, 4, 3, 2, 1]
print(evens.__next__()) #6


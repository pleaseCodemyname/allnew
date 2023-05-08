#반복적인 작업을 사용할때 유용함, 순서를 제어하고 싶을때(yield, next())
def counter3(max): #끝나게 하려면 (max)라는 인수를 줘야함
    t = 0
    while t < max:
        yield t
        t += 1
    return

timer = counter3(5) #4까지(Max)
print(timer.__next__()) #yield는 next로 불렀을때만 , yield는 next에게 반환하는 return
print(timer.__next__())
print(timer.__next__())

print()
for i in counter3(5):
    print(i)
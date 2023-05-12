# 튜플 값은 변경할 수 없음
tuple01 = (10, 20, 30)
tuple01 = tuple01 + (40, )

print('print Tuple : ', tuple01)

tuple02 = 10, 20, 30, 40
print(type(tuple02)) #<class 'tuple'> 되도록이면 괄호를 치기

mylist = [10, 20, 30, 40]
tuple03 = tuple(mylist)

if tuple02 == tuple03:
    print("Component equal")
else:
    print("Component not equal")

tuple04 = (10, 20, 30)
tuple05 = (40, 50, 60)
tuple06 = tuple04 + tuple05
print(tuple06)

tuple07 = tuple04 * 3  #tuple 04를 3번 반복
print(tuple07)

a ,b = 11, 22 #2변수의 값을 바꿀때 상당히 유용함
a, b = b , a
print('a =', a, 'b =', b)

tuple08 = (11, 22, 33, 44, 55, 66)
print(tuple08[1:3])
print(tuple08[3:])

tuple08[0] = 100
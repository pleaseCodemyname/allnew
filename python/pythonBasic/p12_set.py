#!/isr/bin/env python

even = set([0, 2, 4, 6, 8]) #set은 집합([]) 대괄호를 넣어줘야함
# print(even) #{0, 2, 4, 6, 8}
# print(type(even)) #<class 'set'>
#
hello = set("Hello") #set으로 설정하면 {'H', 'e', 'l', 'o'}
print(hello)
#
# s = even | hello
# print(s) #{0, 2, 4, 6, 8, 'H', 'e', 'l', 'o'}

p = even & hello
print(p) #

even.add(10)
print(even) # {0, 2, 4, 6, 8, 10}

hello.remove('e')
print(hello) # {'H', 'l', 'o'}

s1 = set([1, 2, 3, 4, 5])
s2 = set([4, 5, 6, 7, 8])

#intersection 교집합
print(s1.intersection(s2)) #교집합 {4,5}
print(s1 & s2) #교집합(&) {4, 5}

# union 합집합
print(s1.union(s2)) #{1, 2, 3, 4, 5, 6, 7, 8}
print(s1 | s2) #{1, 2, 3, 4, 5, 6, 7, 8}

#difference 차집합
print(s1.difference(s2)) # {1, 2, 3}
print(s2.difference(s1)) # {8, 6, 7}
print(s1 - s2) # {1, 2, 3}
print(s2 - s1) # {8, 6, 7}

s3 = {1, 2 ,3, 4, 5}

if s1 == s2:
    print("s1, s2 is same...")
else:
    print("s1, s2 is not same...")

if s1 == s3:
        print("s1, s3 is same...")
else:
        print("s1, s3 is not same...")

s4 = {6, 7, 8, 9, 10}

if s1.isdisjoint(s2): #s1과 s2의 교집합(공통으로 같고있는 것), 일치하는 값이 있으면(isdisjoint)면 True | False
    print("s1, s2 not have in common")
else:
    print("s1, s2 have in common") #{4, 5} 값이 in common

if s3.isdisjoint(s4): #isdisjoint 공통사항이 있는지 확인
    print("s3, s4 not have in common")
else:
    print("s3, s4 have in common")

print(s1.issubset(s2)) #subset이란? s1= set([1, 2, 3, 4, 5])에서 s2([4, 5, 6, 7, 8])

s5 = {4, 5}

print(s2.issubset(s5)) #false

s = {1, 2, 3}
print(f'set : {s}') #set : {1, 2, 3} 예를 들어, s = {1, 2, 3}이라는 집합(set)이 있다면, print(f'set : {s}')와 같이 f-strings을 사용하여 문자열 안에서
# {s} 부분을 변수 s의 값으로 치환하여 출력할 수 있습니다. 이 경우, 출력 결과는 set : {1, 2, 3}

s.update({'a', 'b', 'c'})  #update는 a, b, c 를 바꾸는게 아니라 추가하는 것임
print(f'set : {s}') #set : {1, 2, 3, 'a', 'b', 'c'}

s.update({11, 12, 13})
print(f'set : {s}') #순서는 중요하지 않고 자기 마음대로 들어감 set : {1, 2, 3, 11, 12, 13, 'a', 'b', 'c'}

s.remove('a')
print(f'set : {s}') # 지울값이 없으면 에러가 남(remove) set:

s.discard("b")
print(f'set : {s}') # 지울값이 없으면 그냥 가만히 있음, 에러를 내지 않음(discard), {set : {1 , 2, 3, 11, 12, 13, 'c'}

s.discard("b")
print(f'set : {s}')

s = {'r', 'd', 'n', 'd', 'o', 'm'}

#set은 집합을 의미함
print(f'set.pop() : {s.pop()}') #random한 값을 추출함
print(f'set : {s}') # set: {'m', 'd', 'o', 'r'}

print(f'set.pop() : {s.pop()}') # set.pop() : m
print(f'set : {s}') # set : {'d', 'o', 'r'}

print(f'set.pop() : {s.pop()}')  # set.pop() : d
print(f'set : {s}') # set : {'o', 'r'}

s.clear()
print(f'set : {s}') #clear 하면 set : set()

s = {'a', 'b', 'c'}

if 'a' in s:
    print('a is Exist')
else:
    print('a is not Exist')

if 'z' in s:
    print('z is Exist')
else:
    print('z is not Exist')

print(f'length of set : {len(s)}') # 3


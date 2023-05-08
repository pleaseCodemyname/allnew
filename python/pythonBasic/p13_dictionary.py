me = {"name": "Moon", "age" : 22, "gender" : "male"} #key값은 중복될 수 없으며, list나 set이 올 수 없음, list타입과 겹침

myname = me["name"] #key는 고유한 값이어야함
print(myname)

me["age"] = 25
print(me)

dict={}
print(dict)

me[10] = 10 #key10(숫자) : 10(value, 숫자)
print(me)

me['10'] = 10 #key'10'(문자) : 10(value, 숫자)
print(me)

me['job'] = "teacher"
print(me)

me['list'] = [1, 2, 3, 4, 5] #문자키('list')의 [1, 2, 3, 4, 5] 숫자
print(me)

me[(1,2)] = "this is value"  #me[(1,2)] 튜플은 변하지 않음 (2, 1)로 변할 수 없음 / [list]는 값의 순서가 변함
print(me)

me[3] = (3, 'aa', 5)  #(3, 'aa', 5) 튜플 값임
print(me)

print("===========")
print(f'me[list] : {me["list"]}')
print(f'me[(1, 2)] : {me[(1, 2)]}')
print(f'me[3] : {me[3]}')

print(f'me[(1, 2)] : {me[(1, 2)]}')
me[(1, 2)] = "This is real value"
print(f'me[(1, 2)] : {me[(1, 2)]}')

dic = {'a' : 1234, "b" : "blog", "c" : 3333}

if 'b' in dic:
    print("b is exist")
else:
    print("b is not exist")

if 'e' in dic: #dic안에 e가 있는지 없는지 확인
    print("e is exist")
else:
    print("e is not exist")

if 'blog' in dic.values(): #dic.value에서 'blog'란 value가 있는지
    print("value is exist")
else:
    print("value is not exist")

# keys()
print(dic.keys())

for k in dic.keys():
    print(f'key : {k}')

# values()
if 'blog' in dic.values():
    print("value is exist")
else:
    print("value is not exist")

print(dic.values())

for v in dic.values():
    print(f'value : {v}')

# itmes()
print(dic.items())

for i in dic.items():
    print(f'all : {i}')
    print(f'key : {i[0]}')
    print(f'value : {i[1]}')
    print()

# get
v1 = dic.get('b')
print(f"dic.get['b'] : {v1}") #get을 통해서 b의 key값을 가져왔더니 저절로 v1은 b의 blog를 가져옴 (get을 통해서 해당되는 index의 값을 가져올 수 있음)

v2 = dic.get('z')
print(f"dic.get['z'] : {v2}") #z에 값이 없으니깐 None을 가져옴

print(f'before : {dic}')

# del
del dic['c']

print(f'after : {dic}')

# clear
dic.clear()
print(f'dic : {dic}')

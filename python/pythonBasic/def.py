def hello():
    print('hello')

hello()

def hello(i):
    print(f'hello {i}') #type(i) = str
hello('yun') #str형식으로 넣어줘야함


# def add_num(a, b):
#     print(a + b)
#
# i = add_num(3, 4) # add_num에 이미 7이 들어갔음
# print(i)

def add_num(a,b):
    return a + b #return은 항상 마지막에 / 후에 어떤 값을 넣으면 무시해버림

i = add_num(3,4)
print(i)
print(i + 5)


def add_nums(*args):
    return args

print(add_nums(1,2,3,4,5,6,7)[-1]) #튜플임(소괄호)

#반복문
def input_me(name='yun', age=20): #age 기본값
    return name, age

print(input_me('kim', 20)) #튜플
print(input_me('lee'))
print(input_me(10)) #이름에 10이 들어감, 이름이 10인거임
print(input_me(age=30))

def input_me(**kwargs): #**무한대로 넣어서 쓸 수 있음
    return kwargs

print(input_me(name='kim', age=20)) #type=dict
print(input_me(name="lee", age = 20, food = 'pizza'))
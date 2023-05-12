def nolamda(x, y):
    return 3 * x + 2 * y

x, y = 3, 5

result = nolamda(x, y)
print('일반 함수 방식 : %d' % (result)) # 일반 함수 방식 : 19

yeslamda = lambda x, y : 3 * x + 2 * y #람다를 사용하는 이유? 익명함수
# 뭔가 연산하는데 무슨 연산이라고 하기 애매함, 이름을 부르기 애매함. 그래서 그냥 이름을 짓지 않고
result = yeslamda(x,y)
print('람다 방식 : %d' % (result)) #람다 방식 : 19

result = yeslamda(5, 7)
print("람다 방식 2 : %d" % (result)) #람다 방식 2 : 29


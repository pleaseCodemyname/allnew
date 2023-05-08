#클로저 함수
#첫번째 파라미터를 던졌을떄 나오는게 아니고, 나중에 값을 묶어서 보내고 싶다. Calc는 전역변수
#add 안에 calc 가 감싸주고 있음, 두가지의 중첩된 함수 (클로저를 만들려면 반드시 중첩된 함수)
#클로저함수를 사용하는 이유? 내부함수에는 관심에는 없고 외부함수에는 실행을 delay?
def calc(a):
    def add(b):
        return a + b
    return add
sum = calc(1)
print(sum(2))

def hello(msg):
    message = "Hi, " + msg
    def say():
        print(message) #"Hi, " + msg(Moon)
    return say

f = hello('Moon')
f()
# 장점? 전역변수가 많아지면 메모리를 많이 차지함, closure를 사용하면 전역변수가 많을 필요가 없음 & 코드 간결화 & 필요한 시점에 언제든지 Reuse 가능 편리성


def add(c):
    a = c + 9
    return a

print(add(11))
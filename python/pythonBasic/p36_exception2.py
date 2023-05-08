a = "Hello" #문자
b = 1 # 숫자

try:
    c = a + b
    print(c)
except:
    print('The Error is occurred') #문자열하고 Assemble 했기 때문에 에러임 / Error 일때도 나타나지만 Error 중단의 의미가 없음
print(a) #상관없이 진행됨

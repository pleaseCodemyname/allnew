#무한 루프
n = 0 #변수 초기화

while True : #조건문이 항상 True임, n 변수의 초기값이 1이더라도 while true는 계속 실행함
    n += 1 #1씩 증가

    if n > 10 : #n이 9까지 반복할꺼야, 10이면
        break #break
    if ((n % 2) == 0) : #n이 2의 배수인 것들만
        print(n) # 출력할 것임

# n = 0

# while True :
#    n += 1
#   if n > 10:
#   break
#   if ((n % 10 == 0):
#   print(n)

#변수 초기화
#조건문이 항상 참임
#n 은 1씩 증가
# n이 9까지만 할 것임(b)
#n을 2의배수만 출력할 것임

# n = 0
# while Ture:
#     n += 1
#     if n > 10:
#         break
#     if ((n % 2 == 0)):
#         print(n)
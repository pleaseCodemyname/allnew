import p25_timer

timer = p25_timer.counter2()

# print(timer)
counter = 0
for k in range(1, 101):
    if k % 7 == 0:        # 7의 배수
        counter = timer() #timer는 함수

print(f"result : {counter}") #counter는 변수



# def counter2():
#     t = [0]
#     def increment():
#         t[0] += 1
#         return t[0]
#     return increment
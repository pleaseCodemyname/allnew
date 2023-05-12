# # name = input('이름 입력 : ')
# # print('이름 : %s' % name)  # %s는 문자열 %d 는 숫자\
# #
# # age = int(input('나이 입력 : '))
# # print('나이 : %d' %age)
#
# coffee = 3
# print("우리 매장에 커피 {} 잔이 있습니다.".format(coffee))
#
# money = int(input("돈을 넣어주세요 : "))
# print("{}를 입금하셨습니다.".format(money))
#
# salary = int(input("월급 입력 : "))
# income = 0
# tax = 0
#
# #연봉 구하기
# if salary >= 500:
#     income = 12 * salary
# else:
#     income = 13 * salary
#
# if income >= 10000:
#     tax = 0.2 * income
# elif income >= 7000:
#     tax = 0.15 * income
# else:
#     tax = 0
# print("월급 : %d" % (salary))
# print("연봉 : %d" % (income))
# print("세금 : %d" % (tax))
#
somelist = ['김의찬', '유만식', '이영철' , '심수련', 'a', 'b', 'c']
print(somelist)
print(somelist[-2]) #str
print(type(somelist)) #<class 'list'>
print(type(somelist[0])) #<class 'str'> #리스트안에는 str 속성으로 이루어져 있음, int로도 가능
length = len(somelist)
print('홀수 번째만 출력')
print(somelist[1:length:2]) # 1에서 시작해 4까지 2칸씩 넘기겠다 a[시작:끝:step(간격)] 실제로는 짝수만
print(length) # 4

print(somelist[0:length:2]) # 김의찬, 이영철 / 실제로는 홀수만
print(somelist[0:length:3]) #0김의찬, 3심수련, c



###왜 tuple01 + (40)은 값이 들어가지 않는걸까?
tuple01 = (10, 20, 30)
tuple01 = tuple01 + (40,)
print('print tuple:', tuple01)

tuple08 = (11, 22, 33, 44, 55, 66)
print(tuple08[1:3]) #2번째와 3번쨰

def factorial(x):
    if x ==0:
        return 1
    else:
        return x * factorial(x-1)
input = int(input("input number:"))
print(f'{input} factorial = {factorial(input)}')


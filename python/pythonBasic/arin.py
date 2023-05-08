import random
def binary(num): # 10진수를 2진수로 변환하는 함수를 정의
    binary_num = '' # 2진수를 저장할 변수를 초기화
    while num > 0: # num이 0보다 큰 동안 반복
        div = num // 2 # num을 2로 나눈 몫을 계산
        remain = num % 2 # num을 2로 나눈 나머지를 계산
        binary_num = str(remain) + binary_num # 계산된 나머지를 2진수 문자열에 추가
        num = div # num 변수에 몫을 저장하여 다음 계산에 사용
    return binary_num # 2진수 문자열

result = []
for i in range(1):
    num = random.sample(range(4, 17), 1)[0] # 4에서 16 사이의 난수를 1개 생성하여 num 변수에 저장
    bin_num = binary(num) # num을 2진수로 변환한 결과를 bin_num 변수에 저장
    result.append((num, bin_num)) # num과 bin_num을 튜플로 묶어 result 리스트에 추가

for num, binary in result: # result 리스트의 각 요소에 대해 반복
    print(f"{num} binary number is: [{binary}]") # num과 이진수 문자열을 출력
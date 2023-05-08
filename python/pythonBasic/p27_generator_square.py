#  리스트에 있는 거 하나씩 꺼내서 2배로 만들어 주기 (제곱으로) ^2 함수를 generator로 만들기
def square_number(nums):
    for i in nums:
        yield i * i

mynum = [1, 2, 3, 4, 5]

result = square_number(mynum)

for i in range(len(mynum)): #mynum = 5니깐 5번 반복
    print(f"Square value of mynum[{i}] = {mynum[i]} : {next(result)}") #{} 0부터 시작 / [] mynum의 값 첫번째부터 시작
    #{list index 출력}   [list실제 값 출력]

# mynum = [1, 2, 3, 4, 5]
# def counter3(square):
# for mynum counter3

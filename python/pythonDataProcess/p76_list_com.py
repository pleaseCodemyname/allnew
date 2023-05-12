mylist01 = list(onedata for onedata in range(1, 6))
print(mylist01) # [1 ,2, 3, 4, 5]
print(type(mylist01)) #<class 'list'>

mylist02 = list(10* onedata for onedata in range(1, 6))
print(mylist02) # [10, 20, 30, 40, 50]

mylist03 = [3, 4, 6, 2]
result = [idx ** 2 for idx in mylist03 if idx % 2 ==0] # 2의 배수인 것만 2제곱 하겠다.
print(result) # [16, 36, 4]


from pandas import Series

myindex1 = ['성춘향', '이몽룡', '심봉사']
mylist1 = [40, 50, 60]

myindex2 = ['성춘향', '이몽룡', '뺑덕어멈']
mylist2 = [20, 40, 70]

myseries1 = Series(data=mylist1, index=myindex1)
myseries2= Series(data=mylist2, index=myindex2)

print('\n# 시리즈 01')
print(myseries1)
print('\n# 시리즈 02')
print(myseries2)

print('\n# 두 시리즈 덧셈')
result = myseries1.add(myseries2, fill_value=10)
print(result)

print('\n# 두 시리즈 뻴셈')
result = myseries1.sub(myseries2, fill_value=30)
print(result)

from pandas import Series
import numpy as np

mylist = [10, 40, 30]
myindex = ['김유신', '이순신', '강감찬']

##Case 01와 02의 차이가 없음
print('\n# Case 01')
myseries = Series(mylist)
print(myseries)

print('\n# Case 02')
myseries = Series(data=mylist)
print(myseries)

print('\n# Case 03')
myseries = Series(data=mylist, index=myindex)
print(myseries)

print('\n# Case 04')
myseries = Series(data=mylist, index=myindex, dtype=float) #Float를 사용하면 소수점이 보임 10.0 20.0 30.0
print(myseries)




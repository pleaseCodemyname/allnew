import numpy as np
from pandas import Series, DataFrame

#column의 값을 구별하는지 안하는지에 따라 DataFrame과 Series 차이가 남
myindex = ['강호민', '유재준', '신동진']
mylist = [30, 40, 50]

myseries = Series(data=mylist, index=myindex)
print('\nSeries print')
print(myseries)

myindex = ['강호민', '유재준', '신동진']
mycolumns = ['서울', '부산', '경주'] #열
mylist = list(10 * onedata for onedata in range(1, 10)) #list comprehension, 이 DataFrame 객체는 '서울', '부산', '경주'의 열 이름과 각 열마다 10, 20, ..., 90의 값을 데이터로 갖습니다.

myframe = DataFrame(np.reshape(np.array(mylist), (3, 3)), index=myindex, columns=mycolumns)
print('\nDataFrame print') # 3행 3열
print(myframe)

print('\nDataFrame + Series')
result = myframe.add(myseries, axis =0)
print(result)

myindex2 = ['강호민', '유재준', '김병준']
mycolumns2 = ['서울', '부산', '대구']
mylist2 = list(5 * onedata for onedata in range(1,10))

myframe2 = DataFrame(np.reshape(np.array(mylist2), (3, 3)), index=myindex2, columns=mycolumns2)
print('\nDataFrame print')
print(myframe2)

print('\nDataFrame + DataFrame')
result = myframe.add(myframe2, fill_value=0)
print(result)
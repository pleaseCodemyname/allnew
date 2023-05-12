from pandas import Series

mylist = [10, 40, 30, 20]
myseries = Series(data=mylist, index = ['김유신', '이순신', '강감찬', '광해군']) #index를 따로 만들지 않고 수동으로 넣음

print('\nData Type')
print(type(myseries)) #<class 'pandas.core.series.Series'>

myseries.index.name = '점수'
print('\nindex name of series')
print(myseries.name) #점수

myseries.name = '학생들 시험'
print('\nindex name of series')
print(myseries.index.name)  # 학생들 시험

print('\nname of series')
print(myseries.index)
#Index(['김유신', '이순신', '강감찬', '광해군'], dtype='object', name='점수')

print('\nvalue of series')
print(myseries.values)
# [10 40 30 20]

print('\nprint information of series')
print(myseries)
#점수
#김유신    10
#이순신    40
#강감찬    30
#광해군    20
#Name: 학생들 시험, dtype: int64

print('\nrepeat print')
for idx in myseries.index:
    print('Index : ' + idx + ', Values : ' + str(myseries[idx]))
#Index : 김유신, Values : 10
#Index : 이순신, Values : 40
#Index : 강감찬, Values : 30
#Index : 광해군, Values : 20

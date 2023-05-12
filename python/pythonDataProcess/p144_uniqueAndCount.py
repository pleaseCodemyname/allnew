from pandas import Series

print('\nUnique, count, isin')
mylist = ['라일락', '코스모스', '코스모스', '백일홍', '코스모스', '코스모스', '들장미', '들장미', '라일락', '라일락']
myseries = Series(mylist)

print('\nUnique()')
myunique = myseries.unique()
print(myunique) #['라일락' '코스모스' '백일홍' '들장미'] 중복된 값을 한 번만 처리해서 출력함

print('\nvalue_count()')
print(myseries.value_counts()) #각 Value들이 몇 개 있는지 확인

print('\nisin')
mask = myseries.isin(['들장미', '라일락'])
print(mask) #들장미랑 라일락만 있는 것만 True, False 값을 줌 (dtype = bool)
print('-' * 50)

print(myseries[mask])  #들장미 라일락값만 몇번째 index에 있는지 출력함 정해져있는 것만 출력
print('-' * 50)

print('\nfinished')

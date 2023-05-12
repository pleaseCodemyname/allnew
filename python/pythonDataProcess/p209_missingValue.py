import numpy as np
import pandas as pd
from pandas import DataFrame, Series

print('\n# 시리즈의 누락 데이터 처리')
print('#원본 시리즈')
myseries = Series(['강감찬', '이순신', np.nan, '광해군'])
print(myseries)

print('\n# isnull() 함수 : NaN이면 True')
print(myseries.isnull())

print('\n# notnull() 함수 : NaN이 아니면 True')
print(myseries.notnull())
print("-" * 40)

print('\n# notnull() 이용하여 참인 항목만 출력')
print(myseries[myseries.notnull()]) #notnull(빈 값이 아닌 것)을 출력

print('\n# dropna() 이용 누락 데이터 처리')
print(myseries.dropna()) #같은 기능임(Nan 값만)

filename = 'excel02.csv'
myframe = pd.read_csv(filename, index_col='이름', encoding='utf-8')
print(myframe)

print('\n# dropna() 이용 누락 데이터 처리') #강감찬 데이터만 나옴
cleaned = myframe.dropna(axis=0) #강감찬만 나온
print(cleaned)
#        국어    영어    수학
# 이름
# 강감찬  10.0  20.0  30.0

print('\n# how="all" 이용 누락 데이터 처리') #모든 데이터에 NaN이 있으니깐 박영희만 제거됨
cleaned = myframe.dropna(axis=0, how='all') #모든 데이터가 제거
print(cleaned)
#       국어    영어    수학
# 이름
# 강감찬  10.0  20.0  30.0
# 홍길동  40.0   NaN   NaN
# 김철수   NaN  50.0  60.0

print('\n# how="all" 이용 누락 데이터 처리') #데이터에 하나라도 NaN이 있다면 제거
cleaned = myframe.dropna(axis=0, how='any')
print(cleaned)
#        국어    영어    수학
# 이름
# 강감찬  10.0  20.0  30.0

print('\n# [영어] 칼럼에 NaN 제거')
print(myframe.dropna(subset=['영어']))
#        국어    영어    수학
# 이름
# 강감찬  10.0  20.0  30.0
# 김철수   NaN  50.0  60.0

print('\n# 컬럼기준, how="all" 이용 누락 데이터 처리')
cleaned = myframe.dropna(axis=1, how='all') #열에 모든게 NaN이 있으면 삭제
print(cleaned)
#        국어    영어    수학
# 이름
# 강감찬  10.0  20.0  30.0
# 홍길동  40.0   NaN   NaN
# 박영희   NaN   NaN   NaN
# 김철수   NaN  50.0  60.0

print('\n# 컬럼기준, how="any" 이용 누락 데이터 처리')
cleaned = myframe.dropna(axis=1, how='any') #열에 하나라도 NaN이 있으면 삭제
print(cleaned)
# Empty DataFrame
# Columns: []
# Index: [강감찬, 홍길동, 박영희, 김철수]

print('## before')
print(myframe)
myframe.loc[['강감찬', '홍길동'],['국어']] = np.nan #홍길동과 강감찬의 국어성적을 nan으로 바꿨음
#      국어    영어    수학
# 이름
# 강감찬 NaN  20.0  30.0
# 홍길동 NaN   NaN   NaN
# 박영희 NaN   NaN   NaN
# 김철수 NaN  50.0  60.0
print('## after')
print((myframe))

print(myframe.dropna(axis=1, how="all")) #국어제거됨
print(myframe)
#       영어    수학
# 이름
# 강감찬  20.0  30.0
# 홍길동   NaN   NaN
# 박영희   NaN   NaN
# 김철수  50.0  60.0


print('## thresh option')
print(myframe.dropna(axis=1, thresh=2)) #thresh 조회옵션, NaN이 아닌애들의 갯수를 count

myframe.loc[['강감찬'], ['영어']] = np.nan

print(myframe.dropna(axis=1, thresh=3)) #not null count 이상

print(myframe.dropna(axis=1, how="any"))


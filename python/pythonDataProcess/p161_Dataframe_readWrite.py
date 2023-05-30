import numpy as np
from pandas import DataFrame

myindex = ['이순신', '김유신', '강감찬','광해군', '연산군']
mycolumns = ['서울','부산','광주','목포','경주']
mylist = list(10 * onedata for onedata in range(1, 26))
print(mylist) #10~250까지

myframe = DataFrame(np.reshape(mylist, (5,5)), index=myindex, columns=mycolumns)
print(myframe) #5행 5열

print('\n1 row data read of series')
result = myframe.iloc[1]
print(type(result))
print(result) #두번째 행의 값을 가져오겠다 (김유신)

print('\nmulti row data read of series')
result = myframe.iloc[[1,3]]

print(type(result))
print(result) #김유신과 광해군 데이터 가져옴

print('\neven row data read of series')
result = myframe.iloc[0::2]
print(type(result))
print(result) #0에서 부터 시작해 2칸씩 뛰어서 가져옴(짝수자리)

print('\nodd row data read of series')
result = myframe.iloc[1::2]
print(type(result))
print(result) #1에서 부터 시작해 2칸씩 뛰어서 가져옴(홀수자리)

print('\n김유신 included row data read of series')
result = myframe.loc[['김유신']]
print(type(result))
print(result)

print('\n김유신 included row data read of Dataframe')
result = myframe.loc[['김유신']]
print(type(result))
print(result)

#index로 읽을때는 iloc / data로 읽을때는 loc
print('\n이순신, 강감찬 included row data read of Dataframe')
result = myframe.loc[['이순신', '강감찬']]
print(type(result))
print(result)

print(myframe.index)
print('-' * 50)

print('\n이순신, 광주 실적 included row data read of DataFrame')
result = myframe.loc[['이순신'], ['광주']] #이순신 행 / 광주(열) 값을 가져오겠음
print(type(result))
print(result)

print('\n연산군, 강감찬 / 광주, 목포  실적 included row data read of DataFrame')
result = myframe.loc[['연산군', '강감찬'], ['광주', '목포']] #행(row)열(column)
print(type(result))
print(result)

print('\n이순신 ~ 강감찬 / 서울 ~목포 실적 included row data read of Dataframe')
result = myframe.loc['이순신':'강감찬', '서울':'목포']
print(type(result))
print(result)

print('\n김유신 ~ 광해군 / 부산 실적 included row data read of Dataframe')
result = myframe.loc['김유신':'광해군', ['부산']]
print(type(result))
print(result)

print('\nBoolean Data process')
result = myframe.loc[[False, True, True, False, True]] #행을 걸렀음
print(result)

print('\n부산 실적 <= 100')
result = myframe.loc[myframe['부산'] <=100]
print(result)

print('\n목포 실적 <= 140')
result = myframe.loc[myframe['목포'] <=140]
print(result)

cond1 = myframe['부산'] >= 70
cond2 = myframe['목포'] >= 140

print(type(cond1)) #<class Series>
print('-' * 40)

df = DataFrame([cond1, cond2])
print(df)
print('-' * 40)

print(df.all())
print('-' * 40)

print(df.any())
print('-' * 40)

result = myframe.loc[df.all()]
print(result)
print('-' * 40)

result = myframe.loc[df.any()]
print(result)
print('-' * 40)

print('\nlambda function')
result = myframe.loc[lambda df: df['광주'] >=130]
print(result)

print('\ndata set 30 => 이순신, 강감찬 부산 실적')
myframe.loc[['이순신', '강감찬'], ['부산']] = 30
print(myframe)

print('\ndata set 30 => 김유신 ~ 광해군 경주 실적')
myframe.loc['김유신':'광해군',['경주']] = 80
print(myframe)

print('\ndata set 50 => 연산군 모든 실적')
myframe.loc[['연산군'], :] = 50
print(myframe)

print('\ndata set 60 => 모든 사람의 광주 실적')
myframe.loc[:, ['광주']] = 60
print(myframe)

print('\ndata set 0 => 경주 실적 < = 60인 사람 경주, 광주 실적') #경주와 광주의 60이하인 사람 실
myframe.loc[myframe['경주'] <= 60, ['경주', '광주']] = 0
print(myframe)

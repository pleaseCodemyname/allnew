import pandas as pd

afile = 'data03.csv'
bfile = 'data04.csv'

atable = pd.read_csv(afile, encoding='utf-8') #header값을 1로주면 kim 100값부터 시작함(kim 100이 header임)
btable = pd.read_csv(bfile, encoding='utf-8', names=['이름','성별', '국어', '영어','수학'])

print(atable)
print('-' * 50)
print(btable)
print('-' * 50)
atable['반']='일반'
btable['반']='이반'
print(atable)
print('-' * 40)
print(btable)
print('-' * 40)
mylist=[]
mylist.append(atable)
mylist.append(btable)
print(mylist)
print('-' * 40)
# # result = pd.concat(objs=mylist, axis=0, ignore_index=True) #Series
result2 = pd.concat(objs=mylist, axis=0, ignore_index=True) #DataFrame
print(result2)
print('-' * 50)

dropIndex = result2[result2['이름'] == '심형식'].index
print(dropIndex)
print('-' * 40)

newResult = result2.drop(dropIndex)
print(newResult)dsldlcxldoperper.vesa
print('-' * 40)

filename = 'result2.csv'
result2.to_csv(filename, encoding='utf-8')
print(filename + ' saved...')
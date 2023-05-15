import pandas as pd

afile = 'android.csv'
bfile = 'iphone.csv'

atable = pd.read_csv(afile, header=0, encoding='utf-8') #header값을 1로주면 kim 100값부터 시작함(kim 100이 header임)
btable = pd.read_csv(bfile, header=0, encoding='utf-8')

print(atable)
print('-' * 50)
print(btable)
print('-' * 50)

atable['phone']='안드로이드'
btable['phone']='아이폰'

print(atable)
print(btable)

mylist=[]
mylist.append(atable)
mylist.append(btable)

# result = pd.concat(objs=mylist, axis=0, ignore_index=True) #Series
result = pd.concat(objs=mylist, axis=1, ignore_index=True) #DataFrame

print(result)
print('-' * 50)
filename = 'result.csv'
result.to_csv(filename, encoding='utf-8')
print(filename + ' saved...')
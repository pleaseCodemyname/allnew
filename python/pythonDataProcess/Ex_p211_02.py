import numpy as np
import pandas as pd
from pandas import DataFrame, Series

sdata = [[60.00, np.nan, 90.00], [np.nan, 80.00,50.00], [40.00, 50.00, np.nan]]
myindex = ['강감찬', '김유신', '이순신']
mycolumn = ['국어', '영어', '수학']
myframe = DataFrame(data=sdata, index=myindex, columns=mycolumn)
print('Before')
print(myframe)

myframe.loc[myframe['국어'].isnull(), '국어'] = myframe['국어'].mean()
myframe.loc[myframe['영어'].isnull(), '영어'] = myframe['영어'].mean()
myframe.loc[myframe['수학'].isnull(), '수학'] = myframe['수학'].mean()
# myframe.loc[['김유신'],['국어']]= 50.00
# myframe.loc[['강감찬'],['영어']]=65.00
# myframe.loc[['이순신'],['수학']]=70.00
print('\nAfter')
print(myframe)
print('-' * 40)
print(myframe.describe())





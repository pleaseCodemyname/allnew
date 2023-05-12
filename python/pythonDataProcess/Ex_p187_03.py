import pandas as pd

result = []
myColumns =('이름', '나이')
myencoding = 'utf-8'
mydata =[('김철수', 10), ('박영희', 20)]

for idx in mydata:
    sublist = []
    sublist.append(mydata[0])
    sublist.append(mydata[1])
    result.append(mydata)

myframe = pd.DataFrame(result, columns=myColumns)

filename = 'csv_02_01.CSV'
myframe.to_csv(filename, encoding=myencoding, mode='w', index=False)

filename = 'csv_02_02.CSV'
myframe.to_csv(filename, encoding=myencoding, mode='w', index=False, sep="#")
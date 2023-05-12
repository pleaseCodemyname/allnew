from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np
from bs4 import BeautifulSoup

plt .rcParams['font.family'] = 'Malgun Gothic'

html = open('ex5-10.html', 'r', encoding="utf-8")
soup = BeautifulSoup(html, 'html.parser')

result=[]
tbody= soup.find("tbody")
tds = tbody.findAll('td')
for data in tds:
    result.append(data.text)
print(result)
print('-' * 50)

mycolumns = ['이름','국어', '영어']
myframe= DataFrame(np.reshape(result, (4,3)),  columns=mycolumns)
a = myframe.set_index(keys=["이름"])
print(a)
print('-' * 50)

a.astype(float).plot(kind='line', title='Score', legend=True)
filename='scoreGraph.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' Saved...')
plt.show()

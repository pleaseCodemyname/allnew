import urllib.request
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from pandas import DataFrame

plt.rcParams['font.family'] = 'Malgun Gothic'

url = "http://movie.daum.net/ranking/reservation"
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

infos = soup.findAll('div', attrs={'class':'thumb_cont'})

print('-' * 40)
print(infos)
print('-' * 40)

no =0
result = []
for info in infos:
    no += 1
    mytitle = info.find('a', attrs={'class':'link_txt'})
    title = mytitle.string
    print(title)

    mygrade = info.find('span', attrs={'class':'txt_grade'})
    grade = mygrade.string
    print(grade)

    mypercent = info.find('span', attrs={'class': 'txt_num'})
    percent = mypercent.string
    print(percent)

    myrelease = info.find('span', attrs={'class': 'txt_info'})
    release2 = myrelease.find('span', attrs={'class': 'txt_num'})
    release = release2.string
    print(release)

    result.append((no, title, grade, percent, release))
    print(result)

    mycolumn = ["순위", "제목", "평점", "예매율", "개봉일"]
    myframe=DataFrame(result, columns=mycolumn)
    a = myframe.set_index(keys=['순위'])
    print(a)

    filename = 'daumMovie.csv'
    myframe.to_csv(filename, encoding='utf8', index=False)
    print(filename, ' saved...', sep='')
    print('finished')

    #strip은 아무것도 없으면 제거
    # myframe = pd.read_csv(filename, index_col='제목', encoding='utf-8')
    #
    # myframe['평점']= myframe['평점'].astype(float)
    # myframe['예매율']= myframe['예매율'].str.replace('%', '').astype(float)
    # print(myframe)
    # print('-' * 40)
    #
    # filename2 = 'Theater.png'
    # plt.savefig(filename2, dpi=400, bbox_inches='tight')
    # print(filename2 + 'Saved....')
    # plt.show()






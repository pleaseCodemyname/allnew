import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'

filename = '점수데이터.csv'
myframe = pd.read_csv(filename, encoding='utf-8', index_col=0)

print(myframe['jumsu'].unique())

frame01 = myframe.loc[myframe['jumsu'] == 'lower', 'length']
frame01.index.name = 'lower'
print(frame01.head()) #head 5개 출력 10개 출력하고 싶으면 frame.01(head(10))
print('-' * 40)

frame02 = myframe.loc[myframe['jumsu'] == 'upper', 'length']
frame02.index.name = 'upper'
print(frame02.head())
print('-' * 40)

totalframe = pd.concat([frame01, frame02], axis=1, ignore_index=True) #기존 인덱스를 무시하고 원래 점수데이터 인덱스 무시하고, frame01, frame02
totalframe.columns = ['lower', 'upper']
print(totalframe.head())
print('-' * 40)

totalframe.plot(kind='box')

plt.xlabel("점수 구분")
plt.ylabel("길이")
plt.grid(False)
plt.title("점수에 따른 길이의 상자 수염 그래프")

filename = 'boxPlot01_image.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' Saved...')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# 데이터 가져오기
# 아래 예시는 케글에서 예시 데이터를 가져오는 것으로 가정하였습니다.
# 실제 데이터를 가져오는 코드에 맞게 수정해주셔야 합니다.
data = pd.read_csv('kaggle_data.csv')

# 필요한 데이터 추출
new_york_data = data[data['City'] == 'New York']
seoul_data = data[data['City'] == 'Seoul']
tokyo_data = data[data['City'] == 'Tokyo']

# 그래프 그리기
plt.plot(new_york_data['Date'], new_york_data['Temperature'], label='New York')
plt.plot(seoul_data['Date'], seoul_data['Temperature'], label='Seoul')
plt.plot(tokyo_data['Date'], tokyo_data['Temperature'], label='Tokyo')

# 그래프 축 설정
plt.xlabel('X')
plt.ylabel('Date')

# X축 범위 설정
plt.xlim(-20, 50)

# 범례 표시
plt.legend()

# 그래프 저장
plt.savefig('result_plot.png')

# CSV 파일 생성
result_data = pd.concat([new_york_data, seoul_data, tokyo_data])
result_data.to_csv('result_data.csv', index=False)

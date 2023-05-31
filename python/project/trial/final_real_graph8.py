import pymongo
import os
import json
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from pymongo import MongoClient

# 폰트 설정
plt.rcParams['font.family'] = 'AppleGothic'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath("./")))
secret_file = os.path.join(BASE_DIR, "../secret.json")

with open(secret_file) as f:
    secrets = json.load(f)

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        errorMsg = "Set the {} environment variable.".format(setting)
    return errorMsg

HOSTNAME = get_secret("ATLAS_Hostname")
USERNAME = get_secret("ATLAS_Username")
PASSWORD = get_secret("ATLAS_Password")

# MongoDB 연결
client = MongoClient(f"mongodb+srv://{USERNAME}:{PASSWORD}@{HOSTNAME}")
db = client["project"]
collections = [db["collection2018"], db["collection2020"], db["collection2022"], db["collection2023"]]

# 데이터프레임 생성
df_list = []
year_list = [2018, 2020, 2022, 2023]
for year, collection in zip(year_list, collections):
    data = collection.find_one({}, {"_id": 0, "counts": 1})["counts"]
    df = pd.DataFrame(data).T.reset_index()
    df.columns = ["City"] + list(df.columns[1:])
    df["City"] = df["City"].str.split("|").str[1]
    df["Year"] = year
    df = df[["Year", "City"] + list(df.columns[1:-1])]
    df_list.append(df)

df = pd.concat(df_list)
df = df.reset_index(drop=True)

print(df)
# 그래프 그리기
plt.figure(figsize=(12, 4))

# 도시별 색상 매핑 딕셔너리
city_colors = {"Tokyo": "red", "Osaka": "blue", "Fukuoka": "green"}

# 도시별 그래프 그리기
for i, city in enumerate(["Tokyo", "Osaka", "Fukuoka"]):
    plt.subplot(1, 3, i + 1)
    handles = []
    labels = []
    
    # 년도별 그래프 그리기
    for year in [2018, 2020, 2022, 2023]:
        city_data = df[(df["Year"] == year) & (df["City"] == city)]
        if not city_data.empty:
            x = range(1, 13)  # 월
            y = city_data.iloc[:, 2:].values[0]  # 도시별 월별 데이터

            bar_width = 0.3  # 막대 그래프의 너비
            opacity = 0.8  # 막대 그래프의 투명도

            bars = plt.bar(x, y, bar_width,
                           alpha=opacity,
                           color=city_colors.get(city, "gray"))  # 이 부분을 수정했습니다.
            handles.append(bars[0])
            labels.append(str(year))

            # 막대 위에 값 표시
            for j, v in enumerate(y):
                plt.text(x[j], v + 0.5, str(v), ha='center')

    plt.xlabel("Month")
    plt.ylabel("Count")
    plt.title(f"{city} Data")
    plt.xticks(range(1, 13))

    y_min = df.iloc[:, 2:].values[~np.isnan(df.iloc[:, 2:].values)].min()
    y_max = df.iloc[:, 2:].values[~np.isnan(df.iloc[:, 2:].values)].max()
    plt.ylim(ymin=y_min, ymax=y_max)

    plt.legend(handles, labels)

plt.tight_layout()  # 그래프 간격 조정

plt.savefig('final_graph8.png')
plt.show()

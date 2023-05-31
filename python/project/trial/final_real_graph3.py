import pymongo
import os
import json
import matplotlib.pyplot as plt
import pandas as pd

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

# 몽고DB 연결
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

df_combined = pd.concat(df_list)
df_combined = df_combined.reset_index(drop=True)

# 도시별 색상 매핑 딕셔너리
city_colors = {"도쿄": "red", "오사카": "blue", "후쿠오카": "green"}

# 그래프 그리기
plt.figure(figsize=(10, 6))

bar_width = 0.2
opacity = 0.8

for i, year in enumerate(year_list):
    year_data = df_combined[df_combined["Year"] == year]
    x = range(1, 13)  # 1부터 12까지의 월을 나타내는 range 생성

    for j, city in enumerate(year_data["City"].unique()):
        city_data = year_data[year_data["City"] == city]
        y = city_data.values[0][2:14]  # 도시별 월별 데이터
        plt.bar([p + (i + j * bar_width) * bar_width for p in x], y, bar_width,
                alpha=opacity,
                color=city_colors.get(city, "gray"),
                label=f"{city} ({year})")

plt.xlabel("Month")
plt.ylabel("Value")
plt.title("Combined Data by Year and City")

plt.xticks(range(1, 13))  # x 축의 tick 위치를 1부터 12까지 설정
plt.legend()
plt.savefig('final_graph3.png')
plt.show()

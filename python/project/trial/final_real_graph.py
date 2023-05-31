import pymongo
import os
import json
import matplotlib.pyplot as plt
import pandas as pd

from pymongo import MongoClient
from matplotlib import font_manager, rc

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

df = pd.concat(df_list)
df = df.reset_index(drop=True)

print(df)

# 그래프 그리기
plt.figure(figsize=(10, 6))

bar_width = 0.2
opacity = 0.8
colors = ["red", "blue", "green", "orange"]

for i, city in enumerate(df["City"].unique()):
    city_data = df[df["City"] == city]
    values = []
    for index, row in city_data.iterrows():
        count_data = row.to_dict()
        for key in count_data:
            if key != "Year" and key != "City":
                values.append(count_data[key])
    x = range(1, 13)  # 1부터 12까지의 월을 나타내는 range 생성
    y = values[:12]  # 첫 12개의 값만 사용 (월별 데이터)

    # 막대 그래프 그리기
    plt.bar([p + i * bar_width for p in x], y, bar_width,
            alpha=opacity,
            color=colors[i % len(colors)],
            label=city)

plt.xlabel("Month")
plt.ylabel("Value")
plt.title("Combined Data")

plt.xticks(range(1, 13))  # x 축의 tick 위치를 1부터 12까지 설정
plt.legend()
plt.savefig('final_graph.png')
plt.show()

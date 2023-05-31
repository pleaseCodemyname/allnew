import os
import json
import pandas as pd
import matplotlib.pyplot as plt
from pymongo import MongoClient

# 폰트 설정
plt.rcParams['font.family'] = 'AppleGothic'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
secret_file = os.path.join(BASE_DIR, "../secret.json")

with open(secret_file) as f:
    secrets = json.load(f)


def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        errorMsg = "Set the {} environment variable.".format(setting)
    return errorMsg


# MongoDB 연결
HOSTNAME = get_secret("ATLAS_Hostname")
USERNAME = get_secret("ATLAS_Username")
PASSWORD = get_secret("ATLAS_Password")

client = MongoClient(f"mongodb+srv://{USERNAME}:{PASSWORD}@{HOSTNAME}")
db = client["project"]
collections = [db["collection2018"], db["collection2020"], db["collection2022"], db["collection2023"]]

# 데이터프레임 생성
df_list = []
year_list = [2018, 2020, 2022, 2023]

for year, collection in zip(year_list, collections): #zip([2018, 2020, 2022, 2023], db["collections2018~2023"])
    data = collection.find({}, {"_id": 0, "year":1, "counts": 1}) #collection에 있는 id(key): 0(value)만 제외하고 나머지는 다 가져옴
    
    if data:
        counts = data["counts"] 
        df = pd.DataFrame(counts).T.reset_index()
        df.columns = ["City"] + list(df.columns[1:])
        df["City"] = df["City"].str.split("|").str[1]
        df["Year"] = year
        df = df[["Year", "City"] + list(df.columns[1:-1])]
        df_list.append(df)

if df_list:
    df = pd.concat(df_list)
    df = df.reset_index(drop=True)

    # 그래프 그리기
    plt.figure(figsize=(12, 4))

    # 도시별 색상 매핑 딕셔너리
    city_colors = {"도쿄": "red", "오사카": "blue", "후쿠오카": "green"}

    # 도시별 그래프 그리기
    for i, city in enumerate(["도쿄", "오사카", "후쿠오카"]):
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

                bars = plt.bar(x, y, bar_width, alpha=opacity, color=city_colors.get(city, "gray"))
                handles.append(bars[0])
                labels.append(str(year))

                # 막대 위에 값 표시
                for j, v in enumerate(y):
                    plt.text(x[j], v + 0.5, str(v), ha='center')

        plt.xlabel("Month")
        plt.ylabel("Count")
        plt.title(f"{city} 데이터")
        plt.xticks(range(1, 13))
        plt.ylim(0, 25)  # y축 범위 설정
        plt.legend(handles, labels)

    plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.4, hspace=0.4)  # 그래프 간격 조정

    plt.savefig('final_graph4.png')
    plt.clf()
    plt.show()
else:
    print("데이터가 없습니다.")

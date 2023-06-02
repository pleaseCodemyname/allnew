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
#client = MongoClient(f"mongodb+srv://{USERNAME}:{PASSWORD}@{HOSTNAME}")
#db = client["project"]
#collections = [db["collection2018"], db["collection2020"], db["collection2022"], db["collection2023"]]

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

# 인덱스 데이터를 리스트로 변환
month_list = list(df2.Month.unique())
city_list = list(df2.City.unique())

# 그래프 그리기
plt.figure(figsize=(20,10))
city_dict = {}
for city in city_list:
    data = df2[df2['City'] == city].groupby('Month')['Count'].sum().reindex(month_list, fill_value=0)
    city_dict[city] = list(data)
    plt.plot(month_list, data, label=city)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('Month', fontsize=18)
plt.ylabel('Count', fontsize=18)
plt.legend(title='City', loc='best', fontsize=15)
plt.show()

#그래프 그리기
# for city in df["City"]:
#     plt.plot(df.columns[1:], df.loc[df["City"] == city].values[0][1:], marker='o', label=city)

# # 그래프 레이블 및 제목 설정
# plt.xlabel('Month')
# plt.ylabel('Count')
# plt.title('2018 Youtube Titles&Tags Cities Word Counts')

# # 범례 표시
# plt.legend()

# # 그래프 저장
# plt.savefig('final_graph.png')
# # 그래프 보여주기
# plt.show()

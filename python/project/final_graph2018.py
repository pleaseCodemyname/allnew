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
collection = db["collection2018"]

# 컬렉션에서 데이터 가져오기
data = collection.find_one({}, {"_id": 0, "counts": 1})["counts"]

# 데이터프레임 생성
df = pd.DataFrame(data).T.reset_index()
df.columns = ["City"] + list(df.columns[1:])

# 도시 그룹 컬럼 이름 수정
df["City"] = df["City"].str.split("|").str[1]

# 출력
print(df)
# 그래프 그리기
for city in df["City"]:
    plt.plot(df.columns[1:], df.loc[df["City"] == city].values[0][1:], marker='o', label=city)

# 그래프 레이블 및 제목 설정
plt.xlabel('Month')
plt.ylabel('Count')
plt.title('2018 Youtube Titles&Tags Cities Word Counts')

# 범례 표시
plt.legend()

# 그래프 저장
plt.savefig('final_2018graph.png')
# 그래프 보여주기
plt.show()

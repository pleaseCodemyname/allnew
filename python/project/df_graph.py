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


def create_dataframe_and_graph(year):
    # 몽고DB 연결
    client = MongoClient(f"mongodb+srv://{USERNAME}:{PASSWORD}@{HOSTNAME}")
    db = client["project"]
    # 컬렉션 선택
    collection_name = f"collection{year}"
    collection = db[collection_name]
    
    # 컬렉션에서 데이터 가져오기
    data = collection.find_one({}, {"_id": 0, "counts": 1})["counts"]

    # 데이터프레임 생성
    df = pd.DataFrame(data).T.reset_index()
    df.columns = ["City"] + list(df.columns[1:])

    # 도시 그룹 컬럼 이름 수정
    df["City"] = df["City"].str.split("|").str[1]

    # 그래프 그리기
    fig, ax = plt.subplots()
    for city in df["City"]:
        ax.plot(df.columns[1:], df.loc[df["City"] == city].values[0][1:], marker='o', label=city)

    # 그래프 레이블 및 제목 설정
    ax.set_xlabel('Month')
    ax.set_ylabel('Count')
    ax.set_title(f'{year} Youtube Titles&Tags Cities Word Counts')

    # 범례 표시
    ax.legend()

    # 그래프 저장
    graph_filename = f'final_{year}graph.png'
    fig.savefig(graph_filename)
    plt.close(fig)

    return graph_filename, df
#main.py
import os
import json
import calendar
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from googleapiclient.discovery import build
from datetime import datetime
from fastapi import FastAPI
from pymongo import MongoClient
from bson import ObjectId
from collections import defaultdict
from typing import List

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# secret.json 파일에서 API 키를 가져옵니다.
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

# Atlas API 정보
HOSTNAME = get_secret("ATLAS_Hostname")
USERNAME = get_secret("ATLAS_Username")
PASSWORD = get_secret("ATLAS_Password")

# Secret.json의 API 키
api_key = secrets["jy_youtube_apiKey4"]
youtube = build("youtube", "v3", developerKey=api_key)

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return FileResponse("static/index2.html")

# FastAPI1(유튜브에서 일본여행을 검색했을때의 영상의 제목, 조회수, 게시날짜 및 Tag 가져오기)
@app.get("/youtube")
async def get_youtube_videos(keyword: str = ""):
    global result
    result = []
    years = [2018, 2020, 2022, 2023]

    for year in years:
        months = range(1, 13) if year != 2023 else range(1, 6)

        for month in months:
            _, last_day = calendar.monthrange(year, month)
            published_after_date = datetime(year, month, 1)
            published_before_date = datetime(year, month, last_day)

            search_request = youtube.search().list(
                part="snippet",
                q=keyword,
                order="viewCount",
                type="video",
                publishedAfter=published_after_date.isoformat("T") + "Z",
                publishedBefore=published_before_date.isoformat("T") + "Z",
                maxResults=5,
            )

            search_response = search_request.execute()

            for item in search_response["items"]:
                video_id = item["id"]["videoId"]
                video_request = youtube.videos().list(part="snippet,statistics", id=video_id)
                video_response = video_request.execute()
                video_info = video_response["items"][0]

                tags = video_info["snippet"]["tags"] if "tags" in video_info["snippet"] else []
                video_info["snippet"]["tags"] = tags

                result.append({
                    "_id": str(ObjectId()),
                    "Title": video_info["snippet"]["title"],
                    "View Count": video_info["statistics"]["viewCount"],
                    "Published At": video_info["snippet"]["publishedAt"],
                    "Tags": tags
                })

    client = MongoClient(f"mongodb+srv://{USERNAME}:{PASSWORD}@{HOSTNAME}")
    db = client["project"]
    db.drop_collection("alldata")
    collection = db["alldata"]

    for item in result:
        collection.insert_one(item)

    return result

# FastAPI2(/youtube로 불러온 전체 데이터를 연도별 리스트로 묶어놓은 것)
@app.get("/youtube_list")
async def get_youtube_videos():
    client = MongoClient(f"mongodb+srv://{USERNAME}:{PASSWORD}@{HOSTNAME}")
    db = client["project"]
    collection = db["alldata"]

    data = list(collection.find())

    year_data_dict = defaultdict(list)

    for item in data:
        year = int(item["Published At"][0:4])
        year_data_dict[year].append(item)

    year_data_list = [{"Year": year, "Data": items} for year, items in sorted(year_data_dict.items())]

    with open("dataset.json", "w", encoding="utf-8") as file:
        json.dump(year_data_list, file, ensure_ascii=False, default=json_util.default)

    collection_list = db["alldata_list"]
    db.drop_collection("alldata_list")
    collection_list.insert_many(json.loads(json_util.dumps(year_data_list)))

    return year_data_list

# FastAPI 4 (년도별 월별 도쿄, 오사카, 후쿠오카 (한글, 영문) 언급 횟수 Count)
@app.get("/find/{year}")
async def find_year_data(year: int):
    client = MongoClient(f"mongodb+srv://{USERNAME}:{PASSWORD}@{HOSTNAME}")
    db = client["project"]
    collection = db["alldata_list"]

    result = collection.find_one({"Year": year})
    if result is None:
        return {"message": "No data found for the given year"}

    data = result["Data"]

    city_groups = {'도쿄 | Tokyo': ['도쿄', 'Tokyo'], '오사카 | Osaka': ['오사카', 'Osaka'], '후쿠오카 | Fukuoka': ['후쿠오카', 'Fukuoka']}
    years = ['2018', '2020', '2022', '2023']

    months_2023 = range(1, 6) if datetime.now().year == 2023 else range(1, 13)

    if str(year) not in years:
        return {"error": "잘못된 연도입니다."}

    if year == 2023:
        valid_months = months_2023
    else:
        valid_months = range(1, 13)

    count_dict = {city_group: {str(month): 0 for month in valid_months} for city_group in city_groups}

    for item in data:
        title = item["Title"]
        tags = item["Tags"]
        published_at = item["Published At"]
        month = int(published_at.split("-")[1])

        if month in valid_months:
            for city_group, city_names in city_groups.items():
                count = sum(len(re.findall(city_name, title, re.IGNORECASE)) for city_name in city_names) + sum(len(re.findall(city_name, tag, re.IGNORECASE)) for city_name in city_names for tag in tags)
                count_dict[city_group][str(month)] += count

    collection_name = f"collection{str(year)}"
    db.drop_collection(f"collection{str(year)}")
    db[collection_name].insert_one({"year": year, "counts": count_dict})

    return {
        "year": year,
        "counts": count_dict
    }

# FastAPI5
@app.get("/combined_graph")
async def get_combined_graph():
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

    # 그래프 그리기
    plt.figure(figsize=(12, 4))

    # 년도별 색상 매핑 딕셔너리
    year_colors = {2018: "black", 2020: "orange", 2022: "blue", 2023: "pink"}

    # 도시별 그래프 그리기
    for i, city in enumerate([" Tokyo", " Osaka", " Fukuoka"]):
        plt.subplot(1, 3, i + 1)
        handles = []
        labels = []

        # 년도별 그래프 그리기
        for year in [2018, 2020, 2022, 2023]:
            city_data = df[(df["Year"] == year) & (df["City"] == city)]
            if not city_data.empty:
                x = range(1, 13)  # 월
                y = city_data.iloc[:, 2:].values[0]  # 도시별 월별 데이터

                # Skip plotting bars with a value of NaN
                y = np.nan_to_num(y, nan=0.0)

                bar_width = 0.5  # 막대 그래프의 너비
                opacity = 0.8  # 막대 그래프의 투명도

                bars = plt.bar(x, y, bar_width,
                                alpha=opacity,
                                color=year_colors.get(year, "gray"))
                handles.append(bars[0])
                labels.append(str(year))

                # 막대 위에 값 표시 (0.0은 제외)
                for j, v in enumerate(y):
                    if v != 0:
                        plt.text(x[j], v + 0.5, str(int(v)), ha='center')

        plt.xlabel("Month")
        plt.ylabel("Count")
        plt.title(f"{city} Data")
        plt.xticks(range(1, 13))

        y_min = np.nanmin(df.iloc[:, 2:].values)
        y_max = np.nanmax(df.iloc[:, 2:].values)
        plt.ylim(ymin=0, ymax=30)
        plt.legend(handles, labels)
        legend = plt.legend(handles, labels, loc='upper right', bbox_to_anchor=(1, 1), fontsize='small')

    plt.tight_layout()  # 그래프 간격 조정

    combined_graph_filename = 'final_combined_graph.png'
    plt.savefig(combined_graph_filename)
    plt.close()  # Close the plot to release resources

    # 이미지 파일을 FastAPI의 FileResponse로 반환
    return FileResponse(combined_graph_filename, media_type="image/png")


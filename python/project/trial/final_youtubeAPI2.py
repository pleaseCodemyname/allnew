import os
import json
import calendar
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from fastapi.responses import FileResponse
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from bson import json_util
from googleapiclient.discovery import build
from datetime import datetime
from fastapi import FastAPI
from pymongo import MongoClient
from bson import ObjectId
from collections import defaultdict
from typing import List
from df_graph import create_dataframe_and_graph

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
api_key = secrets["youtube_apiKey2"]
youtube = build("youtube", "v3", developerKey=api_key)

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return FileResponse("static/index2.html")

#FastAPI1(유튜브에서 일본여행을 검색했을때의 영상의 제목, 조회수, 게시날짜 및 Tag 가져오기)
@app.get("/youtube") #
async def get_youtube_videos(keyword: str = ""): 
    global result # 전역변수 result 선언
   
    result = []  # 결과를 저장할 리스트
    years = [2018, 2020, 2022, 2023] # 고정된 년도 범위

    for year in years:
        months = range(1, 13) if year != 2023 else range(1, 6) #2018, 2020, 2022는 1~12월 / 2023는 1~6월

        for month in months:
            _, last_day = calendar.monthrange(year, month) #해당 월이 몇일까지 있는지, 해당월의 첫 날짜까 무슨 요일인지 Tuple형태로 반환
            published_after_date = datetime(year, month, 1) #게시월의 시작일 ex) published_after_date는 2022-10-01 00:00:00
            published_before_date = datetime(year, month, last_day) #게시월의 마지막 날짜 ex) published_before_date는 2022-10-31 00:00:00

            search_request = youtube.search().list( #YouTube API에서 제공하는 Search API를 호출하는 메서드
                part="snippet", #함수의 인자 Part = Snippet 유형으로 설정되어 있음, 이는 반환되는 데이터의 종류를 지정, Snippet(비디오 제목, 채널명, 게시 날짜, 비디오에 대한 설명 등의 정보 모두 포함)
                q=keyword, #keyword(검색어)= q에 전달
                order="viewCount", 
                type="video", # 이 코드에서는 비디오(동영상) 타입만을 Search하기 때문에, video = type에 전달
                publishedAfter=published_after_date.isoformat("T") + "Z", # datetime.datetime 클래스의 객체이므로, 검색 API에서 사용하기 위해 isoformat()메소드 사용하여 ISO 형식으로 변환해야함
                publishedBefore=published_before_date.isoformat("T") + "Z", #isoformat()을 호출하면 ex) 2020-02-01T:00:00 반환 / Z문자열 추가하면 UTC시간대임을 나타냄
                maxResults=5,  # 월별로 5개의 동영상 추출
            )

            # YouTube API 요청 응답 코드
            search_response = search_request.execute() #API 요청 값의 JSON 형태의 데이터 값

            for item in search_response["items"]: #요청받은값["items"]
                video_id = item["id"]["videoId"]  #각 동영상의 ID를 추출하여 다시 동영상에 대한 정보를 가져오는 API요청을 보냄
                video_request = youtube.videos().list(part="snippet,statistics", id=video_id)
                video_response = video_request.execute()
                video_info = video_response["items"][0]

                # 태그 정보를 배열 형식으로 변환합니다.
                tags = video_info["snippet"]["tags"] if "tags" in video_info["snippet"] else []
                video_info["snippet"]["tags"] = tags #동영상에 태그가 있으면 태그와 같이 반환, 없으면 []리스트로 반환

                #해당 값 추출하여 result 리스트에 추가
                result.append({
                    "_id": str(ObjectId()), #ObjectId()는 MongoDB에서 직접사용하지 못하고 문자열 형태로 변경되어야 사용 가능함
                    "Title": video_info["snippet"]["title"],
                    "View Count": video_info["statistics"]["viewCount"],
                    "Published At": video_info["snippet"]["publishedAt"],
                    "Tags": tags
                })

    client = MongoClient(f"mongodb+srv://{USERNAME}:{PASSWORD}@{HOSTNAME}")
    db = client["project"]
    db.drop_collection("alldata")
    collection = db["alldata"]

    # Insert the results into MongoDB
    for item in result:
        collection.insert_one(item)

    return result
    result = []

#265개 중 205개가 들어간 이유는 API 제한 사항으로 인해 검색 결과에서 일부 비디오가 누락되었기 때문임.

#FastAPI2(/youtube로 불러온 전체 데이터를 연도별 리스트로 묶어놓은 것)
@app.get("/youtube_list")
async def get_youtube_videos():
    client = MongoClient(f"mongodb+srv://{USERNAME}:{PASSWORD}@{HOSTNAME}")
    db = client["project"]
    collection = db["alldata"]

    data = list(collection.find()) # 모든 데이터 list로 변환

    year_data_dict = defaultdict(list)

    for item in data:
        year = int(item["Published At"][0:4])
        year_data_dict[year].append(item)

    # 리스트로 변환하여 정렬된 결과 얻기
    year_data_list = [{"Year": year, "Data": items} for year, items in sorted(year_data_dict.items())]

    # JSON 파일로 저장
    with open("dataset.json", "w", encoding="utf-8") as file:
        json.dump(year_data_list, file, ensure_ascii=False, default=json_util.default)

    # alldata_list 컬렉션에 데이터 저장
    collection_list = db["alldata_list"]
    db.drop_collection("alldata_list")
    collection_list.insert_many(json.loads(json_util.dumps(year_data_list)))

    return year_data_list

#FastAPI 4 (년도별 월별 도쿄, 오사카, 후쿠오카 (한글, 영문) 언급 횟수 Count)
@app.get("/find/{year}")
async def find_year_data(year: int):
    client = MongoClient(f"mongodb+srv://{USERNAME}:{PASSWORD}@{HOSTNAME}")
    db = client["project"]
    collection = db["alldata_list"]

    # 해당 연도의 데이터 가져오기
    result = collection.find_one({"Year": year})
    if result is None:
        return {"message": "No data found for the given year"}

    data = result["Data"]

    # 연도에 따라 월 범위 설정
    city_groups = {'도쿄|Tokyo': ['도쿄', 'Tokyo'], '오사카|Osaka': ['오사카', 'Osaka'], '후쿠오카|Fukuoka': ['후쿠오카', 'Fukuoka']}
    years = ['2018', '2020', '2022', '2023']  # Year 필드의 값을 문자열로 변경

    months_2023 = range(1, 6) if datetime.now().year == 2023 else range(1, 13)

    if str(year) not in years:  # year를 문자열로 변환하여 비교
        return {"error": "잘못된 연도입니다."}

    if year == 2023: #year이 2023이면
        valid_months = months_2023 #valid months(5월까지만)
    else:
        valid_months = range(1, 13) #아니면(12월까지)

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

#FastAPI5
@app.get("/graph/{year}")
async def create_data(year: int):
    if year not in [2018, 2020, 2022, 2023]:
        return "Invalid year"

    graph_filename, df = create_dataframe_and_graph(year)

    # 그래프 파일을 클라이언트에게 반환
    return FileResponse(graph_filename, media_type="image/png")

#FastApi 6
@app.get("/combined_graph")
async def get_combined_graph():
    def combined_graph():
        fig = Figure(figsize=(12, 4))
        canvas = FigureCanvas(fig)

        # 그래프 그리기 코드 생략

        graph_filename = "combined_graph.png"
        canvas.print_png(graph_filename)
        return graph_filename

    graph_filename = combined_graph()
    return FileResponse(graph_filename, media_type='image/png')

# @app.get("/combined_graph")
# def get_graph():
#     global df
#     if df is None:
#         # 데이터프레임 생성 및 초기화하는 코드 추가
#         # ...

#     data = df.to_dict()  # 데이터프레임을 딕셔너리로 변환
#     return {
#         "data": data,
#         "graph_filename": graph_filename
#     }

@app.get("/combined_graphs")
async def get_combined_graph():
# 폰트 설정
    plt.rcParams['font.family'] = 'AppleGothic'
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath("./")))
    secret_file = os.path.join(BASE_DIR, "../secret.json")

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

            # Skip plotting bars with a value of 0.0
            if np.count_nonzero(y) > 0:
                bar_width = 0.5  # 막대 그래프의 너비
                opacity = 0.8  # 막대 그래프의 투명도

                bars = plt.bar(x, y, bar_width,
                               alpha=opacity,
                               color=year_colors.get(year, "gray"))
                handles.append(bars[0])
                labels.append(str(year))

                # 막대 위에 값 표시 (0.0은 제외)
                for j, v in enumerate(y):
                    if not np.isnan(v) and v != 0.0 and np.isfinite(v):
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
plt.show()

# 그래프 파일명과 데이터프레임 반환
combined_graph_data = {
    "graph_filename": combined_graph_filename,
    "data": df.to_dict(orient="records")
}
import os
import json
import calendar
import re

from bson import json_util
from urllib.parse import quote
from googleapiclient.discovery import build
from datetime import datetime
from fastapi import FastAPI
from pymongo import MongoClient
from bson import ObjectId
from collections import defaultdict

app = FastAPI()

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
api_key = secrets["youtube_apiKey4"]
youtube = build("youtube", "v3", developerKey=api_key)

@app.get("/youtube")
async def get_youtube_videos(keyword: str = "일본여행"):
    global result
    # 결과를 저장할 리스트
    result = []

    # 고정된 년도 범위
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
                maxResults=5,  # 월별로 5개의 동영상 추출
            )

            # YouTube API 요청 실행
            search_response = search_request.execute()

            for item in search_response["items"]:
                video_id = item["id"]["videoId"]
                video_request = youtube.videos().list(part="snippet,statistics", id=video_id)
                video_response = video_request.execute()
                video_info = video_response["items"][0]

                # 태그 정보를 배열 형식으로 변환합니다.
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
    collection = db["alldata"]

    # Insert the results into MongoDB
    for item in result:
        collection.insert_one(item)

    return result
    result = []

#265개 중 205개가 들어간 이유는 API 제한 사항으로 인해 검색 결과에서 일부 비디오가 누락되었기 때문임.


#FastAPI2

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
    collection_list.insert_many(json.loads(json_util.dumps(year_data_list)))

    return year_data_list

@app.get("/find/{year}")
async def find_year_data(year: int):
    client = MongoClient(f"mongodb+srv://{USERNAME}:{PASSWORD}@{HOSTNAME}")
    db = client["project"]
    collection = db["alldata_list"]

    city_names = ['도쿄', '오사카', '후쿠오카']
    years = [2018, 2020, 2022, 2023]
    months_2023 = range(1, 6) if datetime.now().year == 2023 else range(1, 13)

    if year not in years:
        return {"error": "잘못된 연도입니다."}

    if year == 2023:
        valid_months = months_2023
    else:
        valid_months = range(1, 13)

    count_dict = {city_name: {str(month): 0 for month in valid_months} for city_name in city_names}

    for item in collection.find({"Year": str(year)}):
        for video in item["Data"]:
            month = str(int(video["Published At"][5:7]))
            if month in valid_months:
                for city_name in city_names:
                    title_word_count = len(re.findall(r'\b{}\b'.format(city_name), video["Title"], flags=re.IGNORECASE))
                    tag_word_count = sum(len(re.findall(r'\b{}\b'.format(city_name), tag, flags=re.IGNORECASE)) for tag in video["Tags"])
                    count_dict[city_name][month] += title_word_count + tag_word_count

    result = {
        "_id": str(ObjectId()),
        "year": str(year),
        "count_dict": count_dict
    }

    collection_name = f"collection{str(year)}"
    db[collection_name].insert_one(result)

    return result


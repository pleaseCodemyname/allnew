import os
import json
import calendar
import csv

from urllib.parse import quote
from googleapiclient.discovery import build
from datetime import datetime
from fastapi import FastAPI
from pymongo import MongoClient
from bson import ObjectId

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
api_key = secrets["youtube_apiKey2"]
youtube = build("youtube", "v3", developerKey=api_key)

@app.get("/alldata")
async def get_all_data(keywords: str = "일본여행"):
    all_data = []

    years = [2018, 2020, 2022, 2023]

    for year in years:
        videos = await get_youtube_videos(keywords, year)
        all_data.extend(videos)

    return all_data

async def get_youtube_videos(keywords: str, year: int):
    result = []

    if year not in [2018, 2020, 2022, 2023]:
        raise ValueError("Year must be 2018, 2020, 2022, or 2023")

    encoded_keywords = quote(keywords)

    for month in range(1, 13):
        _, last_day = calendar.monthrange(year, month)
        published_after_date = datetime(year, month, 1)
        published_before_date = datetime(year, month, last_day)

        search_request = youtube.search().list(
            part="snippet",
            q=keywords,
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
    collection = db["alldata"]
    collection.insert_many(result)
    client.close()

    return result
#265개 중 205개가 들어간 이유는 API 제한 사항으로 인해 검색 결과에서 일부 비디오가 누락되었기 때문임.

@app.get("/youtube")
async def get_youtube_videos(year: int):
    if year not in [2018, 2020, 2022, 2023]:
        raise ValueError("Year must be 2018, 2020, 2022, or 2023")
    else:
        # MongoDB에서 해당 연도의 데이터를 가져옵니다.
        client = MongoClient(f"mongodb+srv://{USERNAME}:{PASSWORD}@{HOSTNAME}")
        db = client["project"]
        collection = db["alldata"]
        videos = collection.find({}, {"_id": 0}) #id를 제외하고 나머지 필드만 반환

    return list(videos)

    
    # if year == 2018:
    #     db.drop_collection("data_2018")
    #     collection = db["data_2018"]
    #     csv_file = "/allnew/python/project/arin_2018.csv"
    # elif year == 2020:
    #     db.drop_collection("data_2020")
    #     collection = db["data_2020"]
    #     csv_file = "/allnew/python/project/arin_2020.csv"
    # elif year == 2022:
    #     db.drop_collection("data_2022")
    #     collection = db["data_2022"]
    #     csv_file = "/allnew/python/project/arin_2022.csv"
    # elif year == 2023:
    #     db.drop_collection("data_2023")
    #     collection = db["data_2023"]
    #     csv_file = "/allnew/python/project/arin_2023.csv"
    # else:
    #     raise ValueError("Year must be 2018, 2020, 2022 or 2023")
    
    # # Save the results in a CSV file
    # with open(csv_file, "w", newline="", encoding="utf-8") as file:
    #     writer = csv.writer(file)
    #     writer.writerow(["Title", "View Count", "Published At", "Tags"])
    #     for item in result:
    #         writer.writerow([item["Title"], item["View Count"], item["Published At"], item["Tags"]])

    # # Insert the results into MongoDB
    # for item in result:
    #     collection.insert_one(item)
    
    # return result
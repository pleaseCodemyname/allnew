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
#HOSTNAME = get_secret("ATLAS_Hostname")
#USERNAME = get_secret("ATLAS_Username")
#PASSWORD = get_secret("ATLAS_Password")

# Secret.json의 API 키
#api_key = secrets["jy_youtube_apiKey"]
#youtube = build("youtube", "v3", developerKey=api_key)

@app.get("/alldata")
async def get_all_data():
    all_data = []
    keywords = "일본여행"

    for year in [2018, 2020, 2022, 2023]:
        videos = await get_youtube_videos(keywords, year)
        all_data.extend(videos)

    # Save the data to MongoDB
    # project.insert_many(all_data)

    return {"message": "All data has been retrieved and stored in the database."}


@app.get("/youtube")
async def get_youtube_videos(keywords: str, year: int):
    global result
# 결과를 저장할 리스트
    result = []

    if year not in [2018, 2020, 2022, 2023]:
        raise ValueError("Year must be 2018, 2020, 2022 or 2023")

    encoded_keywords = quote(keywords) #한글 키워드를 URL 인코딩

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

        #request값 요청한 것 reponse에 담는 과정
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
    
    if year == 2018:
        db.drop_collection("data_2018")
        collection = db["data_2018"]
        csv_file = "/allnew/python/project/arin_2018.csv"
    elif year == 2020:
        db.drop_collection("data_2020")
        collection = db["data_2020"]
        csv_file = "/allnew/python/project/arin_2020.csv"
    elif year == 2022:
        db.drop_collection("data_2022")
        collection = db["data_2022"]
        csv_file = "/allnew/python/project/arin_2022.csv"
    elif year == 2023:
        db.drop_collection("data_2023")
        collection = db["data_2023"]
        csv_file = "/allnew/python/project/arin_2023.csv"
    else:
        raise ValueError("Year must be 2018, 2020, 2022 or 2023")
    
    # Save the results in a CSV file
    with open(csv_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "View Count", "Published At", "Tags"])
        for item in result:
            writer.writerow([item["Title"], item["View Count"], item["Published At"], item["Tags"]])

    # Insert the results into MongoDB
    for item in result:
        collection.insert_one(item)
    
    return result
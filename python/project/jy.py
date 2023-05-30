from fastapi import FastAPI, Query
from pymongo import MongoClient
import pandas as pd
import numpy as np
import json
from googleapiclient.discovery import build
from datetime import datetime
import calendar
from collections import defaultdict
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath("./")))
secret_file = os.path.join(BASE_DIR, "../secret.json")
with open(secret_file) as f:
    secret_data = json.load(f)
api_key = secret_data["jy_youtube_apiKey2"]
youtube = build("youtube", "v3", developerKey=api_key)

HOSTNAME = secret_data["ATLAS_Hostname"]
USERNAME = secret_data["ATLAS_Username"]
PASSWORD = secret_data["ATLAS_Password"]
client = MongoClient(f"mongodb+srv://{USERNAME}:{PASSWORD}@{HOSTNAME}")
db = client["project"]
collection = db["data_2018"]


@app.get("/youtube")
async def get_youtube_videos(keywords: str, year: int, month: int):
    if month not in range(1, 13):
        raise ValueError("Month must be between 1 and 12")
    if year not in [2018, 2020, 2022]:
        raise ValueError("Year must be 2018, 2020, or 2022")

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
        maxResults=50,
    )

    search_response = search_request.execute()
    result = []

    for item in search_response["items"]:
        video_id = item["id"]["videoId"]
        video_request = youtube.videos().list(part="snippet,statistics", id=video_id)
        video_response = video_request.execute()
        video_info = video_response["items"][0]
        result.append(
            {
                "Title": video_info["snippet"]["title"],
                "View Count": video_info["statistics"]["viewCount"],
                "Published At": video_info["snippet"]["publishedAt"],
                "Tags": video_info["snippet"]["tags"]
                if "tags" in video_info["snippet"]
                else "No tags.",
            }
        )
    
    for item in result:
        collection.insert_one(item)
    
    return result
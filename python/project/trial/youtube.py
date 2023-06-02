import os
import json
import calendar
from googleapiclient.discovery import build
from datetime import datetime
from collections import defaultdict
from fastapi import FastAPI

# FastAPI 인스턴스 생성
app = FastAPI()

# YouTube API 키 및 기타 설정 가져오기
BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath("./")))
secret_file = os.path.join(BASE_DIR, "../secret.json")

with open(secret_file) as f:
    secrets = json.load(f)

#api_key = secrets["jy_youtube_apiKey"]
#youtube = build("youtube", "v3", developerKey=api_key)

@app.get("/youtube")
async def count_video_info(keyword: str, year: int):
    result = defaultdict(int)

    for month in range(1, 13):
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
            maxResults=1,
        )

        search_response = search_request.execute()

        for item in search_response["items"]:
            video_id = item["id"]["videoId"]
            video_request = youtube.videos().list(part="snippet", id=video_id)
            video_response = video_request.execute()
            video_info = video_response["items"][0]
            title = video_info["snippet"]["title"]
            tag_count = len(video_info["snippet"].get("tags", []))
            result[month] += 1
            result[(month, "title")] += 1
            result[(month, "tag_count")] += tag_count

    return dict(result)

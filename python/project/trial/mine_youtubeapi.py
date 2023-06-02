from fastapi import FastAPI
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser
from pymongo import MongoClient
import os
import json
import pandas as pd

app = FastAPI()

# Load your YouTube API credentials
BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath("./")))
secret_file = os.path.join(BASE_DIR, '../secret.json')
with open(secret_file) as f:
    secrets = json.loads(f.read())

#DEVELOPER_KEY = "AIzaSyB0vDBPwjFp2u2uSoQFGVhtu_CXTFuoLiM"
#YOUTUBE_API_SERVICE_NAME = "youtube"
#YOUTUBE_API_VERSION = "v3"

# Create a YouTube API client
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

@app.get("/youtube")
async def get_youtube_data():
    try:
        search_response = youtube.search().list(
            q="", #값에따라 바뀜 결과값이 바뀜
            order="relevance",
            part="snippet",
            maxResults=50
        ).execute()

        titles = []
        for item in search_response['items']:
            titles.append(item['snippet']['title'])

        data = []
        for item in search_response['items']:
            item_dict = {}
            item_dict['q'] = item['snippet']['title']
            # Add other necessary information to item_dict
            data.append(item_dict)

        df = pd.DataFrame(data)

        return {"titles": titles, "data": df.to_dict()}
    except HttpError as e:
        return {"error": str(e)}




from fastapi import FastAPI
from pymongo import MongoClient
import requests
import json
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath("./")))
secret_file = os.path.join(BASE_DIR, "../secret.json")

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        errorMsg = "Set the {} environment variable.".format(setting)
        return errorMsg

HOSTNAME = get_secret("ATLAS_Hostname")
USERNAME = get_secret("ATLAS_Username")
PASSWORD = get_secret("ATLAS_Password")

client = MongoClient(f"mongodb+srv://{USERNAME}:{PASSWORD}@{HOSTNAME}")
print("Connected to MongoDB....")

db = client["miniProject2"]
collection = db["2018count"]  # 찾아오는 데이터

@app.get("/find")
async def find_videos(year: int, keyword: str):
    months = range(1, 13)  # 1월부터 12월까지의 월
    years = [2018, 2020, 2022, 2023]  # 2018년부터 2023년까지의 연도
    city_names = ['도쿄', '오사카', '후쿠오카']  # 검색하려는 도시 리스트

    # 연도별 월별 도시별 키워드 카운트를 저장할 딕셔너리
    count_dict = {year: {month: {city: 0 for city in city_names}
                         for month in months} for year in years}

    for year in years:
        for month in months:
            if year == 2023 and month > 3:  # 2023년은 3월까지만 데이터가 있다고 하셨으므로
                break

            # URL에서 JSON 데이터를 가져와서 youtube_videos 변수에 저장
            url = f"http://192.168.1.79:3000/youtube?keywords={keyword}&year={year}"
            response = requests.get(url)
            if response.status_code == 200:
                youtube_videos = response.json()
            else:
                print("요청에 실패했습니다. 상태 코드:", response.status_code)
                continue

            titles = [video["Title"] for video in youtube_videos]
            tags = [
                video["Tags"] if video["Tags"] != "No tags." else []
                for video in youtube_videos
            ]
            for city in city_names:
                documents = collection.find({"도시명": city})  # 해당 도시의 모든 문서를 찾음
                for document in documents:
                    # 연도별 월별 도시별 키워드 카운트를 업데이트
                    count_dict[year][month][city] += document.get(
                        str(month), 0)
                for title, tag_list in zip(titles, tags):
                    title_word_count = title.count(keyword)
                    tag_word_count = sum(tag.count(keyword)
                                         for tag in tag_list)
                    count_dict[year][month][city] += title_word_count + tag_word_count  # 연도별 월별 도시별 키워드 카운트를 업데이트
    return count_dict  # 최종 결과를 반환
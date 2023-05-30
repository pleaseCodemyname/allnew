@app.get("/youtube")
async def get_youtube_videos(keywords: str):
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
4
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

from googleapiclient.discovery import build
import pandas as pd
import operator
from fastapi import FastAPI

app = FastAPI()

class JourneyKeywordAPI:
    def __init__(self):
        #self.DEVELOPER_KEY = "AIzaSyB0vDBPwjFp2u2uSoQFGVhtu_CXTFuoLiM"
        #self.YOUTUBE_API_SERVICE_NAME = "youtube"
        #self.YOUTUBE_API_VERSION = 'v3'

    def videoId_likes(self):
        #youtube = build(self.YOUTUBE_API_SERVICE_NAME, self.YOUTUBE_API_VERSION, developerKey=self.DEVELOPER_KEY)

        search_response = youtube.search().list(
            q='#나고다 여행',
            order='viewCount',
            part='snippet',
            maxResults=6
        ).execute()

        videoIds = []
        for i in range(0, len(search_response['items'])):
            videoIds.append((search_response['items'][i]['id']['videoId']))

        channel_title_lst = []
        channel_rating_good = []
        dicts = {}

        for k in range(0, len(search_response['items'])):
            videoIdslists = youtube.videos().list(
                part='snippet, statistics',
                id=videoIds[k],
            ).execute()

            channel_title_lst.append(videoIdslists['items'][0]['snippet'].get('channelTitle'))

            channel_rating_good.append(videoIdslists['items'][0]['statistics'].get('likeCount'))

        for title_plus_rating in zip(channel_title_lst, channel_rating_good):
            dicts[title_plus_rating[0]] = int(title_plus_rating[1])
        sdicts = sorted(dicts.items(), key=operator.itemgetter(1), reverse=True)

        return sdicts

    def channelID_likes_DataFrame(self, sdicts):
        df = pd.DataFrame(sdicts)
        df.columns = ['Channel_title', 'Video_likes']
        return df

journey_api = JourneyKeywordAPI()
sdicts = journey_api.videoId_likes()
df = journey_api.channelID_likes_DataFrame(sdicts)

print("######################################")
print("#                                    #")
print("#            나고다여행               #")
print("#             조회수 TOP6              #")
print("#                                    #")
print("######################################")
print(df)

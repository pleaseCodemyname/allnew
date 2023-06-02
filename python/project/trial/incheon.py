import requests
import json
import pandas as pd
from fastapi import FastAPI
import os.path

BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath("./")))
secret_file = os.path.join(BASE_DIR, '../secret.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        errorMsg = "Set the {} environment variable.".format(setting)
        return errorMsg

app = FastAPI()


@app.get('/departureData')
async def getData():
    #url = 'https://apis.data.go.kr/B551177/StatusOfSrvDestinations/getServiceDestinationInfo'
    
    #params = '?serviceKey=' + get_secret("data_apiKey")
    params += '&airport_code='
    params += '&type=JSON'
    url += params
    print(url)

    response = requests.get(url)
    print(response)
    print('-' * 50)

    contents = response.text
    dict = json.loads(contents)
    items = dict['items'][0]
    
    item = ['airportCode', 'airportName', 'countryName']
    
    validItem = {}
    for _ in item:
        validItem[_] = items[_]
        
    return validItem
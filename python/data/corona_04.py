import requests
import json
import pandas as pd 
from datetime import datetime,timedelta
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

url = 'http://apis.data.go.kr/1352000/ODMS_COVID_02/callCovid02Api'

today = (datetime.today() - timedelta(1)).strftime("%Y%m%d")
print(today)

params = '?serviceKey=' + get_secret("data_apiKey")
params += '&pageNo=1'
params += '&numOfRows=500'
params += '&apiType=JSON'
params += '&status_dt=' + str(today)

url += params
print(url)

response = requests.get(url)
print(response)
print('-' * 50)

contents = response.text
print(type(contents))
print(contents)
print('-' * 50)

dict = json.loads(contents)
print(type(dict))
print(dict)
print('-' * 50)

items = dict['items'][0]
print(type(items))
print(items)
print('-' * 50)


item = ['gPntCnt', 'hPntCnt', 'accExamCnt', 'statusDt']
validItem = {key: value for key, value in items.fromkeys(item).items()}
print(validItem)

validItem = {} #딕셔너리 공백, 딕셔너리 key value 쌍, 그래서 transpose할 필요가 없다. 
for _ in item:
    validItem[_] = items[_]
print(validItem)
print('-' * 50)

df = pd.DataFrame.from_dict(validItem, orient='index').rename(columns={0:"result"}) 
print(type(df))
print(df)
print('-' * 50)
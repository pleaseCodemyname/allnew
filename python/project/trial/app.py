import json, urllib.request, datetime, math
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

def getRequestUrl(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            return response.read().decode('utf-8')
    except Exception as e:
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

def getCurrencyData(searchdate, data):
    end_point = ' https://www.koreaexim.go.kr/site/program/financial/exchangeJSON'
    access_key = '3AF16048417F43BD9AE611C6879E0550E063A7DE'
	

    parameters = ''
    parameters += "?resultType=json"
    parameters += "&authkey=" + get_secret("currency_apiKey")
    parameters += "&searchdate=" + str(searchdate) 
    parameters += "&data=" + str(data)  
    url = end_point + parameters

    print('URL')
    print(url)

    result = getRequestUrl(url)
    if (result == None):
        return None
    else:
        return json.loads(result)

jsonResult = []

searchdate = 20210506 
data = 1
while(True):
    print('searchdate : %d, data : %d' % (searchdate, data))
    jsonData = getCurrencyData(searchdate, data)
    print(jsonData)

    # if (jsonData['CurrencyInfo']['header']['resultCode'] == '00'):
    #     totalCount = jsonData['MedicalInstitInfo']['body']['totalCount']
    #     print('데이터 총 개수 : ', totalCount)  

    #     for item in jsonData['MedicalInstitInfo']['body']['items']['item']:
    #         jsonResult.append(item)

    #     if totalCount == 0:
    #         break
    #     nPage = math.ceil(totalCount / numOfRows)
    #     if (pageNo == nPage):  
    #         break  

    #     pageNo += 1
    # else :
    #     break

    # savedFilename = 'currency.json'
    # with open(savedFilename, 'w', encoding='utf8') as outfile:
    #     retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
    #     outfile.write(retJson)

    # print(savedFilename + ' file saved..')



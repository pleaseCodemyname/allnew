import requests
import json

url = r"http://192.168.1.77:3000/all_yeardatatop10?year=2018"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    # JSON 데이터를 파일로 저장합니다
    with open("asdf.json", "w") as file:
        json.dump(data, file)

    print("데이터를 성공적으로 저장했습니다.")
else:
    print("요청에 실패했습니다. 상태 코드:", response.status_code)

# a = {"노선" : "인천(ICN)", 
#     "상대공항" : "간사이",
#     "운항" : "9886"   }

# print(type(a))
# print(a)
# print(a['노선'])

# q = {'a' : 1, 'b' : 2}
# print(type(q))
# print(q.values())

# change = list(q.values())
# print(change)
# print(change[0])

# #youtube에서 "일본 여행" 검색했을때 "일본"만 추출해서, 연도별 월별 top10 
# search = {q : "일본 여행"}


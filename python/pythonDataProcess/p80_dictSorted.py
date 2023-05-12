wordInfo = {'세탁기' : 50, '선풍기' : 30, '청소기' : 40, '냉장고': 60}

myxticks = sorted(wordInfo, key= wordInfo.get, reverse=True) #값에 의한 정렬, key를 받아서 값에 의한 정렬 (value 값이 큰것부터 정렬) / reverse가 desc / asc 역할
print(myxticks) # ['냉장고', '세탁기', '청소기', '선풍기'] / wordInfo.get('세탁기') = 50이 반환됨

reverse_key = sorted(wordInfo.keys(), reverse=True)
print(reverse_key) # ['청소기', '세탁기', '선풍기', '냉장고'] #ㄱ~ㅎ 역순으로 정렬한 것임

chartdata = sorted(wordInfo.values(), reverse=True)
print(chartdata) # [60, 50, 40, 30]
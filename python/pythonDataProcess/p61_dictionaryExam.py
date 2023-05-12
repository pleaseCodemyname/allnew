dictionary = {'김유신' : 50, '윤봉길' : 40, '김구' : 60}
print('dictionary list : ', dictionary)

for key in dictionary.keys():
    print(key) #김유신/윤봉길/김구 ##key값 출력

for value in dictionary.values():
    print(value) #50/40/60 ##value값 출력

for key in dictionary.keys():
    print('{}의 나이는 {}입니다.'.format(key, dictionary[key]))
# 김유신의 나이는 50입니다/윤봉길의 나이는 40입니다/김구의 나이는 60입니다.

for key, value in dictionary.items():
    print('{}의 나이는 {}입니다.'.format(key, value)) #items를 사용하면 key:value 값 전체로 가져옴
# 김유신의 나이는 50입니다/윤봉길의 나이는 40입니다/김구의 나이는 60입니다.


findKey = '유관순'

if findKey in dictionary:
    print(findKey + '(은)는 존재합니다.')
else:
    print(findKey + '(은)는 존재하지 않습니다.')
#유관순(은)는 존재하지 않습니다.

result = dictionary.pop('김구')
print(result) # 60 '김구'라는 key값은 삭제되고 value=60 만 남아서 result에 할당되었음.
print('After pop dictionary : ', dictionary) # After pop dictionary :  {'김유신': 50, '윤봉길': 40}
print('pop value : ', result) # pop value : 60 / 왜 result에 value 값만 나오는건가?

dictionary.clear()
print('dictionary list : ', dictionary)
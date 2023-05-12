import re

mylist = ['ab123', 'cd456', 'ef789', 'abc12']

regex = '[a-z]{2}\d{3}'
pattern = re.compile(regex)

print('# 문자열 2개, 숫자 3개 패턴 찾기')
totallist = []
for a in mylist:
    if pattern.match(a):
        print(a, '은(는) 조건에 적합')
        totallist.append(a)
    else:
        print(a, '은(는) 조건에 부적합')
print('조건에 적합한 항목들')
print(totallist)
#re = regular expression
#내용은 다르지만 패턴이 같은 것을 "Pattern Matching"
# ^= 행의 시작 / $ = 행의 끝
#[a]{2} =ar가 2번 반복
#\d
#finditer = 반복 가능한 객체로 반환


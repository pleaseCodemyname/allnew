from bs4 import BeautifulSoup

html = open('fruits.html', 'r', encoding="utf-8")
soup = BeautifulSoup(html, 'html.parser')
body = soup.select_one("body")
ptag = body.find('p') #body값에 있는 p를 찾는다
print('1번째 p 태그 : ', ptag['class'])
ptag['class'][1] = 'white' #red를 white로 변경
print('1번째 p 태그 : ', ptag['class'])
ptag['id'] ='apple'
print('-' * 50)

print('1번째 p 태그의 id 속성 : ', ptag['id']) #속성을 apple로 지정해줌
print('-' * 50)

body_tag = soup.find('body') #body부분만 출력
print(body_tag)
print('-' * 50)

idx = 0
print('children 속성으로 하위 항목 보기')
for child in body_tag.children:
    idx += 1
    print(str(idx) + '번째 요소 : ', child)
print('-' * 50)

mydiv = soup.find('div')
print(mydiv)
print('-' * 50)

print('div의 부모 태그')
print(mydiv.parent)
print('-' * 50)

mytag = soup.find("p", attrs={'class': 'hard'})
print(mytag)
print('-' * 50)

print('mytage의 부모 태그는? ')
print(mytag.parent())
print('-' * 50)

print('mytag의 모든 상위 부모 태그들의 이름')
parents = mytag.find_parent()
for p in parents:
    print(p.name)
print('-' * 50)
from urllib.request import urlopen
url = "https://www.airport.kr/co/ko/cpr/statisticCategoryOfLocal.do"
html_data = urlopen(url)
print(html_data.read())
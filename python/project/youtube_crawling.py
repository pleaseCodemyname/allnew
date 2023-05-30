from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
# filename ='/Users/BIT/Downloads/chromedriver_win32/chromedriver.exe'
import time
import pandas as pd

keyword = "일본 여행"
yt_url = f'https://www.youtube.com/results?search_query={keyword}'

driver = webdriver.Chrome()
driver.get(yt_url)

html = bs(driver.page_source, 'lxml')
driver.close()

yt_content = html_select_one('a#video-title')
title = yt_content.get('title')
content_url = 'https://www.youtube.com' + yt_content.get('href')

start_pos = yt_content.get('aria-label').find('조회수') + 4
#rfind(): 문자열에서 마지막에서부터 문자의 위치를 찾는 함수
end_pos = yt_content.get('aria-label').rfind('회')

reviews = yt_content.get('aria-label')[start_pos:end_pos]   
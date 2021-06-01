# 爬取豆瓣电影 top50
import re

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}

response = requests.get('https://movie.douban.com/top250', headers=headers)
html = response.text
# print(html)
'''soup = BeautifulSoup(html, 'lxml')
movie_ol = soup.find('ol', attrs={'class': 'grid_view'})
# print(movie_ol)'''
soup2 = BeautifulSoup(html, 'lxml')
movie_div = soup2.find_all('div', attrs={'class': 'hd'})
# print(movie_div)
# print(type(movie_div))

for i in movie_div:
    # print(type(i))      #<class 'bs4.element.Tag'>

    # movie_title = re.findall(r'class="title">(\w\w\w)</span>', i.text, re.A)
    movie_title = re.findall(r'<a class="" href="(\w\w\w)">', i.text, re.A)
    print(movie_title)





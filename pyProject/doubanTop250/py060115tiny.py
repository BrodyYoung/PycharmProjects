import re
import requests
from bs4 import BeautifulSoup

# 爬取豆瓣电影 top250
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}
url = 'https://movie.douban.com/top250'
response = requests.get(url, headers=headers)
html = response.text

soup = BeautifulSoup(html, 'lxml')

paginator = soup.find('div', attrs={'class': "paginator"})
page_set = set()
page_set.add(url)
for p in paginator.find_all('a'):
    href = p.attrs.get('href')
    page_url = 'https://movie.douban.com/top250' + href
    page_set.add(page_url)

for ps in page_set:
    page_html = requests.get(ps, headers=headers)
    bsoup = BeautifulSoup(page_html.text, 'lxml')

    movie_div = bsoup.find_all('div', attrs={'class': 'hd'})

    for i in movie_div:
        print('-------------------')
        s = str(i)
        movie_href = re.findall(r'<a class="" href="(.*?)">', s, re.A)
        print(movie_href)
        movie_title = re.findall(r'class="title">(.*?)</span>', s, re.A)
        print(movie_title)

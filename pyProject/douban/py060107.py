import re

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}
response = requests.get('https://www.douban.com/group/topic/198233257/', headers=headers)
html = response.text
# print(html)

soup = BeautifulSoup(html, 'lxml')
comment_eles = soup.find('ul', attrs={'id': 'comments'})
# print(comment_eles)

mail = re.findall('\w+@\w+.\w+', comment_eles.text, re.A)
print(mail)

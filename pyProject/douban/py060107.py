import re
import requests
from bs4 import BeautifulSoup
from collections import OrderedDict

# 获取豆瓣话题评论中的邮箱（自己的尝试）
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}
response = requests.get('https://www.douban.com/group/topic/198233257/', headers=headers)
html = response.text
# print(html)

soup = BeautifulSoup(html, 'lxml')
comment_eles = soup.find('ul', attrs={'id': 'comments'})
# print(comment_eles)
# print(type(comment_eles))  # <class 'bs4.element.Tag'>

mail = re.findall(r'\w+@\w+.\w+', comment_eles.text, re.A)
# print(mail)
print(type(mail))  # <class 'list'>
mail_less = OrderedDict().fromkeys(mail).keys()
# print(mail_less)

for m in mail_less:
    print(m)

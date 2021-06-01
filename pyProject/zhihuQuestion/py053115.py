import re
import requests
from bs4 import BeautifulSoup
import lxml

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}
response = requests.get('https://www.zhihu.com/question/462390587', headers=headers)
html = response.text
# print(html)
# wenti
question = re.findall(r'<h1 class="QuestionHeader-title">(.*?)</h1>', html)
print(question)
# biaoqian
tags = re.findall(r'aria-owns="null-content">(.*?)</div></div></a>',html)
print(tags)
# wentiumiaoshu
desc = re.findall(r'<div class="QuestionRichText QuestionRichText--expandable QuestionRichText--collapsed"><div><span>(.*?)</span>',html)
print(desc)


desc = re.findall(r'<div class="QuestionRichText QuestionRichText--expandable QuestionRichText--collapsed"><div><span>(.*?)</span>',html)
print(desc)

soup=BeautifulSoup(html,'lxml')

answer=soup.find_all(attrs={'class':'List-item'})
print(answer)

# re.findall(r'',soup)

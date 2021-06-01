import json
import re
import requests
from bs4 import BeautifulSoup

response = requests.get('http://ncov.dxy.cn/ncovh5/view/pneumonia')
html = response.content.decode()
# print(html)

soup = BeautifulSoup(html, 'lxml')
script = soup.find(id='getListByCountryTypeService2true')
# print(script)

# print(script.string)
json_str = re.findall(r'\[.+\]', script.string)[0]
# print(json_str)
py_json=json.loads(json_str)

'''with open('resrc/ncov.json','w',encoding='utf8') as fp:
    json.dump(py_json,fp,ensure_ascii=False)'''


region = re.findall(r'"provinceName":"(\w*)"', json_str)
print(region)

currentConfirmedCount = re.findall(r'"currentConfirmedCount":(\w*)', json_str)
print(currentConfirmedCount)
'''
confirmedCount = re.findall(r'"confirmedCount":(\w*)', json_str)
print(confirmedCount)

confirmedCountRank = re.findall(r'"confirmedCountRank":(\w*)', json_str)
print(confirmedCountRank)

deadCount = re.findall(r'"deadCount":(\w*)', json_str)
print(deadCount)
'''
d=dict()
for r in region:
    for c in currentConfirmedCount:
        d[r]=c
print(d)
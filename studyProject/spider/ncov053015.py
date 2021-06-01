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

text = script.string
# print(text)
json_str = re.findall(r'\[.+\]', text)[0]
# print(json_str)
py_json = json.loads(json_str)

with open('resrc/ncov.json', 'w', encoding='utf8') as fp:
    json.dump(py_json, fp, ensure_ascii=False)

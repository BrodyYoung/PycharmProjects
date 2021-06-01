import re

import requests


response = requests.get('https://top.baidu.com/board?tab=homepage')
html = response.content.decode()
# print(html)

real_text=re.findall(r'<span class="c-single-text-ellipsis">(.*?)</span>',html)
# print(title)
title=re.findall(r'<span class="title_jDbBV c-theme-color">(.*?)</span>',html)
print(title)


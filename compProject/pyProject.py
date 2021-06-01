import re
import requests

url = 'https://book.qidian.com/info/1026816156#Catalog'
response = requests.get(url)

# 目标小说主页源码
html = response.text
# print(html)

# ul = re.findall(r'class="cf".*?</ul>', html, re.S)

# 获取每一章节的信息
ul = re.findall(r'class="cf".*?</ul>', html, re.S)[0]
# 获取章节信息列表
chapter_info_list = re.findall(r'<a href="(.*?)" title="(.*?)">', ul)
# 获取每一章节的标题
title = re.findall(r'title="(.*?)">', ul)
# print(title)
# print(ul)
print(chapter_info_list)
'''
ul = re.findall(r'class="cf".*?</ul>', html, re.S)[0]
# chapter_info_list = re.findall(r'<a href="(.*?)" title="(.*?)">', ul)
# title = re.findall(r'title="(.*?)">', ul)
title = re.findall(r'<ul class="cf"><a .*?>(.*?)</a></ul>', ul)
# title = re.findall(r'<ul class=".*">(.*?)</ul>', ul)
print(title)

'''



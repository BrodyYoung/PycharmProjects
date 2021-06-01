import re
import requests

# 成功版本

# url = 'https://book.qidian.com/info/1026816156#Catalog'        # 人世间
# url = 'https://book.qidian.com/info/1024644779#Catalog'         # 补天码农
url = 'https://book.qidian.com/info/1027713794#Catalog'         # 补天码农
response = requests.get(url)
# 目标小说主页源码
html = response.text
# print(html)
ul = re.findall(r'class="cf">(.*?)</ul>', html, re.S)[0]
# print(ul)
chapter_info_list = re.findall(r'<a href="(.*?)" ', ul)
# print(chapter_info_list)
title = re.findall(r'<a .*?>(.*?)</a>', ul)
# print(title)

# 新建一个文件，保存小说内容
# fb = open('resrc/renshijian.txt', 'w', encoding='utf-8')
fb = open('resrc/yishujia.txt', 'w', encoding='utf-8')
# 循环每个章节，分别去下载
for i in range(len(chapter_info_list)):
    # chapter_url, chapter_title = chapter_info
    chapter_url = 'https:' + chapter_info_list[i]
    # print(chapter_url)
    chapter_title = title[i]
    # print(chapter_title)

    # 下载章节内容
    chapter_response = requests.get(chapter_url)
    chapter_response.encoding = 'utf8'
    chapter_html = chapter_response.text
    # print(chapter_html)
    # 提取章节内容
    chapter_content = re.findall(r'<div class="read-content j_readContent" id="">(.*?)</div>', chapter_html, re.S)[0]
    # print(chapter_content)

    # 清洗数据
    chapter_content = chapter_content.replace('<p>', '')
    # print(chapter_content)

    # 数据持久化
    fb.write('\t\t\t')
    fb.write(chapter_title)
    fb.write('\n')
    fb.write(chapter_content)
    fb.write('\n')

fb.close()

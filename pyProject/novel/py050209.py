import requests
import re

# 原始代码

url = 'https://www.xz23.com/zhongfanshibasui/'
response = requests.get(url)
# 编码方式
response.encoding = 'gbk'
# 目标小说主页源码
html = response.text
print(html)
# 获取每一章节的信息
dl = re.findall(r'id="booklistBox".*?</dl>', html, re.S)[0]
# 获取章节信息列表
chapter_info_list = re.findall(r'<a href="(.*?)" title="(.*?)">', dl)
# 获取每一章节的标题
title = re.findall(r'title="(.*?)">', dl)[0]
# print(title)

# 新建一个文件，保存小说内容
fb = open('%s.txt' % title, 'w', encoding='utf-8')

# 循环每个章节，分别去下载
for chapter_info in chapter_info_list:
    # chapter_url, chapter_title = chapter_info
    chapter_url = chapter_info[0]
    chapter_title = chapter_info[1]
    # 下载章节内容
    chapter_response = requests.get(chapter_url)
    chapter_response.encoding = 'gbk'
    chapter_html = chapter_response.text
    # 提取章节内容
    chapter_content = re.findall(r'id="content">(.*?)</div>', chapter_html, re.S)[0]
    # 清洗数据
    chapter_content = chapter_content.replace('<br/><br/>', '')
    chapter_content = chapter_content.replace('<br />', '')
    chapter_content = chapter_content.replace('&nbsp;', '')
    # print(chapter_content)
    # 数据持久化
    fb.write(chapter_title)
    fb.write('\n')
    fb.write(chapter_content)
    fb.write('\n')
# print(title)

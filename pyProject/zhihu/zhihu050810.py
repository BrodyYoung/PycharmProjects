import requests
from lxml import etree
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}
r = requests.get('https://www.zhihu.com/question/21358581',headers=headers)
html=r.text
s = etree.HTML(html)
# 获取问题内容
q_content = s.xpath('//*[@class="QuestionHeader-title"]/text()')[0]
# 获取问题描述
q_describe = s.xpath('//*[@class="RichText ztext"]/text()')[0]
# 获取关注数和浏览量，这两个属性一样
q_number = s.xpath('//*[@class="NumberBoard-itemValue"]/text()')
concern_num = q_number[0]
browing_num = q_number[1]
# 打印
print('问题:',q_content,'\n','描述:',q_describe,'\n','关注数:',concern_num,'\n','浏览量:',browing_num)
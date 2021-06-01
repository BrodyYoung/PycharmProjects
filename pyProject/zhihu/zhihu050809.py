import requests
import xpath
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}
r=requests.get('https://www.zhihu.com/question/21358581', headers=headers)
html=r.text
print(html)

s=etree.HTML(html)
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}

response = requests.get('https://blog.csdn.net/rank/list', headers=headers)
html = response.text
# print(html)



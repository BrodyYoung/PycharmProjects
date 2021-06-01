import requests

response = requests.get('http://www.baidu.com')
response.encoding = 'utf8'
# print(response.text)

print(response.content.decode())

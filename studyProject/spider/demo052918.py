import re

r = re.findall('\d{2}', 'ttt12yt24')
print(r)        # 12   24
r = re.findall('a.c', 'abcta\nc')
print(r)        # abc
r = re.findall('a.c', 'abcta\nc', re.DOTALL)
print(r)        # abc    a\nc

r = re.findall('a(.+)d', 'abcde')
print(r)        # bc

r=re.findall('a\nb','a\nb')
print(r)

r=re.findall('a\\\\nb','a\\nb')
print(r)

r=re.findall(r'a\\nb','a\\nb')
print(r)



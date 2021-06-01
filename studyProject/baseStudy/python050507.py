# 字符串
a = 'Hello,world'
print(a.index('l'))  # 2
print(a.rindex('l'))  # 8
# print(a.index('p'))  # ValueError: substring not found
print(a.find('o'))  # 4
print(a.rfind('o'))  # 6
print(a.rfind('p'))  # -1
print('---------------------------------')
# 转为大写
print(a.upper())
# 转为小写
print(a.lower())
# 首字母大写
print(a.capitalize())
# 每个单词首字母都大写
print(a.title())
# 大小写相互转换
print(a.swapcase())
print('---------------------------------')
b = 'python'
print(b.center(10, '*'))

print(b.ljust(10, '*'))
print(b.rjust(10, '*'))
print('-23fgre'.rjust(10, '*'))
print(b.zfill(10))
c = '-567'
print(c.zfill(10))
d = '-*/-+%34'
print(d.zfill(10))
print('---------------------------------')
e = 'he llo wor ld,yes,py,th,on '
print(e.split())
print(e.split(' ', maxsplit=1))

print(e.split(','))
print(e.split(',', maxsplit=2))
print(e.rsplit(',', maxsplit=2))
print('---------------------------------')
s = 'hello,Python,Python,Python'
print(s.replace('Python', 'Java'))
print(s.replace('Python', 'Java', 2))
lst = ['abc', 'xyz', 'opq']
print('|'.join(lst))
t = ('Hel', 'low', 'or', 'ld')
print('*'.join(t))
p = 'Hello'
print('/'.join(p))
print('---------------------------------')
a = 'abcdddd'
b = 'abcdefg'
c = 'abc'
print(a > b)
print(a > c)
print(ord('d'), ord('e'))
print(chr(100), chr(101))
print('---------------------------------')
s = 'hello,world'
print(s[:5])  # hello
print(s[2:4])  # ll
print(s[6:])  # world
print(s[0::2])  # hlowrd
print(s[::-1])  # dlrow,olleh
print('---------------------------------')
s = '电脑'
g = s.encode(encoding='GBK')
print(g)
u = s.encode(encoding='UTF-8')
print(u)
print(g.decode(encoding='GBK'))
print(u.decode(encoding='UTF-8'))

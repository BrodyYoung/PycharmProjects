# 格式化符号

name = 'yang'
age = 23
weight = 61.5
id = 17

print('我的名字是%s，我今年%d岁了，我体重是%.2f公斤，我的学号是%06d' % (name, age, weight, id))
print(f'我的名字是{name}，我今年{age}岁了，我体重是{weight}公斤，我的学号是{id}')

print('yang' + 'yun', 'bo' * 3)

s = 'mynameisyangyunbo'
s1 = 'yangyunbo'
# 字符串截取
print(s[3:6])  # ame
print(s[-5:-2])  # yun

print(s[2:-4])
print(s)

# 元组 ：可重复
t1, t2 = (3, 8, 1, 9), (0, 6, 5, 1, 9)
print(t1 + t2)

a = 'panalama'
b = 'babeiben'
c = 'cecancui'
abc = a + \
      b + \
      c
print(abc)

#dict类型

dc={}
dc['one']='dictByOne'
dc['two']='dictByTwo'
dc['two']='DICTByTwo'
dc['three']='dictByThree'
print(dc)   # 输出完整字典
print(dc['two'])  #输出dc字典中key=two的value
print(dc.keys())
print(dc.values())


#数据类型转换

x='528'
y=int(x)
print(y)
print(type(y))

p=523
q=str(p)
print(q)
print(type(q))
















# 创建字典
a = dict(name='yang', age=23, gender='男', id='20170001')
print(a, type(a))

b = {'name': 'zhang', 'age': 21}
print(b, type(b))

c = {}
print(c)
print('---------------------------------------')
# 获取操作
print(a.get('name'))  # yang
print(a.get('pwd'))  # None
print(a.get('pwd', 99))  # 99
print(a['age'])  # 23
# print(a['pwd'])  # KeyError: 'pwd'

print('------------------------------------------')
d = {'张三': 94, '李四': 97, '王五': 69}
# 判断元素
print('李四' in d)
print('赵六' not in d)
d['赵六'] = 74
print(d)
d['张三'] = 90
print(d)
del d['王五']
print(d)
d.clear()
print(d)
print('------------------------------------------')
e = {'张三': 94, '李四': 97, '王五': 69}
keys = e.keys()
print(keys, type(keys))
values = e.values()
print(values, type(values))
items = e.items()
print(items, type(items))
print('------------------------------------------')
for i in e:
    print(i, e[i])
print('------------------------------------------')
fruits = ['apple', 'banana', 'orange']
prices = [12, 25, 10]
f = {fruits.upper(): prices for fruits, prices in zip(fruits, prices)}
print(f)
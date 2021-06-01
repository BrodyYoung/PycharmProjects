# 元组
# 创建元组
a = ('a', ['v', 'g', 'd'], 't')
print(a, type(a))
b = ('b',)
print(b, type(b))
c = tuple(('a', 'ty', 'po'))
print(c, type(c))
d = tuple(('a',))
print(d, type(d))
print('------------------------------')
a[1].append('c')
print(a)
print('------------------------------')
for i in c:
    print(i)
print('------------------------------')
# 集合
# 创建集合
a = {15, 467, 6.8, 's'}
print(a)
b = set(range(4))
print(b)
c = set([1, 7, '42d'])
print(c)
d = set(('a', 'b', 'c'))
print(d)
e = set()
print(e)
f = set('HelloWorld')
print(f)
# 添加元素
a.add('tring')
print(a)
a.update({'a', 'b', 'c'})
print(a)  # {'a', 's', 6.8, 'b', 'tring', 15, 467, 'c'}
# 判断操作
print('s' in a)
print('c' not in a)
# 删除操作
a.remove('a')
print(a)
# a.remove('a')
a.discard(15)
print(a)
a.discard(15)
print(a)
a.pop()
print(a)
a.clear()
print(a)
print('------------------------------')
# 集合生成式
s = {i * i for i in range(6)}
print(s)
print('------------------------------')
# 集合之间的关系
s1 = {1, 2, 3, 4, 5, 6}
s2 = {1, 2, 3, 4}
s3 = {1, 2, 3, 4}
s4 = {1, 2, 30, 40}
print(s1 == s2)  # false
print(s2 != s3)  # false

print(s1.issuperset(s2))  # true

print(s2.issubset(s1))  # true
print(s2.issubset(s3))  # true

print(s2.isdisjoint(s4))  # false
print('------------------------------')
t1 = {1, 2, 3, 4, 5}
t2 = {3, 4, 5, 6, 7}
# 求交集
print(t1.intersection(t2))  # {3，4，5}
print(t1 & t2)
# 求并集
print(t1.union(t2))  # {1，2，3，4，5，6，7}
print(t1 | t2)
# 求差集
print(t1.difference(t2))  # {1，2}
print(t1 - t2)
# 求对称差集
print(t1.symmetric_difference(t2))  # {1,2,6,7}
print(t1 ^ t2)

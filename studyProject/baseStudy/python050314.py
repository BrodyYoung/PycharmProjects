# 列表
a = ['a', 'b', 10, 5.7, True, 'a', 'b', 'c', 'd']
b = list(['a', 'b', 'c', 'd', 'b'])
print(a.index('b'))
print(b.index('b', 2, 6))
print(a[-2])
print(a[2])
print('---------------------------------')
print(a[::])  # ['a', 'b', 10, 5.7, True, 'a', 'b', 'c', 'd']
print(a[:8:3])  # ['a', 5.7, 'b']
print(a[2::2])  # [10, True, 'b', 'd']
print(a[3:7:])  # [5.7, True, 'a', 'b']
print(a[1:7:2])  # ['b', 5.7, 'a']

print(a[::-1])  # ['d', 'c', 'b', 'a', True, 5.7, 10, 'b', 'a']
print(a[7:3:-1])  # ['c', 'b', 'a', True]
print('---------------------------------')
print('d' in a)
print('f' in a)
print('d' not in a)
print('f' not in a)
print('---------------------------------')
for i in a:
    print(i)

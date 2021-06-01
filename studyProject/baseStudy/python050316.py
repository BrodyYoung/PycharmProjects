# 列表添加操作
ls = ['a', 'b', 'c']
ll = ['e', 'f']
lt = ['x', 'y', 'z']
print("原列表是：", ls)
ls.append('d')
ls.append(ll)
ls.extend(ll)
ls.insert(1, 'o')
ls[2:] = lt
print(ls)
print('---------------------------')
# 删除列表操作
q = ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c']
q.remove('c')
print(q)  # ['a', 'b', 'd', 'e', 'a', 'b', 'c']
q.pop(1)
print(q)  # ['a', 'd', 'e', 'a', 'b', 'c']
q.pop()
print(q)  # ['a', 'd', 'e', 'a', 'b']
newls = q[1:4]
print(newls)  # ['d', 'e', 'a']
print(q)  # ['a', 'd', 'e', 'a', 'b']
q[1:4] = []
print(q)  # ['a', 'b']
q.clear()  # []
print(q)
# del q
# print(q)  # NameError: name 'q' is not defined
print('---------------------------------')
a = [1, 2, 3, 4, 5]
a[2] = 30
print(a)

a[1:3] = ['a', 'b', 'c', 'd']
print(a)

print('---------------------------------')
# 对列表排序
x = [25, 19, 42, 61]
new = sorted(x)
print(new)  # [19,25,42,61]
print(x)  # [25, 19, 42, 61]
x.sort()
print(x)  # [19,25,42,61]
x.sort(reverse=False)  # 升序排列 ，默认
print(x)  # [19,25,42,61]
x.sort(reverse=True)  # 降序排列
print(x)  # [61,42,25,19]
print('---------------------------------')
# 列表生成式
lst = [2 * i for i in range(1, 6)]
print(lst)

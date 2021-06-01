# 循环结构
a = range(10)
print(list(a))

b = range(2, 10)
print(list(b))

c = range(2, 10, 2)
print(list(c))

a = 0
sum = 0
while a <= 4:
    sum = sum + a
    a += 1
print(sum)

d = 0
sum = 0
while d % 2 == 0 and d <= 100:
    sum += d
    d += 2
print(sum)

print('-----------------------------')
for i in range(11):
    print(i)

for t in 'Hello World':
    print(t)

for _ in range(5):
    print('循环结构')

print('----------------')
# 用for-in 计算1到100之间的偶数和
su = 0
for a in range(0, 101, 2):
    su += a
print(su)

print('---------------')
for r in range(100, 1000):
    ge = r % 10
    shi = r // 10 % 10
    bai = r // 100
    # print(bai, shi, ge)
    if bai ** 3 + shi ** 3 + ge ** 3 == r:
        print(r)

print('---------------')
for i in range(3):
    pwd = input('请输入密码')
    if pwd == '8888':
        print('密码正确')
        break
    else:
        print('密码错误')
print('---------------')
i = 0
while i < 3:
    pwd = input('请输入密码')
    if pwd == '8888':
        print('密码正确')
        break
    else:
        print('密码错误')
    i += 1
print('---------------')
for r in range(1, 51):
    if r % 5 == 0:
        print(r)
        continue
for r in range(1, 51):
    if r % 5 != 0:
        continue
    print(r)

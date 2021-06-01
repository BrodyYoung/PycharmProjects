# a = input('请输入第一个数')
# b = input('请输入第二个数')
#
# c = int(a) + int(b)
# print(c)

x = y = z = 10
print(x, id(x))
print(y, id(y))
print(z, id(z))

m = 10
n = 10
print(m == n)
print(m is n)

s = 'nihao'
t = 'nihao'
print(s == t)
print(s is t)

p = {10, 20, 30}
q = {10, 20, 30}
print(p == q)
print(p is q)
print("----------------------逻辑运算符-----------------------")
u = 10
v = 20
print(u == 10 and v == 20)  # true
print(u == 0 and v == 20)  # false
print(u == 0 or v == 20)  # true
print(not v == 20)  # false

print('-----------------------位运算符-----------------------')
print(4 & 8)
print(4 | 8)

print(4 <<1)
print(4>> 2)